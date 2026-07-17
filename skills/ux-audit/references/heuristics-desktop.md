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

- **Expectation-setting** — does the entry point tell the truth about what's inside? "Choose Single, 2-Pack, or Baby" with only two cards is a copy/reality mismatch.
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

- **Contrast** — WCAG AA: 4.5:1 body, 3:1 large text and UI boundaries. Check text on gradients, on images, and inside blurred overlays especially.
- **Focus visibility** — a visible ring on every focusable element; never `outline: none` without a replacement.
- **Keyboard-only completion** — can the entire journey be finished without a mouse?
- **Semantics** — real buttons and inputs, labelled. Icon-only controls with accessible names. Headings in order.
- **Representation** — in a personalisation product, the range of skin tones, body types, hair textures, and gender presentation is a C6 concern, not a content nit.
- **Motion** — auto-playing video, parallax, and transitions honouring `prefers-reduced-motion`.
- **Zoom** — layout holds at 200% browser zoom.

## Capture checklist

- [ ] Every state at 1440×900
- [ ] Modals, interstitials, upsells
- [ ] Hover state on a representative interactive element
- [ ] Keyboard focus state
- [ ] Validation and error states
- [ ] Empty and loading states
- [ ] One narrow breakpoint (~768px) if responsive behaviour is in scope
