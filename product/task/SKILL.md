---
name: task
description: Capture something into Google Tasks that needs doing but claims no time yet — including tasks whose whole content is "schedule this". Also promotes a task to a calendar event once it gets a time. Use on /task, "add a task", "remind me to", "I need to", "put X in the queue", "I keep saying I'll meet up with X". For things that claim a time slot now, use /schedule instead.
---

# /task (v0.3)

Things that must **not be forgotten** but do **not** claim a calendar slot yet.

**He names the surface.** "I need to book Dan" is a **task** even though the work is later
scheduling. Do not helpfully turn it into an event. The judgment call he does **not** want
you to make: *"should this be on the calendar now?"* vs *"this needs to happen"* (which can
include *schedule this*). If he said task / remind me / I need to / queue it — use Tasks.

```
/task grab coffee with parker
/task deposit the check
/task book dan
/task feedback …
```

## Read first

| | |
| --- | --- |
| Tasks limits | `_shared/workspace-tags.md` |
| API | `_shared/google-workspace-mechanics.md` |
| Feedback Open | `FEEDBACK.md` |
| Hub OAuth | `levihirsch0@gmail.com` · `~/.config/collevity/gcal/` |

Skim FEEDBACK Open. Lists: resolve **id by title**. Create a list only if he asked for that name.

Same hub account as calendar. You are picking a **task list**, not a different Google login.

## Lists

| list | holds |
| --- | --- |
| **Scheduling queue** | wants a time, does not have one — mostly people (Parker, book Dan, coffee with X) |
| **My Tasks** | everything else that is still just a to-do (deposit the check, errands) |

Standing multi-session arcs → `/orchestrate intake` (thread registry), not here. This surface
is the small stuff that is real enough not to drop.

## What Tasks can and cannot hold

Resource: `title · notes · due · status · parent · position · links`.

**No tags, no color, no `extendedProperties`.** Unknown fields are accepted and **silently
dropped**. Domain, if it matters, is a line in `notes` — or skip it.

- `parent` = one-level subtasks (real; Calendar does not have this)
- `position` = sibling order only
- A **due date** makes the task show on the Calendar UI. Undated stays in the side panel.
  Inventing a due date is inventing a commitment. **Only if he gave one.**

## Process

1. Pick list (table above). Ask only if truly ambiguous.
2. Due only if he said a date.
3. Notes = why / context when he gave any (worth more later than a bare title).
4. Write via Tasks API (MCP is fine).
5. Report: list, title, dated or not. Stop.

## Promotion → `/schedule`

When **he** gives a time or says schedule it now:

1. `/schedule` with title, notes, time (calendar pick per schedule skill).
2. Event `cv_source=task` (+ normal tag set).
3. **Close the task** after the event exists — no open shadow.
4. Notes → event description.

Do not promote on your own.

## Modes

| | |
| --- | --- |
| `/task …` | capture (or promote if he just gave a time) |
| `/task feedback …` | `FEEDBACK.md` only |

## Do not

| Don't | Do |
| --- | --- |
| Invent due dates | Undated is fine |
| Turn task → event to be helpful | He named Tasks |
| Write fake metadata fields | They drop silently; use notes |
| Push small items into the thread registry | Registry is for standing arcs |
| Delete a list without reading it | Deletes every task in it |
| Leave a promoted task open | Close after the event exists |
| Propose calendar blocks from a task capture | That is `/schedule` when he asks |

## Done when

Right list, honest due (or none), notes if he had a why, findable on his phone.
