# OYYO Pro 3.0

**Large-machine reasoning candidate** · Local text-model candidate

A larger catalog candidate for detailed reasoning and technical work on well-provisioned machines. Evaluate it against a representative task before assigning important workloads.

## Suitable requests

Capabilities in the runtime catalog: chat, reasoning, coding. These are routing labels and intended tasks, not independent benchmark results. Provide the source facts, audience, constraints and desired format; OYYO can prepare a role-specific prompt.

> Produce a detailed technical decision memo from these specifications, with trade-offs, risks and validation criteria.

## Requirements

| Item | Catalog information |
| --- | --- |
| Package ID | `oyyo-pro-3.0-q4` |
| Parameter class | 27 billion; architecture-dependent, not a memory estimate |
| Weight download | 16.46 GB (16,464,440,224 bytes) |
| Artifact | GGUF · Q4_K_M |
| Minimum system RAM estimate | 40 GB |
| Recommended system RAM estimate | 60 GB |
| Suggested free disk before download | More than 17.9 GiB; includes the runtime fit-check margin, excludes unrelated app/storage needs |
| CPU | Compatible installed inference backend; actual performance must be measured |
| GPU | Optional; partial offload depends on backend, drivers, free VRAM and context |
| Catalog license identifier | `apache-2.0`; applicable artifact terms govern use |

System RAM and GPU VRAM are separate resources. These RAM values are catalog estimates, not measurements or guarantees. Context buffers, concurrent roles and other apps increase memory demand. A 4 GB GPU does not make every model runnable; sufficient system RAM and a compatible engine remain necessary.

## Intended workflow

Supply the goal, relevant source facts, audience, constraints and desired format. The OYYO workspace can prepare the task-specific brief and select an eligible model. A catalog listing describes an option; readiness requires successful qualification and acceptance on the relevant device.

**Available for private demos and private beta. [Request early access](https://oyyo.one/contact).**

## Limits and verification

Engine compatibility and quality are unverified until local checks complete. The download alone does not establish that this build can run it.

This is a text model. It does not by itself generate images/video, transcribe audio, browse the web, execute code, publish posts or export documents. Those features require the corresponding OYYO tool, speech pack or connected service. Output length and supplied context are controlled by runtime settings; a maximum usable context is not certified in this registry.

OYYO names identify product configurations. They do not assert that the underlying weights were originally trained by OYYO. Required rights, attribution and provenance records remain applicable; see [licensing](../LICENSE.md) and [provenance policy](../provenance/README.md).

## Artifact integrity

`SHA-256: 322e194ff79741c7baa497c240f677f54b201b0efab44ca8e50f122b39123482`

A hash identifies the configured artifact; it is not a quality score. Changing the artifact or inference implementation can require requalification. See [qualification](../docs/QUALIFICATION.md), [hardware](../docs/HARDWARE.md) and [routing](../docs/ROUTING.md).

Copyright © 2026 OYYO · HRN INNOVATION TECHNOLOGIES LTD. All rights reserved.
