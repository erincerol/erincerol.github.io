#!/usr/bin/env python3
"""Generate eritech.studio /guides/: the guides index and one long-form page per entry in brand.GUIDES."""
import datetime
import html
import os
import re
import sys

from brand import (REPO, DOMAIN, CF_SNIPPET, PALETTES, APPS, BRAND, ORG_REF, SITE_LASTMOD, GUIDES, plain_text,
                   jsonld_script, breadcrumb, ios_badge, play_badge, og_image)
import content_guides
import content_returns

STALE_AFTER_DAYS = 180
APP_LINES = {
    "dial-in-espresso": ('<strong><a href="/apps/kohii/">Kohii</a></strong> logs every shot &mdash; dose, yield, time, '
                         'grind &mdash; so the next one starts from the last.'),
    "return-windows": ('<strong><a href="/apps/warranty-box/">Warranty Box</a></strong> reminds you before the window '
                       'closes &mdash; add the purchase and forget it.'),
}

GUIDE_CSS = """.guide h2{margin-top:38px}
.guide h3{font-family:Georgia,"Times New Roman",serif;font-size:1.05rem;margin:24px 0 6px}
.calc{margin:18px 0 8px}
.checked{font-size:.85rem;color:var(--muted);margin:-18px 0 26px}
.grid{width:100%;border-collapse:collapse;margin:6px 0 16px;font-size:.93rem}
.grid th{text-align:left;font-weight:600;font-size:.8rem;letter-spacing:.04em;text-transform:uppercase;color:var(--muted);padding:8px 10px 8px 0;border-bottom:1px solid var(--line)}
.grid td{padding:10px 10px 10px 0;border-bottom:1px solid var(--line);vertical-align:top}
.grid td:first-child{font-weight:600}
.grid td a+span{display:block;font-size:.8rem;color:var(--muted);white-space:nowrap}
.sources{font-size:.85rem;color:var(--muted)}
@media(max-width:600px){
.grid thead{display:none}
.grid,.grid tbody,.grid tr,.grid td{display:block;width:100%}
.grid tr{padding:10px 0;border-bottom:1px solid var(--line)}
.grid td{border:none;padding:3px 0}
.grid td[data-label]::before{content:attr(data-label) ": ";color:var(--muted);font-size:.85rem}
.grid td:first-child{font-size:1.02rem}
}
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>@@TAB_TITLE@@</title>
<meta name="description" content="@@META_DESC@@">
<link rel="canonical" href="@@URL@@">
<meta property="og:type" content="article">
<meta property="og:site_name" content="@@BRAND@@">
<meta property="og:title" content="@@OG_TITLE@@">
<meta property="og:description" content="@@META_DESC@@">
<meta property="og:url" content="@@URL@@">
<meta property="og:image" content="@@DOMAIN@@/assets/og/@@OG@@.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
@@CF@@
<style>
@@CSS@@@@GUIDE_CSS@@</style>
@@JSONLD@@
</head>
<body>
<nav class="crumb"><a href="/">@@BRAND@@</a><span>/</span><a href="/guides/">Guides</a></nav>
<main class="guide">
<header>
<h1>@@H1@@</h1>
<p class="lede">@@LEDE@@</p>
</header>
@@BODY@@
@@FAQ@@
<section class="app-block">
@@APP_BLOCK@@
</section>
<section class="more-tools">
<h2>Related</h2>
<ul class="cluster">
@@RELATED@@
</ul>
</section>
</main>
<footer>
<p><a href="/">@@BRAND@@</a> &middot; <a href="/apps/">Apps</a> &middot; <a href="/tools/">Free tools</a> &middot; <a href="/guides/">Guides</a> &middot; <a href="mailto:admin@eritech.studio">admin@eritech.studio</a></p>
<p>Google Play and the Google Play logo are trademarks of Google LLC. Apple and the Apple logo are trademarks of Apple Inc.</p>
</footer>
@@SCRIPT@@</body>
</html>
"""


def attr(s):
    return html.escape(html.unescape(s), quote=True)


def app_of(slug):
    return next(a for a in APPS if a["slug"] == slug)


def paragraphs(items):
    return "\n".join("<p>" + p + "</p>" for p in items)


def faq_html(faqs):
    return ('<section class="faq">\n<h2>Frequently asked questions</h2>\n' +
            "".join("<h3>" + q + "</h3>\n<p>" + a + "</p>\n" for q, a in faqs) + "</section>")


def table(head, rows, labels=None):
    out = '<table class="grid">\n<thead><tr>' + "".join("<th>" + h + "</th>" for h in head) + "</tr></thead>\n<tbody>\n"
    for row in rows:
        out += "<tr>" + "".join(
            ("<td>" if i == 0 or not labels else '<td data-label="' + labels[i] + '">') + cell + "</td>"
            for i, cell in enumerate(row)) + "</tr>\n"
    return out + "</tbody>\n</table>"


def espresso_body(calc_html):
    e = content_guides.ESPRESSO
    assert len(e["table"]) == 6 and len(e["rows"]) == 6 and len(e["faqs"]) == 4
    return "\n".join([
        "<h2>What the shot is telling you</h2>",
        table(["Symptom", "What to change", "Direction"], e["table"], ["Symptom", "Change", "Direction"]),
        "\n".join("<h3>" + h + "</h3>\n<p>" + p + "</p>" for h, p in e["rows"]),
        "<h2>Change one thing at a time</h2>",
        paragraphs(e["one_thing"]),
        "<h2>A worked example</h2>",
        "<p>" + e["worked_intro"] + "</p>",
        table(["Shot", "Recipe", "How it tasted", "Next change"], e["worked"], ["Shot", "Recipe", "Taste", "Next"]),
        "<p>" + e["worked_outro"] + "</p>",
        "<h2>Work out your own numbers</h2>",
        '<section class="calc" aria-label="Espresso ratio calculator">\n' + calc_html + "\n</section>",
        '<p class="note">The same calculator, with ristretto, normale and lungo ranges explained, is on the '
        '<a href="/tools/espresso-ratio-calculator/">espresso ratio calculator</a> page.</p>',
    ])


def long_date(iso):
    d = datetime.date.fromisoformat(iso)
    return "%d %s %d" % (d.day, d.strftime("%B"), d.year)


def short_date(iso):
    d = datetime.date.fromisoformat(iso)
    return "%d %s %d" % (d.day, d.strftime("%b"), d.year)


def retailer_rows(rows):
    for r in rows:
        assert r["url"].startswith("https://") and re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["checked"]), r["retailer"]
        condition = r["condition"] + ((" " + r["note"]) if r.get("note") else "")
        yield [r["retailer"], r["window"], r["holiday"] or "&mdash;", condition,
               '<a href="' + attr(r["url"]) + '" rel="nofollow noopener">Policy</a><span>checked ' +
               short_date(r["checked"]) + '</span>']


def warn_if_stale(rows):
    today = datetime.date.today()
    for r in rows:
        age = (today - datetime.date.fromisoformat(r["checked"])).days
        if age > STALE_AFTER_DAYS:
            print("WARNING: return-windows row %s was checked %d days ago (%s); re-check it." %
                  (r["retailer"], age, r["checked"]), file=sys.stderr)


def returns_body():
    c = content_returns
    rows = c.UK + c.US
    warn_if_stale(rows)
    last = max(r["checked"] for r in rows)
    head = ["Retailer", "Standard window", "Holiday window", "Condition", "Source"]
    labels = [None, "Standard", "Holiday", "Condition", "Source"]
    return "\n".join([
        '<p class="checked">Last checked ' + long_date(last) + '. Retailers change these, so follow the policy link '
        'before you rely on a figure.</p>',
        "<h2>Your legal baseline</h2>",
        "<h3>In the UK</h3>",
        "<p>" + c.UK_BASELINE + "</p>",
        '<p>The <a href="/tools/uk-return-rights-checker/">UK return rights checker</a> works out which of these '
        'windows you are in from the date you bought.</p>',
        "<h3>In the US</h3>",
        "<p>" + c.US_BASELINE + "</p>",
        '<p class="sources">Sources: ' + "; ".join('<a href="' + attr(u) + '" rel="nofollow noopener">' + l + '</a>'
                                                     for l, u in c.BASELINE_SOURCES) + '.</p>',
        "<h2>UK retailers</h2>",
        table(head, retailer_rows(c.UK), labels),
        "<h2>US retailers</h2>",
        table(head, retailer_rows(c.US), labels),
        '<p class="note">Each figure is the retailer&rsquo;s standard policy as published on the date shown. Many '
        'have exceptions for particular categories, marketplace sellers and personalised items; the policy page has '
        'the detail. Your legal rights apply on top of any shop policy.</p>',
    ])


GUIDE_CONTENT = {
    "dial-in-espresso": dict(lede=lambda: content_guides.ESPRESSO["lede"], faqs=lambda: content_guides.ESPRESSO["faqs"],
                             meta="Sour, bitter, thin or harsh: what each espresso taste means, which variable to "
                                  "change and in which direction, with a worked dial-in from 1:2 in 28 seconds."),
    "return-windows": dict(lede=lambda: content_returns.LEDE, faqs=lambda: content_returns.FAQS,
                           meta="Return windows for Apple, John Lewis, IKEA, M&S, Target, Best Buy, Costco and more, "
                                "with UK and US legal rights and each retailer’s own policy."),
}


def related(g, tool_titles, descs):
    app = app_of(g["app"])
    items = ['<li><a href="/apps/' + app["slug"] + '/">' + app["name"] + '</a><span class="d">The app this guide '
             'comes from.</span></li>']
    items += ['<li><a href="/tools/' + s + '/">' + tool_titles[s] + '</a><span class="d">' + descs[s] + '</span></li>'
              for s in g["tools"]]
    return "\n".join(items)


def page_jsonld(g, url, meta, faqs):
    return jsonld_script({"@context": "https://schema.org", "@graph": [
        breadcrumb((BRAND, DOMAIN + "/"), ("Guides", DOMAIN + "/guides/"), (plain_text(g["h1"]), url)),
        {"@type": "Article", "headline": plain_text(g["h1"]), "description": meta, "url": url,
         "mainEntityOfPage": url, "inLanguage": "en-GB", "datePublished": g["published"],
         "dateModified": SITE_LASTMOD, "author": ORG_REF, "publisher": ORG_REF,
         "image": DOMAIN + "/assets/og/guide-" + g["slug"] + ".png"},
        {"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": plain_text(q), "acceptedAnswer": {"@type": "Answer", "text": plain_text(a)}}
            for q, a in faqs]},
    ]})


def build_guide(g, shared_css, tool_titles, descs, espresso_html, espresso_js):
    app = app_of(g["app"])
    pal = PALETTES[app["palette"]]
    c = GUIDE_CONTENT[g["slug"]]
    url = DOMAIN + "/guides/" + g["slug"] + "/"
    faqs = c["faqs"]()
    if g["slug"] == "dial-in-espresso":
        body = espresso_body(espresso_html)
        script = ("<script>\n" + espresso_js + "\ndocument.querySelectorAll('.calc input,.calc select').forEach("
                  "function(el){el.addEventListener('input',calc);el.addEventListener('change',calc)});\ncalc();\n"
                  "</script>\n")
    else:
        body = returns_body()
        script = ""
    campaign = g["slug"].replace("-", "_")
    app_block = ('<p>' + APP_LINES[g["slug"]] + '</p>\n<div class="badges">' +
                 ios_badge(app["app_id"], campaign, prefix="guide") +
                 play_badge(app["pkg"], "guide_" + campaign, medium="guide") + '</div>')
    css = shared_css
    for k in ("BG", "SURFACE", "TEXT", "MUTED", "ACCENT", "LINE", "ON"):
        css = css.replace("@@" + k + "@@", pal[k.lower()])
    page = TEMPLATE
    for k, v in [("@@CSS@@", css), ("@@GUIDE_CSS@@", GUIDE_CSS), ("@@TAB_TITLE@@", tab_title(g)),
                 ("@@META_DESC@@", attr(c["meta"])), ("@@OG_TITLE@@", attr(g["h1"])), ("@@URL@@", url),
                 ("@@OG@@", "guide-" + g["slug"]), ("@@CF@@", CF_SNIPPET), ("@@BRAND@@", BRAND), ("@@DOMAIN@@", DOMAIN),
                 ("@@JSONLD@@", page_jsonld(g, url, c["meta"], faqs)), ("@@H1@@", g["h1"]), ("@@LEDE@@", c["lede"]()),
                 ("@@BODY@@", body), ("@@FAQ@@", faq_html(faqs)), ("@@APP_BLOCK@@", app_block),
                 ("@@RELATED@@", related(g, tool_titles, descs)), ("@@SCRIPT@@", script)]:
        page = page.replace(k, v)
    check(g, url, page, campaign, c["meta"])
    out = os.path.join(REPO, "guides", g["slug"])
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "index.html"), "w") as f:
        f.write(page)
    print("wrote guides/" + g["slug"] + "/index.html (%d words)" % words(body + faq_html(faqs) + c["lede"]()))
    og_image("guide-" + g["slug"] + ".png", plain_text(g["h1"]), pal, kicker="Guide  ·  eritech.studio/guides")
    return url


def words(fragment):
    return len(plain_text(fragment).split())


def tab_title(g):
    return html.escape(plain_text(g["h1"]) + " | " + BRAND, quote=False)


def check(g, url, page, campaign, meta):
    problems = []
    if '<link rel="canonical" href="' + url + '">' not in page:
        problems.append("canonical")
    if len(meta) > 155:
        problems.append("description %d chars" % len(meta))
    if "ct=guide_" + campaign not in page or "utm_campaign%3Dguide_" + campaign not in page:
        problems.append("store tags")
    if '"@type": "FAQPage"' not in page or "@@" in page:
        problems.append("schema or placeholder")
    if "<title>" + tab_title(g) + "</title>" not in page:
        problems.append("title")
    if problems:
        raise SystemExit("gen_guides: " + g["slug"] + ": " + ", ".join(problems))


INDEX = """<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Guides | Eritech Studios</title>
<meta name="description" content="Practical guides from the makers of Kohii, Warranty Box, Cellar Book and more: dialling in espresso, return windows by retailer, and moving your cellar.">
<link rel="canonical" href="@@DOMAIN@@/guides/">
<meta property="og:type" content="website">
<meta property="og:title" content="Guides — Eritech Studios">
<meta property="og:description" content="Practical guides on espresso, returns and wine cellars from the makers of our apps.">
<meta property="og:url" content="@@DOMAIN@@/guides/">
<meta property="og:image" content="@@DOMAIN@@/assets/og/guides.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
@@CF@@
@@ITEMLIST@@
<style>
*{box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.6;color:#3B342C;max-width:680px;margin:40px auto;padding:0 20px;background:#FAF7F2}
h1{font-family:Georgia,"Times New Roman",serif;font-size:2rem;color:#1F1A15;margin-bottom:5px}
.subtitle{color:#6F6857;margin-top:0;margin-bottom:32px}
.crumb{font-size:.9rem;color:#6F6857;margin-bottom:22px}
.crumb a,.crumb a:visited{color:#6F6857;text-decoration:underline;text-underline-offset:2px}
ul{list-style:none;padding:0;margin:0}
li{margin-bottom:11px}
li a,li a:visited{display:block;position:relative;padding:14px 40px 14px 18px;background:#FFFDFA;border:1px solid #E9E3D9;border-left:4px solid var(--acc,#7A3B24);border-radius:10px;text-decoration:none;color:#3B342C}
li a:hover{border-color:var(--acc,#7A3B24);box-shadow:0 3px 14px rgba(60,45,30,.08)}
li a::after{content:"";position:absolute;right:17px;top:50%;width:7px;height:7px;border-right:2px solid var(--acc,#7A3B24);border-bottom:2px solid var(--acc,#7A3B24);transform:translateY(-50%) rotate(-45deg);opacity:.55}
li a strong{display:block;color:#1F1A15;font-size:1.05rem;font-family:Georgia,serif}
li a span{display:block;font-size:.92rem;color:#6F6857}
li a em{display:block;font-style:normal;font-size:.8rem;color:#6F6857;margin-top:2px}
footer{margin-top:44px;padding-top:20px;border-top:1px solid #E9E3D9;color:#6F6857;font-size:.85rem}
footer a,footer a:visited{color:#6F6857;text-decoration:underline;text-underline-offset:2px}
</style>
</head>
<body>
<nav class="crumb"><a href="/">Eritech Studios</a> / Guides</nav>
<h1>Guides</h1>
<p class="subtitle">Longer reads from the apps we build: what to change, what the rules are, and how to move your records.</p>
<ul>
@@ROWS@@
</ul>
<footer>
<p><a href="/">Eritech Studios</a> &middot; <a href="/apps/">Apps</a> &middot; <a href="/tools/">Free tools</a> &middot; <a href="mailto:admin@eritech.studio">admin@eritech.studio</a></p>
</footer>
</body>
</html>
"""

APP_GUIDES = {
    ("cellar-book", "from-cellartracker"): ("Moving from CellarTracker to Cellar Book",
                                            "Bring your CellarTracker list across in one import, with a preview first."),
}


def build_index():
    entries = [(DOMAIN + "/guides/" + g["slug"] + "/", "/guides/" + g["slug"] + "/", plain_text(g["h1"]), g["h1"],
                g["blurb"], app_of(g["app"])) for g in GUIDES]
    for a in APPS:
        for sub in a.get("guides", []):
            title, blurb = APP_GUIDES[(a["slug"], sub)]
            path = "/apps/" + a["slug"] + "/" + sub + "/"
            entries.append((DOMAIN + path, path, title, title, blurb, a))
    rows = "\n".join('<li style="--acc:%s"><a href="%s"><strong>%s</strong><span>%s</span><em>From %s</em></a></li>'
                     % (a["web_accent"], path, h1, blurb, a["name"]) for _, path, _, h1, blurb, a in entries)
    itemlist = jsonld_script({"@context": "https://schema.org", "@type": "ItemList", "name": "Eritech Studios guides",
                              "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": name, "url": url}
                                                  for i, (url, _, name, _, _, _) in enumerate(entries)]})
    page = (INDEX.replace("@@DOMAIN@@", DOMAIN).replace("@@CF@@", CF_SNIPPET).replace("@@ITEMLIST@@", itemlist)
            .replace("@@ROWS@@", rows))
    os.makedirs(os.path.join(REPO, "guides"), exist_ok=True)
    with open(os.path.join(REPO, "guides", "index.html"), "w") as f:
        f.write(page)
    print("wrote guides/index.html")
    og_image("guides.png", "Guides", dict(bg="#FAF7F2", accent="#7A3B24", text="#1F1A15", muted="#998F83"),
             kicker="eritech.studio/guides")
    return DOMAIN + "/guides/"


def build(shared_css, tool_titles, descs, espresso_html, espresso_js):
    urls = [build_index()]
    urls += [build_guide(g, shared_css, tool_titles, descs, espresso_html, espresso_js) for g in GUIDES]
    return urls
