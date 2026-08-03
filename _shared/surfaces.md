# Where things go (suite surfaces)

One map for process + Google-stratum skills. **Levi names the surface** when he speaks.
Skills **offer** at boundaries; they do not auto-invoke each other.

## Capture / plan surfaces

| Need | Surface | Skill |
| --- | --- | --- |
| Day metrics + narrative for a calendar day | daily-tracking log | `/checkin` |
| Standing multi-session work arc | thread registry | `/orchestrate intake` |
| Must not forget, **no time claimed** | Google Tasks | `/task` |
| Time claimed / event should exist | Google Calendar (plan) | `/schedule` |
| Reconstruct what already happened | calendar `ACTUAL - transcribed from log` | `/log` |
| Persist a session + feed registry | SPP lake + registry | `/session-save` |

### Tasks lists (under `/task`)

| List | Holds |
| --- | --- |
| **Scheduling queue** | wants a time, does not have one (people, "book X") |
| **My Tasks** | other residue (errands, deposit the check) |

Not a third list for "threads." Standing arcs → registry, not Tasks.

## Edges (offer only)

```
checkin ──close──▶ offer /log <date>     (only if day is core-complete)
        └─close──▶ offer /task           (commitments with no home; his words)
   log ──gather0─▶ stop → /checkin first (missing/thin log; he may override)
orchestrate ─6b──▶ offer /task           (parking-lot task-level, not threads)
  task ──promote▶ /schedule              (only when he gives a time / says so)
session-save ────▶ registry writeback    (threads only; not tasks/events)
```

**Never auto:** `orchestrate → /schedule`, `checkin → /log` (invoke), `checkin → /task` (invoke),
`task → event` without his time.

## Routing reflexes (holistic intent)

| He said / situation | Do |
| --- | --- |
| "put it on the calendar" / named a time | `/schedule` |
| "remind me" / "I need to" / no time | `/task` |
| "book Dan" (scheduling is the *work*) | `/task` (Scheduling queue) — not an event yet |
| "transcribe yesterday" / "what actually happened" | `/log` |
| "check in" / daily tracking fields | `/checkin` (not `/log`) |
| multi-session arc still open | registry via `/orchestrate` — not Tasks |
| small residue sitting in parking lot | offer `/task` — not a new registry row |
| dated gate on a thread | name it in orchestrate; **stop** — he schedules |

## Shared rules that cross skills

- **No tags in titles.** Color + calendar are the human-visible handles.
- **Domains** = free-text `cv_domain` + provisional color map — not separate calendars, not enforced.
- **Overlap is never an error** (calendar).
- **No invented due dates** (Tasks) and **no unasked calendar blocks** (schedule / orchestrate).
- **Offer once, never act** at skill boundaries.

Paths and API facts: `google-workspace-mechanics.md`. Tags: `workspace-tags.md`.
