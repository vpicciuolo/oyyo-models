# Choose a model for your computer

Start with the RAM available to OYYO, the work you want to do and a small representative task. A larger download does not automatically provide a better experience.

## A practical starting point

| Total system RAM | Starting candidates | Guidance |
| --- | --- | --- |
| 4 GB | Pocket 2.0 | Catalog minimum only. Operating-system and app memory can leave too little free RAM; close other apps and use short requests. |
| 6 GB | Pocket 2.0; evaluate Spark 2.0 or Swift 3.0 | Start with the smallest candidate. Keep one model resident. |
| 8 GB | Nano 1.0, Nano 2.0, Focus Mini 1.0 at their minimum estimates | Minimum is not recommended headroom. Prefer a smaller option when the machine is busy. |
| 12–16 GB | Core 1.0, Code 1.0, Reason 1.0; evaluate Core 2.0 at 16 GB | Read the recommended RAM column, not only the minimum. Test context length and latency. |
| 20–32 GB | Pro 1.0, Focus Pro 1.0, smaller options with more headroom | Longer prompts and multiple resident models can still consume the available memory. |
| 40–64+ GB | Evaluate Pro 3.0 or Team 3.0 | Verify the exact backend supports the architecture. More RAM does not remove compatibility checks. |

These are catalog-based starting points. No entry certifies a particular CPU, laptop or operating system. The recommended minimum for one model is not the memory requirement for several models at once.

## CPU and GPU

**CPU inference** uses system RAM and a compatible inference engine. Performance depends on the CPU, supported instructions, memory bandwidth, threads and prompt size. This registry publishes no universal tokens-per-second estimate.

**GPU acceleration** requires a compatible installed engine, drivers and a supported device. GPU presence alone does not enable acceleration. GPU VRAM is not system RAM. Context/KV buffers, working allocations and other apps consume memory beyond the weight file size.

**Partial offload** can keep part of a model in system RAM and place supported layers on the GPU. The GPU does not always need to hold all weights, but the computer must still have enough memory overall. The current runtime exposes configurable layer/device settings; it does not prove that any model can run on any computer.

A **4 GB VRAM** machine can evaluate smaller models or a supported CPU/GPU split when system RAM is sufficient. It cannot be promised to run every model. Neither quantization nor incremental offload removes the need for real memory and compatibility.

## What the Windows fit check means

The current fit estimate checks total system RAM against the catalog minimum and requires free disk greater than `weight size × 1.1 + 1 GiB`. It also warns when free system memory is below the minimum estimate. The GPU-fit heuristic compares detected VRAM with weight size plus a margin; it is a rough indication, not a measured execution guarantee.

Download space, model residency and generation buffers are different allocations. Leave extra space for application updates, documents, meeting audio and any retained model packages.

## Keep the experience responsive

- Start with one job and one resident model on modest hardware.
- Use short, relevant source excerpts instead of attaching an entire repository to a greeting.
- Choose the smallest qualified model that produces acceptable results on your task.
- Increase context, answer length or concurrency only when the machine has headroom.
- Measure time to first output and total completion on real requests. A multi-role workflow can involve several inference passes even when it uses one model.
- Benchmark again after changing the model artifact or inference implementation as required by the runtime.

The Windows runtime and Mac installation feeds have separate baselines. Apple unified memory is not an additional pool of discrete GPU VRAM. Metal, NPU and other accelerator claims need their own build and device evidence; do not infer them from this Windows catalog.

[Full lineup](../README.md#local-text-lineup) · [Qualification](QUALIFICATION.md)
