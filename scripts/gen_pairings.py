#!/usr/bin/env python3
"""Wine Pairing Finder pages, built from Cellar Book's wine_pairings.json at the commit pinned in data/pairings.lock."""
import base64
import html
import json
import os
import re
import subprocess

from brand import (REPO, DOMAIN, CF_SNIPPET, PALETTES, BRAND, ORG_REF, jsonld_script, breadcrumb,
                   play_badge, ios_badge, og_image)

SOURCE_REPO = "erincerol/cellar-book"
SOURCE_PATH = "ios/Modules/ReferenceData/Sources/ReferenceData/Resources/wine_pairings.json"
LOCK = os.path.join(REPO, "data", "pairings.lock")
GENERATED = os.path.join(REPO, "data", "pairings.generated.json")
GENERATED_REF = os.path.join(REPO, "data", "pairings.generated.ref")

SLUG = "wine-pairing"
TITLE = "Wine Pairing Finder"
SUBLINE = "Pick what's for dinner — the wines that sit well with it."
INDEX_H1 = "What wine goes with tonight's dinner?"
SHEET_TITLE = "Pair with a dish"
APP_LINE = ('This is the same filter <strong><a href="/apps/cellar-book/">Cellar Book</a></strong>&rsquo;s '
            'Tonight screen uses to pick from what you already own.')
WINE_TYPES = ["Red", "White", "Rosé", "Sparkling", "Dessert", "Fortified"]
OG_KICKER = TITLE + "  ·  eritech.studio/tools"

INDEX_EXPLAINER = (
    "How wine and food fit together",
    "Matching wine to food is less about rules than about four things you can taste: weight, acidity, tannin "
    "and sweetness. Weight comes first. Light dishes want light wines and rich dishes want fuller ones, so that "
    "neither drowns the other. Acidity is the great refresher; a wine with good acidity cuts through fat and "
    "salt and stands up to sharp sauces, which is why tomato-based pasta and bright Italian reds get on so well. "
    "Tannin, the drying grip in young red wine, softens against protein and fat, which is why it belongs with red "
    "meat and quarrels with delicate fish, lean white meat and chilli heat. Sweetness in the wine tames spice and "
    "balances salt, and with pudding it has to outweigh the sweetness on the plate. Pick what&rsquo;s for dinner "
    "above and you will see the wine types and grapes that sit well with it, grouped the way Cellar Book groups "
    "them when it suggests a bottle from your own rack. None of this is a test. A pairing that follows every rule "
    "can still be dull, and a bottle you love will usually be good with whatever you are eating; treat the "
    "suggestions here as a place to start, not a verdict.")

EXPLAINERS = {
    "red-meat": (
        "Red meat is rich with fat and protein, and that is exactly what tannin is for. The grip you feel on your "
        "gums from a young Cabernet Sauvignon, a Malbec or a Tannat comes from compounds that bind to protein; meet "
        "them with a steak and they latch onto the meat instead, so the wine tastes rounder and the beef tastes "
        "cleaner. Fat works the other way, coating the mouth so the next sip feels softer than the last. That is why "
        "the list here leans dark and structured: Syrah with its pepper, Nebbiolo and Aglianico with their firm "
        "tannin, a left-bank Bordeaux with some age. Weight matters as much as grip. A charred rib or a slow braise "
        "has real flavour, and a light red simply disappears beside it, so you want a wine that holds its own on "
        "the palate. Acidity earns its place too, particularly with tomato-based ragùs or anything finished with a "
        "pan sauce, which is where Sangiovese and Tempranillo come in. Softer choices such as Merlot or Grenache suit "
        "leaner cuts and gentler cooking, where the meat has less fat to tame the tannin. The one thing to steer away "
        "from is a big, oaky red with a lean, well-done cut; with nothing to soften it, the tannin turns drying and "
        "faintly bitter. Rarer meat, more fat and a heavier hand with the seasoning all call for more structure in "
        "the glass."),
    "lamb": (
        "Lamb has a sweetness and a gentle gaminess that young, fiercely tannic reds can trample, which is why the "
        "pick here is a red with some years on it. Time in bottle softens tannin and draws out savoury, leathery and "
        "dried-herb notes, and those meet lamb&rsquo;s own flavour halfway. A Rioja that has spent years in barrel "
        "and bottle is the classic match for a roast leg with rosemary, and a mature left-bank Bordeaux does much the "
        "same for a rack. Lamb is fattier than it looks, though, especially shoulder and chops, so there is still "
        "room for structure: Syrah, Mourvedre and Grenache from the south of France, Xinomavro and Agiorgitiko from "
        "Greece, or Okuzgozu and Bogazkere from Anatolia, where lamb is the everyday meat and the local reds grew up "
        "beside it. Herbs and garlic push lamb towards wines with a savoury, scrubby edge rather than lush fruit. "
        "Spiced dishes such as a tagine or kofta suit a warm, generous Grenache or a Châteauneuf-du-Pape, whose "
        "ripeness meets the spice without fighting it. Slow-cooked shoulder, falling apart after hours in the oven, "
        "wants less tannin than a pink-roasted rack; the meat is already soft, so the wine can be too. If all you "
        "have is a young, firm red, open it an hour or two ahead and let the air do some of the work the years would "
        "have done."),
    "game": (
        "Game tastes of where it lived. Venison, pheasant, grouse, pigeon and wild duck carry earthy, iron-rich and "
        "sometimes slightly high flavours that make bright, fruit-forward wine taste simple and sweet beside them. "
        "What works is something savoury with a little age: a wine that has moved past primary fruit into forest "
        "floor, mushroom, leather and dried cherry, so that it echoes the meat rather than shouting over it. Pinot "
        "Noir is the natural partner for feathered game, and a red Burgundy or a Côte de Nuits with some depth is "
        "about as good as it gets with roast partridge or duck. Nebbiolo does the same job with more structure; a "
        "Barolo or Barbaresco given air before dinner has the tannin for venison and the tar-and-roses perfume for "
        "a rich game pie. Most game is lean, so tannin has little fat to soften it, which is why age matters: "
        "mellowed tannin will not dry the meat out. Furred game and slow braises can take darker wines such as "
        "Syrah from Côte-Rôtie, Mourvedre or a Priorat, especially when juniper, red wine or berries are in the "
        "sauce. Sweet accompaniments such as redcurrant jelly nudge you towards riper fruit, perhaps a Sonoma Pinot. "
        "Whatever you choose, keep the oak quiet; heavy new oak masks exactly the savoury notes that make the "
        "pairing work."),
    "poultry": (
        "Chicken, turkey and duck are among the most accommodating things you can put on a plate, which is why the "
        "list for poultry is long and runs from whites to light reds. The meat itself is mild; what decides the "
        "wine is the cooking and the sauce. A simple roast chicken wants a white with body, a white Burgundy, a "
        "Chenin Blanc from Vouvray or a waxy Semillon, because its weight matches the crisp skin and the juices "
        "without overpowering the flesh. Cream and butter sauces push you further that way, and a full Viognier, "
        "Marsanne or Roussanne holds up beautifully. Go the other direction, with mushrooms, bacon or a red wine "
        "sauce, and a soft red makes more sense: Pinot Noir, a Beaujolais served lightly chilled, or a Cabernet "
        "Franc from Chinon. Duck is richer and fattier than other birds and can carry more, a red Burgundy or a "
        "supple Merlot, while fruit sauces such as orange or cherry favour a red with bright acidity. Turkey at "
        "Christmas, surrounded by stuffing, sprouts and cranberry, is a case for Pinot Noir or a juicy, low-tannin "
        "Zweigelt. Spice-rubbed or barbecued chicken suits an off-dry Riesling or a cold rosé. The thing to avoid is "
        "heavy tannin; lean white meat has little fat to soften it, and a big young red will make the bird taste "
        "dry."),
    "pork": (
        "Pork sits between white meat and red, and it pairs that way: a red without too much tannin, or a rich "
        "white. The meat is sweet and fairly fatty, especially belly and shoulder, so wines with good acidity cut "
        "through it and keep each mouthful fresh. Heavy tannin is unnecessary and can taste harsh against that "
        "sweetness, which is why the reds on this list are the soft and juicy ones: Pinot Noir, Gamay, Barbera, "
        "Dolcetto, Zweigelt and Blaufrankisch. A roast loin with crackling suits a Beaujolais or a Chinon; a "
        "slow-cooked shoulder with smoky, sticky flavours can take a riper Zinfandel or Pinotage. On the white side, "
        "pork&rsquo;s natural partner is fruit, apple and pear above all, and whites that taste of the orchard with "
        "good acidity feel made for it: Chenin Blanc from Vouvray, a Riesling from the Mosel or Alsace, or a "
        "peppery Gruner Veltliner. Pork in cream and mustard wants something fuller, Chardonnay or Viognier. "
        "Sausages and charcuterie lean towards Italian reds such as Barbera or Montepulciano, whose acidity cuts the "
        "salt and fat. Chinese and Southeast Asian pork dishes, sticky and sweet with a touch of chilli, are where an "
        "off-dry Riesling or a Gewurztraminer shines, the sweetness in the glass matching the glaze. A dry rosé is "
        "an easy bridge for anything that comes off the grill."),
    "fish": (
        "Fish is delicate and often lean, and the old rule of white wine with fish holds for good reasons. Tannin in "
        "red wine can react with fish oils and leave a metallic taste, while acidity does what a squeeze of lemon "
        "does: it lifts the flavour and freshens the palate. So the default is a dry white with freshness, and the "
        "list here is mostly that: Sauvignon Blanc from Sancerre or Marlborough, Albarino from Rías Baixas, Chablis, "
        "Assyrtiko, Vermentino, Gruner Veltliner. Match the weight of the wine to the fish and its sauce. Sole, "
        "plaice and other white fish simply cooked want something light and crisp; a meaty fillet of turbot, hake "
        "or cod in a butter sauce can take a rounder white Burgundy or a Chenin Blanc from Vouvray. Oily fish such "
        "as mackerel, sardines and salmon carry more flavour and fat, and they are where light, low-tannin reds "
        "become possible: Pinot Noir, a pale Etna red from Sicily, Mencia, Cinsault or a lightly chilled Chinon. "
        "Smoked fish suits an aromatic or off-dry white, Riesling being the obvious choice, and a cold, dry sherry "
        "is an underrated partner for anything fried. Champagne and other sparkling wines cut through batter and fat "
        "with ease, and a cold, pale rosé from Provence works wherever you would otherwise reach for a crisp white."),
    "shellfish": (
        "Shellfish tastes of the sea, and the wines that suit it best taste as though they were made within sight of "
        "it: a crisp white with salt in it. Oysters, mussels, clams, prawns and crab are sweet, briny and delicate, "
        "so you want high acidity, little or no oak and a mineral, almost saline edge. Muscadet is the classic with "
        "oysters, bone-dry and briny after resting on its lees. Albarino from Rías Baixas, Assyrtiko from Santorini, "
        "Vermentino and Vinho Verde come from coastlines too, and that salinity shows in the glass. Chablis, lean "
        "and stony, is the textbook choice for a seafood platter. Sauvignon Blanc from Sancerre or Marlborough suits "
        "shellfish with herbs, garlic or a sharp dressing. Richer preparations change the picture. Lobster, scallops "
        "seared in butter or crab in a creamy sauce want more body, a white Burgundy, a Semillon or a perfumed "
        "Viognier, while a dry, cold sherry is a remarkable match for prawns and anything fried in batter. Sparkling "
        "wine works across the board because its bubbles and acidity scrub the palate clean between mouthfuls; "
        "Champagne with oysters is a cliché because it is right. Red wine is the one thing to keep away, since "
        "tannin and the iodine in shellfish together taste of metal."),
    "pasta-rice": (
        "Pasta and rice dishes are mostly about the sauce, and the wines that suit them best are something Italian "
        "and easy-going. Italian reds grew up alongside tomato, olive oil and hard cheese, so they tend to have high "
        "acidity and moderate tannin, which is exactly what a tomato sauce needs. Tomato is sharp; a wine with less "
        "acidity than the sauce will taste flat and flabby beside it. Sangiovese, whether a Chianti or something "
        "simpler, is the default for a ragù or a pizza, Barbera does the same with softer tannin, and Dolcetto and "
        "Montepulciano are relaxed, everyday reds that never get in the way. Richer dishes such as lasagne, a slow "
        "beef ragù or a mushroom risotto can take more structure: Nebbiolo from Barolo or Barbaresco, or a "
        "Valpolicella. Cream, butter and seafood change the colour of the glass. Carbonara, spaghetti with clams, "
        "seafood risotto and pasta with pesto all suit a crisp Italian white, Pinot Grigio, Vermentino, Trebbiano "
        "or Garganega, the grape behind Soave. Rice dishes from around the Mediterranean follow the same logic, with "
        "Bobal, Xinomavro, Agiorgitiko and Okuzgozu playing the part the Italian reds play at home. Keep it simple; "
        "this is a family that rewards a wine you can drink by the glass rather than one you have to think about."),
    "spicy": (
        "Chilli heat changes the rules. Capsaicin makes alcohol burn hotter and tannin taste harsher, so a big, "
        "oaky, high-alcohol red with a curry can feel like pouring fuel on a fire. Sweetness does the opposite: it "
        "calms the heat and lets the flavours of the dish come through. That is why the pick here is a white with a "
        "touch of sweetness, and why Riesling, especially an off-dry Mosel with its low alcohol and bright acidity, "
        "is the classic match for Thai, Sichuan and Indian food. Gewurztraminer brings lychee, rose and ginger that "
        "meet aromatic spices on their own terms, and Torrontes, Muscat, Viognier and Malvasia have the perfume to "
        "stand up to lemongrass, coriander and lime. Acidity matters as much as sugar; it keeps the wine refreshing "
        "against rich coconut sauces. Not everything spicy is hot, though. Smoky, barbecued and warmly spiced "
        "dishes, from chilli con carne to harissa lamb, often want a red, and there the trick is ripe fruit and soft "
        "tannin: Grenache, a Châteauneuf-du-Pape, Zinfandel, Malbec, Carmenere or Pinotage. A Barossa Shiraz suits "
        "smoky, sweet-spiced barbecue. Serve reds slightly cool and keep the alcohol modest where you can. The "
        "hotter the dish, the more the glass should lean towards sweetness, freshness and fruit."),
    "vegetables": (
        "Vegetables are harder to match than meat because they vary so much: bitter greens, sweet roots, earthy "
        "mushrooms, tangy tomatoes. The common thread is freshness, which is why the pick is a bright white or a "
        "light red. Green vegetables, asparagus, peas, courgettes and soft herbs above all, share flavour compounds "
        "with Sauvignon Blanc, and a Sancerre or a Marlborough Sauvignon picks up those green notes rather than "
        "clashing with them. Gruner Veltliner, with its white-pepper edge, is one of the few wines that handles "
        "asparagus and artichoke gracefully. Salads dressed with vinaigrette need high acidity in the wine, or the "
        "dressing will make it taste flat; Albarino, Assyrtiko, Verdejo and Vinho Verde are all sharp enough. "
        "Roasted and grilled vegetables develop sweetness and char, and they welcome a light red: a Beaujolais, a "
        "Chinon with its leafy edge, Barbera or Cinsault, served a little cool. Mushrooms, lentils and earthier "
        "dishes can take a warmer Grenache. A dry Provence rosé suits a table of mezze, ratatouille or grilled "
        "peppers. Vegetable dishes heavy with cheese or cream follow the cheese or the cream rather than the "
        "vegetable. What rarely works is heavy tannin or heavy oak; with no protein or fat to soften them, both "
        "taste coarse."),
    "cheese": (
        "Cheese and wine are an old partnership, but they are trickier together than tradition suggests. Strong "
        "cheese coats the palate with fat and salt and can flatten a delicate wine, while a big, tannic red can "
        "taste metallic against a creamy rind. The rule of thumb here is a wine with more age than the cheese: "
        "young, fresh cheeses suit young, fresh wines, and mature, nutty cheeses suit wines that have developed "
        "savoury depth of their own. A fresh goat&rsquo;s cheese with a Sancerre is the classic case, the acidity in "
        "the wine matching the tang of the cheese. Soft, bloomy cheeses such as Brie welcome Champagne, whose "
        "bubbles cut through the richness, or a light Beaujolais. Hard, aged cheeses, Comté, Parmesan or a mature "
        "Cheddar, stand up to structured reds with some years on them: a Rioja, a Barolo, a Brunello from "
        "Montalcino, a mature Bordeaux. Blue cheese is where sweetness comes in, and the old pairings exist for a "
        "reason: Sauternes with Roquefort, Port with Stilton, the sugar balancing the salt and the intensity "
        "matching the intensity. A Tokaji Aszú, a PX or a Madeira does a similar job. Washed-rind cheeses, pungent "
        "and sticky, are easiest with an aromatic white such as Gewurztraminer. On a mixed board, a dry sherry or a "
        "sparkling wine is the most forgiving companion."),
    "dessert": (
        "The most important rule in dessert pairing is also the simplest: the wine should be something sweeter than "
        "the pudding. If the dessert is sweeter than the wine, the wine tastes thin, sour and oddly bitter; if the "
        "wine is sweeter, it tastes rich and balanced, and the dessert seems lighter. That is why the list here is "
        "short and made up entirely of sweet and fortified wines. Sauternes and Tokaji Aszú, both made from grapes "
        "concentrated by noble rot, have the honeyed richness and the bright acidity to suit fruit tarts, crème "
        "brûlée and anything with apricot or almond. Sweet Muscat, floral and grapey, is lovely with fruit puddings "
        "and lighter, creamy desserts. Chocolate is the hardest thing to pair, because it is bitter and coats the "
        "mouth, and it needs a wine with real power: a Port from the Douro, a dark, sticky fortified Muscat or a "
        "Madeira. Sticky toffee pudding, Christmas pudding and anything with dried fruit or caramel meet their match "
        "in Pedro Ximenez, black and syrupy; some people pour it straight over vanilla ice cream, and it works. "
        "Serve sweet wines cold and in small glasses. Their intensity means a little goes a long way, and a single "
        "bottle can see a table of six through pudding."),
}

EXTRA_CSS = """.sheet .sheet-title{font-size:1.1rem;margin:0 0 14px}
.chips{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:8px}
.chips a,.chips a:visited{display:inline-flex;align-items:center;min-height:44px;padding:0 14px;border:1px solid var(--line);border-radius:16px;color:var(--text);text-decoration:none;font-size:.92rem}
.chips a:hover{border-color:var(--accent)}
.chips a[aria-current=page],.chips a[aria-current=page]:visited{background:var(--line);border-color:var(--accent);color:var(--accent)}
.answer{margin-top:22px;padding-top:18px;border-top:1px solid var(--line)}
.answer .opening{color:var(--muted);font-size:.92rem;margin:0 0 2px}
.answer .whisper{font-family:Georgia,"Times New Roman",serif;font-style:italic;font-size:1.65rem;line-height:1.3;margin:0 0 6px}
.answer .prompt{color:var(--muted);margin:0}
.wines h3{font-size:.78rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:600;margin:20px 0 4px}
.wines ul{list-style:none;padding:0;margin:0}
.wines li{padding:6px 0;border-bottom:1px solid var(--line)}
.wines li:last-child{border-bottom:none}
.wines .w{font-family:Georgia,"Times New Roman",serif;font-style:italic;color:var(--muted);font-size:.95rem;margin-left:4px}
.wines .type-w{font-family:Georgia,"Times New Roman",serif;font-style:italic;color:var(--muted);margin:0 0 4px}
.wines ul.regions{margin-top:2px}
.wines ul.regions li{border:none;padding:2px 0 0 14px;font-size:.92rem}
"""

SWITCH_JS = """(function(){
if(!window.fetch||!window.DOMParser||!history.pushState)return;
var cache={};
var swapped=['link[rel=canonical]','meta[name=description]','meta[property="og:title"]','meta[property="og:description"]','meta[property="og:url"]','meta[property="og:image"]','script[type="application/ld+json"]'];
function chip(e){return e.target.closest?e.target.closest('.chips a'):null}
function get(u){
return cache[u]||(cache[u]=fetch(u).then(function(r){if(!r.ok)throw new Error(r.status);return r.text()})
.catch(function(err){delete cache[u];throw err}))}
function swap(doc){
document.title=doc.title;
swapped.forEach(function(sel){var a=document.head.querySelector(sel),b=doc.head.querySelector(sel);if(a&&b)a.replaceWith(b)});
document.querySelector('.crumb').replaceWith(doc.querySelector('.crumb'));
document.querySelector('main').replaceWith(doc.querySelector('main'))}
function go(u,push){
get(u).then(function(t){
swap(new DOMParser().parseFromString(t,'text/html'));
if(!push)return;
history.pushState(null,'',u);
var c=document.querySelector('.chips a[href="'+new URL(u).pathname+'"]');
if(c)c.focus({preventScroll:true})})
.catch(function(){location.href=u})}
document.addEventListener('click',function(e){
var a=chip(e);
if(!a||e.defaultPrevented||e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;
e.preventDefault();
if(a.href!==location.href)go(a.href,true)});
['pointerover','pointerdown'].forEach(function(t){document.addEventListener(t,function(e){var a=chip(e);if(a)get(a.href)})});
window.addEventListener('popstate',function(){go(location.href,false)});
})();"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>@@TAB_TITLE@@</title>
<meta name="description" content="@@META_DESC@@">
<link rel="canonical" href="@@URL@@">
<meta property="og:type" content="website">
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
@@CSS@@@@EXTRA_CSS@@</style>
@@JSONLD@@
</head>
<body>
<nav class="crumb"><a href="/">@@BRAND@@</a><span>/</span><a href="/tools/">Free tools</a>@@CRUMB@@</nav>
<main>
<header>
<h1>@@H1@@</h1>
</header>
<section class="calc sheet" aria-labelledby="sheet-title">
<h2 class="sheet-title" id="sheet-title">@@SHEET_TITLE@@</h2>
<ul class="chips">
@@CHIPS@@
</ul>
<div class="answer">
@@ANSWER@@
</div>
</section>
<section class="explainer">
<h2>@@EXPLAINER_TITLE@@</h2>
<p>@@EXPLAINER@@</p>
</section>
<section class="app-block">
@@APP_BLOCK@@
</section>
<section class="more-tools">
@@RELATED@@
</section>
</main>
<footer>
<p>&copy; 2026 @@BRAND@@ &middot; <a href="mailto:admin@eritech.studio">admin@eritech.studio</a></p>
<p>Google Play and the Google Play logo are trademarks of Google LLC. Apple and the Apple logo are trademarks of Apple Inc.</p>
</footer>
<script>
@@SWITCH_JS@@
</script>
</body>
</html>
"""


def text(s):
    return html.escape(s, quote=False)


def attr(s):
    return html.escape(s, quote=False).replace('"', "&quot;")


def page_url(fid=None):
    return DOMAIN + "/tools/" + SLUG + "/" + (fid + "/" if fid else "")


def load():
    with open(LOCK) as f:
        ref = f.read().strip()
    if not re.fullmatch(r"[0-9a-f]{40}", ref):
        raise SystemExit("data/pairings.lock must hold one full Cellar Book commit hash, got: " + repr(ref))
    cached = os.path.exists(GENERATED) and os.path.exists(GENERATED_REF) and open(GENERATED_REF).read().strip() == ref
    if not cached:
        api = "repos/" + SOURCE_REPO + "/contents/" + SOURCE_PATH + "?ref=" + ref
        res = subprocess.run(["gh", "api", api, "--jq", ".content"], capture_output=True, text=True)
        if res.returncode != 0:
            raise SystemExit("gh api could not fetch wine_pairings.json at " + ref + ":\n" + res.stderr)
        raw = base64.b64decode(res.stdout)
        json.loads(raw)
        with open(GENERATED, "wb") as f:
            f.write(raw)
        with open(GENERATED_REF, "w") as f:
            f.write(ref + "\n")
    with open(GENERATED, encoding="utf-8") as f:
        return ref, json.load(f)


def validate(data):
    ids = [f["id"] for f in data["families"]]
    if set(ids) != set(EXPLAINERS) or len(ids) != len(EXPLAINERS):
        raise SystemExit("Families in wine_pairings.json do not match the explainers in gen_pairings.py.\n"
                         "JSON: " + ", ".join(ids) + "\nExplainers: " + ", ".join(EXPLAINERS))
    for row in data["rows"]:
        unknown = set(row["fam"]) - set(ids)
        if unknown:
            raise SystemExit("Row " + json.dumps(row, ensure_ascii=False) + " names unknown families " + str(unknown))
        if row["t"] is not None and row["t"] not in range(len(WINE_TYPES)):
            raise SystemExit("Row " + json.dumps(row, ensure_ascii=False) + " has an unknown wine type")
        if row["t"] is None and not row["g"]:
            raise SystemExit("Row " + json.dumps(row, ensure_ascii=False) + " has neither a type nor a grape")
        if row["t"] is None and not any(r["g"] == row["g"] and not r["r"] and r["t"] is not None for r in data["rows"]):
            raise SystemExit("Row " + json.dumps(row, ensure_ascii=False) + " has no type and no grape row to sit under")


def grape_type(grape, fid, rows):
    bases = [r for r in rows if r["g"] == grape and not r["r"] and r["t"] is not None]
    carrying = [r for r in bases if fid in r["fam"]]
    return min(r["t"] for r in (carrying or bases))


def wines_for(fid, rows):
    groups = [{"why": None, "grapes": {}, "regions": []} for _ in WINE_TYPES]
    for row in rows:
        if fid not in row["fam"]:
            continue
        group = groups[row["t"] if row["t"] is not None else grape_type(row["g"], fid, rows)]
        if not row["g"]:
            if row["r"]:
                group["regions"].append(row)
            else:
                group["why"] = row["why"]
            continue
        grape = group["grapes"].setdefault(row["g"], {"why": None, "regions": []})
        if row["r"]:
            grape["regions"].append(row)
        else:
            grape["why"] = row["why"]
    return [(WINE_TYPES[t], g) for t, g in enumerate(groups) if g["why"] or g["grapes"] or g["regions"]]


def whisper(why):
    return ' <span class="w">' + text(why) + '</span>' if why else ""


def region_list(regions):
    if not regions:
        return ""
    return ('<ul class="regions">\n' + "\n".join(
        '<li>' + text(r["r"] + (" · " + r["g"] if r["g"] else "")) + whisper(r["why"]) + '</li>'
        for r in regions) + '\n</ul>')


def wines_html(fid, rows):
    out = '<div class="wines">\n'
    for label, g in wines_for(fid, rows):
        out += '<h3>' + text(label) + '</h3>\n'
        if g["why"]:
            out += '<p class="type-w">' + text(g["why"]) + '</p>\n'
        items = ['<li><strong>' + text(name) + '</strong>' + whisper(gr["why"]) + region_list(gr["regions"]) + '</li>'
                 for name, gr in g["grapes"].items()]
        items += ['<li><strong>' + text(r["r"]) + '</strong>' + whisper(r["why"]) + '</li>' for r in g["regions"]]
        if items:
            out += '<ul>\n' + "\n".join(items) + '\n</ul>\n'
    return out + '</div>'


def chips_html(families, current):
    return "\n".join(
        '<li><a href="/tools/' + SLUG + '/' + f["id"] + '/"' +
        (' aria-current="page"' if f["id"] == current else '') + '>' + text(f["label"]) + '</a></li>'
        for f in families)


def dish(family):
    return family["label"].lower().replace("&", "and")


def app_block(campaign):
    return ('<p>' + APP_LINE + '</p>\n<div class="badges">' + ios_badge("6796370046", campaign) +
            play_badge("com.eritech.cellarbook", campaign) + '</div>')


def render(shared_css, pal, *, url, tab_title, og_title, meta_desc, og, crumb, h1, chips, answer,
           explainer_title, explainer, campaign, related, jsonld):
    page = TEMPLATE
    for k, v in [
        ("@@CSS@@", shared_css), ("@@EXTRA_CSS@@", EXTRA_CSS),
        ("@@BG@@", pal["bg"]), ("@@SURFACE@@", pal["surface"]), ("@@TEXT@@", pal["text"]),
        ("@@MUTED@@", pal["muted"]), ("@@ACCENT@@", pal["accent"]), ("@@LINE@@", pal["line"]), ("@@ON@@", pal["on"]),
        ("@@TAB_TITLE@@", attr(tab_title)), ("@@META_DESC@@", attr(meta_desc)), ("@@OG_TITLE@@", attr(og_title)),
        ("@@URL@@", url), ("@@OG@@", og), ("@@CF@@", CF_SNIPPET), ("@@JSONLD@@", jsonld),
        ("@@CRUMB@@", crumb), ("@@H1@@", text(h1)), ("@@SHEET_TITLE@@", SHEET_TITLE), ("@@CHIPS@@", chips),
        ("@@ANSWER@@", answer), ("@@EXPLAINER_TITLE@@", explainer_title), ("@@EXPLAINER@@", explainer),
        ("@@APP_BLOCK@@", app_block(campaign)), ("@@RELATED@@", related),
        ("@@DOMAIN@@", DOMAIN), ("@@BRAND@@", BRAND), ("@@SWITCH_JS@@", SWITCH_JS),
    ]:
        page = page.replace(k, v)
    out = os.path.join(REPO, url[len(DOMAIN) + 1:], "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    print("wrote " + os.path.relpath(out, REPO))


def build(shared_css, related_html):
    ref, data = load()
    validate(data)
    families, rows = data["families"], data["rows"]
    pal = PALETTES["cellar"]
    index_url = page_url()

    index_list = ('<h2>Every dish, one page each</h2>\n<ul class="cluster">\n' + "\n".join(
        '<li><a href="/tools/' + SLUG + '/' + f["id"] + '/">' + text(f["label"]) + '</a><span class="d">' +
        text(f["why"]) + '</span></li>' for f in families) + '\n</ul>\n')
    render(shared_css, pal, url=index_url, tab_title=TITLE + " | " + BRAND, og_title=INDEX_H1,
           meta_desc="Pick what's for dinner and see the wine types and grapes that sit well with it, "
                     "from red meat to pudding. Free, no signup.",
           og=SLUG, crumb="", h1=INDEX_H1, chips=chips_html(families, None),
           answer='<p class="prompt">' + text(SUBLINE) + '</p>',
           explainer_title=INDEX_EXPLAINER[0], explainer=INDEX_EXPLAINER[1], campaign="wine_pairing",
           related=index_list + related_html,
           jsonld=jsonld_script({"@context": "https://schema.org", "@graph": [
               breadcrumb((BRAND, DOMAIN + "/"), ("Free tools", DOMAIN + "/tools/"), (TITLE, index_url)),
               {"@type": "WebApplication", "@id": index_url, "name": TITLE, "url": index_url,
                "description": SUBLINE, "applicationCategory": "LifestyleApplication", "operatingSystem": "Any",
                "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "GBP"},
                "publisher": ORG_REF}]}))
    og_image(SLUG + ".png", TITLE, pal, kicker="Free tool  ·  eritech.studio/tools", sub=SUBLINE)

    for f in families:
        url = page_url(f["id"])
        h1 = "What wine goes with " + dish(f) + "?"
        meta = f["opening"] + ", " + f["why"] + ". The wine types and grapes that suit " + dish(f) + ", and why they work."
        render(shared_css, pal, url=url, tab_title=h1 + " | " + BRAND, og_title=h1, meta_desc=meta,
               og=SLUG + "-" + f["id"],
               crumb='<span>/</span><a href="/tools/' + SLUG + '/">' + TITLE + '</a>', h1=h1,
               chips=chips_html(families, f["id"]),
               answer=('<p class="opening">' + text(f["opening"]) + '</p>\n<p class="whisper">' + text(f["why"]) +
                       '</p>\n' + wines_html(f["id"], rows)),
               explainer_title="Why these wines work with " + text(dish(f)), explainer=EXPLAINERS[f["id"]],
               campaign="wine_pairing_" + f["id"], related=related_html,
               jsonld=jsonld_script({"@context": "https://schema.org", "@graph": [
                   breadcrumb((BRAND, DOMAIN + "/"), ("Free tools", DOMAIN + "/tools/"), (TITLE, index_url),
                              (f["label"], url)),
                   {"@type": "WebPage", "name": h1, "url": url, "description": meta,
                    "isPartOf": {"@id": index_url}, "publisher": ORG_REF}]}))
        og_image(SLUG + "-" + f["id"] + ".png", f["label"], pal, kicker=OG_KICKER, sub=f["why"])

    check(families)
    print("wine pairing pages built from " + SOURCE_REPO + "@" + ref)
    return [index_url] + [page_url(f["id"]) for f in families]


def check(families):
    def read(fid=None):
        with open(os.path.join(REPO, "tools", SLUG, *( [fid] if fid else []), "index.html"), encoding="utf-8") as f:
            return f.read()

    def fail(msg):
        raise SystemExit("wine pairing check failed: " + msg)

    for fid, body in [(None, INDEX_EXPLAINER[1])] + list(EXPLAINERS.items()):
        words = len(html.unescape(body).split())
        if not 150 <= words <= 300 or "!" in body:
            fail((fid or "index") + " explainer has " + str(words) + " words or an exclamation mark")

    expected_chips = ['/tools/' + SLUG + '/' + f["id"] + '/' for f in families]
    index = read()
    index_chips = index.split('<ul class="chips">')[1].split('</ul>')[0]
    if re.findall(r'<li><a href="([^"]+)"', index_chips) != expected_chips:
        fail("index chips")
    if 'aria-current' in index_chips:
        fail("index has a selected chip")
    for href in expected_chips:
        if index.count('href="' + href + '"') < 2:
            fail("index does not list " + href)
    if 'ct=calc_wine_pairing&' not in index or 'utm_campaign%3Dwine_pairing"' not in index:
        fail("index store tags")

    for f in families:
        page = read(f["id"])
        url = page_url(f["id"])
        h1 = re.search(r"<h1>(.*?)</h1>", page).group(1)
        if h1 != "What wine goes with " + text(dish(f)) + "?":
            fail(f["id"] + " h1 " + h1)
        if '<link rel="canonical" href="' + url + '">' not in page or '<meta property="og:url" content="' + url + '">' not in page:
            fail(f["id"] + " canonical")
        headline = re.search(r'<p class="whisper">(.*?)</p>', page).group(1)
        if html.unescape(headline) != f["why"]:
            fail(f["id"] + " headline is not the family's why")
        chips = page.split('<ul class="chips">')[1].split('</ul>')[0]
        if re.findall(r'<li><a href="([^"]+)"', chips) != expected_chips:
            fail(f["id"] + " chip hrefs")
        if re.findall(r'href="([^"]+)" aria-current="page"', chips) != [expected_chips[[x["id"] for x in families].index(f["id"])]]:
            fail(f["id"] + " selected chip")
        if ('ct=calc_wine_pairing_' + f["id"] + '&') not in page or ('utm_campaign%3Dwine_pairing_' + f["id"] + '"') not in page:
            fail(f["id"] + " store tags")
        desc = re.search(r'<meta name="description" content="([^"]*)"', page).group(1)
        if len(html.unescape(desc)) >= 155:
            fail(f["id"] + " meta description is " + str(len(desc)) + " characters")
        if '<meta property="og:image" content="' + DOMAIN + '/assets/og/' + SLUG + '-' + f["id"] + '.png">' not in page:
            fail(f["id"] + " og:image")
        if page.count("<script>") != 1 or SWITCH_JS not in page:
            fail(f["id"] + " is missing the chip switcher or carries another inline script")
