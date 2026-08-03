# log changelog

## v0.5 — 2026-08-03

Defect fixes + the checkin dependency made explicit.

- `_shared/` and lake-reader refs made absolute — they did not resolve from the load path
- **gather step 0:** stop and send him to `/checkin <date>` when the daily log is missing or
  mostly blank. The log is the spine; without it the lake alone yields a mostly-`inferred`
  day, which is the failure this skill exists to avoid
- `/checkin` now offers `/log` at close, once the day is `core-complete`

## v0.6.1 — 2026-08-03

Version align; description distinguishes ACTUAL vs plan calendar vs checkin.

## v0.6 — 2026-08-03

Suite compatibility: surfaces map; absolute daily-log path; gather0 is offer-/checkin not
auto-invoke; disambiguate from checkin "daily tracking".

## v0.5 — 2026-08-03

Claude: gather0 thin-log gate; absolute shared refs; edges as offers.

## v0.4 — 2026-08-03

Pass-3: simplicity / clarity / readability. Same rules; denser layout; uniform shape.

## v0.3 — 2026-08-03

Pass-2: ACTUAL unpolluted; dropper ≠ ledger; no free/busy policy; no collision handling.

## v0.2.1 — 2026-08-03

Domain map provisional; no shoehorning.

## v0.2 — 2026-08-03

Pass-1: paths, write table, re-run safety, FEEDBACK, default yesterday.

## v0.1 — 2026-08-03

Scaffold from Google-integration session. Process only; scripts live until a shape repeats.
