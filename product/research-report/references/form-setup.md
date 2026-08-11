# UI Form setup (bare functional)

**Why this file exists:** workspace-mcp cannot create Google Forms. The skill does **not** depend on a Form — it writes the Submit Log sheet directly.

A Form is the **dumbed-down UI path** for people who will not use CLI/skill.

## Already live

| Artifact | URL |
|---|---|
| Submit Log sheet | https://docs.google.com/spreadsheets/d/1PG3sMTPQCZ1sXVHObq5uxE-fajRM1aOfuhm_tQyA8pE/edit |

Headers match `submit-schema.md`.

## Option A — Manual Form (fast)

1. forms.google.com → Blank  
2. Title: `Research Brief — Submit`  
3. Add questions matching schema labels (see SUBMIT-SCHEMA in process folder).  
4. Responses → Select response destination → **Select existing spreadsheet** → the Submit Log above.  
5. Map question order to columns (Form will add its own timestamp column — either align or treat Form responses as a second tab).

**Note:** Google Forms often creates a new tab with Form-native headers. Prefer Option B if you want exact column keys.

## Option B — Apps Script one-shot (exact fields)

1. Open the Submit Log spreadsheet.  
2. Extensions → Apps Script.  
3. Paste `create-submit-form.gs` from this folder.  
4. Run `createResearchBriefSubmitForm` once (authorize).  
5. Script creates Form + links responses to `submissions` tab (or documents the Form URL).  
6. Put Form URL into `_meta!form_url` and `drive-ids.md`.

## Branded fork (optional later)

Functionality first. Branding (marks, colors) can wrap the same field list without changing schema.

## Skill behavior

- `submit_route=skill_cli` → skill writes sheet.  
- `submit_route=form` → human used Form; skill may only verify/settle if asked.
