#!/usr/bin/env python3
from pathlib import Path
import re, sys
p=Path(__file__).resolve().parents[1]/'index.html'
s=p.read_text(encoding='utf-8')
checks={
'pilot_version':'v1.1.1-rc1' in s,
'seven_chambers':len(re.findall(r'class="chamber(?: open)?" data-step="[1-7]"',s))==7,
'completion_button':'id="completeBtn"' in s,
'local_consent':'Local-only consent:' in s,
'privacy_warning':'Local data privacy:' in s,
'ascii_export':'const exportStem=' in s,
'required_fields':"['arrival','Record one present-moment observation.']" in s and "['lesson','Record the lesson retained.']" in s,
'no_fetch':'fetch(' not in s,
'no_xhr':'XMLHttpRequest' not in s,
'no_websocket':'WebSocket' not in s,
'no_external_script':not re.search(r'<script[^>]+src=',s,re.I),
'no_external_stylesheet':not re.search(r"<link[^>]+rel=['\"]stylesheet['\"]",s,re.I),
}
failed=[k for k,v in checks.items() if not v]
for k,v in checks.items(): print(('PASS' if v else 'FAIL'),k)
if failed: sys.exit(1)
