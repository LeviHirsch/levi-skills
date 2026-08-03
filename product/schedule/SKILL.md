---
name: schedule
description: Put something on Levi's Google Calendar from a loose natural-language description — pick the calendar, set the time, tag it by domain, apply color. Use on /schedule, "put X on the calendar", "schedule X", "add X to my calendar", "block time for X", or when Levi describes an event that should exist. For things that need doing but claim no time, use /task instead. For reconstructing a past day, use /log.
---

# /schedule (v0.3)

One loose sentence → one (or a clearly named series of) calendar events.

**He names the surface.** If he said calendar / schedule / put it on the calendar, do that.
Do not re-route into a task. Do not invent extra blocks. Only place what he asked for or what
already has a real time attached.

```
/schedule lunch with cody tuesday noon at st elmos
/schedule sabrina mon+thu 945-130, fri 945-5, next three weeks
/schedule call with quinn and autumn 830am their time (NZ) monday
/schedule feedback …
```

## Read first

| | |
| --- | --- |
| Tags | `_shared/workspace-tags.md` |
| Color map (provisional) | `_shared/domains.json` |
| API + access map | `_shared/google-workspace-mechanics.md` |
| Feedback Open | `FEEDBACK.md` |
| Hub OAuth | `levihirsch0@gmail.com` · `~/.config/collevity/gcal/` |

Skim FEEDBACK Open. Honor prefer / dislike.

Tags need the **raw Calendar API** (`workspace-mcp` cannot write `extendedProperties`). Scripts
stay live until a shape repeats; the skill is the milestone.

## Process

### 1. Parse

Title, date, start, end/duration, location, recurrence, attendees, calendar hint, timezone,
domain if obvious.

- Resolve dates/weekdays **with code**, not in your head. Weekday + date both given → verify
  they match; if not, stop and ask.
- Timezones via `zoneinfo`. Default context: America/New_York unless he said otherwise. When
  sides differ (e.g. NZ), report which local calendar day each side lands on.
- **Title:** his words, human. No tag prefixes, no naming scheme of your own. He has not
  locked a title convention — do not invent one.

### 2. Pick the calendar

You are choosing a **calendar under the hub account**, not switching Google accounts.
OAuth is always `levihirsch0@gmail.com`. Resolve the calendar id by its summary/title at runtime.

**Signal order — stop at the first solid hit:**

1. **He names it** ("on nascentech", "Haptic", "primary", a calendar title).
2. **Content of the event:**

   | calendar | when |
   | --- | --- |
   | primary (`levihirsch0`) | personal, family, friends, faith, home, unmarked default |
   | `levi@nascentech.com` | NascenTech work (external 1:1s, Sabrina-style blocks, company-facing) |
   | `Haptic Info/Admin` | whole Haptic team should see it — **writer; mail can fan out via Groups** |

3. **Still unclear** — glance at a few recent events on the candidate calendars and match
   shape (how the first real week was disambiguated), **or** ask once. Do not interview.

**Off limits for this skill**

- `ACTUAL - transcribed from log` → `/log` only
- `levi@nascen.tech` → decommission path; do not add new work there
- **Do not use a separate calendar per domain.** Domains are tags + color, not calendars.

State which calendar you picked in the report.

### 3. Fill gaps

Ask about **times and people**. Guess the rest; say what you guessed. Keep the back-and-forth
short.

- No end → sane duration (often ~1h; keep longer when the event kind or he implies it), state it.
- Location / description missing → leave empty.
- Domain → observe; do not interrogate. Free text; map is provisional (see tags doc).
- Attendees → **only with an explicit yes.** `sendUpdates` defaults to `all`. Confirm the list
  out loud before write. Addresses that look like people are often **Groups**.

### 4. Write (raw API when tagging)

| field | value |
| --- | --- |
| `cv_schema` | `v1` |
| `cv_source` | `schedule` |
| `cv_domain` | free text that fits |
| `cv_sub` | optional |
| `colorId` | `domains.json` if mapped, else `_fallback` |
| `sendUpdates` | `none` unless attendees approved |

Optional and **not UI-visible** for events you own — set only when he asked or it clearly fits;
do not treat as a signal he will see:

- `status: tentative` if he said tentative / soft / not locked
- `transparency: transparent` if he wants a soft free block

Do not invent a free/busy policy on your own.

### 5. Report

One short screen: when, which calendar, domain/color, guesses. Stop.

## Recurrence

Mechanics doc first. Three traps:

1. No `UNTIL` → runs to ~2040. Cap or say it is unbounded.
2. Different times on different weekdays → **separate series**.
3. End series, keep history → PATCH `UNTIL`. Parent delete kills the past.

## Modes

| | |
| --- | --- |
| `/schedule …` | do the event work |
| `/schedule feedback …` | `FEEDBACK.md` only |

## Do not

| Don't | Do |
| --- | --- |
| Flag overlaps / "collisions" | Overlap is often fine (call in the car, soft blocks) |
| Propose blocks he did not ask for | Only what he asked or what already has a real time |
| Put tags in the title | Title stays human |
| Re-ask what he already answered | Check silently; speak only if it disagrees |
| Add attendees to be helpful | Explicit approval only |
| Force a domain from the map | Free text; map is adjustable |
| Write to ACTUAL or nascen.tech | Wrong calendars |
| Route by domain-as-calendar | Tags + color, one (or few) calendars |

## Done when

Event on the right calendar at the right time; tags + color set; guesses stated; no surprise email.
