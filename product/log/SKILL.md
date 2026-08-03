---
name: log
description: Reconstruct a past day onto the ACTUAL calendar from the daily-tracking log plus the Collevity lake — timed blocks placed directly, untimed activity bounded from evidence, every block marked logged or inferred. The "actual" half of intent-vs-actual. Use on /log, "transcribe my day", "put yesterday on the calendar", "reconstruct <date>". For future events use /schedule.
---

# /log (v0.1)

Turn a day that already happened into tagged blocks on the **ACTUAL** calendar, so intent and
actual can eventually be compared.

This is reconstruction, not capture. It is backward-looking, batch, and evidence-bound.
`/checkin` builds the daily log; `/log` reads it. The chain is `checkin -> log -> calendar`.

```
/log 2026-08-01
/log yesterday
```

## Read first

| | |
| --- | --- |
| Tag schema | `_shared/workspace-tags.md` |
| API facts, and the two lake signals | `_shared/google-workspace-mechanics.md` |
| Target calendar | `ACTUAL - transcribed from log` |

## Two steps, kept separate on purpose

```
gather(date)        -> evidence     the weak half, meant to be replaced
transcribe(evidence)-> blocks       the half that stays
```

Keep the seam clean. When Collevity's context-retrieval engine exists, `gather` becomes one
call to it and `transcribe` does not change.

### gather — hybrid, and structured does most of the work

Cheap and structured carries the load. Do all of it:

1. Daily log for **N and N+1**. Levi writes catch-up in the afternoon, so the tail of each
   day — evenings, the previous night's sleep — lands in the *next* day's file. This is not
   an edge case; it happened on the first day ever transcribed.
2. Lake entries for N, plus the edges of N-1 and N+1.
3. Keyword sweep for references to N from any date — retrospective mentions carry no
   matching timestamp.

**Read full text. Never infer from a truncated field.** On the first real run, most of what
looked like missing data was sitting in text that had been cut off in a preview. The
inference rate collapsed from 6/13 to 5/17 once the source was read properly.

The two lake sources answer different questions:

| source | use it for |
| --- | --- |
| `dropper-excel` | **what** — content, thinking, decisions, retrospective narration |
| `claude-hook` / `grok-hook` | **when** — a dense activity trace; session clusters bound working blocks |

### transcribe

1. **Place logged times first.** Anything with a clock in the log or stated plainly in a drop.
2. **Then bound the gaps** using hook clusters and drop timestamps.
3. **Mark every block** `cv_confidence=logged` or `inferred`. Without this an inference
   becomes indistinguishable from a record and the ACTUAL calendar quietly becomes fiction.
4. **Containers** — places and stretches that contain other blocks (a library session, guests
   over) get their own block, and the blocks inside them carry `cv_parent`.
5. **Tag and color** per `domains.json`. Domains are observed; a day only shows the domains
   that day contained.
6. **Confirm with Levi before treating it as done.** The first run needed two corrections he
   caught and no amount of reading would have.

## Overlap is the point

Nested and concurrent blocks are usually the accurate record. A call taken while biking, work
done while guests played a game, a decision made inside a longer session. Never resolve,
never warn, never collapse.

## Do not

| Don't | Do |
| --- | --- |
| Infer from truncated text | Pull the full entry, then decide |
| Read only day N | Read N and N+1; the evening is in the next file |
| Treat every lake row as content | Hooks are a presence signal, not narration |
| Leave confidence unmarked | Every block says logged or inferred |
| Present the result as settled | Confirm; he will catch what you cannot |
| Write to the planning calendars | ACTUAL only |

## Known gaps

- `gather` is a floor. Cross-references beyond a keyword sweep need the retrieval engine.
- Sub-hour activity is mostly unrecoverable; the log's granularity is the ceiling.
- The parts of the day with recorded times are the routine parts. The substantive work is
  exactly what has no clock on it.

## Done when

- The day is on ACTUAL with tagged, colored, confidence-marked blocks
- Containers carry children via `cv_parent`
- Levi has seen it and corrected what was wrong
