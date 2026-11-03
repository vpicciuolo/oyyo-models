# OYYO Code 1.0

**Coding, debugging and code review** · Local text-model candidate

A coding-focused candidate for understanding source, drafting small changes, identifying edge cases and reviewing implementation choices. Best used with exact snippets, errors and expected behaviour.

## Suitable requests

Capabilities in the runtime catalog: coding, code-review, debugging. These are routing labels and intended tasks, not independent benchmark results. Provide the source facts, audience, constraints and desired format; OYYO can prepare a role-specific prompt.

> Review this function for correctness and input handling. Propose a minimal patch and explain how to test it.

## Requirements

| Item | Catalog information |
| --- | --- |
| Package ID | `oyyo-code-1.0-q4` |
| Parameter class | 7 billion; architecture-dependent, not a memory estimate |
| Weight download | 4.68 GB (4,683,073,536 bytes) |
| Artifact | GGUF · Q4_K_M |
| Minimum system RAM estimate | 12 GB |
| Recommended system RAM estimate | 18 GB |
| Suggested free disk before download | More than 5.8 GiB; includes the runtime fit-check margin, excludes unrelated app/storage needs |
| CPU | Compatible installed inference backend; actual performance must be measured |
| GPU | Optional; partial offload depends on backend, drivers, free VRAM and context |
| Catalog license identifier | `apache-2.0`; applicable artifact terms govern use |

System RAM and GPU VRAM are separate resources. These RAM values are catalog estimates, not measurements or guarantees. Context buffers, concurrent roles and other apps increase memory demand. A 4 GB GPU does not make every model runnable; sufficient system RAM and a compatible engine remain necessary.

## Intended workflow

Supply the goal, relevant source facts, audience, constraints and desired format. The OYYO workspace can prepare the task-specific brief and select an eligible model. A catalog listing describes an option; readiness requires successful qualification and acceptance on the relevant device.

**Available for private demos and private beta. [Request early access](https://oyyo.one/contact).**

## Limits and verification

Reading text is not repository access. Edits, builds and tests require authorised tools and execution evidence.

This is a text model. It does not by itself generate images/video, transcribe audio, browse the web, execute code, publish posts or export documents. Those features require the corresponding OYYO tool, speech pack or connected service. Output length and supplied context are controlled by runtime settings; a maximum usable context is not certified in this registry.

OYYO names identify product configurations. They do not assert that the underlying weights were originally trained by OYYO. Required rights, attribution and provenance records remain applicable; see [licensing](../LICENSE.md) and [provenance policy](../provenance/README.md).

## Artifact integrity

`SHA-256: 509287f78cb4d4cf6b3843734733b914b2c158e43e22a7f4bf5e963800894d3c`

A hash identifies the configured artifact; it is not a quality score. Changing the artifact or inference implementation can require requalification. See [qualification](../docs/QUALIFICATION.md), [hardware](../docs/HARDWARE.md) and [routing](../docs/ROUTING.md).

Copyright © 2026 OYYO · HRN INNOVATION TECHNOLOGIES LTD. All rights reserved.
