# OYYO Core 2.0

**Reasoning, analysis and code** · Local text-model candidate

A mid-sized candidate for structured analysis, debugging explanations and multi-step technical work. Supply source material and explicit acceptance criteria.

## Suitable requests

Capabilities in the runtime catalog: reasoning, coding, analysis. These are routing labels and intended tasks, not independent benchmark results. Provide the source facts, audience, constraints and desired format; OYYO can prepare a role-specific prompt.

> Analyse this bug report and source snippet. Give the likely cause, a proposed patch and meaningful verification steps.

## Requirements

| Item | Catalog information |
| --- | --- |
| Package ID | `oyyo-core-2.0-q4` |
| Parameter class | 9 billion; architecture-dependent, not a memory estimate |
| Weight download | 5.68 GB (5,680,522,464 bytes) |
| Artifact | GGUF · Q4_K_M |
| Minimum system RAM estimate | 16 GB |
| Recommended system RAM estimate | 24 GB |
| Suggested free disk before download | More than 6.8 GiB; includes the runtime fit-check margin, excludes unrelated app/storage needs |
| CPU | Compatible installed inference backend; actual performance must be measured |
| GPU | Optional; partial offload depends on backend, drivers, free VRAM and context |
| Catalog license identifier | `apache-2.0`; applicable artifact terms govern use |

System RAM and GPU VRAM are separate resources. These RAM values are catalog estimates, not measurements or guarantees. Context buffers, concurrent roles and other apps increase memory demand. A 4 GB GPU does not make every model runnable; sufficient system RAM and a compatible engine remain necessary.

## Intended workflow

Supply the goal, relevant source facts, audience, constraints and desired format. The OYYO workspace can prepare the task-specific brief and select an eligible model. A catalog listing describes an option; readiness requires successful qualification and acceptance on the relevant device.

**Available for private demos and private beta. [Request early access](https://oyyo.one/contact).**

## Limits and verification

More memory than Core 1.0. Code is a proposal until applied and tested through actual tools.

This is a text model. It does not by itself generate images/video, transcribe audio, browse the web, execute code, publish posts or export documents. Those features require the corresponding OYYO tool, speech pack or connected service. Output length and supplied context are controlled by runtime settings; a maximum usable context is not certified in this registry.

OYYO names identify product configurations. They do not assert that the underlying weights were originally trained by OYYO. Required rights, attribution and provenance records remain applicable; see [licensing](../LICENSE.md) and [provenance policy](../provenance/README.md).

## Artifact integrity

`SHA-256: 03b74727a860a56338e042c4420bb3f04b2fec5734175f4cb9fa853daf52b7e8`

A hash identifies the configured artifact; it is not a quality score. Changing the artifact or inference implementation can require requalification. See [qualification](../docs/QUALIFICATION.md), [hardware](../docs/HARDWARE.md) and [routing](../docs/ROUTING.md).

Copyright © 2026 OYYO · HRN INNOVATION TECHNOLOGIES LTD. All rights reserved.
