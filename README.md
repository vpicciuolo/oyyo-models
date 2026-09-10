<div align="center">

# OYYO Models

### Model registry, compatibility metadata, provenance and qualification records for the OYYO AI ecosystem

**Portable AI · Model Qualification · Provenance · Compatibility · Model Cards · Hardware Profiles · Reproducibility**

[OYYO](https://oyyo.one) · [Benchmark](https://github.com/vpicciuolo/oyyo-benchmark) · [SDK](https://github.com/vpicciuolo/oyyo-sdk) · [Release Gate](./docs/RELEASE_GATE.md) · [Founder](https://github.com/vpicciuolo) · [Investors](https://oyyo.one/investors)

**Version:** `0.1.0-foundation` · **Made in UAE 🇦🇪 · Dubai-IT**

</div>

> [!IMPORTANT]
> **OYYO is proprietary technology and is not open source.** This repository is public to expose selected model metadata, compatibility information, provenance records and qualification rules. Public repository visibility does not grant rights to OYYO's private runtime, orchestration engine, proprietary models or other intellectual property.

## What is OYYO Models?

OYYO Models is the public registry layer for model artifacts that are evaluated for use within the OYYO ecosystem.

Its purpose is not to collect models simply because they are popular. It is designed to record **what a model is, where it came from, what license applies, how it was transformed, what hardware it supports, how it performed under OYYO Benchmark, and whether it passed the OYYO release gate**.

The repository separates marketing claims from verifiable model identity and release evidence.

## OYYO model philosophy

A third-party or internally developed model does **not** become an official OYYO model because it has a high leaderboard score, a large download count or a well-known name.

An official release must satisfy the OYYO qualification process, including:

1. exact upstream identity and revision
2. license and redistribution review
3. artifact checksums and provenance
4. intended CPU portability testing
5. target accelerator testing where claimed
6. OYYO Benchmark qualification
7. malformed-input, security and reliability testing
8. a published model card with known limitations
9. human acceptance review

See the full **[Official Model Release Gate](./docs/RELEASE_GATE.md)**.

## Planned OYYO model family

The following names define the intended OYYO product tiers. They do **not** mean that model weights for every tier are already released.

| Tier | Intended role |
| --- | --- |
| **OYYO Nano** | Ultra-light local and edge tier |
| **OYYO Mini** | Compact everyday local tier |
| **OYYO Core** | Primary general portable tier |
| **OYYO Code** | Coding and technical execution specialist |
| **OYYO Vision** | Vision and multimodal specialist |
| **OYYO Growth** | Business, research, marketing and growth specialist |
| **OYYO Max** | Larger high-performance tier |

Naming conventions are documented in **[`docs/NAMING.md`](./docs/NAMING.md)**.

## What this repository records

### Model manifests

Machine-readable model package metadata is defined under [`schemas/`](./schemas/). A manifest can describe model identity, tier, source, artifact format, quantization, hashes, requirements and compatibility information.

### Compatibility profiles

[`compatibility/`](./compatibility/) records supported or evaluated runtime and hardware backends. OYYO's portability goals require model selection to consider real memory, CPU/GPU/NPU and runtime constraints rather than parameter count alone.

### Model cards

[`model-cards/`](./model-cards/) contains official OYYO model cards only after a candidate has passed the release gate. Model cards are intended to capture capabilities, limitations, intended use, evaluation context and release-specific facts.

### Provenance

[`provenance/`](./provenance/) records upstream identity, exact revision, licensing, conversion or fine-tuning lineage, quantization, checksums, build information where material, benchmark version and release date.

## Example manifest

The foundation repository includes an example manifest at:

[`examples/oyyo-mini.example.json`](./examples/oyyo-mini.example.json)

It demonstrates the metadata format only. An example manifest is **not** an official model release.

## Relationship with OYYO Benchmark

OYYO Models and OYYO Benchmark are deliberately separate.

```text
Candidate model
      ↓
Identity + license + provenance
      ↓
Compatibility validation
      ↓
OYYO Benchmark
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
├── provenance/     Source lineage, licenses and checksums
├── schemas/        Machine-readable manifest schemas
└── VERSION         Registry version
```

## OYYO public engineering ecosystem

| Repository | Purpose |
| --- | --- |
| **[oyyo-models](https://github.com/vpicciuolo/oyyo-models)** | Model manifests, compatibility metadata, model cards, provenance and release-gate records |
| **[oyyo-benchmark](https://github.com/vpicciuolo/oyyo-benchmark)** | Independent evaluation, qualification methodology and reproducible metrics |
| **[oyyo-sdk](https://github.com/vpicciuolo/oyyo-sdk)** | Python and TypeScript integration surface for OYYO-compatible and OYYO-native APIs |

The **OYYO core runtime and orchestration engine remain private and proprietary**.

## What is OYYO?

OYYO is being built as a **proprietary AI orchestration system for modern business**, designed to coordinate models, tools, memory, agents, multimodal capabilities and structured work through a portable runtime architecture.

The model layer is only one part of OYYO. The system is designed so model choice can evolve while orchestration, memory, tools, artifacts, business workflows and hardware-aware execution remain part of a larger architecture.

Learn more at **[oyyo.one](https://oyyo.one)**.

## Licensing and model rights

There are two separate questions:

1. **OYYO platform rights**: OYYO is proprietary technology and is not open source.
2. **Individual model rights**: upstream or derived model artifacts can have their own licenses and redistribution terms. No model license should be inferred from the visibility of this repository.

Every official model release must carry explicit provenance and applicable licensing information.

## Status

This repository is currently at the **foundation stage (`0.1.0`)**. The registry structure, manifest schema and release-gate process are being established before official model families are promoted.

## Ownership and rights

**Copyright © 2026 OYYO · HRN INNOVATION TECHNOLOGIES LTD. All rights reserved.**

OYYO is proprietary technology. Unless an individual file or third-party artifact explicitly states otherwise, no license to use, copy, modify, distribute, sublicense or create derivative works is granted merely because material is visible in this public repository.

---

<div align="center">

**OYYO · AI orchestration for real work · Made in UAE 🇦🇪 · Dubai-IT**

[Website](https://oyyo.one) · [Benchmark](https://github.com/vpicciuolo/oyyo-benchmark) · [SDK](https://github.com/vpicciuolo/oyyo-sdk) · [Founder](https://github.com/vpicciuolo)

</div>
