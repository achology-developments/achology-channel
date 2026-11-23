What this needs from Chat: write Kain's 23 November signature of the redraw into the About record (RULING__About_Page_Redraw_Signed_S552) and re-read the human halves of chapters 1, 7 and 8 on the redrawn page; nothing else.

**DOCUMENT TYPE:** Ship brief, not a page spec.
**Date:** 2026-11-23. **Session:** S556 (Branch E, theme). **Theme version:** 0.708.397, deployed to achologytest.com.

# SHIP: the About page redraw, built as Kain signed it

**What changed.** /about/ is now the redraw Kain signed in Safari on 23 November ("Yes, build it"), top to bottom: the Cream Hero banner with the film and the Academy's faces wall behind it; the section bar (Overview, The Story, Five Aspects, The Founders, Ten Ways, FAQs, Where to Begin); Achology: What It Is, and Who It's For as Answer Tabs (one reading column, the chosen tab off-white with the 3 orange bar) with The Thinking that Drives Achology beneath; The Achology Story in the Academy history component; Five Aspects of the Achology Experience as the school pages' one reviews block, its cards alternating film, review, film / review, film, review, two rows shown and the third behind its control; the founders on sand; Ten Different Ways as Feature and Nine (the dark DiMAP card, nine cards three by three); the questions as three cards of four, the third Recognition and Trust (Chat's ANSWER__About_Questions_Third_Card_S544); Where Would You Like to Begin?. Every word is the page's own, carried unchanged.

**How it is built.** No markup was retyped. tools/about_page_data.py lifts the signed page whole from the preview file Kain signed (previews/about-redraw-s544/about.html, only his two picks) into data/about-page/main.json; page-about.php prints it through about-setup.php, which draws the questions block and Where to Begin live from their one homes and loads the Academy and school page sheets in the preview's order. The preview's own joins, tabs and Ten Ways rules are about-page.css and about-page.js. The schema (AboutPage, Organization, BreadcrumbList, VideoObject) is unchanged.

**Proved before it shipped.** previews/about-redraw-s544/compare_built.py read every element of all nine blocks on the built page and the signed preview in WebKit (box, words, type, colour, ground, shown) at 1440, 1024, 768 and 390, and every state (each of the five answer tabs, the films control, a story chapter, the phone's swipe rows): 0 differences, page heights identical. The check was shown able to fail (105 and 97 differences against the preview's other options). On the build site after deploy, at 1440 and 390: the films alternate, all five tabs show their own answer and mark the chosen tab, Ten Ways is one feature and nine cards, the three question cards are there, no broken picture, no sideways scroll, no script error.

**Rank Math.** The page's title, description and focus keyword (post 184) were already set and the redraw kept the page's words, so they stand unchanged. The score is Kain's one-click rescore.

**Gate.** GATE_LINE

**Files.** page-about.php, about-setup.php, about-page.css, about-page.js, data/about-page/main.json, tools/about_page_data.py, previews/about-redraw-s544/sim.py, compare_built.py, built.html, style.css. Commits on main up to b55c6001.

**Needed from Chat.** (1) Kain's signature line into the About record, as the S552 ruling asks. (2) The human halves of chapters 1, 7 and 8 were read on the old page; the page is redrawn, so they need reading again on the build site.

OWED BACK: the two above.
