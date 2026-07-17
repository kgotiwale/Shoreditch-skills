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

**Inputs:** screenshots, a live URL (driven via browser automation), or Figma frames.

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

## Changing a skill

Skills are studio standards, so treat edits like standards changes:

1. Branch, edit, open a PR.
2. If you're changing `rubric.md`, say what it re-rates. Threshold changes silently reclassify past findings and break comparability between decks.
3. The scorecard template's CSS is deliberately client-neutral. Restyling per client defeats the point — only the data and header meta should change per engagement.

## Repo layout

```
skills/
└── ux-audit/
    ├── SKILL.md                    # trigger + workflow
    ├── references/
    │   ├── rubric.md               # RAG thresholds, tie-breakers, calibration
    │   ├── heuristics-desktop.md   # hover, focus, keyboard, wide layouts
    │   ├── heuristics-mobile.md    # touch targets, thumb zone, gestures, safe areas
    │   └── journey-mapping.md      # captures → states, collapsing repeats
    └── assets/
        └── scorecard-template.html # the deliverable
```
