# Figma build

Turning a verified inventory into a library the studio can build pages from.

Load the `figma-use` skill before any `use_figma` call and `figma-generate-library` alongside it.
This file carries only what is specific to rebuilding *someone else's* system.

## Build order

Variables, then text styles, then components. Reversing this means rebinding everything later.

1. **Primitives**: raw harvested values. Colours, sizes, spacing, breakpoints. Set `scopes = []`
   so they stay out of every picker.
2. **Semantic**: aliased to primitives, properly scoped. `text/primary`, `action/primary`,
   `border/default`. This is the layer designers use.
3. **Text styles**: the client's ramps, named after their atoms.
4. **Components**: nothing hardcoded. Every fill, stroke and spacing bound.

Put the client's own component ID in every component description. A designer should be able to
select a layer in Figma and trace it back to production CSS without asking anyone.

```js
set.description = 'O-ACCRD-RW-RBWM / A-EXPCNT-RW-RBWM. Header 16px weight 300, ' +
  '20px vertical padding, chevron right-aligned, 1px hairline below. Live on the ISA and ' +
  'calculator pages; not available to article templates.';
```

Where you invent something the client does not have, say so in the description. A "featured"
card state nobody has built is a proposal, and the description is where that stays honest.

## Applying a licensed font the API cannot load

The problem: the client's font is installed on the designer's machine and visible in Figma
desktop, but `use_figma` runs in a different context. `listAvailableFontsAsync()` does not list
it and `loadFontAsync()` throws. Setting `fontName` directly is therefore blocked:

```
in set_fontName: Cannot use unloaded font "Univers Next for HSBC Regular"
```

**The way through is a FONT_FAMILY variable.** `setBoundVariable('fontFamily', …)` does not
perform the loaded-font check.

```js
const coll = figma.variables.createVariableCollection('Typography');
const fv = figma.variables.createVariable('font/family', coll, 'STRING');
fv.scopes = ['FONT_FAMILY'];
fv.setValueForMode(coll.modes[0].modeId, 'Univers Next for HSBC');

// works on text styles and text nodes alike, no font load required
style.setBoundVariable('fontFamily', fv);
textNode.setBoundVariable('fontFamily', fv);
```

Bind the styles and every text node. One token then drives the whole library, so a font rename
is a one-value change.

Two further benefits worth knowing:

- **It normalises broken font metadata.** Badly built TTFs declare themselves as separate
  families (`Univers Next for HSBC Light` with style `Bold`). Binding forces every node onto one
  family, so anyone opening the file gets one missing-font prompt instead of several.
- **You keep edit access.** Text bound to an unloadable font cannot have its `characters`
  changed. Unbind, set a loadable font, edit, rebind:

```js
t.setBoundVariable('fontFamily', null);
t.fontName = { family: 'Inter', style: 'Regular' };
t.characters = 'new copy';
t.setBoundVariable('fontFamily', fv);
```

Style names must still exist in the target family. Map the substitute's styles to the client's
weights before binding and check for leftovers afterwards.

## Working across pages

`setCurrentPageAsync` is allowed once per `use_figma` call, which makes whole-file operations
look like one call per page. `page.loadAsync()` avoids that. It loads a page's content without
making it current, so a single script can sweep every page.

```js
for (const page of figma.root.children) {
  await page.loadAsync();
  for (const t of page.findAllWithCriteria({ types: ['TEXT'] })) { /* … */ }
}
```

Use `findAllWithCriteria` over `findAll` with a predicate. It uses an indexed lookup and is
dramatically faster on a large file.

## API constraints that cost time

| Constraint | Consequence |
|---|---|
| `figma.root.name` is not settable | Rename the file by hand; do not script it |
| Failed scripts are atomic | Nothing partially applied. Read the error, fix, retry |
| MCP tool-call limits apply per seat | Batch aggressively. Variables are cheap, node creation is not |
| `figma.notify()` throws | Use `return` for all output |
| Screenshots render in the MCP's environment | A client font absent there shows a fallback. Never verify type from a returned screenshot |

Errors sometimes report a state that has in fact applied. Re-read before retrying a whole batch.
On one run, four text styles reported failure and were already correct.

## Structuring the file

Pages in reading order, separators between groups:

```
Cover · Read me
——— FOUNDATIONS ———   Colour · Type · Grid, shape & depth
——— COMPONENTS ———    one page per family
——— GAPS ———          New build required
```

The **Read me** page is not optional. It records what was audited, the method, the date, and
every caveat: font substitutions, components rebuilt from CSS rather than imported, and anything
the studio proposed. Without it, a designer six months from now cannot tell which parts are the
client's and which are ours.

The **gaps** page earns its place too. Building the missing components as explicit proposals,
labelled as such, is more useful than a list, because it gives the client something to react to.

## Validate as you go

After each component: screenshot it and check for clipped text, overlapping nodes and wrong
spacing. After the library: sweep for hardcoded values.

```js
// anything still carrying a raw fill is unfinished
page.findAllWithCriteria({ types: ['FRAME','RECTANGLE','TEXT'] })
    .filter(n => Array.isArray(n.fills) && n.fills.some(f => !f.boundVariables?.color));
```
