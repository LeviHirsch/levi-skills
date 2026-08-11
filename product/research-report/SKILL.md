---
name: research-report
description: Walk through drafting and submitting a NascenTech/Haptic research brief (Levi structure). Use on /research-report, research brief, research report, start an RR, submit research brief, copy research template. Covers GDoc template copy, section coach, submit schema, PDF settle guidance. Employee- and agent-operable.
---

# /research-report (v0.1.0)

Structured research brief for company questions. **Levi’s five-section spine is fixed.**  
Working surface: **Google Doc**. Settled archive: **PDF only** (no docx history).

```
/research-report start …
/research-report draft …
/research-report submit …
/research-report settle …
/research-report status
/research-report feedback …
```

**IDs:** prefer `references/drive-ids.org.md` if present (server/org). Else `references/drive-ids.md` (personal dev).  
**Hub:** org = `mini@nascentech.com` on nascentech mini; personal dev = laptop only.

Skim `FEEDBACK.md` Open items on invoke.

---

## Refs

| | |
| --- | --- |
| IDs / paths | `drive-ids.org.md` (org) **or** `drive-ids.md` (personal) |
| Submit fields | `references/submit-schema.md` |
| Structure + modules | `references/structure.md` |
| Full process | shared-drive / iCloud `…/research-reports/PROCESS.md` |
| Feedback | `FEEDBACK.md` |

---

## Modes

| Mode | When | Behavior |
|---|---|---|
| **Interactive** | Human in chat / CLI | Section coach, ask gaps, promote user voice |
| **Agent-quiet** | Unattended / server | Defaults from context; only stop on hard gaps |

Same steps either way. Prefer **user phrasing** over polish rewrite.

---

## Commands

### `start` — open a working brief

1. Resolve **org unit**: Haptic (default for product questions) · NascenTech · other.  
2. Resolve **Core Question** (required). Soft: author, team code, origination, title.  
3. Early: preferred **submit route** (`skill_cli` default here; `form` if they want UI later).  
4. Copy template GDoc (`copy_drive_file`):
   - Haptic → template id in `drive-ids.md`
   - NascenTech → NT template  
   Destination: `working` folder (or org subfolder).  
5. Name: `[DRAFT] <short title> — <Author>`  
6. Report: Doc URL, name, route, next = draft sections.

Do **not** draft inside the template files themselves.

### `draft` — fill structure

Coach **one movement at a time** unless they dump a full draft.

Order:

1. Purpose & Scope (Context/Problem · Core Question)  
2. Brief  
3. Exploration (Landscape · Principles · Mechanisms)  
4. Application (Vision · Objectives · Immediate Steps)  
5. Conclusion (Synthesis · Extending Questions)  
6. Optional Sources / footnotes  

Then offer modules for **submit** (not forced on page 1):

- For Levi  
- Author reflection  
- Provenance (mostly me / mixed / mostly AI + tools)  

**Stance**

- Keep Levi structure; no redesign.  
- User voice > rewrite.  
- Delete grey cue lines as sections fill.  
- No hard “delete unopened sources”; capture provenance honesty.  
- Length soft only — don’t pad.

Update the working GDoc when tools allow (`update_drive_file` with md/docx content, or guide the human). If Docs update is awkward mid-session, keep a section buffer and write in batches.

### `submit` — process packet + log

Collect **submit schema** fields (`references/submit-schema.md`). Required minimum:

- `gdoc_url`, `title`, `author`, `org_unit`  
- `core_question_own_words`  
- `version_intent`  
- `submit_route`  
- `checklist_read_fully` = true  

Strongly recommend: `for_levi`. Soft: reflection, provenance, team_code, origination.

**Write a row** to the Submit Log sheet (`submissions` tab) via Sheets MCP (`modify_sheet_values` on next empty row, or append if table exists).  
`submitted_at` = ISO now.

If `version_intent` is `still_draft`: log only; **do not** settle PDF.

If settle-class intent: proceed to `settle` (or hand off steps).

### `settle` — PDF archive

Only when intent is first review / minor bump / major rescope.

1. Export working GDoc → **PDF** (`get_drive_file_download_url` with `export_format=pdf` when available).  
2. Name:

```text
RR-####-<TEAM>_<Title>_<AuthorFirstLast>_vMAJOR.MINOR_YYYY-MM-DD.pdf
```

3. Place under settle path for org (Haptic default in `drive-ids.md`).  
4. **No docx archive.**  
5. Primary = newest freeze for that `RR-####` (flat sort ok for now).  
6. Report path + version. Claim next `RR-####` by scanning library filenames if no registry.

### `status`

Summarize configured Drive IDs, submit log URL, last known draft if in session, settle path. Note org shared-drive not live on personal hub yet.

### `feedback`

→ `FEEDBACK.md` only (convention in `_shared/skill-feedback-convention.md`).

---

## Workspace integration (personal hub today)

| Action | Tool / method |
|---|---|
| Copy template | `copy_drive_file` |
| Read Doc | `get_drive_file_content` |
| Update Doc | `update_drive_file` (content replace — preserve file id) |
| Export PDF | `get_drive_file_download_url` + `export_format=pdf` |
| Submit log | Sheets `modify_sheet_values` on Submit Log |
| Form (UI) | Not creatable via current MCP — sheet is backend; see `references/form-setup.md` |

**Known gap:** native Google Docs **comments** not exposed to agents. Human review in GDoc UI; agent feedback via end-of-doc block or chat until custom commenter exists.

**Org target:** same skill on server CLI with shared Drive IDs swapped in `drive-ids.md` (viewable via `ssh nt` when ready). Personal paths remain valid for Levi solo use.

---

## Don't

| | |
|---|---|
| Redesign the five sections | Structure is Levi’s |
| Archive docx as history | PDF only |
| Draft in the template GDoc | Always copy first |
| Enforce hard length / source police | Soft + provenance |
| Require Slack | Not in use |
| Block on org shared Drive | Personal tree works; swap IDs later |
| Invent RR numbers without checking library | Scan existing `RR-####` |

---

## Done

Working GDoc exists · structure filled or in progress · submit fields logged when submitted · settle-class freezes as named PDF in library · user voice preserved · process modules not forced into page-1 chrome.
