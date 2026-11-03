# OYYO Pro 1.0

**Detailed analysis and technical planning** · Local text-model candidate

A larger candidate for structured comparisons, engineering explanations and coding plans. Useful for requests with several constraints and a more substantial final deliverable.

## Suitable requests

Capabilities in the runtime catalog: reasoning, coding, analysis. These are routing labels and intended tasks, not independent benchmark results. Provide the source facts, audience, constraints and desired format; OYYO can prepare a role-specific prompt.

> Compare these three architecture options against cost, reliability and maintenance. State assumptions and recommend a validation plan.

## Requirements

| Item | Catalog information |
| --- | --- |
| Package ID | `oyyo-pro-1.0-q4` |
| Parameter class | 14 billion; architecture-dependent, not a memory estimate |
| Weight download | 9.00 GB (9,001,752,960 bytes) |
| Artifact | GGUF · Q4_K_M |
| Minimum system RAM estimate | 20 GB |
| Recommended system RAM estimate | 30 GB |
| Suggested free disk before download | More than 10.2 GiB; includes the runtime fit-check margin, excludes unrelated app/storage needs |
| CPU | Compatible installed inference backend; actual performance must be measured |
| GPU | Optional; partial offload depends on backend, drivers, free VRAM and context |
| Catalog license identifier | `apache-2.0`; applicable artifact terms govern use |

System RAM and GPU VRAM are separate resources. These RAM values are catalog estimates, not measurements or guarantees. Context buffers, concurrent roles and other apps increase memory demand. A 4 GB GPU does not make every model runnable; sufficient system RAM and a compatible engine remain necessary.

## Intended workflow

Supply the goal, relevant source facts, audience, constraints and desired format. The OYYO workspace can prepare the task-specific brief and select an eligible model. A catalog listing describes an option; readiness requires successful qualification and acceptance on the relevant device.

**Available for private demos and private beta. [Request early access](https://oyyo.one/contact).**

## Limits and verification

Higher memory and latency costs. Larger size is not evidence of better performance on a particular task.

This is a text model. It does not by itself generate images/video, transcribe audio, browse the web, execute code, publish posts or export documents. Those features require the corresponding OYYO tool, speech pack or connected service. Output length and supplied context are controlled by runtime settings; a maximum usable context is not certified in this registry.

OYYO names identify product configurations. They do not assert that the underlying weights were originally trained by OYYO. Required rights, attribution and provenance records remain applicable; see [licensing](../LICENSE.md) and [provenance policy](../provenance/README.md).

## Artifact integrity

`SHA-256: 500a8806e85ee9c83f3ae08420295592451379b4f8cf2d0f41c15dffeb6b81f0`

A hash identifies the configured artifact; it is not a quality score. Changing the artifact or inference implementation can require requalification. See [qualification](../docs/QUALIFICATION.md), [hardware](../docs/HARDWARE.md) and [routing](../docs/ROUTING.md).

Copyright © 2026 OYYO · HRN INNOVATION TECHNOLOGIES LTD. All rights reserved.
