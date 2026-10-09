#!/usr/bin/env python3
"""Offline inspector for the normalized JA21 DeepML Motion corpus."""
from __future__ import annotations
import argparse, gzip, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / 'corpus' / 'technical' / 'deepml_motion_animation_technical_corpus_10000.jsonl.gz'
def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument('--corpus', type=Path, default=DEFAULT)
    p.add_argument('--topic'); p.add_argument('--class-name', choices=['positive','negative','certification'])
    p.add_argument('--tier', type=int, choices=range(1,7)); p.add_argument('--id'); p.add_argument('--limit', type=int, default=20)
    a = p.parse_args(); shown = 0
    with gzip.open(a.corpus, 'rt', encoding='utf-8') as f:
        for line in f:
            r = json.loads(line); ident,ped = r['identity'],r['pedagogy']
            if a.id and ident['id'] != a.id: continue
            if a.topic and ped['topic'] != a.topic: continue
            if a.class_name and ped['class'] != a.class_name: continue
            if a.tier and ped['tier'] != a.tier: continue
            print(json.dumps(r, indent=2, ensure_ascii=False)); shown += 1
            if shown >= a.limit: break
    return 0
if __name__ == '__main__': raise SystemExit(main())
