---
name: log
description: Reconstruct a past day onto the ACTUAL calendar from the daily-tracking log plus the Collevity lake — timed blocks placed directly, untimed activity bounded from evidence, every block marked logged or inferred. The "actual" half of intent-vs-actual. Use on /log, "transcribe my day", "put yesterday on the calendar", "reconstruct <date>". For future events use /schedule.
---

# /log (v0.3)

Reconstruct a day that already happened onto **`ACTUAL - transcribed from log`**.

This is not `/schedule`. It is backward, batch, evidence-bound. Separate calendar on purpose
so the primary plan calendar does not get polluted. `/checkin` builds the daily log; `/log`
reads that log (plus the lake) and writes ACTUAL.

```
/log 2026-08-01
/log yesterday
/log feedback …
```

Default date if omitted: **yesterday**.

## Read first

| | |
| --- | --- |
| Tags | `_shared/workspace-tags.md` |
| Color map (provisional) | `_shared/domains.json` |
| API + lake signals | `_shared/google-workspace-mechanics.md` |
| Feedback Open | `FEEDBACK.md` |
| Target calendar | `ACTUAL - transcribed from log` only |
| Daily logs | `…/03_TACTIC/daily-tracking/<YYYY-MM-DD>.md` |
| Lake reader | `product/checkin/read_lake_day.py` |
| Hub OAuth | `levihirsch0@gmail.com` · `~/.config/collevity/gcal/` |

Skim FEEDBACK Open. Writes need the **raw Calendar API** for tags. Scripts stay live until a
shape repeats.

## Two steps

```
gather(date)         → evidence
transcribe(evidence) → blocks on ACTUAL
```

Keep the seam. Better retrieval later should replace gather, not rewrite transcribe.

### gather

1. Daily log for **N and N+1** — catch-up is often written the next afternoon; evenings and
   prior-night sleep land in N+1. This already bit on the first real day.
2. Lake for N (and edges of N−1 / N+1) via the reader — do not reimplement:
   `python3 <reader> <date>`
3. Keyword sweep for later mentions of N (retrospectives have no matching timestamp).

**Read full text. Never decide from a truncated preview.** First real run: most "missing"
data was still in the uncut text; full reads cut the inference rate hard.

| source | use |
| --- | --- |
| daily log | spine of what happened (the actual) |
| `dropper-excel` | **what** he was thinking / deciding — not a full ledger of the day |
| `claude-hook` / `grok-hook` | **when** he was in sessions (bounds work blocks) |

### transcribe

1. Place **clocked** items first (log times, explicit times in drops).
2. Bound gaps from hook clusters + drop timestamps.
3. Every block: `cv_confidence=logged` or `inferred`. No unmarked guesses on ACTUAL.
4. Containers (library stretch, guests over) get their own block; children get `cv_parent`
   after the parent event id exists.
5. Domain = free text that fits; color from provisional map or `_fallback`. Do not shoehorn.
6. Titles human and accurate to who was there — not a forced naming scheme.
7. Show him the picture; correct what reading cannot catch. First pass is not sacred.

### Write (ACTUAL only, raw API)

| | |
| --- | --- |
| calendar | `ACTUAL - transcribed from log` |
| title | human, no tag prefixes |
| `cv_schema` | `v1` |
| `cv_source` | `log-transcription` |
| `cv_domain` | free text |
| `cv_confidence` | `logged` \| `inferred` |
| `cv_parent` | when nested |
| `colorId` | map or `_fallback` |

Do not invent a free/busy scheme for ACTUAL unless he asks — it did not show up usefully in
the UI when tried.

### Re-runs

If that day already has ACTUAL events: say so, ask replace / amend / abort. No silent duplicate.

## Overlap

Nested and concurrent blocks are usually right (work while guests are over, call on a bike).
Do not warn, do not collapse, do not "fix collisions."

## Modes

| | |
| --- | --- |
| `/log [date]` | gather → transcribe → ACTUAL |
| `/log feedback …` | `FEEDBACK.md` only |

## Do not

| Don't | Do |
| --- | --- |
| Infer from truncated text | Full entry first |
| Read only day N | N and N+1 |
| Treat hooks as narrative | Presence signal only |
| Leave confidence blank | logged or inferred every time |
| Call it done without him | He catches what you miss |
| Write to primary / plan calendars | ACTUAL only |
| Silently overwrite a transcribed day | Ask first |
| Put tags in titles | Titles stay human |

## Limits

- gather is a floor until better retrieval exists.
- Log granularity caps what you can honestly place; unclocked real work gets bounded, not faked precise.

## Done when

Day on ACTUAL, tagged/colored/confidence-marked, containers linked, he has corrected what was wrong.
