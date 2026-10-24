#!/usr/bin/env python3
"""Generate the GitHub profile README banner."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "profile-banner.png"
SCALE = 2

BG = (9, 11, 13)
TEXT = (242, 238, 230)
MUTED = (158, 163, 166)
DIM = (111, 118, 122)
ORANGE = (255, 106, 61)
BORDER = (43, 47, 50)

AVENIR = "/System/Library/Fonts/Avenir Next.ttc"
MENLO = "/System/Library/Fonts/Menlo.ttc"


def font(size: int, kind: str = "regular"):
    if kind == "heavy":
        return ImageFont.truetype(AVENIR, size * SCALE, index=8)
    if kind == "medium":
        return ImageFont.truetype(AVENIR, size * SCALE, index=5)
    if kind == "mono":
        return ImageFont.truetype(MENLO, size * SCALE, index=0)
    if kind == "mono-bold":
        return ImageFont.truetype(MENLO, size * SCALE, index=1)
    return ImageFont.truetype(AVENIR, size * SCALE, index=7)


def text(draw, xy, value, size, kind="regular", fill=TEXT):
    draw.text(
        (xy[0] * SCALE, xy[1] * SCALE),
        value,
        font=font(size, kind),
        fill=fill,
    )


def main() -> None:
    img = Image.new("RGB", (1280 * SCALE, 320 * SCALE), BG)
    draw = ImageDraw.Draw(img)

    for x in range(0, 1280, 64):
        draw.line((x * SCALE, 0, x * SCALE, 320 * SCALE), fill=(21, 25, 28), width=1)
    for y in range(0, 320, 64):
        draw.line((0, y * SCALE, 1280 * SCALE, y * SCALE), fill=(21, 25, 28), width=1)

    draw.rectangle(
        (64 * SCALE, 44 * SCALE, 94 * SCALE, 74 * SCALE),
        outline=ORANGE,
        width=2 * SCALE,
    )
    text(draw, (79, 59), "ZT", 12, "mono-bold", ORANGE)
    text(draw, (112, 50), "PORTFOLIO / DATA & AI SYSTEMS", 10, "mono", MUTED)

    text(draw, (64, 116), "Dr. Zhao Tang", 58, "heavy", TEXT)
    draw.rectangle(
        (64 * SCALE, 194 * SCALE, 126 * SCALE, 199 * SCALE),
        fill=ORANGE,
    )
    text(
        draw,
        (64, 222),
        "Software Engineer · Data & AI Systems",
        24,
        "medium",
        TEXT,
    )

    text(draw, (930, 60), "DATA / AI /", 16, "mono-bold", ORANGE)
    text(draw, (930, 90), "RELIABILITY", 16, "mono-bold", TEXT)
    text(draw, (930, 135), "BUILD", 10, "mono", DIM)
    text(draw, (930, 154), "MEASURE", 10, "mono", DIM)
    text(draw, (930, 173), "OPERATE", 10, "mono", DIM)
    draw.line((930 * SCALE, 204 * SCALE, 1216 * SCALE, 204 * SCALE), fill=BORDER, width=2 * SCALE)
    text(draw, (930, 226), "zt5rice.github.io", 11, "mono", MUTED)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    img.resize((1280, 320), Image.Resampling.LANCZOS).save(OUTPUT, quality=95)
    print(OUTPUT)


if __name__ == "__main__":
    main()
