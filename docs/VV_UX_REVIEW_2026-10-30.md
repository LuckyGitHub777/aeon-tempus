# V&V / UX Review — 2026-10-30

## Source
This corrective record incorporates the user-supplied end-to-end review reproduced in chat on 2026-10-30. That review reported testing of the public repository, prerelease download, checksum path, downloaded HTML, browser behavior, privacy behavior, and automated accessibility scanning. Claims in the original report that were not independently reproduced by this corrective pass remain attributed to that source.

## Reproduced / accepted defects in v1.1.1-rc1
1. Release checksum file named repository paths rather than the downloaded HTML asset, so a normal `sha256sum -c` release verification failed.
2. Markdown summary omitted required chamber content and could report stale action data.
3. Missing-field errors inside collapsed chambers were not visibly revealed.
4. Completion could fail when persistent browser storage was unavailable.
5. The privacy notice appeared after extensive input and local-file persistence exposed records to other local HTML files sharing the browser's file origin.
6. Default range positions produced a neutral clarity result even when the user never rated clarity.
7. Same-tag release automation could leave an older asset published after repository changes.

Additional UX findings: print title visibility, desktop chevron wrapping, distant mobile completion control, oversized embedded image, second scenario not replacing the first, and non-clickable README links.

## Corrective disposition in v1.1.2-rc1
- **Checksum:** fixed with a release-specific checksum asset naming the downloaded HTML basename.
- **Integrity:** new CI test verifies every path listed in `SHA256SUMS.txt` and checks the manifest's declared digests.
- **Export:** fixed; all seven chambers, lesson, grounded return, current selected action, node record, and measurement state are exported.
- **Error visibility:** fixed; the relevant chamber opens and the first missing field receives focus.
- **Storage failure:** fixed; in-memory session fallback preserves the active workflow.
- **Local-file privacy:** fixed by defaulting `file://` use to session-only memory; durable records require explicit export.
- **Clarity:** fixed; no delta or neutral signal is emitted until both sliders are explicitly rated.
- **Release freshness:** fixed; same-tag reruns compare the published asset digest against repository bytes and fail on mismatch.
- **Print/desktop/mobile/scenario/README/image size:** corrected.

## Controlled browser regression result
The corrective build was exercised in headless Chromium against the exact HTML bytes. Direct `file://` navigation is blocked by this audit environment, so the file-mode branch was simulated by forcing the same `FILE_MODE` branch while loading the exact document content. The following passed:

- session-only file privacy state;
- no external network requests;
- no JavaScript console/page errors;
- scenario replacement;
- default clarity remains `Not rated` / `Not measured`;
- collapsed missing-field chamber is revealed and focused;
- seven-chamber completion succeeds with persistent storage unavailable;
- Markdown export includes all required chamber/return fields and the latest selected action;
- explicit clarity ratings produce the expected delta and session signal;
- print title remains visible;
- desktop chevron aligns with the chamber header row;
- 375 px mobile viewport has no horizontal overflow;
- fixed mobile `Review & Complete` control is visible.

## Remaining evidence limitations
- Direct local-file navigation could not be re-run in this audit environment because Chromium returned `ERR_BLOCKED_BY_ADMINISTRATOR`; the user-supplied review did independently exercise downloaded-file behavior on Chrome.
- Safari, Firefox, real-phone, and screen-reader testing remain open.
- An earlier automated accessibility scan was reported as 0 issues by the user-supplied review, but this corrective pass did not independently rerun that specific scanner.
- Real-user effectiveness remains unvalidated.
