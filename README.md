<div align="center">

# OYYO Models

### Native OYYO model family, model registry, compatibility metadata, provenance and qualification records for the OYYO AI ecosystem

**Native AI · Portable AI · Model Qualification · Provenance · Compatibility · Hardware Profiles · Reproducibility**

[OYYO](https://oyyo.one) · [Benchmark](https://github.com/vpicciuolo/oyyo-benchmark) · [SDK](https://github.com/vpicciuolo/oyyo-sdk) · [Release Gate](./docs/RELEASE_GATE.md) · [Founder](https://github.com/vpicciuolo) · [Investors](https://oyyo.one/investors)

**Version:** `0.1.0-foundation` · **Made in UAE 🇦🇪 · Dubai-IT**

</div>

> [!IMPORTANT]
> **OYYO is proprietary technology and is not open source.** This repository is public to expose selected model metadata, compatibility information, provenance records and qualification rules. Public repository visibility does not grant rights to OYYO's private runtime, orchestration engine, proprietary models, model-development methods or other intellectual property.

## What is OYYO Models?

OYYO Models is the public registry and qualification layer for the native OYYO model family and other model artifacts evaluated for use within the OYYO ecosystem.

OYYO is being engineered with its own proprietary native model family as a first-class foundation. OYYO-native models are intended to run both online/cloud and locally/offline on compatible hardware. OYYO can operate independently using its native models while its intelligence fabric can also work with additional local/offline models and external cloud providers when useful.

The purpose of this repository is not to collect models simply because they are popular. It records **what a model is, where it came from, what rights and provenance apply, how it was transformed, what hardware it supports, how it performed under OYYO Benchmark, and whether it passed the OYYO release gate**.

The repository separates marketing claims from verifiable model identity and release evidence.

## OYYO model philosophy

An official OYYO model is not defined by leaderboard position, download count or a well-known upstream name.

Every official OYYO-native or qualified model release must satisfy the OYYO qualification process, including:

1. exact identity, architecture and revision
2. license/rights and provenance review
3. artifact checksums and reproducible lineage
4. intended CPU portability testing
5. target accelerator testing where claimed
6. OYYO Benchmark qualification
7. malformed-input, security and reliability testing
8. quantization and capability-regression evaluation
9. a published model card with known limitations
10. human acceptance review

See the full **[Official Model Release Gate](./docs/RELEASE_GATE.md)**.

## Planned OYYO native model family

The following names define the intended OYYO product families. Parameter bands are engineering targets only and can change as benchmark, efficiency and deployment evidence improves. They do **not** mean that weights for every tier are already released.

| Tier | Indicative target class | Intended role |
| --- | ---: | --- |
| **OYYO Nano** | ~1–4B | Ultra-light local, mobile and edge tier |
| **OYYO Mini** | ~7–9B | Compact everyday local tier |
| **OYYO Core** | ~14–32B | Primary general professional OYYO intelligence |
| **OYYO Max** | ~70B class and/or efficient MoE | High-performance workstation, enterprise and cloud tier |
| **OYYO Code** | Specialist variants | Coding and technical execution |
| **OYYO Vision** | Specialist/multimodal variants | Vision, screenshot, image and document intelligence |
| **OYYO Growth** | Specialist variants | Business, research, marketing and growth workflows |

OYYO model engineering prioritizes **capability per GB of memory, per watt, per unit of latency and per serving cost**, not parameter count alone.

Naming conventions are documented in **[`docs/NAMING.md`](./docs/NAMING.md)**.

## Native model development direction

OYYO evaluates the strongest capabilities available across contemporary model families and develops its own model family through independently controlled and legally permitted engineering paths, including architecture research, original and licensed datasets, synthetic data, fine-tuning, distillation where permitted, preference/reinforcement methods, tool-use training, multimodal work and OYYO-specific evaluation.

The objective is not to clone one provider. The objective is to build proprietary OYYO intelligence optimized for OYYO's runtime, memory, agents, tools, real business work and broad hardware compatibility.

## Online, offline and collaborative execution

OYYO-native models are designed around three execution realities:

```text
OYYO Cloud
  └─ OYYO-native hosted models

OYYO Local / Offline
  └─ OYYO-native models on compatible user hardware

OYYO Intelligence Fabric
  ├─ OYYO-native models
  ├─ additional local/offline models
  └─ external cloud models when enabled and useful
```

The core OYYO experience must not depend on the continuing availability of any external model provider.

## What this repository records

### Model manifests

Machine-readable model package metadata is defined under [`schemas/`](./schemas/). A manifest can describe model identity, tier, source, artifact format, quantization, hashes, requirements and compatibility information.

### Compatibility profiles

[`compatibility/`](./compatibility/) records supported or evaluated runtime and hardware backends. OYYO's portability goals require model selection to consider real memory, CPU/GPU/NPU and runtime constraints rather than parameter count alone.

### Model cards

[`model-cards/`](./model-cards/) contains official OYYO model cards only after a candidate has passed the release gate. Model cards are intended to capture capabilities, limitations, intended use, evaluation context and release-specific facts.

### Provenance

[`provenance/`](./provenance/) records identity, exact revision, applicable rights/licensing, conversion or training lineage where publishable, quantization, checksums, build information where material, benchmark version and release date.

## Example manifest

The foundation repository includes an example manifest at:

[`examples/oyyo-mini.example.json`](./examples/oyyo-mini.example.json)

It demonstrates the metadata format only. An example manifest is **not** an official model release.

## Relationship with OYYO Benchmark

OYYO Models and OYYO Benchmark are deliberately separate but developed in parallel with the private OYYO Core Runtime.

```text
OYYO model candidate
      ↓
Identity + rights + provenance
      ↓
Compatibility validation
      ↓
OYYO Benchmark
      ↓
Runtime + hardware qualification
      ↓
Security + reliability checks
      ↓
Human acceptance review
      ↓
Official OYYO model record
```

Benchmark methodology and reproducible evaluation live in **[oyyo-benchmark](https://github.com/vpicciuolo/oyyo-benchmark)**.

## Repository map

```text
oyyo-models/
├── compatibility/  Runtime and hardware compatibility metadata
├── docs/           Naming and release qualification rules
├── examples/       Example manifests
├── model-cards/    Official model cards after qualification
├── provenance/     Source lineage, rights/licenses and checksums
├── schemas/        Machine-readable manifest schemas
└── VERSION         Registry version
```

## OYYO public engineering ecosystem

| Repository | Purpose |
| --- | --- |
| **[oyyo-models](https://github.com/vpicciuolo/oyyo-models)** | Native model family records, manifests, compatibility metadata, model cards, provenance and release-gate records |
| **[oyyo-benchmark](https://github.com/vpicciuolo/oyyo-benchmark)** | Independent evaluation, qualification methodology and reproducible metrics |
| **[oyyo-sdk](https://github.com/vpicciuolo/oyyo-sdk)** | Python and TypeScript integration surface for OYYO-native and OYYO-compatible APIs |

The **OYYO core runtime, orchestration/intelligence fabric and proprietary model-development internals remain private and proprietary**.

## What is OYYO?

OYYO is a **proprietary AI platform with its own native AI model family**, built to provide one intelligent environment for modern work across local, offline, hybrid and cloud deployment.

The platform combines OYYO-native models, hardware-adaptive runtime execution, persistent memory and knowledge, tools, agents, multimodal capabilities and structured work. Its orchestration layer can additionally coordinate other local and cloud models, but OYYO is designed to operate independently with its own models.

**One intelligence. One workspace. One place for everything.**

Learn more at **[oyyo.one](https://oyyo.one)**.

## Commercial model

OYYO is designed around predictable monthly plans based on product tier and users/seats. OYYO does not position customer access around a falling token or credit balance. Compute/token accounting may be used internally for engineering and operations, but it is not the core customer billing experience.

## Policy profiles

The public OYYO Cloud service follows OYYO's centrally defined public-cloud policy. Organization deployments can apply organization/user policy profiles. Local/offline products may expose configurable user policy profiles where product configuration and applicable requirements permit.

## Licensing and model rights

There are two separate questions:

1. **OYYO platform/model rights**: OYYO platform technology and OYYO proprietary models are not open source unless OYYO explicitly states otherwise for a specific artifact.
2. **Third-party model rights**: upstream or derived third-party artifacts can have their own licenses and redistribution terms. No model license should be inferred from repository visibility.

Every official model release must carry explicit provenance and applicable rights/licensing information.

## Status

This repository is currently at the **foundation stage (`0.1.0`)**. The model registry, native-family architecture targets, manifest schema and release-gate process are being established as the OYYO Native Models program runs in parallel with OYYO Benchmark and OYYO Core Runtime.

## Ownership and rights

**Copyright © 2026 OYYO · HRN INNOVATION TECHNOLOGIES LTD. All rights reserved.**

OYYO is proprietary technology. Unless an individual file or third-party artifact explicitly states otherwise, no license to use, copy, modify, distribute, sublicense or create derivative works is granted merely because material is visible in this public repository.

---

<div align="center">

**OYYO · One intelligence. One workspace. One place for everything. · Made in UAE 🇦🇪 · Dubai-IT**

[Website](https://oyyo.one) · [Benchmark](https://github.com/vpicciuolo/oyyo-benchmark) · [SDK](https://github.com/vpicciuolo/oyyo-sdk) · [Founder](https://github.com/vpicciuolo)

</div>
