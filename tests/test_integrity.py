#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, sys
root=Path(__file__).resolve().parents[1]
def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()
fail=[]; entries={}
for line in (root/'SHA256SUMS.txt').read_text().splitlines():
    if not line.strip(): continue
    h,path=line.split('  ',1); entries[path]=h; p=root/path
    if not p.exists(): fail.append(f'missing {path}'); continue
    if digest(p)!=h: fail.append(f'hash mismatch {path}')
manifest=json.loads((root/'MANIFEST.json').read_text())
for item in manifest['files']:
    if entries.get(item['path'])!=item['sha256']: fail.append(f"manifest/sums mismatch {item['path']}")
current=digest(root/'index.html')
release=root/'releases/AEON_TEMPUS_ECLIPSE_NODE_THETA7_v1.1.4-rc1.html'
if current!=digest(release): fail.append('index/release bytes differ')
old=root/'releases/AEON_TEMPUS_ECLIPSE_NODE_THETA7_v1.1.2-rc1.html'
if digest(old)!='09c17e62b84726282e5332f5bd4daf6ed14020b3aa7a5587f158448e6bb9f50a': fail.append('v1.1.2-rc1 history changed')
rc3=root/'releases/AEON_TEMPUS_ECLIPSE_NODE_THETA7_v1.1.3-rc1.html'
if digest(rc3)!='b730b20d11b915e46a469c99f88af31063ed53018fd8ece156a0fe303c909130': fail.append('v1.1.3-rc1 history changed')
release_line=(root/'RELEASE_SHA256SUMS.txt').read_text().strip().split('  ',1)
if release_line != [current,'AEON_TEMPUS_ECLIPSE_NODE_THETA7_v1.1.4-rc1.html']: fail.append('release checksum contract mismatch')
if fail:
    print('\n'.join('FAIL '+x for x in fail)); sys.exit(1)
print(f'PASS verified {len(entries)} repository digests')
print('PASS manifest agrees with SHA256SUMS')
print('PASS current index equals v1.1.4-rc1 release candidate')
print('PASS v1.1.2-rc1 and v1.1.3-rc1 remain immutable')
print('PASS release checksum names current downloadable HTML')
