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

- **Touch targets** — below 44×44pt (iOS HIG) / 48×48dp (Material) is a finding. Below ~32px is Red.
- **Target spacing** — adjacent targets under 8px apart, even if each is individually large enough.
- **Thumb reach** — destructive or primary actions stranded in the top corners of a tall device. Not automatically a finding; a finding when the *primary* action lives there.
- **Contrast** — WCAG AA: 4.5:1 body text, 3:1 large text and UI boundaries. Check white-on-gradient and text-over-image especially.
- **Pinch-zoom disabled** — `user-scalable=no` or `maximum-scale=1` is a C6 Red.
- **Safe areas** — content or controls under the notch, home indicator, or rounded corners.
- **Orientation lock** — forcing portrait with no functional reason excludes mounted and assistive setups.
- **Motion** — parallax, auto-advancing carousels, or transitions that ignore `prefers-reduced-motion`.
- **Screen reader basics** — icon-only buttons with no accessible name; decorative images announced; focus order after a modal opens.

## Capture checklist

- [ ] Every state at 390×844
- [ ] Modals, sheets, interstitials
- [ ] Soft keyboard open on every input screen
- [ ] Validation and error states
- [ ] Empty and loading states
- [ ] Landscape, if the product allows it
