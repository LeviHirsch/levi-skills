# Promotion guide — `01_promotion.md`

How to **think** then **write** the promotion layer. Skill step 6 requires this.

Promotion is **lossy**: resume + durable locks + pointers.  
Threaded = diary. Raw = truth. Wrong layer = thrash on cold open.

---

## Readers (priority)

1. Tired future Levi — first move?  
2. `/orchestrate` / registry — slug, state, resume-point, registry yes/no  
3. Curious future Levi — what not to re-argue  
4. Forensics — pointers only, not a rewrite  

If a sentence fails 1–3 → threaded or nowhere.

---

## Process (before typing)

**Extract → rank → write.** Do not stream from an empty template.

| Step | Do |
| --- | --- |
| **A Crown** | One sentence: primary next move, multi-arc ranking, or "closed clean" → **At a glance** |
| **B Open arcs** | Inventory unfinished work; rank P0/P1/P2 |
| **C Settled** | Only lines that would make future-you choose *worse* if missing |
| **D Keep** | Expensive framing only (or skip) |
| **E Landed** | Paths resume needs (or skip); memory files go here |
| **F Notes** | ≤3 landmines/posture (or skip); never "please review draft" |
| **G Length** | Target 40–90 lines; soft cap 120; omit empty sections |
| **H Check** | Open threads alone enough to resume? Open first? One first-move per P0? No re-paste of linked docs? OK at 11pm? |

### Rank

| | Meaning | In file |
| --- | --- | --- |
| **P0** | Must not lose | Full block; usually `registry: yes` |
| **P1** | Real, not standing alone | Under detail or block with `registry: no` |
| **P2** | Mention / expired | Drop or one Notes line |

**Cap:** ≤3 `registry: yes` unless Levi wants more.

---

## Template

Delete sections with nothing real to say.

```markdown
# <Title Case slug>

**When:** <YYYY-MM-DD[, window]>
**Who:** Levi, <model>
**Package:** `<…/claude_session-persistent-packages/<folder>/>`
**Siblings:** [02_threaded.md](02_threaded.md) · [03_raw.jsonl](03_raw.jsonl) (<size>)

> **At a glance:** <next move or closed clean>

## Open threads

### `thread-slug` — <short title>
- **state:** active | blocked | dormant | done
- **resume-point:** <ONE glance line>
- **registry:** yes | no
- **detail:**
  - <cold-start facts>
  - <ordered steps if order matters>
  - **Do not:** <wrong re-entry if common>

## Keep (do not re-derive)
- <expensive framing; prefer "see path X">

## Settled
- **<Name>** — <one-line durable lock>

## Landed
- `<path>` — <what it is>

## Notes
- <≤3 load-bearing bullets>
```

Tiny arc form: `- [\`slug\` | blocked | registry:yes] <resume-point>`

Header extras only if needed: cwd-slug note · supersedes · multi-day span.  
No second Cross-refs section that only repeats Siblings.

---

## Section jobs

| Section | Job | Not |
| --- | --- | --- |
| At a glance | Crown / closed | Arc novel |
| Open threads | Cold resume + registry feed | Unranked backlog |
| Keep | Protect framing | Repeat open-thread detail |
| Settled | Durable locks | Play-by-play, "we closed" |
| Landed | Find artifacts | Every touch |
| Notes | Landmines / posture | Draft ceremony, restating open threads |

**Retired:** mandatory "Captured to memory" (use Landed when real).

---

## Quality

**Good resume-point:** `D-004 mint paste-back; then live verify + close`  
**Bad:** `Continue cas` · whole paragraphs (→ detail)

**Good detail:** named gate, commands/paths, already-done, **Do not**  
**Bad:** re-derive design, bullet farm, stale dates without flag

**Multi-arc:** P0 first; secondary blocks or `registry: no`; time-sensitive noise → Notes, not peer P0s.

---

## Anti-patterns

1. Diary before Open threads  
2. Empty ceremony (`None` sections)  
3. 8–15 peer open bullets  
4. Decisions as play-by-play  
5. Duplicate cross-refs  
6. Draft meta in the file  
7. Tool-call / turn narrative in promotion  
8. No single crown (competing priorities)  
9. Re-pasting docs that should be links  
10. Everything `registry: yes`

---

## Example (shape)

```markdown
# Cas Verify Mint Paste Blocker

**When:** 2026-07-22 (from 2026-06-30)
**Who:** Levi, claude-opus-4-8
**Package:** `…/2026-07-22-1742_cas-verify-mint-paste-blocker__-Users-levi/`
**Siblings:** [02_threaded.md](02_threaded.md) · [03_raw.jsonl](03_raw.jsonl) (~1.0 MB)

> **At a glance:** Blocked on D-004 mint paste-back; then verify + close.

## Open threads

### `cas-verify` — mint paste-back
- **state:** blocked
- **resume-point:** Implement D-004 (pty `code#state` paste-back); live `/spec verify` AC2.x; `/spec close`.
- **registry:** yes
- **detail:**
  - Gate: `cas mint()` never prompts/writes paste-back.
  - On close also record Phase5→iter2; AC3.6/4.2 live PASS.
  - **Do not:** mocked-only verify as proof add works.

## Settled
- **DEC-017** — setup-token uses remote callback + manual paste-back.

## Landed
- `…/claude-account-switcher/spec/` — deferred D-004; verified-not-closed.
```

---

## Layers

| | Promotion does |
| --- | --- |
| Threaded | Link via Siblings; no turn dump |
| Raw | Size only |
| Registry | Feed from Open threads fields |
| Memory/specs | Link under Keep/Landed |
