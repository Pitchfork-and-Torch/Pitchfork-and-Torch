"""Convert GitHub avatar to dense ASCII for the profile neofetch card.

Samples the photo with monospace cell aspect correction so the face is not
squished when rendered with tall character cells.
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets" / "avatar.jpg"
OUT = ROOT / "assets" / "avatar-ascii.txt"

# Columns (horizontal resolution). Rows are derived from photo aspect + char cell.
WIDTH = 72

# Monospace glyphs are ~0.55 as wide as they are tall. Correct sample grid so
# the rendered portrait matches the photo proportions.
CHAR_ASPECT = 0.55  # char_width / char_height

# User request: a bit more vertical presence than pure 1:1 match.
HEIGHT_BOOST = 1.15  # +15% taller

# Classic dense ramp; dark pixels map to denser glyphs.
CHARS = " .:-=+*#%@"


def main() -> None:
    img = Image.open(SRC).convert("L")
    w, h = img.size
    # Crop center face (cut floral wallpaper edges)
    left = int(w * 0.10)
    top = int(h * 0.02)
    right = int(w * 0.90)
    bottom = int(h * 0.95)
    img = img.crop((left, top, right, bottom))
    cw, ch = img.size
    photo_aspect = ch / cw  # height / width of the cropped photo

    # rows so that (rows * char_h) / (cols * char_w) ≈ photo_aspect * boost
    # → rows / cols ≈ photo_aspect * CHAR_ASPECT * boost
    height = max(
        24,
        int(round(WIDTH * photo_aspect * CHAR_ASPECT * HEIGHT_BOOST)),
    )

    img = ImageOps.autocontrast(img, cutoff=3)
    img = ImageEnhance.Contrast(img).enhance(1.5)
    img = ImageEnhance.Brightness(img).enhance(1.05)
    img = img.filter(ImageFilter.SMOOTH_MORE)
    img = ImageOps.posterize(img, bits=4)
    img = img.resize((WIDTH, height), Image.Resampling.LANCZOS)

    pixels = list(img.get_flattened_data())
    n = len(CHARS) - 1
    lines: list[str] = []
    for y in range(height):
        row = pixels[y * WIDTH : (y + 1) * WIDTH]
        chars = []
        for p in row:
            idx = n - int((p / 255) * n)
            chars.append(CHARS[idx])
        lines.append("".join(chars).rstrip())

    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()

    text = "\n".join(lines) + "\n"
    OUT.write_text(text, encoding="utf-8")
    print(text)
    print(
        f"--- wrote {OUT} ({len(lines)} lines × {max(map(len, lines))} cols) "
        f"photo_aspect={photo_aspect:.3f} char_aspect={CHAR_ASPECT} boost={HEIGHT_BOOST} ---"
    )


if __name__ == "__main__":
    main()
