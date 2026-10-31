#!/usr/bin/env python3
from pathlib import Path
import re, sys
p=Path(__file__).resolve().parents[1]/'index.html'
s=p.read_text(encoding='utf-8')
checks={
'pilot_version':'v1.1.4-rc1' in s,
'shared_origin_session_only':"const SESSION_ONLY=FILE_MODE||SHARED_ORIGIN" in s and 'github\\.io' in s,
'shared_origin_recovery':'recoveredOnLoad' in s,
'seven_chambers':len(re.findall(r'class="chamber(?: open)?" data-step="[1-7]"',s))==7,
'file_mode':"const FILE_MODE=location.protocol==='file:'" in s,
'unload_guard':"beforeunload" in s and 'Not saved — export to keep' in s,
'legacy_cleanup':'clearRealLocalKeys(LEGACY_STORAGES)' in s and 'v1-1-3-rc1' in s,
'scenario_confirm':"Replace your text with the sample scenario?" in s,
'error_semantics':"aria-invalid" in s and "aria-describedby" in s and "clearFieldError" in s,
'export_clears_dirty':s.count('markExported()')>=2,
'no_fetch':'fetch(' not in s,
'no_xhr':'XMLHttpRequest' not in s,
'no_websocket':'WebSocket' not in s,
'no_external_script':not re.search(r'<script[^>]+src=',s,re.I),
'no_external_stylesheet':not re.search(r'<link[^>]+rel=.stylesheet.',s,re.I),
}
failed=[k for k,v in checks.items() if not v]
for k,v in checks.items(): print(('PASS' if v else 'FAIL'),k)
if failed: sys.exit(1)
