# schedule changelog

## v0.5 — 2026-08-03

Defect fixes + cross-skill posture.

- `_shared/` refs made absolute (`~/.claude/skills/_shared/…`) — they did not resolve from
  the load path
- `cv_source` now always means which skill wrote the event; new `cv_origin=task` records a
  promoted task
- Nothing routes *into* `/schedule` automatically — `/orchestrate` names dated gates and stops

## v0.4 — 2026-08-03

Pass-3: simplicity / clarity / readability. Same rules; denser layout; calendar detail
defers to mechanics; uniform Refs → Steps → Don't → Done shape.

## v0.3 — 2026-08-03

Pass-2 (user-intent fidelity): hub vs calendar pick; no unasked blocks/collision nags;
no title scheme; lean voice; free/busy only if asked.

## v0.2.1 — 2026-08-03

Domain schema flexible / not overcommitted.

## v0.2 — 2026-08-03

Pass-1: paths, FEEDBACK, color fix, ACTUAL off-limits, UI-invisible fields, Groups note.

## v0.1 — 2026-08-03

Scaffold from Google-integration session. Process only; scripts live until a shape repeats.
