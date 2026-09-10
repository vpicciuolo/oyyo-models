# OYYO Model Provenance

Traceable source, transformation, licensing and release lineage for models evaluated or released within the **OYYO proprietary AI ecosystem**.

> [!IMPORTANT]
> **OYYO is proprietary technology and is not open source.** Provenance records are published to make model identity and release evidence inspectable. Public provenance does not grant rights to OYYO technology or to any third-party model artifact.

## Why provenance matters

A model name is not enough to reproduce or trust an AI result. Different revisions, conversions, fine-tunes, quantizations and runtime builds can behave differently while still being described under the same family name.

OYYO therefore treats provenance as part of model qualification, not as optional documentation.

## Required release record

Every official OYYO model release should record, where applicable:

- upstream model identity
- exact upstream revision or commit
- source repository, registry or model identifier
- source URLs or canonical identifiers
- upstream license and redistribution conditions
- OYYO-specific rights or restrictions where applicable
- conversion lineage
- fine-tuning lineage
- quantization method and parameters
- artifact format
- cryptographic checksums
- build environment where material to reproducibility
- runtime/backend used for validation
- OYYO Benchmark version
- compatibility profile
- release date
- human review or approval state

## Qualification relationship

```text
Source identity
      ↓
License review
      ↓
Transformation lineage
      ↓
Checksums
      ↓
Compatibility validation
      ↓
OYYO Benchmark
      ↓
Model card
      ↓
Official release record
```

Provenance is one required part of the **[OYYO Official Model Release Gate](../docs/RELEASE_GATE.md)**.

## Related OYYO resources

- [OYYO Models](../README.md)
- [OYYO Model Cards](../model-cards/README.md)
- [Release gate](../docs/RELEASE_GATE.md)
- [OYYO Benchmark](https://github.com/vpicciuolo/oyyo-benchmark)
- [OYYO SDK](https://github.com/vpicciuolo/oyyo-sdk)
- [OYYO website](https://oyyo.one)

## Rights

Individual model artifacts may have licenses that differ from OYYO platform rights. The applicable rights must be established from the specific release record and upstream license; they must never be inferred from this repository being publicly visible.

**Copyright © 2026 OYYO · HRN INNOVATION TECHNOLOGIES LTD. All rights reserved.**
