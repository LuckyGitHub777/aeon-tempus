# V&V Evidence — 2026-10-30

## Static checks
`python tests/test_static.py` passed all repository-defined checks:

- pilot version marker present;
- seven chamber elements present;
- completion control present;
- local-only consent language present;
- plaintext local-storage privacy warning present;
- ASCII-safe export helper present;
- substantive completion fields enforced;
- no `fetch(` usage;
- no XMLHttpRequest usage;
- no WebSocket usage;
- no external script sources;
- no external stylesheets.

JavaScript extracted from the single inline script also passed `node --check`.

HTML inspection found 78 IDs and 78 unique IDs.

## Controlled Chromium smoke test
The exact `index.html` content was loaded into headless Chromium using Playwright. Because this execution environment blocks direct loopback HTTP navigation by administrator policy, the HTML was injected with `page.set_content`. A test-only in-memory `localStorage` shim was injected so application logic could execute without changing the artifact.

Passed checks:

- v1.1.1-rc1 title rendered;
- no page errors;
- initial progress `0/7`;
- privacy notice rendered;
- local-only consent notice rendered;
- checking all seven chamber boxes alone did **not** permit completion;
- the missing Arrival field was marked as an error;
- completing the required substantive fields plus safeguards permitted completion;
- completion rendered as `SELF-ATTESTED SEQUENCE COMPLETION`;
- JSON export filename was ASCII-safe (`THETA-7-...json`);
- Markdown export filename was ASCII-safe (`THETA-7-..._SUMMARY.md`);
- no external scripts;
- no external stylesheets;
- no horizontal overflow at 375 px mobile width;
- no horizontal overflow at 1440 px desktop width.

## Evidence limitation
This is controlled technical evidence, not target-device, cross-browser, accessibility, real-user, or effectiveness validation. Direct file-open and hosted HTTPS tests remain pending outside this restricted environment.
