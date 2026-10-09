#!/usr/bin/env python3
"""Structural and integrity validator for JA21_DMLM_Suite_1.0.0."""
from __future__ import annotations
import csv, gzip, hashlib, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
def sha(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for c in iter(lambda:f.read(1024*1024),b''): h.update(c)
    return h.hexdigest()
def fail(msg): print('FAIL:',msg); raise SystemExit(1)
def main():
    corpus=ROOT/'corpus'/'technical'/'deepml_motion_animation_technical_corpus_10000.jsonl.gz'
    with gzip.open(corpus,'rt',encoding='utf-8') as f: records=[json.loads(x) for x in f]
    if len(records)!=10000: fail(f'corpus count {len(records)}')
    if len({r['identity']['id'] for r in records})!=10000: fail('duplicate IDs')
    if sorted(r['identity']['sequence'] for r in records)!=list(range(1,10001)): fail('sequence discontinuity')
    for r in records:
        observed=hashlib.sha256(r['source']['program'].encode()).hexdigest()
        if observed!=r['source']['source_hash'].replace('sha256:',''): fail(f'source hash {r["identity"]["id"]}')
    scripts=sorted((ROOT/'script_pack_1000').rglob('*.deepml'))
    if len(scripts)!=1000: fail(f'script count {len(scripts)}')
    with (ROOT/'catalogs'/'SCRIPT_CATALOG.csv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
    if len(rows)!=1000: fail(f'catalog count {len(rows)}')
    bypath={r['path']:r for r in rows}
    classes=set(); tiers=set(); topics=set(); cert=0
    for p in scripts:
        rel=p.relative_to(ROOT).as_posix(); text=p.read_text(encoding='utf-8'); row=bypath.get(rel)
        if not row: fail(f'uncataloged {rel}')
        if not text.startswith('deepml motion 0.3\n'): fail(f'header {rel}')
        if '\nmodule ' not in text: fail(f'module {rel}')
        if 'policy deterministic' not in text or 'policy no_network' not in text: fail(f'policy {rel}')
        if text.count('{')!=text.count('}'): fail(f'braces {rel}')
        observed=hashlib.sha256(text.rstrip('\n').encode()).hexdigest()
        if observed!=row['source_hash'].replace('sha256:',''): fail(f'script hash {rel}')
        classes.add(row['class']); tiers.add(int(row['tier'])); topics.add(row['topic'])
        if row['class']=='certification': cert += 1
    if classes!={'positive','negative','certification'}: fail(f'class coverage {classes}')
    if tiers!={1,2,3,4,5,6}: fail(f'tier coverage {tiers}')
    if len(topics)!=45: fail(f'topic coverage {len(topics)}')
    if cert!=30: fail(f'certification count {cert}')
    mp=ROOT/'manifests'/'MANIFEST.json'
    if mp.exists():
        m=json.loads(mp.read_text(encoding='utf-8'))
        for item in m['files']:
            p=ROOT/item['path']
            if not p.exists(): fail(f'missing manifest file {item["path"]}')
            if sha(p)!=item['sha256']: fail(f'manifest hash {item["path"]}')
    print('PASS: 10,000 records; 1,000 scripts; hashes, policies, braces, coverage, catalogs, certification holdouts, and manifest verified.')
    return 0
if __name__=='__main__': raise SystemExit(main())
