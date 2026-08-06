#!/usr/bin/env python3
"""Generate eritech.studio /apps/<slug>/ landing pages.

Each page is both an app landing page (ASO support — it captures "<thing> app"
searches and funnels them to the stores with tagged links) and a topic hub for
that app's subject, linking out to the free calculators on the same theme.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import (REPO, DOMAIN, CF_SNIPPET, PALETTES, APPS,
                   play_badge, ios_badge, og_image)

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>@@TAB_TITLE@@</title>
<meta name="description" content="@@META_DESC@@">
<link rel="canonical" href="@@DOMAIN@@/apps/@@SLUG@@/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Eri Tech Studio">
<meta property="og:title" content="@@NAME@@">
<meta property="og:description" content="@@META_DESC@@">
<meta property="og:url" content="@@DOMAIN@@/apps/@@SLUG@@/">
<meta property="og:image" content="@@DOMAIN@@/assets/og/app-@@SLUG@@.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="apple-itunes-app" content="app-id=@@APPID@@, app-argument=@@DOMAIN@@/apps/@@SLUG@@/">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
@@CF@@
<style>
:root{--bg:@@BG@@;--surface:@@SURFACE@@;--text:@@TEXT@@;--muted:@@MUTED@@;--accent:@@ACCENT@@;--line:@@LINE@@;--on-accent:@@ON@@}
*{box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--text);margin:0;line-height:1.6}
main{max-width:680px;margin:0 auto;padding:0 20px 40px}
.crumb{max-width:680px;margin:0 auto;padding:18px 20px;font-size:.9rem;color:var(--muted)}
.crumb a,.crumb a:visited{color:var(--muted);text-decoration:underline;text-underline-offset:2px;text-decoration-thickness:1px}
.crumb a:hover{color:var(--accent)}
.crumb span{margin:0 8px}
h1{font-family:Georgia,"Times New Roman",serif;font-size:2.1rem;line-height:1.2;margin:10px 0 6px}
.lede{color:var(--muted);margin:0 0 26px;font-size:1.05rem}
h2{font-family:Georgia,"Times New Roman",serif;font-size:1.3rem;margin:34px 0 10px}
p{margin:0 0 14px}
a,a:visited{color:var(--accent);text-decoration:underline;text-underline-offset:2px;text-decoration-thickness:1px}
.badges{display:flex;align-items:center;gap:6px;flex-wrap:wrap;margin:0 0 8px}
.badges a img{display:block}
.badge-appstore img{height:52px}
.badge-play img{height:78px;margin:-13px}
.feat{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:20px 24px;margin:26px 0}
.feat ul{margin:0;padding-left:20px}
.feat li{margin-bottom:9px}
.feat li:last-child{margin-bottom:0}
.tools{list-style:none;padding:0;margin:0}
.tools li{margin-bottom:9px}
.tools a{display:block;padding:12px 16px;background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:10px;text-decoration:none}
.tools a:hover{border-color:var(--accent)}
.tools strong{display:block;color:var(--text)}
.tools span{font-size:.9rem;color:var(--muted)}
.note{font-size:.88rem;color:var(--muted)}
footer{max-width:680px;margin:30px auto 0;padding:20px;border-top:1px solid var(--line);color:var(--muted);font-size:.85rem}
footer a,footer a:visited{color:var(--muted);text-decoration:underline;text-underline-offset:2px}
</style>
<script type="application/ld+json">
{"@context":"https://schema.org","@graph":[
{"@type":"SoftwareApplication","name":"@@NAME@@","applicationCategory":"LifestyleApplication",
 "operatingSystem":"iOS, Android","description":"@@META_DESC@@",
 "url":"@@DOMAIN@@/apps/@@SLUG@@/",
 "publisher":{"@type":"Organization","name":"Eri Tech Studio","url":"@@DOMAIN@@/"},
 "sameAs":["https://apps.apple.com/app/id@@APPID@@","https://play.google.com/store/apps/details?id=@@PKG@@"]},
{"@type":"BreadcrumbList","itemListElement":[
{"@type":"ListItem","position":1,"name":"Eri Tech Studio","item":"@@DOMAIN@@/"},
{"@type":"ListItem","position":2,"name":"Apps","item":"@@DOMAIN@@/apps/"},
{"@type":"ListItem","position":3,"name":"@@NAME@@","item":"@@DOMAIN@@/apps/@@SLUG@@/"}]}]}
</script>
</head>
<body>
<nav class="crumb"><a href="/">Eri Tech Studio</a><span>/</span><a href="/apps/">Apps</a></nav>
<main>
<h1>@@H1@@</h1>
<p class="lede">@@LEDE@@</p>
<div class="badges">@@BADGES@@</div>
<p class="note">Free to download &middot; one-time unlock &middot; no subscription</p>
@@INTRO@@
<div class="feat">
<h2 style="margin-top:0">What it does</h2>
<ul>
@@FEATURES@@
</ul>
</div>
@@BODY@@
<h2>Free tools on this theme</h2>
<ul class="tools">
@@TOOLS@@
</ul>
<h2>Privacy</h2>
<p>@@NAME@@ stores everything on your device. There is no account, no server and no cloud sync, and nothing you enter is transmitted anywhere. Read the full <a href="/privacy-policies/@@PRIVACY@@">privacy policy</a>.</p>
</main>
<footer>
<p><a href="/">Eri Tech Studio</a> &middot; <a href="/apps/">All apps</a> &middot; <a href="/tools/">Free tools</a> &middot; <a href="mailto:admin@eritech.studio">admin@eritech.studio</a></p>
<p>Google Play and the Google Play logo are trademarks of Google LLC. Apple and the Apple logo are trademarks of Apple Inc.</p>
</footer>
</body>
</html>
"""

TOOL_META = {
    "sourdough-hydration-calculator": ("Sourdough Hydration Calculator", "Flour, water and starter in — true hydration % out."),
    "bakers-percentage-calculator": ("Baker's Percentage Calculator", "Scale any bread formula from flour or dough weight."),
    "starter-feeding-ratio-calculator": ("Starter Feeding Ratio Calculator", "1:1:1, 1:2:2, 1:5:5 — feed amounts and peak times."),
    "dough-temperature-calculator": ("Dough Temperature Calculator", "Hit a target dough temperature via the water."),
    "wine-cellar-value-calculator": ("Wine Cellar Value Calculator", "Count by tier — total, average, replacement figure."),
    "coffee-ratio-calculator": ("Coffee Ratio Calculator", "Coffee-to-water ratios for every brew method."),
    "espresso-ratio-calculator": ("Espresso Ratio Calculator", "Dose, yield, ratio — enter any two, solve the third."),
    "coffee-freshness-calculator": ("Coffee Freshness Calculator", "Roast date in, peak drinking window out."),
    "wine-drink-window-calculator": ("Wine Drink Window Calculator", "Style and vintage in — ageing, ready, or fading."),
    "plant-watering-calculator": ("Plant Watering Calculator", "Watering intervals by species, season and light."),
    "uk-return-rights-checker": ("UK Return Rights Checker", "Which legal return or refund window you're in."),
    "packing-list-generator": ("Packing List Generator", "Trip length and climate in — a list with quantities."),
    "japan-trip-cost-calculator": ("Japan Trip Cost Calculator", "Nights and style in — a line-by-line budget."),
}

CONTENT = {
"kohii": dict(
    h1="Kohii &mdash; the barista log",
    tab="Kohii — Coffee & Espresso Journal App | Eri Tech Studio",
    lede="A brew journal for people who dial in. Espresso, pour-over, AeroPress, moka and cold brew, all logged offline.",
    desc="Kohii is an offline coffee journal for espresso and pour-over. Log dose, yield, time and grind, rate every cup, and track bean freshness from the roast date. No account, one-time unlock.",
    features=["Log dose, yield, time, grind and a live brew ratio for every cup",
              "Every method — espresso, V60, Chemex, AeroPress, moka, French press, cold brew",
              "Rate acidity, bitterness, sweetness and body, then one-tap &ldquo;Brew Again&rdquo; your best shot",
              "Track beans by roaster, origin and roast date, with freshness worked out for you",
              "Fully offline, no account, one-time unlock"],
    intro="<p>Most coffee notes live in three different places at once &mdash; a note on your phone, a photo of a bag, and whatever you can remember about the grind setting you were on last week. Kohii exists because a dial-in only converges if you can see what you changed last time.</p>",
    body="""<h2>Why logging a brew changes the coffee</h2>
<p>Dialling in is a search problem. Three variables move the cup &mdash; the ratio of coffee to water, the grind, and the contact time &mdash; and each one pulls the others around. Change two at once and you learn nothing, because you cannot attribute the result. Change one, write down what you did, and taste: that is the whole method, and it works far faster than any amount of reading.</p>
<p>The awkward part is that it depends on remembering yesterday. A shot that ran sour at 18&nbsp;g in and 36&nbsp;g out over 22 seconds tells you to grind finer, but only if you can recall those numbers exactly. That is the entire reason a brew log exists, and why a bag of expensive coffee is often wasted on rediscovering something you had already worked out a fortnight earlier.</p>
<h2>Freshness is a variable too</h2>
<p>The other thing a log surfaces is that beans move under you. Coffee needs to rest after roasting &mdash; roughly ten days for espresso, less for filter &mdash; and it then holds a peak for a few weeks before the aromatics fade. A recipe that was perfect on day fourteen will taste flat on day fifty, and if you are not tracking the roast date it looks like your technique regressed. It did not; the coffee got older. Kohii tracks that from the roast date, and there is a free <a href="/tools/coffee-freshness-calculator/">coffee freshness calculator</a> here if you just want to check a bag.</p>
<h2>Offline, because a kitchen is not a spreadsheet</h2>
<p>Everything lives on your phone. No account to make, no sync to fail, nothing to lose when a service shuts down &mdash; and it works fine in a cafe basement with no signal.</p>"""),

"the-bake-log": dict(
    h1="The Bake Log &mdash; sourdough, tracked",
    tab="The Bake Log — Sourdough Starter & Baking Tracker App | Eri Tech Studio",
    lede="A baking journal for sourdough. Starter feedings that actually remind you, guided bakes, and a record of every loaf.",
    desc="The Bake Log is an offline sourdough app for tracking starters, feeding reminders, hydration, fermentation times and finished bakes. No account, one-time unlock.",
    features=["Feeding reminders that fire even when the phone is locked or has rebooted",
              "Multiple starters, each with its own schedule and feeding history",
              "Guided bakes that walk a whole day — autolyse, coil folds, bulk fermentation, shaping",
              "Log hydration, flour blend, timings and crumb against every recipe",
              "Fully offline, no account, one-time unlock"],
    intro="<p>Sourdough runs on timing, and timing runs on memory. The Bake Log was built because a starter peaks whether or not you are paying attention, and a loaf you cannot reconstruct is a loaf you cannot repeat.</p>",
    body="""<h2>The starter is a schedule, not an ingredient</h2>
<p>A sourdough starter is a living culture on a clock. Feed it and it climbs, peaks, and falls, and the window where it is ripe enough to raise bread but not yet exhausted is a matter of hours &mdash; hours that shift with the feeding ratio and the temperature of your kitchen. Feed at 1:1:1 and it may peak in four; feed at 1:5:5 and it might take twelve. Neither is more correct, but using the wrong one for the day you have planned is why bakes fail for reasons that feel mysterious.</p>
<p>That is a reminder problem more than a baking problem, which is why feeding alerts are the core of the app rather than a feature bolted on. Work out your own ratios with the free <a href="/tools/starter-feeding-ratio-calculator/">starter feeding ratio calculator</a>.</p>
<h2>Hydration explains more failures than technique</h2>
<p>The second thing worth writing down is hydration &mdash; the water in a dough as a percentage of the flour. It is the number that decides whether a dough is firm and forgiving or slack and open, and it is also the number most often quoted wrongly, because a starter is itself flour and water and has to be counted. Two bakers following the same recipe can end up several points apart for exactly that reason. There is a free <a href="/tools/sourdough-hydration-calculator/">sourdough hydration calculator</a> that folds the starter in, and a <a href="/tools/bakers-percentage-calculator/">baker's percentage calculator</a> for scaling a formula to the tin you actually own.</p>
<h2>A record you can actually repeat</h2>
<p>The point of logging a bake is the loaf after next. Flour brand, hydration, room temperature, bulk time, how the crumb came out &mdash; kept together, those turn a good result into a repeatable one, and a bad one into information. It all stays on your device, offline, with no account.</p>"""),

"warranty-box": dict(
    h1="Warranty Box &mdash; receipts and warranties, kept",
    tab="Warranty Box — Warranty & Receipt Tracker App | Eri Tech Studio",
    lede="Every receipt, warranty and return deadline in one place, with a reminder before the window closes.",
    desc="Warranty Box is an offline warranty and receipt tracker. Store proof of purchase, log serial numbers and get reminded before a return window or warranty expires. No account, one-time unlock.",
    features=["Store receipts and product photos as proof of purchase",
              "Log serial numbers, retailers, purchase dates and prices",
              "Reminders before a return window or warranty period expires",
              "Group items by expiry so you can see what lapses next",
              "Fully offline, no account, one-time unlock"],
    intro="<p>The moment you need a receipt is always months after you filed it somewhere sensible. Warranty Box exists because consumer rights are worth very little if you cannot prove when and where you bought the thing.</p>",
    body="""<h2>Your rights depend on paperwork you no longer have</h2>
<p>In the UK, the Consumer Rights Act 2015 gives you thirty days to reject a faulty item outright, and up to six years to pursue a remedy &mdash; with the burden of proof sitting on the retailer for the first six months. That is a genuinely strong position, and almost all of it rests on being able to evidence the purchase date and the seller. A faded till receipt in a drawer is the difference between a refund and a shrug.</p>
<p>Separately, buying online gives you fourteen days to change your mind under the Consumer Contracts Regulations &mdash; a right that does not exist for anything you bought in a shop, where returns are entirely the retailer's own policy. The two get conflated constantly. There is a free <a href="/tools/uk-return-rights-checker/">UK return rights checker</a> here that tells you which window a purchase is actually in.</p>
<h2>The deadline is the part that gets missed</h2>
<p>Almost nobody forgets that an appliance has a warranty. What they miss is that it ended last month. Return windows are measured in days and warranties in years, so both fail the same way &mdash; silently, with no prompt. Reminders before the window closes are the entire value, which is why the app schedules them per item.</p>
<h2>Nothing leaves the device</h2>
<p>Receipts carry your name, your card's last digits and where you shop. That is exactly the sort of thing that should not sit on someone else's server, so it does not: everything is stored locally, with no account and no sync.</p>"""),

"cellar-book": dict(
    h1="Cellar Book &mdash; a private wine ledger",
    tab="Cellar Book — Wine Cellar & Collection Tracker App | Eri Tech Studio",
    lede="What you own, what it is worth waiting for, and what is ready tonight.",
    desc="Cellar Book is an offline wine cellar app for tracking your collection, drink windows and tasting notes, with label photos and an offline map of your regions. No account, one-time unlock.",
    features=["Track every bottle with vintage, producer, region and quantity",
              "Drink windows, so you can see what is ageing, ready or fading",
              "Label photos instead of a spreadsheet of names you will not recognise",
              "Tasting notes on the 100-point scale, kept per bottle",
              "An offline atlas of the regions your collection comes from",
              "Fully offline, no account, one-time unlock"],
    intro="<p>A cellar is only an asset if you drink it at the right time. Cellar Book exists because the difference between a great bottle and an expensive disappointment is usually five years, not money.</p>",
    body="""<h2>The drink window is the whole problem</h2>
<p>Wine built for ageing follows an arc: tight and unforgiving when young, open and layered through the middle, then slowly drying out. The stretch in the middle &mdash; the drink window &mdash; is where the bottle repays what you paid for it. Miss the front of it and you waste the wine on tannin; miss the back and you are drinking the memory of fruit.</p>
<p>Structure sets that window. Tannin, acidity and sugar are preservatives, which is why a Barolo can improve for two decades while most supermarket reds are best within a year of release, and why vintage Port is barely awake at fifteen years. Producer and vintage move it further. There is a free <a href="/tools/wine-drink-window-calculator/">wine drink window calculator</a> here that gives a sensible range for a style and year.</p>
<h2>A collection outgrows memory faster than you expect</h2>
<p>Thirty bottles is roughly where a cellar stops being something you can hold in your head. After that you are guessing about what is in the back of the rack, buying duplicates of things you already have, and pulling the wrong bottle on the night it matters. A label photo solves recognition far better than a typed name, because that is how you actually remember wine.</p>
<h2>Yours alone</h2>
<p>What you own and what you paid is nobody else's business. Cellar Book keeps all of it on your device &mdash; no account, no cloud, no marketplace quietly learning your buying habits.</p>"""),

"leaflet": dict(
    h1="Leaflet &mdash; plant care that remembers",
    tab="Leaflet — Plant Care, Watering Reminder & Journal App | Eri Tech Studio",
    lede="Watering and feeding schedules that actually remind you, and a photo timeline showing a year of growth in one scroll.",
    desc="Leaflet is an offline plant care app with watering reminders, feeding schedules and a growth photo timeline for every houseplant. No AI identification, no subscription, no account.",
    features=["Watering and feeding schedules per plant, with reminders that fire",
              "A photo timeline per plant — a year of growth in one scroll",
              "Care history, repotting dates and adoption dates kept per plant",
              "A needs-care-today view so nothing gets quietly forgotten",
              "No AI identification and no subscription — fully offline"],
    intro="<p>Houseplants rarely die of neglect in one dramatic moment. They die of a schedule that drifted. Leaflet is a care journal for people who already know what their plants are and want to keep them alive.</p>",
    body="""<h2>&ldquo;Water once a week&rdquo; kills more plants than forgetting</h2>
<p>It is the most repeated houseplant advice and the least useful, because thirst is not a property of the plant alone. It depends on light, on how warm and dry the room is, on pot size and material, and on whether the plant is growing or dormant. The same Monstera might want water every six days in a bright July window and every three weeks in a dim December corner. A fixed weekly schedule is therefore wrong for most of the year, and it is wrong in the dangerous direction &mdash; toward soil that never dries.</p>
<p>Overwatering is what actually does the damage. Most houseplants tolerate going too dry: they droop, you water, they recover. Constantly wet soil suffocates roots and invites rot, which is usually fatal by the time it is visible above the surface. There is a free <a href="/tools/plant-watering-calculator/">plant watering calculator</a> here that gives a starting interval by species, season and light &mdash; a starting point to check against the soil, not a rule.</p>
<h2>Growth is invisible day to day</h2>
<p>The other thing a journal gives you is proof that anything is happening. Plants move too slowly to notice, so a difficult year of adjusting light and watering can feel like no progress at all &mdash; until you put two photos side by side eleven months apart. That is also, in practice, the most shared thing anyone does with a plant app.</p>
<h2>No AI, deliberately</h2>
<p>Leaflet does not identify plants from a photo. It is built for people who already know what they own and want a record rather than a guess, which is also why there is no subscription and nothing to log into.</p>"""),

"travel-binder": dict(
    h1="The Travel Binder &mdash; the whole trip, offline",
    tab="The Travel Binder — Offline Trip Planner & Itinerary App | Eri Tech Studio",
    lede="Flights, hotels, bookings, documents, packing and a map of the whole trip. Works in airplane mode, in a country with no signal.",
    desc="The Travel Binder is a fully offline trip planner. Flights, hotels, bookings, documents, packing lists and checklists in one binder, with exports to PDF, Markdown, JSON and CSV. No account, no cloud.",
    features=["Every booking in one timeline — flights, trains, hotels, restaurants, activities",
              "A wishlist of places you can promote onto a day when you decide to go",
              "Packing lists and checklists with reminders before you travel",
              "Passports, insurance and rail passes kept in a document pocket",
              "Exports to PDF, Markdown, JSON and CSV — your plans are never locked in",
              "No account, no cloud, works in airplane mode"],
    intro="<p>The moment you most need your itinerary is the moment you have no signal, no roaming and four percent battery. The Travel Binder was built out of a real trip run from a hand-made file of notes, and it assumes the network will not be there.</p>",
    body="""<h2>Offline is the feature, not a fallback</h2>
<p>Travel apps tend to treat connectivity as a given and offline as a degraded mode &mdash; and several put offline access behind a subscription, which is a strange thing to charge for at the exact moment the app is least able to help you. Landing in a new country is reliably the worst-connected hour of any trip: no local SIM yet, airport wifi behind a captive portal, and a queue where somebody wants to see your booking. Everything here is stored on the device, so the binder opens the same whether or not anything is reachable.</p>
<h2>Planning and travelling are two different jobs</h2>
<p>Before a trip you are collecting &mdash; a restaurant somebody mentioned, a shop worth the detour, a museum that needs booking a month ahead. That is a wishlist, not an itinerary, and forcing it onto a calendar too early is why plans feel brittle. Keeping candidates separate until you commit them to a day matches how people actually plan. Then, on the ground, you want the opposite: one day at a time, next thing highlighted.</p>
<h2>Your plans should outlive the app</h2>
<p>Exports run to PDF for printing, and Markdown, JSON and CSV for anything else &mdash; so an itinerary can move into Obsidian, Notion or a spreadsheet without being retyped. Two free tools here work whether or not you use the app: a <a href="/tools/packing-list-generator/">packing list generator</a> that sizes quantities to the trip, and a <a href="/tools/japan-trip-cost-calculator/">Japan trip cost calculator</a> for budgeting.</p>"""),
}

# ---------------------------------------------------------------- build

os.makedirs(os.path.join(REPO, "apps"), exist_ok=True)

for app in APPS:
    c = CONTENT[app["slug"]]
    pal = PALETTES[app["palette"]]
    badges = (ios_badge(app["app_id"], app["slug"].replace("-", "_"), prefix="app") +
              play_badge(app["pkg"], app["slug"].replace("-", "_"), medium="app_page"))
    feats = "\n".join("<li>%s</li>" % f for f in c["features"])
    tools = "\n".join(
        '<li><a href="/tools/%s/"><strong>%s</strong><span>%s</span></a></li>' % (t, TOOL_META[t][0], TOOL_META[t][1])
        for t in app["tools"])

    html = TEMPLATE
    for k, v in [("@@TAB_TITLE@@", c["tab"]), ("@@META_DESC@@", c["desc"]), ("@@NAME@@", app["name"]),
                 ("@@SLUG@@", app["slug"]), ("@@DOMAIN@@", DOMAIN), ("@@CF@@", CF_SNIPPET),
                 ("@@APPID@@", app["app_id"]), ("@@PKG@@", app["pkg"]), ("@@PRIVACY@@", app["privacy"]),
                 ("@@BG@@", pal["bg"]), ("@@SURFACE@@", pal["surface"]), ("@@TEXT@@", pal["text"]),
                 ("@@MUTED@@", pal["muted"]), ("@@ACCENT@@", pal["accent"]), ("@@LINE@@", pal["line"]),
                 ("@@ON@@", pal["on"]), ("@@H1@@", c["h1"]), ("@@LEDE@@", c["lede"]),
                 ("@@BADGES@@", badges), ("@@INTRO@@", c["intro"]), ("@@FEATURES@@", feats),
                 ("@@BODY@@", c["body"]), ("@@TOOLS@@", tools)]:
        html = html.replace(k, v)

    d = os.path.join(REPO, "apps", app["slug"])
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w").write(html)
    print("wrote apps/%s/index.html" % app["slug"])
    og_image("app-%s.png" % app["slug"], app["name"], pal, kicker="eritech.studio")

# ---------------------------------------------------------------- /apps/ index

rows = "\n".join(
    '<li><a href="/apps/%s/"><strong>%s</strong><span>%s</span></a></li>' % (
        a["slug"], a["name"], CONTENT[a["slug"]]["lede"]) for a in APPS)

index = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Our Apps &mdash; Private, Offline Logbooks | Eri Tech Studio</title>
<meta name="description" content="Six fully offline apps for iOS and Android — coffee, sourdough, warranties, wine, plants and travel. No account, no cloud, one-time purchase.">
<link rel="canonical" href="@@DOMAIN@@/apps/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Eri Tech Studio">
<meta property="og:title" content="Our Apps — Eri Tech Studio">
<meta property="og:description" content="Six fully offline logbook apps for iOS and Android. No account, no cloud, one-time purchase.">
<meta property="og:url" content="@@DOMAIN@@/apps/">
<meta property="og:image" content="@@DOMAIN@@/assets/brand/og-default.png">
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
li a,li a:visited{display:block;padding:14px 18px;background:#FFFDFA;border:1px solid #E9E3D9;border-left:4px solid #7A3B24;border-radius:10px;text-decoration:none;color:#3B342C}
li a:hover{border-color:#7A3B24;box-shadow:0 3px 14px rgba(60,45,30,.08)}
li a strong{display:block;color:#1F1A15;font-size:1.05rem;font-family:Georgia,serif}
li a span{font-size:.92rem;color:#6F6857}
footer{margin-top:44px;padding-top:20px;border-top:1px solid #E9E3D9;color:#6F6857;font-size:.85rem}
footer a,footer a:visited{color:#6F6857;text-decoration:underline;text-underline-offset:2px}
</style>
</head>
<body>
<nav class="crumb"><a href="/">Eri Tech Studio</a> / Apps</nav>
<h1>Our Apps</h1>
<p class="subtitle">Six private logbooks for things worth keeping a record of. All fully offline, all one-time purchases.</p>
<ul>
@@ROWS@@
</ul>
<footer>
<p><a href="/">Eri Tech Studio</a> &middot; <a href="/tools/">Free tools</a> &middot; <a href="mailto:admin@eritech.studio">admin@eritech.studio</a></p>
</footer>
</body>
</html>
"""
apps_itemlist = ('<script type="application/ld+json">\n'
    '{"@context":"https://schema.org","@type":"ItemList","name":"Eri Tech Studio apps","itemListElement":['
    + ",".join('{"@type":"ListItem","position":%d,"name":"%s","url":"%s/apps/%s/"}' % (i + 1, a["name"], DOMAIN, a["slug"])
               for i, a in enumerate(APPS)) + ']}\n</script>')
index = (index.replace("@@DOMAIN@@", DOMAIN).replace("@@CF@@", CF_SNIPPET)
         .replace("@@ROWS@@", rows).replace("@@ITEMLIST@@", apps_itemlist))
open(os.path.join(REPO, "apps", "index.html"), "w").write(index)
print("wrote apps/index.html")
