# Changelog

## v1.1.2-rc1 — 2026-10-30

UX and distribution corrective release candidate based on the reproduced V&V review.

### Fixed
- Release verification now uses `RELEASE_SHA256SUMS.txt`, which names the downloadable HTML asset directly.
- Added repository integrity tests so stale hashes fail CI.
- Release automation verifies an existing same-tag asset digest and fails on mismatch rather than silently leaving stale bytes published.
- Exported Markdown now includes all seven chambers, lesson, grounded return activity, and the current selected action.
- Missing required fields in collapsed chambers are opened, scrolled into view, and focused.
- Completion no longer fails when persistent browser storage is unavailable.
- Downloaded `file://` use is session-only by default to avoid shared local-file storage exposure.
- Clarity is not scored until before/after ratings are explicitly entered.
- Fixed desktop chamber chevron alignment, print-title visibility, mobile completion access, and sample-scenario switching.
- Compressed the embedded presentation artwork from PNG to WebP for the UI while preserving the original source PNG under `assets/`.

### Validation
- Added browser regression coverage for scenario switching, missing-field reveal, storage fallback, complete/export flow, clarity state, print title, desktop alignment, mobile affordance, overflow, and network isolation.

## v1.1.1-rc1 — 2026-10-30

Corrective pilot candidate derived from the full-chat V&V review.

### Changed
- Required substantive entries for present observation, obscuration, direct observation, unresolved uncertainty, grounded action, and retained lesson before completion.
- Completion label changed to self-attested sequence completion.
- Added local-only consent clarification.
- Added plaintext localStorage privacy warning.
- Reframed clarity deltas as session-level self-reported signals.
- Added ASCII-safe export filenames.
- Legacy v1.0 local-storage state is removed only after successful migration into the current key.
- Added explicit pilot-candidate status language.

## v1.1.0 — superseded
Added real-life engineering layer, scenario launcher, validation lab, clarity delta, Markdown export, and migration support.

## v1.0.0 — superseded
Initial single-file seven-chamber Theta-7 interface.
