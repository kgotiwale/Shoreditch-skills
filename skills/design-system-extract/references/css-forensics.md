# CSS forensics

Reading a production stylesheet for what it tells you about a design system.

## Finding all the stylesheets

Sites split CSS by template family. One page gives you one slice.

```bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/120 Safari/537.36"
curl -sL -A "$UA" "$URL" | grep -oE 'href="[^"]*\.css[^"]*"' | sort -u
```

Sample four page types before you conclude you have the whole system: a section landing, a
product or detail page, an article, and a tool or form. If two of them load different
stylesheets, the client is running more than one system and that is a headline finding, not
a footnote.

Record total bytes parsed. Every absence claim in the deliverable cites it.

## Deriving the naming convention

Never assume. Extract every class, group by prefix, and read the distribution.

```python
cls = re.findall(r'\.([A-Za-z][A-Za-z0-9_-]{2,})', css)
prefix = collections.Counter(re.split(r'--|__', c)[0] for c in set(cls))
```

Conventions you will meet:

| Convention | Looks like | Notes |
|---|---|---|
| Atomic IDs | `O-ACCRD-RW-RBWM` | Tier, name, platform, owner. Common in enterprise |
| BEM | `crh-hero-banner__main-wrapper--version-c` | Block, element, modifier |
| Utility | `m-md-8`, `offset-lg-2` | Grid and spacing helpers, usually noise |
| Third-party | `vjs-big-play-button`, `ui-slider` | Video.js, jQuery UI. **Not the client's system** |

Flag third-party classes explicitly. A player or date-picker the client does not own is a
constraint on what can be redesigned, and it belongs in the audit as such.

### The too-narrow regex trap

Write the permissive pattern first, count the matches, then tighten only if you must.

```python
# too specific, silently drops components whose platform segment differs
r'\b([AMOT]-[A-Z0-9]{3,}-RW-[A-Z]{2,6})\b'

# permissive, catches ART-DEV, WIH and other variants
r'\b([AMOT]-[A-Z0-9]{2,}(?:-[A-Z0-9]{2,}){1,3})\b'
```

Sanity-check the count against the markup by eye. If the page visibly has a card component and
your inventory has no card, the pattern is wrong.

## Parsing with media queries

A naive `{...}` regex flattens base rules and breakpoint overrides together, so you get the
mobile value where you wanted desktop, or a merge of both. Parse recursively, keeping the
`@media` context. `assets/extract.py` does this.

Base declarations are the ones with no media context. Quote those as the component's spec and
note the breakpoint overrides separately.

## Techniques that hide in CSS

Things that will not show up if you search for the obvious keyword.

### Border triangles

Angled shapes are frequently drawn with a zero-size box and coloured borders, not `clip-path`.

```css
border-width: 0 475px 477px 0;
border-color: rgba(0,0,0,0) rgba(0,0,0,0) #fff;
```

That is a 45° wedge (legs 475 and 477 → `atan(475/477)` = 44.88°). Searching for `clip-path`
finds nothing; searching for `transparent` also finds nothing, because the value is written
`rgba(0,0,0,0)`. Search for **both** spellings:

```bash
grep -oE '(transparent|rgba\(0, ?0, ?0, ?0\))' style.css | sort | uniq -c
```

Play arrows, chevrons, tooltips and speech-bubble tails use the same trick.

### Icon fonts

`content: "\e001"` with a proprietary `font-family` means the icon set is a font you do not
have. Note it as an asset gap and rebuild icons as vectors, saying so.

### Inset shadows as keylines

`box-shadow: inset 5px 0 0 0 #db0011` is a left keyline, not elevation. A site can have zero
real drop shadows and still use `box-shadow` a dozen times. Separate the two before writing
"the system has no elevation".

### Per-component type scales

Large systems accumulate parallel ramps. One real audit found three: the main atoms
(`A-TYPS1`–`S7`), a legacy ramp (`A-TYP{px}`), and a calculator-local ramp (`lc-t22l`, `lc-t28b`)
that ignored both. Group font-size declarations by their selector prefix and look for clusters
that do not reference the main atoms.

### Colours that only exist inside one component

Harvest the palette globally, then harvest it again per organism. Error states and tool-specific
tints often never appear in the main palette. They are still real tokens.

## Reading value from frequency

Count, do not eyeball.

```python
collections.Counter(re.findall(r'#([0-9a-fA-F]{3,8})\b', css))
collections.Counter(re.findall(r'@media[^{]*?(\d{3,4})px', css))
```

- The two or three breakpoints carrying hundreds of media queries are the real ones. The rest
  are edge cases.
- A colour appearing three times in 2MB is not a system token. Say so rather than including it.
- `border-radius: 0` appearing twenty times and nothing else means the system is deliberately
  square. That is a finding.

## Component families worth counting separately

Report counts per family, since it tells the reader where the system is mature and where it is thin.

Typography, links, buttons, panels and surfaces, form inputs, layout and grid, navigation,
media, tables, notifications.

A system with 26 link atoms and no table component is telling you something about what it was
built for.
