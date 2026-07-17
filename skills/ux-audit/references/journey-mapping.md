# Journey mapping

Turning raw captures into the list of states you actually audit. Do this before rating anything — the state list is the audit's skeleton, and getting it wrong means findings land in the wrong place or get double-counted.

## States, not screenshots

A **state** is a distinct thing the user perceives and acts on. One screenshot ≠ one state, in both directions:

- One screenshot can hold two states (a screen with a modal over it → audit the modal separately; the screen behind it was already captured).
- Two screenshots can be one state (the same grid scrolled to a different offset).

## Collapse repeats

Long flows repeat by design. A 2-pack builder runs the whole single-figure build twice.

**Collapse when** the second instance is functionally identical and differs only in context labelling.
**Keep separate when** the repeat introduces something new — a transition modal, a changed default, a different price.

When you collapse, say so:

> **17 · Second Pop! — Build (repeat)** — identical step order to Pop 1; context labels switch to "SECOND POP!".

Then audit only what the repeat *adds* — usually the context-switching and any state that failed to carry over. Don't re-rate the same tile grid twice; it inflates the tally and buries the real findings.

Confirm the collapse with the client. Some want a card per screenshot for 1:1 traceability against their own captures.

## Name states from the interface

Use the label the product uses, not your own coinage. If the screen says "Looks Good?", the state is "Looks Good? — Packaging Preview" — the product's words plus a clarifier where the label is opaque.

Never invent codenames. The reader has to match your card to their screen without a decoder.

## Phases

Group states into 4–6 phases naming what the user is *doing*: Entry · Build · Transition · Review · Cart. Phases carry the roll-up ("every Red is in Review and Cart") and that pattern is often the headline finding.

## Number in journey order

Sequential, in the order a real user hits them. Modals get their own number at the point they fire — an upsell that interrupts Review is its own state between Review and Cart, because that interruption *is* the finding.

## What to capture beyond the happy path

Auditors under-capture these, and they hold a disproportionate share of Reds:

- **Interstitials and upsell modals** — every one between intent and action.
- **Validation and error states** — submit empty, submit bad data.
- **Empty states** — empty cart, no results.
- **Loading** — especially anything over a second on a builder or a total.
- **Entry variants** — direct link vs nav vs campaign landing can differ.
- **Exit** — where the journey hands off (cart → checkout), because totals must reconcile across the seam.

## Uncaptured states

If you can't reach a state, list it as uncaptured with the reason. Never fill the gap by inference.

> **Uncaptured:** checkout (requires payment credentials) — totals reconciliation past the cart seam unverified.

Uncaptured states are not Green. They're a stated limit on the audit's coverage, and they belong in the deliverable so nobody reads silence as a pass.

## Sanity check before rating

- [ ] Every state numbered in journey order
- [ ] Repeats collapsed and labelled, or expanded by client preference
- [ ] Modals and interstitials have their own entries
- [ ] Phases assigned
- [ ] Uncaptured states listed with reasons
- [ ] Names match the product's own labels
