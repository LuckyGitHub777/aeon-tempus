# AEON-TEMPUS · Eclipse Node Theta-7

A symbolic, human-governed uncertainty-reflection and decision-support interface.

> **Status:** v1.1.3-rc1 — privacy and data-loss corrective pilot candidate.  
> **Evidence boundary:** this project does **not** establish a literal spacetime portal, extraterrestrial installation, temporal mechanism, or other paranormal/scientific claim.

## Use now

[Open the current GitHub prerelease](https://github.com/LuckyGitHub777/aeon-tempus/releases/tag/v1.1.3-rc1).

Download:
- [AEON_TEMPUS_ECLIPSE_NODE_THETA7_v1.1.3-rc1.html](https://github.com/LuckyGitHub777/aeon-tempus/releases/download/v1.1.3-rc1/AEON_TEMPUS_ECLIPSE_NODE_THETA7_v1.1.3-rc1.html)
- [RELEASE_SHA256SUMS.txt](https://github.com/LuckyGitHub777/aeon-tempus/releases/download/v1.1.3-rc1/RELEASE_SHA256SUMS.txt)

Put both files in one folder, then verify:

```bash
sha256sum -c RELEASE_SHA256SUMS.txt
```

macOS:

```bash
shasum -a 256 -c RELEASE_SHA256SUMS.txt
```

Windows PowerShell:

```powershell
Get-FileHash .\AEON_TEMPUS_ECLIPSE_NODE_THETA7_v1.1.3-rc1.html -Algorithm SHA256
```

Compare the PowerShell value with `RELEASE_SHA256SUMS.txt`.

Then open the HTML in a modern browser. The application is self-contained and makes no network requests.

## Local-file privacy and keeping your work

When the downloaded HTML is opened as `file://`, Theta-7 keeps entries only for the current tab/session. **Export JSON or Markdown before closing or reloading if you want to keep the record.** While unexported session data exists, the action bar says **Not saved — export to keep** and the browser is asked to warn before leaving.

On startup in local-file mode, Theta-7 removes compatible legacy localStorage keys from earlier versions without hydrating them into the current form.

If the interface is later served from a normal web origin, browser localStorage may be used and remains unencrypted.

## What v1.1.3-rc1 corrects

- warns before leaving local/session-only work changed since the last export;
- clears the warning state after JSON or Markdown export;
- removes legacy local-file persisted records without reading them into the form;
- protects custom scenario text with confirmation before sample replacement;
- adds accessible invalid-field semantics and clears them when corrected;
- preserves the v1.1.2-rc1 release artifact unchanged;
- retains release checksum and same-tag digest-mismatch protections.

## Repository map

- `index.html` — current browser experience
- `releases/` — immutable release candidates
- `assets/` — original source artwork
- `docs/` — canon, specifications, evidence boundary, validation, and V&V
- `archive/` — superseded historical artifacts
- `tests/` — static, integrity, and direct-file browser regression checks
- `SHA256SUMS.txt` — repository integrity manifest
- `RELEASE_SHA256SUMS.txt` — checksum for the current downloadable release asset

## Evidence status

Automated validation covers the corrective behaviors in `docs/VV_UX_REVIEW_2026-10-30.md`. Still open: Safari/Firefox target-device checks, real-phone testing, manual screen-reader/WCAG review, and the planned 5–10-person pilot.

## Public availability and license

The repository is public. No open-source license has been selected; public availability does not change the evidence boundary or imply scientific validation. See `NOTICE.md`.
