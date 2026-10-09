# JA21 DeepML Motion/Animation Language
## A Technical Textbook for Rigs, Clips, Controllers, Compilation, Runtime Replay, and Coupled Mechanics

**Suite edition:** 1.0.0  
**Language profile:** DeepML Motion 0.3  
**Technical corpus:** 10,000 records  
**Example library:** 1,000 source-faithful programs

> Motion is treated here as executable evidence: hierarchy, transforms, timing, constraints, policies, compiler stages, runtime traces, tolerances, R12/MCRT relations, and provenance remain connected.

## Editorial architecture

- **SOPHIA:** semantic integrity, mathematical claim boundaries, motion invariants, and evidence discipline.
- **CHARLOTTE:** corpus taxonomy, learning architecture, indexing, terminology, and editorial coherence.
- **LANDON:** compiler/runtime contracts, deterministic replay, diagnostics, and package engineering.
- **Professor:** technical pedagogy, laboratories, assessment, and curriculum sequencing.
- **Podium:** publication quality, visual hierarchy, navigability, release presentation, and institutional finish.

## How to use this book

Chapters 1–6 establish motion data and time. Chapters 7–11 build control, solving, retargeting, and synchronization. Chapters 12–17 cover procedural and integrated systems. Chapters 18–22 focus on optimization, diagnostics, evidence lowering, coupled mechanics, and the standalone toolchain capstone. Each chapter includes a corpus-derived program, an engineering checklist, a laboratory, and review questions.

## Table of contents

1. The Motion Language as an Evidence-Bearing JA21 Suite
2. Transforms, Coordinate Spaces, and Composition
3. Skeletons, Joints, Bind Poses, and Rig Topology
4. Poses, Channels, and Motion State
5. Clips, Keyframes, Interpolation, and Time
6. Curves, Compression, and Tolerance Evidence
7. Blend Trees, Masks, and Weight Normalization
8. State Machines, Layers, Guards, and Reachability
9. Inverse Kinematics, Constraints, and Scheduling
10. Retargeting, Bind-Space Maps, and Cache Identity
11. Root Motion and Scene/Timeline Synchronization
12. Procedural Animation and Deterministic Seeds
13. Motion Matching and Trajectory Prediction
14. Locomotion Controllers and Contact Preservation
15. Physics-Aware Animation and Bounded Recovery
16. Portal Traversal, Cinematic Motion, and Editorial Timing
17. Crowd Motion, Scheduling, and Scalable Replay
18. Compiler Optimization for Motion Graphs
19. Diagnostics: Invalid Rigs, Solvers, States, and Replays
20. R12/MCRT Lowering, Provenance, and Replay
21. Smithson 8S Coupled Mechanics for Motion Systems
22. Capstone: A Standalone DeepML Motion Toolchain

# Chapter 1: The Motion Language as an Evidence-Bearing JA21 Suite

## Learning objectives

- Explain the role of motion module in the DeepML Motion evidence chain.
- Author and inspect a bounded motion module program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

The Motion Language as an Evidence-Bearing JA21 Suite is taught as a governed relation rather than an isolated visual trick. The principal concerns are language identity, module boundaries, deterministic policy, and the source-to-runtime evidence chain. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Motion Module part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_00005
policy deterministic
policy no_network
skeleton Rig00005 {
  joint Root parent none bind transform(vec3(0,0,0), quat.identity)
  joint Hip parent Root bind transform(vec3(0,0.6,0), quat.identity)
  joint Foot parent Hip bind transform(vec3(0,-0.7,0), quat.identity)
}
pose Idle00005 for Rig00005 { Root.rotation = quat.identity Hip.rotation = quat.axis_angle(y, 5deg) }
clip Clip00005 duration 1s interpolation cubic { channel Hip.rotation key 0s quat.identity key 1s quat.axis_angle(y, 20deg) }
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Build an annotated evidence map for ten foundation programs.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct motion module behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 2: Transforms, Coordinate Spaces, and Composition

## Learning objectives

- Explain the role of transform in the DeepML Motion evidence chain.
- Author and inspect a bounded transform program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

Transforms, Coordinate Spaces, and Composition is taught as a governed relation rather than an isolated visual trick. The principal concerns are translation, rotation, scale, local and world spaces, composition order, and stable transform identity. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Transform part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_00002
policy deterministic
policy no_network
skeleton Rig00002 {
  joint Root parent none bind transform(vec3(0,0,0), quat.identity)
  joint Hip parent Root bind transform(vec3(0,0.3,0), quat.identity)
  joint Foot parent Hip bind transform(vec3(0,-0.4,0), quat.identity)
}
pose Idle00002 for Rig00002 { Root.rotation = quat.identity Hip.rotation = quat.axis_angle(y, 2deg) }
clip Clip00002 duration 3s interpolation cubic { channel Hip.rotation key 0s quat.identity key 1s quat.axis_angle(y, 20deg) }
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Compare two transform-composition orders and document the semantic difference.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct transform behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 3: Skeletons, Joints, Bind Poses, and Rig Topology

## Learning objectives

- Explain the role of skeleton in the DeepML Motion evidence chain.
- Author and inspect a bounded skeleton program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

Skeletons, Joints, Bind Poses, and Rig Topology is taught as a governed relation rather than an isolated visual trick. The principal concerns are acyclic joint hierarchies, parentage, bind-space evidence, stable names, and topology validation. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Skeleton part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_00004
policy deterministic
policy no_network
skeleton Rig00004 {
  joint Root parent none bind transform(vec3(0,0,0), quat.identity)
  joint Hip parent Root bind transform(vec3(0,0.5,0), quat.identity)
  joint Foot parent Hip bind transform(vec3(0,-0.6,0), quat.identity)
}
pose Idle00004 for Rig00004 { Root.rotation = quat.identity Hip.rotation = quat.axis_angle(y, 4deg) }
clip Clip00004 duration 5s interpolation cubic { channel Hip.rotation key 0s quat.identity key 1s quat.axis_angle(y, 20deg) }
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Design a small rig plus three invalid topology tests.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct skeleton behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 4: Poses, Channels, and Motion State

## Learning objectives

- Explain the role of pose in the DeepML Motion evidence chain.
- Author and inspect a bounded pose program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

Poses, Channels, and Motion State is taught as a governed relation rather than an isolated visual trick. The principal concerns are named poses, channel ownership, value domains, masking, and reusable motion state. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Pose part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_00001
policy deterministic
policy no_network
skeleton Rig00001 {
  joint Root parent none bind transform(vec3(0,0,0), quat.identity)
  joint Hip parent Root bind transform(vec3(0,0.2,0), quat.identity)
  joint Foot parent Hip bind transform(vec3(0,-0.3,0), quat.identity)
}
pose Idle00001 for Rig00001 { Root.rotation = quat.identity Hip.rotation = quat.axis_angle(y, 1deg) }
clip Clip00001 duration 2s interpolation cubic { channel Hip.rotation key 0s quat.identity key 1s quat.axis_angle(y, 20deg) }
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Author a pose library and prove channel-target validity.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct pose behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 5: Clips, Keyframes, Interpolation, and Time

## Learning objectives

- Explain the role of clip in the DeepML Motion evidence chain.
- Author and inspect a bounded clip program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

Clips, Keyframes, Interpolation, and Time is taught as a governed relation rather than an isolated visual trick. The principal concerns are clip duration, key ordering, interpolation, sampling clocks, boundaries, events, and deterministic playback. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Clip part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_00009
policy deterministic
policy no_network
skeleton Rig00009 {
  joint Root parent none bind transform(vec3(0,0,0), quat.identity)
  joint Hip parent Root bind transform(vec3(0,1.0,0), quat.identity)
  joint Foot parent Hip bind transform(vec3(0,-1.1,0), quat.identity)
}
pose Idle00009 for Rig00009 { Root.rotation = quat.identity Hip.rotation = quat.axis_angle(y, 9deg) }
clip Clip00009 duration 5s interpolation cubic { channel Hip.rotation key 0s quat.identity key 1s quat.axis_angle(y, 20deg) }
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Create a clip with two interpolation profiles and a boundary test.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct clip behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 6: Curves, Compression, and Tolerance Evidence

## Learning objectives

- Explain the role of curve compression in the DeepML Motion evidence chain.
- Author and inspect a bounded curve compression program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

Curves, Compression, and Tolerance Evidence is taught as a governed relation rather than an isolated visual trick. The principal concerns are curve representation, key reduction, error metrics, compression tolerances, and replay equivalence. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Curve Compression part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_07512
policy deterministic
policy no_network
motion_graph Optimize07512 {
  pose A = constant_pose(Rig07512)
  curve HipRotation = keys([0:0, 0.25:0.1, 0.5:0.2, 0.75:0.3, 1:0.4])
  channel DeadChannel enabled false
  blend B weights [0.2,0.3,0.5]
  ik Chain schedule after blend
}
optimize Optimize07512 using [pose_constant_folding, curve_compression(0.001), dead_channel_removal, blend_normalization, retarget_cache, ik_scheduling, state_minimization]
lower Optimize07512 to DEEPML_MOTION_R12
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Compress a curve and publish before/after error evidence.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct curve compression behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 7: Blend Trees, Masks, and Weight Normalization

## Learning objectives

- Explain the role of blend tree in the DeepML Motion evidence chain.
- Author and inspect a bounded blend tree program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

Blend Trees, Masks, and Weight Normalization is taught as a governed relation rather than an isolated visual trick. The principal concerns are parameterized blending, normalization, masks, layer order, degenerate weights, and deterministic ties. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Blend Tree part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_01006
policy deterministic
policy no_network
skeleton Rig01006 { joint Root parent none joint Hip parent Root joint Knee parent Hip joint Foot parent Knee }
blend_tree Locomotion01006 parameter speed { idle at 0 walk at 1 run at 3 }
mask LowerBody { include [Hip, Knee, Foot] }
ik FootIK01006 chain [Hip, Knee, Foot] target GroundTarget iterations 14
retarget SourceRig5 -> Rig01006 map { Hips: Hip LeftFoot: Foot }
state_machine Move01006 { Idle -> Walk when speed > 0.1 Walk -> Run when speed > 2.0 Run -> Idle when speed == 0 }
root_motion from Root axes [x,z]
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Build a locomotion blend tree with a bounded zero-weight fallback.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct blend tree behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 8: State Machines, Layers, Guards, and Reachability

## Learning objectives

- Explain the role of state machine in the DeepML Motion evidence chain.
- Author and inspect a bounded state machine program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

State Machines, Layers, Guards, and Reachability is taught as a governed relation rather than an isolated visual trick. The principal concerns are motion states, guards, transition priority, layered evaluation, reachability, minimization, and event order. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make State Machine part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_01003
policy deterministic
policy no_network
skeleton Rig01003 { joint Root parent none joint Hip parent Root joint Knee parent Hip joint Foot parent Knee }
blend_tree Locomotion01003 parameter speed { idle at 0 walk at 1 run at 3 }
mask LowerBody { include [Hip, Knee, Foot] }
ik FootIK01003 chain [Hip, Knee, Foot] target GroundTarget iterations 11
retarget SourceRig2 -> Rig01003 map { Hips: Hip LeftFoot: Foot }
state_machine Move01003 { Idle -> Walk when speed > 0.1 Walk -> Run when speed > 2.0 Run -> Idle when speed == 0 }
root_motion from Root axes [x,z]
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Model a layered state machine and test an unreachable state.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct state machine behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 9: Inverse Kinematics, Constraints, and Scheduling

## Learning objectives

- Explain the role of inverse kinematics in the DeepML Motion evidence chain.
- Author and inspect a bounded inverse kinematics program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

Inverse Kinematics, Constraints, and Scheduling is taught as a governed relation rather than an isolated visual trick. The principal concerns are joint chains, targets, iteration limits, tolerances, contact constraints, solver order, and nonconvergence. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Inverse Kinematics part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_01001
policy deterministic
policy no_network
skeleton Rig01001 { joint Root parent none joint Hip parent Root joint Knee parent Hip joint Foot parent Knee }
blend_tree Locomotion01001 parameter speed { idle at 0 walk at 1 run at 3 }
mask LowerBody { include [Hip, Knee, Foot] }
ik FootIK01001 chain [Hip, Knee, Foot] target GroundTarget iterations 9
retarget SourceRig0 -> Rig01001 map { Hips: Hip LeftFoot: Foot }
state_machine Move01001 { Idle -> Walk when speed > 0.1 Walk -> Run when speed > 2.0 Run -> Idle when speed == 0 }
root_motion from Root axes [x,z]
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Specify a foot IK chain with a deterministic failure mode.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct inverse kinematics behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 10: Retargeting, Bind-Space Maps, and Cache Identity

## Learning objectives

- Explain the role of retargeting in the DeepML Motion evidence chain.
- Author and inspect a bounded retargeting program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

Retargeting, Bind-Space Maps, and Cache Identity is taught as a governed relation rather than an isolated visual trick. The principal concerns are semantic joint mapping, proportion differences, bind poses, retarget caches, invalid maps, and provenance. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Retargeting part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_01002
policy deterministic
policy no_network
skeleton Rig01002 { joint Root parent none joint Hip parent Root joint Knee parent Hip joint Foot parent Knee }
blend_tree Locomotion01002 parameter speed { idle at 0 walk at 1 run at 3 }
mask LowerBody { include [Hip, Knee, Foot] }
ik FootIK01002 chain [Hip, Knee, Foot] target GroundTarget iterations 10
retarget SourceRig1 -> Rig01002 map { Hips: Hip LeftFoot: Foot }
state_machine Move01002 { Idle -> Walk when speed > 0.1 Walk -> Run when speed > 2.0 Run -> Idle when speed == 0 }
root_motion from Root axes [x,z]
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Retarget one clip between two rigs and document every mapping assumption.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct retargeting behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 11: Root Motion and Scene/Timeline Synchronization

## Learning objectives

- Explain the role of root motion in the DeepML Motion evidence chain.
- Author and inspect a bounded root motion program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

Root Motion and Scene/Timeline Synchronization is taught as a governed relation rather than an isolated visual trick. The principal concerns are root extraction, local motion, world displacement, scene clocks, timeline bindings, and synchronization drift. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Root Motion part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_01004
policy deterministic
policy no_network
skeleton Rig01004 { joint Root parent none joint Hip parent Root joint Knee parent Hip joint Foot parent Knee }
blend_tree Locomotion01004 parameter speed { idle at 0 walk at 1 run at 3 }
mask LowerBody { include [Hip, Knee, Foot] }
ik FootIK01004 chain [Hip, Knee, Foot] target GroundTarget iterations 12
retarget SourceRig3 -> Rig01004 map { Hips: Hip LeftFoot: Foot }
state_machine Move01004 { Idle -> Walk when speed > 0.1 Walk -> Run when speed > 2.0 Run -> Idle when speed == 0 }
root_motion from Root axes [x,z]
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Design a root-motion policy and a scene/timeline replay test.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct root motion behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 12: Procedural Animation and Deterministic Seeds

## Learning objectives

- Explain the role of procedural animation in the DeepML Motion evidence chain.
- Author and inspect a bounded procedural animation program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

Procedural Animation and Deterministic Seeds is taught as a governed relation rather than an isolated visual trick. The principal concerns are generated motion, declared inputs, deterministic seeds, local databases, constraint composition, and bounded state. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Procedural Animation part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_02505
policy deterministic
policy no_network
skeleton Rig02505 { joint Root parent none joint Hip parent Root joint FootL parent Hip joint FootR parent Hip }
procedural animation Procedural02505 seed 2505 {
  trajectory = predict_trajectory(velocity, horizon=1.0s)
  match = motion_match(database="local:motions_3", trajectory=trajectory)
  constrain contact FootL to ground when phase < 0.5
  constrain contact FootR to ground when phase >= 0.5
}
layered state_machine Layers02505 { base: Locomotion upper: Gesture additive: Breathing }
synchronize Procedural02505 with scene.Actor6 and timeline.Sequence9
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Build a procedural cycle whose output can be reproduced from a seed and state snapshot.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct procedural animation behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 13: Motion Matching and Trajectory Prediction

## Learning objectives

- Explain the role of motion matching in the DeepML Motion evidence chain.
- Author and inspect a bounded motion matching program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

Motion Matching and Trajectory Prediction is taught as a governed relation rather than an isolated visual trick. The principal concerns are feature vectors, local motion databases, distance metrics, prediction horizons, tie-breaks, and query provenance. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Motion Matching part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_02504
policy deterministic
policy no_network
skeleton Rig02504 { joint Root parent none joint Hip parent Root joint FootL parent Hip joint FootR parent Hip }
procedural animation Procedural02504 seed 2504 {
  trajectory = predict_trajectory(velocity, horizon=1.0s)
  match = motion_match(database="local:motions_2", trajectory=trajectory)
  constrain contact FootL to ground when phase < 0.5
  constrain contact FootR to ground when phase >= 0.5
}
layered state_machine Layers02504 { base: Locomotion upper: Gesture additive: Breathing }
synchronize Procedural02504 with scene.Actor5 and timeline.Sequence8
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Specify a motion-matching query and a deterministic equal-score tie-break.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct motion matching behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 14: Locomotion Controllers and Contact Preservation

## Learning objectives

- Explain the role of locomotion controller in the DeepML Motion evidence chain.
- Author and inspect a bounded locomotion controller program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

Locomotion Controllers and Contact Preservation is taught as a governed relation rather than an isolated visual trick. The principal concerns are controller composition, parameters, contacts, foot-slide tolerances, root motion, and phase-aware transitions. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Locomotion Controller part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_05001
policy deterministic
policy no_network
character Rig05001 {
  skeleton Humanoid1
  controller Locomotion { blend: locomotion_3 ik: feet trajectory: predictive }
  controller Cinematic { timeline: "cinematic_7" masks: [upper_body, face] }
  portal traversal { entry_pose: PortalEnter exit_pose: PortalExit root_motion: preserve }
  physics coupling { ragdoll: bounded recovery: deterministic }
}
crowd motion Crowd05001 agents 61 controller Rig05001 avoidance deterministic
package motion Rig05001 as "motion_05001.msslb"
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Create a locomotion controller with measurable contact and slide criteria.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct locomotion controller behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 15: Physics-Aware Animation and Bounded Recovery

## Learning objectives

- Explain the role of physics aware animation in the DeepML Motion evidence chain.
- Author and inspect a bounded physics aware animation program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

Physics-Aware Animation and Bounded Recovery is taught as a governed relation rather than an isolated visual trick. The principal concerns are animation/physics handoff, ragdoll state, impulses, recovery, contact, energy bounds, and deterministic reconciliation. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Physics Aware Animation part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_05003
policy deterministic
policy no_network
character Rig05003 {
  skeleton Humanoid3
  controller Locomotion { blend: locomotion_5 ik: feet trajectory: predictive }
  controller Cinematic { timeline: "cinematic_9" masks: [upper_body, face] }
  portal traversal { entry_pose: PortalEnter exit_pose: PortalExit root_motion: preserve }
  physics coupling { ragdoll: bounded recovery: deterministic }
}
crowd motion Crowd05003 agents 63 controller Rig05003 avoidance deterministic
package motion Rig05003 as "motion_05003.msslb"
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Design a bounded fall-and-recovery sequence with explicit handoff evidence.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct physics aware animation behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 16: Portal Traversal, Cinematic Motion, and Editorial Timing

## Learning objectives

- Explain the role of portal traversal in the DeepML Motion evidence chain.
- Author and inspect a bounded portal traversal program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

Portal Traversal, Cinematic Motion, and Editorial Timing is taught as a governed relation rather than an isolated visual trick. The principal concerns are entry and exit poses, spatial discontinuity, root preservation, masks, camera timing, and timeline contracts. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Portal Traversal part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_05004
policy deterministic
policy no_network
character Rig05004 {
  skeleton Humanoid4
  controller Locomotion { blend: locomotion_6 ik: feet trajectory: predictive }
  controller Cinematic { timeline: "cinematic_10" masks: [upper_body, face] }
  portal traversal { entry_pose: PortalEnter exit_pose: PortalExit root_motion: preserve }
  physics coupling { ragdoll: bounded recovery: deterministic }
}
crowd motion Crowd05004 agents 64 controller Rig05004 avoidance deterministic
package motion Rig05004 as "motion_05004.msslb"
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Build a portal traversal sequence synchronized to a cinematic marker track.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct portal traversal behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 17: Crowd Motion, Scheduling, and Scalable Replay

## Learning objectives

- Explain the role of crowd motion in the DeepML Motion evidence chain.
- Author and inspect a bounded crowd motion program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

Crowd Motion, Scheduling, and Scalable Replay is taught as a governed relation rather than an isolated visual trick. The principal concerns are agent identity, local avoidance, scheduling, shared motion data, deterministic variation, and scalable traces. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Crowd Motion part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_05005
policy deterministic
policy no_network
character Rig05005 {
  skeleton Humanoid0
  controller Locomotion { blend: locomotion_0 ik: feet trajectory: predictive }
  controller Cinematic { timeline: "cinematic_0" masks: [upper_body, face] }
  portal traversal { entry_pose: PortalEnter exit_pose: PortalExit root_motion: preserve }
  physics coupling { ragdoll: bounded recovery: deterministic }
}
crowd motion Crowd05005 agents 65 controller Rig05005 avoidance deterministic
package motion Rig05005 as "motion_05005.msslb"
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Specify a 64-agent deterministic crowd test with stable identities and seeds.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct crowd motion behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 18: Compiler Optimization for Motion Graphs

## Learning objectives

- Explain the role of pose constant folding in the DeepML Motion evidence chain.
- Author and inspect a bounded pose constant folding program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

Compiler Optimization for Motion Graphs is taught as a governed relation rather than an isolated visual trick. The principal concerns are pose folding, curve compression, dead-channel removal, blend normalization, cache reuse, IK scheduling, and state minimization. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Pose Constant Folding part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_07503
policy deterministic
policy no_network
motion_graph Optimize07503 {
  pose A = constant_pose(Rig07503)
  curve HipRotation = keys([0:0, 0.25:0.1, 0.5:0.2, 0.75:0.3, 1:0.4])
  channel DeadChannel enabled false
  blend B weights [0.2,0.3,0.5]
  ik Chain schedule after blend
}
optimize Optimize07503 using [pose_constant_folding, curve_compression(0.001), dead_channel_removal, blend_normalization, retarget_cache, ik_scheduling, state_minimization]
lower Optimize07503 to DEEPML_MOTION_R12
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Prove one motion optimization using a declared equivalence or tolerance relation.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct pose constant folding behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 19: Diagnostics: Invalid Rigs, Solvers, States, and Replays

## Learning objectives

- Explain the role of joint cycle in the DeepML Motion evidence chain.
- Author and inspect a bounded joint cycle program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

Diagnostics: Invalid Rigs, Solvers, States, and Replays is taught as a governed relation rather than an isolated visual trick. The principal concerns are stage-aware diagnostics, joint cycles, missing bind poses, invalid maps, IK failures, unreachable states, tolerance failures, and replay mismatch. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Joint Cycle part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_09002
policy deterministic
policy no_network
skeleton Rig09002 { joint A parent B joint B parent A }
certify motion Rig09002 profile strict
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Create a diagnostic portfolio with one failure from each responsible stage.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct joint cycle behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 20: R12/MCRT Lowering, Provenance, and Replay

## Learning objectives

- Explain the role of r12 mcrt lowering in the DeepML Motion evidence chain.
- Author and inspect a bounded r12 mcrt lowering program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

R12/MCRT Lowering, Provenance, and Replay is taught as a governed relation rather than an isolated visual trick. The principal concerns are stable relation identities, operators, states, errors, confidence, provenance, semantic hashes, and replay evidence. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make R12 Mcrt Lowering part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_07502
policy deterministic
policy no_network
motion_graph Optimize07502 {
  pose A = constant_pose(Rig07502)
  curve HipRotation = keys([0:0, 0.25:0.1, 0.5:0.2, 0.75:0.3, 1:0.4])
  channel DeadChannel enabled false
  blend B weights [0.2,0.3,0.5]
  ik Chain schedule after blend
}
optimize Optimize07502 using [pose_constant_folding, curve_compression(0.001), dead_channel_removal, blend_normalization, retarget_cache, ik_scheduling, state_minimization]
lower Optimize07502 to DEEPML_MOTION_R12
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Lower one accepted and one rejected motion program into auditable evidence records.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct r12 mcrt lowering behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 21: Smithson 8S Coupled Mechanics for Motion Systems

## Learning objectives

- Explain the role of scene timeline sync in the DeepML Motion evidence chain.
- Author and inspect a bounded scene timeline sync program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

Smithson 8S Coupled Mechanics for Motion Systems is taught as a governed relation rather than an isolated visual trick. The principal concerns are latent five-dimensional centers, S^3 fibers, phase, sparse pairwise and triadic coupling, projections, judgement gaps, and claim boundaries. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Scene Timeline Sync part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_02506
policy deterministic
policy no_network
skeleton Rig02506 { joint Root parent none joint Hip parent Root joint FootL parent Hip joint FootR parent Hip }
procedural animation Procedural02506 seed 2506 {
  trajectory = predict_trajectory(velocity, horizon=1.0s)
  match = motion_match(database="local:motions_4", trajectory=trajectory)
  constrain contact FootL to ground when phase < 0.5
  constrain contact FootR to ground when phase >= 0.5
}
layered state_machine Layers02506 { base: Locomotion upper: Gesture additive: Breathing }
synchronize Procedural02506 with scene.Actor7 and timeline.Sequence10
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Create an 8S motion annotation that keeps latent, projected, and judgement evidence separate.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct scene timeline sync behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Chapter 22: Capstone: A Standalone DeepML Motion Toolchain

## Learning objectives

- Explain the role of character rig in the DeepML Motion evidence chain.
- Author and inspect a bounded character rig program.
- Identify the earliest responsible compiler or runtime failure stage.
- Preserve deterministic, no-network, provenance, and R12/MCRT requirements.
- Design positive, negative, and certification tests for the chapter invariant.

## Core lesson

Capstone: A Standalone DeepML Motion Toolchain is taught as a governed relation rather than an isolated visual trick. The principal concerns are a bounded parser, validator, compiler, runtime, replay harness, corpus tests, package manifest, and honest release evidence. A valid DeepML Motion program therefore carries more than a plausible pose on screen: it carries stable identity, declared coordinate and time assumptions, deterministic policy, no-network policy, provenance, and an expected compiler/runtime route.

The authoring model begins with explicit declarations. Rigs, joints, poses, clips, controllers, targets, databases, adapters, and timelines are named rather than inferred from incidental file order. Motion values must state the space in which they are interpreted, and temporal values must state the clock or duration to which they belong. This keeps a motion asset reproducible when moved between an editor, compiler, runtime, renderer, or certification harness.

The compiler model establishes the earliest responsible proof. Grammar identifies structure; name resolution binds motion entities; structural validation checks hierarchy, target, and timeline relationships; semantic validation checks composition, ordering, constraints, tolerances, and transition rules; the safety gate enforces capabilities; normalization creates a canonical motion graph; optimization is admitted only under an explicit equivalence or tolerance profile; R12 and MCRT emission preserve the accepted or rejected relation. Invalid programs are not partially lowered as if they were valid.

The runtime model evaluates admitted motion in a stable order. Sampling clocks, transition order, blend normalization, solver iteration, contact evaluation, root-motion application, procedural seeds, database tie-breaks, physics handoffs, and adapter calls must be replayable. When exact floating-point or provider identity is not promised, the runtime records the declared tolerance and the evidence used to judge equivalence. Failure produces a bounded diagnostic and state snapshot rather than silent correction.

The most common implementation error is to let visual plausibility replace language correctness. A character may look acceptable while its joint hierarchy is cyclic, a channel targets the wrong space, blend weights drift, root motion is applied twice, an IK solve fails silently, a retarget map loses semantic joints, or a replay chooses a different database candidate. DeepML Motion treats these as testable language and runtime defects. Positive records show accepted behavior; negative records show required rejection; certification records test whether the complete contract remains intact.

The five review lenses keep the chapter balanced. SOPHIA asks whether the mathematical and semantic claim is precise. CHARLOTTE asks whether the concept is named, indexed, and teachable. LANDON asks whether compiler and runtime evidence can be reproduced. Professor asks whether a learner can move from explanation to laboratory and assessment. Podium asks whether the resulting artifact is navigable, legible, and publication-ready. Together they make Character Rig part of a full language suite instead of an undocumented feature.

## Corpus-derived program

```deepml
deepml motion 0.3
module corpus.deepml_motion.example_05002
policy deterministic
policy no_network
character Rig05002 {
  skeleton Humanoid2
  controller Locomotion { blend: locomotion_4 ik: feet trajectory: predictive }
  controller Cinematic { timeline: "cinematic_8" masks: [upper_body, face] }
  portal traversal { entry_pose: PortalEnter exit_pose: PortalExit root_motion: preserve }
  physics coupling { ragdoll: bounded recovery: deterministic }
}
crowd motion Crowd05002 agents 62 controller Rig05002 avoidance deterministic
package motion Rig05002 as "motion_05002.msslb"
```

## Engineering checklist

- Preserve language, module, rig, asset, and relation identities.
- Declare coordinate spaces, clocks, tolerances, and evaluation order.
- Enforce deterministic and no-network policy through compiler and runtime evidence.
- Reject invalid structure or semantics at the earliest responsible stage.
- Preserve source hash, semantic hash, R12 relation, MCRT relation, provenance, and replay context.
- Distinguish exact identity from tolerance-based visual or numerical equivalence.

## Laboratory

Publish a ten-feature toolchain design with positive, negative, and certification evidence.

## Evidence to submit

- Selected corpus and script IDs
- Source and semantic hashes
- Expected compiler/runtime stage and result
- Diagnostic or tolerance profile
- R12/MCRT fields affected
- Replay inputs, output evidence, and limitations

## Review questions

1. What invariant defines correct character rig behavior?
2. Which compiler stage should establish or reject that invariant?
3. Which runtime state must be recorded for deterministic replay?
4. How can visual plausibility conceal a semantic defect?
5. Which positive, negative, and certification cases provide adequate coverage?

---

# Appendix A: Corpus Profile

- Records: 10,000
- Topics: 45
- Positive: 7,875
- Negative: 2,095
- Certification: 30
- Tiers: 1 (1,000), 2 (1,500), 3 (2,500), 4 (2,500), 5 (1,500), 6 (1,000)

# Appendix B: Required Standalone Policies

- Deterministic evaluation
- No network access
- No unknown code execution
- Stable rig, joint, asset, state, and relation identifiers
- Provenance preservation
- Explicit coordinate, clock, equivalence, and tolerance profiles
- Rejection at the earliest responsible stage

# Appendix C: Native-Evidence Boundary

The textbook and suite describe a source-to-runtime contract derived from the uploaded corpus. Native compilation, skeletal evaluation, playback, solving, rendering, and replay remain implementation tasks until a conforming compiler and runtime are supplied and tested.
