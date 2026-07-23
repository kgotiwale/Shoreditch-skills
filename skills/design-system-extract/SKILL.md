---
name: design-system-extract
description: Reverse-engineer a live website's design system into an evidence-backed component inventory, a stakeholder audit document, and a working Figma library. Use when asked to "pull their design system", "audit a client's components", "what can we reuse from their site", "extract design tokens", "rebuild their system in Figma", or when starting a redesign where the client already has a shipped site. Not for auditing usability (use ux-audit) or for greenfield systems with no live site.
---

# Design System Extract

Turn a shipped website into three things: an inventory of what exists, evidence of what is
actually used, and a Figma library the studio can build new pages from.

The failure mode this skill exists to prevent is a confident inventory that nobody checked.
A component list assembled from a stylesheet reads as authoritative and is frequently wrong:
class names lie about their values, half the declarations are dead code, and the same organism
ships in configurations that look like different components. Every claim in the deliverable
has to be traceable to something you actually observed.

## Grounding rules: non-negotiable

Everything you output carries one of three labels. Never blur them.

| Label | Means | Evidence required |
|---|---|---|
| **Observed** | You saw it in the source | A CSS selector and its declarations, or a measured DOM node |
| **Derived** | You calculated it from observations | The inputs and the arithmetic (e.g. legs 475×477 → 44.88°) |
| **Proposed** | The studio invented it | Say so in the same sentence. Never let it pass as the client's |

Four rules that follow from that:

1. **"Exists in CSS" and "is in use" are different claims.** A component defined in a stylesheet
   may render on no page you sampled. Report both numbers, always: how many components the CSS
   defines, and how many appeared in the pages you checked.
2. **Reuse claims need a page count.** "Reusable" means you saw it on two or more page types.
   One sighting is a sighting, not a pattern. Quote the count.
3. **Absence claims need a stated scope.** Never write "there is no charges table component".
   Write "no match in the 1.98MB of CSS parsed across two clientlibs". You searched a corpus,
   not the universe.
4. **Names lie. Verify every value.** This is not hypothetical: on one real audit
   `A-PAR13-ART-DEV` was 17px, not 13px, and it was the most-used body style on the site.
   Read the computed value; never infer a value from a class name.

## Workflow

Five phases. Do not start building in Figma before phase 3 is done. Components built from
unverified specs cost more to correct than to build.

### Phase 1. Acquire

Find the real stylesheets, not a rendered approximation.

```bash
# discover the stylesheet URLs the page actually loads
curl -sL -A "$UA" "$URL" | grep -oE 'href="[^"]*\.css[^"]*"'
```

Download every stylesheet the site loads and record its byte size, which you quote as
your search scope. Modern sites split by template family, so **fetching one page's CSS may miss
half the system.** Sample pages of different types (landing, product, article, tool) and collect
the union of their stylesheets.

Fetch the page HTML with `curl`, not a browser, wherever the site renders server-side. It is an
order of magnitude faster and gives the same class attributes. Use the browser only for phase 3.

### Phase 2. Discover the taxonomy

**Do not guess the naming pattern. Derive it.**

Extract all class names, group by prefix, and look at what dominates. Clients use conventions
you will not predict: atomic IDs (`O-ACCRD-RW-RBWM`), BEM (`crh-hero-banner__main-wrapper`),
utility classes, or several at once.

The trap here is writing a regex that is too specific and silently missing components. On a
real audit, requiring `-RW-` in the pattern hid `M-CNT-ITEM-ART-DEV`, the single most reused
component on the site. **Start permissive, then tighten.** Count what your pattern catches and
sanity-check the total against a manual look at the markup.

`assets/extract.py` does the parsing. It is media-query aware, which matters because base
declarations and breakpoint overrides live in separate rules and a naive regex merges them wrongly.

### Phase 3. Verify against the rendered page

CSS tells you what is declared. The browser tells you what is true.

For every component you intend to build, open the page and read `getComputedStyle` plus
`getBoundingClientRect`. Confirm at minimum: font family, size, line height, colour, padding,
border, radius, and the measured box.

This phase catches the things that make a deliverable wrong:

- Declarations overridden by later rules or breakpoints
- Values that are responsive, where the CSS shows one of several
- Components rendered by JavaScript that never appear in the served HTML
- Dead CSS for components no page uses

See [references/verification.md](references/verification.md) for the extraction snippets.

### Phase 4. Build the Figma library

Order matters: variables, then text styles, then components. Building components first means
rebinding everything later.

Follow [references/figma-build.md](references/figma-build.md). It carries the API constraints
that will otherwise cost you an afternoon, including how to apply a client's licensed font
that the Figma environment cannot load.

### Phase 5. Write the audit

The Figma library answers "what can we use". The document answers "what does this mean for us".
Those are different jobs and the second is what stakeholders read.

Load the `writing` skill before drafting. Structure that works:

1. **The short version**: the two or three findings that change decisions
2. **How the system is named**: so the reader can talk to the client's engineers
3. **Foundations**: colour, type, shape, grid, with real values
4. **The reuse matrix**: every component you need, matched against what exists, with a verdict
5. **What is missing**: the gaps, with your search scope stated
6. **What this changes**: implications, not observations

The reuse matrix is the centre of the document. Three verdicts only: **Yes**, **Partly**, **No**.
Every row cites the component ID and the condition attached.

## What good looks like

- Every foundation value traceable to a selector or a measurement
- A usage matrix showing which components appear on which page types
- Named gaps with the search scope stated
- A Figma library where nothing is hardcoded, with all fills, strokes and spacing bound to variables
- Component descriptions carrying the client's own component ID, so a designer in Figma can
  trace any layer back to production CSS

## Scope boundaries

Stop at the system. This skill inventories and rebuilds; it does not judge. If the client's
contrast fails or their hierarchy is broken, that is a `ux-audit`, and mixing the two produces
a document that does neither job.

Do not build all of a large system. Inventory all of it, build the subset the project needs,
and say plainly which components you built and which you only catalogued.

## References

| File | Load when |
|---|---|
| [references/css-forensics.md](references/css-forensics.md) | Parsing stylesheets, finding the taxonomy, reading techniques that hide in CSS |
| [references/verification.md](references/verification.md) | Measuring rendered components, building the usage matrix |
| [references/figma-build.md](references/figma-build.md) | Building the library: variables, components, font and API constraints |
| `assets/extract.py` | Run it in phase 2. Media-aware parser, taxonomy discovery, usage matrix |

## Prior art

Superposition, Project Wallace and CSS Stats extract tokens from a URL and produce a report.
Use them to cross-check your colour and type values. A second opinion on a palette is cheap.
They do not discover component taxonomy, prove what is in use, or build the Figma library,
which is the part that takes judgement.
