# OYYO Model Cards

Official capability, evaluation, limitation and release records for models qualified for the **OYYO proprietary AI ecosystem**.

> [!IMPORTANT]
> **OYYO is not open source.** A public model card documents a model release; it does not grant rights to OYYO technology or override the explicit license attached to an individual model artifact.

## Purpose

An OYYO model card is published only after a candidate completes the OYYO qualification process. Model cards are intended to make release claims inspectable rather than relying on model names, popularity or vendor benchmark marketing.

An official card should document, where applicable:

- model and release identity
- intended OYYO tier and use cases
- upstream source and revision
- applicable license information
- architecture and artifact format
- quantization or conversion details
- supported runtime and hardware profiles
- OYYO Benchmark version and results
- business, coding, language, agent and multimodal capabilities tested
- security and reliability observations
- known limitations and unsupported scenarios
- checksums and provenance references
- release date and review status

## Release gate

A model card is not sufficient by itself to create an official OYYO release. Candidates must complete the **[OYYO Official Model Release Gate](../docs/RELEASE_GATE.md)** and relevant **[OYYO Benchmark](https://github.com/vpicciuolo/oyyo-benchmark)** evaluation.

```text
Candidate → Provenance → Compatibility → Benchmark → Reliability → Human Review → Model Card → Release
```

## Current status

At foundation version `0.1.0`, this directory defines the location and policy for future official OYYO model cards. Product-tier names in the repository are roadmap identifiers and should not be interpreted as proof that weights are already released.

## Related OYYO resources

- [OYYO Models](../README.md)
- [Provenance records](../provenance/README.md)
- [Release gate](../docs/RELEASE_GATE.md)
- [OYYO Benchmark](https://github.com/vpicciuolo/oyyo-benchmark)
- [OYYO SDK](https://github.com/vpicciuolo/oyyo-sdk)
- [OYYO website](https://oyyo.one)

**Copyright © 2026 OYYO · HRN INNOVATION TECHNOLOGIES LTD. All rights reserved.**
