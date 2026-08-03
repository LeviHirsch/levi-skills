---
name: log
description: Reconstruct a past day onto the ACTUAL calendar from the daily-tracking log plus the Collevity lake — timed blocks placed directly, untimed activity bounded from evidence, every block marked logged or inferred. The "actual" half of intent-vs-actual. Use on /log, "transcribe my day", "put yesterday on the calendar", "reconstruct <date>". For future events use /schedule.
---

# /log (v0.2)

Turn a day that already happened into tagged blocks on the **ACTUAL** calendar.

This is reconstruction, not capture. Backward-looking, batch, evidence-bound.
`/checkin` builds the daily log; `/log` reads it and writes the calendar. Chain:
`checkin → log → ACTUAL`.

```
/log 2026-08-01
/log yesterday
/log feedback …
```

Default date if none given: **yesterday** (today is often still open in check-in).

## Read first

| | |
| --- | --- |
| Tag schema | `_shared/workspace-tags.md` |
| Domain → color | `_shared/domains.json` |
| API facts + lake signals | `_shared/google-workspace-mechanics.md` |
| Feedback (Open) | `FEEDBACK.md` in this folder |
| Target calendar | `ACTUAL - transcribed from log` (name exact) |
| Daily logs | `…/00_COLLEVITY/03_TACTIC/daily-tracking/<YYYY-MM-DD>.md` |
| Lake reader | `product/checkin/read_lake_day.py` (or `~/.claude/skills/checkin/read_lake_day.py`) |
| Hub / creds | `levihirsch0@gmail.com` · `~/.config/collevity/gcal/` |

Skim **FEEDBACK.md → Open** on invoke; honor `prefer` / `dislike`.

**Write only to ACTUAL.** Never to primary or other planning calendars.

`workspace-mcp` cannot write tags — use the raw Calendar API for ACTUAL writes (same pattern
as `/schedule`). Scripts stay live until a shape repeats.

## Two steps, kept separate

```
gather(date)         → evidence     weak half; improve freely
transcribe(evidence) → blocks       stable half; do not fold gather into it
```

When Collevity has a better retrieval path, only `gather` changes.

### gather

Do all of this. Cheap structured sources first:

1. **Daily log for N and N+1.** Catch-up is written in the afternoon, so evenings and the
   previous night's sleep often land in the *next* day's file. Not an edge case — it showed
   up on the first day ever transcribed.
2. **Lake for N**, plus the edges of N−1 and N+1, via the lake reader (do not reimplement):
   `python3 <reader> <date>`
3. **Keyword sweep** for references to N from other dates — retrospective mentions do not
   carry a matching timestamp.

**Read full text. Never infer from a truncated field.** Truncated previews caused most of the
false "missing data" on the first real run; reading full entries collapsed the inference rate
sharply.

| lake source | use for |
| --- | --- |
| `dropper-excel` | **what** — content, thinking, decisions, retrospective narration |
| `claude-hook` / `grok-hook` | **when** — presence / session clusters that bound working blocks |

Dropper is thought capture, not a ledger of what happened. The daily log is the primary
"actual" spine; the lake fills gaps and bounds time.

### transcribe

1. **Place logged times first** — anything with a clock in the log or stated plainly in a drop.
2. **Bound the gaps** using hook clusters and drop timestamps.
3. **Mark every block** `cv_confidence=logged` or `inferred`. Without this, inference and
   record become the same thing on ACTUAL.
4. **Containers** — places / stretches that contain other blocks get their own event; children
   carry `cv_parent` = parent event id (set after parent is created).
5. **Domain + color** from observation + `domains.json` (unmapped → `_fallback`). Domains are
   observed; a day only shows what that day contained.
6. **Draft → confirm → write** (or write small and correct). Do not treat the first pass as
   settled. Levi will catch what pure reading cannot.

### Write each block (raw API)

| field | value |
| --- | --- |
| calendar | `ACTUAL - transcribed from log` |
| title | human, no tag prefixes |
| start / end | resolved times |
| `cv_schema` | `v1` |
| `cv_source` | `log-transcription` |
| `cv_domain` | observed |
| `cv_sub` | optional |
| `cv_confidence` | `logged` \| `inferred` |
| `cv_parent` | parent event id when nested |
| `colorId` | from `domains.json` |

### Re-runs

Before writing a day that may already be on ACTUAL: list existing events that day on ACTUAL.
If any exist, **say so and ask** — replace, amend, or abort. Do not silently duplicate a day.

## Overlap is normal

Nested and concurrent blocks are usually the accurate record (call while biking, work while
guests are over). Never resolve, never warn, never collapse for "conflict."

## Modes

| Command | What |
| --- | --- |
| `/log [date]` | gather → transcribe → ACTUAL |
| `/log feedback …` | append taste to `FEEDBACK.md` only |

Feedback convention: `_shared/skill-feedback-convention.md`.

## Do not

| Don't | Do |
| --- | --- |
| Infer from truncated text | Pull the full entry, then decide |
| Read only day N | Read N and N+1; evening often lives in N+1 |
| Treat every lake row as content | Hooks are presence, not narration |
| Leave confidence unmarked | Every block says logged or inferred |
| Present the result as settled without him | Confirm; he catches what you cannot |
| Write to planning calendars | ACTUAL only |
| Silently re-transcribe over an existing day | Ask first |
| Put tags in titles | Titles stay human |

## Limits (honest floor)

- `gather` is a floor. Cross-references beyond keyword sweep need better retrieval later.
- Sub-hour activity is mostly unrecoverable; log granularity is the ceiling.
- Clocked parts of the day are often the routine parts; substantive work is often unclocked
  and must be bounded from lake presence + narrative.

## Done when

- The day is on ACTUAL with tagged, colored, confidence-marked blocks
- Containers link children via `cv_parent`
- Levi has seen it and corrected what was wrong
