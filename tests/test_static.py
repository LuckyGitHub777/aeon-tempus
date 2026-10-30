#!/usr/bin/env python3
from pathlib import Path
import re, sys
p=Path(__file__).resolve().parents[1]/'index.html'
s=p.read_text(encoding='utf-8')
checks={
'pilot_version':'v1.1.2-rc1' in s,
'seven_chambers':len(re.findall(r'class="chamber(?: open)?" data-step="[1-7]"',s))==7,
'completion_button':'id="completeBtn"' in s and 'id="mobileCompleteBtn"' in s,
'privacy_before_entry':'id="privacyTop"' in s and 'session memory only' in s,
'file_mode_session_only':"const FILE_MODE=location.protocol==='file:'" in s and 'session-memory-file-privacy' in s,
'clarity_requires_rating':'clarityBeforeRated' in s and 'clarityAfterRated' in s and "delta===null?'Not measured'" in s,
'complete_summary':'## Chamber I — Arrival' in s and '**Lesson retained:**' in s and '**Grounded return activity:**' in s,
'scenario_replaces':"$('#trigger').value=item.trigger" in s and "$('#obscuration').value=item.obscuration" in s,
'error_reveal':'function revealError(el)' in s,
'desktop_chevron_grid':'grid-template-columns:64px 1fr auto 28px' in s,
'print_title':'-webkit-text-fill-color:#111!important' in s,
'webp_embedded':'data:image/webp;base64,' in s and 'data:image/png;base64,' not in s,
'compact_size':p.stat().st_size < 1_000_000,
'no_fetch':'fetch(' not in s,
'no_xhr':'XMLHttpRequest' not in s,
'no_websocket':'WebSocket' not in s,
'no_external_script':not re.search(r'<script[^>]+src=',s,re.I),
'no_external_stylesheet':not re.search(r'<link[^>]+rel=.stylesheet.',s,re.I),
}
failed=[k for k,v in checks.items() if not v]
for k,v in checks.items(): print(('PASS' if v else 'FAIL'),k)
if failed: sys.exit(1)
