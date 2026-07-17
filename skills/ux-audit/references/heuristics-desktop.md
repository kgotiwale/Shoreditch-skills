# Desktop heuristics

Load when desktop is in scope. Baseline viewport 1440×900. These are prompts for what to look at — the rating still comes from `rubric.md`.

## C1 · User Interface Design

- **Wide-viewport layout** — large dead zones while content crowds into a column. A two-panel builder with an empty lower-right quadrant is a finding.
- **Line length** — running text past ~80 characters.
- **Selected/active state** — is it unmistakable, and is it the *same* treatment on every screen? Yellow border on one step and white on the next is an inconsistency finding.
- **Disabled vs enabled** — a muted or olive-tinted primary button that reads disabled while active. Extremely common, always a finding.
- **Visual hierarchy** — does the primary action win against decorative and promotional elements?
- **Density** — desktop can carry more, but check whether a grid of 26 options gets any grouping or just scrolls.

## C2 · Information Architecture

- **Progress and orientation** — "step X of Y" in a multi-step flow. Absent = finding, weight it by flow length.
- **Completion state** — can the user see which steps are done, skipped, or remaining?
- **Nav discoverability** — a full step list hidden behind a small chevron is a findability failure, not a UI nit.
- **Grouping and counts** — accordion headers with item counts ("LONG HAIR (21)") are a Green pattern; ungrouped mega-grids are a finding.
- **Category naming** — does the label predict the contents? "Tops" that contains full-body outfits is a mismatch.
- **Cart/order model** — does the cart's structure match the mental model the builder created? Fragmenting one configured product into many rows is a C2 Red.

## C3 · Interaction Design

- **Hover states** — every interactive element needs one. Absent hover on a clickable tile is a finding.
- **Cursor** — pointer on interactive, default on static. Grab/grabbing on draggable.
- **Keyboard navigation** — full path traversable by Tab, in logical order, with a *visible* focus ring. Focus trapped in modals and returned on close.
- **Feedback** — does every selection visibly change the preview and, where relevant, the price?
- **Consistency of interaction model** — tap-to-select on nine steps and an explicit "Add" button on the tenth is a model switch. Finding.
- **Sub-flow signposting** — a choice that silently reveals a further required sub-step (pick hat → now pick hat colour) with no forewarning.
- **Interstitials and upsell modals** — count them between intent and action. A modal pushing an option the user could already toggle inline is redundant friction.
- **Error prevention and recovery** — can the user undo? Is destructive action confirmed? Does Back lose work?

## C4 · Content

- **Expectation-setting** — does the entry point tell the truth about what's inside? Subcopy naming three options where only two are selectable is a copy/reality mismatch.
- **Pricing transparency** — surcharges named before commitment, at the point of choice, not at review.
- **Input guidance** — character limits, format, examples, what's allowed. A bare "TYPE HERE" is a finding.
- **Undecoded UI meaning** — badges, icons, or numbers with no legend. Route to C1 if it's the affordance, C4 if the copy is missing.
- **Terminology** — user's vocabulary, not the system's. Consistent term for the same thing across screens.
- **Legal and finality** — "Final Sale", returns, and shipping terms legible and placed where the decision is made.

## C5 · Functionality

- **Cross-screen number consistency** — the single highest-value check. Does every total agree across builder, review, and cart? Any delta is Red until explained on-screen.
- **State sync** — preview shows an item the price doesn't reflect (or vice versa).
- **Persistence** — build survives back-navigation, refresh, and a new tab.
- **Edit paths** — do the edit affordances on a review screen actually return you to the right step with state intact?
- **Calculation** — surcharges, quantity multipliers, and discounts summing correctly.

## C6 · Accessibility

**WCAG levels are not a severity scale.** A / AA / AAA measures how ambitious the *requirement* is, not how bad the *failure* is. A failed Level A criterion is the most essential tier, not the mildest — mapping A/AA/AAA onto Green/Amber/Red inverts the meaning. Rate:

- **Red** — fails any Level **A or AA** success criterion in scope.
- **Amber** — passes A/AA but fails AAA, or passes on a technicality (programmatic label present but [SC 2.5.3 Label in Name](https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html) mismatched).
- **Green** — passes all in-scope A/AA.

Record the conformance level as metadata in the rationale, never as the rating itself.

**Per-element WCAG ratings are not a conformance claim.** WCAG conformance is formally claimed per *full page* (WCAG 2.2 §5.2.2). Our per-element findings are a diagnostic. If the deliverable touches accessibility, say so explicitly — don't let a client read the scorecard as a conformance audit.

- **Contrast** — 4.5:1 body text, 3:1 large text ([SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)), 3:1 UI components and graphical objects ([SC 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)) — all AA. Applying 4.5:1 to borders and icons is a false positive.
- **Focus visibility** — a visible ring on every focusable element ([SC 2.4.7](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html), **AA**); never `outline: none` without a replacement. New in 2.2: [SC 2.4.11 Focus Not Obscured](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html) (AA) — sticky headers must not cover the focused element.
- **Keyboard-only completion** — can the entire journey be finished without a mouse?
- **Semantics** — real buttons and inputs, labelled ([SC 4.1.2](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html), A). Headings in order.
- **Forms and checkout** — [SC 3.3.1 Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html) (A), [3.3.2 Labels or Instructions](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html) (A), [3.3.3 Error Suggestion](https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html) (**AA**), [3.3.4 Error Prevention (Legal, Financial, Data)](https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data.html) (AA), [3.3.7 Redundant Entry](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html) (A, new in 2.2).
- **Representation** — in a personalisation product, the range of skin tones, body types, hair textures, and gender presentation is a C6 concern, not a content nit.
- **Motion** — auto-playing video, parallax, and transitions honouring `prefers-reduced-motion`.
- **Zoom** — layout holds at 200% browser zoom.
- **Do not audit against SC 4.1.1 Parsing** — obsolete and removed in WCAG 2.2.

## Norman's vocabulary — use it, it makes findings precise

From *The Design of Everyday Things* (Revised, 2013), Ch. 1:

> **"Affordances determine what actions are possible. Signifiers communicate where the action should take place. We need both."**

An affordance is a *relationship* between an object's properties and an agent's capabilities — not a property. A **signifier** is "any perceivable indicator that communicates appropriate behavior to a person."

This resolves the most common audit muddle. A muted-olive Next button that is actually clickable has the affordance and a *broken signifier* — the element says "you cannot act here" while permitting action. That's a **C1** finding, and "signifier contradicts affordance" states it exactly.

**Norman's Gulfs** ([coined 1986 by Hutchins, Hollan & Norman](https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/) — not Norman alone):

> "We bridge the **Gulf of Execution** through the use of signifiers, constraints, mappings, and a conceptual model. We bridge the **Gulf of Evaluation** through the use of feedback and a conceptual model."

Execution-gulf failures are usually C1/C2. Evaluation-gulf failures — user acted but can't tell what happened — are usually C3/C5.

**Slips vs mistakes** (Norman & Reason) — for C3 error findings:
- **Slip** — goal correct, execution wrong. Design fix: better signifiers, constraints, undo.
- **Mistake** — goal or plan wrong. Design fix: a better conceptual model.

Naming which one an error state invites is more useful than "error handling is poor".

## Capture checklist

- [ ] Every state at 1440×900
- [ ] Modals, interstitials, upsells
- [ ] Hover state on a representative interactive element
- [ ] Keyboard focus state
- [ ] Validation and error states
- [ ] Empty and loading states
- [ ] One narrow breakpoint (~768px) if responsive behaviour is in scope
