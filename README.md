# Shoreditch Design Studio — Claude Skills

Shared skills for the studio. Source of truth lives here; everyone installs from this repo so audits come out the same regardless of who ran them.

## Install

```bash
git clone <remote-url> shoreditch-skills
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

## Changing a skill

Skills are studio standards, so treat edits like standards changes:

1. Branch, edit, open a PR.
2. If you're changing `rubric.md`, say what it re-rates. Threshold changes silently reclassify past findings and break comparability between decks.
3. The scorecard template's CSS is deliberately client-neutral. Restyling per client defeats the point — only the data and header meta should change per engagement.

## Repo layout

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
