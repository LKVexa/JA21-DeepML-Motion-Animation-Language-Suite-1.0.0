# JA21 DeepML Motion Animation Language Suite 1 0 0 main Updated Corpus Audit

This updated copy supplies rigs, poses, blends and retargeting service contracts. Its import boundary is: Keep simulation and physical/display execution evidence distinct.

## Source and coverage

Original input: `JA21-DeepML-Motion-Animation-Language-Suite-1.0.0-main.zip`. Source SHA 256: `a14639c4c87b81e1174c4205ad6435a6e6a95f7e79254e8b6997b10c2122f517`. The source archive is preserved in the parent folder. All 1,167 original leaf files were read and hashed; 31,390 stored JSONL rows were structurally parsed, including historical/reconstructed copies. Nested ZIPs are materialized in `.expanded` directories. Dataset row counts include duplicate representations and metadata headers; they are not unique executable programs.

Original checks and locations are in [the source manifest](audit/source_manifest.json). Current payload bytes are in [the updated manifest](audit/updated_manifest.json), and changes are in [the ledger](audit/change_ledger.json). Embedded source layers have [separate coverage](audit/embedded_layer_coverage.json). Historical hashes and modeled labels retain their historical meaning. The updated manifest and qualification sidecars govern this release.

## Upgrades and open implementation work

### deepml.motion-GRAMMAR-001 High priority

Published EBNF is not complete. Undefined domain/lexical references prevent complete source parsing.

Status: **qualified; full domain grammar remains implementation backlog**. Precise per-profile grammar errata, machine-readable reference-gap index, draft lexical appendix and README link. Existing source grammar remains historical/provisional rather than being filled with permissive catch-all rules.

Evidence: `JA21-DeepML-Motion-Animation-Language-Suite-1.0.0-main.zip::JA21-DeepML-Motion-Animation-Language-Suite-1.0.0-main/JA21_DMLM_Suite_1.0.0.zip::JA21_DMLM_Suite_1.0.0/specifications/DEEPML_MOTION_LANGUAGE.ebnf`.

Remaining gate: Full domain grammar remains open.

### deepml.motion-EVIDENCE-001 High priority

Generated pass/runtime/AST labels are expected modeled evidence; no native compiler/runtime binary is supplied.

Status: **applied**. Every current published corpus/technical gzip record gains explicit _deepml_audit: modeled_not_executed, observed_result null, native_execution_eligible false, exact source SHA evidence and conflict quarantine.

Evidence: `JA21-DeepML-Motion-Animation-Language-Suite-1.0.0-main.zip::JA21-DeepML-Motion-Animation-Language-Suite-1.0.0-main/JA21_DMLM_Suite_1.0.0.zip::JA21_DMLM_Suite_1.0.0/corpus/technical/deepml_motion_animation_technical_corpus_10000.jsonl.gz`.

### deepml.motion-VALIDATOR-001 Medium priority

Inherited structural validator does not apply the published JSON Schema or demonstrate lexical, type, proof or runtime conformance.

Status: **applied and independently verified: Draft202012 full dataset validation and focused authority/corruption tests PASS**. New offline Draft202012 schema validator additionally enforces source/profile/policy consistency, independently recomputes audit qualification and checks master/shard equality. Publication schema requires the new audit extension; tests exercise source corruption, policy removal, forged execution flags and external references.

Evidence: `JA21-DeepML-Motion-Animation-Language-Suite-1.0.0-main.zip::JA21-DeepML-Motion-Animation-Language-Suite-1.0.0-main/JA21_DMLM_Suite_1.0.0.zip::JA21_DMLM_Suite_1.0.0/tools/validate_suite.py`.

### deepml.motion-EXTENSION-001 Medium priority

Editorial couplingMechanics8SRecord rule is not reachable from program, and conceptual annotations do not supply executable mathematical/numerical evidence.

Status: **qualified**. Grammar index explicitly records disconnected extension and errata qualifies it as a separately adopted, independently evidenced experimental extension.

Evidence: `JA21-DeepML-Motion-Animation-Language-Suite-1.0.0-main.zip::JA21-DeepML-Motion-Animation-Language-Suite-1.0.0-main/JA21_DMLM_Suite_1.0.0.zip::JA21_DMLM_Suite_1.0.0/specifications/DEEPML_MOTION_LANGUAGE.ebnf`.

### BASE-06 Medium priority

Nested packaging, raw modeled labels and historical copies need explicit current provenance and reuse boundaries.

Status: **APPLIED**. Expanded materialized payload; source and updated manifests; change ledger; dataset-bound qualification; individual audit and fabric role.

Evidence: `audit/source_manifest.json | audit/updated_manifest.json | audit/dataset_qualification.json`.

Remaining gate: Keep simulation and physical/display execution evidence distinct.

## Contribution to the new fabric language

Profile owner: `deepml.motion`. Rigs, poses, blends and retargeting service contracts. Keep simulation and physical/display execution evidence distinct.

The [adapter contract](audit/fabric_adapter_contract.json) is a proposed interface with executable_adapter_implemented=false. It preserves source authority rather than using a feature label as inferred semantics. See [the collection architecture](../../fabric_language/ARCHITECTURE.md) and the [8S foundation](../../fabric_language/profiles/coupling8s/PROFILE.md).

## Qualification and verification

Use [dataset qualifications](audit/dataset_qualification.json) before training, importing or treating a record as evidence. A modeled pass or a structural validator pass is not native execution, authenticated federation, race proof, or physical device evidence. Current JA and DeepML technical records carry additional qualifications; deliberate negative examples remain negative examples.

The release provides an offline integrity checker: run `python tools/verify_release.py --deep` from the collection root. Per-profile test reports and validators qualify the exact behavior they checked. Complete grammars, native adapters, authenticated transports and a bootable unikernel remain separately tracked implementation gates.
