from playwright.sync_api import sync_playwright
from pathlib import Path
import json, os, shutil, tempfile
root=Path(__file__).resolve().parents[1]; html=root/'index.html'; src=html.read_text(encoding='utf-8')
errors=[]; requests=[]; dialogs=[]
with sync_playwright() as p:
    exe=os.getenv('THETA7_BROWSER_PATH') or next((shutil.which(x) for x in ('google-chrome','google-chrome-stable','chromium','chromium-browser') if shutil.which(x)),None)
    if not exe: raise RuntimeError('No Chromium/Chrome found')
    b=p.chromium.launch(headless=True,executable_path=exe,args=['--no-sandbox'])
    page=b.new_page(accept_downloads=True,viewport={'width':1280,'height':900}); page.set_default_timeout(8000)
    page.on('pageerror',lambda e:errors.append(str(e))); page.on('console',lambda m:errors.append(m.text) if m.type=='error' else None)
    page.on('request',lambda r:requests.append(r.url) if not r.url.startswith(('file://','data:','blob:')) else None)
    legacy='aeon-tempus-theta7-v1-1-1-rc1'
    page.add_init_script("""try{if(!sessionStorage.getItem('__theta_seeded')){localStorage.setItem('aeon-tempus-theta7-v1-1-1-rc1',JSON.stringify({meta:{version:'1.1.1-rc1'},fields:{arrival:'legacy secret'}}));sessionStorage.setItem('__theta_seeded','1')}}catch(e){}""")
    page.goto(html.as_uri(),wait_until='load')
    assert page.evaluate("location.protocol")=='file:'
    assert page.evaluate(f"localStorage.getItem('{legacy}')") is None
    assert page.locator('#arrival').input_value()==''
    page.wait_for_function("document.querySelector('#toast').textContent.includes('Removed data saved by an earlier version')")
    def accept_dialog(d): dialogs.append(d.type); d.accept()
    page.on('dialog',accept_dialog)
    page.locator('#arrival').fill('dirty local work')
    assert page.locator('#saveState').inner_text()=='Not saved — export to keep'
    page.reload(wait_until='load')
    assert 'beforeunload' in dialogs
    page.locator('#arrival').fill('exported local work')
    with page.expect_download() as dl: page.click('#exportBtn')
    tmp=Path(tempfile.mkdtemp())/dl.value.suggested_filename; dl.value.save_as(str(tmp))
    before=len(dialogs); page.reload(wait_until='load'); assert len(dialogs)==before
    page.remove_listener('dialog',accept_dialog)
    page.click('article.chamber[data-step="2"] .chamber-head'); page.locator('#obscuration').fill('my custom text'); page.select_option('#scenarioSelect','conflict')
    seen=[]
    def dismiss_confirm(d): seen.append(d.message); d.dismiss()
    page.once('dialog',dismiss_confirm); page.click('#loadScenarioBtn')
    assert seen==['Replace your text with the sample scenario?']
    assert page.locator('#obscuration').input_value()=='my custom text'
    page.click('#completeBtn'); page.wait_for_function("document.activeElement && document.activeElement.id === 'arrival'")
    described=page.locator('#arrival').get_attribute('aria-describedby')
    assert page.locator('#arrival').get_attribute('aria-invalid')=='true'
    assert described and page.locator('#'+described).count()==1
    page.locator('#arrival').fill('corrected')
    assert page.locator('#arrival').get_attribute('aria-invalid') is None
    assert page.locator('#arrival').get_attribute('aria-describedby') is None
    # Shared *.github.io origin: session-only, with recovery of earlier hosted autosave.
    shared_url='https://theta7-check.github.io/aeon-tempus/'
    ctx=b.new_context(accept_downloads=True,viewport={'width':1280,'height':900})
    ctx.route('https://theta7-check.github.io/**',lambda route: route.fulfill(status=200,content_type='text/html; charset=utf-8',body=src) if route.request.url.rstrip('/').endswith('/aeon-tempus') else route.fulfill(status=404,body=''))
    sp=ctx.new_page(); sp.set_default_timeout(8000); shared_dialogs=[]
    sp.on('pageerror',lambda e:errors.append(str(e)))
    sp.on('dialog',lambda d:(shared_dialogs.append(d.type),d.accept()))
    sp.goto(shared_url,wait_until='load')
    assert sp.evaluate("location.hostname").endswith('.github.io')
    assert 'shared-site privacy' in sp.locator('#saveState').inner_text()
    assert 'on this website and in a downloaded copy' in sp.locator('#privacyTop').inner_text()
    sp.evaluate("localStorage.setItem('aeon-tempus-theta7-v1-1-3-rc1',JSON.stringify({meta:{version:'1.1.3-rc1'},fields:{arrival:'earlier hosted entry'}}))")
    sp.reload(wait_until='load')
    assert sp.locator('#arrival').input_value()=='earlier hosted entry'
    assert sp.evaluate("localStorage.getItem('aeon-tempus-theta7-v1-1-3-rc1')") is None
    assert sp.locator('#saveState').inner_text()=='Not saved — export to keep'
    sp.locator('#arrival').fill('shared-site entry'); sp.wait_for_timeout(900)
    assert sp.evaluate("Object.keys(localStorage).filter(k=>k.startsWith('aeon-tempus')).length")==0
    sp.reload(wait_until='load')
    assert shared_dialogs.count('beforeunload')>=1
    assert sp.locator('#mobileCompleteBtn').get_attribute('aria-label').startswith('Review & Complete')
    ctx.close()
    assert requests==[] and errors==[]
    print(json.dumps({'file_mode':'direct','legacy_cleanup':True,'beforeunload':True,'export_clears_dirty':True,'scenario_confirm':True,'error_semantics':True,'shared_origin_session_only':True,'shared_origin_recovery':True,'requests':requests,'errors':errors},indent=2))
    b.close()
