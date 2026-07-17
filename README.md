# Shoreditch Design Studio — Claude Skills

Shared Claude Code skills for the studio. **Private repo** — see [Confidentiality](#confidentiality).

This is the single source of truth for studio skills. Everyone installs from here, so the work comes out consistent regardless of who ran it — that's the entire point. New studio skills belong in this repo, not in a client folder and not in a personal `~/.claude/skills/`.

## Install

```bash
git clone https://github.com/kgotiwale/Shoreditch-skills.git shoreditch-skills
cd shoreditch-skills
./install.sh
```

`install.sh` symlinks each skill into `~/.claude/skills/`, making them available in **every** project — which matters, because client work lives in client folders, not in here. Because they're symlinks, `git pull` updates everyone's skills in place.

Restart Claude Code after installing.

## Skills

### `ux-audit`

Granular, per-element UX audit of a product journey on desktop or mobile. Rates every element Red / Amber / Green and renders a shareable scorecard.

```
/ux-audit
```

Or just describe the work — "audit this checkout flow on mobile", "UX review of these screens" — and it triggers.

**Inputs:** screenshots, a live URL (driven via Playwright MCP), or Figma frames.

**Optional setup — only needed for the live-URL path:**

```bash
claude mcp add playwright npx @playwright/mcp@latest   # multi-viewport capture
```

Without it the skill still works from screenshots; it will say the capture path is unavailable rather than guessing at pages it can't see. Accessibility findings additionally lean on `npx @axe-core/cli` when a live URL is in scope — no install needed, it runs via npx.

**Output:** a published scorecard artifact — per-element findings, RAG tallies, lens breakdown, ranked critical pain points, platform filters.

**The six lenses:**

| Code | Lens |
|------|------|
| C1 | User Interface Design |
| C2 | Information Architecture |
| C3 | Interaction Design |
| C4 | Content |
| C5 | Functionality |
| C6 | Accessibility |

**The RAG scale:**

- 🟢 **Good** — intuitive; user acts without hesitation.
- 🟠 **Needs improvement** — task completes, but costs a re-read or an extra step.
- 🔴 **Critical** — blocks, erodes trust, shows wrong data, or excludes.

The rating thresholds and tie-breakers live in `skills/ux-audit/references/rubric.md`. That file is what makes two auditors agree — read it before disputing a rating.

Our three points aren't invented: [MeasuringU's Minor/Moderate/Critical](https://measuringu.com/rating-severity/) maps 1:1, and [Baymard's Interruption/Disruptive/Harmful](https://baymard.com/research/methodology) maps cleanly and is e-commerce-native. The one thing we *did* invent is **Green** — every published scale rates *problems*, and a non-problem never gets logged, so no established scale has a positive end. We rate elements, so we need one. Be honest about that in client conversations.

**Read this before quoting a number at a client:** the audit is a single evaluator, and the research on that is unflattering — ~35% problem detection, ~50% false alarms, and severity correlating at 0.24 between any two evaluators ([Hertzum & Jacobsen 2003](https://mortenhertzum.dk/publ/IJHCI2003.pdf)). Nielsen prescribes 3–5 evaluators reconciled. The rubric's tie-breakers attack the documented cause of false positives, but they don't make one evaluator equal three. Every deliverable says so in its footer. Don't let a scorecard get read as measurement.

```
skills/
└── ux-audit/
    ├── SKILL.md                      # trigger + workflow
    ├── references/
    │   ├── rubric.md                 # RAG thresholds, tie-breakers, calibration
    │   ├── heuristics-desktop.md     # hover, focus, keyboard, wide layouts, Norman
    │   ├── heuristics-mobile.md      # touch targets, gestures, safe areas, WCAG 2.2
    │   ├── journey-mapping.md        # captures → states, collapsing repeats
    │   ├── cognitive-walkthrough.md  # Norman's 7 questions, Krug's trunk test
    │   └── deceptive-patterns.md     # dark patterns, and where the line sits
    └── assets/
        └── scorecard-template.html   # the deliverable
```

Thresholds are cited to primary sources throughout, because the near-misses bite: Apple's 44**pt** and WCAG 2.5.5's 44**px** are unrelated standards and the latter is **AAA** — the AA floor is **24px** (SC 2.5.8, five exceptions). Contrast is 4.5:1 text / 3:1 large text / 3:1 non-text; applying 4.5:1 to a border is a false positive. Don't loosen a citation without checking the source.

### `workshop-synthesis`

Photos of an in-person customer workshop — sticky walls, affinity clusters, dot-voted boards, flipcharts — into a stakeholder readout.

```
/workshop-synthesis
```

Or describe it — "summarise the workshop", "write up these stickies" — and it triggers.

**Inputs:** photos. It refuses to synthesise from a verbal recollection of a session; that's someone's memory, not the room's output. It also asks for the activity prompts, the customer/internal split, and what decision the readout feeds — a note answering *"what frustrates you?"* is different evidence from an unprompted one.

**Output:** a readout — themes with note-level evidence, prioritisation, rejected ideas, single-source signals, open questions, an ambiguity ledger, and method limitations.

**The three passes** are the whole skill, and the rule is that they never merge:

| Pass | Produces | Status |
|------|----------|--------|
| 1. Transcribe | what is physically on the board, note by note | **Data** |
| 2. Cluster | groupings — the room's own, wherever they exist | **Findings** |
| 3. Interpret | themes, readings, recommendations | **Insight** |

[NN/g's ladder](https://www.nngroup.com/articles/data-findings-insights-differences/). A photographed sticky, a cluster, and a theme name are three different epistemic objects, and collapsing them is how a facilitator's pet theory ends up wearing a customer's clothes. Every claim in the output cites note IDs (`W1-N014`), so a sceptic can open the photo and check — anything that can't is tagged `Me:` ([NN/g's convention](https://www.nngroup.com/articles/group-notetaking/)) or cut.

**The room's clustering is authoritative — the skill will not re-cluster.** If participants grouped notes physically, that grouping *is* the finding. It only clusters where the wall is genuinely ungrouped.

**Unreadable handwriting comes back to you marked on the photo**, not as a ledger line you can't act on:

```bash
python3 skills/workshop-synthesis/scripts/annotate.py --image WALL.jpg --marks marks.json
```

Boxes every uncertain note in magenta with its ID and a legend strip saying what's needed. This happens *before* clustering — a theme built on a guessed note has to be rebuilt once corrected, so guesses get resolved while they're still cheap.

```
skills/
└── workshop-synthesis/
    ├── SKILL.md              # the three passes, output, quality bar
    └── scripts/
        └── annotate.py       # mark unreadable notes for a human to decipher
```

**Two rules here are counter-intuitive, and both are cited — don't "fix" them:**

- **No minimum cluster size.** A single note is a legitimate finding. [NN/g is explicit](https://www.nngroup.com/articles/affinity-diagram/) that small clusters signal diverse perspectives, and *Contextual Design* caps first-level groups at **four** — so a fat pile is a signal to **split**, not a strong theme. Frequency is a property of a theme, never its entry ticket.
- **Counts scope evidence; they never project rates.** "7 of the 10 participants in this session", never "70% of customers". [NN/g argues against](https://www.nngroup.com/articles/actionable-usability-findings/) even the "three users couldn't find it" framing — it reads as blaming users and invites dismissal. Rank by severity.

**Read this before promising a client a readout from photos:** handwriting OCR is unreliable enough that the [CHI 2019 team](https://chi2021.acm.org/contents/wp-content/uploads/example_papers/Subramonyam-LaTeX-Single-Column.pdf) who built a sticky-note capture system declined to use it at all, using fiducial markers instead — and no vendor publishes an accuracy figure. Hence flag-and-ask over guess. Photo quality caps output quality: brief whoever shoots the walls with the capture guidance at the end of `SKILL.md` (wide shot per wall first, camera parallel, un-overlap the notes, capture the legend and the prompt) — most of it is unrecoverable afterwards.

## Adding a new skill

```
skills/<skill-name>/
├── SKILL.md          # required: frontmatter (name, description) + the workflow
├── references/       # optional: split out bulk the skill loads on demand
└── assets/           # optional: templates, deliverables
```

The `description` in frontmatter is what decides whether the skill triggers — write it as the situations it applies to, not as a title. Re-run `./install.sh` to link a newly added skill.

Two conventions this repo holds to:

**Examples stay client-neutral.** Generalise to the archetype — "category header states its surcharge", never "ACME's LINEN +£10 label". Keep the concreteness; drop the client. Vague examples calibrate nothing, but client-specific ones tie a shared skill to one product's vocabulary and leak engagement detail into a repo other people read. Generalise on the way in — retrofitting leaves the original wording in git history forever.

**Say what you can't do.** Where a skill depends on tooling that might be absent, it must refuse and ask rather than degrade silently. `ux-audit` will not fetch static HTML and infer a JS app's screens; it stops and requests screenshots. A confident answer about something never observed is the worst output any of these can produce.

## Changing a skill

Skills are studio standards, so treat edits like standards changes:

1. Branch, edit, open a PR.
2. If you're changing `rubric.md`, say what it re-rates. Threshold changes silently reclassify past findings and break comparability between decks.
3. The scorecard template's CSS is deliberately client-neutral. Restyling per client defeats the point — only the data and header meta should change per engagement.

## Confidentiality

**This repo is private and should stay private.** The working tree is client-neutral, but the git history isn't: commits before `394a0f2` contain a named client's audit findings verbatim, from before the calibration examples were generalised. `git log -p` surfaces them.

Making this public would require rewriting history first — which gets painful once teammates have cloned. If public release is ever on the table, raise it before adding collaborators, not after.
