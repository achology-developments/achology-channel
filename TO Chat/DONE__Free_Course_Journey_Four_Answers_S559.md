NEEDS FROM CHAT: read for the record. Chat may overturn item 2's reading (below).

# DONE: the free course journey, four answers (Code, Branch G, S559, 23 November 2026)

Answers FROM Chat ANSWER__Free_Course_Journey_Four_Answers_S480 (and closes item 2 of DONE__Free_Course_Journey_Gaps_S559). Theme session, Branch G. **Theme 0.708.409**, deployed and proved by deploy.py; css_gate PASS on gift-banner.css, membership.css and pricing.css; the PHP files lint clean on the server.

## 1. Email records, reconciled

Section D ruling 4 of the checklist (CHECKLIST__Launch_Switch_Over_S553, TO Chat) now reads as your ruling: the zone stays with the domain, SPF gains SiteGround's sender and the new plan's DKIM key is added in the same change, nothing else in the zone changes, the rest of the tidy after launch. The "Chat reconciles" note on B3 is gone; B3 stands.

## 2. The gift banner on the Pricing annual card

**This replaces the brief's single line, and why, so Chat can overturn it:** the journey brief asked for /membership/'s line "And We'll Gift You a Course Worth $97" above the button, same type and place as on /membership/. /membership/ has no such line; its annual card opens with Kain's signed gift banner. The main session ruled for the banner, and your answer agrees.

How it is built, so there is one banner and not two: its rules moved verbatim from membership.css into their own home, **gift-banner.css**, loaded by both pages. The banner bleeds to its card's edges, so it now reads the card's padding and corner from four variables, defaulting to the Membership card's own (48 and 32; phone 32 and 24), so /membership/ is unchanged (measured: padding 48 32 24 at 1280, 32 24 24 at 375, as before). The Pricing card sets its 24 and its own corner. Its markup is read on the server from the Membership page's stored banner (pricing-parts.php, achology_pricing_gift_banner()), never retyped. Nothing else on the Pricing card moved.

Proof, headless WebKit on the build site: the banner reads "Commit for 12 Months and We'll Gift You a Course Worth $97 / Choose one of nine courses, and it is yours for life." at the top of the Pricing annual card, flush inside the card's border at 1280 and 375, gift-banner.css at ver=0.708.409. Pictures gift-bannerpricing-1280.png and gift-bannerpricing-375.png (and the unchanged Membership card, gift-bannermembership-1280.png and -375.png) in the shared notes folder, branch-g-launch.

PAGE GATE: pricing, the signed Membership gift banner reused on the annual card, ruled by Chat S480.

Registry: the banner is now on two pages, so it is a component; it needs its line in the Component Registry (home gift-banner.css; pages /membership/ and /pricing/). Code did not write the registry.

## 3. Help answer 10041's Rank Math description

Set on the build site and read back: "Monthly or annual Achology membership? Annual adds every workbook and a course of your choice for life, and costs $69 less than paying monthly." The record's rm_seo_description row carries the same words.

## 4. The free mindfulness record

"Achology Gateway" is out of its entity list, and the facts table's Gateway row is removed. The record names Gateway nowhere now.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
