from playwright.sync_api import sync_playwright
from pathlib import Path
import json, os, shutil, tempfile
root=Path(__file__).resolve().parents[1]; html=root/'index.html'; src=html.read_text()
errors=[]; requests=[]
with sync_playwright() as p:
    exe=os.getenv('THETA7_BROWSER_PATH') or next((shutil.which(x) for x in ('google-chrome','google-chrome-stable','chromium','chromium-browser') if shutil.which(x)),None)
    if not exe: raise RuntimeError('No Chromium/Chrome found')
    b=p.chromium.launch(headless=True,executable_path=exe,args=['--no-sandbox']); page=b.new_page(viewport={'width':1440,'height':1000},accept_downloads=True)
    page.set_default_timeout(5000); page.emulate_media(reduced_motion='reduce')
    page.on('console',lambda m: errors.append(m.text) if m.type=='error' else None); page.on('pageerror',lambda e: errors.append(str(e)))
    page.on('request',lambda r: requests.append(r.url) if not r.url.startswith(('file://','data:','blob:','about:')) else None)
    simulated=False
    if os.getenv('THETA7_SIMULATE_FILE_MODE')=='1': simulated=True
    else:
        try: page.goto(html.as_uri(),wait_until='load')
        except Exception as e:
            if 'ERR_BLOCKED_BY_ADMINISTRATOR' not in str(e): raise
            simulated=True
    if simulated:
        page.goto('about:blank'); page.set_content(src.replace("const FILE_MODE=location.protocol==='file:';","const FILE_MODE=true;",1),wait_until='load')
    assert 'Session only' in page.locator('#saveState').inner_text(); assert page.locator('#privacyTop').count()==1
    page.select_option('#scenarioSelect','decision'); page.click('#loadScenarioBtn'); a=page.locator('#trigger').input_value()
    page.select_option('#scenarioSelect','conflict'); page.click('#loadScenarioBtn'); assert page.locator('#trigger').input_value()!=a
    assert page.locator('#clarityDelta').inner_text()=='Not measured'
    page.click('#completeBtn'); assert page.evaluate('document.activeElement.id')=='arrival'; assert page.locator('#arrival').evaluate('e=>e.classList.contains("error")')
    vals={'arrival':'At a desk.','obscuration':'Source reliability unknown.','observed':'Two accounts disagree.','unresolved':'Reliability remains unresolved.','selected_action':'Compare against primary record.','lesson':'Keep uncertainty visible.'}
    page.evaluate("v=>{for(const [id,x] of Object.entries(v)){let e=document.getElementById(id);e.value=x;e.dispatchEvent(new Event('input',{bubbles:true}))}}",vals)
    page.evaluate("()=>{let e=document.getElementById('grounding');e.value='Movement or walk';e.dispatchEvent(new Event('input',{bubbles:true}));document.querySelectorAll('.step-check,.condition').forEach(x=>{x.checked=true;x.dispatchEvent(new Event('change',{bubbles:true}))})}")
    page.locator('#selected_action').fill('Check primary source before any public claim.')
    page.click('#completeBtn'); assert page.locator('#completion').evaluate('e=>e.classList.contains("show")'); assert page.locator('#completionDelta').inner_text()=='Not measured'
    with page.expect_download() as d: page.click('#exportMdBtn')
    out=Path(tempfile.mkdtemp())/d.value.suggested_filename; d.value.save_as(str(out)); md=out.read_text()
    for x in ('## Chamber I — Arrival','## Chamber II — Obscuration','**Lesson retained:**','**Grounded return activity:**','Check primary source before any public claim.','Clarity change: Not measured'): assert x in md
    page.locator('#clarityBefore').evaluate("e=>{e.value='2';e.dispatchEvent(new Event('input',{bubbles:true}))}"); page.locator('#clarityAfter').evaluate("e=>{e.value='4';e.dispatchEvent(new Event('input',{bubbles:true}))}")
    assert page.locator('#clarityDelta').inner_text()=='+2'
    page.emulate_media(media='print'); assert page.locator('h1').evaluate("e=>getComputedStyle(e).webkitTextFillColor")!='transparent'; page.emulate_media(media='screen')
    r=page.locator('article.chamber[data-step="1"] .chamber-head').evaluate("e=>{let a=e.querySelector('.state').getBoundingClientRect(),c=e.querySelector('.chev').getBoundingClientRect();return Math.abs((a.y+a.height/2)-(c.y+c.height/2))}"); assert r<8
    page.set_viewport_size({'width':375,'height':812}); assert page.locator('#mobileCompleteBtn').is_visible(); overflow=page.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth'); assert overflow<=1
    assert requests==[] and errors==[]
    print(json.dumps({'file_mode':'simulated' if simulated else 'direct','completion':True,'export':True,'clarity':True,'mobile_overflow_px':overflow,'requests':requests,'errors':errors},indent=2)); b.close()
