CHECKED = "2026-10-28"
LEDE = "Standard return windows at major UK and US retailers, each read from the retailer&rsquo;s own returns policy page, with the date it was last checked."
UK_BASELINE = "For most things bought online, by phone or by mail order, the Consumer Contracts Regulations 2013 give you 14 days to cancel, starting the day after the goods arrive, and then a further 14 days from telling the seller to send them back. If goods are faulty, not as described or not fit for purpose, the Consumer Rights Act 2015 gives you 30 days after delivery to reject them for a full refund, whether you bought them online or in a shop."
US_BASELINE = "There is no general federal right to return something you have bought: the FTC Cooling-Off Rule gives three business days to cancel only certain sales made away from the seller&rsquo;s regular place of business, such as at your home or a hotel, so most returns depend on the retailer&rsquo;s own policy. State law fills some of the gap &mdash; New York, for example, requires sellers to post their refund policy and, if they do not, to give a refund or credit for unused goods returned within 30 days with proof of purchase."
BASELINE_SOURCES = [
    ("Consumer Contracts Regulations 2013, regulation 30 (legislation.gov.uk)", "https://www.legislation.gov.uk/uksi/2013/3134/regulation/30"),
    ("Consumer Contracts Regulations 2013, regulation 35 (legislation.gov.uk)", "https://www.legislation.gov.uk/uksi/2013/3134/regulation/35"),
    ("Consumer Rights Act 2015, section 22 (legislation.gov.uk)", "https://www.legislation.gov.uk/ukpga/2015/15/section/22"),
    ("Accepting returns and giving refunds (GOV.UK)", "https://www.gov.uk/accepting-returns-and-giving-refunds"),
    ("Changing your mind about something you&rsquo;ve bought (Citizens Advice)", "https://www.citizensadvice.org.uk/consumer/changed-your-mind/changing-your-mind-about-something-youve-bought/"),
    ("Buyer&rsquo;s remorse: the FTC&rsquo;s Cooling-Off Rule (ftc.gov)", "https://consumer.ftc.gov/articles/buyers-remorse-ftcs-cooling-rule-may-help"),
    ("Cooling-Off Rule, 16 CFR Part 429 (govinfo.gov)", "https://www.govinfo.gov/content/pkg/CFR-2024-title16-vol1/xml/CFR-2024-title16-vol1-part429.xml"),
    ("Store refunds and exchanges (Washington State Attorney General)", "https://www.atg.wa.gov/store-refunds-exchanges"),
    ("New York General Business Law section 218-A (nysenate.gov)", "https://www.nysenate.gov/legislation/laws/GBS/218-A"),
]
UK = [
    dict(retailer="Apple (UK)", window="14 days from receipt", holiday=None, condition="Return with the original receipt, packaging and accessories; opened software and media can be exchanged but not refunded.", url="https://www.apple.com/uk/shop/help/returns_refund", checked="2026-10-28", note="Online orders: tell Apple within 14 days, then 14 more to return."),
    dict(retailer="John Lewis", window="30 days", holiday="Gifts bought 1 Oct&ndash;24 Dec 2026 can be returned until 23 Jan 2027", condition="Unused, with original packaging and labels in good condition, and proof of purchase; items opened beyond inspection only if faulty.", url="https://www.johnlewis.com/customer-services/returns?dt=informationOnOurReturnsPolicy", checked="2026-10-28", note="Hygiene items, personalised goods and most mattresses excluded."),
    dict(retailer="IKEA (UK)", window="365 days", holiday=None, condition="Unopened products for a full refund; tested or assembled products in good condition are also taken back, refunded to a refund card.", url="https://www.ikea.com/gb/en/customer-service/returns-claims/return-policy/", checked="2026-10-28", note=None),
    dict(retailer="M&amp;S", window="28 days", holiday="Full-price items bought from 22 Oct 2026 can be returned until 17 Jan 2027", condition="Original condition, unworn and unused; hygiene and beauty items only with seals intact.", url="https://www.marksandspencer.com/c/help/returns-and-refunds", checked="2026-10-28", note="Sale items bought online: 14 days."),
]
US = [
    dict(retailer="Apple (US)", window="14 days from receipt", holiday=None, condition="Original condition with all included parts, accessories and packaging; Apple may refuse devices with active security features.", url="https://www.apple.com/shop/open/salespolicies", checked="2026-10-28", note=None),
    dict(retailer="Target", window="90 days", holiday="Bought 1 Nov&ndash;24 Dec 2026: electronics until 24 Jan 2027, Apple and Beats until 8 Jan 2027", condition="Most unopened items in new condition; opened or damaged items, or items without a receipt, may be refused.", url="https://www.target.com/help/article/000061980", checked="2026-10-28", note="Electronics 30 days; Apple and Beats 14 days; Target Owned Brands one year."),
    dict(retailer="Best Buy", window="15 days from receipt", holiday=None, condition="Like-new condition; apparel unworn with original tags; damaged items or those missing major contents may be refused.", url="https://www.bestbuy.com/site/help-topics/return-exchange-policy/pcmcat260800050014.c?id=pcmcat260800050014&intl=nosplash", checked="2026-10-28", note="Activatable devices 14 days; My Best Buy Plus and Total members 60 days."),
    dict(retailer="Costco", window="No stated time limit for most items", holiday=None, condition="Covered by a satisfaction guarantee; custom orders, tickets, gift cards and precious metals cannot be returned.", url="https://customerservice.costco.com/app/answers/answer_view/a_id/1191", checked="2026-10-28", note="Electronics and major appliances 90 days from receipt."),
    dict(retailer="Home Depot", window="90 days", holiday=None, condition="Proof of purchase needed; 30-day categories such as furniture must be unused in original factory-sealed packaging.", url="https://www.homedepot.com/c/Return_Policy", checked="2026-10-28", note="Furniture, TVs and computers 30 days; most gas generators 7 days."),
    dict(retailer="Nordstrom", window="No time limits; handled case by case", holiday=None, condition="Designer items and special-occasion dresses with tags and packaging; car seats unopened; gift cards not returnable.", url="https://www.nordstrom.com/browse/customer-service/return-policy", checked="2026-10-28", note="Marketplace sellers set their own return-by date."),
    dict(retailer="IKEA (US)", window="365 days unopened; 180 days opened", holiday=None, condition="Unopened products within 365 days; opened products within 180 days with proof of purchase for a full refund.", url="https://www.ikea.com/us/en/customer-service/returns-claims/return-policy/", checked="2026-10-28", note=None),
]
FAQS = [
    ("Can a shop refuse a return in the UK?", "Yes, if nothing is wrong with the item and you bought it in person. Citizens Advice says you have no automatic right to a refund just because you changed your mind, so it comes down to the shop&rsquo;s own policy. That changes if the item is faulty, not as described or not fit for purpose: the Consumer Rights Act 2015 gives you 30 days to reject it for a full refund. Online and phone orders also carry a 14-day cancellation period."),
    ("Do I need a receipt to return something?", "Usually you need some proof of purchase, but it does not have to be the till receipt. GOV.UK says a business can ask for proof and gives a receipt, a bank statement or the packaging as examples. In the US it depends on the retailer: Target says returns without a receipt may be limited, and Nordstrom refunds to a gift card at the current price when it has no record of the sale. Keeping the receipt or order email is the safest route."),
    ("Does the return window start from purchase or delivery?", "It depends on the retailer, so check the exact wording. Best Buy counts from the day you receive the item, while Target counts online orders from when they are invoiced, which happens when any part ships or is ready for pickup. For UK online orders, the legal 14-day cancellation period starts the day after the goods arrive, whatever the retailer&rsquo;s own policy says; a retailer can offer longer, but not less."),
]
UNVERIFIED = [
    ("Amazon UK", "amazon.co.uk help pages returned HTTP 503 to the fetcher, so the policy could not be read."),
    ("Argos", "argos.co.uk and help.argos.co.uk returned HTTP 403, so the policy could not be read."),
    ("Currys", "The currys.co.uk returns and terms pages returned HTTP 403, so the policy could not be read."),
    ("Next", "next.co.uk returned HTTP 403; only a Seasons sub-brand help page loaded, and it does not say when the window starts."),
    ("ASOS", "asos.com customer-care pages timed out on every attempt, so the policy could not be read."),
    ("Boots", "boots.com returned a bot-check page, so the policy could not be read."),
    ("Amazon (US)", "amazon.com help pages returned HTTP 503 to the fetcher, so the policy could not be read."),
    ("Walmart", "walmart.com help pages returned a robot check, so the policy could not be read."),
    ("Zara (US)", "zara.com help-centre pages returned HTTP 403, so the policy could not be read."),
]
