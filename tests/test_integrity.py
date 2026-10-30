#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, sys
root=Path(__file__).resolve().parents[1]

def digest(p):
    h=hashlib.sha256();
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()

fail=[]
entries={}
for line in (root/'SHA256SUMS.txt').read_text().splitlines():
    if not line.strip(): continue
    h,path=line.split('  ',1); entries[path]=h
    p=root/path
    if not p.exists(): fail.append(f'missing {path}'); continue
    got=digest(p)
    if got!=h: fail.append(f'hash mismatch {path}: {got} != {h}')
manifest=json.loads((root/'MANIFEST.json').read_text())
for item in manifest['files']:
    path=item['path']; expected=item['sha256']
    if entries.get(path)!=expected: fail.append(f'manifest/sums mismatch {path}')
current=digest(root/'index.html')
release=digest(root/'releases/AEON_TEMPUS_ECLIPSE_NODE_THETA7_v1.1.2-rc1.html')
if current!=release: fail.append('index/release bytes differ')
release_line=(root/'RELEASE_SHA256SUMS.txt').read_text().strip().split('  ',1)
if release_line != [release,'AEON_TEMPUS_ECLIPSE_NODE_THETA7_v1.1.2-rc1.html']:
    fail.append('release checksum does not name/match downloadable HTML')
if fail:
    print('\n'.join('FAIL '+x for x in fail)); sys.exit(1)
print(f'PASS verified {len(entries)} repository digests')
print('PASS manifest agrees with SHA256SUMS')
print('PASS current index equals versioned release candidate')
print('PASS release checksum names the downloadable HTML asset')
