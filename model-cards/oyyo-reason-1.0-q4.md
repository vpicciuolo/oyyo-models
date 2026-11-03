# OYYO Reason 1.0

**Multi-step reasoning and mathematics** · Local text-model candidate

A specialist candidate for reasoning-heavy comparisons, mathematical explanation and technical problem decomposition. State the problem, available facts and desired output format.

## Suitable requests

Capabilities in the runtime catalog: reasoning, math, coding. These are routing labels and intended tasks, not independent benchmark results. Provide the source facts, audience, constraints and desired format; OYYO can prepare a role-specific prompt.

> Solve this scheduling problem with the supplied constraints. Show a clear solution and check every constraint.

## Requirements

| Item | Catalog information |
| --- | --- |
| Package ID | `oyyo-reason-1.0-q4` |
| Parameter class | 7 billion; architecture-dependent, not a memory estimate |
| Weight download | 4.68 GB (4,683,073,248 bytes) |
| Artifact | GGUF · Q4_K_M |
| Minimum system RAM estimate | 12 GB |
| Recommended system RAM estimate | 18 GB |
| Suggested free disk before download | More than 5.8 GiB; includes the runtime fit-check margin, excludes unrelated app/storage needs |
| CPU | Compatible installed inference backend; actual performance must be measured |
| GPU | Optional; partial offload depends on backend, drivers, free VRAM and context |
| Catalog license identifier | `apache-2.0`; applicable artifact terms govern use |

System RAM and GPU VRAM are separate resources. These RAM values are catalog estimates, not measurements or guarantees. Context buffers, concurrent roles and other apps increase memory demand. A 4 GB GPU does not make every model runnable; sufficient system RAM and a compatible engine remain necessary.

## How to use it

1. Install OYYO through the [Runtime Runner](https://github.com/vpicciuolo/oyyo-runtime-runner).
2. Open **More → Model lineup** and find **OYYO Reason 1.0**.
3. Review the hardware fit estimate, download the package and run its local quality check.
4. After successful qualification and acceptance, leave routing on Auto or select this model explicitly. A failed check must not be bypassed.
5. Write the request naturally. Use a profile, task template or selected agents when you need reusable instructions.

Availability here means a catalog entry with a pinned artifact, not a published global certification or a guarantee of successful execution on every backend. Device-specific pass/fail and timing results remain in that installation.

## Limits and verification

May be slower than a small chat model. Verify calculations, citations and constraint satisfaction independently.

This is a text model. It does not by itself generate images/video, transcribe audio, browse the web, execute code, publish posts or export documents. Those features require the corresponding OYYO tool, speech pack or connected service. Output length and supplied context are controlled by runtime settings; a maximum usable context is not certified in this registry.

OYYO names identify product configurations. They do not assert that the underlying weights were originally trained by OYYO. Required rights, attribution and provenance records remain applicable; see [licensing](../LICENSE.md) and [provenance policy](../provenance/README.md).

## Artifact integrity

`SHA-256: 78272d8d32084548bd450394a560eb2d70de8232ab96a725769b1f9171235c1c`

A hash identifies the configured artifact; it is not a quality score. Changing the artifact or inference implementation can require requalification. See [qualification](../docs/QUALIFICATION.md), [hardware](../docs/HARDWARE.md) and [routing](../docs/ROUTING.md).

Copyright © 2026 OYYO · HRN INNOVATION TECHNOLOGIES LTD. All rights reserved.
