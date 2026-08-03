# Where things go (suite surfaces)

One map for process + Google-stratum skills. **Levi names the surface** when he speaks.
Skills **offer** at boundaries; they do not auto-invoke each other.

Keep this map **light**. Prefer his words over sharp gates. Fuzzy when is normal on calendar.

## Capture / plan surfaces

| Need | Surface | Skill |
| --- | --- | --- |
| Day metrics + narrative for a calendar day | daily-tracking log | `/checkin` |
| Standing multi-session work arc | thread registry | `/orchestrate intake` |
| Must not forget, **not an event yet** | Google Tasks | `/task` |
| Should exist as a calendar event (when can be fuzzy) | Google Calendar (plan) | `/schedule` |
| Reconstruct what already happened | calendar `ACTUAL - transcribed from log` | `/log` |
| Persist a session + feed registry | SPP lake + registry | `/session-save` |

### Tasks lists (under `/task`)

| List | Holds |
| --- | --- |
| **Scheduling queue** | wants to become an event someday — mostly people ("book X") — **no slot claimed yet** |
| **My Tasks** | other residue (errands, deposit the check) |

Not a third list for "threads." Standing arcs → registry, not Tasks.

## Edges (offer only)

```
checkin ──close──▶ offer /log <date>     (prefer when day is core-complete)
        └─close──▶ offer /task           (commitments with no home; his words)
   log ──gather0─▶ offer /checkin first  (missing/thin log; he may override)
orchestrate ─6b──▶ offer /task           (parking-lot task-level, not threads)
  task ──promote▶ /schedule              (when he steers to calendar; fuzzy when OK)
session-save ────▶ registry writeback    (threads only; not tasks/events)
```

**Never auto-invoke** another skill. Offers surface; he accepts or ignores.

**Promote gate is intent, not precision:** he wants it on the calendar — not "he gave a
clock time." `/schedule` already guesses duration and fuzzy windows.

## Routing reflexes

| He said / situation | Do |
| --- | --- |
| "put it on the calendar" / "schedule X" / claims a slot (fuzzy OK) | `/schedule` |
| "remind me" / "I need to" / queue it / not an event yet | `/task` |
| "book Dan" (scheduling is the *work*, no slot yet) | `/task` (Scheduling queue) |
| "transcribe yesterday" / reconstruct what happened | `/log` |
| "check in" / daily tracking fields | `/checkin` (not `/log`) |
| multi-session arc still open | registry via `/orchestrate` — not Tasks |
| small residue in parking lot | offer `/task` — not a new registry row |
| dated gate on a thread | name it in orchestrate; **stop** — he schedules |

When unsure between task and schedule: **believe the verb he used**. Do not upgrade a task
into an event to be helpful, and do not demote a calendar ask into a task because the clock
was vague.

## Shared rules that cross skills

- **No tags in titles.** Color + calendar are the human-visible handles.
- **Domains** = free-text `cv_domain` + provisional color map — not separate calendars, not enforced.
- **Overlap is never an error** (calendar).
- **No invented due dates** on Tasks (due ≠ fuzzy event when).
- **No unasked calendar blocks** (create what he asked; schedule may guess *how* to place it).
- **Offer once, never act** at skill boundaries.

Paths and API facts: `google-workspace-mechanics.md`. Tags: `workspace-tags.md`.
