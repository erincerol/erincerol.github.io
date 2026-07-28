#!/usr/bin/env python3
"""Generate favicon.ico and apple-touch-icon.png — Georgia 'E' monogram on #111."""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"

def monogram(size, radius_ratio=0.0):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    r = int(size * radius_ratio)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill="#111111")
    font = ImageFont.truetype(FONT, int(size * 0.62))
    bbox = d.textbbox((0, 0), "E", font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(((size - w) / 2 - bbox[0], (size - h) / 2 - bbox[1]), "E", font=font, fill="#FAFAFA")
    return img

# favicon.ico with rounded corners at 16/32/48
monogram(48, 0.18).save(
    os.path.join(ROOT, "favicon.ico"),
    sizes=[(16, 16), (32, 32), (48, 48)])
# apple-touch-icon: full-bleed square, iOS applies its own mask
monogram(180, 0.0).convert("RGB").save(os.path.join(ROOT, "apple-touch-icon.png"))
print("wrote favicon.ico + apple-touch-icon.png")
