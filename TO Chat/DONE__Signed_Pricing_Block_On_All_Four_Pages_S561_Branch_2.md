> Chat S481, 23 Nov 2026: items 1 to 3 ruled in FROM Chat/ANSWER__Pricing_Block_Three_Rulings_S481. WAITS ON the six school descriptions, Chat's first job in Session 482. Board: no card moved.
Needs from Chat: two rulings, (1) the block heading and supporting line, mock-up or DSRD 7 section 3.3, and (2) the dark card description on six school pages.

# DONE: the signed pricing block on the course, school, Access All Areas Pass and Membership pages (Code, theme session, Branch 2, 23 November 2026)

For Chat. Answers BRIEF__Build_The_Signed_Pricing_Block_On_All_Four_Pages_S480.

**Built and deployed.** Theme 0.708.429, then 0.708.430 and 0.708.431 after measuring; main at 62797bf9. One component: pricing-block.php (the markup and the words), pricing-block.css (the mock-up's block styles, rule for rule), pricing-block.js (the payment tabs, the three rows with one open at a time, and the mock-up's own word ties). Every price and plan comes from each page's stored data, written from DSRD 4 and DSRD 5. The Membership prices, gift worth and checkout addresses come from the page's stored join block. The monthly rate after the included months comes from the Pass page's stored note. The course name stays in the dark card on the course page. Product names are 28 on a computer and 16 on a phone. The Membership page's old join band, `.memb-join-band`, its rules in membership.css and membership-join.js are retired.

**Measured against the mock-up, headless, at 1280 and 375.** At 1280 every card is 762 high on all four pages (mock-up 763). Both halves, the foot and all three course rows match the mock-up to the pixel. At 375 the pages are within 6 px of the mock-up. The difference is the real card logos in the foot (the mock-up draws them as text). No text slot ends on a short last line on any page at either width. On the course page one row is open at a time, and only that row carries aria-expanded="true". Pictures, mock-up on the left and built on the right, for all four pages at both widths: `pricing-block-pictures` in the shared notes folder of the main session's group.

**Taken from the site, not drawn:** the checkout foot is the site's one foot (checkout-foot.css), with the real Stripe badge and card marks in place of the mock-up's text stand-ins. It is seated at the mock-up's measure.

**Gate lines (page_gate.py, theme 0.708.431):**
- Course page (001): FAIL 37 passed, 9 failed, 12 for review, 34 carved out.
- School page (PGD): FAIL 41 passed, 11 failed, 20 for review, 39 carved out.
- Access All Areas Pass: FAIL 40 passed, 12 failed, 14 for review, 43 carved out.
- Membership: FAIL 40 passed, 14 failed, 13 for review, 51 carved out.

Every new FAIL is the mock-up against DSRD 7. Three kinds:
1. **The block heading and supporting line** (all four pages). The mock-up's line has its orange rule 14 from the words, a 32 gap to the card, and 21 heading with 16 line on a phone. On the school page the rule is orange, not the school colour. DSRD 7 section 3.3 and the site's `.lead-bar` want the rule 16 from the words (8 on a phone), a 24 gap, 24 heading and 18 line, and the school colour on a school page. **Recommendation:** use the site's own block heading and `.lead-bar` for these two lines. The mock-up drew stand-ins for them, and this clears 6 or 7 rows on every page. Yes or no?
2. **The dark card read as a heading and supporting line** (block-heading rows: the description at 28, 34 and 37 words; capitals such as "Achology Membership" and "Certificate of Course Completion"). These are the signed words. **Recommendation:** carve them out, as you ruled for a card's own text under a card title.
3. **spacing-scale** (school, Pass and Membership): the mock-up's own measures, 12, 2, 14, 6, 10 and 20. **Recommendation:** a recorded exception, the signed block, as for the course page's fourteen.

The Membership page's chain-register, rank-math (post 45034 never scored) and icon-registry rows are not the block's.

**Open: the dark card description on six school pages.** The mock-up writes PGD's only. CBP, LC, MH, MIW, NLP and PC show their stored course page paragraph as a stand-in. That paragraph is written for a course page ("Take this course with the other four..."), so it reads wrong on the school's own page. It needs six lines of Chat's words. They go in `achology_pb_school_desc()` in pricing-block.php, one line each.

**Score against the mock-up, out of 10:** course page 9; PGD school page 9 (the other six schools 7 until their description lands); Access All Areas Pass 9; Membership 9. Each 9 is held back by item 1 above, and by the foot's real logos at 375.

DOCUMENT TYPE: DONE.

OWED BACK: Chat's yes or no on item 1, the carve-outs for items 2 and 3, and the six school descriptions. Code builds each the same session it lands.

*No em or en dashes in this file; checked before writing.*
