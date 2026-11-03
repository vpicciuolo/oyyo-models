# OYYO Spark 2.0

**Short content and language drafts** · Local text-model candidate

A compact writing and translation candidate for email drafts, short social copy and language adaptation. Specify audience, tone and the language you want.

## Suitable requests

Capabilities in the runtime catalog: chat, writing, translation. These are routing labels and intended tasks, not independent benchmark results. Provide the source facts, audience, constraints and desired format; OYYO can prepare a role-specific prompt.

> Write three short product announcements in English and Italian using only the facts in this brief.

## Requirements

| Item | Catalog information |
| --- | --- |
| Package ID | `oyyo-spark-2.0-q4` |
| Parameter class | 2 billion; architecture-dependent, not a memory estimate |
| Weight download | 1.28 GB (1,280,835,840 bytes) |
| Artifact | GGUF · Q4_K_M |
| Minimum system RAM estimate | 6 GB |
| Recommended system RAM estimate | 9 GB |
| Suggested free disk before download | More than 2.3 GiB; includes the runtime fit-check margin, excludes unrelated app/storage needs |
| CPU | Compatible installed inference backend; actual performance must be measured |
| GPU | Optional; partial offload depends on backend, drivers, free VRAM and context |
| Catalog license identifier | `apache-2.0`; applicable artifact terms govern use |

System RAM and GPU VRAM are separate resources. These RAM values are catalog estimates, not measurements or guarantees. Context buffers, concurrent roles and other apps increase memory demand. A 4 GB GPU does not make every model runnable; sufficient system RAM and a compatible engine remain necessary.

## Intended workflow

Supply the goal, relevant source facts, audience, constraints and desired format. The OYYO workspace can prepare the task-specific brief and select an eligible model. A catalog listing describes an option; readiness requires successful qualification and acceptance on the relevant device.

**Available for private demos and private beta. [Request early access](https://oyyo.one/contact).**

## Limits and verification

Language coverage and translation quality require representative tests. Review proper names and specialised terminology.

This is a text model. It does not by itself generate images/video, transcribe audio, browse the web, execute code, publish posts or export documents. Those features require the corresponding OYYO tool, speech pack or connected service. Output length and supplied context are controlled by runtime settings; a maximum usable context is not certified in this registry.

OYYO names identify product configurations. They do not assert that the underlying weights were originally trained by OYYO. Required rights, attribution and provenance records remain applicable; see [licensing](../LICENSE.md) and [provenance policy](../provenance/README.md).

## Artifact integrity

`SHA-256: aaf42c8b7c3cab2bf3d69c355048d4a0ee9973d48f16c731c0520ee914699223`

A hash identifies the configured artifact; it is not a quality score. Changing the artifact or inference implementation can require requalification. See [qualification](../docs/QUALIFICATION.md), [hardware](../docs/HARDWARE.md) and [routing](../docs/ROUTING.md).

Copyright © 2026 OYYO · HRN INNOVATION TECHNOLOGIES LTD. All rights reserved.
