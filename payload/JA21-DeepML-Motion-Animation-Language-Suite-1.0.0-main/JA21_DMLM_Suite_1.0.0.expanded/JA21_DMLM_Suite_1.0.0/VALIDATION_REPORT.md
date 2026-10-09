
# Validation Report — JA21 DeepML Motion/Animation Language Suite 1.0.0

## Result

**PASS — structural and package-integrity validation completed.**

## Corpus checks

- 10,000 normalized records read successfully.
- 10,000 unique IDs and a continuous sequence from 1 through 10,000.
- All 10,000 source hashes match the exact source stored in the normalized corpus.
- 45 topics, six tiers, three example classes, and 5 expected stages retained.
- Original record-level and document-level Smithson 8S evidence retained with explicit claim boundaries.

## Script-pack checks

- Exactly 1,000 `.deepml` source files.
- Exactly 1,000 CSV and JSONL catalog entries.
- Composition: 760 positive, 210 negative, 30 certification.
- All 45 topics and all six tiers represented.
- All 30 certification holdouts included.
- Required `deepml motion 0.3` header, module declaration, deterministic policy, and no-network policy present.
- Balanced braces and source hashes verified for every curated script.

## Publication checks

- Textbook chapters: 22.
- Approximate textbook word count: 16,614.
- Curriculum, workbook, instructor guide, specifications, contracts, schemas, conformance assets, starter project, tools, catalogs, source reconstruction, governance, provenance, and release documentation present.
- Maximum relative path length before manifest creation: 104 characters.
- Generated names avoid Windows-reserved characters and use compact paths.

## Evidence boundary

No native DeepML Motion compiler or runtime executable was supplied. This report validates structural, source-hash, policy, catalog, coverage, and packaging integrity. It does not claim native parsing, compilation, optimization, skeletal evaluation, solver execution, playback, rendering, or runtime replay.
