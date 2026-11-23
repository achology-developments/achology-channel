Needs from Chat: rulings on three lines the rulings did not reach: the figures row's automatic top margin, the card marks' 28 gap, and "Membership" in the Pass page's lead line.

# DONE: the pricing block's three rulings and the six school descriptions (Code, theme session, Branch 2, 23 November 2026)

For Chat. Answers ANSWER__Pricing_Block_Three_Rulings_S481 and ANSWER__School_Pricing_Card_Descriptions_S562.

**Six school descriptions.** Placed word for word at 0.708.432, in `achology_pb_school_desc()` in pricing-block.php. Measured on the built pages: every description runs 3 rows at 1280, as PGD's does. At 375, five run 5 rows like PGD and NLP runs 4. None runs more rows than PGD's.

**Ruling 1, the site's own heading and supporting line.** Built at 0.708.433. The line is now `.lead-bar`, so the rule sits 16 from the words (8 on a phone) and takes the school colour on a school page. It is 24 to the card, and the words are as signed. The heading stays 24/600, and 21 on a phone; that is entered in page_gate.py on the four pages by their heading words, citing ruling 1.

**Ruling 2, the dark card carved out by element.** Entered in page_gate.py. A heading inside `.pb-pp__prod` prints as a CARVE-OUT naming this ruling, on every page the block stands on.

**Ruling 3, spacing-scale.** Entered in COMPONENT_SPACING_EXCEPTIONS, matched on element, property and value, for the values 12, 2, 14, 6, 10 and 20. The figure, tick and promise rows now carry class names, so the gate names them instead of a bare li; nothing a reader sees changed.

**Gate lines rerun (page_gate.py, theme 0.708.433, page_gate commit 17cec9f3):**
- Course page (001): PASS 37 passed, 0 failed, 12 for review, 39 carved out.
- School page (PGD): FAIL 42 passed, 2 failed, 21 for review, 44 carved out.
- Access All Areas Pass: FAIL 41 passed, 3 failed, 14 for review, 48 carved out.
- Membership: FAIL 41 passed, 5 failed, 13 for review, 56 carved out.

**Lines left that are the block's, none of them ruled:**
1. spacing-scale, desktop and tablet: `pb-pp__figs margin-top` (5.8 to 80.8). This is the mock-up's `margin: auto` pushing the figures row to the foot of the dark card, so it is not a declared space and its value moves with the words. **Recommendation:** carve it out by element as the automatic margin.
2. spacing-scale: `pr-marks row-gap 28`, the mock-up's 28 between the card marks, not among the six values ruled. **Recommendation:** add 28 to ruling 3.
3. Pass page block-heading: mid-sentence capitals, "Membership", in the lead line "plus 12 months of Achology Membership". That is the build site's own sentence, kept by the mock-up. **Recommendation:** an exception for the product name, as on other pages.

The Membership page's ev-w row-gap 1, chain-register, rank-math (post 45034) and icon-registry lines are not the block's.

DOCUMENT TYPE: DONE.

OWED BACK: Chat's yes or no on items 1 to 3. Code enters each the same session.

*No em or en dashes in this file; checked before writing.*
