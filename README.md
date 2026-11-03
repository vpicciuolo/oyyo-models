<div align="center">

# OYYO Models

### Find the right OYYO model for the work you want to do.

**Everyday assistance · Writing · Coding · Analysis · Mathematics · Local meetings**

[Choose a model](#choose-by-task) · [Full lineup](#local-text-lineup) · [Hardware guide](docs/HARDWARE.md) · [Request early access](https://oyyo.one/contact)

**Catalog 0.1.14 · Snapshot: 3 November 2026**

**Available for private demos and private beta. [Request early access](https://oyyo.one/contact).**

</div>

OYYO combines models, task-specific prompts, persistent memory and specialist agent roles in one workspace. Start with a simple request; the runtime can select a qualified model and prepare instructions for the task. More demanding requests can be split into bounded specialist jobs, reviewed and assembled into one answer.

This repository documents the **15 local text-model candidates currently listed in the Windows runtime**, the NotzUp speech pack and the connected-model option. It contains descriptions and metadata, not model weights or a universal performance certificate. OYYO names are product configuration names; required artifact licenses and provenance remain applicable.

## Choose by task

| Your goal | Options to evaluate | What to provide |
| --- | --- | --- |
| Short replies on a small computer | Pocket 2.0, Spark 2.0, Swift 3.0 | A narrow question, language and length |
| Everyday writing and planning | Nano 1.0, Nano 2.0, Core 1.0 | Audience, facts, goal and output format |
| Marketing and content | Spark 2.0, Nano 1.0, Core 1.0 | Brand facts, channel, audience and call to action |
| Coding and debugging | Code 1.0, Core 2.0, Focus Mini 1.0 | Code, error, expected behaviour and tests |
| Maths and technical analysis | Reason 1.0, Focus Pro 1.0, Pro 1.0 | Inputs, units, constraints and verification criteria |
| Larger analytical workloads | Pro 3.0, Team 3.0, Focus Mini 2.0 | Structured source material and acceptance criteria |
| Meetings and notes | [NotzUp Tiny ALL S1–S4](model-cards/oyyo-notzup-tiny-all.md) + a qualified local text model | A short recording/transcript, then the desired notes or language |
| Optional connected assistance | [Prime S3 0.13](model-cards/oyyo-prime-s3-0.13.md) | An enabled connected account and task-relevant context |

These are starting points based on catalog capabilities, **not ranked benchmark winners**. Use device qualification and representative tasks to choose. Leaving OYYO on Auto avoids requiring an everyday user to select a model for each request.

## Local text lineup

RAM figures are estimates for system RAM. Download sizes use decimal GB. GPU memory is separate. Every option requires a compatible engine and local qualification before use.

| OYYO model | Specialization | Download | RAM minimum / recommended | Details |
| --- | --- | ---: | ---: | --- |
| **OYYO Nano 1.0** | Everyday writing and planning | 2.50 GB | 8 / 16 GB | [Model card](model-cards/oyyo-nano-1.0-q4.md) |
| **OYYO Core 1.0** | Balanced professional work | 5.03 GB | 12 / 18 GB | [Model card](model-cards/oyyo-core-1.0-q4.md) |
| **OYYO Pro 1.0** | Detailed analysis and technical planning | 9.00 GB | 20 / 30 GB | [Model card](model-cards/oyyo-pro-1.0-q4.md) |
| **OYYO Pocket 2.0** | Small-machine assistance | 0.53 GB | 4 / 6 GB | [Model card](model-cards/oyyo-pocket-2.0-q4.md) |
| **OYYO Spark 2.0** | Short content and language drafts | 1.28 GB | 6 / 9 GB | [Model card](model-cards/oyyo-spark-2.0-q4.md) |
| **OYYO Nano 2.0** | Compact planning and coding help | 2.74 GB | 8 / 12 GB | [Model card](model-cards/oyyo-nano-2.0-q4.md) |
| **OYYO Core 2.0** | Reasoning, analysis and code | 5.68 GB | 16 / 24 GB | [Model card](model-cards/oyyo-core-2.0-q4.md) |
| **OYYO Focus Mini 1.0** | Compact technical and multilingual work | 2.49 GB | 8 / 12 GB | [Model card](model-cards/oyyo-focus-mini-1.0-q4.md) |
| **OYYO Focus Pro 1.0** | Mathematics and detailed technical analysis | 8.89 GB | 20 / 30 GB | [Model card](model-cards/oyyo-focus-pro-1.0-q4.md) |
| **OYYO Code 1.0** | Coding, debugging and code review | 4.68 GB | 12 / 18 GB | [Model card](model-cards/oyyo-code-1.0-q4.md) |
| **OYYO Reason 1.0** | Multi-step reasoning and mathematics | 4.68 GB | 12 / 18 GB | [Model card](model-cards/oyyo-reason-1.0-q4.md) |
| **OYYO Pro 3.0** | Large-machine reasoning candidate | 16.46 GB | 40 / 60 GB | [Model card](model-cards/oyyo-pro-3.0-q4.md) |
| **OYYO Team 3.0** | Large multi-role workload candidate | 22.13 GB | 32 / 48 GB | [Model card](model-cards/oyyo-team-3.0-q4.md) |
| **OYYO Focus Mini 2.0** | Mid-size technical candidate | 4.99 GB | 12 / 18 GB | [Model card](model-cards/oyyo-focus-mini-2.0-q4.md) |
| **OYYO Swift 3.0** | Compact responsive-work candidate | 1.10 GB | 6 / 9 GB | [Model card](model-cards/oyyo-swift-3.0-q4.md) |

## Speech, connected assistance and creative work

| Option | Execution | Availability and requirements |
| --- | --- | --- |
| **OYYO-NotzUP-Tiny ALL S1–S4** | Local speech-to-text | Optional 77.7 MB speech pack, compatible speech engine and speech qualification. S1–S4 are device performance tiers using the same weights. Windows beta capture/import is limited to 115 seconds. |
| **OYYO Prime S3 0.13 · Connected model** | Connected account | Optional account-backed assistance; not an offline weight download. Connection, account access and applicable service limits are required. |
| **Images, video and vision** | Tool-dependent | Text models can prepare briefs, prompts and storyboards. This Windows catalog does not ship a qualified local image/video generation or vision model. Connected generation requires a separately available tool. |
| **PDF, Word and PowerPoint** | Document tools | Artifact creation is a runtime/tool capability, not a separate text-model family. Review exports before distribution. |

See the [capability boundaries](docs/CAPABILITIES.md) for voice, creative work, exports and company departments. Roadmap names such as standalone Vision, Growth or Max do not represent available weights in this catalog.

## Private access

**Available for private demos and private beta. [Request early access](https://oyyo.one/contact).**

Tell us about the work you want to improve, your department and the kind of demo you would like to see. Public catalogs describe capabilities; access and demonstrations are arranged privately.

## OYYO public catalogs

| Repository | Discover |
| --- | --- |
| [OYYO Models](https://github.com/vpicciuolo/oyyo-models) | Model lineup, specializations, requirements and capability guides |
| [OYYO Agents](https://github.com/vpicciuolo/oyyo-agents) | All 200 workspace agent roles, department coverage and specialist functions |
| [OYYO Teams](https://github.com/vpicciuolo/oyyo-teams) | Seven built-in workflow groups, collaboration, review and reusable configurations |
| [OYYO Task Library](https://github.com/vpicciuolo/oyyo-task-library) | 225 guided tasks, specialist briefs and 12 creative style options |
| [OYYO Benchmark](https://github.com/vpicciuolo/oyyo-benchmark) | Evaluation methodology, qualification and reproducibility |
| [OYYO SDK](https://github.com/vpicciuolo/oyyo-sdk) | Developer interfaces and integration documentation |

[Complete ecosystem index](docs/ECOSYSTEM.md)

## Learn more

| Guide | What you will find |
| --- | --- |
| [Model cards](model-cards/README.md) | Every candidate, examples, requirements, limitations and artifact identity |
| [Hardware](docs/HARDWARE.md) | CPU, GPU, RAM, VRAM, disk and low-memory choices |
| [Routing and teams](docs/ROUTING.md) | Task understanding, prompt preparation, multiple roles and models |
| [Practical examples](docs/USAGE.md) | Marketing, coding, finance, HR, research and meeting requests |
| [Qualification](docs/QUALIFICATION.md) | What a local check proves, what it does not and how acceptance works |
| [Capability boundaries](docs/CAPABILITIES.md) | Speech, images, video, vision, exports and automation |
| [Machine-readable catalog](catalog/models.json) | OYYO names, package IDs, capabilities and requirements |
| [Naming](docs/NAMING.md) · [Release gate](docs/RELEASE_GATE.md) | Product naming and the broader official-release process |

## Status and rights

The Windows runtime baseline for this snapshot is **0.1.14**. Operating-system builds have separate qualification baselines; a Windows model listing does not establish Mac or mobile qualification. No device-specific benchmark scores, global speed claims or completed foundation-model training are asserted here.

OYYO application technology is proprietary. Individual model artifacts retain their own terms. See [LICENSE.md](LICENSE.md) and the [provenance policy](provenance/README.md). Product aliases do not transfer ownership or remove attribution obligations. This catalog omits download-provider branding from the product selection tables; required license and provenance information remains with the applicable artifact records and distribution.

**Copyright © 2026 OYYO · HRN INNOVATION TECHNOLOGIES LTD. All rights reserved.**
