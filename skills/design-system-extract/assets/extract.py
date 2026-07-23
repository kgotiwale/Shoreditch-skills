#!/usr/bin/env python3
"""
Design system extractor.

Parses production stylesheets and sampled page HTML into an evidence-backed inventory:
component taxonomy, foundation tokens, and a usage matrix showing what is actually rendered.

Media-query aware: base declarations and breakpoint overrides are kept apart, so a component's
spec is not silently merged with its mobile override.

Usage
-----
    python3 extract.py --css site.css [more.css ...] \
                       --pages pages/*.html \
                       --out ./inventory

Outputs (in --out):
    rules.json      every parsed rule as [media, selector, declarations]
    atoms.json      component ID -> merged base declarations
    usage.json      page -> {component ID: count}
    report.txt      human-readable summary

Notes
-----
Nothing here decides what a component *is*. It surfaces candidates and counts evidence.
Judgement stays with the person reading the report.
"""

import argparse
import collections
import glob
import json
import os
import re
import sys

# Permissive by design. Tighten only after checking what it catches.
# Matches atomic IDs like O-ACCRD-RW-RBWM, M-CNT-ITEM-ART-DEV, A-TYPS4L-RW-DEV.
ATOMIC = re.compile(r'\b([AMOT]-[A-Z0-9]{2,}(?:-[A-Z0-9]{2,}){1,3})\b')

# Third-party class prefixes. Flag, do not attribute to the client.
THIRD_PARTY = re.compile(r'^(vjs-|ui-|slick-|swiper-|mfp-|fancybox|owl-|tns-|flatpickr)')

FOUNDATION_PROPS = (
    'font-size', 'font-weight', 'line-height', 'letter-spacing', 'font-family',
    'color', 'background-color', 'background',
    'border', 'border-color', 'border-width', 'border-radius',
    'padding', 'margin', 'width', 'height', 'min-width', 'box-shadow', 'opacity',
)


# ---------------------------------------------------------------- parsing

def parse_css(text, media=None, out=None):
    """Recursive descent over rules, preserving @media context."""
    if out is None:
        out = []
    i, n = 0, len(text)
    while i < n:
        at = text.find('@', i)
        br = text.find('{', i)
        if br == -1:
            break
        if at != -1 and at < br:
            head_end = text.find('{', at)
            if head_end == -1:
                break
            head = text[at:head_end]
            depth, j = 1, head_end + 1
            while j < n and depth:
                if text[j] == '{':
                    depth += 1
                elif text[j] == '}':
                    depth -= 1
                j += 1
            if head.startswith(('@media', '@supports')):
                parse_css(text[head_end + 1:j - 1], head.strip(), out)
            i = j
            continue
        sel = text[i:br].strip()
        depth, j = 1, br + 1
        while j < n and depth:
            if text[j] == '{':
                depth += 1
            elif text[j] == '}':
                depth -= 1
            j += 1
        out.append((media, sel, text[br + 1:j - 1].strip()))
        i = j
    return out


def merge_base_declarations(rules):
    """Merge declarations for selectors that are exactly one component class, no media."""
    merged = collections.defaultdict(dict)
    for media, sel, body in rules:
        if media:
            continue
        for part in sel.split(','):
            part = part.strip()
            m = re.fullmatch(r'\.([AMOT]-[A-Z0-9]{2,}(?:-[A-Z0-9]{2,}){1,3})', part)
            if not m:
                continue
            for decl in body.split(';'):
                if ':' in decl:
                    k, v = decl.split(':', 1)
                    merged[m.group(1)][k.strip()] = v.strip()
    return merged


# ---------------------------------------------------------------- analysis

def taxonomy(css):
    """Group class names by prefix so the naming convention reveals itself."""
    classes = set(re.findall(r'\.([A-Za-z][A-Za-z0-9_-]{2,})', css))
    families = collections.Counter()
    third_party = set()
    for c in classes:
        if THIRD_PARTY.match(c):
            third_party.add(c)
            continue
        families[re.split(r'--|__', c)[0]] += 1
    return families, third_party, len(classes)


def foundations(css):
    """Frequency-counted foundation values. Frequency separates tokens from one-offs."""
    def norm_hex(h):
        h = h.lower()
        if len(h) == 3:
            h = ''.join(c * 2 for c in h)
        return '#' + h[:6]

    return {
        'colors': collections.Counter(
            norm_hex(h) for h in re.findall(r'#([0-9a-fA-F]{3,8})\b', css)
            if len(h) in (3, 6, 8)),
        'font_sizes': collections.Counter(re.findall(r'font-size:\s*([^;}]+)', css)),
        'font_weights': collections.Counter(re.findall(r'font-weight:\s*(\d{3})', css)),
        'font_families': collections.Counter(re.findall(r'font-family:\s*([^;}]+)', css)),
        'radii': collections.Counter(re.findall(r'border-radius:\s*([^;}]+)', css)),
        'shadows': collections.Counter(re.findall(r'box-shadow:\s*([^;}]+)', css)),
        'breakpoints': collections.Counter(re.findall(r'@media[^{]*?(\d{3,4})px', css)),
        # both spellings: CSS minifiers write rgba(0,0,0,0), authors write transparent
        'transparent_borders': len(re.findall(
            r'border-color:[^;}]*(?:transparent|rgba\(0, ?0, ?0, ?0\))', css)),
    }


def usage_matrix(page_files):
    """component ID -> count, per page, main region only."""
    usage = {}
    for f in page_files:
        html = open(f, encoding='utf-8', errors='ignore').read()
        m = re.search(r'<main[^>]*>(.*?)</main>', html, re.S | re.I)
        body = m.group(1) if m else html
        usage[os.path.splitext(os.path.basename(f))[0]] = collections.Counter(ATOMIC.findall(body))
    return usage


# ---------------------------------------------------------------- report

def write_report(path, css_bytes, files, fams, third_party, total_classes,
                 found, ids, merged, usage):
    L = []
    w = L.append
    w('DESIGN SYSTEM EXTRACT')
    w('=' * 74)
    w(f'Corpus: {css_bytes:,} bytes across {len(files)} stylesheet(s)')
    w(f'Distinct classes: {total_classes:,}')
    w('Quote the corpus size with every absence claim.')
    w('')

    w('COMPONENT IDS')
    w('-' * 74)
    tiers = collections.Counter(i[0] for i in ids)
    w(f'Total: {len(ids)}   ' + '  '.join(f'{k}={v}' for k, v in sorted(tiers.items())))
    w('')
    for i in ids:
        w(f'  {i}')
    w('')

    w('CLASS FAMILIES (distinct classes per prefix)')
    w('-' * 74)
    for k, v in fams.most_common(40):
        w(f'  {v:5d}  {k}')
    if third_party:
        w('')
        w(f'THIRD-PARTY (not the client\'s system): {len(third_party)} classes')
        for c in sorted(third_party)[:20]:
            w(f'  {c}')
    w('')

    w('FOUNDATIONS')
    w('-' * 74)
    w('Colours (top 30 by frequency):')
    for k, v in found['colors'].most_common(30):
        w(f'  {k}  {v:5d}')
    w('')
    for key, label in (('font_sizes', 'Font sizes'), ('font_weights', 'Font weights'),
                       ('radii', 'Border radii'), ('breakpoints', 'Breakpoints'),
                       ('shadows', 'Box shadows')):
        w(f'{label}: ' + ', '.join(f'{k}({v})' for k, v in found[key].most_common(14)))
    w('')
    w('Font families:')
    for k, v in found['font_families'].most_common(6):
        w(f'  {v:5d}  {k[:88]}')
    if found['transparent_borders']:
        w('')
        w(f'Transparent-border declarations: {found["transparent_borders"]}. '
          'Check for border-triangle shapes (angles, arrows, tooltip tails)')
    w('')

    if usage:
        w('USAGE MATRIX')
        w('-' * 74)
        pages = sorted(usage)
        w(f'Pages sampled: {len(pages)} ({", ".join(pages)})')
        w('')
        cross = collections.defaultdict(set)
        for p in pages:
            for cid in usage[p]:
                cross[cid].add(p)
        w('Components by breadth of use:')
        for cid, ps in sorted(cross.items(), key=lambda x: (-len(x[1]), x[0])):
            w(f'  {len(ps)}/{len(pages)}  {cid:30s} {",".join(sorted(ps))}')
        w('')
        defined_only = sorted(set(ids) - set(cross))
        w(f'DEFINED IN CSS BUT ON NO SAMPLED PAGE: {len(defined_only)}')
        w('Dead code, or used on pages not sampled. Do not report as "in use".')
        for cid in defined_only[:60]:
            w(f'  {cid}')

    open(path, 'w').write('\n'.join(L) + '\n')


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--css', nargs='+', required=True, help='stylesheet files')
    ap.add_argument('--pages', nargs='*', default=[], help='sampled page HTML files')
    ap.add_argument('--out', default='./inventory', help='output directory')
    args = ap.parse_args()

    css_files = [f for pat in args.css for f in (glob.glob(pat) or [pat])]
    page_files = [f for pat in args.pages for f in (glob.glob(pat) or [pat])]
    missing = [f for f in css_files + page_files if not os.path.isfile(f)]
    if missing:
        sys.exit('Not found: ' + ', '.join(missing))

    os.makedirs(args.out, exist_ok=True)
    css = '\n'.join(open(f, encoding='utf-8', errors='ignore').read() for f in css_files)
    css_bytes = sum(os.path.getsize(f) for f in css_files)

    rules = parse_css(css)
    merged = merge_base_declarations(rules)
    fams, third_party, total_classes = taxonomy(css)
    found = foundations(css)
    ids = sorted(set(ATOMIC.findall(css)))
    usage = usage_matrix(page_files) if page_files else {}

    json.dump(rules, open(os.path.join(args.out, 'rules.json'), 'w'))
    json.dump(merged, open(os.path.join(args.out, 'atoms.json'), 'w'), indent=1)
    json.dump({k: dict(v) for k, v in usage.items()},
              open(os.path.join(args.out, 'usage.json'), 'w'), indent=1)
    write_report(os.path.join(args.out, 'report.txt'), css_bytes, css_files, fams,
                 third_party, total_classes, found, ids, merged, usage)

    print(f'Parsed {css_bytes:,} bytes, {len(rules):,} rules')
    print(f'Component IDs: {len(ids)}   Pages sampled: {len(usage)}')
    print(f'Written to {args.out}/ - read report.txt first')
    if not ids:
        print('\nNo atomic IDs matched. The client likely uses a different convention.\n'
              'read the CLASS FAMILIES section and adjust the ATOMIC pattern.')


if __name__ == '__main__':
    main()
