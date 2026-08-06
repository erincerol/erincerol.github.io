# Eri Tech Studio — brand asset spec

Delivered August 2026. Direction **The Keeper**, cut A. Everything here is geometry and outlines: no file
depends on a font being installed, and no file contains a gradient, bevel, shadow or non-uniform stroke.

---

## 1. The mark

Two corner mounts, diagonally opposed, holding an empty portrait space. It is the apparatus of an album
page — the thing that keeps a record in place without printing on it, altering it, or taking it away.

Drawn on a **32-unit grid**, so 1 unit = 0.5 px at favicon size and every measure lands on a half-pixel.

| Measure | Units | At 16 px |
|---|---|---|
| Mark bounding box | 26 × 27 | 13 × 13.5 px |
| Vertical arm thickness | 4.9 | 2.45 px |
| Horizontal arm thickness | 4.6 | 2.30 px |
| Vertical arm reach | 16.0 | 8.0 px |
| Horizontal arm reach | 12.5 | 6.25 px |
| Outer corner radius | 2.6 | 1.3 px |
| Inner corner fillet | 1.2 | 0.6 px |

Four corrections are baked in and must survive any redraw:

1. **Horizontal arms are 6% thinner than vertical arms.** A horizontal bar reads heavier than a vertical
   one at equal measure. Equalising the numbers un-equalises the mark.
2. **The inner corner is filleted, not mitred.** A sharp inner angle traps ink and prints as a blob at
   small sizes. The fillet is roughly a quarter of the outer radius, which is how a die-cut corner behaves.
3. **The arms are deliberately unequal — vertical longer than horizontal.** This is load-bearing. Equal
   arms make a viewfinder, a crop mark, a QR target. Unequal arms make the held space *portrait*, and a
   portrait rectangle is a card, a page, a photograph. If someone "tidies" this to a square, the mark
   stops meaning anything.
4. **Arm ends are square-cut.** Rounded ends soften the mark into something clinical and eat a third of
   the arm's mass at 16 px.

### The round cut

Circular and squircle masks remove the corners, which is where this mark keeps its mass. So for every
masked surface the mark is the **same drawing scaled to 0.724 about its centre**, which puts the outer
corner arcs exactly on the 80% maskable safe circle.

It is not a redrawn simplification — there is nothing to simplify. It is the mark with the margin the
mask demands. Used in `apple-touch-icon.png`, `icon-192.png`, `icon-512.png`,
`play-developer-icon.png`, `avatar.png` and `logo-mark-round.svg`.

---

## 2. The wordmark

**Fraunces 72pt SemiBold** — that is opsz 72, wght 600, SOFT 0, WONK 0. Not the variable font's default
instance, which resolves to wght 900 / opsz 9 / WONK 1 and is far too heavy and quirky for a logotype.
Not the 144pt cut either, which is too high-contrast below about 40 px.

Corrections applied on top of the typed letterforms:

- **Tracking −14/1000 em** with kerning on. A display serif set at logotype size wants a tighter fit than
  its default.
- **Word space reduced to 82%** of the font's default (191.5 → 157 units). `i` followed by `T` already
  has a large optical opening, because the T's left arm sits high and the i is short. The default space
  reads as a gap.
- **Vertical alignment by cap height (700 units), not bounding box.** The `h` in Tech ascends to 743, so
  bbox alignment would sit the whole wordmark low.
- **All type converted to outlines.** Every delivered SVG renders identically on a machine with no fonts
  installed at all.

`Eri Tech` is the wordmark. `Eri Tech Studio` is the company's name in prose; it is too long for the
horizontal lockup and turns to dirt below about 140 px wide. `eritech.studio` belongs in the footer.

---

## 3. Palette

The one change from the brief: **the accent moves from Terracotta `#A4552F` to Iron Oxide `#7A3B24`.**
Same hue family, roughly 30% darker. The reason is not favouritism — nobody counts hues — it is that
`#A4552F` sits at the same lightness and saturation as The Bake Log's `#C26D43` and Travel Binder's
`#C2442D`, so the studio colour reads as a peer in the row rather than the ground beneath it. A parent
brand should be the darkest and quietest thing on the page. It also clears 4.5:1 on Paper, which the
lighter tone only just managed.

| Name | Hex | Role |
|---|---|---|
| Paper | `#FAF7F2` | grounds, email tiles, all full-bleed icons |
| Warm Ink | `#1F1A15` | the mark, display text, linework |
| Body Ink | `#3B342C` | body text |
| **Iron Oxide** | **`#7A3B24`** | the accent — links, marks, small emphasis |
| Muted | `#998F83` | secondary text |
| Hairline | `#E9E3D9` | borders, rules, the email tile edge |

**Site change required:** find-and-replace `#A4552F` → `#7A3B24` across the repo, then re-export nothing —
no delivered asset uses the accent. The mark is Warm Ink on Paper, or Paper on Warm Ink. Colour is never
load-bearing.

---

## 4. Clear space and minimums

- **Clear space:** one quarter of the mark's height on all sides, measured **from the arm ends**, not from
  the implied card — the card is invisible and therefore useless as a measure.
- **Minimums:** mark 16 px · horizontal lockup 120 px wide · stacked lockup 80 px wide.
- **The wordmark never appears below 24 px of mark height.** `email-logo.png` sits exactly on that floor
  by design; nothing should go under it.
- **Not cleared for photographic backgrounds.** If unavoidable, use an opaque Paper tile.
- **Never place the mark on a coloured rounded square.** That is what an app icon is. The whole reason
  this mark survives next to the six is that it is a different category of object — line and space on the
  page, beside illustrations in tiles. Putting it in a tile throws that away and makes it a seventh app.

---

## 5. File manifest

Paths mirror the target repo `erincerol/erincerol.github.io` exactly, so each folder drops straight in.

### `brand/root/` → repo root

| File | Size | Notes |
|---|---|---|
| `favicon.svg` | 32 viewBox | Warm Ink, explicit `fill` on both paths. Add the dark swap yourself — see §6 |
| `favicon-onDark.svg` | 32 viewBox | Paper. Standalone dark cut, in case you prefer two files to one |
| `favicon-16.png` | 16 | Transparent. Source for the `.ico` — see §6 |
| `favicon-32.png` | 32 | Transparent |
| `favicon-48.png` | 48 | Transparent |
| `apple-touch-icon.png` | 180 | Opaque Paper, full bleed, **no rounded corners, no alpha**. Round cut |
| `icon-192.png` | 192 | Opaque Paper, round cut, safe inside the 80% maskable circle |
| `icon-512.png` | 512 | As above |

### `brand/assets/brand/` → `/assets/brand/`

| File | Size | Notes |
|---|---|---|
| `logo-master.svg` | 949 × 2624 | Source of truth. Seven named artboards: `artboard-mark`, `-mark-onDark`, `-mark-round`, `-horizontal`, `-horizontal-onDark`, `-stacked`, `-stacked-onDark` |
| `logo-mark.svg` / `.png` | 32 vb / 512 | Warm Ink, transparent |
| `logo-mark-onDark.svg` / `.png` | 32 vb / 512 | Paper, transparent |
| `logo-mark-round.svg` | 32 vb | The 0.724 cut, for anything masked |
| `logo-horizontal.svg` / `.png` | 725 × 160 | Mark + wordmark |
| `logo-horizontal-onDark.svg` / `.png` | 725 × 160 | |
| `logo-stacked.svg` / `.png` | 386 × 320 | Mark above wordmark |
| `logo-stacked-onDark.svg` / `.png` | 386 × 320 | |
| `og-default.png` | 1200 × 630 | Paper ground, stacked lockup, generous margin |

### `brand/assets/badges/` → `/assets/badges/`

Both are **opaque** with a visible hairline edge, and both are raster only — Outlook will not render SVG,
and a transparent PNG with dark ink becomes an invisible smudge when a mail client inverts the message
background. No CSS fix works across Gmail, Outlook and Apple Mail together.

| File | Size | Displays at |
|---|---|---|
| `email-logo.png` | 320 × 80 | 160 × 40 — set `width` and `height` explicitly |
| `email-mark.png` | 80 × 80 | 40 × 40 |

### `brand/store/`

| File | Size | Notes |
|---|---|---|
| `play-developer-icon.png` | 512 | Opaque Paper, no rounded corners, round cut |
| `play-developer-header.png` | 4096 × 2304 | Paper ground, stacked lockup at 33% of frame height, centred. Play crops this hard on some layouts — the lockup sits well inside a central safe area with no artwork anywhere near the edge |
| `avatar.png` | 512 | **Warm Ink ground, Paper mark** — deliberately inverted. Reddit feeds are white or near-black; a Paper-ground avatar with a hairline edge disappears on white. Reads inside a circular crop |

### Favicon markup

```html
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<!-- do NOT add media="(prefers-color-scheme: ...)" here; Chrome ignores it on rel=icon -->
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest">
```

---

## 6. The two things not delivered, and what to do

### `favicon.ico`

A multi-resolution `.ico` is a container format, not an image — it cannot be authored as vector or canvas
output. The three PNGs are drawn and checked individually at their exact sizes; pack them without
resampling:

```sh
magick brand/root/favicon-16.png brand/root/favicon-32.png brand/root/favicon-48.png favicon.ico
```

Or, if you would rather not install ImageMagick:

```sh
pip install pillow
python -c "from PIL import Image; \
Image.open('brand/root/favicon-48.png').save('favicon.ico', sizes=[(16,16),(32,32),(48,48)])"
```

The Pillow route resamples from 48 rather than using the hand-checked 16, so prefer the first. Verify
afterwards that the 16 px frame in the packed file is pixel-identical to `favicon-16.png` — some tools
silently re-render.

### The dark-mode favicon swap

`favicon.svg` ships Warm Ink with an explicit `fill` on each path, so light mode is correct and it matches
the three PNGs exactly. The `prefers-color-scheme` rule is **not** in the file: a `<style>` element does
not survive my write path, with or without CDATA, and shipping a favicon whose only fill declaration lives
in a stripped element would render it pure black. Explicit fills fail safe; a missing rule does not.

Paste these three lines into `favicon.svg`, immediately after `<title>`:

```xml
  <style type="text/css">
    @media (prefers-color-scheme: dark) { .m { fill: #FAF7F2 } }
  </style>
```

Both paths already carry `class="m"`, so nothing else changes: the media rule overrides the presentation
attribute in dark mode and is inert in light mode. Ten seconds of work, and it is the only hand edit in the
whole set.

Do not try to do this with `media` on `<link rel="icon">` instead — Firefox honours it, Chrome ignores it,
and you would get the light mark on a dark tab bar in the browser most of your visitors use.
`favicon-onDark.svg` is delivered for anywhere you're placing the asset by hand rather than relying on the
browser, which is the only case where two files beat one.

### Play Console dimensions

`play-developer-header.png` is 4096 × 2304 and `play-developer-icon.png` is 512 × 512, per the brief.
Google changes these without notice. **Check both against the Play Console upload fields before final
export.** If the header spec has moved, the lockup is centred at 33% of frame height and re-exports
cleanly at any 16:9 or wider frame from `logo-master.svg` — nothing is pinned to 4096.

---

## 7. Accept criteria

| Criterion | Status |
|---|---|
| 16 × 16 favicon legible at 100% zoom on a real tab bar | Pass. Two elements, no counters |
| No stroke thinner than 2 px at 16 px | Pass. Thinnest is 2.30 px |
| No counter that fills in | Pass. There are no counters |
| `apple-touch-icon` survives a circular mask; no alpha, no pre-rounded corners | Pass, via the round cut |
| Mark survives black-on-white at 24 px | Pass |
| Email PNGs opaque and legible on `#FFFFFF` and `#1A1A1A` | Pass |
| All type outlined; SVGs render without Fraunces | Pass |
| `favicon.svg` carries a `prefers-color-scheme: dark` swap | **Needs one hand edit** — three lines, given verbatim in §6 |
| Reads beside the six app icons without becoming a seventh | Pass — see the note in §4 about coloured tiles, which is the only way to break this |
| No gradient, bevel, shadow, or inconsistently scaling stroke | Pass |

## 8. One thing outside this brief

**WarrantyBox's icon is the odd one out in your own portfolio** — a bold white monogram in an angular
black tile, geometric where the other five are warm and illustrative, and the only one that looks like a
tech product rather than a hobby. It is not part of this commission. But once the studio mark sits at the
top of the developer page, WarrantyBox is the icon that will look wrong first.
