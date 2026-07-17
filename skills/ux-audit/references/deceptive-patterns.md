# Deceptive patterns

Called "dark patterns" when Harry Brignull coined it in 2010; "deceptive patterns" is now the preferred term, and it's the one regulators use.

A deceptive pattern is not bad design — it's design working correctly **against** the user. That distinction drives how we rate it: the usual "does the user complete the task?" tie-breaker misfires here, because the pattern's whole point is that the user completes a task *they didn't intend*.

## Rating rule

**A pattern that causes unintended spend or unintended data disclosure is Red.** The rubric's money tie-breaker already covers it: *"Does the user risk paying something they didn't intend?"* Yes → Red, regardless of whether the flow "works".

**Asymmetric emphasis alone, with no cost, is Amber.** A prominent "Yes" and a quiet "No Thanks" where both are one click and nothing is charged is a nudge, not a trap.

Route to **C3** when the mechanism is interaction (pre-checked boxes, misdirection, obstruction) and **C4** when the mechanism is language (confirmshaming, false urgency, weasel copy).

## The catalogue

Check each state against these. Named per Brignull's taxonomy and the EU/FTC enforcement vocabulary.

**Sneaking** — cost or commitment revealed late.
- *Sneak into basket* — items added the user didn't choose.
- *Hidden costs* — fees appearing only at the final step.
- *Hidden subscription* — a one-off purchase that silently recurs.
- *Drip pricing* — the headline price is never the price paid.

**Urgency** — pressure, often fabricated.
- *False countdown* — a timer that resets on reload.
- *Fake low stock / "17 people are viewing this"* — unverifiable scarcity claims.

**Misdirection** — attention steered away from the user's interest.
- *Confirmshaming* — the decline option is worded to shame ("No thanks, I don't like saving money").
- *Visual interference* — the option you want is styled to recede.
- *Trick wording* — double negatives in opt-outs.
- *Pressured selling* — the upsell presented as the default path.

**Obstruction** — the unwanted path is made hard.
- *Roach motel* — trivial to subscribe, laborious to cancel.
- *Price comparison prevention* — you can't see two options side by side.
- *Intermediate currency* — spend in points so real money feels abstract.

**Forced action** — something unrelated is required to proceed.
- *Forced enrolment* — an account required for a guest-viable task.
- *Nagging* — repeated interruption until the user relents.

**Social proof** — manufactured consensus.
- *Fake activity notifications*, unverifiable testimonials.

**Interface interference** — the control itself misleads.
- *Preselection* — the paid option checked by default.
- *Toggle ambiguity* — you can't tell whether on means on.
- *Disguised ads* — promotional content styled as UI.

## Judgement calls

**Not every upsell is deceptive.** An upsell that is honestly priced, honestly described, and equally easy to decline is legitimate commerce. Three tests distinguish them:

1. **Symmetry** — is declining as easy as accepting? Same number of clicks, both visible without scrolling?
2. **Honesty** — does the copy make claims you can verify? A countdown that survives a reload is a lie, not a nudge.
3. **Default** — does inaction cost the user money? Pre-selected paid options fail here immediately.

**Redundant nagging is its own finding** even when each individual instance is honest. An add-on the user could already toggle inline, re-pitched as a blocking modal, is *Nagging* — the pattern is the repetition. (The Funko audit's UV Protector modal is exactly this: honest copy, honest price, but pitched a second time as an interruption after the inline checkbox already offered it.)

**Distinguish emphasis from entrapment.** Funko's UV modal styles "Okay" as a black primary and "No Thanks" as muted — asymmetric emphasis, but both are one click, nothing is pre-checked, and nothing is charged by inaction. That's **Amber** (C3), not Red. Calling it Red would be exactly the false positive the literature warns about.

## Regulatory footing

Worth knowing, because it changes how a client hears the finding:

- **EU** — the Digital Services Act (Art. 25) prohibits deceptive design on online platforms; the Consumer Rights Directive covers drip pricing.
- **UK** — the Digital Markets, Competition and Consumers Act 2024 addresses drip pricing and fake reviews; the CMA has published guidance on online choice architecture.
- **US** — the FTC's ROSCA enforcement targets negative-option and hidden-subscription patterns.

Do **not** render legal conclusions in an audit. "This may breach the DSA" is not our call to make. State the pattern and its user cost; flag that it *"sits in territory regulators are actively enforcing"* and recommend the client take legal advice. That's the honest line between a UX finding and a compliance opinion.
