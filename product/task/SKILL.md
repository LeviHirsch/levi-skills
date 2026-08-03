---
name: task
description: Capture something into Google Tasks that needs doing but claims no time yet — including tasks whose whole content is "schedule this". Also promotes a task to a calendar event once it gets a time. Use on /task, "add a task", "remind me to", "I need to", "put X in the queue", "I keep saying I'll meet up with X". For things that claim a time slot now, use /schedule instead.
---

# /task (v0.2.1)

The surface for things that need to **not be forgotten** but do not claim a slot.

Levi names the surface. "I need to book Dan" is a task even though the doing is scheduling.
Do not helpfully turn it into an event.

```
/task grab coffee with parker
/task deposit the check
/task book dan
/task feedback …
```

## Read first

| | |
| --- | --- |
| Tag schema + Tasks limits | `_shared/workspace-tags.md` |
| API facts | `_shared/google-workspace-mechanics.md` |
| Feedback (Open) | `FEEDBACK.md` in this folder |
| Hub account | `levihirsch0@gmail.com` |
| Creds | `~/.config/collevity/gcal/` (Tasks use the same OAuth) |

Skim **FEEDBACK.md → Open** on invoke; honor `prefer` / `dislike`.

Resolve list ids by **title** via the Tasks API (do not hardcode ids). Create a missing list
only if Levi asked for it by name.

## The lists

| list | holds |
| --- | --- |
| **Scheduling queue** | wants a time, does not have one — mostly people ("grab coffee with Parker", "book Dan") |
| **My Tasks** | loose residue that is not a scheduling problem (deposit the check, pick up something) |

Anything big enough to be a standing arc belongs in the **thread registry** via
`/orchestrate intake`, not here. This is for residue — too small for a thread, too real to drop.

## What Tasks cannot do

**No tags. No color. No `extendedProperties`.** Full resource:
`title · notes · due · status · parent · position · links`.

Unknown fields are accepted by the API and **silently discarded** — a write that looks like
it worked did not. If domain matters, put it in `notes` as a visible line (or leave it off).

- `position` = sibling ordering under the same parent, not metadata
- `parent` = real one-level hierarchy — use subtasks when something decomposes

A task **with** a due date appears on the Calendar UI. Undated ones stay in the side panel.
That is why inventing a due date is not free.

## Process

1. **Pick the list** from the two above. Ask only if genuinely ambiguous.
2. **Due date only if Levi gave one.** Do not invent deadlines.
3. **Notes** carry the *why* when there is one — context that the title cannot hold.
4. **Write** via Tasks API (MCP is fine here; there are no tags to set).
5. **Report** the list, the title, and whether it is dated. Then stop.

## Promotion (task → calendar)

When a queued item gets a real time (Levi gives one, or asks to schedule it now):

1. Hand off to `/schedule` with the title, notes, and time.
2. On the calendar event, set `cv_source=task` (and the rest of the tag set per schedule).
3. **Close the task** after the event exists — do not leave an open shadow of the event.
4. Carry notes into the event description.

Do not promote on your own initiative. He names when something moves from queue to calendar.

## Modes

| Command | What |
| --- | --- |
| `/task …` | capture (or promote if a time is now given) |
| `/task feedback …` | append taste to `FEEDBACK.md` only; do not create a task |

Feedback convention: `_shared/skill-feedback-convention.md`.

## Do not

| Don't | Do |
| --- | --- |
| Invent due dates | Undated is the honest state for most of this |
| Turn a task into an event to be helpful | He named the surface |
| Write structured metadata onto a task | It is silently dropped. Use `notes` |
| Promote small items into registry threads | Registry is for standing arcs |
| Delete a list without reading it first | List deletion takes every task with it |
| Leave a promoted task open | Close it once the event exists |

## Done when

- The item is on the right list, with notes if there was a reason
- Nothing got a due date Levi did not give
- He can find it on his phone
