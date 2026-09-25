#!/usr/bin/env python3
"""Generate eritech.studio /tools/ calculator pages, OG images, robots.txt and sitemap.xml."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand import (REPO, DOMAIN, CF_SNIPPET, PALETTES, APPS, ACCENT_BY_APP,
                   BRAND, ORG_REF, SITE_LASTMOD, plain_text, jsonld_script, breadcrumb,
                   play_badge, ios_badge, og_image)

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>@@TAB_TITLE@@</title>
<meta name="description" content="@@META_DESC@@">
<link rel="canonical" href="@@DOMAIN@@/tools/@@SLUG@@/">
<meta property="og:type" content="website">
<meta property="og:title" content="@@OG_TITLE@@">
<meta property="og:description" content="@@META_DESC@@">
<meta property="og:url" content="@@DOMAIN@@/tools/@@SLUG@@/">
<meta property="og:image" content="@@DOMAIN@@/assets/og/@@SLUG@@.png">
<meta name="twitter:card" content="summary_large_image">
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
.crumb a,a:visited{color:var(--muted);text-decoration:none}
.crumb a:hover{color:var(--accent)}
.crumb span{margin:0 8px}
h1{font-family:Georgia,"Times New Roman",serif;font-size:2rem;line-height:1.25;margin:10px 0 6px}
.lede{color:var(--muted);margin:0 0 28px}
h2{font-family:Georgia,"Times New Roman",serif;font-size:1.3rem;margin:34px 0 10px}
p{margin:0 0 14px}
a,a:visited{color:var(--accent);text-decoration:underline;text-underline-offset:2px;text-decoration-thickness:1px}
.calc{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:22px;margin-bottom:8px}
.field{margin-bottom:14px}
.field label{display:block;font-size:.85rem;color:var(--muted);margin-bottom:5px}
input[type=number],input[type=date],select{width:100%;padding:11px 12px;font-size:1rem;border:1px solid var(--line);border-radius:9px;background:var(--bg);color:var(--text)}
.row{display:flex;gap:12px}
.row .field{flex:1}
.seg{display:flex;gap:8px;margin-bottom:16px;flex-wrap:wrap}
.seg button{flex:1;min-width:130px;padding:10px 12px;font-size:.9rem;border:1px solid var(--line);background:var(--bg);color:var(--muted);border-radius:9px;cursor:pointer}
.seg button.on{background:var(--accent);border-color:var(--accent);color:var(--on-accent);font-weight:600}
.result{margin-top:18px;padding:16px 18px;border-radius:10px;background:var(--bg);border:1px dashed var(--line)}
.result .big{font-family:Georgia,"Times New Roman",serif;font-size:1.9rem;line-height:1.25}
.result .sub{color:var(--muted);font-size:.92rem;margin-top:6px}
.result table{border-collapse:collapse;width:100%}
.result td{padding:5px 0;border-bottom:1px solid var(--line)}
.result tr:last-child td{border-bottom:none;font-weight:700}
.result td:last-child{text-align:right;font-variant-numeric:tabular-nums}
.note{font-size:.85rem;color:var(--muted);margin-top:12px;margin-bottom:0}
.app-block{margin-top:36px;padding:20px 22px;border:1px solid var(--line);border-radius:14px;background:var(--surface)}
.app-block p{margin:0 0 14px}
.badges{display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.badges a img{display:block}
.badge-appstore img{height:52px}
.badge-play img{height:78px;margin:-13px}
.badges .soon{display:inline-block;padding:10px 16px;border-radius:9px;border:1px solid var(--line);color:var(--muted);font-size:.92rem}
.more-tools ul{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:8px 18px}
@media(max-width:540px){.more-tools ul{grid-template-columns:1fr}.row{flex-direction:column;gap:0}}
.more-tools a,a:visited{text-decoration:none}
.more-tools a:hover{text-decoration:underline}
footer{max-width:680px;margin:30px auto 0;padding:20px;border-top:1px solid var(--line);color:var(--muted);font-size:.85rem}
footer a,a:visited{color:var(--muted)}
.faq h3{font-family:Georgia,"Times New Roman",serif;font-size:1.05rem;margin:22px 0 6px}
.worked td{padding:4px 0;border-bottom:1px solid var(--line)}
.worked{border-collapse:collapse;width:100%;margin:0 0 14px}
.worked td:last-child{text-align:right;font-variant-numeric:tabular-nums}
.more-tools ul.cluster{grid-template-columns:1fr;margin-bottom:6px}
.more-tools .d{display:block;color:var(--muted);font-size:.9rem}
@@EXTRA_CSS@@</style>
@@JSONLD@@
</head>
<body>
<nav class="crumb"><a href="/">@@BRAND@@</a><span>/</span><a href="/tools/">Free tools</a></nav>
<main>
<header>
<h1>@@H1@@</h1>
<p class="lede">@@LEDE@@</p>
</header>
<section class="calc" aria-label="Calculator">
@@CALC_HTML@@
</section>
@@EXPLAINER@@
@@DEPTH@@
@@FAQ@@
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
@@CALC_JS@@
document.querySelectorAll('.calc input,.calc select').forEach(function(el){el.addEventListener('input',calc);el.addEventListener('change',calc)});
calc();
</script>
</body>
</html>
"""

# ---------------------------------------------------------------- app blocks

def bakelog_block(campaign, built=True):
    return (("<p>This calculator is built into <strong><a href=\"/apps/the-bake-log/\">The Bake Log</a></strong>, along with " if built else "<p>A free web tool from the makers of <strong><a href=\"/apps/the-bake-log/\">The Bake Log</a></strong> &mdash; ") +
            'starter feeding reminders, guided bake timelines and a full bake journal. Offline, no account, free to start.</p>'
            '<div class="badges">' + ios_badge("6790971986", campaign) +
            play_badge("com.eritech.thebakelog", campaign) + '</div>')

def kohii_block(campaign, built=True):
    return (("<p>This calculator is built into <strong><a href=\"/apps/kohii/\">Kohii &mdash; The Barista Log</a></strong>, along with " if built else "<p>A free web tool from the makers of <strong><a href=\"/apps/kohii/\">Kohii &mdash; The Barista Log</a></strong> &mdash; ") +
            'brew logging, dial-in history and bean freshness tracking. Offline, no account.</p>'
            '<div class="badges">' + ios_badge("6790972283", campaign) +
            play_badge("com.eritech.kohii", campaign) + '</div>')

CELLAR_TONIGHT_SHELF_PPID = "5c62f941-daf9-4164-baa7-f7ab12a6df70"

def cellar_block(campaign, built=True, ppid=None):
    return (("<p>This calculator is built into <strong><a href=\"/apps/cellar-book/\">Cellar Book</a></strong>, which tracks " if built else "<p>A free web tool from the makers of <strong><a href=\"/apps/cellar-book/\">Cellar Book</a></strong>, which tracks ") +
            'drink windows on every bottle in your cellar — see what is ageing, ready or fading at a glance, with label photos, tasting '
            'notes on the 100-point scale and an offline map of your collection&rsquo;s regions.</p>'
            '<div class="badges">' + ios_badge("6796370046", campaign, ppid=ppid) +
            play_badge("com.eritech.cellarbook", campaign) + '</div>')

def leaflet_block(campaign, built=True):
    return (("<p>This calculator is built into <strong><a href=\"/apps/leaflet/\">Leaflet</a></strong>, which keeps " if built else "<p>A free web tool from the makers of <strong><a href=\"/apps/leaflet/\">Leaflet</a></strong>, which keeps ") +
            'watering and feeding schedules for every plant you own, with a photo timeline so you can watch a year of growth in one scroll. '
            'Offline, with no AI gimmicks.</p>'
            '<div class="badges">' + ios_badge("6796375617", campaign) +
            play_badge("com.eritech.leaflet", campaign) + '</div>')

def travelbinder_block(campaign):
    return ('<p>This tool comes from <strong><a href="/apps/travel-binder/">The Travel Binder</a></strong> — a fully offline binder for flights, '
            'hotels, bookings, documents, packing and checklists, with the whole trip on one map. '
            'No account, no cloud, no AI.</p>'
            '<div class="badges">' + ios_badge("6797601401", campaign) +
            play_badge("com.eritech.travelbinder", campaign) + '</div>')

def warranty_block(campaign):
    return ('<p><strong><a href="/apps/warranty-box/">Warranty Box</a></strong> keeps every receipt, warranty and return deadline in one place and '
            'reminds you before a window closes. Offline, no account.</p>'
            '<div class="badges">' + ios_badge("6790972644", campaign) +
            play_badge("com.eritech.warrantybox", campaign) + '</div>')

# ---------------------------------------------------------------- pages

PAGES = []

PAGES.append(dict(
    slug="sourdough-hydration-calculator",
    palette="bakelog",
    tab_title="Sourdough Hydration Calculator — Free & Instant | Eritech Studios",
    og_title="Sourdough Hydration Calculator",
    meta_desc="Work out your dough's hydration percentage from flour, water and starter — or work backwards from a target hydration. Free, no signup.",
    h1="Sourdough Hydration Calculator",
    lede="Flour, water and starter in — true hydration out. Or set a target and get the water to add.",
    calc_html="""<div class="seg" id="mode">
<button class="on" data-m="hyd" type="button">Find hydration %</button>
<button data-m="water" type="button">Find water needed</button>
</div>
<div class="row">
<div class="field"><label for="flour">Flour (g)</label><input type="number" id="flour" value="500" min="0" inputmode="decimal"></div>
<div class="field" id="f-water"><label for="water">Water (g)</label><input type="number" id="water" value="350" min="0" inputmode="decimal"></div>
<div class="field" id="f-target" hidden><label for="target">Target hydration (%)</label><input type="number" id="target" value="70" min="1" inputmode="decimal"></div>
</div>
<div class="row">
<div class="field"><label for="starter">Starter (g) — optional</label><input type="number" id="starter" value="100" min="0" inputmode="decimal"></div>
<div class="field"><label for="sh">Starter hydration (%)</label><input type="number" id="sh" value="100" min="1" inputmode="decimal"></div>
</div>
<div class="result"><div class="big" id="out">&mdash;</div><div class="sub" id="outsub"></div></div>
<p class="note">Starter counts toward the totals: a 100% starter is half flour, half water by weight.</p>""",
    calc_js="""function $(i){return document.getElementById(i)}
function num(i){var v=parseFloat($(i).value);return isNaN(v)?0:v}
var mode='hyd';
function band(h){
if(h<60)return 'Stiff dough — bagel and pretzel territory.';
if(h<68)return 'Moderate — easy to handle, a good place to start.';
if(h<75)return 'Classic sourdough range — balanced structure and an open crumb.';
if(h<85)return 'High hydration — slack dough, very open crumb, trickier shaping.';
return 'Very high hydration — ciabatta-style, needs confident handling.'}
function calc(){
var f=num('flour'),st=num('starter'),sh=num('sh');
var sf=st*100/(100+sh),sw=st*sh/(100+sh);
if(mode==='hyd'){
var w=num('water'),tf=f+sf,tw=w+sw;
if(tf<=0){$('out').innerHTML='&mdash;';$('outsub').textContent='';return}
var h=tw/tf*100;
$('out').textContent=h.toFixed(1)+'% hydration';
$('outsub').textContent=band(h)+' Total flour '+Math.round(tf)+' g, total water '+Math.round(tw)+' g.'
}else{
var t=num('target'),w2=t/100*(f+sf)-sw;if(w2<0)w2=0;
$('out').textContent=Math.round(w2)+' g water';
$('outsub').textContent='Add '+Math.round(w2)+' g water to '+Math.round(f)+' g flour'+(st>0?' and '+Math.round(st)+' g starter':'')+' for '+t+'% overall hydration.'}}
document.querySelectorAll('#mode button').forEach(function(b){b.addEventListener('click',function(){
mode=b.dataset.m;
document.querySelectorAll('#mode button').forEach(function(x){x.classList.toggle('on',x===b)});
$('f-water').hidden=(mode!=='hyd');$('f-target').hidden=(mode==='hyd');calc()})});""",
    explainer="""<section>
<h2>What is dough hydration?</h2>
<p>Hydration is the weight of water in a dough expressed as a percentage of the weight of flour. Mix 500&nbsp;g of flour with 350&nbsp;g of water and you have a 70% hydration dough. Bakers use this convention — baker&rsquo;s percentages, where flour is always 100% — because it makes recipes scalable: the ratio describes the dough no matter how big the batch is.</p>
<h2>Why the starter changes the number</h2>
<p>A sourdough starter is itself made of flour and water, so it has to be counted. A starter kept at 100% hydration is half flour and half water by weight: add 100&nbsp;g of it to your dough and you have really added 50&nbsp;g of flour and 50&nbsp;g of water. Ignore that and your &ldquo;70% dough&rdquo; can be several points wetter or drier than you think — which is exactly why two bakers following the same recipe sometimes end up with very different doughs. This calculator folds the starter into the totals for you.</p>
<h2>What hydration should I aim for?</h2>
<p>There is no single right answer, but the ranges are well established. Around 60–68% gives a firm, forgiving dough that is easy to shape — the best place to learn. 70–75% is the classic sourdough range, balancing an open crumb with manageable handling. Above 78% the dough turns slack and sticky and rewards experience with coil folds and gentle shaping.</p>
<p>Flour matters as much as the number: wholegrain and strong bread flours absorb far more water than plain white flour, so an 80% wholemeal dough can feel drier than a 72% white one. Treat the percentage as a starting point, adjust by feel, and keep notes on what each flour can take.</p>
</section>""",
    app_block=bakelog_block("sourdough_hydration", built=False),
    depth="""<section>
<h2>How it works</h2>
<p>The calculator first splits your starter into the flour and water it contains. A starter kept at a hydration of <em>h</em>% holds flour equal to its weight &times; 100 &divide; (100 + <em>h</em>), and water equal to its weight &times; <em>h</em> &divide; (100 + <em>h</em>). Those amounts are added to the flour and water you weigh out, and hydration is total water divided by total flour, multiplied by 100.</p>
<p>Working backwards is the same sum rearranged. To reach a target, the water to add is that percentage of the total flour, minus the water the starter is already carrying.</p>
<h2>A worked example</h2>
<p>Take a common formula: 500&nbsp;g of flour, 350&nbsp;g of water and 100&nbsp;g of starter at 100% hydration. On paper, 350 over 500 looks like a 70% dough.</p>
<table class="worked">
<tr><td>Flour inside the starter (100 &times; 100 &divide; 200)</td><td>50&nbsp;g</td></tr>
<tr><td>Water inside the starter (100 &times; 100 &divide; 200)</td><td>50&nbsp;g</td></tr>
<tr><td>Total flour (500 + 50)</td><td>550&nbsp;g</td></tr>
<tr><td>Total water (350 + 50)</td><td>400&nbsp;g</td></tr>
<tr><td>True hydration (400 &divide; 550 &times; 100)</td><td>72.7%</td></tr>
</table>
<p>The dough is nearly three points wetter than the recipe suggests. To bring it back to a true 70%, work backwards: 70% of 550&nbsp;g is 385&nbsp;g of water, less the 50&nbsp;g the starter supplies, which leaves 335&nbsp;g to add.</p>
</section>""",
    faqs=[
        ("How do I calculate sourdough hydration?",
         "Divide the total weight of water by the total weight of flour and multiply by 100 &mdash; counting the flour and water inside your starter as well as what you weigh out. A 100% starter is half flour and half water, so 100&nbsp;g of it adds 50&nbsp;g of each."),
        ("Does the starter count towards hydration?",
         "Yes. Starter is flour and water, so leaving it out understates both totals. With a generous amount of starter the difference can be several percentage points, which is enough to change how the dough handles."),
        ("What hydration should a beginner use?",
         "Somewhere between 60% and 68% with white bread flour. The dough is firm enough to shape without sticking to everything, and still bakes into a good loaf. Once shaping feels comfortable, move up a few points at a time."),
        ("What if my starter is not 100% hydration?",
         "Enter its actual hydration in the starter field. A stiff starter at 50% hydration is two-thirds flour and one-third water, so it adds more flour and less water to the dough than a liquid starter of the same weight. The calculator adjusts both totals for you."),
        ("Does water added later, such as with the salt, count?",
         "Yes. Hydration describes the finished dough, so any water that ends up in it counts &mdash; including water held back and worked in later with the salt. Add it to the water figure before you calculate."),
    ],
))

PAGES.append(dict(
    slug="bakers-percentage-calculator",
    palette="bakelog",
    tab_title="Baker's Percentage Calculator — Free & Instant | Eritech Studios",
    og_title="Baker's Percentage Calculator",
    meta_desc="Scale any bread recipe with baker's percentages — enter flour or target dough weight and get exact gram amounts for water, salt and levain. Free, no signup.",
    h1="Baker&rsquo;s Percentage Calculator",
    lede="Scale any bread formula. Start from your flour, or from the dough weight you want to end up with.",
    calc_html="""<div class="seg" id="mode">
<button class="on" data-m="flour" type="button">From flour weight</button>
<button data-m="dough" type="button">From dough weight</button>
</div>
<div class="field" id="f-flour"><label for="flour">Flour (g)</label><input type="number" id="flour" value="500" min="0" inputmode="decimal"></div>
<div class="field" id="f-dough" hidden><label for="dough">Target dough weight (g)</label><input type="number" id="dough" value="960" min="0" inputmode="decimal"></div>
<div class="row">
<div class="field"><label for="wp">Water (%)</label><input type="number" id="wp" value="70" min="0" inputmode="decimal"></div>
<div class="field"><label for="sp">Salt (%)</label><input type="number" id="sp" value="2" min="0" step="0.1" inputmode="decimal"></div>
<div class="field"><label for="lp">Levain (%)</label><input type="number" id="lp" value="20" min="0" inputmode="decimal"></div>
</div>
<div class="result"><table id="tbl"></table></div>
<p class="note">Levain here means ripe starter added to the final mix, counted as a percentage of the flour weight.</p>""",
    calc_js="""function $(i){return document.getElementById(i)}
function num(i){var v=parseFloat($(i).value);return isNaN(v)?0:v}
var mode='flour';
function calc(){
var wp=num('wp'),sp=num('sp'),lp=num('lp'),sum=(100+wp+sp+lp)/100,f;
if(mode==='flour'){f=num('flour')}else{f=sum>0?num('dough')/sum:0}
var w=f*wp/100,s=f*sp/100,l=f*lp/100,total=f+w+s+l;
$('tbl').innerHTML='<tr><td>Flour (100%)</td><td>'+Math.round(f)+' g</td></tr>'+
'<tr><td>Water ('+wp+'%)</td><td>'+Math.round(w)+' g</td></tr>'+
'<tr><td>Salt ('+sp+'%)</td><td>'+(Math.round(s*10)/10)+' g</td></tr>'+
'<tr><td>Levain ('+lp+'%)</td><td>'+Math.round(l)+' g</td></tr>'+
'<tr><td>Total dough</td><td>'+Math.round(total)+' g</td></tr>'}
document.querySelectorAll('#mode button').forEach(function(b){b.addEventListener('click',function(){
mode=b.dataset.m;
document.querySelectorAll('#mode button').forEach(function(x){x.classList.toggle('on',x===b)});
$('f-flour').hidden=(mode!=='flour');$('f-dough').hidden=(mode==='flour');calc()})});""",
    explainer="""<section>
<h2>How baker&rsquo;s percentages work</h2>
<p>In a bread formula every ingredient is written as a percentage of the total flour weight, with flour itself fixed at 100%. A classic sourdough might read: flour 100%, water 70%, salt 2%, levain 20%. The percentages describe the dough itself, independent of batch size — which is what makes them so useful. Double the flour and every other gram amount doubles with it, and any two recipes can be compared at a glance.</p>
<h2>Scaling up and down</h2>
<p>The most common real-world use is working backwards from a target. Your banneton takes roughly a 950&nbsp;g loaf, so how much flour do you start with? Divide the target dough weight by the sum of the percentages (here 1.92) and you get the flour weight; everything else follows. This calculator does both directions — give it flour and it builds the formula down the page, give it a dough weight and it solves for the flour first.</p>
<h2>Sensible ranges</h2>
<p>Salt almost always sits at 1.8–2.2% — below that bread tastes flat, above 2.5% fermentation slows noticeably. Levain typically runs 15–25% of the flour: more levain ferments faster and tips the flavour toward sour, less gives you a longer, more forgiving timeline. Water is the variable bakers argue about; see the <a href="/tools/sourdough-hydration-calculator/">hydration calculator</a> for what the percentage actually means for handling and crumb.</p>
<p>One caution when comparing formulas: some recipes count the flour and water inside the levain toward the totals, and some do not. It rarely changes the bread much, but it explains why two &ldquo;75% hydration&rdquo; recipes can behave differently.</p>
</section>""",
    app_block=bakelog_block("bakers_percentage", built=False),
    depth="""<section>
<h2>How it works</h2>
<p>From a flour weight, the sums are direct. Flour is 100%, and every other line is the flour multiplied by its percentage and divided by 100: 70% water on 500&nbsp;g of flour is 350&nbsp;g. The total dough is the four lines added together.</p>
<p>From a dough weight, the calculator adds the percentages to the flour&rsquo;s 100 and divides by 100 to get a multiplier &mdash; 1.92 for the default formula. The target weight divided by that multiplier is the flour, and the other lines are worked out from the flour as before. Flour, water, levain and the total are rounded to the nearest gram, and salt to a tenth of a gram, where a single gram is a large share of the quantity. The levain is treated as one ingredient: the flour and water inside it are not added to the flour and water lines.</p>
<h2>A worked example</h2>
<p>Say you want a 1&nbsp;kg loaf from the default formula: 70% water, 2% salt and 20% levain.</p>
<table class="worked">
<tr><td>Sum of percentages (100 + 70 + 2 + 20)</td><td>192%</td></tr>
<tr><td>Multiplier (192 &divide; 100)</td><td>1.92</td></tr>
<tr><td>Flour (1,000 &divide; 1.92)</td><td>521&nbsp;g</td></tr>
<tr><td>Water (520.8 &times; 70%)</td><td>365&nbsp;g</td></tr>
<tr><td>Salt (520.8 &times; 2%)</td><td>10.4&nbsp;g</td></tr>
<tr><td>Levain (520.8 &times; 20%)</td><td>104&nbsp;g</td></tr>
<tr><td>Total dough</td><td>1,000&nbsp;g</td></tr>
</table>
<p>The other lines are calculated from the unrounded flour, 520.8&nbsp;g, so the rounded figures add up to 1,000.4&nbsp;g rather than exactly 1,000 &mdash; a rounding artefact, not an error. If you are doing it by hand, carry the decimal through in the same way. In practice a few grams stay behind on the bowl and the bench, so if the loaf has to reach a set weight, ask for a little more than you need.</p>
</section>""",
    faqs=[
        ("How do I calculate baker&rsquo;s percentage?",
         "Divide the weight of each ingredient by the total flour weight and multiply by 100. With 500&nbsp;g of flour, 350&nbsp;g of water is 70% and 10&nbsp;g of salt is 2%. If a recipe uses more than one flour &mdash; white and wholemeal, say &mdash; add them together first: the combined flour is the 100%, and each flour can then be written as its share of that total."),
        ("Why do baker&rsquo;s percentages add up to more than 100%?",
         "Because flour is fixed at 100% and everything else is measured against it, not against the whole dough. A formula of 70% water, 2% salt and 20% levain adds up to 192%, which simply means the finished dough weighs 1.92 times the flour. That sum is the number to divide by when you work back from a dough weight to the flour you need."),
        ("How much flour do I need for a 1&nbsp;kg loaf?",
         "It depends on the formula. Add up the percentages, divide by 100, and divide 1,000&nbsp;g by the result. For 70% water, 2% salt and 20% levain the divisor is 1.92, which gives about 521&nbsp;g of flour. A wetter or richer formula has a larger sum, so the same 1&nbsp;kg of dough needs less flour."),
        ("How do I scale a bread recipe up or down?",
         "Convert it to baker&rsquo;s percentages once, then choose a new flour weight and multiply each percentage by it. Because every ingredient keeps the same relationship to the flour, the dough keeps the same character at any size. Alternatively, work from the dough weight you want &mdash; the number of loaves times the weight of each &mdash; and let the percentages solve for the flour."),
        ("Is levain counted as flour in baker&rsquo;s percentage?",
         "Formulas differ. In this calculator the levain is a single ingredient, stated as a percentage of the flour you weigh out, and its own flour and water are not added to the flour and water lines. Some bakers work from total flour instead, folding the levain&rsquo;s flour and water into the figures. To see what that does to the real water percentage, use the <a href=\"/tools/sourdough-hydration-calculator/\">hydration calculator</a>."),
    ],
))

PAGES.append(dict(
    slug="starter-feeding-ratio-calculator",
    palette="bakelog",
    tab_title="Sourdough Starter Feeding Ratio Calculator — Free & Instant | Eritech Studios",
    og_title="Starter Feeding Ratio Calculator",
    meta_desc="Work out flour and water amounts for any sourdough starter feeding ratio — 1:1:1, 1:2:2, 1:5:5 or your own — with expected peak times. Free, no signup.",
    h1="Sourdough Starter Feeding Ratio Calculator",
    lede="Pick a ratio, enter how much starter you&rsquo;re keeping, and get the flour and water to feed it.",
    calc_html="""<div class="row">
<div class="field"><label for="ratio">Feeding ratio (starter : flour : water)</label>
<select id="ratio">
<option value="1,1,1">1 : 1 : 1</option>
<option value="1,2,2" selected>1 : 2 : 2</option>
<option value="1,5,5">1 : 5 : 5</option>
<option value="1,10,10">1 : 10 : 10</option>
<option value="custom">Custom&hellip;</option>
</select></div>
<div class="field"><label for="keep">Starter you&rsquo;re keeping (g)</label><input type="number" id="keep" value="20" min="0" inputmode="decimal"></div>
</div>
<div class="row" id="customrow" hidden>
<div class="field"><label for="ca">Starter part</label><input type="number" id="ca" value="1" min="1" inputmode="decimal"></div>
<div class="field"><label for="cb">Flour part</label><input type="number" id="cb" value="3" min="0" inputmode="decimal"></div>
<div class="field"><label for="cc">Water part</label><input type="number" id="cc" value="3" min="0" inputmode="decimal"></div>
</div>
<div class="result"><div class="big" id="out">&mdash;</div><div class="sub" id="outsub"></div></div>
<p class="note">Peak estimates assume a healthy starter at roughly 22–24&nbsp;&deg;C room temperature. Cooler kitchens run slower.</p>""",
    calc_js="""function $(i){return document.getElementById(i)}
function num(i){var v=parseFloat($(i).value);return isNaN(v)?0:v}
function peak(mult){
if(mult<=1)return '4–6 hours';
if(mult<=2)return '6–8 hours';
if(mult<=5)return '8–12 hours';
return '12–16 hours'}
function calc(){
var sel=$('ratio').value,a,b,c;
$('customrow').hidden=(sel!=='custom');
if(sel==='custom'){a=num('ca')||1;b=num('cb');c=num('cc')}
else{var p=sel.split(',');a=+p[0];b=+p[1];c=+p[2]}
var k=num('keep'),fl=k*b/a,w=k*c/a,total=k+fl+w;
$('out').textContent=Math.round(fl)+' g flour + '+Math.round(w)+' g water';
$('outsub').textContent='Feed '+Math.round(k)+' g starter to make '+Math.round(total)+' g total. Expected peak: about '+peak(b/a)+'.'}""",
    explainer="""<section>
<h2>What the ratio means</h2>
<p>A feeding ratio is written starter&nbsp;:&nbsp;flour&nbsp;:&nbsp;water, by weight. Feeding at 1:2:2 means that for every gram of starter you keep, you add two grams of flour and two of water — so 20&nbsp;g of starter gets 40&nbsp;g of flour and 40&nbsp;g of water, making 100&nbsp;g. All the ratios here keep the starter at 100% hydration; only the amount of fresh food changes.</p>
<h2>Choosing a ratio</h2>
<p>The ratio is really a timer. A small feed like 1:1:1 gives the culture little fresh food, so it peaks fast — typically four to six hours — and turns sour quickly afterwards. Bigger feeds dilute the culture and take longer to peak: 1:2:2 lands around six to eight hours, 1:5:5 around eight to twelve, and 1:10:10 can hold overnight and beyond. Pick the ratio that makes your starter peak when you actually need it, rather than fighting your schedule.</p>
<h2>Reading the peak</h2>
<p>A ripe starter has domed or just begun to flatten, smells pleasantly tangy rather than harsh, and is full of bubbles through the body of the culture, not just on top. Temperature moves everything: at 26&nbsp;&deg;C a 1:5:5 feed can behave like a 1:2:2 at 20&nbsp;&deg;C. If your kitchen runs cold, use a smaller ratio or find a warmer spot; if your starter races past its peak before you wake up, feed it more heavily.</p>
<p>Whatever ratio you settle on, consistency beats cleverness — the same feed at the same times teaches you exactly what &ldquo;ready&rdquo; looks like for your jar.</p>
</section>""",
    app_block=bakelog_block("starter_feeding", built=False),
    depth="""<section>
<h2>How it works</h2>
<p>A ratio of <em>a</em>&nbsp;:&nbsp;<em>b</em>&nbsp;:&nbsp;<em>c</em> is scaled to the starter you are keeping. The flour to add is the kept starter &times; <em>b</em> &divide; <em>a</em>, and the water is the kept starter &times; <em>c</em> &divide; <em>a</em>. The total is simply the three added together.</p>
<p>The peak estimate comes from how much fresh flour the culture has to work through, relative to itself &mdash; the flour part divided by the starter part. Up to 1&times; it expects a peak in about 4&ndash;6 hours, up to 2&times; about 6&ndash;8, up to 5&times; about 8&ndash;12, and beyond that 12&ndash;16. Those windows assume a healthy starter at roughly 22&ndash;24&nbsp;&deg;C.</p>
<h2>A worked example</h2>
<p>Say you want a ripe starter first thing in the morning and you feed it at ten o&rsquo;clock the night before. An overnight gap calls for a large feed, so choose 1:5:5 and keep 15&nbsp;g of starter.</p>
<table class="worked">
<tr><td>Flour (15 &times; 5 &divide; 1)</td><td>75&nbsp;g</td></tr>
<tr><td>Water (15 &times; 5 &divide; 1)</td><td>75&nbsp;g</td></tr>
<tr><td>Total in the jar (15 + 75 + 75)</td><td>165&nbsp;g</td></tr>
<tr><td>Expected peak (flour is 5&times; the starter)</td><td>8&ndash;12 hours</td></tr>
</table>
<p>A ten o&rsquo;clock feed should peak somewhere between six and ten the next morning. If your kitchen is cold overnight, expect the later end of that window or beyond; if it is warm, check early.</p>
</section>""",
    faqs=[
        ("What is the best sourdough starter feeding ratio?",
         "There is no single best ratio &mdash; the right one is whichever peaks when you need it. 1:1:1 peaks fastest, typically in about 4&ndash;6 hours at a warm room temperature, while 1:5:5 takes roughly 8&ndash;12 and suits an overnight feed. Choose by your schedule, then keep it consistent so you learn what ripe looks like for your jar."),
        ("How much flour and water should I feed my starter?",
         "Multiply the starter you keep by each side of the ratio. At 1:1:1, 50&nbsp;g of starter gets 50&nbsp;g of flour and 50&nbsp;g of water. At 1:5:5, 15&nbsp;g of starter gets 75&nbsp;g of each. The amount you keep, not the size of your jar, sets the quantities."),
        ("What does 1:1:1 mean for a sourdough starter?",
         "Equal weights of starter, flour and water. It is the smallest common feed, so the culture has little fresh food to work through: it rises quickly, peaks within a few hours at a warm room temperature, and turns sour soon afterwards if it is not used."),
        ("Why does my starter peak too early or too late?",
         "Temperature is the usual reason. The estimates here assume roughly 22&ndash;24&nbsp;&deg;C; a warmer kitchen speeds everything up and a cooler one slows it down considerably. If your starter peaks before you need it, feed a larger ratio. If it is late, use a smaller ratio or move the jar somewhere warmer."),
        ("Do I have to discard starter before feeding?",
         "The ratio is based on how much starter you keep, so discarding is really about keeping feeds small. Keeping 10&ndash;20&nbsp;g and discarding the rest means modest amounts of fresh flour each time. Keep it all, and the flour and water have to grow to match &mdash; the jar, and the flour bill, get bigger with every feed."),
    ],
))

PAGES.append(dict(
    slug="coffee-ratio-calculator",
    palette="kohii",
    tab_title="Coffee to Water Ratio Calculator — Free & Instant | Eritech Studios",
    og_title="Coffee Ratio Calculator",
    meta_desc="Work out coffee-to-water ratios for V60, Chemex, AeroPress, French press, moka pot, cold brew and espresso. Free, no signup.",
    h1="Coffee to Water Ratio Calculator",
    lede="Pick a brew method, enter your coffee or your water, and get the other side of the ratio.",
    calc_html="""<div class="row">
<div class="field"><label for="method">Brew method</label>
<select id="method">
<option value="16" selected>V60 / pour-over (1:16)</option>
<option value="16">Chemex (1:16)</option>
<option value="15">AeroPress (1:15)</option>
<option value="15">French press (1:15)</option>
<option value="10">Moka pot (1:10)</option>
<option value="8">Cold brew concentrate (1:8)</option>
<option value="2">Espresso (1:2)</option>
</select></div>
<div class="field"><label for="ratio">Ratio — 1 :</label><input type="number" id="ratio" value="16" min="1" step="0.5" inputmode="decimal"></div>
</div>
<div class="seg" id="mode">
<button class="on" data-m="c2w" type="button">Coffee &rarr; water</button>
<button data-m="w2c" type="button">Water &rarr; coffee</button>
</div>
<div class="field" id="f-coffee"><label for="coffee">Coffee (g)</label><input type="number" id="coffee" value="20" min="0" step="0.1" inputmode="decimal"></div>
<div class="field" id="f-water" hidden><label for="water">Water (g / ml)</label><input type="number" id="water" value="320" min="0" inputmode="decimal"></div>
<div class="result"><div class="big" id="out">&mdash;</div><div class="sub" id="outsub"></div></div>
<p class="note">Grams and millilitres of water are interchangeable — a scale is far more accurate than a jug either way.</p>""",
    calc_js="""function $(i){return document.getElementById(i)}
function num(i){var v=parseFloat($(i).value);return isNaN(v)?0:v}
var mode='c2w';
$('method').addEventListener('change',function(){$('ratio').value=$('method').value});
function calc(){
var r=num('ratio');if(r<=0)r=1;
if(mode==='c2w'){var c=num('coffee');
$('out').textContent=Math.round(c*r)+' g water';
$('outsub').textContent=c+' g coffee at 1:'+r+' &rarr; '+Math.round(c*r)+' g water.';$('outsub').innerHTML=$('outsub').textContent.replace('&rarr;','\\u2192')}
else{var w=num('water');
$('out').textContent=(Math.round(w/r*10)/10)+' g coffee';
$('outsub').textContent=w+' g water at 1:'+r+' \\u2192 '+(Math.round(w/r*10)/10)+' g coffee.'}}
document.querySelectorAll('#mode button').forEach(function(b){b.addEventListener('click',function(){
mode=b.dataset.m;
document.querySelectorAll('#mode button').forEach(function(x){x.classList.toggle('on',x===b)});
$('f-coffee').hidden=(mode!=='c2w');$('f-water').hidden=(mode==='c2w');calc()})});""",
    explainer="""<section>
<h2>What a brew ratio means</h2>
<p>A ratio of 1:16 means one gram of ground coffee for every sixteen grams of water — 20&nbsp;g of coffee to 320&nbsp;g of water. It is the single most useful number in brewing, because it fixes strength before you touch grind size or technique. Two people using the same ratio, water and beans will make recognisably similar cups; two people guessing with scoops will not.</p>
<h2>Why methods differ</h2>
<p>Percolation methods like V60 and Chemex run comfortably at 1:15 to 1:17 — the classic filter-strength cup. Immersion methods such as French press and AeroPress are often brewed slightly tighter, around 1:14 to 1:15, because some water stays trapped in the bed. A moka pot at roughly 1:10 lands between filter and espresso, cold brew concentrate at 1:8 is made to be diluted, and espresso at 1:2 is its own world — see the <a href="/tools/espresso-ratio-calculator/">espresso ratio calculator</a> for dose and yield.</p>
<h2>Adjusting to taste</h2>
<p>Move the ratio for strength, the grind for extraction. If the cup tastes weak and thin, tighten the ratio (1:15 instead of 1:16); if it is muddy and heavy, loosen it. If it tastes sour, grind finer or brew hotter; bitter, coarser or cooler. Change one variable at a time, keep the rest fixed, and taste after each change — that is dialling in, and it works faster than any amount of theory.</p>
</section>""",
    app_block=kohii_block("coffee_ratio"),
    depth="""<section>
<h2>How it works</h2>
<p>Choosing a brew method fills in its ratio: 1:16 for V60 and Chemex, 1:15 for AeroPress and French press, 1:10 for a moka pot, 1:8 for cold brew concentrate and 1:2 for espresso. You can type any ratio over the top of it. The calculator then does one of two sums. Going from coffee to water, it multiplies the coffee by the ratio and rounds to the nearest gram. Going from water to coffee, it divides the water by the ratio and rounds to a tenth of a gram. Water in grams and in millilitres is treated as the same thing.</p>
<h2>A worked example</h2>
<p>Say you are brewing 500&nbsp;g of water in a cafetière and want to know how much coffee to weigh out.</p>
<table class="worked">
<tr><td>Water</td><td>500&nbsp;g</td></tr>
<tr><td>Ratio (French press preset)</td><td>1:15</td></tr>
<tr><td>Coffee (500 &divide; 15 = 33.33&hellip;, rounded)</td><td>33.3&nbsp;g</td></tr>
<tr><td>The same water at 1:16 (500 &divide; 16 = 31.25, rounded)</td><td>31.3&nbsp;g</td></tr>
</table>
<p>Two grams sounds like nothing, but moving from 1:16 to 1:15 puts roughly 7% more coffee into the same water, and that is a difference you can taste. It is also why the scale matters more than the exact starting ratio: whichever number you choose, you can repeat it tomorrow and adjust from a known point.</p>
</section>""",
    faqs=[
        ("What is the golden ratio for coffee?",
         "Usually a filter ratio somewhere between about 1:15 and 1:18 &mdash; roughly 55 to 67&nbsp;g of coffee per litre of water. It is a range rather than a single number, because beans, roast and personal taste all move it. 1:16 is a sensible middle to start from: brew it, then tighten the ratio if the cup is thin, or loosen it if it is heavy."),
        ("How many grams of coffee per cup?",
         "It depends on the cup, which is why a ratio is more useful than a scoop. For 250&nbsp;g of water, 1:16 gives 15.6&nbsp;g of coffee and 1:15 gives 16.7&nbsp;g, so somewhere around 15 to 17&nbsp;g is a good starting point for a mug of filter. For a bigger mug, enter the water you actually pour and let the ratio scale the coffee with it."),
        ("Is a 1:16 ratio coffee to water or water to coffee?",
         "Coffee to water: one part coffee to sixteen parts water, by weight. Some recipes write it the other way round as 16:1, and some give a dose per litre instead. To convert, divide 1,000 by the ratio &mdash; 1:16 is 62.5&nbsp;g of coffee per litre &mdash; or divide 1,000 by the grams per litre to get back to a ratio."),
        ("Does the bloom water count towards the ratio?",
         "Yes. For pour-over, the ratio covers all the water that goes through the coffee, bloom included, so a recipe that blooms with 40&nbsp;g and then pours to 320&nbsp;g uses 320&nbsp;g in total. The cup holds a little less, because the wet grounds keep some back. Espresso is counted differently: its ratio compares the dry dose with the liquid in the cup, not the water that went in."),
        ("What ratio should I use for a cafetière?",
         "Around 1:15 is a good starting point, and it is what the French press preset uses. Immersion brewing is often run a little tighter than pour-over, from about 1:14 to 1:15, because some water stays trapped in the grounds. If the cup tastes weak, move towards 1:14 before changing anything else; if it tastes heavy, try 1:16."),
    ],
))

PAGES.append(dict(
    slug="espresso-ratio-calculator",
    palette="kohii",
    tab_title="Espresso Ratio Calculator — Free & Instant | Eritech Studios",
    og_title="Espresso Ratio Calculator",
    meta_desc="Solve espresso dose, yield or brew ratio from the other two — with ristretto, normale and lungo ranges explained. Free, no signup.",
    h1="Espresso Ratio Calculator",
    lede="Dose, yield, ratio — enter any two and solve the third.",
    calc_html="""<div class="seg" id="mode">
<button class="on" data-m="yield" type="button">Solve for yield</button>
<button data-m="dose" type="button">Solve for dose</button>
<button data-m="ratio" type="button">Solve for ratio</button>
</div>
<div class="row">
<div class="field"><label for="dose">Dose — dry coffee in (g)</label><input type="number" id="dose" value="18" min="0" step="0.1" inputmode="decimal"></div>
<div class="field"><label for="yield">Yield — espresso out (g)</label><input type="number" id="yield" value="36" min="0" step="0.1" inputmode="decimal"></div>
<div class="field"><label for="ratio">Ratio — 1 :</label><input type="number" id="ratio" value="2" min="0.5" step="0.1" inputmode="decimal"></div>
</div>
<div class="result"><div class="big" id="out">&mdash;</div><div class="sub" id="outsub"></div></div>
<p class="note">Weigh the liquid espresso on a scale under the cup — volume and crema lie, grams don&rsquo;t.</p>""",
    calc_js="""function $(i){return document.getElementById(i)}
function num(i){var v=parseFloat($(i).value);return isNaN(v)?0:v}
var mode='yield';
function style(r){
if(r<1.5)return 'a ristretto — concentrated, heavy body';
if(r<=2.5)return 'a normale — the classic modern range';
return 'a lungo — lighter body, higher extraction'}
function setDim(){['dose','yield','ratio'].forEach(function(k){
var solved=(k===mode);$(k).disabled=solved;$(k).style.opacity=solved?0.55:1})}
function calc(){
var d=num('dose'),y=num('yield'),r=num('ratio');
if(mode==='yield'){y=d*r;$('yield').value=Math.round(y*10)/10;
$('out').textContent=(Math.round(y*10)/10)+' g out'}
else if(mode==='dose'){d=r>0?y/r:0;$('dose').value=Math.round(d*10)/10;
$('out').textContent=(Math.round(d*10)/10)+' g in'}
else{r=d>0?y/d:0;$('ratio').value=Math.round(r*100)/100;
$('out').textContent='1 : '+(Math.round(r*100)/100)}
var rr=d>0?y/d:0;
$('outsub').textContent=Math.round(d*10)/10+' g in \\u2192 '+Math.round(y*10)/10+' g out ('+(Math.round(rr*100)/100)+') — '+style(rr)+'.'}
document.querySelectorAll('#mode button').forEach(function(b){b.addEventListener('click',function(){
mode=b.dataset.m;
document.querySelectorAll('#mode button').forEach(function(x){x.classList.toggle('on',x===b)});
setDim();calc()})});
setDim();""",
    explainer="""<section>
<h2>Dose, yield, ratio</h2>
<p>Three numbers define an espresso recipe. The <strong>dose</strong> is the dry coffee in the basket, the <strong>yield</strong> is the liquid espresso in the cup, and the <strong>brew ratio</strong> is yield divided by dose. A modern standard shot is 18&nbsp;g in, 36&nbsp;g out — a 1:2 ratio — in somewhere around 25 to 32 seconds. Fix any two and the third follows, which is exactly what this calculator does.</p>
<h2>Ristretto, normale, lungo</h2>
<p>Ratios under about 1:1.5 are ristretto territory: intense, syrupy, muted acidity, and unforgiving of an uneven grind. 1:1.5 to 1:2.5 is the normale range where most cafes and most beans live. Push past 1:2.5 into lungo and you trade body for clarity and higher extraction — often a good call for lighter roasts that taste sour and underdeveloped at 1:2.</p>
<h2>Dialling in</h2>
<p>Keep the dose fixed to whatever your basket is designed for — changing it moves everything at once. Then use grind to control time and ratio to control style. Sour, sharp, fast shots want a finer grind; bitter, harsh, slow ones want coarser. If a shot is balanced but too intense, lengthen the ratio rather than grinding coarser. And always judge by taste, not by the clock: the timer is a diagnostic, not the goal. Logging each change — dose, yield, time, grind setting — is what turns twenty sink shots into five.</p>
</section>""",
    app_block=kohii_block("espresso_ratio"),
    depth="""<section>
<h2>How it works</h2>
<p>Choose which number to solve for and the calculator greys that field out and fills it in from the other two. Yield is dose &times; ratio, dose is yield &divide; ratio, and ratio is yield &divide; dose. Dose and yield are shown to a tenth of a gram, the ratio to two decimal places.</p>
<p>It then names the style from yield &divide; dose. Anything below 1:1.5 is a ristretto, 1:1.5 up to and including 1:2.5 is a normale, and anything longer than 1:2.5 is a lungo.</p>
<h2>A worked example</h2>
<p>You dose 18.5&nbsp;g into the basket and stop the shot when the scale under the cup reads 42&nbsp;g.</p>
<table class="worked">
<tr><td>Dose</td><td>18.5&nbsp;g</td></tr>
<tr><td>Yield</td><td>42&nbsp;g</td></tr>
<tr><td>Ratio (42 &divide; 18.5 = 2.270&hellip;, to two decimals)</td><td>1&nbsp;:&nbsp;2.27</td></tr>
<tr><td>Style (between 1:1.5 and 1:2.5)</td><td>Normale</td></tr>
</table>
<p>A comfortable normale, a little longer than the textbook 1:2. For this dose the lungo line sits at 18.5 &times; 2.5 = 46.25&nbsp;g, so letting the shot run much past 46&nbsp;g changes the label. To hit exactly 1:2 instead, solve for yield: 18.5&nbsp;g in calls for 37&nbsp;g out.</p>
</section>""",
    faqs=[
        ("What is the best ratio for espresso?",
         "There is no single best, but 1:2 &mdash; 18&nbsp;g in, 36&nbsp;g out &mdash; is the usual starting point and sits in the middle of the normale range. From there, taste decides. Lighter roasts often open up at longer ratios such as 1:2.5, while darker roasts and milk drinks can suit something shorter. Move the ratio in small steps and keep the dose fixed while you do."),
        ("What is the difference between a ristretto and a lungo?",
         "With the same dose, it comes down to how much liquid you let through. A ristretto stops early, below about 1:1.5, for a small, syrupy, intense shot. A lungo runs past 1:2.5, for a longer, lighter-bodied cup with more of the coffee extracted. A normale sits between them. They are points on one scale rather than separate drinks, which is why a ratio describes them better than a name."),
        ("How long should an espresso shot take?",
         "Around 25 to 32 seconds is a common target for an 18&nbsp;g in, 36&nbsp;g out shot. Treat it as a diagnostic rather than a rule. A shot that runs much faster usually wants a finer grind, and one that crawls wants a coarser one &mdash; but if a shot outside the window tastes good, it is a good shot, and the clock can be ignored."),
        ("Should I measure espresso by weight or by volume?",
         "By weight. Crema is a foam of gas bubbles, so a fresh shot looks bigger than it is and shrinks as it settles, and the amount of crema changes from bean to bean and day to day. A scale under the cup reads the same every time. The yield you weigh includes the crema, and that is fine &mdash; it is part of the drink."),
        ("How much coffee goes in a double shot?",
         "Commonly around 18&nbsp;g, but the right dose is the one your basket was designed for, and many baskets have it stamped on them. Too little and the puck sits loose and wet; too much and it presses against the shower screen. Settle on a dose, then leave it alone while you use grind and yield to dial in."),
    ],
))

PAGES.append(dict(
    slug="coffee-freshness-calculator",
    palette="kohii",
    tab_title="Coffee Freshness Calculator — Free & Instant | Eritech Studios",
    og_title="Coffee Freshness Calculator",
    meta_desc="Enter a roast date and see whether your beans are resting, at their peak, or past it — for espresso and filter. Free, no signup.",
    h1="Coffee Freshness Calculator",
    lede="How long after the roast date is coffee at its best? Enter yours and see where the bag stands.",
    calc_html="""<div class="row">
<div class="field"><label for="roast">Roast date</label><input type="date" id="roast"></div>
<div class="field"><label for="method">Brewing as</label>
<select id="method">
<option value="esp" selected>Espresso</option>
<option value="fil">Filter / pour-over</option>
</select></div>
</div>
<div class="result"><div class="big" id="out">&mdash;</div><div class="sub" id="outsub"></div></div>
<p class="note">Windows assume whole beans in a sealed bag away from heat and light. Ground coffee fades several times faster.</p>""",
    calc_js="""function $(i){return document.getElementById(i)}
var W={esp:{rest:10,peakEnd:45,useEnd:60},fil:{rest:5,peakEnd:30,useEnd:45}};
function fmt(d){return d.toLocaleDateString(undefined,{day:'numeric',month:'short'})}
function calc(){
var v=$('roast').value;if(!v){$('out').innerHTML='&mdash;';$('outsub').textContent='Pick your roast date.';return}
var w=W[$('method').value];
var roast=new Date(v+'T00:00:00'),now=new Date();
var days=Math.floor((now-roast)/86400000);
var restEnd=new Date(roast.getTime()+w.rest*86400000);
var peakEnd=new Date(roast.getTime()+w.peakEnd*86400000);
if(days<0){$('out').textContent='Future roast date';$('outsub').textContent='That date has not happened yet.';return}
if(days<w.rest){$('out').textContent='Still resting — day '+days;
$('outsub').textContent='Fresh roasts release CO\\u2082 that disrupts extraction. Best from around '+fmt(restEnd)+', in the sweet spot until roughly '+fmt(peakEnd)+'.'}
else if(days<=w.peakEnd){$('out').textContent='In the sweet spot — day '+days;
$('outsub').textContent='Degassed and flavourful. Expect the peak to hold until around '+fmt(peakEnd)+'.'}
else if(days<=w.useEnd){$('out').textContent='Past peak — day '+days;
$('outsub').textContent='Still perfectly drinkable, but aromatics are fading. Grind fine-tuning can claw some back.'}
else{$('out').textContent='Likely stale — day '+days;
$('outsub').textContent='Flavour will be flat and papery. Fine for milk drinks; buy fresher for anything black.'}}""",
    explainer="""<section>
<h2>Why coffee needs to rest</h2>
<p>Roasting fills beans with carbon dioxide, and for the first days after roast that gas escapes faster than water can extract flavour. Brew too early and the bloom is violent, extraction is uneven, and the cup tastes sharp and hollow. This is why &ldquo;fresher is better&rdquo; is only half true: coffee needs a rest before it needs urgency.</p>
<h2>Espresso and filter age differently</h2>
<p>Espresso is the fussier method. The pressure of a 9-bar shot amplifies degassing problems, so most roasts want ten days or more of rest before they pull cleanly, and then drink beautifully for roughly four to six weeks. Filter brewing is gentler: beans are usually ready within about five days and stay in their window for around a month. Lighter roasts generally rest longer and fade slower than dark ones, which peak sooner and stale faster — treat the windows here as sensible defaults, not laws.</p>
<h2>Making beans last</h2>
<p>Oxygen, heat, light and moisture are the enemies, in that order. Keep beans whole and sealed — a bag with a one-way valve or an airtight container in a cupboard is fine — and grind just before brewing, since ground coffee loses aromatics within minutes rather than weeks. For a supply you cannot drink in time, freezing works far better than its reputation: portion beans into small airtight containers, freeze on arrival, and grind straight from frozen. A bag frozen in its sweet spot effectively pauses there.</p>
</section>""",
    app_block=kohii_block("coffee_freshness"),
    depth="""<section>
<h2>How it works</h2>
<p>The calculator counts whole days from the roast date to today, rounding down, so the roast date itself is day&nbsp;0 and a bag roasted yesterday counts as day&nbsp;1 all of today. It then places that number in one of four windows that depend on the brewing method.</p>
<p>For espresso, days 0 to 9 are resting, days 10 to 45 are the sweet spot, days 46 to 60 are past peak, and anything after day 60 is likely stale. Filter runs earlier and shorter: resting to day 4, the sweet spot from day 5 to day 30, past peak to day 45, and likely stale after that. The dates it shows are simply the roast date plus 10 and 45 days for espresso, or plus 5 and 30 for filter.</p>
<h2>A worked example</h2>
<p>A bag roasted seven days ago, read for each method:</p>
<table class="worked">
<tr><td>Days since roast</td><td>7</td></tr>
<tr><td>Espresso (resting until day 10, since 7 &lt; 10)</td><td>Still resting &mdash; day 7</td></tr>
<tr><td>Espresso ready from (roast date + 10 days)</td><td>In 3 days</td></tr>
<tr><td>Espresso sweet spot ends (roast date + 45 days)</td><td>In 38 days</td></tr>
<tr><td>Filter (ready from day 5, and 7 &le; 30)</td><td>In the sweet spot &mdash; day 7</td></tr>
<tr><td>Filter sweet spot ends (roast date + 30 days)</td><td>In 23 days</td></tr>
</table>
<p>The same bag can be too young for one method and ready for another. If it is the only coffee in the house, brew it as filter for a few days and move it to the espresso machine from day 10.</p>
</section>""",
    faqs=[
        ("How long after the roast date is coffee good?",
         "For filter, most beans are at their best from about five days to a month after roasting. Espresso is fussier, and the window used here runs from around day 10 to day 45. After that the coffee stays drinkable for roughly another fortnight, but its aromatics fade steadily. These are sensible defaults for whole beans kept sealed, not hard limits &mdash; roast level and storage both move them."),
        ("Can coffee be too fresh?",
         "Yes. For the first days after roasting, beans are still releasing a lot of carbon dioxide, and it gets in the way of extraction. Brewed too early, filter coffee blooms hard and espresso pulls unevenly, and both tend to taste sharp and hollow. A few days&rsquo; rest for filter, and ten or so for espresso, usually sorts it out without any change to your recipe."),
        ("Is old coffee safe to drink?",
         "Stale coffee is a flavour problem rather than a safety one. Kept dry and sealed, roasted beans lose aroma and turn flat and papery long before anything else happens to them. The exception is moisture: beans that have got damp can grow mould, and those belong in the bin. Otherwise, old beans are fine in milk drinks, just disappointing black."),
        ("Should I keep coffee in the fridge?",
         "It is better not to. Each time a cold bag comes out into a warm kitchen, moisture condenses on the beans, and coffee readily picks up odours from whatever else is in there. A sealed container in a cool, dark cupboard suits beans you will finish within the window. For anything longer, use the freezer, portioned so you only take out what you need and the rest stays frozen."),
        ("What is the difference between a roast date and a best-before date?",
         "A roast date tells you when the beans were roasted, which is what this calculator needs. A best-before date is set by the seller and often falls many months after roasting, so on its own it says little about where the coffee sits in its flavour window. If a bag carries only a best-before date, there is no reliable way to work out its age."),
    ],
))

PAGES.append(dict(
    slug="wine-drink-window-calculator",
    palette="cellar",
    tab_title="Wine Drink Window Calculator — Free & Instant | Eritech Studios",
    og_title="Wine Drink Window Calculator",
    meta_desc="Enter a wine style and vintage and get its likely drinking window — still ageing, ready now, at peak, or fading. Free, no signup.",
    h1="Wine Drink Window Calculator",
    lede="When should you open that bottle? Pick the style, enter the vintage, and see where it sits today.",
    calc_html="""<div class="row">
<div class="field"><label for="style">Wine style</label>
<select id="style">
<option value="8,25" selected>Barolo / Barbaresco</option>
<option value="8,30">Bordeaux — classed growth red</option>
<option value="3,10">Bordeaux — everyday red</option>
<option value="4,12">Red Burgundy — village / premier cru</option>
<option value="5,20">Napa Valley Cabernet</option>
<option value="5,20">Northern Rh&ocirc;ne Syrah</option>
<option value="8,25">Rioja Gran Reserva</option>
<option value="5,15">Chianti Classico Riserva</option>
<option value="3,10">White Burgundy</option>
<option value="3,20">German Riesling (Kabinett / Sp&auml;tlese)</option>
<option value="8,20">Vintage Champagne</option>
<option value="15,40">Vintage Port</option>
<option value="1,5">Everyday red</option>
<option value="0,2">Everyday white / ros&eacute;</option>
</select></div>
<div class="field"><label for="vintage">Vintage</label><input type="number" id="vintage" value="2019" min="1900" max="2100" inputmode="numeric"></div>
</div>
<div class="result"><div class="big" id="out">&mdash;</div><div class="sub" id="outsub"></div></div>
<p class="note">Windows are broad guides for well-made, well-stored examples of each style — producer, vintage quality and storage all shift them.</p>""",
    calc_js="""function $(i){return document.getElementById(i)}
function calc(){
var v=parseInt($('vintage').value,10);
if(isNaN(v)||v<1900||v>2100){$('out').innerHTML='&mdash;';$('outsub').textContent='Enter a vintage year.';return}
var p=$('style').value.split(','),a=v+ +p[0],b=v+ +p[1];
var now=new Date().getFullYear();
$('out').textContent='Drink '+a+' \\u2013 '+b;
var third=(b-a)/3;
if(now<a){$('outsub').textContent='Still ageing — about '+(a-now)+' more year'+(a-now===1?'':'s')+' before the window opens.'}
else if(now<=b){
if(now>=a+third&&now<=b-third){$('outsub').textContent='In its drink window and around its likely peak. A very good time to open one.'}
else if(now<a+third){$('outsub').textContent='The window has just opened — drinking well now, and should improve further.'}
else{$('outsub').textContent='In its window but on the later slope — drink sooner rather than later.'}}
else{$('outsub').textContent='Past its likely window. It may still be enjoyable, but expect faded fruit — open it with modest expectations.'}}""",
    explainer="""<section>
<h2>What a drink window is</h2>
<p>A drink window is the stretch of years when a wine is likely to show at its best — after harsh youthful tannin and raw oak have softened, and before fruit fades and oxidation takes over. Wines built for ageing follow an arc: tight and primary young, then open and layered through the middle of the window, then gradually drier and more fragile at the end.</p>
<h2>What sets the window</h2>
<p>Structure does. Tannin, acidity, sugar and alcohol are preservatives, which is why a Barolo or a classed-growth Bordeaux can improve for two decades while most supermarket reds are at their best within a year or two of release. Sweet and fortified wines stretch furthest of all — vintage Port is often barely ready at fifteen years. Within a style, the producer and the vintage matter enormously: a great year adds years to the window, a weak one shortens it, and a light producer&rsquo;s wine will always drink earlier than a blockbuster&rsquo;s.</p>
<h2>Using the estimate well</h2>
<p>Treat the window as a planning tool, not a countdown. If you own several bottles of the same wine, open them across the window — one early, one at the projected peak — and let the wine tell you how it is evolving; that is far more reliable than any table. Storage is the silent variable: these ranges assume a cool, dark, stable spot around 12–14&nbsp;&deg;C. A bottle kept warm ages measurably faster, so shorten the window for anything stored in a kitchen.</p>
</section>""",
    app_block=cellar_block("wine_drink_window", ppid=CELLAR_TONIGHT_SHELF_PPID),
    depth="""<section>
<h2>How it works</h2>
<p>Each style in the list carries two numbers: how many years after the vintage its window usually opens, and how many years after the vintage it usually closes. Barolo and Barbaresco run from eight to twenty-five years, classed-growth Bordeaux from eight to thirty, red Burgundy from four to twelve, vintage Port from fifteen to forty, and an everyday white or ros&eacute; from the vintage year itself to two years on. Add both offsets to your vintage and you have the window.</p>
<p>The calculator then sets that window against the current year. Before it opens, you get the number of years still to wait. Inside it, the window is divided into thirds: the first third reads as just opened and still improving, the middle third as around the likely peak, and the final third as the later slope. Once the closing year has passed, the wine is marked as past its likely window.</p>
<h2>A worked example</h2>
<p>Take a 2016 Barolo, checked in 2026.</p>
<table class="worked">
<tr><td>Style offsets (Barolo / Barbaresco)</td><td>8 to 25 years</td></tr>
<tr><td>Window (2016 + 8, 2016 + 25)</td><td>Drink 2024 &ndash; 2041</td></tr>
<tr><td>One third of the window (17 &divide; 3)</td><td>about 5.7 years</td></tr>
<tr><td>Just opened</td><td>2024&ndash;2029</td></tr>
<tr><td>Around its likely peak</td><td>2030&ndash;2035</td></tr>
<tr><td>Later slope</td><td>2036&ndash;2041</td></tr>
<tr><td>Verdict for 2026</td><td>The window has just opened &mdash; drinking well now, and should improve further.</td></tr>
</table>
<p>Two years into a seventeen-year window, the wine is approachable but not yet at its best on these numbers; the middle stretch begins in 2030. The estimate knows nothing about the producer or how the 2016 growing season went in Piedmont, so if you hold several bottles, opening one now is the most reliable way to judge when to open the rest.</p>
</section>""",
    faqs=[
        ("When should I drink my wine?",
         "Most wine is made to be enjoyed within a year or two of release, and keeping it longer gains nothing. Only wines with real structure &mdash; firm tannin, high acidity, sweetness or fortification &mdash; improve with age. For those, the middle of the drink window is the safest bet, while the early years favour fresh fruit and the later years favour softer, more savoury flavours."),
        ("How long can you keep a bottle of red wine?",
         "It depends almost entirely on the style. The calculator gives an everyday red one to five years from the vintage and an everyday Bordeaux three to ten, while a classed-growth Bordeaux runs to thirty and vintage Port to forty. Those figures assume a well-made example kept somewhere cool, dark and steady; poorer storage shortens every one of them."),
        ("How can I tell if a wine is past its best?",
         "Colour is the first clue: reds fade towards brick and brown at the rim, and whites deepen to gold or amber. On the nose and palate, fresh fruit gives way to dried fruit and nutty, sherry-like notes, and the acidity starts to stand out on its own. A wine in that state is rarely harmful, just flat &mdash; taste it before deciding to pour it away."),
        ("Is it better to open a wine early or late in its window?",
         "Neither is wrong; it is a matter of taste. Early in the window a wine shows more primary fruit and firmer tannin. Later it trades fruit for secondary flavours such as leather, earth and dried herbs, with a softer texture. If you are unsure which you prefer, the middle third &mdash; what the calculator calls the likely peak &mdash; balances the two."),
        ("How should I store wine I want to age?",
         "Somewhere cool, dark and stable, ideally around 12&ndash;14&nbsp;&deg;C, away from strong light and vibration. Steadiness matters as much as the exact figure, since repeated warming and cooling ages a wine faster. Bottles sealed with cork are traditionally kept on their side so the cork stays in contact with the wine and does not dry out."),
    ],
))

PAGES.append(dict(
    slug="plant-watering-calculator",
    palette="leaflet",
    tab_title="Plant Watering Calculator — Free & Instant | Eritech Studios",
    og_title="Plant Watering Calculator",
    meta_desc="How often to water a Monstera, Pothos, snake plant and more — interval estimates by species, season and light. Free, no signup.",
    h1="Plant Watering Calculator",
    lede="A starting interval for your plant, adjusted for the season and the light it actually gets.",
    calc_html="""<div class="field"><label for="species">Plant</label>
<select id="species">
<option value="7,10" selected>Monstera deliciosa</option>
<option value="7,10">Pothos</option>
<option value="14,21">Snake plant (Sansevieria)</option>
<option value="14,21">ZZ plant</option>
<option value="7,10">Fiddle leaf fig</option>
<option value="7,10">Pilea peperomioides</option>
<option value="5,7">Alocasia</option>
<option value="5,7">Calathea / prayer plant</option>
<option value="5,7">Peace lily</option>
<option value="7,10">Spider plant</option>
<option value="14,28">Succulents &amp; cacti</option>
<option value="3,5">Ferns</option>
</select></div>
<div class="row">
<div class="field"><label for="season">Season</label>
<select id="season">
<option value="1" selected>Spring / summer (growing)</option>
<option value="1.3">Autumn</option>
<option value="1.6">Winter (dormant)</option>
</select></div>
<div class="field"><label for="light">Light</label>
<select id="light">
<option value="0.8">Bright, near a window</option>
<option value="1" selected>Medium, a few metres in</option>
<option value="1.3">Low light</option>
</select></div>
</div>
<div class="result"><div class="big" id="out">&mdash;</div><div class="sub" id="outsub"></div></div>
<p class="note">Always confirm with the soil: water when the top 2–5&nbsp;cm is dry, whatever the calendar says.</p>""",
    calc_js="""function $(i){return document.getElementById(i)}
function calc(){
var p=$('species').value.split(','),s=parseFloat($('season').value),l=parseFloat($('light').value);
var lo=Math.round(p[0]*s*l),hi=Math.round(p[1]*s*l);
if(lo<1)lo=1;if(hi<=lo)hi=lo+1;
$('out').textContent='Every '+lo+'\\u2013'+hi+' days';
$('outsub').textContent='A starting point, not a rule — check the soil before each watering and let the top few centimetres dry out first.'}""",
    explainer="""<section>
<h2>Why there is no fixed schedule</h2>
<p>&ldquo;Water once a week&rdquo; is the most common houseplant advice and the most common cause of dead houseplants. A plant&rsquo;s thirst depends on how much light it gets, how warm and dry the room is, the size and material of the pot, and how fast it is growing — the same Monstera might want water every six days in a bright July window and every three weeks in a dim December corner. An interval is only ever a starting point.</p>
<h2>Reading the signals</h2>
<p>The soil is the real schedule. Push a finger 2–5&nbsp;cm into the pot: for most tropical foliage plants, water when that depth is dry; for succulents, cacti, snake plants and ZZ plants, wait until the pot is dry throughout. Lifting the pot works too — a dry pot is startlingly light. When you do water, water thoroughly until it runs from the drainage holes, then empty the saucer. Frequent little sips keep the surface wet and the roots thirsty.</p>
<h2>Overwatering kills more than drought</h2>
<p>Most houseplants tolerate going a little too dry: leaves droop, you water, they recover. Constantly wet soil is different — it suffocates roots and invites rot, which is usually fatal by the time it shows. Yellowing lower leaves on damp soil mean water less, not more. In autumn and winter, growth slows and drying takes far longer, so stretch every interval; almost everything on this list wants a drier, calmer off-season than its summer routine.</p>
</section>""",
    app_block=leaflet_block("plant_watering", built=False),
    depth="""<section>
<h2>How it works</h2>
<p>Each plant starts from a base range in days, meant for the growing season in medium light: 7&ndash;10 days for Monstera, Pothos, fiddle leaf fig, Pilea and spider plant; 5&ndash;7 for Alocasia, Calathea and peace lily; 3&ndash;5 for ferns; 14&ndash;21 for snake plants and ZZ plants; and 14&ndash;28 for succulents and cacti.</p>
<p>Both ends of that range are then multiplied by a season factor and a light factor. Spring and summer leave the range as it is, autumn stretches it by &times;1.3 and winter by &times;1.6. Bright light near a window shortens it to &times;0.8, medium light leaves it alone, and low light stretches it by &times;1.3 &mdash; a plant in good light grows faster and uses water sooner. Each end is rounded to the nearest whole day, the lower figure never drops below one day, and the upper figure always sits at least a day above the lower.</p>
<h2>A worked example</h2>
<p>A Monstera in a dim spot, in the middle of winter.</p>
<table class="worked">
<tr><td>Plant</td><td>Monstera deliciosa, 7&ndash;10 days</td></tr>
<tr><td>Season</td><td>Winter (dormant), &times;1.6</td></tr>
<tr><td>Light</td><td>Low light, &times;1.3</td></tr>
<tr><td>Combined factor (1.6 &times; 1.3)</td><td>&times;2.08</td></tr>
<tr><td>Lower end (7 &times; 2.08 = 14.56)</td><td>15 days</td></tr>
<tr><td>Upper end (10 &times; 2.08 = 20.8)</td><td>21 days</td></tr>
<tr><td>Result</td><td>Every 15&ndash;21 days</td></tr>
</table>
<p>Move the same plant to a bright window in summer and the range falls to every 6&ndash;8 days &mdash; nearly three times as often. Read the winter figure as the point to start checking rather than the day to water: if the top 2&ndash;5&nbsp;cm of soil is still damp at fifteen days, leave it and check again in a few days.</p>
</section>""",
    faqs=[
        ("How often should I water a Monstera?",
         "As a starting point, every 7&ndash;10 days in spring and summer in medium light, every 6&ndash;8 days in a bright window, and as little as every 15&ndash;21 days in a dim room in winter. The soil has the final say: water when the top 2&ndash;5&nbsp;cm is dry, water thoroughly until it runs from the drainage holes, then empty the saucer."),
        ("How often should I water a snake plant?",
         "Less often than almost anything else on the list. The calculator starts at every 14&ndash;21 days in the growing season in medium light, stretching to roughly every 29&ndash;44 days in winter in low light. Snake plants store water in their leaves and rot easily, so wait until the pot is dry all the way through, not just at the surface."),
        ("Should I water houseplants less in winter?",
         "Yes, for almost all of them. Shorter days mean slower growth, so the soil takes much longer to dry and the same routine that suited summer leaves roots sitting wet. The exception is a pot close to a radiator, which can dry out faster than you would expect &mdash; one more reason to check the soil rather than follow the calendar."),
        ("How do I know if I am overwatering a plant?",
         "Yellowing lower leaves while the soil is still damp are the classic sign. Others include a sour or musty smell from the pot, soft or darkening stems at the base, fungus gnats hovering over the surface, and a plant that wilts even though the soil is wet &mdash; which usually means the roots are already damaged. Let the pot dry out well before watering again."),
        ("Does the pot change how often I need to water?",
         "Considerably, and the calculator does not account for it. Unglazed terracotta is porous and dries faster than plastic or glazed ceramic; a small pot dries faster than a large one; and a pot without drainage holes holds water at the bottom where you cannot see it. Adjust the interval for your own pots and let the soil guide you."),
    ],
))

PAGES.append(dict(
    slug="uk-return-rights-checker",
    palette="warranty",
    tab_title="UK Return Rights Checker — Free & Instant | Eritech Studios",
    og_title="UK Return Rights Checker",
    meta_desc="Check your UK rights to return or get a refund — the 14-day online cooling-off period and the Consumer Rights Act windows for faulty goods. Free, no signup.",
    h1="UK Return Rights Checker",
    lede="Enter when and where you bought, and see which legal window you&rsquo;re in right now.",
    calc_html="""<div class="row">
<div class="field"><label for="bought">Purchase / delivery date</label><input type="date" id="bought"></div>
<div class="field"><label for="channel">Bought</label>
<select id="channel">
<option value="online" selected>Online / at a distance</option>
<option value="store">In store</option>
</select></div>
</div>
<div class="field"><label for="reason">Why are you returning it?</label>
<select id="reason">
<option value="mind" selected>Changed my mind</option>
<option value="fault">It&rsquo;s faulty / not as described</option>
</select></div>
<div class="result"><div class="big" id="out">&mdash;</div><div class="sub" id="outsub"></div></div>
<p class="note">General information for England, Wales and Northern Ireland (Scotland differs slightly on final time limits) — not legal advice. Some goods, e.g. perishables and personalised items, are excluded from the cooling-off right.</p>""",
    calc_js="""function $(i){return document.getElementById(i)}
function fmt(d){return d.toLocaleDateString(undefined,{day:'numeric',month:'short',year:'numeric'})}
function calc(){
var v=$('bought').value;
if(!v){$('out').innerHTML='&mdash;';$('outsub').textContent='Pick your purchase or delivery date.';return}
var d=new Date(v+'T00:00:00'),now=new Date();
var days=Math.floor((now-d)/86400000);
if(days<0){$('out').textContent='Future date';$('outsub').textContent='That date has not happened yet.';return}
var ch=$('channel').value,re=$('reason').value;
if(re==='mind'){
if(ch==='online'){
var dl=new Date(d.getTime()+14*86400000);
if(days<=14){$('out').textContent='You can still cancel';
$('outsub').textContent='Under the Consumer Contracts Regulations you have 14 days from delivery to tell the seller you are cancelling — until '+fmt(dl)+' — and then 14 more days to send the goods back. Day '+days+' of 14.'}
else{$('out').textContent='Cooling-off period over';
$('outsub').textContent='The 14-day cancellation right ended on '+fmt(dl)+'. You are now relying on the store&rsquo;s own returns policy — many allow 28+ days as goodwill.'}}
else{$('out').textContent='No automatic right';
$('outsub').textContent='For in-store purchases there is no legal right to return unwanted goods. Check the store&rsquo;s returns policy — most offer one voluntarily, so a receipt and original condition are your best friends.'}}
else{
if(days<=30){$('out').textContent='Short-term right to reject — day '+days+' of 30';
$('outsub').textContent='Under the Consumer Rights Act 2015 you can reject faulty goods within 30 days for a full refund. Contact the retailer (not the manufacturer) now.'}
else if(days<=182){$('out').textContent='Repair or replacement window';
$('outsub').textContent='Within 6 months of purchase the retailer must repair or replace faulty goods, and the law assumes the fault existed at purchase — it is on them to prove otherwise. If one repair fails, you can claim a refund (possibly partly reduced for use).'}
else{$('out').textContent='Late-stage claim';
$('outsub').textContent='You can still pursue a remedy for up to 6 years from purchase (5 years from discovery in Scotland), but the burden of proof now sits with you — you may need evidence the fault was inherent, such as an independent report.'}}}""",
    explainer="""<section>
<h2>Two different laws, two different clocks</h2>
<p>UK return rights come from two places, and mixing them up is the most common mistake. If you simply changed your mind, the <strong>Consumer Contracts Regulations 2013</strong> apply — but only to online, phone and mail-order purchases. You get 14 days from delivery to cancel for any reason, then 14 more to return the goods. Buy the same item in a shop and no such right exists at all: in-store returns of unwanted goods are pure store policy, which is why keeping the receipt matters.</p>
<h2>Faulty goods are much stronger ground</h2>
<p>The <strong>Consumer Rights Act 2015</strong> says goods must be of satisfactory quality, fit for purpose and as described — bought anywhere. In the first 30 days you can reject a faulty item outright for a full refund. From 30 days to six months, the retailer gets one chance at a repair or replacement, and crucially the law presumes the fault was there when you bought it. After six months you can still claim for up to six years, but the burden of proof flips to you.</p>
<h2>Practicalities that decide cases</h2>
<p>Your contract is always with the retailer, not the manufacturer — do not let a shop redirect you to a warranty line to escape its legal obligations. A manufacturer&rsquo;s warranty is a bonus on top of these rights, never a replacement for them. And every route — rejection, repair, warranty claim — depends on proving when and where you bought the thing, which is exactly the paperwork that vanishes when you need it most. Keep receipts, keep serial numbers, and note the dates.</p>
</section>""",
    app_block=warranty_block("uk_returns"),
    depth="""<section>
<h2>How it works</h2>
<p>The checker counts the days since your purchase or delivery date, then applies the rule that fits how you bought and why you are returning. If you changed your mind about something bought online, by phone or by mail order, you are inside the cooling-off period for 14 days from delivery, and then have a further 14 days to send the goods back. If you bought it in a shop, there is no legal right to return unwanted goods, so it points you to the shop&rsquo;s own policy.</p>
<p>If the item is faulty, it uses the Consumer Rights Act 2015 stages: up to 30 days, the short-term right to reject for a full refund; up to six months, repair or replacement, with the fault presumed to have been there from the start; after that, a claim is still possible for up to six years (five in Scotland), but you need to show the fault was there when you bought it.</p>
<h2>Worked examples</h2>
<table class="worked">
<tr><td>Bought online, changed my mind, delivered 9 days ago</td><td>You can still cancel &mdash; day 9 of 14</td></tr>
<tr><td>Bought in a shop, changed my mind</td><td>No automatic right &mdash; store policy</td></tr>
<tr><td>Faulty, bought 20 days ago</td><td>Short-term right to reject</td></tr>
<tr><td>Faulty, bought 50 days ago</td><td>Repair or replacement window</td></tr>
<tr><td>Faulty, bought eight months ago</td><td>Late-stage claim &mdash; proof on you</td></tr>
</table>
<p>The same fault can therefore mean a straight refund, a repair, or an argument about evidence, depending only on the date. That is why the purchase date and proof of where you bought are worth keeping for everything that costs real money.</p>
<p class="note">General information about consumer law in the UK, not legal advice. For help with a specific problem, contact <a href="https://www.citizensadvice.org.uk/consumer/" rel="noopener">Citizens Advice</a>.</p>
</section>""",
    faqs=[
        ("How long do I have to return something bought online in the UK?",
         "Under the Consumer Contracts Regulations 2013 you have 14 days from delivery to tell the seller you want to cancel, and then another 14 days to send the goods back. The right covers most goods bought online, by phone or by mail order, but some are excluded &mdash; including perishable goods, personalised items, and sealed hygiene products once unsealed."),
        ("Can I return something to a shop because I changed my mind?",
         "Not as a legal right. For goods bought in person, returning something you simply do not want depends entirely on the shop&rsquo;s own returns policy. Most shops offer one, often with conditions, so keep the receipt and the item in its original condition until you are sure."),
        ("What are my rights if something I bought is faulty?",
         "Under the Consumer Rights Act 2015, goods must be of satisfactory quality, fit for purpose and as described, wherever you bought them. Within 30 days you can reject a faulty item for a full refund. After that, the retailer normally gets one chance to repair or replace it before you can ask for a refund or a price reduction."),
        ("Do I need a receipt to return a faulty item?",
         "You need proof of purchase, but it does not have to be the till receipt. A bank or card statement, an order confirmation or a similar record showing when and where you bought the item is usually enough."),
        ("Should I contact the retailer or the manufacturer?",
         "The retailer. Your contract is with the seller, so your statutory rights are against them, not the manufacturer. A manufacturer&rsquo;s warranty is an extra you can use alongside those rights, never a replacement for them."),
        ("Are the rules different in Scotland?",
         "The consumer rights themselves are the same across the UK. What differs is the time limit for pursuing a claim: generally up to six years in England, Wales and Northern Ireland, and five years in Scotland."),
    ],
))

PAGES.append(dict(
    slug="packing-list-generator",
    palette="travelbinder",
    tab_title="Packing List Generator — Free & Instant | Eritech Studios",
    og_title="Packing List Generator",
    meta_desc="Generate a packing list from your trip length, climate and style — with quantities worked out for you. Free, no signup.",
    h1="Packing List Generator",
    lede="Trip length, climate and style in &mdash; a categorised list with actual quantities out.",
    extra_css=""".plist{display:grid;grid-template-columns:1fr 1fr;gap:16px 24px;margin-top:16px}
.plist h4{margin:0 0 5px;font-family:Georgia,"Times New Roman",serif;font-size:.95rem;color:var(--accent)}
.plist ul{list-style:none;padding:0;margin:0}
.plist li{font-size:.88rem;padding:2px 0 2px 16px;position:relative;line-height:1.5}
.plist li:before{content:"";position:absolute;left:0;top:9px;width:7px;height:7px;border:1px solid var(--muted);border-radius:2px}
@media(max-width:540px){.plist{grid-template-columns:1fr}}
""",
    calc_html="""<div class="row">
<div class="field"><label for="nights">Trip length (nights)</label><input type="number" id="nights" value="14" min="1" max="90" inputmode="numeric"></div>
<div class="field"><label for="climate">Climate at destination</label>
<select id="climate">
<option value="freezing">Freezing &mdash; below 0&deg;C</option>
<option value="cold" selected>Cold &mdash; 0&ndash;10&deg;C (Japan in December)</option>
<option value="mild">Mild &mdash; 10&ndash;18&deg;C</option>
<option value="warm">Warm &mdash; 18&ndash;26&deg;C</option>
<option value="hot">Hot and humid &mdash; above 26&deg;C</option>
</select></div>
</div>
<div class="row">
<div class="field"><label for="style">Trip style</label>
<select id="style">
<option value="city" selected>City / sightseeing</option>
<option value="outdoors">Hiking / outdoors</option>
<option value="beach">Beach</option>
<option value="business">Business</option>
</select></div>
<div class="field"><label for="laundry">Laundry access</label>
<select id="laundry"><option value="yes" selected>Yes &mdash; hotel or coin laundry</option><option value="no">No</option></select></div>
<div class="field"><label for="bag">Luggage</label>
<select id="bag"><option value="checked" selected>Checked bag</option><option value="carry">Carry-on only</option></select></div>
</div>
<div class="result"><div class="big" id="out">&mdash;</div><div class="sub" id="outsub"></div>
<div class="plist" id="list"></div></div>
<p class="note">Quantities assume you re-wear outer layers and wash base layers. It is a starting list, not a rule.</p>""",
    calc_js="""function $(i){return document.getElementById(i)}
function num(i){var v=parseFloat($(i).value);return isNaN(v)?0:v}
var CLIMATE={
freezing:{label:'freezing',layers:['Thermal base layers &times;2','Insulated coat','Fleece or mid layer','Wool hat, gloves and scarf','Thick socks &times;3','Waterproof boots']},
cold:{label:'cold',layers:['Warm coat','Jumper or fleece &times;2','Thermal top &times;1','Hat and gloves','Scarf','Water-resistant shoes']},
mild:{label:'mild',layers:['Light jacket','Jumper &times;1','Packable rain shell','Comfortable walking shoes']},
warm:{label:'warm',layers:['Light overshirt or cardigan','Packable rain shell','Sunglasses','Sun hat']},
hot:{label:'hot and humid',layers:['Linen overshirt','Packable rain shell','Sunglasses','Sun hat','Quick-dry towel']}};
var STYLE={
city:['Day bag or small backpack','Walking shoes, already worn in','Compact umbrella','Portable battery'],
outdoors:['Hiking boots','Daypack 20&ndash;30L','Water bottle','Blister plasters','Head torch','Dry bag'],
beach:['Swimwear &times;2','Quick-dry towel','Flip flops','Reef-safe sun cream','After-sun'],
business:['Suit or smart outfit','Dress shoes','Laptop and charger','Wrinkle spray or travel steamer']};
function calc(){
var nights=Math.max(1,Math.round(num('nights')));
var c=CLIMATE[$('climate').value],st=$('style').value;
var laundry=$('laundry').value==='yes',carry=$('bag').value==='carry';
var wear=laundry?Math.min(nights,7):Math.min(nights,14);
var socks=Math.min(wear+1,15),tops=Math.max(2,Math.min(wear,10)),bottoms=Math.max(1,Math.min(Math.ceil(wear/4),4));
if(carry){tops=Math.min(tops,6);bottoms=Math.min(bottoms,2);socks=Math.min(socks,8)}
var sleep=nights>7?2:1;
var groups=[
['Clothing',['Underwear &times;'+socks,'Socks &times;'+socks,'Tops &times;'+tops,'Trousers or skirts &times;'+bottoms,'Sleepwear &times;'+sleep]],
['Layers and outerwear',c.layers],
['Toiletries',['Toothbrush and paste','Deodorant','Shampoo and shower gel'+(carry?' (&le;100 ml)':''),'Razor','Prescriptions in original packaging','Painkillers and plasters']],
['Tech',['Phone and charger','Plug adapter for the destination','Portable battery','Headphones','Spare cable']],
['Documents and money',['Passport, 6+ months validity','Visa or entry registration if required','Travel insurance details','Two cards, carried separately','Some local cash','Offline copies of every booking']],
['For this trip',STYLE[st]]];
var total=0,html='';
groups.forEach(function(g){total+=g[1].length;
html+='<div><h4>'+g[0]+'</h4><ul>';
g[1].forEach(function(i){html+='<li>'+i+'</li>'});
html+='</ul></div>'});
$('list').innerHTML=html;
$('out').textContent=total+' items to pack';
$('outsub').textContent=nights+' nights, '+c.label+' weather, '+(laundry?'laundry available':'no laundry')+(carry?', carry-on only.':'.')}""",
    explainer="""<section>
<h2>Why quantities matter more than the list</h2>
<p>Most packing lists tell you to bring socks. The useful question is how many, and the honest answer depends on one thing above all others: whether you can wash anything. With access to a hotel or coin laundry, almost nobody needs more than about a week of clothing regardless of how long the trip is &mdash; a three-week trip and a seven-day trip pack identically. Without laundry, the count really does scale with the nights, and that is where suitcases get heavy.</p>
<h2>Layers beat garments</h2>
<p>For anything cooler than about 18&nbsp;&deg;C, what keeps you comfortable is the number of layers rather than the thickness of any single item. A thermal base, a jumper and a windproof coat cover a much wider temperature range than one heavy parka, and they pack smaller. Japan in December is the classic case: daytime Tokyo sits around 10&nbsp;&deg;C, but you will alternate between cold streets and aggressively heated trains, shops and restaurants all day. Being able to shed a layer matters more than the coat being warm.</p>
<h2>Carry-on only changes the maths</h2>
<p>Cabin-only travel is less about ruthless minimalism than about two specific constraints: liquids must fit the 100&nbsp;ml rule, and your bulkiest items &mdash; boots, coat &mdash; get worn onto the plane rather than packed. Once those are handled, a week of clothing fits comfortably in a 40&nbsp;L bag, and laundry covers the rest of any trip length.</p>
<h2>The part people actually forget</h2>
<p>It is rarely clothing. It is the plug adapter, the second payment card kept somewhere separate from the first, prescriptions in their original labelled packaging for border checks, and offline copies of every booking &mdash; because the one moment you cannot rely on having signal or battery is the moment you land. Screenshot or download your confirmations before you leave, and keep them somewhere that works in aeroplane mode.</p>
</section>""",
    app_block=travelbinder_block("packing_list"),
    depth="""<section>
<h2>How it works</h2>
<p>Everything in the clothing section flows from one figure: the number of days you need to dress for before you can wash. With laundry access that is your number of nights, capped at seven; without it, the cap rises to fourteen. Underwear and socks are one more than that figure, up to 15. Tops are one per day, never fewer than 2 or more than 10. Trousers or skirts are one per four days, rounded up, between 1 and 4. Sleepwear is 2 for trips over seven nights, otherwise 1.</p>
<p>Carry-on only then caps tops at 6, trousers or skirts at 2 and underwear and socks at 8, and marks toiletries as 100&nbsp;ml or less. The climate picks the layers and outerwear &mdash; thermal base layers, an insulated coat and waterproof boots when freezing; a linen overshirt, sun hat and quick-dry towel when hot and humid. The trip style adds its own short list, such as a 20&ndash;30&nbsp;L daypack and head torch for hiking, or a suit and dress shoes for business. Toiletries, tech and documents are the same for every trip. The headline figure counts lines on the list, not individual garments.</p>
<h2>A worked example</h2>
<p>Fourteen nights of city sightseeing in cold weather, with laundry and a checked bag.</p>
<table class="worked">
<tr><td>Days of clothing (14 nights, capped at 7)</td><td>7</td></tr>
<tr><td>Underwear</td><td>&times;8</td></tr>
<tr><td>Socks</td><td>&times;8</td></tr>
<tr><td>Tops</td><td>&times;7</td></tr>
<tr><td>Trousers or skirts</td><td>&times;2</td></tr>
<tr><td>Sleepwear</td><td>&times;2</td></tr>
<tr><td>Jumper or fleece</td><td>&times;2</td></tr>
<tr><td>Thermal top</td><td>&times;1</td></tr>
<tr><td>Total</td><td>32 items to pack</td></tr>
</table>
<p>Take laundry away and the same fortnight needs underwear and socks &times;15, tops &times;10 and trousers or skirts &times;4 &mdash; nearly double the clothing. Keep no laundry but switch to carry-on only, and the caps bring it back to &times;8, &times;6 and &times;2, which in practice means planning to wash in a sink. The headline stays at 32 in all three cases, because only the quantities change.</p>
</section>""",
    faqs=[
        ("What should I pack for a two-week trip?",
         "If you can do laundry, about a week of clothing: for fourteen nights the generator suggests eight each of underwear and socks, seven tops, two pairs of trousers or skirts and two sets of sleepwear, plus layers for the climate. Add the essentials that do not scale with length &mdash; passport, two separate cards, prescriptions, adapter &mdash; and wash once halfway through."),
        ("How many pairs of socks should I pack?",
         "One pair for each day until you can next wash, plus a spare. With laundry access the generator stops at eight pairs however long the trip; without it, the count is one per night plus a spare, up to fifteen. For carry-on only it caps at eight either way. In freezing weather it also adds three pairs of thick socks to the layers."),
        ("Should I pack more clothes for a longer trip?",
         "Only if you cannot wash them. With laundry the clothing count is the same from seven nights upwards &mdash; a ten-night trip and a thirty-night trip pack the same number of tops and socks. Without laundry the list grows with the nights until fourteen days, then levels off, because beyond a fortnight you will be washing something whatever you planned."),
        ("How do I pack for cold weather without overpacking?",
         "Pack layers rather than bulk. For 0&ndash;10&nbsp;&deg;C the generator suggests a warm coat, two jumpers or fleeces, a thermal top, hat, gloves and scarf &mdash; pieces that combine for cold streets and come off in heated shops and trains. Wear the coat and heaviest shoes on the journey, so they take no space in the bag."),
        ("Can I travel for two weeks with only carry-on luggage?",
         "Usually, provided you can wash clothes along the way. The generator caps a carry-on list at six tops, two pairs of trousers or skirts and eight each of underwear and socks, and marks toiletries as 100&nbsp;ml or less. Size, weight and liquids allowances vary by airline and airport, so check yours before you pack rather than relying on a general figure."),
    ],
))

PAGES.append(dict(
    slug="japan-trip-cost-calculator",
    palette="travelbinder",
    tab_title="Japan Trip Cost Calculator — Free & Instant | Eritech Studios",
    og_title="Japan Trip Cost Calculator",
    meta_desc="Estimate what a trip to Japan costs — accommodation, food, transport, JR Pass and flights, broken down per day and per person. Free, no signup.",
    h1="Japan Trip Cost Calculator",
    lede="What does two weeks in Japan actually cost? Set your length and style for a line-by-line estimate.",
    extra_css=""".result td:nth-child(2),.result td:nth-child(3){text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
.result td:nth-child(2){color:var(--muted);padding-right:16px}
.result td:first-child{padding-right:12px}
.result .sub{margin-top:12px}
""",
    calc_html="""<div class="row">
<div class="field"><label for="nights">Nights in Japan</label><input type="number" id="nights" value="14" min="1" max="90" inputmode="numeric"></div>
<div class="field"><label for="people">Travellers</label><input type="number" id="people" value="2" min="1" max="6" inputmode="numeric"></div>
</div>
<div class="field"><label for="style">Travel style</label>
<select id="style">
<option value="budget">Budget &mdash; hostels and business hotels, convenience stores and cheap eats</option>
<option value="mid" selected>Mid-range &mdash; three-star hotels, restaurants, the occasional taxi</option>
<option value="comfort">Comfort &mdash; four-star hotels and ryokan, sit-down dining</option>
</select></div>
<div class="row">
<div class="field"><label for="pass">JR Pass, per person</label>
<select id="pass">
<option value="0" selected>None &mdash; pay per journey</option>
<option value="50000">7-day ordinary</option>
<option value="80000">14-day ordinary</option>
<option value="100000">21-day ordinary</option>
</select></div>
<div class="field"><label for="flight">Return flights each (&pound;)</label><input type="number" id="flight" value="750" min="0" inputmode="numeric"></div>
<div class="field"><label for="rate">Rate (&yen; per &pound;)</label><input type="number" id="rate" value="190" min="1" inputmode="decimal"></div>
</div>
<div class="result"><table id="tbl"></table><div class="sub" id="outsub"></div></div>
<p class="note">Planning estimates, not quotes. The exchange-rate field is editable &mdash; check today&rsquo;s rate before you rely on the pound figures.</p>""",
    calc_js="""function $(i){return document.getElementById(i)}
function num(i){var v=parseFloat($(i).value);return isNaN(v)?0:v}
var STYLE={budget:{stay:7000,food:3000,local:800,act:1000},
mid:{stay:15000,food:6500,local:1200,act:2200},
comfort:{stay:32000,food:13000,local:1800,act:4000}};
function calc(){
var nights=Math.max(1,Math.round(num('nights'))),people=Math.max(1,Math.round(num('people')));
var s=STYLE[$('style').value],rate=num('rate')||190;
var days=nights+1,rooms=Math.ceil(people/2);
var stay=s.stay*rooms*nights,food=s.food*people*days,local=s.local*people*days,act=s.act*people*days;
var pass=num('pass')*people,flights=num('flight')*people*rate;
var total=stay+food+local+act+pass+flights;
function row(l,y){return '<tr><td>'+l+'</td><td>&yen;'+Math.round(y).toLocaleString()+'</td><td>&pound;'+Math.round(y/rate).toLocaleString()+'</td></tr>'}
var h=row('Accommodation &mdash; '+rooms+(rooms===1?' room':' rooms')+' &times; '+nights+' nights',stay)+
row('Food and drink',food)+row('Local transport',local)+row('Activities and entry fees',act);
if(pass>0)h+=row('JR Pass &times;'+people,pass);
if(flights>0)h+=row('Return flights &times;'+people,flights);
h+=row('Total',total);
$('tbl').innerHTML=h;
var onTheGround=total-flights;
$('outsub').textContent='About \\u00a3'+Math.round(total/people/rate).toLocaleString()+' per person all in, or \\u00a3'+Math.round(onTheGround/people/days/rate).toLocaleString()+' per person per day once you are there.'}""",
    explainer="""<section>
<h2>Where the money actually goes</h2>
<p>Japan has a reputation for being eye-wateringly expensive that the daily numbers do not really support. Food in particular is a bargain relative to western Europe: a bowl of ramen or a convenience-store breakfast costs a fraction of the London equivalent, and even a good sit-down dinner rarely matches a comparable meal at home. What does cost money is accommodation, which typically accounts for close to half of on-the-ground spending, and long-distance rail. Those two lines are where your travel style shows up; the rest moves surprisingly little between budget and comfort trips.</p>
<h2>The JR Pass is no longer automatic</h2>
<p>For years the advice was simple &mdash; buy the Japan Rail Pass, always. The October 2023 price rise changed that, taking the seven-day ordinary pass to &yen;50,000. It now only pays for itself if you are covering serious distance: as a rough test, a Tokyo&ndash;Kyoto return alone runs roughly &yen;28,000, so a pass makes sense on a Tokyo&ndash;Kyoto&ndash;Hiroshima-style itinerary and rarely does if you are basing yourself in one or two cities. Price your actual planned journeys individually before buying, rather than assuming. Regional passes are often the better answer.</p>
<h2>What this estimate leaves out</h2>
<p>Shopping, which in Japan has a way of expanding to fill whatever space you leave it. Also travel insurance, any domestic flights, and one-off splurges such as a kaiseki dinner or a night in a high-end ryokan &mdash; a single ryokan stay with dinner and breakfast can equal three ordinary hotel nights. Budget those separately rather than trying to average them into a daily figure.</p>
<h2>Using the number</h2>
<p>Treat the daily rate as your planning anchor and the total as a target to test against. If the figure comes out higher than you would like, accommodation is almost always the most effective lever &mdash; moving from mid-range hotels to business hotels changes the total far more than eating more cheaply ever will, and business hotels in Japan are clean, well-located and perfectly pleasant.</p>
</section>""",
    app_block=travelbinder_block("japan_trip_cost"),
    depth="""<section>
<h2>How it works</h2>
<p>Each travel style carries a set of daily planning allowances in yen: a room rate per night, and per-person amounts for food and drink, local transport, and activities and entry fees. These are rough planning assumptions, not quotes &mdash; prices change, and the calculator cannot know what you will actually book.</p>
<p>Rooms are counted as one per two travellers, rounded up, and charged for every night. Food, transport and activities are counted per person for every day on the ground, which is the number of nights plus one, since arrival and departure days both involve spending. A JR Pass, if you choose one, is added per person. Flights are entered in pounds and converted to yen at the rate you give. The total is shown in both currencies, along with a per-person figure and a per-person daily figure that excludes flights.</p>
<h2>A worked example</h2>
<p>Two people sharing a room for 14 nights at the mid-range preset, paying per journey rather than buying a JR Pass, with return flights entered at &pound;750 each and the rate field left at its starting value of &yen;190 to the pound:</p>
<table class="worked">
<tr><td>Accommodation (1 room &times; 14 nights)</td><td>&yen;210,000</td></tr>
<tr><td>Food and drink (2 people &times; 15 days)</td><td>&yen;195,000</td></tr>
<tr><td>Local transport (2 &times; 15 days)</td><td>&yen;36,000</td></tr>
<tr><td>Activities and entry fees (2 &times; 15 days)</td><td>&yen;66,000</td></tr>
<tr><td>Return flights (2 &times; &pound;750)</td><td>&yen;285,000</td></tr>
<tr><td>Total</td><td>&yen;792,000 (about &pound;4,168)</td></tr>
</table>
<p>That works out at roughly &pound;2,084 per person all in, or about &pound;89 per person per day once you are there. Every one of those figures rests on the presets and on the rate in the box, so change anything that does not match your trip &mdash; and check the current exchange rate before relying on the pound amounts.</p>
</section>""",
    faqs=[
        ("How much does a two-week trip to Japan cost?",
         "It depends mostly on where you sleep and how far you travel by train. Using this calculator&rsquo;s mid-range presets, two people sharing a room for 14 nights come to roughly &pound;4,200 including flights &mdash; but that is a planning figure built on assumptions. Replace the flight price and exchange rate with your own, and compare real hotel prices for your dates."),
        ("What is a realistic daily budget for Japan?",
         "The calculator shows a per-person daily figure for time on the ground, excluding flights. In the worked example above it comes to about &pound;89 at mid-range. Accommodation moves that number more than anything else, so it is the first line to test against actual prices for your dates and cities."),
        ("Should I include a JR Pass?",
         "Only if your itinerary covers serious distance. Add up the individual fares for the journeys you actually plan and compare them with the pass price before selecting it here. For trips based in one or two cities, paying per journey is often cheaper, and a regional pass may suit better than the national one."),
        ("What exchange rate does the calculator use?",
         "Whatever you enter. The rate box starts with a placeholder so the page works straight away, but it is not a live rate &mdash; check the current rate before trusting the pound figures. The yen totals do not depend on it, except for flights, which are converted from the pound fare you enter."),
        ("Why are there more days than nights?",
         "A 14-night trip has 15 days on the ground if you count the day you arrive and the day you leave, and you eat and get around on both. So food, local transport and activities are counted for nights plus one, while accommodation is counted per night."),
        ("How does the calculator count hotel rooms?",
         "It assumes two travellers share each room and rounds up, so three people get two rooms. If you are booking a family room, a single, or beds in a hostel dormitory, treat the accommodation line as approximate and adjust your expectations accordingly."),
    ],
))


PAGES.append(dict(
    slug="dough-temperature-calculator",
    palette="bakelog",
    tab_title="Dough Temperature Calculator — Free & Instant | Eritech Studios",
    og_title="Dough Temperature Calculator",
    meta_desc="Work out the water temperature you need to hit your desired dough temperature, from flour and room temperature. Free, no signup.",
    h1="Dough Temperature Calculator",
    lede="The one number that decides how fast your dough ferments &mdash; and the water temperature that gets you there.",
    calc_html="""<div class="seg" id="unit">
<button class="on" data-u="C" type="button">&deg;C</button>
<button data-u="F" type="button">&deg;F</button>
</div>
<div class="row">
<div class="field"><label for="ddt">Desired dough temperature</label><input type="number" id="ddt" value="25" step="0.5" inputmode="decimal"></div>
<div class="field"><label for="flour">Flour temperature</label><input type="number" id="flour" value="20" step="0.5" inputmode="decimal"></div>
</div>
<div class="row">
<div class="field"><label for="room">Room temperature</label><input type="number" id="room" value="20" step="0.5" inputmode="decimal"></div>
<div class="field"><label for="friction">Friction factor</label><input type="number" id="friction" value="2" step="0.5" inputmode="decimal"></div>
</div>
<div class="field"><label for="uselev">Using a levain or preferment?</label>
<select id="uselev"><option value="yes" selected>Yes &mdash; include its temperature</option><option value="no">No &mdash; straight dough</option></select></div>
<div class="field" id="f-lev"><label for="lev">Levain / preferment temperature</label><input type="number" id="lev" value="21" step="0.5" inputmode="decimal"></div>
<div class="result"><div class="big" id="out">&mdash;</div><div class="sub" id="outsub"></div></div>
<p class="note">Friction factor is the heat your mixing adds: roughly 1&ndash;2&thinsp;&deg;C by hand, 3&ndash;5&thinsp;&deg;C in a stand mixer, more in a spiral mixer.</p>""",
    calc_js="""function $(i){return document.getElementById(i)}
function num(i){var v=parseFloat($(i).value);return isNaN(v)?0:v}
var unit='C';
function calc(){
var lev=$('uselev').value==='yes';
$('f-lev').hidden=!lev;
var mult=lev?4:3;
var sum=num('flour')+num('room')+num('friction')+(lev?num('lev'):0);
var water=num('ddt')*mult-sum;
var w=Math.round(water*10)/10;
$('out').textContent=w+'\u00b0'+unit+' water';
var lo=unit==='C'?0:32, hi=unit==='C'?60:140;
var warn='';
if(w<lo)warn=' That is below freezing \u2014 your flour or room is too cold to hit this target; warm the flour or lower the target.';
else if(w>hi)warn=' That is hot enough to damage yeast \u2014 lower the target or cool the room instead.';
$('outsub').textContent='Mix at this water temperature to land near '+num('ddt')+'\u00b0'+unit+'. Formula: '+mult+' \u00d7 target \u2212 (flour + room + friction'+(lev?' + levain':'')+').'+warn}
document.querySelectorAll('#unit button').forEach(function(b){b.addEventListener('click',function(){
var toF=b.dataset.u==='F'&&unit==='C', toC=b.dataset.u==='C'&&unit==='F';
if(toF||toC){['ddt','flour','room','lev'].forEach(function(id){
var v=num(id);$(id).value=toF?Math.round(v*9/5+32):Math.round((v-32)*5/9)});
$('friction').value=toF?Math.round(num('friction')*9/5):Math.round(num('friction')*5/9)}
unit=b.dataset.u;
document.querySelectorAll('#unit button').forEach(function(x){x.classList.toggle('on',x===b)});calc()})});""",
    explainer="""<section>
<h2>Why bakers control dough temperature</h2>
<p>Fermentation is a chemistry reaction, and like every chemistry reaction it runs faster when it is warm. A dough finishing its mix at 27&thinsp;&deg;C will complete bulk fermentation dramatically sooner than the same dough at 22&thinsp;&deg;C &mdash; often by hours. This is why the same recipe behaves like a different recipe in July and January, and why &ldquo;bulk for four hours&rdquo; is close to meaningless as an instruction on its own.</p>
<p>Desired dough temperature, or DDT, is how bakeries make timings repeatable. You pick the temperature you want the dough to be when mixing finishes, then adjust the one ingredient whose temperature you can easily change &mdash; the water &mdash; to land there. Most sourdough sits happily between 24 and 26&thinsp;&deg;C; enriched doughs are often kept cooler to protect the butter.</p>
<h2>The formula</h2>
<p>For a straight dough, multiply your target by three, then subtract the flour temperature, the room temperature and the friction factor. If you are adding a levain or preferment, multiply by four instead and subtract its temperature too &mdash; the multiplier simply counts how many temperature sources are in the mix.</p>
<p>The friction factor is the heat that mixing itself adds. Hand mixing contributes very little, roughly 1&ndash;2&thinsp;&deg;C. A stand mixer adds noticeably more, around 3&ndash;5&thinsp;&deg;C depending on how long you run it, and a spiral mixer more again. It is worth measuring your own once: mix a batch, record every temperature, and rearrange the formula to solve for friction. That single number then makes every future bake predictable.</p>
<h2>When the answer looks absurd</h2>
<p>A cold kitchen in winter can produce a required water temperature above 40&thinsp;&deg;C, and that is a genuine signal rather than an error &mdash; but be careful, because water much beyond 50&thinsp;&deg;C starts damaging yeast on contact. The better fix is usually to warm the flour instead, or to accept a lower target and simply let the bulk run longer. Conversely, in a hot kitchen the calculator will ask for fridge-cold or even iced water, which is exactly what summer baking requires.</p>
</section>""",
    app_block=bakelog_block("dough_temperature", built=False),
    depth="""<section>
<h2>How it works</h2>
<p>The calculator multiplies your desired dough temperature by the number of temperature sources in the mix &mdash; three for a straight dough (flour, room and friction), four when a levain or preferment is included &mdash; and subtracts the sum of the temperatures you know. What is left is the temperature the water needs to be. The friction factor goes into that sum as though it were a reading, although it is really the heat added by mixing.</p>
<p>The answer is rounded to one decimal place. Below 0&nbsp;&deg;C (32&nbsp;&deg;F) the calculator warns that the flour or room is too cold to reach the target; above 60&nbsp;&deg;C (140&nbsp;&deg;F) it warns that the water would be hot enough to damage yeast. Switching between &deg;C and &deg;F converts the temperatures you have entered to whole degrees, and scales the friction factor by 9/5 without the 32-degree offset, because it is a rise in temperature rather than a reading.</p>
<p>The formula is a rule of thumb. It gives every source equal weight whatever the actual quantities, which is one reason to measure your own friction factor: it absorbs some of that error for the recipe you make most.</p>
<h2>A worked example</h2>
<p>Take the default settings: a target of 25&nbsp;&deg;C, flour and room both at 20&nbsp;&deg;C, a hand-mixing friction factor of 2&nbsp;&deg;C, and a levain at 21&nbsp;&deg;C.</p>
<table class="worked">
<tr><td>Target &times; four sources (25 &times; 4)</td><td>100</td></tr>
<tr><td>Known temperatures (20 + 20 + 2 + 21)</td><td>63</td></tr>
<tr><td>Water temperature (100 &minus; 63)</td><td>37&nbsp;&deg;C</td></tr>
</table>
<p>37&nbsp;&deg;C is roughly body temperature &mdash; comfortably warm, and well short of anything that troubles yeast. Leave the levain out and the same kitchen needs 33&nbsp;&deg;C water (25 &times; 3 = 75, less 42). The levain is 4&nbsp;&deg;C cooler than the target, so including it asks the water to make up exactly those 4 degrees.</p>
</section>""",
    faqs=[
        ("What temperature should my dough be?",
         "Most sourdough is happy between 24 and 26&nbsp;&deg;C, but the right number depends on how long you want fermentation to take. A warmer target shortens bulk fermentation and a cooler one lengthens it, so choose the one that fits your day. Whatever you pick, check the dough itself with a probe thermometer at the end of mixing, rather than trusting the room."),
        ("How do I calculate water temperature for bread dough?",
         "Multiply your desired dough temperature by three, then subtract the flour temperature, the room temperature and the friction factor. For a 25&nbsp;&deg;C target with flour and room at 20&nbsp;&deg;C and a friction factor of 2, that is 75 &minus; 42, or 33&nbsp;&deg;C water. With a levain or preferment, multiply by four and subtract its temperature as well."),
        ("What is the friction factor in bread making?",
         "It is the heat that mixing adds to the dough, expressed in degrees. To measure your own, record the flour, room and water temperatures (and the levain&rsquo;s, if used), mix as normal, then take the dough&rsquo;s temperature. Multiply that by three &mdash; or four with a levain &mdash; and subtract the other readings. What remains is your friction factor for that mixer and mixing time."),
        ("Can I use the dough temperature formula in Fahrenheit?",
         "Yes, provided every reading is in the same scale. The friction factor is larger in Fahrenheit because it is a temperature rise: each &deg;C of rise is 1.8&nbsp;&deg;F, so a 2&nbsp;&deg;C hand-mixing factor becomes about 4&nbsp;&deg;F. The calculator converts all the fields when you switch units, rounding to whole degrees."),
        ("Does the levain temperature matter?",
         "Yes &mdash; the four-source formula gives it the same weight as the flour and the room. Enter 5&nbsp;&deg;C for a levain straight from the fridge in the default example and the required water jumps from 37&nbsp;&deg;C to 53&nbsp;&deg;C, past the point where caution is wise. Letting the levain warm up first, or warming the flour, is the gentler fix."),
    ],
))

PAGES.append(dict(
    slug="wine-cellar-value-calculator",
    palette="cellar",
    tab_title="Wine Cellar Value Calculator — Free & Instant | Eritech Studios",
    og_title="Wine Cellar Value Calculator",
    meta_desc="Estimate what your wine collection is worth by tier, for insurance or planning. Free, no signup, nothing stored.",
    h1="Wine Cellar Value Calculator",
    lede="What is actually sitting in the rack? Count by tier and get a total, an average, and a replacement figure.",
    extra_css=""".result td:nth-child(2),.result td:nth-child(3){text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
.result td:nth-child(2){color:var(--muted);padding-right:16px}
""",
    calc_html="""<div class="field"><label for="cur">Currency</label>
<select id="cur"><option value="&pound;" selected>&pound; GBP</option><option value="$">$ USD</option><option value="&euro;">&euro; EUR</option></select></div>
<div class="row">
<div class="field"><label for="c1">Everyday bottles</label><input type="number" id="c1" value="24" min="0" inputmode="numeric"></div>
<div class="field"><label for="p1">Average each</label><input type="number" id="p1" value="12" min="0" inputmode="decimal"></div>
</div>
<div class="row">
<div class="field"><label for="c2">Good bottles</label><input type="number" id="c2" value="18" min="0" inputmode="numeric"></div>
<div class="field"><label for="p2">Average each</label><input type="number" id="p2" value="30" min="0" inputmode="decimal"></div>
</div>
<div class="row">
<div class="field"><label for="c3">Fine wine</label><input type="number" id="c3" value="8" min="0" inputmode="numeric"></div>
<div class="field"><label for="p3">Average each</label><input type="number" id="p3" value="80" min="0" inputmode="decimal"></div>
</div>
<div class="row">
<div class="field"><label for="c4">Cellar-worthy / investment</label><input type="number" id="c4" value="4" min="0" inputmode="numeric"></div>
<div class="field"><label for="p4">Average each</label><input type="number" id="p4" value="250" min="0" inputmode="decimal"></div>
</div>
<div class="result"><table id="tbl"></table><div class="sub" id="outsub"></div></div>
<p class="note">Nothing you type is sent anywhere or stored &mdash; the sum happens in your browser.</p>""",
    calc_js="""function $(i){return document.getElementById(i)}
function num(i){var v=parseFloat($(i).value);return isNaN(v)?0:v}
function calc(){
var cur=$('cur').value;
var rows=[['Everyday',num('c1'),num('p1')],['Good',num('c2'),num('p2')],
['Fine wine',num('c3'),num('p3')],['Cellar-worthy',num('c4'),num('p4')]];
var bottles=0,total=0,h='';
rows.forEach(function(r){var v=r[1]*r[2];bottles+=r[1];total+=v;
if(r[1]>0)h+='<tr><td>'+r[0]+'</td><td>'+r[1]+' bottles</td><td>'+cur+Math.round(v).toLocaleString()+'</td></tr>'});
h+='<tr><td>Total</td><td>'+bottles+' bottles</td><td>'+cur+Math.round(total).toLocaleString()+'</td></tr>';
$('tbl').innerHTML=h;
$('outsub').innerHTML=bottles>0?('Average '+cur+(total/bottles).toLocaleString(undefined,{minimumFractionDigits:2,maximumFractionDigits:2})+' a bottle. '+
(total>10000?'Above a typical home-contents single-item limit \u2014 worth telling your insurer.':'Keep a copy of this figure with your insurance documents.')):'Enter some bottles above.'}""",
    explainer="""<section>
<h2>Why put a number on a cellar</h2>
<p>Most people who collect wine seriously have no idea what the rack is worth, and the usual moment of discovery is a bad one &mdash; a flood, a failed cooling unit, a house move, or an insurer asking for a figure after something has already gone wrong. Standard home contents policies frequently cap any single item, and some exclude alcohol above a threshold entirely, so a cellar that quietly grew past five figures may be substantially uninsured without anyone deciding that.</p>
<h2>Purchase price is not replacement cost</h2>
<p>The figure that matters for insurance is what it would cost to buy the collection again today, which for anything mature is usually well above what you paid. A Bordeaux bought on release for £40 and drunk fifteen years later might cost £120 to replace, if it is still available at all &mdash; and for sought-after vintages, availability is the real constraint rather than price. Valuing by tier, as above, gets you far closer than totting up old receipts.</p>
<h2>Value and readiness are different questions</h2>
<p>A cellar has two clocks running: what a bottle is worth, and whether it is ready. They diverge more than people expect. Fine wine generally appreciates while it is still ageing, plateaus around its drinking window, then falls away as the risk of being past it grows &mdash; which means the financially optimal moment to sell often arrives before the best moment to drink. Deciding which of those you care about, bottle by bottle, is most of what cellar management actually is. The <a href="/tools/wine-drink-window-calculator/">drink window calculator</a> handles the other clock.</p>
<h2>Treat this as a planning figure</h2>
<p>Tier averages give you an order of magnitude, not a valuation. For probate, a formal insurance schedule or a sale, you want a merchant valuation or auction estimates against actual bottles and vintages. What this is good for is the question most collectors cannot answer at all: roughly what is in there, and is it more than you assumed.</p>
</section>""",
    app_block=cellar_block("cellar_value", built=False),
    depth="""<section>
<h2>How it works</h2>
<p>You sort your bottles into four tiers &mdash; everyday, good, fine wine, and cellar-worthy or investment &mdash; and give each tier a count and an average price per bottle. Each tier&rsquo;s value is its count multiplied by its average, and the collection&rsquo;s total is the sum of the four. The average per bottle is that total divided by the number of bottles.</p>
<p>If the total comes to more than 10,000 in your chosen currency, the calculator notes that this is above a typical home-contents single-item limit. That is a prompt to check your policy, not a statement about it. Everything happens in your browser; nothing you type is sent or stored.</p>
<h2>A worked example</h2>
<p>A modest but growing cellar, using the calculator&rsquo;s starting figures in pounds:</p>
<table class="worked">
<tr><td>Everyday (24 &times; &pound;12)</td><td>&pound;288</td></tr>
<tr><td>Good (18 &times; &pound;30)</td><td>&pound;540</td></tr>
<tr><td>Fine wine (8 &times; &pound;80)</td><td>&pound;640</td></tr>
<tr><td>Cellar-worthy (4 &times; &pound;250)</td><td>&pound;1,000</td></tr>
<tr><td>Total (54 bottles)</td><td>&pound;2,468</td></tr>
<tr><td>Average per bottle (2,468 &divide; 54)</td><td>&pound;45.70</td></tr>
</table>
<p>The four cellar-worthy bottles are under a tenth of the collection by count but account for about 40% of its value. That is typical, and it is why the top tier deserves the most care when you set its average: a few bottles priced at what they cost years ago can understate the whole figure.</p>
</section>""",
    faqs=[
        ("How do I get an accurate valuation of my wine collection?",
         "Value it bottle by bottle rather than by tier: look up current merchant or auction prices for each specific wine and vintage, and allow for condition, fill level and how it has been stored. For insurance schedules, probate or a sale, ask a wine merchant or auction house for a formal valuation. A tier-based calculator like this one gives you a sound order of magnitude, not an accurate valuation."),
        ("Should I value wine at what I paid or what it would cost to replace?",
         "For insurance, use replacement cost &mdash; what it would take to buy the same bottles today. For anything mature or sought after, that is usually more than you paid on release, and some bottles may not be available to buy again at any price."),
        ("What average price should I use for each tier?",
         "Use what a typical bottle in that tier would cost to buy now, not the price on an old receipt. If you are unsure, look up current prices for two or three representative bottles in the tier and take a rough middle. Be most careful with the top tier, where a small number of bottles can carry much of the value."),
        ("Does home insurance cover a wine collection?",
         "It varies by policy, so check the wording. Many contents policies cap individual items or valuables, and some limit or exclude alcohol above a certain value. If your total is significant, ask your insurer whether the collection needs to be declared or listed separately."),
        ("Does wine increase in value?",
         "Some does. Fine wine from well-regarded producers and vintages often costs more to replace as it matures, especially as it becomes scarce. Everyday wine, made to be drunk young, generally does not appreciate. Value tends to plateau around a wine&rsquo;s drinking window and can fall away if it is kept too long."),
    ],
))


PAGES.append(dict(
    slug="pizza-dough-calculator",
    palette="bakelog",
    tab_title="Pizza Dough Calculator — Free & Instant | Eritech Studios",
    og_title="Pizza Dough Calculator",
    meta_desc="Flour, water, salt, oil and yeast or sourdough starter for any number of pizza dough balls — Neapolitan, New York, Roman pan or Detroit. Free, no signup.",
    h1="Pizza Dough Calculator",
    lede="Pick a style, say how many bases you want, and get the exact weights &mdash; scaled to your dough balls, not someone else&rsquo;s recipe.",
    extra_css=""".result td:nth-child(2){text-align:right;color:var(--muted);padding-right:16px;font-variant-numeric:tabular-nums}
.result td:nth-child(3){text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
""",
    calc_html="""<div class="field"><label for="style">Style</label>
<select id="style">
<option value="62,2.8,0,0,260" selected>Neapolitan &mdash; soft, fast, wood-fired or steel</option>
<option value="63,2,2.5,1.5,300">New York &mdash; foldable slice, oil and a little sugar</option>
<option value="75,2.2,2,0,500">Roman pan (teglia) &mdash; wet, airy, tray-baked</option>
<option value="70,2,3,0,450">Detroit &mdash; thick, crisp-bottomed pan</option>
</select></div>
<div class="row">
<div class="field"><label for="balls">Dough balls</label><input type="number" id="balls" value="4" min="1" max="60" inputmode="numeric"></div>
<div class="field"><label for="ballw">Weight each (g)</label><input type="number" id="ballw" value="260" min="50" inputmode="numeric"></div>
</div>
<div class="row">
<div class="field"><label for="hyd">Hydration (%)</label><input type="number" id="hyd" value="62" min="45" max="100" step="0.5" inputmode="decimal"></div>
<div class="field"><label for="salt">Salt (%)</label><input type="number" id="salt" value="2.8" min="0" max="6" step="0.1" inputmode="decimal"></div>
</div>
<div class="row">
<div class="field"><label for="oil">Oil (%)</label><input type="number" id="oil" value="0" min="0" max="12" step="0.5" inputmode="decimal"></div>
<div class="field"><label for="sugar">Sugar (%)</label><input type="number" id="sugar" value="0" min="0" max="8" step="0.5" inputmode="decimal"></div>
</div>
<div class="field"><label for="leav">Leavening</label>
<select id="leav"><option value="yeast" selected>Commercial yeast</option><option value="sd">Sourdough starter</option></select></div>
<div class="row" id="r-sd" hidden>
<div class="field"><label for="sp">Starter (% of total flour)</label><input type="number" id="sp" value="15" min="1" max="50" step="1" inputmode="decimal"></div>
<div class="field"><label for="sh">Starter hydration (%)</label><input type="number" id="sh" value="100" min="50" max="200" step="5" inputmode="decimal"></div>
</div>
<div class="row" id="r-yeast">
<div class="field"><label for="ferm">Fermentation</label>
<select id="ferm">
<option value="0.4">Same day, room temperature</option>
<option value="0.15" selected>24 hours cold</option>
<option value="0.08">48 hours cold</option>
<option value="0.05">72 hours cold</option>
</select></div>
<div class="field"><label for="ytype">Yeast</label>
<select id="ytype">
<option value="1" selected>Instant dry</option>
<option value="1.25">Active dry</option>
<option value="3">Fresh</option>
</select></div>
</div>
<div class="result"><table id="tbl"></table><div class="sub" id="outsub"></div></div>
<p class="note">Percentages are baker&rsquo;s percentages &mdash; every ingredient relative to flour, which is always 100%. Change the style and the four fields below it reset; edit them afterwards to taste.</p>""",
    calc_js="""function $(i){return document.getElementById(i)}
function num(i){var v=parseFloat($(i).value);return isNaN(v)?0:v}
function size(g){
if(g<230)return 'about a 9\u201310 inch base';
if(g<270)return 'about a 10\u201311 inch base';
if(g<310)return 'about a 12 inch base';
if(g<360)return 'about a 13\u201314 inch base';
return 'a tray or deep-pan portion'}
$('style').addEventListener('change',function(){
var p=$('style').value.split(',');
$('hyd').value=p[0];$('salt').value=p[1];$('oil').value=p[2];$('sugar').value=p[3];$('ballw').value=p[4];calc()});
function row(label,p,grams,dp){
var v=dp?Math.round(grams*10)/10:Math.round(grams);
return '<tr><td>'+label+'</td><td>'+(p===''?'':p+'%')+'</td><td>'+v.toLocaleString()+' g</td></tr>'}
function calc(){
var sd=$('leav').value==='sd';
$('r-sd').hidden=!sd; $('r-yeast').hidden=sd;
var balls=Math.max(1,Math.round(num('balls'))),bw=num('ballw');
var hyd=num('hyd'),salt=num('salt'),oil=num('oil'),sugar=num('sugar');
var total=balls*bw,h='',note='';
if(sd){
var Ft=total/(1+(hyd+salt+oil+sugar)/100);
var Wt=Ft*hyd/100;
var st=Ft*num('sp')/100, shy=num('sh')||100;
var sf=st*100/(100+shy), sw=st*shy/(100+shy);
h=row('Flour (to add)','',Ft-sf)+row('Water (to add)','',Wt-sw)+
row('Starter',Math.round(num('sp')*10)/10,st,1)+row('Salt',salt,Ft*salt/100,1);
if(oil>0)h+=row('Oil',oil,Ft*oil/100,1);
if(sugar>0)h+=row('Sugar',sugar,Ft*sugar/100,1);
note=' Your starter brings '+Math.round(sf)+' g flour and '+Math.round(sw)+' g water, already counted.';
}else{
var yeast=num('ferm')*parseFloat($('ytype').value);
var flour=total/((100+hyd+salt+oil+sugar+yeast)/100);
h=row('Flour',100,flour)+row('Water',hyd,flour*hyd/100)+row('Salt',salt,flour*salt/100,1);
if(oil>0)h+=row('Oil',oil,flour*oil/100,1);
if(sugar>0)h+=row('Sugar',sugar,flour*sugar/100,1);
h+=row('Yeast',Math.round(yeast*1000)/1000,flour*yeast/100,1);
}
h+='<tr><td>Total dough</td><td></td><td>'+Math.round(total).toLocaleString()+' g</td></tr>';
$('tbl').innerHTML=h;
$('outsub').textContent=balls+' × '+Math.round(bw)+' g — '+size(bw)+' each, at '+hyd+'% hydration.'+note}""",
    explainer="""<section>
<h2>Why pizza recipes are written as percentages</h2>
<p>Every serious pizza formula is expressed in baker&rsquo;s percentages: flour is always 100%, and everything else is stated relative to it. A dough at 62% hydration, 2.8% salt has 620&nbsp;g of water and 28&nbsp;g of salt for every kilo of flour. It reads oddly at first and then becomes the only sensible way to write a recipe, because it separates the *character* of the dough from the *quantity* you happen to be making.</p>
<p>That matters here more than in most baking, because pizza is portioned before it is baked. You do not want &ldquo;a batch&rdquo; &mdash; you want six balls of 260&nbsp;g. Working backwards from the finished ball weight to the flour is exactly the sum this calculator does, and it is fiddly by hand because the percentages have to be divided out of the total rather than multiplied into it.</p>
<h2>Hydration is what separates the styles</h2>
<p>Neapolitan sits around 58&ndash;65%. It is a fast, hot bake &mdash; 60 to 90 seconds in a wood oven &mdash; and a wetter dough would not set before the top burned. New York runs slightly higher and adds oil and a touch of sugar, which softens the crumb and helps it brown in a cooler deck oven; the oil is also what makes a slice foldable rather than crisp.</p>
<p>Roman pan pizza, teglia, goes to 75&ndash;80% and sometimes beyond. That much water gives the huge irregular holes and the light, shattering base, at the cost of a dough that cannot be shaped by hand in the usual way &mdash; it is stretched into an oiled tray instead. Detroit sits between the two, with enough oil in the pan to effectively fry the bottom.</p>
<h2>Cold fermentation needs far less yeast</h2>
<p>The yeast quantity here changes sharply with your plan, and that surprises people. A same-day dough at room temperature wants roughly 0.4% instant yeast; a 72-hour cold ferment wants nearer 0.05% &mdash; around an eighth. Use the same-day quantity for a three-day dough and it will over-proof in the fridge, going slack, sour and gassy before you bake it.</p>
<p>Time is doing the work in place of yeast, and it is doing it better: a long cold ferment develops flavour through slow enzymatic breakdown that a fast rise never reaches. If you take one thing from this page, make it that &mdash; less yeast and more time is almost always the upgrade.</p>
<h2>Making it with sourdough</h2>
<p>Switch the leavening to a starter and the sums change, because a starter is not just a raising agent &mdash; it is flour and water you have already added. A 100% hydration starter is half of each by weight, so 150&nbsp;g of it brings 75&nbsp;g of flour and 75&nbsp;g of water into the dough. Ignore that and a formula you believe is 62% hydration can land several points off, which is the most common reason a sourdough pizza dough handles differently from the recipe it came from. The calculator subtracts both from what you add.</p>
<p>Typical amounts run 10&ndash;20% of the total flour. Less starter with a longer, cooler rise gives a milder, more extensible dough &mdash; usually what you want for pizza, since aggressive sourness fights tomato and cheese. Expect timings to lengthen considerably: a dough ready in four hours with commercial yeast may want a full day, and the <a href="/tools/starter-feeding-ratio-calculator/">feeding ratio</a> you used beforehand decides how lively it is when you mix.</p>
<p>Baking bread as well as pizza? The <a href="/tools/sourdough-hydration-calculator/">hydration calculator</a> and the <a href="/tools/dough-temperature-calculator/">dough temperature calculator</a> cover the same ground for sourdough.</p>
</section>""",
    app_block=bakelog_block("pizza_dough", built=False),
    depth="""<section>
<h2>How it works</h2>
<p>The calculator starts from the dough you want: the number of balls times the weight of each gives the total. With commercial yeast, the yeast percentage comes from your fermentation plan &mdash; 0.4% for a same-day dough, 0.15% for 24&nbsp;hours cold, 0.08% for 48 and 0.05% for 72 &mdash; multiplied by 1 for instant dry yeast, 1.25 for active dry or 3 for fresh. The total dough is divided by the sum of every percentage, flour&rsquo;s 100 included, over 100; that gives the flour, and each other ingredient is its percentage of it. Flour and water are rounded to the gram; salt, oil, sugar and yeast to a tenth of a gram.</p>
<p>With a sourdough starter, the flour is found the same way without the yeast, and it is the total flour, including what the starter carries. The starter is its percentage of that total, split into flour and water by its hydration, and those amounts are taken off to give the flour and water you actually add.</p>
<h2>A worked example</h2>
<p>The default: four Neapolitan balls of 260&nbsp;g at 62% hydration and 2.8% salt, fermented for 24&nbsp;hours in the fridge with instant dry yeast.</p>
<table class="worked">
<tr><td>Total dough (4 &times; 260)</td><td>1,040&nbsp;g</td></tr>
<tr><td>Yeast (0.15% &times; 1 for instant)</td><td>0.15%</td></tr>
<tr><td>Sum of percentages (100 + 62 + 2.8 + 0.15)</td><td>164.95%</td></tr>
<tr><td>Flour (1,040 &divide; 1.6495)</td><td>630&nbsp;g</td></tr>
<tr><td>Water (630.5 &times; 62%)</td><td>391&nbsp;g</td></tr>
<tr><td>Salt (630.5 &times; 2.8%)</td><td>17.7&nbsp;g</td></tr>
<tr><td>Yeast (630.5 &times; 0.15%)</td><td>0.9&nbsp;g</td></tr>
</table>
<p>Under a gram of yeast for four pizzas is right for a day in the fridge, and too little for a scale that reads in whole grams; one reading to 0.1&nbsp;g is worth having. Switch to fresh yeast and the percentage triples to 0.45%, or 2.8&nbsp;g, with the flour and water each dropping a gram to make room.</p>
</section>""",
    faqs=[
        ("How much flour do I need for one pizza?",
         "It depends on the ball weight and the formula. For a 260&nbsp;g Neapolitan ball at 62% hydration, 2.8% salt and a 24-hour cold ferment, it is about 158&nbsp;g of flour, with 98&nbsp;g of water, 4.4&nbsp;g of salt and 0.2&nbsp;g of instant yeast. Weighing that little yeast accurately is one reason to make several balls at once."),
        ("How heavy should a pizza dough ball be?",
         "The style presets here use 260&nbsp;g for Neapolitan, 300&nbsp;g for New York, 450&nbsp;g for Detroit and 500&nbsp;g for Roman pan. As a rough guide, a ball of 230&ndash;269&nbsp;g makes about a 10&ndash;11&nbsp;inch base, 270&ndash;309&nbsp;g about 12&nbsp;inches, and anything from 360&nbsp;g upwards is better suited to a tray. Thinner or thicker stretching will shift those sizes."),
        ("How much yeast do I need for a 48-hour cold ferment?",
         "Very little. The calculator uses 0.08% of the flour weight in instant dry yeast for 48&nbsp;hours cold &mdash; about half the 24-hour figure. For four 260&nbsp;g Neapolitan balls that is 0.5&nbsp;g of yeast to 631&nbsp;g of flour. Too much yeast for a long cold rise is a common cause of dough that turns slack and gassy before bake day."),
        ("Can I use fresh or active dry yeast instead of instant?",
         "Yes, but the weight changes. The calculator treats active dry yeast as needing 1.25 times the instant amount and fresh yeast three times as much, because fresh yeast is mostly water. Choose the type in the yeast field and the percentage and grams update for you &mdash; for the default 24-hour dough, 0.9&nbsp;g of instant becomes 2.8&nbsp;g of fresh."),
        ("How do I make pizza dough with a sourdough starter?",
         "Choose the sourdough option and set the starter as a percentage of total flour; 15% is the default. The calculator subtracts the flour and water inside the starter from what you add, so hydration stays true. For four 260&nbsp;g balls at 62% hydration with a 100% starter, that is 94.7&nbsp;g of starter, 584&nbsp;g of flour and 344&nbsp;g of water. Expect a much longer rise than with yeast."),
    ],
))

# ---------------------------------------------------------------- build pages

TOOL_TITLES = {p["slug"]: p["og_title"] for p in PAGES}

def related_section(current_slug):
    gname, slugs = next((g, s) for g, _, _, s in GROUPS if current_slug in s)
    siblings = [s for s in slugs if s != current_slug]
    others = [p["slug"] for p in PAGES if p["slug"] not in slugs]
    html = ""
    if siblings:
        html += ('<h2>More ' + gname.lower() + ' tools</h2>\n<ul class="cluster">\n' + "\n".join(
            '<li><a href="/tools/' + s + '/">' + TOOL_TITLES[s] + '</a><span class="d">' + DESCS[s] + '</span></li>'
            for s in siblings) + '\n</ul>\n')
    html += ('<h2>Other free tools</h2>\n<ul>\n' + "\n".join(
        '<li><a href="/tools/' + s + '/">' + TOOL_TITLES[s] + '</a></li>' for s in others) + '\n</ul>')
    return html

def faq_section(faqs):
    if not faqs:
        return ""
    return ('<section class="faq">\n<h2>Frequently asked questions</h2>\n' + "".join(
        '<h3>' + q + '</h3>\n<p>' + a + '</p>\n' for q, a in faqs) + '</section>')

def page_jsonld(p):
    url = DOMAIN + "/tools/" + p["slug"] + "/"
    graph = [
        breadcrumb((BRAND, DOMAIN + "/"), ("Free tools", DOMAIN + "/tools/"), (p["og_title"], url)),
        {"@type": "WebApplication", "name": p["og_title"], "url": url,
         "description": plain_text(p["meta_desc"]), "applicationCategory": "UtilitiesApplication",
         "operatingSystem": "Any", "browserRequirements": "Requires JavaScript",
         "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "GBP"},
         "publisher": ORG_REF},
    ]
    if p.get("faqs"):
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": plain_text(q),
             "acceptedAnswer": {"@type": "Answer", "text": plain_text(a)}} for q, a in p["faqs"]]})
    return jsonld_script({"@context": "https://schema.org", "@graph": graph})

def build_page(p):
    pal = PALETTES[p["palette"]]
    html = TEMPLATE
    for k, v in [
        ("@@TAB_TITLE@@", p["tab_title"]), ("@@META_DESC@@", p["meta_desc"]),
        ("@@OG_TITLE@@", p["og_title"]), ("@@SLUG@@", p["slug"]), ("@@DOMAIN@@", DOMAIN),
        ("@@CF@@", CF_SNIPPET), ("@@JSONLD@@", page_jsonld(p)), ("@@BRAND@@", BRAND),
        ("@@BG@@", pal["bg"]), ("@@SURFACE@@", pal["surface"]), ("@@TEXT@@", pal["text"]),
        ("@@MUTED@@", pal["muted"]), ("@@ACCENT@@", pal["accent"]), ("@@LINE@@", pal["line"]),
        ("@@ON@@", pal["on"]),
        ("@@H1@@", p["h1"]), ("@@LEDE@@", p["lede"]),
        ("@@CALC_HTML@@", p["calc_html"]), ("@@EXPLAINER@@", p["explainer"]),
        ("@@DEPTH@@", p.get("depth", "")), ("@@FAQ@@", faq_section(p.get("faqs"))),
        ("@@APP_BLOCK@@", p["app_block"]), ("@@RELATED@@", related_section(p["slug"])),
        ("@@CALC_JS@@", p["calc_js"]), ("@@EXTRA_CSS@@", p.get("extra_css", "")),
    ]:
        html = html.replace(k, v)
    out_dir = os.path.join(REPO, "tools", p["slug"])
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w") as f:
        f.write(html)
    print("wrote tools/" + p["slug"] + "/index.html")

# ---------------------------------------------------------------- tools index

GROUPS = [
    ("Travel", "The Travel Binder", ACCENT_BY_APP["The Travel Binder"], ["packing-list-generator", "japan-trip-cost-calculator"]),
    ("Baking", "The Bake Log", ACCENT_BY_APP["The Bake Log"], ["sourdough-hydration-calculator", "bakers-percentage-calculator", "starter-feeding-ratio-calculator", "dough-temperature-calculator", "pizza-dough-calculator"]),
    ("Coffee", "Kohii", ACCENT_BY_APP["Kohii"], ["coffee-ratio-calculator", "espresso-ratio-calculator", "coffee-freshness-calculator"]),
    ("Wine", "Cellar Book", ACCENT_BY_APP["Cellar Book"], ["wine-drink-window-calculator", "wine-cellar-value-calculator"]),
    ("Plants", "Leaflet", ACCENT_BY_APP["Leaflet"], ["plant-watering-calculator"]),
    ("Consumer rights", "Warranty Box", ACCENT_BY_APP["Warranty Box"], ["uk-return-rights-checker"]),
]

DESCS = {
    "sourdough-hydration-calculator": "Flour, water and starter in — true hydration % out, or work backwards from a target.",
    "bakers-percentage-calculator": "Scale any bread formula from flour weight or target dough weight.",
    "starter-feeding-ratio-calculator": "1:1:1, 1:2:2, 1:5:5 — exact feed amounts and expected peak times.",
    "coffee-ratio-calculator": "Coffee-to-water ratios for V60, Chemex, AeroPress, French press and more.",
    "espresso-ratio-calculator": "Dose, yield, ratio — enter any two and solve the third.",
    "coffee-freshness-calculator": "Roast date in, peak window out — for espresso and filter.",
    "wine-drink-window-calculator": "Style and vintage in — ageing, ready, at peak or fading out.",
    "plant-watering-calculator": "Watering intervals by species, season and light.",
    "uk-return-rights-checker": "Which legal return or refund window you're in, from the purchase date.",
    "pizza-dough-calculator": "Style and ball count in — flour, water, salt, oil and yeast out.",
    "dough-temperature-calculator": "Hit a target dough temperature — the water temp you need, from flour and room.",
    "wine-cellar-value-calculator": "Count by tier — total value, average per bottle, replacement figure.",
    "packing-list-generator": "Trip length, climate and style in — a categorised list with quantities out.",
    "japan-trip-cost-calculator": "Nights and travel style in — a line-by-line budget, per person and per day.",
}

for p in PAGES:
    build_page(p)

groups_html = ""
for gname, app, accent, slugs in GROUPS:
    groups_html += ('<section class="group" style="--acc:' + accent + '">\n<h2><span class="dot"></span>' +
                    gname + ' <span class="app">from ' + app + '</span></h2>\n<ul>\n')
    for s in slugs:
        groups_html += ('<li><a href="/tools/' + s + '/"><strong>' + TOOL_TITLES[s] + '</strong>'
                        '<span>' + DESCS[s] + '</span></a></li>\n')
    groups_html += '</ul>\n</section>\n'

tools_index = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Free Tools &amp; Calculators | Eritech Studios</title>
<meta name="description" content="Free calculators for baking, coffee, wine, plants, travel and UK consumer rights — built by Eritech Studios. No signup, no ads on the tools.">
<link rel="canonical" href="@@DOMAIN@@/tools/">
<meta property="og:type" content="website">
<meta property="og:title" content="Free Tools &amp; Calculators — Eritech Studios">
<meta property="og:description" content="Free calculators for baking, coffee, wine, plants, travel and UK consumer rights. No signup.">
<meta property="og:url" content="@@DOMAIN@@/tools/">
<meta property="og:image" content="@@DOMAIN@@/assets/og/tools.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
@@CF@@
@@ITEMLIST@@
<style>
*{box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.6;color:#3B342C;max-width:680px;margin:40px auto;padding:0 20px;background-color:#FAF7F2}
h1{font-family:Georgia,"Times New Roman",serif;font-size:2rem;color:#1F1A15;margin-bottom:5px}
.subtitle{color:#8A8074;margin-top:0;margin-bottom:34px}
.crumb{font-size:.9rem;color:#998F83;margin-bottom:24px}
.crumb a,a:visited{color:#998F83;text-decoration:none}
.crumb a:hover{color:#7A3B24}
h2{font-family:Georgia,"Times New Roman",serif;font-size:1.25rem;color:#1F1A15;margin:34px 0 12px;display:flex;align-items:baseline;gap:9px}
h2 .dot{width:11px;height:11px;border-radius:4px;background:var(--acc);flex:none;align-self:center}
h2 .app{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;font-size:.82rem;color:#9a948e;font-weight:400;letter-spacing:.01em}
ul{list-style:none;padding:0;margin:0}
li{margin-bottom:10px}
li a,a:visited{display:block;padding:13px 18px 12px;background:#FFFDFA;border:1px solid #E9E3D9;border-left:4px solid var(--acc);border-radius:10px;text-decoration:none;color:#3B342C;transition:border-color .15s ease,box-shadow .15s ease}
li a:hover{border-color:var(--acc);box-shadow:0 3px 14px rgba(60,45,30,.08)}
li a{position:relative;padding-right:40px}
li a::after{content:"";position:absolute;right:17px;top:50%;width:7px;height:7px;border-right:2px solid var(--acc);border-bottom:2px solid var(--acc);transform:translateY(-50%) rotate(-45deg);opacity:.55;transition:transform .15s ease,opacity .15s ease}
li a:hover::after{transform:translate(4px,-50%) rotate(-45deg);opacity:1}
li a strong{display:block;color:#1F1A15;font-size:1.02rem}
li a span{font-size:.9rem;color:#8A8074}
footer{margin-top:50px;font-size:.85rem;color:#998F83;border-top:1px solid #E9E3D9;padding-top:20px}
footer a,a:visited{color:#998F83}
</style>
</head>
<body>
<nav class="crumb"><a href="/">Eritech Studios</a> / Free tools</nav>
<h1>Free Tools &amp; Calculators</h1>
<p class="subtitle">Small, fast, free calculators from the apps we build. No signup, nothing gated.</p>
@@GROUPS@@
<footer>
<p>&copy; 2026 Eritech Studios &middot; <a href="mailto:admin@eritech.studio">admin@eritech.studio</a></p>
</footer>
</body>
</html>
"""
itemlist = ('<script type="application/ld+json">\n'
            '{"@context":"https://schema.org","@type":"ItemList","name":"Free tools and calculators",'
            '"itemListElement":[' + ",".join(
    '{"@type":"ListItem","position":%d,"name":"%s","url":"%s/tools/%s/"}' % (i + 1, TOOL_TITLES[s2], DOMAIN, s2)
    for i, s2 in enumerate([x for _, _, _, sl in GROUPS for x in sl])) + ']}\n</script>')
tools_index = (tools_index.replace("@@DOMAIN@@", DOMAIN).replace("@@CF@@", CF_SNIPPET)
               .replace("@@GROUPS@@", groups_html).replace("@@ITEMLIST@@", itemlist))
os.makedirs(os.path.join(REPO, "tools"), exist_ok=True)
with open(os.path.join(REPO, "tools", "index.html"), "w") as f:
    f.write(tools_index)
print("wrote tools/index.html")

# ---------------------------------------------------------------- robots + sitemap

with open(os.path.join(REPO, "robots.txt"), "w") as f:
    f.write("User-agent: *\nAllow: /\nSitemap: " + DOMAIN + "/sitemap.xml\n")
print("wrote robots.txt")

urls = [DOMAIN + "/", DOMAIN + "/apps/", DOMAIN + "/tools/"]
urls += [DOMAIN + "/apps/" + a["slug"] + "/" for a in APPS]
urls += [DOMAIN + "/tools/" + p["slug"] + "/" for p in PAGES]
LASTMOD = os.environ.get("SITEMAP_DATE", SITE_LASTMOD)
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in urls:
    sm += "  <url><loc>" + u + "</loc><lastmod>" + LASTMOD + "</lastmod></url>\n"
sm += "</urlset>\n"
with open(os.path.join(REPO, "sitemap.xml"), "w") as f:
    f.write(sm)
print("wrote sitemap.xml (" + str(len(urls)) + " urls)")

# ---------------------------------------------------------------- OG images

for p in PAGES:
    og_image(p["slug"] + ".png", p["og_title"], PALETTES[p["palette"]])
og_image("tools.png", "Free Tools & Calculators", dict(bg="#FAF7F2", accent="#7A3B24", text="#1F1A15", muted="#998F83"))

print("done")
