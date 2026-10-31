# AEON-TEMPUS · Eclipse Node Theta-7

A symbolic, human-governed uncertainty-reflection and decision-support interface.

> **Status:** v1.1.4-rc1 — shared-site privacy corrective pilot candidate.  
> **Hosted experience:** https://luckygithub777.github.io/aeon-tempus/  
> **Evidence boundary:** this project does **not** establish a literal spacetime portal, extraterrestrial installation, temporal mechanism, or other paranormal/scientific claim.

## Use now

**Open the live website:**  
https://luckygithub777.github.io/aeon-tempus/

The hosted site is the primary browser experience. GitHub Pages deployment is automated from `main` and the deployment workflow verifies the public HTTPS page after every deploy.

For offline use or independent checksum verification, use the current prerelease:

[Open v1.1.4-rc1](https://github.com/LuckyGitHub777/aeon-tempus/releases/tag/v1.1.4-rc1)

Download:
- [AEON_TEMPUS_ECLIPSE_NODE_THETA7_v1.1.4-rc1.html](https://github.com/LuckyGitHub777/aeon-tempus/releases/download/v1.1.4-rc1/AEON_TEMPUS_ECLIPSE_NODE_THETA7_v1.1.4-rc1.html)
- [RELEASE_SHA256SUMS.txt](https://github.com/LuckyGitHub777/aeon-tempus/releases/download/v1.1.4-rc1/RELEASE_SHA256SUMS.txt)

Verify in Linux:

```bash
sha256sum -c RELEASE_SHA256SUMS.txt
```

macOS:

```bash
shasum -a 256 -c RELEASE_SHA256SUMS.txt
```

Windows PowerShell:

```powershell
Get-FileHash .\AEON_TEMPUS_ECLIPSE_NODE_THETA7_v1.1.4-rc1.html -Algorithm SHA256
```

Compare the PowerShell value with `RELEASE_SHA256SUMS.txt`.

## Privacy and keeping your work

Theta-7 keeps entries only for the current tab, both on the website and in a downloaded copy. Browser storage on `*.github.io` is shared by every project site on the same host, and storage for local files can be shared by every local HTML file, so Theta-7 does not write your entries there. **Export JSON or Markdown before closing or reloading if you want to keep the record.** While unexported session data exists, the action bar says **Not saved — export to keep** and the browser is asked to warn before leaving.

On the website, a record that v1.1.3-rc1 autosaved is moved into the open tab and removed from shared storage; export it to keep it. In a downloaded copy, records saved by earlier versions are removed without being read into the form.

## What v1.1.4-rc1 corrects

- keeps website entries in the tab only, because `*.github.io` storage is shared across project sites;
- moves a record autosaved by v1.1.3-rc1 on the website into the tab and removes it from shared storage;
- rewrites the privacy notice for both the website and a downloaded copy;
- makes the mobile Review & Complete button's accessible name start with its visible label.

Carried forward from v1.1.3-rc1:

- warns before leaving local/session-only work changed since the last export;
- clears the warning state after JSON or Markdown export;
- removes legacy local-file persisted records without reading them into the form;
- protects custom scenario text with confirmation before sample replacement;
- adds accessible invalid-field semantics and clears them when corrected;
- preserves the v1.1.2-rc1 release artifact unchanged;
- retains release checksum and same-tag digest-mismatch protections.

## Repository map

- `index.html` — current browser experience and GitHub Pages source artifact
- `releases/` — immutable release candidates
- `assets/` — original source artwork
- `docs/` — canon, specifications, evidence boundary, validation, and V&V
- `archive/` — superseded historical artifacts
- `tests/` — static, integrity, and direct-file browser regression checks
- `SHA256SUMS.txt` — repository integrity manifest
- `RELEASE_SHA256SUMS.txt` — checksum for the current downloadable release asset

## Evidence status

The hosted GitHub Pages deployment is verified live at the URL above. Mainline static/integrity and browser regression gates remain automated. Still open: Safari/Firefox target-device checks, real-phone testing, manual screen-reader/WCAG review, and the planned 5–10-person pilot.

## Public availability and license

The repository and hosted interface are public. No open-source license has been selected; public availability does not change the evidence boundary or imply scientific validation. See `NOTICE.md`.
