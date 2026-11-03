# OYYO-NotzUP-Tiny ALL S1–S4

**Local meeting speech-to-text** · Optional speech pack

Tiny ALL converts a supported meeting audio clip into editable timestamped text. A separate qualified local text model handles summaries, decisions, action items and translation. It is not a general chat or image model.

| Item | Configuration |
| --- | --- |
| Model identifier | `OYYO-NotzUP-Tiny-ALL` |
| Presentation revision | `20260000-1` |
| Weight download | 77,691,713 bytes · approximately 77.7 MB |
| SHA-256 | `be07e048e1e599ad46341c8d2a135645097a538221678b7acdd1b1919c6e1b21` |
| License | MIT; retain applicable attribution and notices |
| Execution in this Windows build | Local speech engine on CPU; a GPU requirement is not asserted |
| Pack memory | No independently measured universal minimum published here; include application, audio and local text-model memory |
| Capture/import limit | 115 seconds per clip in the current Windows beta |
| Quality gate | Pinned engine/model/fixture integrity plus one clean English recognition fixture |

## What S1–S4 means

The four labels use **the same speech weights**, selected by the desktop-compatible device profile. They are not four downloads or four accuracy levels.

| Tier | Device-profile threshold |
| --- | --- |
| S4 | At least 12 available threads and at least 500 MiB/s in the profile benchmark |
| S3 | Otherwise, at least 8 threads and at least 250 MiB/s |
| S2 | Otherwise, at least 4 threads and at least 100 MiB/s |
| S1 | Other measured configurations |

The profile hashes an 8 MiB buffer four times with a round prefix, then uses 32 MiB divided by measured elapsed time with a 1 ms floor. This mirrors the verified desktop tier rules; it does not establish native mobile feature parity or measured transcription speed.

## Meeting workflow

1. Open **More → NotzUp** and set up/check the speech pack if needed.
2. Record or import a supported short clip, or create a note from text.
3. Review the transcript, edit recognition mistakes and add speaker labels where known.
4. Generate the local summary, decisions and action items using an accepted local text model. Unknown owners or deadlines remain unspecified.
5. Translate, search your note library or export through the available document actions.

Meeting and note processing stays under the local-only policy in the Windows 0.1.14 baseline even if connected assistance is enabled elsewhere. Existing historic connected results must not be relabelled as locally produced; regenerate them locally when needed.

## Limits

The English fixture does not certify multilingual, mixed-language, noisy-room or accent performance. Automatic speaker identity/diarisation and long-recording parity are not established in this web beta. A manually entered speaker name is not biometric identification. A small weight file is not the total app memory footprint.

Blueprints, company projects and other general-purpose workflows belong in OYYO's task library rather than the meeting-focused NotzUp surface.

[Qualification](../docs/QUALIFICATION.md) · [Rights](../LICENSE.md)

Copyright © 2026 OYYO · HRN INNOVATION TECHNOLOGIES LTD. All rights reserved.
