---
name: schedule
description: Put something on Levi's Google Calendar from a loose natural-language description — pick the calendar, set the time (fuzzy OK), tag it by domain, apply color. Use on /schedule, "put X on the calendar", "schedule X", "add X to my calendar", "block time for X", or when Levi describes an event that should exist. Precise clock not required. For things that need doing but are not yet events, use /task instead. For reconstructing a past day, use /log.
---

# /schedule (v0.6.1)

Loose sentence → plan-calendar event(s). **He names the surface** — if he said calendar /
schedule / put it on the calendar, do that. Do not re-route into a task. Only create what he
asked for — not extra "helpful" blocks.

**When can be fuzzy.** "Tuesday afternoon", "next three weeks", "830 their time" are enough;
guess end/duration when missing, state the guess. Ask only when the when-window is truly
unusable (no day, no range, weekday+date conflict).

Suite map: `~/.claude/skills/_shared/surfaces.md`. Not on calendar yet → `/task`. Past day →
`/log`. Standing arc → `/orchestrate`. **Never** write ACTUAL here.

```
/schedule lunch with cody tuesday noon at st elmos
/schedule sabrina mon+thu 945-130, fri 945-5, next three weeks
/schedule call with quinn and autumn 830am their time (NZ) monday
/schedule feedback …          → FEEDBACK.md only
```

## Refs

| | |
| --- | --- |
| Suite surfaces | `~/.claude/skills/_shared/surfaces.md` |
| Tags / visibility | `~/.claude/skills/_shared/workspace-tags.md` |
| Color map (provisional) | `~/.claude/skills/_shared/domains.json` |
| API, access, calendar pick | `~/.claude/skills/_shared/google-workspace-mechanics.md` |
| Feedback Open | `FEEDBACK.md` (skim on invoke) |
| Hub OAuth | `levihirsch0@gmail.com` · `~/.config/collevity/gcal/` |

Tags need the **raw Calendar API** (MCP cannot write `extendedProperties`). Scripts stay
live until a shape repeats.

## Steps

**1. Parse** — title, when, duration/end, location, recurrence, attendees, calendar hint,
timezone, domain if obvious.

- Dates/weekdays with **code**, not memory. Weekday + date disagree → stop and ask.
- Timezones: `zoneinfo`; default America/New_York unless he said otherwise. Cross-zone →
  report both local days.
- Title = his words. No tag prefixes. No naming scheme of your own.

**2. Calendar** — pick a calendar under the hub account (not a different login). Full rules
in mechanics; short form:

1. He names it → that one  
2. Else content: primary (personal default) · `levi@nascentech.com` (NascenTech work) ·
   `Haptic Info/Admin` (whole team; mail can fan out)  
3. Still unclear → sample recent events on candidates, or ask once  

Never: `ACTUAL…` (`/log` only), `nascen.tech`, or one-calendar-per-domain. Resolve id by title.

**3. Gaps** — short replies. Guess freely where the cost of being wrong is low; **state guesses**.

- Fuzzy when → place a reasonable block (or short series); say what you assumed  
- No end → ~1h (or longer if obvious); state it  
- No clock but a day/window → pick a sane start inside the window; state it  
- Truly no when at all and he still said "calendar" → ask once for a window, not a full interview  
- Location/description empty is fine  
- Domain free text; map is provisional  
- Attendees only with explicit yes (`sendUpdates` defaults to `all`; Groups fan out)  
  (people are the high-cost gap — not clock precision)

**4. Write** (raw API for tags)

| | |
| --- | --- |
| `cv_schema` / `cv_source` / `cv_domain` | `v1` / `schedule` / free text |
| `cv_sub` | optional |
| `cv_origin` | `task` if promoted from `/task`; omit otherwise |
| `colorId` | map or `_fallback` |
| `sendUpdates` | `none` unless attendees approved |

`cv_source` is always `schedule` here — it records **who wrote the event**, not where the idea
came from. Origin goes in `cv_origin`.

`status: tentative` and `transparency: transparent` only when he asked or it clearly fits —
**not visible** in the UI for events he owns. Do not invent a free/busy policy.

**5. Report** — when, calendar, domain/color, guesses. One screen. Stop.

## Recurrence

See mechanics. Traps: no `UNTIL` → ~2040; different times per weekday → separate series;
end and keep past → PATCH `UNTIL` (parent delete kills history).

## Don't

| | |
| --- | --- |
| Flag overlaps | Often fine |
| Propose unasked blocks | Only what he asked to put on the calendar |
| Tags in title | Human title only |
| Re-ask answered facts | Check silently |
| Helpful attendees | Explicit yes only |
| Shoehorn domain / domain-as-calendar | Free text + color on the right calendar |
| Write ACTUAL or nascen.tech | Wrong calendars |

## Done

Right calendar and time · tags + color · guesses stated · no surprise email.
