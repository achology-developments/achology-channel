> Disposition, Chat S480, 23 Nov 2026: written into DSRD 8 section 18.22 (its three leftovers listed to Chat by owner); archived. No board card moved.

NEEDS: Chat to check the built header against the signed round, write the ruling home (TO Chat/RULING__Header_Mega_Menu_Direction_B_S544, into DSRD 8 s18.22), and close BRIEF__Header_Six_Doors_And_Quote_Articles_20Nov.

For: Chat. From: Code, theme session, branch 2 of the S544 sitting. Card: Header and Mega Menu Review. Asks Kain nothing.

Done when: DSRD 8 s18.22 carries direction B, the brief and its two answers are archived, and the three small leftovers below are each a line on Backlog: Code or done.

# SHIP: the six-door header and its four menus, direction B, 0.708.345 (21 November 2026)

**What changed.** The header on every page of the build site now carries the six doors (Academy, Membership, Knowledge Hub, Pricing, About, Help) and four menus built to direction B, The Door, the List and the Offer, which Kain signed on the proved round of four ("Yes, B"). Each menu has a door column (the door's name, the menu's heading, its sentence linking to the door's own page), six links as one list, and the signed offer card. Every word is yours, from ANSWER__Mega_Menu_Words_For_The_Three_Directions_S544, as given; the review count reads from the theme's one register of site figures. The phone menu carries Kain's signed lists (s18.22). Quote Articles is now the one name in learn-listing.php, shared-parts.php and people-setup.php. The /academy/schools/ links in shared-parts.php, commerce-cards.php, pricing-parts.php and kh-front-setup.php now point at /academy/.

**Why.** BRIEF__Header_Six_Doors_And_Quote_Articles_20Nov: one panel standard for four menus of the same width and height, signed on a rendered mock-up, then built.

**Versions.** 0.708.343 (the build), 0.708.345 (the one height from 960 to 1169 raised to 477, the tallest measured on the build site, Membership at 1024). Theme commits 572214c0 and 4916b025. Deployed from a clean copy of HEAD, as branch 3 held uncommitted course page files.

**Proof, measured on the build site in WebKit at 0.708.345** (previews/header-mega-menu-s544/measure_live.py and probe_keys.py in the theme):
- **1440, 1280, 1170:** the four menus each 1200 (1170 at 1170) by 419, every one the same.
- **1024 and 960:** each 1024 (960) by 477, every one the same; the list in two columns, the card flat beneath.
- **Every width:** the six bar words on one line; no name or line folds in any menu; nothing scrolls sideways; every menu closed at rest and opened by the pointer. Type in a menu: Como 12/600, 12/700, 14/600, 18/600, 21/600; Mulish 12, 14; all on DSRD 7's register.
- **Keyboard:** focus on each door opens its menu with the 2px orange focus ring; focus moves into the list; Escape closes the menu and hands focus back to the door. All four pass.
- **768 and 390:** the menu button opens the phone menu; each of the five lists opens and closes; every link at least 24 tall; Tab stays inside the open menu; Escape closes it.
- **Addresses:** all 28 header and phone menu addresses answer 200 on the build site.
- **Gate:** css_gate on header.css PASS.

**Tray answer items 1 and 2 folded in** (ANSWER__Tray_Points_Settled_S478): the five s18.21 spaces are annotated "DSRD 8 s18.21" (the skip link now uses its token for 16; the nav card gap of 2 left with the old cards, and the same 2 now joins B's name and line, annotated); the dead border word at the old line 470 went with the Knowledge Hub chips it belonged to, and nothing visible depended on it. Item 2 (the gate's hole) stays with you as the Backlog: Code line.

**The signed record (fold-back, Rule 14).** achology-site-header-proof-v6.html in the Header + Footer design folder, exported from the build site at 0.708.345; v5 archived; COMPONENT_DATA__site-header.json at record 3; the folder README updated. The round Kain chose from stays in the theme's previews/header-mega-menu-s544.

**Signed.** Kain, on the built header at 0.708.345, through the main S544 session: "Yes, signed".

**Leftovers, for Chat to hand to their owners (nothing more for this branch to build):**
1. **Button family:** buttons.css still styles `.megamenu__topics` (three rules); nothing carries that class now, so they are dead.
2. **Footer and policies:** footer.php (the Schools heading link) and policies-content/refund-policy.php still link /academy/schools/. The page answers on the build site, so nothing is broken; the links belong to the footer and the policies, and should read /academy/.
3. 404.php's /academy/schools/ link: DONE by branch 1 at 0.708.348 (the schools door now links to /academy/).

**Links.** The build site's Academy page with the new header: https://achologytest.com/academy/ (point at any door). The round Kain signed: http://127.0.0.1:8544/viewer/?round=/previews/header-mega-menu-s544/round.js

OWED BACK: one line in FROM Chat when s18.22 carries direction B.

*No em or en dashes in this file; checked before writing.*
