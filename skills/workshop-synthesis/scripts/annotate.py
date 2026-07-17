#!/usr/bin/env python3
"""Mark unreadable notes on a workshop photo so a human can decipher them.

Draws a labelled box around each flagged note and writes an annotated copy
alongside a legend strip listing what is being asked about each one.

Usage:
    python3 annotate.py --image WALL.jpg --marks marks.json [--out annotated.jpg]

marks.json:
    [
      {"id": "W1-N014", "box": [0.31, 0.22, 0.39, 0.30], "ask": "illegible - looks like 'latency'?"},
      {"id": "W1-N022", "box": [0.55, 0.61, 0.63, 0.69], "ask": "obscured by note in front"}
    ]

box is [x0, y0, x1, y1] normalised 0-1 from the top-left of the image, so the
coordinates survive any resizing done while reading the photo.
"""

import argparse
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# Loud on yellow, pink, orange and green stickies alike; nobody writes in this.
MARK_COLOR = (255, 0, 200)
TEXT_COLOR = (255, 255, 255)
LEGEND_BG = (24, 24, 28)
LEGEND_FG = (235, 235, 240)

MAC_FONTS = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/Library/Fonts/Arial Bold.ttf",
]


def load_font(size):
    for path in MAC_FONTS:
        if Path(path).exists():
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue
    try:
        return ImageFont.load_default(size)
    except TypeError:  # Pillow < 9.2 has no size arg
        return ImageFont.load_default()


def text_size(draw, text, font):
    x0, y0, x1, y1 = draw.textbbox((0, 0), text, font=font)
    return x1 - x0, y1 - y0


def validate(marks):
    seen = set()
    for i, m in enumerate(marks):
        where = f"marks[{i}]"
        for key in ("id", "box"):
            if key not in m:
                sys.exit(f"{where}: missing required key '{key}'")
        if m["id"] in seen:
            sys.exit(f"{where}: duplicate id {m['id']!r} — ids must be unique")
        seen.add(m["id"])
        box = m["box"]
        if len(box) != 4:
            sys.exit(f"{where}: box needs 4 values [x0,y0,x1,y1], got {len(box)}")
        if not all(isinstance(v, (int, float)) and 0.0 <= v <= 1.0 for v in box):
            sys.exit(f"{where}: box values must be numbers in 0-1, got {box}")
        if box[0] >= box[2] or box[1] >= box[3]:
            sys.exit(f"{where}: box must be [x0,y0,x1,y1] with x0<x1 and y0<y1, got {box}")


def draw_marks(img, marks, font, line_w, pad):
    draw = ImageDraw.Draw(img)
    w, h = img.size
    for m in marks:
        x0, y0, x1, y1 = m["box"]
        px = (x0 * w, y0 * h, x1 * w, y1 * h)
        draw.rectangle(px, outline=MARK_COLOR, width=line_w)

        label = m["id"]
        tw, th = text_size(draw, label, font)
        bw, bh = tw + pad * 2, th + pad * 2

        # Prefer a badge above the box; drop it inside when there is no headroom.
        bx = min(px[0], w - bw)
        by = px[1] - bh - line_w
        if by < 0:
            by = px[1] + line_w
        draw.rectangle([bx, by, bx + bw, by + bh], fill=MARK_COLOR)
        draw.text((bx + pad, by + pad), label, fill=TEXT_COLOR, font=font)
    return img


def add_legend(img, marks, font, pad):
    """Strip under the photo: what we need deciphered, in reading order."""
    w = img.size[0]
    probe = ImageDraw.Draw(img)
    line_h = text_size(probe, "Ag", font)[1] + pad
    header = "Unreadable — please decipher:"
    height = pad * 2 + line_h * (len(marks) + 1)

    out = Image.new("RGB", (w, img.size[1] + height), LEGEND_BG)
    out.paste(img, (0, 0))
    draw = ImageDraw.Draw(out)

    y = img.size[1] + pad
    draw.text((pad, y), header, fill=LEGEND_FG, font=font)
    y += line_h
    for m in marks:
        ask = m.get("ask", "")
        line = f"  {m['id']}" + (f" — {ask}" if ask else "")
        draw.text((pad, y), line, fill=MARK_COLOR, font=font)
        y += line_h
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--image", required=True, help="source photo")
    ap.add_argument("--marks", required=True, help="JSON file of notes to flag")
    ap.add_argument("--out", help="output path (default: <image>.annotated.jpg)")
    ap.add_argument("--no-legend", action="store_true", help="skip the legend strip")
    args = ap.parse_args()

    src = Path(args.image)
    if not src.exists():
        sys.exit(f"no such image: {src}")

    try:
        marks = json.loads(Path(args.marks).read_text())
    except json.JSONDecodeError as e:
        sys.exit(f"{args.marks}: invalid JSON — {e}")
    if not isinstance(marks, list) or not marks:
        sys.exit("marks must be a non-empty JSON array")
    validate(marks)

    img = Image.open(src)
    # EXIF-rotated phone photos would otherwise land the boxes on the wrong notes.
    try:
        from PIL import ImageOps
        img = ImageOps.exif_transpose(img)
    except Exception:
        pass
    img = img.convert("RGB")

    # Scale with the image so marks read the same on a 12MP photo and a screenshot.
    scale = max(img.size) / 1600
    font = load_font(max(14, int(22 * scale)))
    line_w = max(3, int(4 * scale))
    pad = max(4, int(6 * scale))

    img = draw_marks(img, marks, font, line_w, pad)
    if not args.no_legend:
        img = add_legend(img, marks, font, pad)

    out = Path(args.out) if args.out else src.with_suffix(f".annotated{src.suffix or '.jpg'}")
    img.save(out, quality=92)
    print(f"{out}  ({len(marks)} marked)")


if __name__ == "__main__":
    main()
