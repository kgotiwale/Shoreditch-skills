---
name: ux-audit
description: Run a granular, per-element UX audit of a product journey on desktop or mobile, rating every element Red/Amber/Green across six lenses (C1 UI Design, C2 Information Architecture, C3 Interaction Design, C4 Content, C5 Functionality, C6 Accessibility) and rendering a shareable scorecard. Use when asked to "audit", "UX audit", "UI audit", "usability review", "heuristic evaluation", "RAG rate this flow", "review this journey", or when given screenshots / a live URL / Figma frames of a flow to evaluate. Not for code review or visual design critique alone.
---

# UX Audit

Produce an audit a *different* auditor would reproduce. Consistency across the studio comes from the rubric, not from taste — follow it literally.

## Non-negotiables

1. **Findings anchor to elements, never whole screens.** "Checkout is confusing" is not a finding. "Cart total differs from Review subtotal with no explanation" is.
2. **Never invent screens you haven't seen.** No screenshot, no capture, no finding. If the flow is JS-rendered and you can't reach a state, say so and ask — do not infer what a screen "probably" looks like.
3. **State the defect, not the fix.** One sentence. Recommendations are a separate engagement unless explicitly asked.
4. **Rate against `references/rubric.md` thresholds**, not instinct. When torn between two ratings, apply the tie-breakers in the rubric.
5. **Green is a real rating.** An audit that is all Red is a rant. Credit what works — it protects good patterns from being "fixed" in a redesign.

## Workflow

### 1. Scope

Pin down before capturing anything:

- **Product + journey** — exact start and end state (e.g. "landing → build 2-pack → cart").
- **Platform(s)** — desktop, mobile, or both. Drives which heuristics pack loads.
- **Region/locale** — pricing, legal copy, and available options vary.
- **Audience** — first-time buyer vs returning power user changes what counts as friction.

Ask if any are ambiguous. Don't guess the journey's end state.

### 2. Acquire screens

**Screenshots provided** — the baseline path. Work from what you're given.

**Live URL** — drive the page and capture states yourself:
- Capture desktop at 1440×900 and mobile at 390×844 (iPhone 14 baseline) unless told otherwise.
- Capture every state including modals, interstitials, empty states, and validation errors.
- Builders and SPAs need real interaction — click through, don't just load and screenshot.
- If browser automation isn't available in the environment, say so and request screenshots. Do not fall back to fetching static HTML and guessing — a JS builder returns an empty shell.

**Figma frames** — audit pre-build designs via the Figma connector. Flag that dynamic behaviour (loading, errors, live totals) can't be assessed from static frames.

### 3. Map the journey

Read `references/journey-mapping.md`. Convert raw captures into a list of **unique states**, collapse near-identical repeats, and assign each a phase.

### 4. Audit each state

For every state, walk the elements and test each against the six lenses. Load the heuristics pack for the platform:

- `references/heuristics-desktop.md`
- `references/heuristics-mobile.md`

Both platforms in scope → run both packs and mark platform-specific findings.

Aim for real coverage, not a fixed quota — a dense screen may yield six findings, a naming screen two. If a state yields zero, that itself is worth one Green.

### 5. Rate

Apply `references/rubric.md`. Every finding gets: lens code (C1–C6), rating (Green/Amber/Red), element name, one-sentence rationale.

### 6. Roll up

- Tally Green / Amber / Red and percentages.
- Extract the top critical pain points, ordered by severity — these lead the deliverable.
- Note any state that could not be captured, and why.

### 7. Render

Build the scorecard from `assets/scorecard-template.html`:

1. Copy the template to the working directory (or scratchpad).
2. Replace the `data` array and the header metadata. **Only** those — the template's CSS, theming, and render logic are shared studio furniture; don't restyle per client.
3. Publish with the Artifact tool.

Confirm with the client whether repeated states were collapsed and whether they want a fix-priority layer — both change the deliverable's shape.

## Lenses

| Code | Lens | Owns |
|------|------|------|
| **C1** | User Interface Design | Visual hierarchy, layout, affordance, selected/active states, consistency, spacing, type |
| **C2** | Information Architecture | Structure, labelling, navigation, findability, orientation/progress, grouping |
| **C3** | Interaction Design | Feedback, flow, control states, gestures, error prevention and recovery, latency |
| **C4** | Content | Copy clarity, terminology, pricing transparency, guidance, expectation-setting |
| **C5** | Functionality | Whether it actually works — state sync, persistence, calculation correctness, cross-screen consistency |
| **C6** | Accessibility | Contrast, touch targets, keyboard and focus, semantics, representation, motion |

Boundary calls that come up constantly:

- Button *looks* disabled but isn't → **C1** (affordance), not C3.
- Button *is* disabled with no reason given → **C4** (content).
- Price shown ≠ price charged → **C5**, always. Not C4.
- Four skin tones in a personalisation product → **C6** (representation), not C4.
- Option grid hidden behind an undiscoverable chevron → **C2** (findability), not C1.

## Anti-patterns

- Padding the count with restatements of one defect across three lenses. One defect, one finding, best-fit lens.
- Rating a whole screen Amber. Rate elements.
- Copying the Funko audit's findings onto a new client. Different product, different evidence.
- Treating a deliberate brand choice as a defect without evidence it costs the user something.
