---
name: task
description: Capture something into Google Tasks that needs doing but claims no time yet — including tasks whose whole content is "schedule this". Also promotes a task to a calendar event once it gets a time. Use on /task, "add a task", "remind me to", "I need to", "put X in the queue", "I keep saying I'll meet up with X". For things that claim a time slot now, use /schedule instead.
---

# /task (v0.1)

The surface for things that need to **not be forgotten** but do not claim a slot.

Levi names the surface. "I need to book Dan" is a task even though the doing is scheduling.
Do not helpfully turn it into an event.

```
/task grab coffee with parker
/task deposit the check
/task book dan
```

## Read first

| | |
| --- | --- |
| Tag schema and the Tasks limits | `_shared/workspace-tags.md` |
| API facts | `_shared/google-workspace-mechanics.md` |

## The lists

| list | holds |
| --- | --- |
| **Scheduling queue** | things that want a time and do not have one — mostly people. The Parker case |
| **My Tasks** | loose items that live in no Collevity thread. Deposit the check, pick up the FL |

Anything big enough to be a standing arc belongs in the **thread registry** via
`/orchestrate intake`, not here. This is for residue — too small for a thread, too real to drop.

## What Tasks cannot do

**No tags. No color.** The resource is `title · notes · due · status · parent · position`.
Unknown fields are accepted by the API and silently discarded — a write that looks like it
worked did not. If domain matters on a task, put it in `notes` as a visible line.

`position` is sibling ordering, not metadata. `parent` is real one-level hierarchy — Tasks
has the nesting Calendar lacks, so use subtasks when something decomposes.

## Process

1. **Pick the list** from the two above. Ask only if it is genuinely ambiguous.
2. **Due date only if Levi gave one.** Do not invent deadlines — a due date makes the task
   appear on the calendar and start behaving like a commitment he did not make.
3. **Notes** carry the *why*, when there is one. "Thinking about getting baptized; needs
   discipleship" is worth more later than the bare title.
4. **Report** the list, the title, and whether it is dated.

## Promotion

When a queued task gets a time, hand it to `/schedule` and then **close the task** — do not
leave it open as a shadow of the event. Carry the notes across into the event description.

## Do not

| Don't | Do |
| --- | --- |
| Invent due dates | Undated is the honest state for most of this |
| Turn a task into an event to be helpful | He named the surface |
| Write structured metadata to a task | It is silently dropped. Use `notes` |
| Promote small items into registry threads | The registry is for standing arcs |
| Delete a list without reading it | Tasks deletion takes every task with it |

## Done when

- The item is on the right list, with notes if there was a reason
- Nothing got a due date Levi did not give
- He can find it on his phone
