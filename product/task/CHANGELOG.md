# task changelog

## v0.5 — 2026-08-03

Defect fixes + cross-skill posture.

- `_shared/` refs made absolute — they did not resolve from the load path
- Promotion writes `cv_source=schedule` + `cv_origin=task`, resolving a contradiction with
  `/schedule`
- Now the destination for `/orchestrate`'s parking-lot task-level items, and for commitments
  surfaced at the end of `/checkin`

## v0.6.1 — 2026-08-03

Loosen promote gate: intent to calendar, not precise clock. Fuzzy when OK (schedule guesses).

## v0.6 — 2026-08-03

Suite compatibility: surfaces map; fed by checkin/orchestrate offers; promote on calendar intent.

## v0.5 — 2026-08-03

Claude: `cv_source=schedule` + `cv_origin=task` on promote; absolute refs; edges as offers.

## v0.4 — 2026-08-03

Pass-3: simplicity / clarity / readability. Same rules; denser layout; uniform shape.

## v0.3 — 2026-08-03

Pass-2: "book Dan" stays a task; hub + list-by-title; no unasked calendar proposals.

## v0.2.1 — 2026-08-03

Domain flexibility alignment.

## v0.2 — 2026-08-03

Pass-1: paths, FEEDBACK, promotion `cv_source=task`, due-date side-effect.

## v0.1 — 2026-08-03

Scaffold from Google-integration session. Process only; scripts live until a shape repeats.
