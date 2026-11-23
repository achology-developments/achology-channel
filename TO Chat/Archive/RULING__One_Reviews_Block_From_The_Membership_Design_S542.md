> Disposition, Chat S480, 23 Nov 2026: written into DSRD 8 section 44; archived. No board card moved.

**Needs from Chat: a signed SWEEP brief and a WORDS file for one reviews block across every page that carries it (a Chat session is opened by Code for it). Nothing is built yet; Code shows Kain the one block on a school page and Membership side by side before any build.**

# RULING: one reviews block on every page, from the Membership design (Code, S542, 20 November 2026)

**Kain's words, in Code's S542 sitting:**
- On the school pages' "What Our Students Say About Studying at Achology": "I think that three rows deep is actually a little bit much ... keep that 2 rows deep, with the 3rd row optional".
- Of Membership's "What Our Members Say About Achology Membership": "I think there's somehow that we can make a component out of this. I think we need to agree on the title, the subtitle for all types of page, but I think we can standardize all of this and essentially just make these blocks one component ... with options to present 1 row, 2 row, 3 rows, or even 4 rows."
- "we have different videos pulled through onto these blocks per page, and also different reviews that are relevant to the page ... we just need to ensure that the appropriate reviews and videos are pulled through onto the relevant pages."
- "when a website visitor is browsing the page, they only see two rows. The third row opening up is optional for them. They can click something and a new row can open up."
- On Code's first round, which drew a new control the Membership block does not have: "you're proposing something completely different for the schools page. Do you think that's wise?" Code: no.
- To "Shall I make Membership's reviews block the one standard, two rows on the schools?": **"Yes, do that".**

**What that settles:**
1. One shared component, its look Membership's (previews/membership-page/build.py `members()`, "The School Block", Kain's "Yes, build 1" of 20 November): the heading and lead bar, the figures strip, rows of one film beside two reviews, and the two link cards at the foot (memb-ways: Member Testimonials, Student Reviews). The school and course pages' two plain text links (pf-foot, pf-go) give way to the two cards.
2. Each page chooses how many rows show: 1, 2, 3 or 4. Each page keeps its own films and reviews, in their order today.
3. Where a page holds more rows than it shows, one control inside the component opens the rest, the same on every page, between the last row and the two cards. On the school pages two rows show. Membership shows its one row and no control.
4. A phone keeps the school pages' sideways swipe (no rows there).
5. Code's four-option round (previews/school-page-s482/round-more.js) is set aside.

**Pages that carry the block today (Code's count):** the seven schools (`data/school-page/*.json`, 3 films and 6 reviews each), the 28 course pages (`data/course-page/*.json`), the Access All Areas Pass (`data/pass-page/parts.json`), and Membership (its own copy in the preview, not yet a theme template).

*No em or en dashes in this file; checked before writing.*
