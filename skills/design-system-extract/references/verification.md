# Verification

CSS says what is declared. The rendered page says what is true. Never ship a spec you have
only read.

## The usage matrix

The single most useful artefact in the audit. It converts "this component exists" into
"this component is reused", which is the question the client actually has.

Fetch each sampled page's HTML, extract component IDs from the `<main>` region only, since header
and footer markup otherwise inflates every count, then build the matrix.

```python
m = re.search(r'<main[^>]*>(.*?)</main>', html, re.S | re.I)
body = m.group(1) if m else html
ids = collections.Counter(PATTERN.findall(body))
```

Output one row per component: how many page types it appeared on, and which.

```
6/6  M-IMG-RW-DEV               pages 1,2,3,4,5,6
4/6  M-CNT-ITEM-ART-DEV         pages 1,3,5,6
2/6  O-ACCRD-RW-RBWM            pages 2,4
1/6  O-HEROCARD-RW-RBWM         pages 2
```

Read it for structure, not just counts. In the example above, components cluster into two
groups that never co-occur, which is evidence of two parallel systems, which was the headline finding
of that audit. **Clusters in the matrix are findings.**

## Measuring rendered components

Drive a browser, read computed styles. Capture the properties that determine whether a Figma
rebuild is right.

```js
const T = ['fontFamily','fontSize','fontWeight','lineHeight','letterSpacing',
           'color','backgroundColor','padding','border','borderRadius','boxShadow'];
const pick = el => {
  if (!el) return null;
  const c = getComputedStyle(el), r = el.getBoundingClientRect();
  const o = { w: Math.round(r.width), h: Math.round(r.height) };
  T.forEach(p => o[p] = c[p]);
  return o;
};
```

Record the viewport width alongside every measurement. A 44px heading at 1185px wide is
meaningless without the second number.

## What verification catches

Real examples, each of which would have produced a wrong deliverable.

| Trap | How it shows up | Catch it by |
|---|---|---|
| Name lies about value | `A-PAR13` renders at 17–18px | Reading computed `fontSize` |
| Same organism, many configs | `O-HERO-RW-DEV` with and without an angled wedge | Sampling more than one page per component |
| Declared but never used | Nine panel fills in CSS, one on any sampled page | The usage matrix |
| JS-rendered markup | Component absent from served HTML | Compare `curl` output against the live DOM |
| Responsive value | CSS lists three paddings | Measuring at a stated viewport |
| Breakpoint-gated element | Angled wedge is `display:none` below desktop | Checking `display` at more than one width |

## Pseudo-elements

Much of the interesting geometry lives in `::before` and `::after` and is invisible to normal
DOM traversal.

```js
const before = getComputedStyle(el, '::before');
if (before.content && before.content !== 'none') {
  // border widths and colours here often describe a triangle
}
```

## Sampling rule

Sample at least one page per template family, and confirm you have found all the families by
checking which stylesheets each page loads. Two pages that load different CSS bundles belong
to different families however similar they look.

For each component you intend to build, verify on the page where it is most prominent, not the
first one you find it on.

## Screenshots

Take them for your own reference, but treat any screenshot as weaker evidence than a measurement.
Rendering environments differ. A headless browser without the client's licensed font will show
a fallback face and mislead you about metrics.

Where a screenshot is the evidence, say so and state the environment.

## Recording evidence

Keep a machine-readable record so the audit can be re-derived rather than re-argued.

```
usage.json      component ID → { page: count }
atoms.json      component ID → merged base declarations
measured.json   component ID → computed styles + measured box + viewport
```

When a stakeholder challenges a number six weeks later, this is the difference between
checking and guessing.
