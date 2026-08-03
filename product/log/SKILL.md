---
name: log
description: Reconstruct a past day onto the ACTUAL calendar from the daily-tracking log plus the Collevity lake — timed blocks placed directly, untimed activity bounded from evidence, every block marked logged or inferred. The "actual" half of intent-vs-actual. Use on /log, "transcribe my day", "put yesterday on the calendar", "reconstruct <date>". For future events use /schedule.
---

# /log (v0.6)

Past day → blocks on **`ACTUAL - transcribed from log`**. Not `/schedule`: backward, batch,
evidence-bound. Own calendar so primary stays clean.

Suite map: `~/.claude/skills/_shared/surfaces.md`.  
Chain: `/checkin` writes daily log → `/log` reads log + lake → ACTUAL.  
Not the skill for "log my day" metrics — that is `/checkin`.

```
/log 2026-08-01
/log yesterday                  ← default if no date
/log feedback …                 → FEEDBACK.md only
```

## Refs

| | |
| --- | --- |
| Suite surfaces | `~/.claude/skills/_shared/surfaces.md` |
| Tags | `~/.claude/skills/_shared/workspace-tags.md` |
| Color map (provisional) | `~/.claude/skills/_shared/domains.json` |
| API + lake | `~/.claude/skills/_shared/google-workspace-mechanics.md` |
| Feedback Open | `FEEDBACK.md` (skim on invoke) |
| Calendar | `ACTUAL - transcribed from log` **only** |
| Daily logs | `/Users/levi/Library/Mobile Documents/com~apple~CloudDocs/00_COLLEVITY/03_TACTIC/daily-tracking/<YYYY-MM-DD>.md` |
| Lake reader | `~/.claude/skills/checkin/read_lake_day.py` |
| Hub OAuth | `levihirsch0@gmail.com` · `~/.config/collevity/gcal/` |

Tags → raw Calendar API. Scripts live until a shape repeats.

## Steps

```
gather(date)  →  evidence  →  transcribe  →  ACTUAL
```

Keep gather and transcribe separate (better retrieval later replaces gather only).

### gather

0. **Daily log for N must exist and be usable.** If missing or core metrics mostly blank:
   **stop and offer `/checkin <date>`** — do not auto-run checkin. The daily log is the spine;
   lake-only → mostly-`inferred` day (failure mode this skill exists to avoid). He may
   override and proceed thin; that is his call.
1. Daily log **N and N+1** (evenings / prior-night sleep often land in N+1)  
2. Lake N (+ edges N−1/N+1): `python3 <reader> <date>` — do not reimplement  
3. Keyword sweep for later mentions of N  

**Full text only** — never decide from a truncated preview.

| source | for |
| --- | --- |
| daily log | spine of what happened |
| `dropper-excel` | **what** he was thinking (not a full day ledger) |
| hooks | **when** he was in sessions (bounds work) |

### transcribe

1. Clocked times first  
2. Bound gaps (hooks + drop timestamps)  
3. Every block: `cv_confidence=logged` \| `inferred`  
4. Containers own a block; children get `cv_parent` after parent id exists  
5. Domain free text; color from map or `_fallback`  
6. Human titles (accurate who/what — no tag prefixes)  
7. Show him; first pass is not final  

### write (raw API)

| | |
| --- | --- |
| calendar | `ACTUAL - transcribed from log` |
| title | human |
| `cv_schema` / `cv_source` | `v1` / `log-transcription` |
| `cv_domain` / `cv_confidence` | free text / `logged`\|`inferred` |
| `cv_parent` / `colorId` | if nested / map or `_fallback` |

No free/busy policy unless he asks. **Re-run:** if ACTUAL already has that day → ask
replace / amend / abort (no silent duplicate).

## Overlap

Nested/concurrent is usually right. Do not warn or collapse.

## Don't

| | |
| --- | --- |
| Truncated text | Full entry first |
| Day N only | N and N+1 |
| Hooks as story | Presence only |
| Unmarked confidence | logged or inferred |
| Done without him | He catches misses |
| Write plan calendars | ACTUAL only |
| Silent re-transcribe | Ask first |
| Tags in titles | Human only |

## Limits

gather is a floor; log granularity caps honesty. Unclocked work is bounded, not fake-precise.

## Done

Day on ACTUAL · tagged/colored/confidence-marked · containers linked · he corrected misses.
