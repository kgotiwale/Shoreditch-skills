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

**Live URL** — drive the page and capture states yourself via the **Playwright MCP** server:
- `browser_resize` to set the viewport, then `browser_take_screenshot` per state.
- Desktop **1440×900**, mobile **390×844** unless told otherwise.
- Capture every state including modals, interstitials, empty states, and validation errors.
- Builders and SPAs need real interaction — click through, don't just load and screenshot.

```
Is the target a live URL?
├─ No → work from the screenshots / Figma frames provided.
└─ Yes → is the Playwright MCP server available?
   ├─ Yes → drive it. Resize → interact → screenshot, per state, per viewport.
   └─ No  → STOP. Say the capture path is unavailable and request screenshots.
            Do NOT fetch static HTML and infer — a JS builder returns an empty
            shell, and you will invent screens that don't exist.
```

That last branch stays live even with Playwright installed — MCP servers fail at runtime, and the failure mode (confidently auditing a page you never saw) is the worst outcome this skill can produce.

Setup, if the server is missing: `claude mcp add playwright npx @playwright/mcp@latest`

**Accessibility ground truth** — where a live URL exists, run [`@axe-core/cli`](https://www.npmjs.com/package/@axe-core/cli) (Deque, official) against each state and let its output anchor the C6 lens:

```bash
npx @axe-core/cli <url> --tags wcag2a,wcag2aa,wcag22aa
```

Treat it as a black-box script — read its output, don't read its source. Axe verifies what is machine-checkable (contrast, names, roles, structure). It cannot see representation, comprehension, or whether a signifier lies. Those stay judgement — but everything axe *can* check should be cited from axe rather than eyeballed.

**Figma frames** — audit pre-build designs via the Figma connector. Flag that dynamic behaviour (loading, errors, live totals) can't be assessed from static frames.

### 3. Map the journey

Read `references/journey-mapping.md`. Convert raw captures into a list of **unique states**, collapse near-identical repeats, and assign each a phase.

### 4. Audit each state

For every state, walk the elements and test each against the six lenses. Load the heuristics pack for the platform:

- `references/heuristics-desktop.md`
- `references/heuristics-mobile.md`

Both platforms in scope → run both packs and mark platform-specific findings.

Then check the journey against `references/deceptive-patterns.md` — commercial flows especially. Deceptive patterns are invisible to element-by-element rating because each element works *correctly*; the harm is in the arrangement.

Aim for real coverage, not a fixed quota — a dense screen may yield six findings, a naming screen two. If a state yields zero, that itself is worth one Green.

### 5. Walk the flow

Run `references/cognitive-walkthrough.md` over the assembled state list.

Element rating asks "is this element good?". A screen of individually-fine elements can still add up to a flow nobody can finish — and the walkthrough's Q5–Q7 (the Gulf of Evaluation: *what happened? what does it mean? did it work?*) is where the highest-value findings live. Don't skip it because the element pass felt thorough; it's structurally blind to this.

### 6. Rate

Apply `references/rubric.md`. Every finding gets: lens code (C1–C6), rating (Green/Amber/Red), element name, one-sentence rationale.

### 7. Roll up

- Tally Green / Amber / Red and percentages.
- Extract the top critical pain points, ordered by severity — these lead the deliverable.
- Note any state that could not be captured, and why.

### 8. Render

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

- Button *looks* disabled but isn't → **C1**. In Norman's terms the affordance is intact and the *signifier* lies — say it that way, it's precise.
- Button *is* disabled with no reason given → **C4** (content).
- Price shown ≠ price charged → **C5**, always. Not C4.
- Four skin tones in a personalisation product → **C6** (representation), not C4.
- Option grid hidden behind an undiscoverable chevron → **C2** (findability), not C1.
- Upsell where declining costs more clicks than accepting → **C3** (deceptive pattern), not C1.
- User acted but can't tell whether it worked → **C3** (feedback / Gulf of Evaluation), not C5, unless the underlying state is genuinely wrong.

## Anti-patterns

- Padding the count with restatements of one defect across three lenses. One defect, one finding, best-fit lens.
- Rating a whole screen Amber. Rate elements.
- Copying the Funko audit's findings onto a new client. Different product, different evidence.
- Treating a deliberate brand choice as a defect without evidence it costs the user something.
- Flagging "too many steps" as a finding on its own. Per Krug's Second Law, click count isn't the problem — ambiguity per click is. Name the ambiguous steps or drop it.
- Citing "44px, WCAG" for touch targets. That's an **AAA** criterion in the wrong units; the AA floor is **24px**. See the mobile pack.
- Applying 4.5:1 contrast to icons and borders. Non-text is 3:1 (SC 1.4.11). This is a false-positive factory.

## Known limitation — state it in the deliverable

This skill is a **single evaluator**. The literature is unambiguous about what that means: a lone evaluator finds [~35% of problems](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/theory-heuristic-evaluations/), roughly [half of heuristic-evaluation findings are false alarms](https://www.humanfactors.com/newsletters/heuristic_evaluations_vs_usability_testing_the_relative_effectiveness.html), and severity ratings between any two evaluators correlate at just **0.24** ([Hertzum & Jacobsen, *The Evaluator Effect*, 2003](https://mortenhertzum.dk/publ/IJHCI2003.pdf)). Nielsen's own prescription is 3–5 independent evaluators, reconciled.

The rubric's explicit thresholds and tie-breakers exist to attack the documented root cause of false positives — Hertzum's *"vague problem criteria: anything being accepted as a usability problem."* That helps. It does not make one evaluator equal to three.

So: the deliverable's footer must say the audit is heuristic and single-evaluator, and that priority fixes warrant validation. Don't let a client read a scorecard as measurement.
