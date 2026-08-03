---
name: task
description: Capture something into Google Tasks that needs doing but claims no time yet — including tasks whose whole content is "schedule this". Also promotes a task to a calendar event once it gets a time. Use on /task, "add a task", "remind me to", "I need to", "put X in the queue", "I keep saying I'll meet up with X". For things that claim a time slot now, use /schedule instead.
---

# /task (v0.4)

Must not forget · no calendar slot yet. **He names the surface.** "Book Dan" stays a task
even if the doing is later scheduling — do not turn it into an event to be helpful.

```
/task grab coffee with parker
/task deposit the check
/task book dan
/task feedback …              → FEEDBACK.md only
```

## Refs

| | |
| --- | --- |
| Tasks limits | `~/.claude/skills/_shared/workspace-tags.md` |
| API | `~/.claude/skills/_shared/google-workspace-mechanics.md` |
| Feedback Open | `FEEDBACK.md` (skim on invoke) |
| Hub OAuth | `levihirsch0@gmail.com` · `~/.config/collevity/gcal/` |

Same hub as calendar. Pick a **list** (id by title), not another Google login. Create a list
only if he asked for that name.

## Lists

| list | holds |
| --- | --- |
| **Scheduling queue** | wants a time, does not have one (people, "book X") |
| **My Tasks** | other to-dos (errands, deposit the check) |

Standing arcs → `/orchestrate intake`. This is small residue only.

## Limits

Resource: `title · notes · due · status · parent · position · links`.

No tags, no color. Unknown fields **silently drop**. Domain (if any) → a line in `notes`.

- `parent` = one-level subtasks  
- Due date → shows on Calendar UI; undated stays in the side panel. **Due only if he gave one.**

## Steps

1. Pick list. Ask only if ambiguous.  
2. Due only if he said a date.  
3. Notes = why/context when he gave any.  
4. Write (Tasks API / MCP fine).  
5. Report: list, title, dated?. Stop.

## Promote → `/schedule`

When **he** gives a time or says schedule it now:

1. `/schedule` (title, notes, time)  
2. Event gets `cv_source=schedule` + `cv_origin=task` — source = who wrote it, origin = where
   it came from  
3. **Close the task** — no open shadow  
4. Notes → event description  

Do not promote on your own.

## Don't

| | |
| --- | --- |
| Invent due dates | Undated is fine |
| Task → event to help | He named Tasks |
| Fake metadata fields | Silently dropped; use notes |
| Small stuff → thread registry | Registry = standing arcs |
| Delete a list unread | Wipes every task |
| Leave promoted task open | Close after event exists |
| Propose calendar blocks here | `/schedule` when he asks |

## Done

Right list · honest due (or none) · notes if he had a why · findable on phone.
