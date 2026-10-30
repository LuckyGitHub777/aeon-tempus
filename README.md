# AEON-TEMPUS · Eclipse Node Theta-7

A symbolic, human-governed uncertainty-reflection and decision-support interface.

> **Status:** v1.1.2-rc1 — UX-corrective, technically verified pilot candidate.  
> **Evidence boundary:** this project does **not** establish a literal spacetime portal, extraterrestrial installation, temporal mechanism, or other paranormal/scientific claim.

## What it is

AEON-TEMPUS began as a mythic cosmology about eternity, time, memory, and civilization. This repository preserves that creative origin while engineering **Eclipse Node Theta-7** into a grounded seven-stage process:

**Presence → Obscuration → Reflection → Resonance → Reconciliation → Selection → Return**

The current single-file interface helps a user separate observation from interpretation, preserve uncertainty, select a safe and consent-respecting action, record the outcome, and deliberately return to ordinary reality.

## Use now

[Open the current GitHub prerelease](https://github.com/LuckyGitHub777/aeon-tempus/releases/tag/v1.1.2-rc1).

Download:

- [`AEON_TEMPUS_ECLIPSE_NODE_THETA7_v1.1.2-rc1.html`](https://github.com/LuckyGitHub777/aeon-tempus/releases/download/v1.1.2-rc1/AEON_TEMPUS_ECLIPSE_NODE_THETA7_v1.1.2-rc1.html)
- [`RELEASE_SHA256SUMS.txt`](https://github.com/LuckyGitHub777/aeon-tempus/releases/download/v1.1.2-rc1/RELEASE_SHA256SUMS.txt)

Place both files in the same folder and verify with:

```bash
sha256sum -c RELEASE_SHA256SUMS.txt
```

On Windows PowerShell, compare the value returned by:

```powershell
Get-FileHash .\AEON_TEMPUS_ECLIPSE_NODE_THETA7_v1.1.2-rc1.html -Algorithm SHA256
```

with the hash printed in `RELEASE_SHA256SUMS.txt`.

Then open the HTML file in a modern browser. It is self-contained and makes no network requests.

### Privacy behavior

When the downloaded HTML is opened as a local `file://`, Theta-7 deliberately uses **session-only memory** instead of persistent browser `localStorage`. This prevents another local HTML file from reading a persisted Theta-7 record through a shared file origin. Export JSON or Markdown if you want a durable copy.

If the interface is later served from a normal web origin, browser `localStorage` may be used and remains unencrypted.

### Optional GitHub Pages

The repository contains a pinned manual Pages deployment workflow for the intended URL:

https://luckygithub777.github.io/aeon-tempus/

Pages is an optional hosted presentation layer. It is **not currently verified as enabled**, so the GitHub Release is the controlling distribution path.

## What v1.1.2-rc1 fixes

- release checksum verifies the downloaded filename directly;
- integrity CI detects stale repository hashes;
- release automation verifies an existing tag's asset digest instead of silently serving stale bytes;
- Markdown export includes all seven chambers, lesson, grounded return, and current action;
- completion errors reveal the relevant collapsed chamber and focus the missing field;
- completion remains functional when persistent storage is unavailable;
- local-file use defaults to session-only memory for privacy;
- clarity remains **Not measured** until both ratings are explicitly changed;
- desktop chamber chevrons remain aligned in the header row;
- mobile gets an always-available **Review & Complete** control;
- print title is visible;
- changing sample scenarios replaces the prior sample prompt as expected;
- embedded UI artwork is WebP-compressed while the original PNG source remains preserved.

## Repository map

- `index.html` — current browser experience
- `releases/` — preserved release candidates
- `assets/` — original source artwork
- `docs/` — canon, specifications, evidence boundary, validation, and V&V
- `archive/` — superseded historical artifacts, unchanged
- `tests/` — static, integrity, and browser regression checks
- `SHA256SUMS.txt` — repository integrity manifest
- `RELEASE_SHA256SUMS.txt` — checksum for the current downloadable release asset

## Evidence status

Current automated and controlled browser checks cover the defects recorded in `docs/VV_UX_REVIEW_2026-10-30.md`. Still not established:

- Safari and Firefox target-device validation;
- manual screen-reader validation;
- complete WCAG 2.2 AA conformance;
- five-to-ten-person controlled pilot results;
- broad effectiveness claims;
- scientific validation of the cosmology.

See `docs/SAFETY_AND_EVIDENCE_BOUNDARY.md`, `docs/VALIDATION_PLAN.md`, and `docs/VV_STATUS_2026-10-30.md`.

## Public availability and license

The repository is public. No open-source license has been selected; public availability does not change the evidence boundary or imply scientific validation. See `NOTICE.md`.
