# Changelog

## v1.1.4-rc1 — 2026-10-31

Shared-site privacy corrective release candidate.

### Fixed
- On `*.github.io`, entries stay in the open tab instead of browser storage, because every project site on that host shares one storage origin.
- A record autosaved by v1.1.3-rc1 on the website is moved into the tab, removed from shared storage, and flagged **Not saved — export to keep**.
- The privacy notice now describes both the website and a downloaded copy.
- The mobile **Review & Complete** button's accessible name now starts with its visible label.
- Browser regression covers the shared-site mode by serving the page under a `github.io` hostname; the live check expects session-only behavior.

## v1.1.3-rc1 — 2026-10-30

Privacy and data-loss corrective release candidate.

### Fixed
- Warns before leaving local/session-only work containing edits not exported since the last change.
- Action bar shows **Not saved — export to keep** while session-only work is dirty.
- JSON and Markdown export clear the dirty warning state.
- Local-file startup removes earlier-version localStorage records without hydrating them.
- Reset clears compatible legacy keys from real localStorage even in session-only mode.
- Loading a sample scenario asks before replacing custom trigger or obscuration text.
- Required-field errors expose `aria-invalid` and `aria-describedby`, and those attributes clear when corrected.
- Direct-file browser regression coverage now includes unload warning, legacy cleanup, scenario confirmation, and error semantics.

## v1.1.2-rc1 — 2026-10-30

UX and distribution corrective release candidate. Added release-specific checksums, integrity CI, complete exports, visible validation errors, storage fallback, local-file session privacy, explicit clarity rating, mobile completion access, and release freshness checks.

## v1.1.1-rc1 — 2026-10-30

Corrective pilot candidate. Added substantive completion requirements, self-attested completion labeling, local-only consent clarification, localStorage privacy warning, session-level evidence labels, ASCII-safe exports, and pilot-candidate status.

## v1.1.0 — superseded
Added real-life engineering layer, scenario launcher, validation lab, clarity delta, Markdown export, and migration support.

## v1.0.0 — superseded
Initial single-file seven-chamber Theta-7 interface.
