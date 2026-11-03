# OYYO Team 3.0

**Large multi-role workload candidate** · Local text-model candidate

A large catalog candidate intended for substantial chat, reasoning and coding requests. An OYYO agent team can assign this model to a role when it is compatible and qualified.

## Suitable requests

Capabilities in the runtime catalog: chat, reasoning, coding. These are routing labels and intended tasks, not independent benchmark results. Provide the source facts, audience, constraints and desired format; OYYO can prepare a role-specific prompt.

> Combine the supplied specialist findings into one consistent project plan, resolve conflicts and list unresolved decisions.

## Requirements

| Item | Catalog information |
| --- | --- |
| Package ID | `oyyo-team-3.0-q4` |
| Parameter class | 35 billion; architecture-dependent, not a memory estimate |
| Weight download | 22.13 GB (22,134,528,992 bytes) |
| Artifact | GGUF · Q4_K_M |
| Minimum system RAM estimate | 32 GB |
| Recommended system RAM estimate | 48 GB |
| Suggested free disk before download | More than 23.7 GiB; includes the runtime fit-check margin, excludes unrelated app/storage needs |
| CPU | Compatible installed inference backend; actual performance must be measured |
| GPU | Optional; partial offload depends on backend, drivers, free VRAM and context |
| Catalog license identifier | `apache-2.0`; applicable artifact terms govern use |

System RAM and GPU VRAM are separate resources. These RAM values are catalog estimates, not measurements or guarantees. Context buffers, concurrent roles and other apps increase memory demand. A 4 GB GPU does not make every model runnable; sufficient system RAM and a compatible engine remain necessary.

## How to use it

1. Install OYYO through the [Runtime Runner](https://github.com/vpicciuolo/oyyo-runtime-runner).
2. Open **More → Model lineup** and find **OYYO Team 3.0**.
3. Review the hardware fit estimate, download the package and run its local quality check.
4. After successful qualification and acceptance, leave routing on Auto or select this model explicitly. A failed check must not be bypassed.
5. Write the request naturally. Use a profile, task template or selected agents when you need reusable instructions.

Availability here means a catalog entry with a pinned artifact, not a published global certification or a guarantee of successful execution on every backend. Device-specific pass/fail and timing results remain in that installation.

## Limits and verification

The word Team does not mean multiple agents or distributed execution are built into the weights. Runtime orchestration creates the team.

This is a text model. It does not by itself generate images/video, transcribe audio, browse the web, execute code, publish posts or export documents. Those features require the corresponding OYYO tool, speech pack or connected service. Output length and supplied context are controlled by runtime settings; a maximum usable context is not certified in this registry.

OYYO names identify product configurations. They do not assert that the underlying weights were originally trained by OYYO. Required rights, attribution and provenance records remain applicable; see [licensing](../LICENSE.md) and [provenance policy](../provenance/README.md).

## Artifact integrity

`SHA-256: ac0e2c1189e055faa36eff361580e79c5bd6f8e76bffb4ce547f167d53e31a61`

A hash identifies the configured artifact; it is not a quality score. Changing the artifact or inference implementation can require requalification. See [qualification](../docs/QUALIFICATION.md), [hardware](../docs/HARDWARE.md) and [routing](../docs/ROUTING.md).

Copyright © 2026 OYYO · HRN INNOVATION TECHNOLOGIES LTD. All rights reserved.
