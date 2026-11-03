# Qualification and readiness

The public catalog records options. Readiness is a property of an exact artifact, an inference implementation, a device and the checks actually run.

| State | Meaning |
| --- | --- |
| Listed | A catalog entry exists. No execution claim follows. |
| Downloaded | Bytes are present. This alone says nothing about compatibility or answer quality. |
| Integrity verified | Bytes match the pinned artifact hash. A hash is not a capability score. |
| Qualified locally | The current local suite passed for that artifact and inference setup. The suite has a limited scope. |
| Accepted / ready | The runtime acceptance gate permits use on this installation. |
| Needs setup / failed | The option is unavailable until the actual issue is resolved and the required check succeeds. |

## Local text-model checks

The Windows pilot validates responses through a small local qualification suite before accepting a model. The runtime binds qualification to the artifact identity and inference fingerprint. Failed checks must not be relabelled as passes, accepted through lower thresholds or replaced by fabricated results.

The public catalog does **not** publish a score for every model or claim that every download candidate passed on every device. Capability tags are routing metadata. “Coding”, “math” or “multilingual” is not an independently measured accuracy percentage.

Use representative tasks for the work you care about: writing with strict facts, code with executable tests, calculations with known totals, translation reviewed by a competent speaker and retrieval against known source material. Record hardware, backend, prompt, settings and timing when publishing comparisons.

## Speech checks

The NotzUp speech setup checks the pinned speech-engine binary, model bytes and benchmark audio fixture, then tests recognition of one clean English meeting fixture. That is not a certification for every language, accent, noisy room, microphone or speaker-identification scenario.

The S1–S4 device profile is a short CPU hash-throughput and thread-count benchmark. It is separate from ASR quality qualification, not a speech accuracy score and not a different model download.

## Broader official release gate

The [official model release gate](RELEASE_GATE.md) describes the broader provenance, rights, compatibility, reliability, benchmark and review process. Candidate cards in this snapshot are informational catalog cards; they do not assert that every candidate completed that broader process.

[OYYO Benchmark](https://github.com/vpicciuolo/oyyo-benchmark) contains the separate public methodology repository. Do not imply it has evaluated a package unless an actual corresponding result exists.
