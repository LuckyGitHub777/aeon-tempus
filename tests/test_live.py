from playwright.sync_api import sync_playwright
from urllib.parse import urlparse
import json, os, shutil, tempfile
from pathlib import Path

site=os.environ['SITE_URL'].rstrip('/')+'/'
origin=urlparse(site).netloc
errors=[]; external=[]; bad_responses=[]; dialogs=[]
with sync_playwright() as p:
    exe=os.getenv('THETA7_BROWSER_PATH') or next((shutil.which(x) for x in ('google-chrome','google-chrome-stable','chromium','chromium-browser') if shutil.which(x)),None)
    if not exe: raise RuntimeError('No Chromium/Chrome found')
    browser=p.chromium.launch(headless=True,executable_path=exe,args=['--no-sandbox'])
    page=browser.new_page(accept_downloads=True,viewport={'width':1440,'height':1000})
    page.set_default_timeout(10000)
    page.on('pageerror',lambda e: errors.append(str(e)))
    page.on('console',lambda m: errors.append(m.text) if m.type=='error' else None)
    def request_watch(r):
        u=urlparse(r.url)
        if u.scheme in ('http','https') and u.netloc and u.netloc!=origin:
            external.append(r.url)
    page.on('request',request_watch)
    page.on('response',lambda r: bad_responses.append({'status':r.status,'url':r.url}) if r.status>=400 else None)

    page.goto(site,wait_until='load')
    assert page.evaluate("location.protocol")=='https:'
    assert page.locator('body').inner_text().find('ECLIPSE NODE')>=0
    assert page.locator('body').inner_text().find('v1.1.4-rc1')>=0
    privacy=page.locator('#privacyTop').inner_text()
    assert 'on this website and in a downloaded copy' in privacy

    # Shared github.io origin: entries stay in the tab and never reach localStorage.
    def accept_all(d): dialogs.append(d.type); d.accept()
    page.on('dialog',accept_all)
    page.locator('#arrival').fill('Hosted session-only check')
    page.wait_for_timeout(900)
    assert page.locator('#saveState').inner_text()=='Not saved — export to keep'
    assert page.evaluate("Object.keys(localStorage).filter(k=>k.startsWith('aeon-tempus')).length")==0
    page.reload(wait_until='load')
    assert dialogs.count('beforeunload')>=1
    assert page.locator('#arrival').input_value()==''
    page.remove_listener('dialog',accept_all)

    # Custom text must not be silently overwritten by a sample.
    page.click('article.chamber[data-step="2"] .chamber-head')
    page.locator('#obscuration').fill('My hosted custom text')
    page.select_option('#scenarioSelect','conflict')
    seen=[]
    def dismiss(d): seen.append(d.message); d.dismiss()
    page.once('dialog',dismiss)
    page.click('#loadScenarioBtn')
    assert seen==['Replace your text with the sample scenario?']
    assert page.locator('#obscuration').input_value()=='My hosted custom text'

    # Validation semantics must be visible and programmatic.
    page.locator('#arrival').fill('')
    page.click('#completeBtn')
    page.wait_for_function("document.activeElement && document.activeElement.id === 'arrival'")
    described=page.locator('#arrival').get_attribute('aria-describedby')
    assert page.locator('#arrival').get_attribute('aria-invalid')=='true'
    assert described and page.locator('#'+described).count()==1
    page.locator('#arrival').fill('Corrected hosted observation')
    assert page.locator('#arrival').get_attribute('aria-invalid') is None
    assert page.locator('#arrival').get_attribute('aria-describedby') is None

    # Complete the minimum valid sequence and prove export works from the hosted site.
    vals={
      'arrival':'Corrected hosted observation',
      'obscuration':'Some information remains incomplete.',
      'observed':'Two observations are directly available.',
      'unresolved':'The final interpretation remains unresolved.',
      'selected_action':'Check the strongest primary evidence before acting.',
      'lesson':'Preserve uncertainty while taking a reversible next step.'
    }
    page.evaluate("""vals=>{for(const [id,v] of Object.entries(vals)){const e=document.getElementById(id);e.value=v;e.dispatchEvent(new Event('input',{bubbles:true}))}
      const g=document.getElementById('grounding');g.value='Movement or walk';g.dispatchEvent(new Event('input',{bubbles:true}));
      document.querySelectorAll('.step-check,.condition').forEach(e=>{e.checked=true;e.dispatchEvent(new Event('change',{bubbles:true}))})
    }""",vals)
    page.click('#completeBtn')
    assert page.locator('#completion').evaluate("e=>e.classList.contains('show')")
    with page.expect_download() as dl:
        page.click('#exportBtn')
    out=Path(tempfile.mkdtemp())/dl.value.suggested_filename
    dl.value.save_as(str(out))
    data=json.loads(out.read_text())
    assert data['meta']['version']=='1.1.4-rc1'
    assert data['fields']['selected_action']=='Check the strongest primary evidence before acting.'

    # Mobile hosted UX: completion affordance available and no horizontal overflow.
    page.set_viewport_size({'width':375,'height':812})
    assert page.locator('#mobileCompleteBtn').is_visible()
    overflow=page.evaluate("document.documentElement.scrollWidth-document.documentElement.clientWidth")
    assert overflow<=1

    assert external==[], external
    assert bad_responses==[], bad_responses
    assert errors==[], errors
    page.evaluate("localStorage.clear(); sessionStorage.clear()")
    print(json.dumps({
      'site_url':site,
      'mode':'hosted-https',
      'session_only':True,
      'scenario_protection':True,
      'error_semantics':True,
      'completion':True,
      'export_json':True,
      'mobile_complete':True,
      'mobile_overflow_px':overflow,
      'external_requests':external,
      'bad_responses':bad_responses,
      'errors':errors
    },indent=2))
    browser.close()
