# Cognitive walkthrough

Element rating asks *"is this element good?"* — a screen of individually-fine elements can still add up to a flow nobody can complete. The walkthrough asks a different question: **can a user who has never seen this get through it?**

Run this **after** element rating, over the assembled state list. It's cheap and it catches what per-element work structurally cannot.

## The frame

Norman's two gulfs (coined 1986 by [Hutchins, Hollan & Norman](https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/)):

- **Gulf of Execution** — the user is trying to work out how to act. Bridged by signifiers, constraints, mappings, and a conceptual model.
- **Gulf of Evaluation** — the user is trying to work out what just happened. Bridged by feedback and a conceptual model.

Most flows are audited only for the execution gulf. The evaluation gulf is where silent failures live: the price that didn't update, the selection that didn't take, the "did that work?" pause.

## The seven questions

Norman's Fig. 2.7 (*The Design of Everyday Things*, Revised, Ch. 2) — his standard is absolute:

> "Anyone using a product should always be able to determine the answers to all seven questions."

| # | Question | Stage | Usual lens when it fails |
|---|---|---|---|
| 1 | What do I want to accomplish? | Goal | C2 / C4 |
| 2 | What are the alternative action sequences? | Plan | C2 |
| 3 | What action can I do now? | Specify | C1 (signifiers) |
| 4 | How do I do it? | Perform | C1 / C3 |
| 5 | What happened? | Perceive | C3 (feedback) |
| 6 | What does it mean? | Interpret | C4 / C5 |
| 7 | Is this okay? Have I accomplished my goal? | Compare | C5 |

**Q5–Q7 are the evaluation gulf.** They're the ones auditors skip. Ask them at every state.

Norman's related distinction, useful when writing the finding:

> "The information that helps answer questions of execution (doing) is **feedforward**. The information that aids in understanding what has happened is **feedback**."

## Procedure

For each state in the journey, in order:

1. State the user's goal at that moment, in their words.
2. Walk Q1–Q7.
3. Any question the interface doesn't answer → a finding, routed to the lens above.
4. Note where the user must **hold state in their head** across states (a price seen three screens back, a choice they can't re-check). Memory load across a flow is invisible to element rating.

Findings from a walkthrough are ordinary findings — same RAG rubric, same tie-breakers. They just tend to be the ones that matter most, because they're about the flow rather than the furniture.

## Krug's trunk test — orientation, in 30 seconds

From *Don't Make Me Think, Revisited* (3rd ed., Ch. 6). Blogs circulate a truncated 3-item version; **the real list is six**:

> "Imagine that you've been blindfolded and locked in the trunk of a car, then driven around for a while and dumped on a page somewhere deep in the bowels of a Web site. If the page is well designed, when your vision clears you should be able to answer these questions without hesitation:
> - What site is this? (Site ID)
> - What page am I on? (Page name)
> - What are the major sections of this site? (Sections)
> - What are my options at this level? (Local navigation)
> - Where am I in the scheme of things? ("You are here" indicators)
> - How can I search?"

Krug's procedure: take a state, **squint or hold it at arm's length**, and try to circle each of the six as fast as you can. His rationale is the point —

> "the true test isn't whether you can figure it out given enough time and close scrutiny. The standard needs to be that these elements pop off the page so clearly that it doesn't matter whether you're looking closely or not."

Missing "you are here" is the single most common failure in a multi-step builder, and it's a **C2** finding. (It's exactly what the Funko audit's "no progress indicator" Red was — trunk test item 5.)

Not every item applies to every product; a full-screen builder legitimately has no search. Apply the ones that bear on orientation.

## Krug's Second Law — for step-count arguments

> "It doesn't matter how many times I have to click, as long as each click is a mindless, unambiguous choice."
> — *Don't Make Me Think, Revisited*, Ch. 4

His rule of thumb: **"three mindless, unambiguous clicks equal one click that requires thought."**

This kills a lazy finding. "Too many steps" is **not** a finding on its own — a twelve-step builder where every step is obvious is fine. The finding is *ambiguity per step*, not step count. Only raise a length finding when you can name the ambiguous or effortful steps.

Where a hard choice genuinely can't be avoided, Krug's test for the guidance around it — it must be **Brief** ("the smallest amount of information that will help me"), **Timely** ("placed so I encounter it exactly when I need it"), and **Unavoidable** ("formatted in a way that ensures that I'll notice it"). Guidance failing any of the three is a **C4** finding.

## Reservoir of goodwill

Krug's Ch. 11 frame, useful for weighting a Red on a commercial flow. Goodwill is idiosyncratic and situational, you can refill it — but *"sometimes a single mistake can empty it."*

His list of what drains it maps almost directly onto e-commerce audit findings:

- **Hiding information I want** — *"The most common things to hide are customer support phone numbers, shipping rates, and prices."*
- **Punishing me for not doing things your way** — format pedantry in inputs.
- **Asking for information you don't really need.**
- **Shucking and jiving me** — faux sincerity.
- **Putting sizzle in my way** — *"pages bloated with feel-good marketing photos."*
- **Looking amateurish.**

When a finding drains the reservoir *and* involves money, the rubric's money tie-breaker fires — it's Red.

---

**Sources:** Norman, *The Design of Everyday Things* (Revised & Expanded, Basic Books 2013), Ch. 1–2 & 5. Krug, *Don't Make Me Think, Revisited* (3rd ed., New Riders 2014), Ch. 4, 6, 11. Cite the books by chapter. Krug's free sample chapter (Ch. 4, containing the Second Law) is at [sensible.com/downloads/DMMT-Revisited-sample-chapter.pdf](https://sensible.com/downloads/DMMT-Revisited-sample-chapter.pdf); his usability test scripts and checklists are free at [sensible.com/download-files](https://sensible.com/download-files/).
