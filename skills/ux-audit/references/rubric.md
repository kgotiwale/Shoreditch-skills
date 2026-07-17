# Rating rubric

The point of this file is that two auditors, given the same screen, land on the same rating. Apply it literally.

## The scale

### 🟢 Green — Good

> The feature demonstrates good usability, providing an intuitive experience for users.

A first-time user acts correctly **without hesitation**. No re-reading, no hunting, no second-guessing what a control will do. The element does its job and gets out of the way.

Green is not "no complaints" — it's positive evidence something works. Name what it does well.

### 🟠 Amber — Needs improvement

> This aspect could be enhanced to improve user understanding and streamline interaction.

The user **completes the task**, but pays for it: a moment of doubt, a re-read, an extra step, a guess that happens to be right. Remove the friction and the flow measurably improves.

### 🔴 Red — Critical pain point

> Users encounter significant challenges in this area, hindering task completion and requiring urgent attention.

At least one is true:

- **Blocks or abandons** — the user cannot complete the task, or a plausible user quits here.
- **Erodes trust** — surprise costs, unexplained totals, anything that reads as a bait-and-switch.
- **Wrong information** — displayed data contradicts reality or another screen.
- **Excludes** — an accessibility failure that locks a user group out (contrast below WCAG AA, unreachable targets, keyboard traps, no representation in a personalisation product).
- **Undecodable** — an element carries meaning the user has no way to decode, and it affects their decision.

## Where this scale comes from

Our RAG is not invented. Two published scales map to it almost exactly — cite them when a client asks why three points:

**[MeasuringU's 3-point severity](https://measuringu.com/rating-severity/)** — a direct 1:1, no information lost:

| Theirs | Ours |
|---|---|
| **Minor** — "Causes some hesitation or slight irritation." | 🟠 Amber |
| **Moderate** — "Causes occasional task failure for some users; causes delays and moderate irritation." | 🟠 Amber / 🔴 Red boundary |
| **Critical** — "Leads to task failure. Causes user extreme irritation." | 🔴 Red |

**[Baymard's guideline severity](https://baymard.com/research/methodology)** — e-commerce-native, which matches most of our work:

| Theirs | Ours |
|---|---|
| **Interruption** — "the test participants were only interrupted briefly" | 🟠 Amber |
| **Disruptive** — "came to a full stop in what they were doing and had to actively resolve the issue" | 🟠 Amber / 🔴 Red boundary |
| **Harmful** — "unable to complete their task at hand, often having to abandon the site" | 🔴 Red |

**[NN/g's 0–4 scale](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/)** carries more resolution than ours (it separates cosmetic from minor). Its three factors — frequency, impact, persistence — **do not combine by formula**; Nielsen has evaluators "combine all aspects of severity in a single severity rating as an overall assessment." Our RAG does the same. If you find yourself multiplying or averaging factors, you've invented something and attributed it to Nielsen.

### The thing we *are* inventing: Green

Every published scale above rates **problems**, and a problem that isn't a problem never gets logged — so none of them has a Green. By rating **elements** rather than problems, we need an "it works" end that we defined ourselves.

That's a deliberate departure, and it earns its keep — a client redesigning a flow needs to know what *not* to break. But be honest about it: Green is our own construct, not inherited practice. Never claim NN/g or Baymard backing for the Green end of the scale.

### Polarity warning

If you ever cite more than one severity scale, normalise direction first. **Nielsen: 4 = worst. Rubin: 4 = worst. Dumas & Redish: 1 = worst.** Mixing them ships inverted ratings.

## Tie-breakers

Use in order. Stop at the first that resolves.

**Amber vs Red** — Can a first-time user complete the task without outside help (support chat, a friend, trial and error across sessions)?
→ Yes = **Amber**. No = **Red**.

**Amber vs Red, money edition** — Does the user risk paying something they didn't intend, or seeing a number they can't explain?
→ Yes = **Red**, regardless of the first tie-breaker.

**Green vs Amber** — Did you have to explain how it works to justify the Green?
→ If your rationale needs a "once you realise…", it's **Amber**.

**Still torn** — rate the *lower* of the two and note the uncertainty in the rationale. Underrating is recoverable in review; overrating burns credibility.

## Severity ordering for the roll-up

When ranking Reds for the summary, order by:

1. **Trust and money** — wrong totals, surprise charges, fragmented orders.
2. **Blocking** — cannot complete the task.
3. **Exclusion** — accessibility and representation failures.
4. **Undecodable** — meaning the user can't access.

Ties broken by how many users hit the state — a Red on the cart outranks a Red on an optional sub-step.

## Writing a finding

```
Lens · Rating · Element name · One-sentence rationale
```

**Element name** — what the user would call it, not the component name. "Number badges on option tiles", not "TileBadgeComponent".

**Rationale** — states the defect and its consequence. Present tense. No fix. No hedging.

Good:
> Cart total differs from the Review subtotal with only a £3 shipping / −£3 discount shuffle shown — unexplained change at checkout undermines trust.

Bad:
> The cart total might potentially confuse some users and could be improved by adding a clearer breakdown.

(Hedged, no consequence, contains the fix.)

## Calibration examples

Drawn from the Funko Pop! Yourself 2-Pack audit — use as anchors.

| Finding | Lens | Rating | Why that rating |
|---|---|---|---|
| Persistent Back/Next with running subtotal pinned at all times | C1 | 🟢 | Zero hesitation; reliable anchor across every step. |
| "LICENSED TOPS +£10 (4)" — surcharge stated in the category header | C4 | 🟢 | Cost known before commitment; nothing to decode. |
| Three body options shown as unlabelled thumbnails | C4 | 🟠 | User infers from silhouette and is usually right — completes, but guesses. |
| Buddies use "Add" buttons while every prior step was tap-the-tile | C3 | 🟠 | Model switches without warning; user recovers after a beat. |
| No step indicator anywhere in a 12-step builder | C2 | 🔴 | Plausible abandonment — user can't judge whether to start or how much is left. |
| Blue "2"/"3"/"5" badges on tiles with no legend | C1 | 🔴 | Undecodable, and it bears on a purchase decision. |
| Four skin tones in a product called "Pop! *Yourself*" | C6 | 🔴 | Excludes; representation failure at the core of the value proposition. |
| Styled cat and jersey appear as separate cart rows from the 2-Pack | C2 | 🔴 | Reads as duplicate charges — breaks the one-product mental model. |
| Review says £64.99, cart says £68.99 | C5 | 🔴 | Money tie-breaker fires immediately; unexplained delta at peak intent. |

## Hygiene

- **One defect, one finding.** If a single root cause shows on six screens, report it once at its worst instance and note the spread. Don't farm the tally.
- **Don't split one defect across lenses** to inflate coverage. Pick the best-fit lens.
- **Brand choices aren't defects** unless you can name the cost to the user. A loud palette is a choice; a loud palette at 2.1:1 contrast is a C6 Red.
- **A skipped state is not a Green.** If you couldn't reach it, list it as uncaptured.
