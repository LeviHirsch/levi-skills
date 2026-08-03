---
name: schedule
description: Put something on Levi's Google Calendar from a loose natural-language description — pick the calendar, set the time, tag it by domain, apply color. Use on /schedule, "put X on the calendar", "schedule X", "add X to my calendar", "block time for X", or when Levi describes an event that should exist. For things that need doing but claim no time, use /task instead. For reconstructing a past day, use /log.
---

# /schedule (v0.2)

Take one loose sentence and turn it into a correctly-placed, correctly-tagged calendar event.

Levi names the surface. If he said "calendar," do not second-guess it into a task.

```
/schedule lunch with cody tuesday noon at st elmos
/schedule sabrina mon+thu 945-130, fri 945-5, next three weeks
/schedule call with quinn and autumn 830am their time (NZ) monday
/schedule feedback …
```

## Read first

| | |
| --- | --- |
| Tag schema | `_shared/workspace-tags.md` |
| Domain → color | `_shared/domains.json` |
| API facts | `_shared/google-workspace-mechanics.md` |
| Feedback (Open) | `FEEDBACK.md` in this folder |
| Hub account | `levihirsch0@gmail.com` |
| Creds | `~/.config/collevity/gcal/` |

Skim **FEEDBACK.md → Open** on invoke; honor `prefer` / `dislike`.

`workspace-mcp` **cannot write tags.** Use the raw Calendar API with the stored token
(see mechanics). MCP is fine for plain reads and simple untagged CRUD.

Scripts are written live for now. Promote a script to a file only when the same shape
repeats often enough to earn it. The skill is the milestone; durable scripts are not.

## Process

### 1. Parse

Pull out: title, date, start, duration / end, location, recurrence, attendees, calendar hint,
timezone if any, domain if obvious.

Resolve dates and weekdays **computationally**, never mentally. If the input names both a
weekday and a date, verify they agree; if they disagree, stop and ask. Convert timezones with
`zoneinfo` (default calendar context: America/New_York unless the input says otherwise) and
report which calendar day each side lands on when zones differ.

### 2. Route to a calendar

Ask only if genuinely unclear. The signal is usually in the content.

| goes to | when |
| --- | --- |
| `levihirsch0` (primary) | personal, relational, faith, family, anything unmarked |
| `levi@nascentech.com` | NascenTech-facing meetings |
| `Haptic Info/Admin` | anything the whole Haptic team should see — **writer, and it mails everyone** |
| a specific other | only when Levi names it |

**Never write intent/future events to `ACTUAL - transcribed from log`.** That calendar is
`/log` only.

### 3. Fill the gaps

Ask about **times and people**. Guess everything else and say you guessed.

- No end time → pick a sane duration (default ~1h unless the kind of event implies otherwise),
  state it, move on. Levi will correct it or won't.
- Missing location or description → leave empty. Cheap to add later.
- Domain → observe from content; do not interrogate. New domains are legal.
- Attendees → **never add without an explicit yes.** Adding them mails them immediately;
  `sendUpdates` defaults to `all`. Confirm the recipient list out loud before writing.
  Attendee addresses that look like people are often Google **Groups** (fan-out).

### 4. Write

Set on create (raw API when tags are involved):

| field | value |
| --- | --- |
| `extendedProperties.private.cv_schema` | `v1` |
| `extendedProperties.private.cv_source` | `schedule` |
| `extendedProperties.private.cv_domain` | observed free text |
| `extendedProperties.private.cv_sub` | if obvious; optional |
| `colorId` | from `domains.json` for that domain; else `_fallback` — do not error, do not ask |
| `sendUpdates` | `none` unless attendees were explicitly approved |

Optional machine fields (set when the case fits; **not visible in the Google UI** for events
you own — do not rely on them as a signal Levi will see):

- `status: tentative` when he said tentative / soft / not locked
- `transparency: transparent` when he wants a soft block that should not look busy

Domains are **observed, not enforced**. Never refuse a domain because it is missing from
`domains.json`.

### 5. Report

One screen: time, calendar, domain, color, and anything you guessed. Then stop.

## Recurrence

Read the recurrence section of the mechanics doc before touching a series. The three that bite:

1. No `UNTIL` means it runs to ~2040. Ask for a horizon or say out loud that it is unbounded.
2. Different times on different weekdays need **separate series** — one RRULE, one time.
3. To end a series while keeping its past: PATCH `UNTIL`. Deleting the parent destroys history.

## Modes

| Command | What |
| --- | --- |
| `/schedule …` | create / update as asked |
| `/schedule feedback …` | append taste to `FEEDBACK.md` only; do not schedule |

Feedback convention: `_shared/skill-feedback-convention.md`.

## Do not

| Don't | Do |
| --- | --- |
| Flag overlaps as conflicts | Let them overlap. Overlap is often accurate |
| Propose extra blocks he did not ask for | Create what was asked. Nothing else |
| Put tags in the title | Title stays human; tags go in `extendedProperties` |
| Re-ask something he already answered | Verify silently; speak only if the check disagrees |
| Add attendees to be helpful | Never without explicit approval — it sends mail |
| Refuse an unrecognized domain | Use it. Vocabulary is observed |
| Write to the ACTUAL calendar | That is `/log` |
| Treat tentative / free-busy as UI-visible | They are not; surface state in the report if it matters |

## Done when

- The event exists on the right calendar with the right time
- It carries `cv_schema`, `cv_source`, `cv_domain`, and a color
- Every guess you made was stated
- Nobody got emailed who was not approved
