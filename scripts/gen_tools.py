#!/usr/bin/env python3
"""Generate eritech.studio /tools/ calculator pages, OG images, robots.txt and sitemap.xml."""
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://eritech.studio"

CF_SNIPPET = """<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "438cd0e70d5a4d39a4ec168956408116"}'></script><!-- End Cloudflare Web Analytics -->"""

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
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
@@CF@@
<style>
:root{--bg:@@BG@@;--surface:@@SURFACE@@;--text:@@TEXT@@;--muted:@@MUTED@@;--accent:@@ACCENT@@;--line:@@LINE@@;--on-accent:@@ON@@}
*{box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--text);margin:0;line-height:1.6}
main{max-width:680px;margin:0 auto;padding:0 20px 40px}
.crumb{max-width:680px;margin:0 auto;padding:18px 20px;font-size:.9rem;color:var(--muted)}
.crumb a{color:var(--muted);text-decoration:none}
.crumb a:hover{color:var(--accent)}
.crumb span{margin:0 8px}
h1{font-family:Georgia,"Times New Roman",serif;font-size:2rem;line-height:1.25;margin:10px 0 6px}
.lede{color:var(--muted);margin:0 0 28px}
h2{font-family:Georgia,"Times New Roman",serif;font-size:1.3rem;margin:34px 0 10px}
p{margin:0 0 14px}
a{color:var(--accent)}
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
.more-tools a{text-decoration:none}
.more-tools a:hover{text-decoration:underline}
footer{max-width:680px;margin:30px auto 0;padding:20px;border-top:1px solid var(--line);color:var(--muted);font-size:.85rem}
footer a{color:var(--muted)}
@@EXTRA_CSS@@</style>
</head>
<body>
<nav class="crumb"><a href="/">Eri Tech Studio</a><span>/</span><a href="/tools/">Free tools</a></nav>
<main>
<header>
<h1>@@H1@@</h1>
<p class="lede">@@LEDE@@</p>
</header>
<section class="calc" aria-label="Calculator">
@@CALC_HTML@@
</section>
@@EXPLAINER@@
<section class="app-block">
@@APP_BLOCK@@
</section>
<section class="more-tools">
<h2>More free tools</h2>
<ul>
@@RELATED@@
</ul>
</section>
</main>
<footer>
<p>&copy; 2026 Eri Tech Studio &middot; <a href="mailto:admin@eritech.studio">admin@eritech.studio</a></p>
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

APPSTORE_BADGE_IMG = "https://tools.applemediaservices.com/api/badges/download-on-the-app-store/black/en-us"
PLAY_BADGE_IMG = "https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png"

def play_badge(pkg, campaign):
    return ('<a class="badge-play" href="https://play.google.com/store/apps/details?id=' + pkg +
            '&amp;referrer=utm_source%3Dsite%26utm_medium%3Dcalculator%26utm_campaign%3D' + campaign +
            '" rel="noopener"><img src="' + PLAY_BADGE_IMG + '" alt="Get it on Google Play"></a>')

APPLE_PROVIDER_TOKEN = "129172097"  # account-wide, from App Analytics campaign link generator

def ios_badge(app_id, campaign):
    return ('<a class="badge-appstore" href="https://apps.apple.com/app/id' + app_id +
            '?pt=' + APPLE_PROVIDER_TOKEN + '&amp;ct=calc_' + campaign +
            '&amp;mt=8" rel="noopener"><img src="' + APPSTORE_BADGE_IMG +
            '" alt="Download on the App Store"></a>')

def bakelog_block(campaign):
    return ('<p>This calculator is built into <strong>The Bake Log</strong>, along with starter feeding reminders, '
            'guided bake timelines and a full bake journal. Offline, no account, free to start.</p>'
            '<div class="badges">' + ios_badge("6790971986", campaign) +
            play_badge("com.eritech.thebakelog", campaign) + '</div>')

def kohii_block(campaign):
    return ('<p>This calculator is built into <strong>Kohii — The Barista Log</strong>, along with brew logging, '
            'dial-in history and bean freshness tracking. Offline, no account, one-time unlock.</p>'
            '<div class="badges">' + ios_badge("6790972283", campaign) +
            play_badge("com.eritech.kohii", campaign) + '</div>')

def cellar_block(campaign):
    return ('<p>This calculator is built into <strong>Cellar Book</strong>, which tracks drink windows on every '
            'bottle in your cellar — see what is ageing, ready or fading at a glance, with label photos, tasting '
            'notes on the 100-point scale and an offline map of your collection&rsquo;s regions.</p>'
            '<div class="badges">' + ios_badge("6796370046", campaign) +
            play_badge("com.eritech.cellarbook", campaign) + '</div>')

def leaflet_block(campaign):
    return ('<p>This calculator is built into <strong>Leaflet</strong>, which keeps watering and feeding schedules '
            'for every plant you own, with a photo timeline so you can watch a year of growth in one scroll. '
            'No subscription, no AI gimmicks.</p>'
            '<div class="badges">' + ios_badge("6796375617", campaign) +
            play_badge("com.eritech.leaflet", campaign) + '</div>')

def travelbinder_block(campaign):
    return ('<p>This tool comes from <strong>The Travel Binder</strong> — a fully offline binder for flights, '
            'hotels, bookings, documents, packing and checklists, with the whole trip on one map. '
            'No account, no cloud, no AI.</p>'
            '<div class="badges">' + ios_badge("6797601401", campaign) +
            play_badge("com.eritech.travelbinder", campaign) + '</div>')

def warranty_block(campaign):
    return ('<p><strong>Warranty Box</strong> keeps every receipt, warranty and return deadline in one place and '
            'reminds you before a window closes. Offline, no account.</p>'
            '<div class="badges">' + ios_badge("6790972644", campaign) +
            play_badge("com.eritech.warrantybox", campaign) + '</div>')

# ---------------------------------------------------------------- pages

PAGES = []

PAGES.append(dict(
    slug="sourdough-hydration-calculator",
    palette="bakelog",
    tab_title="Sourdough Hydration Calculator | Eri Tech Studio",
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
    app_block=bakelog_block("sourdough_hydration"),
))

PAGES.append(dict(
    slug="bakers-percentage-calculator",
    palette="bakelog",
    tab_title="Baker's Percentage Calculator | Eri Tech Studio",
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
    app_block=bakelog_block("bakers_percentage"),
))

PAGES.append(dict(
    slug="starter-feeding-ratio-calculator",
    palette="bakelog",
    tab_title="Sourdough Starter Feeding Ratio Calculator | Eri Tech Studio",
    og_title="Starter Feeding Ratio Calculator",
    meta_desc="Work out flour and water amounts for any sourdough starter feeding ratio — 1:1:1, 1:2:2, 1:5:5 or your own — with expected peak times. Free, no signup.",
    h1="Starter Feeding Ratio Calculator",
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
    app_block=bakelog_block("starter_feeding"),
))

PAGES.append(dict(
    slug="coffee-ratio-calculator",
    palette="kohii",
    tab_title="Coffee to Water Ratio Calculator | Eri Tech Studio",
    og_title="Coffee Ratio Calculator",
    meta_desc="Work out coffee-to-water ratios for V60, Chemex, AeroPress, French press, moka pot, cold brew and espresso. Free, no signup.",
    h1="Coffee Ratio Calculator",
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
))

PAGES.append(dict(
    slug="espresso-ratio-calculator",
    palette="kohii",
    tab_title="Espresso Ratio Calculator — Dose, Yield & Ratio | Eri Tech Studio",
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
))

PAGES.append(dict(
    slug="coffee-freshness-calculator",
    palette="kohii",
    tab_title="Coffee Freshness Calculator — Roast Date to Peak Window | Eri Tech Studio",
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
))

PAGES.append(dict(
    slug="wine-drink-window-calculator",
    palette="cellar",
    tab_title="Wine Drink Window Calculator | Eri Tech Studio",
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
    app_block=cellar_block("wine_drink_window"),
))

PAGES.append(dict(
    slug="plant-watering-calculator",
    palette="leaflet",
    tab_title="Plant Watering Calculator — How Often to Water | Eri Tech Studio",
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
    app_block=leaflet_block("plant_watering"),
))

PAGES.append(dict(
    slug="uk-return-rights-checker",
    palette="warranty",
    tab_title="UK Return Rights Checker — Refunds, Returns & Faulty Goods | Eri Tech Studio",
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
))

PAGES.append(dict(
    slug="packing-list-generator",
    palette="travelbinder",
    tab_title="Packing List Generator | Eri Tech Studio",
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
<p>It is rarely clothing. It is the plug adapter, the second payment card kept somewhere separate from the first, prescriptions in their original labelled packaging for border checks, and offline copies of every booking &mdash; because the one moment you cannot rely on having signal or battery is the moment you land. Screenshot or download your confirmations before you leave, and keep them somewhere that works in airplane mode.</p>
</section>""",
    app_block=travelbinder_block("packing_list"),
))

PAGES.append(dict(
    slug="japan-trip-cost-calculator",
    palette="travelbinder",
    tab_title="Japan Trip Cost Calculator &mdash; Daily Budget Estimator | Eri Tech Studio",
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
))

# ---------------------------------------------------------------- build pages

TOOL_TITLES = {p["slug"]: p["og_title"] for p in PAGES}

def related_list(current_slug):
    items = []
    for p in PAGES:
        if p["slug"] == current_slug:
            continue
        items.append('<li><a href="/tools/' + p["slug"] + '/">' + p["og_title"] + '</a></li>')
    return "\n".join(items)

def build_page(p):
    pal = PALETTES[p["palette"]]
    html = TEMPLATE
    for k, v in [
        ("@@TAB_TITLE@@", p["tab_title"]), ("@@META_DESC@@", p["meta_desc"]),
        ("@@OG_TITLE@@", p["og_title"]), ("@@SLUG@@", p["slug"]), ("@@DOMAIN@@", DOMAIN),
        ("@@CF@@", CF_SNIPPET),
        ("@@BG@@", pal["bg"]), ("@@SURFACE@@", pal["surface"]), ("@@TEXT@@", pal["text"]),
        ("@@MUTED@@", pal["muted"]), ("@@ACCENT@@", pal["accent"]), ("@@LINE@@", pal["line"]),
        ("@@ON@@", pal["on"]),
        ("@@H1@@", p["h1"]), ("@@LEDE@@", p["lede"]),
        ("@@CALC_HTML@@", p["calc_html"]), ("@@EXPLAINER@@", p["explainer"]),
        ("@@APP_BLOCK@@", p["app_block"]), ("@@RELATED@@", related_list(p["slug"])),
        ("@@CALC_JS@@", p["calc_js"]), ("@@EXTRA_CSS@@", p.get("extra_css", "")),
    ]:
        html = html.replace(k, v)
    out_dir = os.path.join(REPO, "tools", p["slug"])
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w") as f:
        f.write(html)
    print("wrote tools/" + p["slug"] + "/index.html")

for p in PAGES:
    build_page(p)

# ---------------------------------------------------------------- tools index

GROUPS = [
    ("Baking", "The Bake Log", "#A4552F", ["sourdough-hydration-calculator", "bakers-percentage-calculator", "starter-feeding-ratio-calculator"]),
    ("Coffee", "Kohii", "#8F5E1B", ["coffee-ratio-calculator", "espresso-ratio-calculator", "coffee-freshness-calculator"]),
    ("Wine", "Cellar Book", "#722F37", ["wine-drink-window-calculator"]),
    ("Plants", "Leaflet", "#2E7D32", ["plant-watering-calculator"]),
    ("Travel", "The Travel Binder", "#22314A", ["packing-list-generator", "japan-trip-cost-calculator"]),
    ("Consumer rights", "Warranty Box", "#2F6E9E", ["uk-return-rights-checker"]),
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
    "packing-list-generator": "Trip length, climate and style in — a categorised list with quantities out.",
    "japan-trip-cost-calculator": "Nights and travel style in — a line-by-line budget, per person and per day.",
}

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
<title>Free Tools &amp; Calculators | Eri Tech Studio</title>
<meta name="description" content="Free calculators for baking, coffee, wine, plants, travel and UK consumer rights — built by Eri Tech Studio. No signup, no ads on the tools.">
<link rel="canonical" href="@@DOMAIN@@/tools/">
<meta property="og:type" content="website">
<meta property="og:title" content="Free Tools &amp; Calculators — Eri Tech Studio">
<meta property="og:description" content="Free calculators for baking, coffee, wine, plants, travel and UK consumer rights. No signup.">
<meta property="og:url" content="@@DOMAIN@@/tools/">
<meta property="og:image" content="@@DOMAIN@@/assets/og/tools.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
@@CF@@
<style>
*{box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;line-height:1.6;color:#3B342C;max-width:680px;margin:40px auto;padding:0 20px;background-color:#FAF7F2}
h1{font-family:Georgia,"Times New Roman",serif;font-size:2rem;color:#1F1A15;margin-bottom:5px}
.subtitle{color:#8A8074;margin-top:0;margin-bottom:34px}
.crumb{font-size:.9rem;color:#998F83;margin-bottom:24px}
.crumb a{color:#998F83;text-decoration:none}
.crumb a:hover{color:#A4552F}
h2{font-family:Georgia,"Times New Roman",serif;font-size:1.25rem;color:#1F1A15;margin:34px 0 12px;display:flex;align-items:baseline;gap:9px}
h2 .dot{width:11px;height:11px;border-radius:4px;background:var(--acc);flex:none;align-self:center}
h2 .app{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;font-size:.82rem;color:#9a948e;font-weight:400;letter-spacing:.01em}
ul{list-style:none;padding:0;margin:0}
li{margin-bottom:10px}
li a{display:block;padding:13px 18px 12px;background:#FFFDFA;border:1px solid #E9E3D9;border-left:4px solid var(--acc);border-radius:10px;text-decoration:none;color:#3B342C;transition:border-color .15s ease,box-shadow .15s ease}
li a:hover{border-color:var(--acc);box-shadow:0 3px 14px rgba(60,45,30,.08)}
li a strong{display:block;color:#1F1A15;font-size:1.02rem}
li a span{font-size:.9rem;color:#8A8074}
footer{margin-top:50px;font-size:.85rem;color:#998F83;border-top:1px solid #E9E3D9;padding-top:20px}
footer a{color:#998F83}
</style>
</head>
<body>
<nav class="crumb"><a href="/">Eri Tech Studio</a> / Free tools</nav>
<h1>Free Tools &amp; Calculators</h1>
<p class="subtitle">Small, fast, free calculators from the apps we build. No signup, nothing gated.</p>
@@GROUPS@@
<footer>
<p>&copy; 2026 Eri Tech Studio &middot; <a href="mailto:admin@eritech.studio">admin@eritech.studio</a></p>
</footer>
</body>
</html>
"""
tools_index = tools_index.replace("@@DOMAIN@@", DOMAIN).replace("@@CF@@", CF_SNIPPET).replace("@@GROUPS@@", groups_html)
os.makedirs(os.path.join(REPO, "tools"), exist_ok=True)
with open(os.path.join(REPO, "tools", "index.html"), "w") as f:
    f.write(tools_index)
print("wrote tools/index.html")

# ---------------------------------------------------------------- robots + sitemap

with open(os.path.join(REPO, "robots.txt"), "w") as f:
    f.write("User-agent: *\nAllow: /\nSitemap: " + DOMAIN + "/sitemap.xml\n")
print("wrote robots.txt")

urls = [DOMAIN + "/", DOMAIN + "/tools/"]
urls += [DOMAIN + "/tools/" + p["slug"] + "/" for p in PAGES]
urls += [DOMAIN + "/privacy-policies/" + n for n in
         ["kohii.html", "the-bake-log.html", "warranty-box.html", "cellarbook.html", "leaflet.html",
          "travel-binder.html"]]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in urls:
    sm += "  <url><loc>" + u + "</loc></url>\n"
sm += "</urlset>\n"
with open(os.path.join(REPO, "sitemap.xml"), "w") as f:
    f.write(sm)
print("wrote sitemap.xml (" + str(len(urls)) + " urls)")

# ---------------------------------------------------------------- OG images

from PIL import Image, ImageDraw, ImageFont

OG_DIR = os.path.join(REPO, "assets", "og")
os.makedirs(OG_DIR, exist_ok=True)
TITLE_FONT = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Bold.ttf", 78)
SUB_FONT = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 34)

def og_image(fname, title, pal):
    img = Image.new("RGB", (1200, 630), pal["bg"])
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 22, 630], fill=pal["accent"])
    # wrap title
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
    d.text((90, 520), "Free tool  ·  eritech.studio/tools", font=SUB_FONT, fill=pal["muted"])
    img.save(os.path.join(OG_DIR, fname), "PNG")
    print("wrote assets/og/" + fname)

for p in PAGES:
    og_image(p["slug"] + ".png", p["og_title"], PALETTES[p["palette"]])
og_image("tools.png", "Free Tools & Calculators", dict(bg="#FAF7F2", accent="#A4552F", text="#1F1A15", muted="#998F83"))

print("done")
