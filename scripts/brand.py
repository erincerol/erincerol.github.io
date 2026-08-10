#!/usr/bin/env python3
"""Shared studio constants and helpers for the eritech.studio generators.

Imported by gen_tools.py (calculators) and gen_apps.py (app landing pages) so the
palettes, store-link tagging and OG rendering can never drift apart between them.
"""
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://eritech.studio"

CF_SNIPPET = """<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "438cd0e70d5a4d39a4ec168956408116"}'></script><!-- End Cloudflare Web Analytics -->"""

# Per-app palettes. These are the APPS' own colours, not the studio brand —
# the studio accent (#7A3B24) never appears here.
PALETTES = {
    "bakelog":   dict(bg="#FDFBF7", surface="#FFFFFF", text="#2C2523", muted="#7A716B", accent="#A4552F", line="#E5E0D8", on="#FFFFFF"),
    "kohii":     dict(bg="#FAF7F2", surface="#FFFFFF", text="#4A2C1A", muted="#7A6A5A", accent="#8F5E1B", line="#E0D5C5", on="#FFFFFF"),
    "cellar":    dict(bg="#15171A", surface="#1E2126", text="#EDEDED", muted="#8E97A0", accent="#D4B595", line="#2A2E35", on="#15171A"),
    "leaflet":   dict(bg="#0D1F0F", surface="#142B16", text="#F1F8F1", muted="#8FAF8F", accent="#4CAF50", line="#1E3320", on="#0D1F0F"),
    "warranty":  dict(bg="#10161D", surface="#18202A", text="#E8EDF2", muted="#8A97A6", accent="#5FA8D3", line="#232E3B", on="#10161D"),
    # Travel Binder: Paper/Kraft/Ink Navy/Stamp Red per ASSETS_BRIEF §2. `muted` is Faded Ink
    # darkened (#8A8273 -> #6F6857) to clear WCAG AA on Paper; app tokens are unaffected.
    "travelbinder": dict(bg="#F7F3EB", surface="#EDE3D2", text="#22314A", muted="#6F6857", accent="#C2442D", line="#D9CDB8", on="#F7F3EB"),
}

# ---------------------------------------------------------------- store links

APPSTORE_BADGE_IMG = "https://tools.applemediaservices.com/api/badges/download-on-the-app-store/black/en-us"
PLAY_BADGE_IMG = "https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png"
APPLE_PROVIDER_TOKEN = "129172097"  # account-wide, from App Analytics campaign link generator

def play_badge(pkg, campaign, medium="calculator"):
    return ('<a class="badge-play" href="https://play.google.com/store/apps/details?id=' + pkg +
            '&amp;referrer=utm_source%3Dsite%26utm_medium%3D' + medium + '%26utm_campaign%3D' + campaign +
            '" rel="noopener"><img src="' + PLAY_BADGE_IMG + '" alt="Get it on Google Play"></a>')

def ios_badge(app_id, campaign, prefix="calc"):
    return ('<a class="badge-appstore" href="https://apps.apple.com/app/id' + app_id +
            '?pt=' + APPLE_PROVIDER_TOKEN + '&amp;ct=' + prefix + '_' + campaign +
            '&amp;mt=8" rel="noopener"><img src="' + APPSTORE_BADGE_IMG +
            '" alt="Download on the App Store"></a>')

# ---------------------------------------------------------------- OG images

from PIL import Image, ImageDraw, ImageFont

OG_DIR = os.path.join(REPO, "assets", "og")
os.makedirs(OG_DIR, exist_ok=True)
TITLE_FONT = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Bold.ttf", 78)
SUB_FONT = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 34)

def og_image(fname, title, pal, kicker="Free tool  ·  eritech.studio/tools"):
    img = Image.new("RGB", (1200, 630), pal["bg"])
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 22, 630], fill=pal["accent"])
    words, lines, cur = title.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=TITLE_FONT) > 1010:
            lines.append(cur); cur = w
        else:
            cur = t
    lines.append(cur)
    y = 315 - (len(lines) * 96) // 2 - 40
    for ln in lines:
        d.text((90, y), ln, font=TITLE_FONT, fill=pal["text"])
        y += 96
    d.text((90, 520), kicker, font=SUB_FONT, fill=pal["muted"])
    img.save(os.path.join(OG_DIR, fname), "PNG")
    print("wrote assets/og/" + fname)

# ---------------------------------------------------------------- the apps

# Single source of truth for app identity, used by both generators and the sitemap.
# `web_accent` is the app's colour as used on cream site chrome (index cards, group
# markers) — darker than some in-app accents so it holds contrast on #FAF7F2.
APPS = [
    dict(slug="kohii", web_accent="#8F5E1B", name="Kohii", full="Kohii — The Barista Log", palette="kohii",
         app_id="6790972283", pkg="com.eritech.kohii", privacy="kohii.html",
         tools=["coffee-ratio-calculator", "espresso-ratio-calculator", "coffee-freshness-calculator"]),
    dict(slug="the-bake-log", web_accent="#A4552F", name="The Bake Log", full="The Bake Log: Sourdough Baker", palette="bakelog",
         app_id="6790971986", pkg="com.eritech.thebakelog", privacy="the-bake-log.html",
         tools=["sourdough-hydration-calculator", "bakers-percentage-calculator", "starter-feeding-ratio-calculator", "dough-temperature-calculator", "pizza-dough-calculator"]),
    dict(slug="warranty-box", web_accent="#2F6E9E", name="Warranty Box", full="Warranty Box — Track Expiry", palette="warranty",
         app_id="6790972644", pkg="com.eritech.warrantybox", privacy="warranty-box.html",
         tools=["uk-return-rights-checker"]),
    dict(slug="cellar-book", web_accent="#722F37", name="Cellar Book", full="Cellar Book: Wine Cellar Log", palette="cellar",
         app_id="6796370046", pkg="com.eritech.cellarbook", privacy="cellarbook.html",
         tools=["wine-drink-window-calculator", "wine-cellar-value-calculator"]),
    dict(slug="leaflet", web_accent="#2E7D32", name="Leaflet", full="Leaflet: Plant Care & Watering", palette="leaflet",
         app_id="6796375617", pkg="com.eritech.leaflet", privacy="leaflet.html",
         tools=["plant-watering-calculator"]),
    dict(slug="travel-binder", web_accent="#22314A", name="The Travel Binder", full="The Travel Binder: Trip Planner", palette="travelbinder",
         app_id="6797601401", pkg="com.eritech.travelbinder", privacy="travel-binder.html",
         tools=["packing-list-generator", "japan-trip-cost-calculator"]),
]

ACCENT_BY_APP = {a["name"]: a["web_accent"] for a in APPS}
