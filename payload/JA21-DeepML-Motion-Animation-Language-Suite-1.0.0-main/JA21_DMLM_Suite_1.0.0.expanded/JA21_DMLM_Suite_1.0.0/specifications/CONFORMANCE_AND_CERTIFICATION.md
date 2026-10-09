
# Conformance and Certification

## Evidence layers

1. **Metadata conformance** — required IDs, versions, hashes, policies, and provenance exist.
2. **Grammar conformance** — source parses under the declared DeepML Motion 0.3 profile.
3. **Name conformance** — rigs, joints, clips, channels, masks, states, targets, databases, and adapters resolve.
4. **Structural conformance** — hierarchies are acyclic; channel targets, keyframes, bind poses, and retarget maps are valid.
5. **Semantic conformance** — coordinate spaces, blend rules, transitions, contacts, root motion, timing, and solver ordering are valid.
6. **Safety conformance** — capabilities, no-network policy, local assets, and unknown-code restrictions pass.
7. **Runtime conformance** — the expected state trace, output hash, or declared tolerance relation is reproduced.
8. **R12/MCRT conformance** — relation, operator, status, error, confidence, provenance, and replay identity remain consistent.

## Corpus evidence

The suite contains 7,875 positive records, 2,095 negative records, and 30 certification holdouts. A negative example passes when it is rejected at the expected stage with the expected diagnostic behavior.

## Holdout discipline

Certification records must remain separated from ordinary tuning data. Exposure, implementation changes after exposure, and any partial support must be disclosed in the final conformance report.

## Native-evidence boundary

This publication validates corpus structure, exact source hashes, policies, catalogs, braces, coverage, manifests, and archive integrity. It does not claim native parsing, skeletal evaluation, playback, solving, rendering, or replay because no conforming compiler/runtime binary was supplied.
