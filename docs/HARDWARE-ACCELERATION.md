# CPU, GPU and adaptive memory

The Windows 0.1.16 catalog contains 15 local text candidates with CPU and GPU acceleration support. Four pinned candidates are marked compatible with the adaptive engine: Nano 1.0, Core 1.0, Pro 1.0 and Team 3.0. Compatibility is distinct from successful local qualification.

| Selection | Meaning |
| --- | --- |
| CPU | Local inference with system RAM |
| GPU acceleration | Full or partial GPU offload; remaining layers can use CPU and RAM |
| CPU + GPU | Mixed placement with a supported accelerator and installed backend |
| Fits entirely in VRAM | A separate estimate using currently free VRAM and memory reserve |
| Adaptive streaming | Engine-compatible candidates; dense models still need resident RAM, while supported expert models can tier expert data across storage, RAM and GPU |

A GPU inference smoke test on an NVIDIA RTX A500 Laptop GPU placed 246 dense matrices on CUDA, with 1.93 GB VRAM reported in the engine log. This is evidence of that particular GPU run, not a large-model benchmark or a quality qualification. Large expert-model candidates remain subject to resource planning, download integrity, native-backend support and the full quality gate.

macOS builds use their native backend and unified-memory accounting. Windows VRAM estimates and CUDA results must not be represented as Mac qualification results. Native build acceptance is verified separately. macOS ARM64 0.1.16 verified Apple M2 Metal inference with 25/25 layers offloaded. Adaptive expert streaming is unavailable on macOS 14 in this release; the current native package uses standard CPU/Metal placement instead.

[OYYO ONE AI documentation hub](https://github.com/vpicciuolo/oyyo-one-ai) · [OYYO website](https://oyyo.one) · [Exclusive preview](https://oyyo.one/contact#exclusive-preview)

Copyright © 2026 OYYO · HRN INNOVATION TECHNOLOGIES LTD. All rights reserved.
