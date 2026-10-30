# V&V / UX Review — 2026-10-30

## Independent review findings

An independent end-to-end review of the public repository, release download, checksum path, downloaded HTML, browser behavior, privacy behavior, and automated checks identified four remaining corrective areas after v1.1.2-rc1:

1. **Session-only data loss risk:** local-file/session-only work could be lost by closing or reloading without an explicit export warning.
2. **Legacy local-file privacy:** earlier localStorage records needed removal without hydration when running as a downloaded local file.
3. **Scenario overwrite protection:** loading a sample could replace custom trigger or obscuration text without confirmation.
4. **Error semantics:** visible required-field errors needed programmatic `aria-invalid` / `aria-describedby` relationships and automatic clearing after correction.

## v1.1.3-rc1 corrective requirements

- A dirty local/session-only record shows **Not saved — export to keep**.
- Leaving with unexported edits triggers browser before-unload protection; successful JSON or Markdown export clears the dirty state.
- Local-file startup removes compatible legacy localStorage keys and never hydrates them.
- Reset clears current and compatible legacy real-localStorage keys.
- Custom trigger or obscuration text requires confirmation before a sample scenario replaces it.
- Required input errors set `aria-invalid="true"` and reference a concrete error message via `aria-describedby`; correcting the field removes both.
- The v1.1.2-rc1 release file remains byte-for-byte unchanged.
- Release automation fails closed when an existing tag's published HTML digest differs from repository bytes.

## Verification gates

The regression suite must exercise the direct `file://` path in Chrome, including:
- unload warning before export and no warning after export;
- legacy key removal with no hydration into `#arrival`;
- scenario confirmation with dismiss preserving custom text;
- accessible error semantics and clearing on correction.

Static and integrity jobs must pass, followed by release publication and checksum verification.

## Remaining validation beyond this corrective release

Safari/Firefox, real phones, manual screen-reader/WCAG review, and a 5–10-person pilot remain separate evidence gates. They evaluate broader compatibility and real-user effectiveness rather than the corrected functional scope.
