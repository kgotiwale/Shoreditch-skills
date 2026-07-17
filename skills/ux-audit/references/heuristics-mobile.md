# Mobile heuristics

Load when mobile is in scope. Baseline viewport 390×844 (iPhone 14). These are prompts for what to look at — the rating still comes from `rubric.md`.

## C1 · User Interface Design

- **Density under thumb** — controls packed tight enough that a mis-tap is likely (<8px between adjacent targets).
- **Selected state at arm's length** — a 1px border that reads on a 27" monitor often vanishes on a phone in daylight. Selection needs weight, fill, or a check — not just an outline.
- **Sticky chrome budget** — headers + toolbars + cookie bars + chat bubbles eating vertical space. Over ~25% of viewport in persistent chrome is a finding.
- **Truncation** — labels and prices clipped at narrow widths.
- **Text size** — body copy below 16px, or a type scale that collapses to two indistinguishable sizes.

## C2 · Information Architecture

- **Orientation** — with less screen, "where am I / how much is left" gets harder, not easier. Missing progress indication is heavier on mobile than desktop.
- **Nav behind a hamburger or chevron** — acceptable if there's a persistent alternative for the primary path; a finding if the only route to a core step is hidden.
- **Scroll depth** — how many screens of scrolling to reach a decision. Long accordion stacks with no jump affordance.
- **Back semantics** — in-app Back vs OS/browser back doing different things, or OS back destroying build state.

## C3 · Interaction Design

- **Gesture discoverability** — swipe-only actions with no visual affordance. If a gesture is the only route, it's a finding.
- **Gesture collision** — a horizontal carousel inside a vertical scroll, or a swipe near the OS edge-back zone.
- **Feedback latency** — tap with no immediate state change. Anything over ~100ms without a pressed state reads as broken and gets double-tapped.
- **Modals and sheets** — dismissibility (is there an X, does backdrop-tap work, does swipe-down work), and whether a sheet covers the very content it describes.
- **Input friction** — wrong keyboard type (no numeric pad for a number), missing autocomplete/autofill, no input mode for email.
- **Zoom-on-focus** — inputs below 16px font-size trigger iOS auto-zoom, which yanks the layout. Classic silent friction.
- **Interstitials** — every extra modal between intent and action costs more on mobile than desktop. Count them.

## C4 · Content

- **Copy written for desktop width** — sentences that fit one line at 1440px and wrap to four on a phone.
- **Helper text lost below the fold** — guidance that sits far from the control it explains.
- **Truncated legal/pricing** — "Final Sale", shipping terms, or surcharges shrunk to unreadable.
- **Labels dropped for icons** — icon-only controls that carried a label on desktop.

## C5 · Functionality

- **State survival** — does the build/cart survive a backgrounded app, a rotation, a browser back?
- **Cross-viewport parity** — an option available on desktop that silently disappears on mobile.
- **Live totals** — do prices recalculate correctly with a soft keyboard open and the layout shifted?
- **Network reality** — behaviour on a slow connection: unlabelled spinners, layout shift on image load, silent failures.

## C6 · Accessibility

### Touch targets — know which standard you're citing

Three different numbers, three different standards. Citing the wrong one is a false finding.

| Threshold | Source | Status |
|---|---|---|
| **24×24 CSS px** | [WCAG 2.2 SC 2.5.8 Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) | **Level AA** — the conformance floor |
| **44×44 CSS px** | [WCAG 2.2 SC 2.5.5 Target Size (Enhanced)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html) | **Level AAA** — aspiration, not baseline |
| **44×44 pt** | [Apple](https://developer.apple.com/design/tips/) — "at least 44 points x 44 points" | Platform guideline |
| **48×48 dp**, separated by **8dp** | [Material](https://m1.material.io/usability/accessibility.html) | Platform guideline |

**The 44 collision:** Apple's 44**pt** and WCAG 2.5.5's 44**px** are unrelated standards in different units, and 2.5.5 is **AAA**. Never write "44 minimum, WCAG-backed" — that misattributes an AAA criterion as a baseline. The WCAG **AA** floor is **24px**.

How to rate:
- Below **24×24px** → **Red** (fails WCAG AA), unless an SC 2.5.8 exception applies.
- Meets 24px but below the platform guideline (44pt / 48dp) → **Amber**, cite the platform, not WCAG.
- **SC 2.5.8 has five exceptions** — spacing, equivalent, inline, user-agent control, essential. Inline text links are explicitly exempt. Check before flagging.
- **Spacing** — Material asks for **8dp** between targets. Adjacent targets tighter than that are a finding even when each is individually large enough.

### Contrast

- **4.5:1** — body text ([SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), AA).
- **3:1** — large text (18pt / 14pt bold ≈ 24px / 18.5px), same SC.
- **3:1** — UI components, borders, icons, graphical objects ([SC 1.4.11 Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html), AA).

Applying 4.5:1 to a button border or icon is a **false positive** — non-text is governed by 1.4.11 at 3:1. Check white-on-gradient and text-over-image especially.

### Thumb reach — weak evidence, rate accordingly

The primary source is [Hoober, UXmatters 2013](https://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php): 1,333 observations (780 involving screen interaction) — 49% one-handed, 36% cradled, 15% two-handed.

Hoober's own caveats disqualify it as a rule: no demographic data, no record of what users were doing, tablets excluded, only *initial* observations captured — and he notes grip *"is not a static state. Users change the way they're holding their phone very often—sometimes every few seconds."* It is 2013 observational field data predating large-format phones.

So: **thumb reach is a prompt to look, not a threshold to enforce.** Only raise a finding where a *primary* action is stranded in a hard-to-reach corner *and* you can name the cost. Never cite "49% one-handed" as licensing a hard rule.

### The rest

- **Pinch-zoom disabled** — `user-scalable=no` or `maximum-scale=1` is a C6 Red.
- **Safe areas** — content or controls under the notch, home indicator, or rounded corners.
- **Orientation lock** — forcing portrait with no functional reason excludes mounted and assistive setups.
- **Motion** — parallax, auto-advancing carousels, or transitions ignoring `prefers-reduced-motion`.
- **Screen reader basics** — icon-only buttons with no accessible name; decorative images announced; focus order after a modal opens.
- **Do not audit against SC 4.1.1 Parsing** — obsolete and removed in WCAG 2.2.

## Capture checklist

- [ ] Every state at 390×844
- [ ] Modals, sheets, interstitials
- [ ] Soft keyboard open on every input screen
- [ ] Validation and error states
- [ ] Empty and loading states
- [ ] Landscape, if the product allows it
