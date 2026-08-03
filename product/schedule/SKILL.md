---
name: schedule
description: Put something on Levi's Google Calendar from a loose natural-language description — pick the calendar, set the time, tag it by domain, apply color. Use on /schedule, "put X on the calendar", "schedule X", "add X to my calendar", "block time for X", or when Levi describes an event that should exist. For things that need doing but claim no time, use /task instead. For reconstructing a past day, use /log.
---

# /schedule (v0.1)

Take one loose sentence and turn it into a correctly-placed, correctly-tagged calendar event.

Levi names the surface. If he said "calendar," do not second-guess it into a task.

```
/schedule lunch with cody tuesday noon at st elmos
/schedule sabrina mon+thu 945-130, fri 945-5, next three weeks
/schedule call with quinn and autumn 830am their time (NZ) monday
```

## Read first

| | |
| --- | --- |
| Tag schema | `_shared/workspace-tags.md` |
| Domain -> color | `_shared/domains.json` |
| API facts | `_shared/google-workspace-mechanics.md` |

`workspace-mcp` **cannot write tags.** Use the raw Calendar API with the stored token.
Scripts are written live for now; only promote one to a file when the same shape repeats.

## Process

### 1. Parse

Pull out: title, date, start, duration, location, recurrence, attendees, calendar hint.

Resolve dates and weekdays **computationally**, never mentally. If the input names both a
weekday and a date, verify they agree; if they disagree, stop and ask. Same for timezones —
convert with `zoneinfo`, and report which calendar day each side lands on.

### 2. Route to a calendar

Ask only if genuinely unclear. The signal is usually in the content.

| goes to | when |
| --- | --- |
| `levihirsch0` (primary) | personal, relational, faith, family, anything unmarked |
| `levi@nascentech.com` | NascenTech-facing meetings |
| `Haptic Info/Admin` | anything the whole Haptic team should see — **writer, and it mails everyone** |
| a specific other | only when Levi names it |

### 3. Fill the gaps

Ask about **times and people**. Guess everything else and say you guessed.

- No end time -> pick a sane duration, state it, move on. Levi will correct it or won't.
- Missing location, description, color -> leave empty. All are cheap to add later.
- Attendees -> **never add without an explicit yes.** Adding them mails them immediately;
  `sendUpdates` defaults to `all`. Confirm the recipient list out loud before writing.

### 4. Write

Set on create:

- `cv_schema=v1`, `cv_source=schedule`, `cv_domain=<observed>`, `cv_sub` if obvious
- `colorId` from `domains.json`; unmapped domain -> `_fallback`, do not error, do not ask
- `transparency: transparent` for soft blocks Levi should see but not be blocked by
- `status: tentative` when it is a projection rather than a commitment
- `sendUpdates=none` unless attendees were explicitly approved

Domains are **observed, not enforced**. A new domain is legal the first time it is used.
Never refuse a domain because it is missing from `domains.json`.

### 5. Report

Time, calendar, domain, and anything you guessed. One screen. Then stop.

## Recurrence

Read the recurrence section of the mechanics doc before touching a series. The three that
bite:

1. No `UNTIL` means it runs to ~2040. Ask for a horizon or say out loud that it is unbounded.
2. Different times on different weekdays needs **separate series** — one RRULE, one time.
3. To end a series while keeping its past: PATCH `UNTIL`. Deleting the parent destroys history.

## Do not

| Don't | Do |
| --- | --- |
| Flag overlaps as conflicts | Let them overlap. Levi knows his life; overlap is often accurate |
| Propose extra blocks he did not ask for | Create what was asked. Nothing else |
| Put tags in the title | Title stays human; tags go in `extendedProperties` |
| Re-ask something he already answered | Verify silently; speak only if the check disagrees |
| Add attendees to be helpful | Never without explicit approval — it sends mail |
| Refuse an unrecognized domain | Use it. The vocabulary is observed |

## Done when

- The event exists on the right calendar with the right time
- It carries `cv_schema`, `cv_source`, `cv_domain`, and a color
- Every guess you made was stated
- Nobody got emailed who was not approved
