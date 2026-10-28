#!/usr/bin/env python3
"""Per-item tool pages: one URL per plant, per wine style and per packing preset, built on the parent calculators."""
import html
import math
import re

from brand import DOMAIN, SITE_LASTMOD, BRAND, ios_badge, play_badge, plain_text
import content_guides
import content_plants
import content_wine
import gen_pairings

YEAR = int(SITE_LASTMOD[:4])

PLANT_PARENT = "plant-watering-calculator"
WINE_PARENT = "wine-drink-window-calculator"
PACKING_PARENT = "packing-list-generator"
JAPAN_COST = "japan-trip-cost-calculator"

PLANT_LINE = ('<strong><a href="/apps/leaflet/">Leaflet</a></strong> works out this schedule for every plant you own '
              'and reminds you.')
WINE_LINE = ('<strong><a href="/apps/cellar-book/">Cellar Book</a></strong> tracks every bottle&rsquo;s window and '
             'tells you what to open tonight.')
PACKING_LINE = ('<strong><a href="/apps/travel-binder/">The Travel Binder</a></strong> keeps the list, the bookings and '
                'the documents in one offline binder.')

PLANT_SUB = ("A starting point, not a rule — check the soil before each watering and let the top few centimetres "
             "dry out first.")

WINE_PAIRINGS = {
    "barolo": ["game", "red-meat"],
    "bordeaux": ["lamb", "red-meat"],
    "bordeaux-everyday": ["red-meat", "lamb"],
    "red-burgundy": ["game", "poultry"],
    "napa-cabernet": ["red-meat", "cheese"],
    "northern-rhone-syrah": ["game", "red-meat"],
    "rioja-gran-reserva": ["lamb", "red-meat"],
    "chianti-classico-riserva": ["pasta-rice", "red-meat"],
    "white-burgundy": ["poultry", "fish"],
    "german-riesling": ["spicy", "pork"],
    "vintage-champagne": ["shellfish", "fish"],
    "vintage-port": ["cheese", "dessert"],
}

PACKING_PRESETS = [
    dict(slug="japan-winter", chip="Japan in winter", title="Japan packing list for December",
         h1="Japan packing list for December", nights=14, climate="cold", style="city", laundry=True, carry=False,
         meta="A 14-night Japan packing list for December to February: layers for Tokyo and Hokkaido, shoes you can "
              "slip off, IC card and cash. Edit it for your trip."),
    dict(slug="japan-spring", chip="Japan in spring",
         title="Japan packing list for cherry blossom season (March–April)",
         h1="Japan packing list for cherry blossom season (March&ndash;April)", nights=10, climate="mild",
         style="city", laundry=True, carry=False,
         meta="A 10-night Japan packing list for cherry blossom season: light layers, rain cover, a pollen mask, IC "
              "card and cash. Edit it for your own dates."),
]

CLIMATES = {
    "freezing": ("freezing", ["Thermal base layers &times;2", "Insulated coat", "Fleece or mid layer",
                              "Wool hat, gloves and scarf", "Thick socks &times;3", "Waterproof boots"]),
    "cold": ("cold", ["Warm coat", "Jumper or fleece &times;2", "Thermal top &times;1", "Hat and gloves", "Scarf",
                      "Water-resistant shoes"]),
    "mild": ("mild", ["Light jacket", "Jumper &times;1", "Packable rain shell", "Comfortable walking shoes"]),
    "warm": ("warm", ["Light overshirt or cardigan", "Packable rain shell", "Sunglasses", "Sun hat"]),
    "hot": ("hot and humid", ["Linen overshirt", "Packable rain shell", "Sunglasses", "Sun hat", "Quick-dry towel"]),
}
TRIP_STYLES = {
    "city": ["Day bag or small backpack", "Walking shoes, already worn in", "Compact umbrella", "Portable battery"],
    "outdoors": ["Hiking boots", "Daypack 20&ndash;30L", "Water bottle", "Blister plasters", "Head torch", "Dry bag"],
    "beach": ["Swimwear &times;2", "Quick-dry towel", "Flip flops", "Reef-safe sun cream", "After-sun"],
    "business": ["Suit or smart outfit", "Dress shoes", "Laptop and charger", "Wrinkle spray or travel steamer"],
}

CHIP_CSS = """.pick{margin:0 0 18px}
.pick-title{font-size:.85rem;color:var(--muted);margin:0 0 8px}
.chips{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:8px}
.chips a,.chips a:visited{display:inline-flex;align-items:center;min-height:44px;padding:0 14px;border:1px solid var(--line);border-radius:16px;background:var(--surface);color:var(--text);text-decoration:none;font-size:.92rem;white-space:nowrap}
.chips a:hover{border-color:var(--accent)}
.chips a[aria-current=page],.chips a[aria-current=page]:visited{background:var(--line);border-color:var(--accent);color:var(--accent)}
@media(max-width:600px){
.chips{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;margin:0 -20px;padding:0 20px}
.chips::-webkit-scrollbar{display:none}
.chips li{flex:none}
}
"""


def js_round(x):
    return math.floor(x + 0.5)


def plant_interval(lo, hi, season, light):
    a, b = js_round(lo * season * light), js_round(hi * season * light)
    a = max(a, 1)
    return a, (b if b > a else a + 1)


def days(lo, hi):
    return "%d&ndash;%d" % (lo, hi)


def bare(phrase):
    words = re.sub(r"^(a|an) ", "", phrase)
    return words[0].upper() + words[1:]


def chips(label, base, items, current):
    return ('<nav class="pick" aria-label="' + label + '">\n<p class="pick-title">' + label + '</p>\n<ul class="chips">\n' +
            "\n".join('<li><a href="/tools/' + base + '/' + slug + '/"' +
                      (' aria-current="page"' if slug == current else '') + '>' + text + '</a></li>'
                      for slug, text in items) + '\n</ul>\n</nav>\n')


def sections(blocks):
    return "<section>\n" + "\n".join('<h2>' + h + '</h2>\n<p>' + p + '</p>' for h, p in blocks) + "\n</section>"


def app_line(app_id, pkg, campaign, line):
    return ('<p>' + line + '</p>\n<div class="badges">' + ios_badge(app_id, campaign) +
            play_badge(pkg, campaign) + '</div>')


def parent_crumb(parent):
    return '<span>/</span><a href="/tools/' + parent["slug"] + '/">' + parent["og_title"] + '</a>'


def item_page(parent, slug, **kw):
    page = dict(slug=parent["slug"] + "/" + slug, og=parent["slug"] + "-" + slug, palette=parent["palette"],
                calc_js=parent["calc_js"], related_slug=parent["slug"], crumb_extra=parent_crumb(parent),
                parent=(parent["og_title"], DOMAIN + "/tools/" + parent["slug"] + "/"), depth="",
                extra_css=parent.get("extra_css", "") + CHIP_CSS)
    page.update(kw)
    return page


def fill_result(calc_html, out, sub):
    empty = '<div class="big" id="out">&mdash;</div><div class="sub" id="outsub"></div>'
    assert calc_html.count(empty) == 1
    return calc_html.replace(empty, '<div class="big" id="out">' + html.escape(out, quote=False) +
                             '</div><div class="sub" id="outsub">' + html.escape(sub, quote=False) + '</div>')


def plant_pages(parent, species, plant_calc):
    assert list(content_plants.PLANTS) == [s[0] for s in species]
    items = [(slug, bare(phrase)) for slug, _, phrase, _, _ in species]
    parent["chips"] = chips("By plant", parent["slug"], items, None)
    parent["extra_css"] = parent.get("extra_css", "") + CHIP_CSS
    pages = []
    for slug, _, phrase, lo, hi in species:
        c = content_plants.PLANTS[slug]
        summer = plant_interval(lo, hi, 1, 1)
        winter = plant_interval(lo, hi, 1.6, 1.3)
        question = "How often should I water " + phrase + "?"
        meta = ("How often to water " + phrase + ": every %d–%d days in spring and summer, %d–%d in a dim winter room. "
                % (summer + winter) + c["tip"])
        explainer = sections(c["explainer"]) + (
            '\n<p class="note">The <a href="/tools/' + parent["slug"] + '/">plant watering calculator</a> explains how '
            'the intervals are worked out for every plant on the list.</p>')
        campaign = "plant_watering_" + slug.replace("-", "_")
        pages.append(item_page(
            parent, slug, tab_title=question + " | " + BRAND, og_title=question, h1=question, lede=c["lede"],
            meta_desc=meta, calc_html=fill_result(plant_calc(slug), "Every %d–%d days" % summer, PLANT_SUB),
            explainer=explainer, faqs=c["faqs"], chips=chips("By plant", parent["slug"], items, slug), chip_label=bare(phrase),
            app_block=app_line("6796375617", "com.eritech.leaflet", campaign, PLANT_LINE), campaign=campaign))
    return pages


def wine_verdict(vintage, lo, hi):
    a, b = vintage + lo, vintage + hi
    third = (b - a) / 3
    if YEAR < a:
        n = a - YEAR
        return "Still ageing — about %d more year%s before the window opens." % (n, "" if n == 1 else "s")
    if YEAR <= b:
        if a + third <= YEAR <= b - third:
            return "In its drink window and around its likely peak. A very good time to open one."
        if YEAR < a + third:
            return "The window has just opened — drinking well now, and should improve further."
        return "In its window but on the later slope — drink sooner rather than later."
    return "Past its likely window. It may still be enjoyable, but expect faded fruit — open it with modest expectations."


def vintages_paragraph(name, lo, hi):
    third = (hi - lo) / 3
    first, last = YEAR - hi, YEAR - lo
    peak_first, peak_last = math.ceil(YEAR - hi + third), math.floor(YEAR - lo - third)
    text = ("On the calculator&rsquo;s figures, the " + name + " vintages in their window in %d run from %d to %d"
            % (YEAR, first, last))
    if peak_first <= peak_last:
        text += ", and those from %d to %d sit around the likely peak" % (peak_first, peak_last)
    return text + ". Anything from %d onwards is still ageing. Enter your own vintage above to check it." % (last + 1)


def wine_pages(parent, styles, drink_window_calc, families):
    phrases = {f["id"]: f["phrase"] for f in families}
    named = [s for s in styles if s[0]]
    assert list(content_wine.STYLES) == [s[0] for s in named]
    assert set(WINE_PAIRINGS) == set(content_wine.STYLES)
    assert all(fid in phrases for ids in WINE_PAIRINGS.values() for fid in ids)
    items = [(slug, bare(name)) for slug, _, name, _, _ in named]
    parent["chips"] = chips("By style", parent["slug"], items, None)
    parent["extra_css"] = parent.get("extra_css", "") + CHIP_CSS
    vintage = int(re.search(r'id="vintage" value="(\d+)"', drink_window_calc(named[0][0])).group(1))
    pages = []
    for slug, _, name, lo, hi in named:
        c = content_wine.STYLES[slug]
        question = "When should I drink " + name + "?"
        links = " or ".join('<a href="/tools/' + gen_pairings.SLUG + '/' + fid + '/">' + phrases[fid] + '</a>'
                            for fid in WINE_PAIRINGS[slug])
        explainer = sections(c["explainer"] + [
            ("Which vintages are ready", vintages_paragraph(name, lo, hi))]) + (
            '\n<p>Planning the meal? See what goes with ' + links + ' in the <a href="/tools/' + gen_pairings.SLUG +
            '/">wine pairing finder</a>, or how the windows are set on the <a href="/tools/' + parent["slug"] +
            '/">drink window calculator</a>.</p>')
        meta = (plain_text("When to drink " + name) + ": from %d to %d years after the vintage, so %d–%d vintages are "
                "in their window in %d. Check yours free." % (lo, hi, YEAR - hi, YEAR - lo, YEAR))
        campaign = "drink_window_" + slug.replace("-", "_")
        pages.append(item_page(
            parent, slug, tab_title=plain_text(question) + " Drinking window by vintage | " + BRAND,
            og_title=plain_text(question), h1=question, lede=c["lede"], meta_desc=meta,
            calc_html=fill_result(drink_window_calc(slug), "Drink %d – %d" % (vintage + lo, vintage + hi),
                                  wine_verdict(vintage, lo, hi)),
            explainer=explainer, faqs=c["faqs"], chips=chips("By style", parent["slug"], items, slug), chip_label=bare(name),
            app_block=app_line("6796370046", "com.eritech.cellarbook", campaign, WINE_LINE), campaign=campaign))
    return pages


def packing_groups(nights, climate, style, laundry, carry):
    wear = min(nights, 7) if laundry else min(nights, 14)
    socks, tops, bottoms = min(wear + 1, 15), max(2, min(wear, 10)), max(1, min(math.ceil(wear / 4), 4))
    if carry:
        tops, bottoms, socks = min(tops, 6), min(bottoms, 2), min(socks, 8)
    sleep = 2 if nights > 7 else 1
    return [
        ("Clothing", ["Underwear &times;%d" % socks, "Socks &times;%d" % socks, "Tops &times;%d" % tops,
                      "Trousers or skirts &times;%d" % bottoms, "Sleepwear &times;%d" % sleep]),
        ("Layers and outerwear", CLIMATES[climate][1]),
        ("Toiletries", ["Toothbrush and paste", "Deodorant", "Shampoo and shower gel" + (" (&le;100 ml)" if carry else ""),
                        "Razor", "Prescriptions in original packaging", "Painkillers and plasters"]),
        ("Tech", ["Phone and charger", "Plug adapter for the destination", "Portable battery", "Headphones",
                  "Spare cable"]),
        ("Documents and money", ["Passport, 6+ months validity", "Visa or entry registration if required",
                                 "Travel insurance details", "Two cards, carried separately", "Some local cash",
                                 "Offline copies of every booking"]),
        ("For this trip", TRIP_STYLES[style]),
    ]


def packing_calc(parent_calc, p):
    calc = parent_calc
    for old, new in [('id="nights" value="14"', 'id="nights" value="%d"' % p["nights"]),
                     ('<option value="cold" selected>', '<option value="cold">'),
                     ('<option value="%s">' % p["climate"], '<option value="%s" selected>' % p["climate"]),
                     ('<option value="city" selected>', '<option value="city">'),
                     ('<option value="%s">' % p["style"], '<option value="%s" selected>' % p["style"]),
                     ('<option value="yes" selected>', '<option value="yes">'),
                     ('<option value="%s">' % ("yes" if p["laundry"] else "no"),
                      '<option value="%s" selected>' % ("yes" if p["laundry"] else "no")),
                     ('<option value="checked" selected>', '<option value="checked">'),
                     ('<option value="%s">' % ("carry" if p["carry"] else "checked"),
                      '<option value="%s" selected>' % ("carry" if p["carry"] else "checked"))]:
        assert calc.count(old) == 1, old
        calc = calc.replace(old, new)
    groups = packing_groups(p["nights"], p["climate"], p["style"], p["laundry"], p["carry"])
    listing = "".join('<div><h4>' + g + '</h4><ul>' + "".join('<li>' + i + '</li>' for i in items) + '</ul></div>'
                      for g, items in groups)
    total = sum(len(items) for _, items in groups)
    sub = "%d nights, %s weather, %s%s" % (p["nights"], CLIMATES[p["climate"]][0],
                                           "laundry available" if p["laundry"] else "no laundry",
                                           ", carry-on only." if p["carry"] else ".")
    empty = ('<div class="big" id="out">&mdash;</div><div class="sub" id="outsub"></div>\n'
             '<div class="plist" id="list"></div>')
    assert calc.count(empty) == 1
    return calc.replace(empty, '<div class="big" id="out">%d items to pack</div><div class="sub" id="outsub">%s</div>\n'
                               '<div class="plist" id="list">%s</div>' % (total, sub, listing))


def packing_pages(parent, japan_cost):
    js = parent["calc_js"]
    for _, (label, layers) in CLIMATES.items():
        assert "label:'" + label + "'" in js and all("'" + x + "'" in js for x in layers)
    assert all("'" + x + "'" in js for items in TRIP_STYLES.values() for x in items)
    assert [p["slug"] for p in PACKING_PRESETS] == list(content_guides.PRESETS)
    items = [(p["slug"], p["chip"]) for p in PACKING_PRESETS]
    parent["chips"] = chips("Presets", parent["slug"], items, None)
    parent["extra_css"] = parent.get("extra_css", "") + CHIP_CSS
    japan_cost["see_also"] = ('<p>Packing for Japan? There are ready-made lists for <a href="/tools/' + parent["slug"] +
                              '/japan-winter/">December to February</a> and for <a href="/tools/' + parent["slug"] +
                              '/japan-spring/">cherry blossom season</a>.</p>\n')
    pages = []
    for p in PACKING_PRESETS:
        c = content_guides.PRESETS[p["slug"]]
        explainer = sections(c["explainer"]) + (
            '\n<p>Working out the budget too? The <a href="/tools/' + JAPAN_COST + '/">Japan trip cost calculator</a> '
            'gives a line-by-line estimate for the same trip.</p>')
        campaign = "packing_list_" + p["slug"].replace("-", "_")
        pages.append(item_page(
            parent, p["slug"], tab_title=p["title"] + " | " + BRAND, og_title=p["title"], h1=p["h1"], lede=c["lede"],
            meta_desc=p["meta"], calc_html=packing_calc(parent["calc_html"], p), explainer=explainer, faqs=c["faqs"],
            chips=chips("Presets", parent["slug"], items, p["slug"]), chip_label=p["chip"],
            app_block=app_line("6797601401", "com.eritech.travelbinder", campaign, PACKING_LINE), campaign=campaign))
    return pages


def build(pages_by_slug, species, plant_calc, styles, drink_window_calc):
    _, data = gen_pairings.load()
    return {
        "By plant": plant_pages(pages_by_slug[PLANT_PARENT], species, plant_calc),
        "By style": wine_pages(pages_by_slug[WINE_PARENT], styles, drink_window_calc, data["families"]),
        "Presets": packing_pages(pages_by_slug[PACKING_PARENT], pages_by_slug[JAPAN_COST]),
    }


def check(page, html_text):
    url = DOMAIN + "/tools/" + page["slug"] + "/"
    problems = []
    title = re.search(r"<title>(.*?)</title>", html_text).group(1)
    h1 = re.search(r"<h1>(.*?)</h1>", html_text).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', html_text).group(1)
    if '<link rel="canonical" href="' + url + '">' not in html_text:
        problems.append("canonical")
    if not plain_text(title).startswith(plain_text(h1)):
        problems.append("title does not start with the H1")
    if len(html.unescape(desc)) > 155:
        problems.append("description %d chars" % len(html.unescape(desc)))
    if "ct=calc_" + page["campaign"] not in html_text or "utm_campaign%3D" + page["campaign"] not in html_text:
        problems.append("store tags")
    if '"@type": "FAQPage"' not in html_text:
        problems.append("FAQ schema")
    if html_text.count("<script>") != 1:
        problems.append("inline scripts")
    if html_text.count('aria-current="page"') != 1:
        problems.append("selected chip")
    if "@@" in html_text:
        problems.append("unfilled placeholder")
    if problems:
        raise SystemExit("gen_items: " + page["slug"] + ": " + ", ".join(problems))
