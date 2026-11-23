What this needs from Chat: note the Policies index redesign on its card and in DSRD 9 (the page's layout has changed); answer ASK__Policies_Index_Bands_Exception_S555.

**DOCUMENT TYPE:** Ship brief from Code (Branch D, S555), not a page spec.
**Date:** 2026-11-23
**Shipped:** theme 0.708.401, then 0.708.402. Build site: https://achologytest.com/policies/

# SHIP: the Policies index, redesigned, 0.708.402

**What changed.** Kain asked for the main policies page to be brought back in step with the rest of the site. He signed the redesign on its whole-page preview: "Yes, sign it" (RULING__Policies_Index_Redesign_Signed_S552). Every word on the page is Kain's or Chat's.

1. **The frame and rhythm.** The page now uses the site's 1200 frame, with every block on the same left edge as the Academy, Help and Pricing pages. Light Sand and white bands take turns at 64, 48 and 32, with no hairlines between them.
2. **The banner.** Light Sand, two columns. On the left: the title, Chat's line (ANSWER__Policies_Banner_Line_84_S552, one row at 1440), and three facts in the course heroes' icon rail (Seven Legal Policies, Registered in Scotland, UK, Free for Anyone to Read). On the right: a small fanned stack of three of the page's own documents, white cards with their icons. The stack is beside the words on a tablet and dropped on a phone.
3. **The text band.** "Who Runs Achology, and the Standards We Keep", with its line, then Kain's facts in Chat's two paragraphs (ANSWER__Policies_Index_Banner_And_Intro_S552), each in its own card. That card pair is one shared pattern, .intro-pair in policies.css section 22, which the Presuppositions page also uses. The paragraphs are body 16 under the 18 line and end level at 1440 and 1024. Both outbound links are kept (Companies House, tradingstandards.uk).
4. **The documents.** The ten documents are now the Help landing's category card with an icon square, in their signed order. The legal seven sit three then four across, and the standards three keep their orange top edge.
5. **The block standard.** Every block opens the same way: a Como 24/600 heading and a Lead with Bar line, using Chat's one-line leads (ANSWER__Policies_And_Presuppositions_One_Line_Leads_S552). More About Achology now opens the same way too.
6. **Removed, on Kain's signature:** the per-card ghost words (S043) and the word "policies" behind the title (S203), on this page only. The old row-card rules went with them.
7. **Theme files.** template-policies-index.php, policies.css (sections 21 and 22), shared-parts.php (six Lucide icons: cookie, rotate-ccw, handshake, info, accessibility, landmark), style.css.

**Proof.**
- The built page against the signed preview at 1440, 1024 and 375: zero differences.
- page_gate at 0.708.402: 53 pass, 18 fail. The 18 fails are 15 band lines waiting on the ASK, the site-wide chapter 7 line, Rank Math at 85 (the S203 exception, waiting on Kain's rescore) and keyword density (template words).
- axe: zero violations.
- All 14 links return 200.
- css_gate PASS.
- deploy.py: local, the server and the zip agree.
- The DSRD6_RECORD is updated: chapters 2, 10 and 11, and an S555 section.

**Needed from Chat:** the ASK above; the card; DSRD 9's Policies index section (the signed S389 spec describes the old 800 column and row cards).

OWED BACK: the ASK's answer.

*No em or en dashes in this file; checked before writing.*
