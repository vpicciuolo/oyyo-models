# OYYO Models

Public metadata, manifests, provenance, compatibility profiles and distribution support for free portable OYYO models.

**Project:** https://oyyo.one  
**Version:** `0.1.0-foundation`

## Principle

No third-party base model becomes an official OYYO model only because it is popular or scores well on vendor benchmarks. Official model releases must pass OYYO Benchmark qualification, licensing review, compatibility validation and reproducibility checks.

## Planned model family

- **OYYO Nano** — ultra-light local tier
- **OYYO Mini** — compact everyday local tier
- **OYYO Core** — primary general portable tier
- **OYYO Code** — coding specialist
- **OYYO Vision** — multimodal specialist
- **OYYO Growth** — growth/business specialist
- **OYYO Max** — larger high-performance local tier

These are product tier names, not declarations that model weights already exist.

## Repository contents

- `schemas/` — machine-readable package/manifest formats
- `examples/` — example manifests only
- `compatibility/` — hardware/backend compatibility data
- `model-cards/` — official model cards when models qualify
- `provenance/` — checksums and source lineage

Large weights should live on model hosting/release storage, not ordinary Git history.
