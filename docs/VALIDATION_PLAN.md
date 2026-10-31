# Validation Plan

## Current status
v1.1.4-rc1 is the current candidate for GitHub Pages and remains a pilot candidate rather than a broadly validated product.

Hosted experience: https://luckygithub777.github.io/aeon-tempus/

## Required pilot validation
1. Keep the automated GitHub Pages deployment gate green; each deployment must fetch the public HTTPS page and verify the expected AEON-TEMPUS markers.
2. Download the current GitHub Release HTML and `RELEASE_SHA256SUMS.txt`; verify the release checksum for offline use.
3. Open the downloaded HTML directly on target Windows and macOS devices; verify session-only local-file behavior, unload warning, export clearing, and legacy cleanup.
4. Test current Chrome, Edge, Firefox, and Safari where applicable.
5. Perform a WCAG 2.2 AA-oriented manual audit and screen-reader checks.
6. Run a controlled 5–10 person pilot using safe, ordinary scenarios.

## Pilot measures
Predefine thresholds before testing: independent completion rate, critical misunderstanding rate, actionability, usability, abandonment chamber, safety concerns, completion time, and explicitly rated clarity-before/clarity-after delta.

Clarity change is self-reported session evidence only and does not establish broad effectiveness.
