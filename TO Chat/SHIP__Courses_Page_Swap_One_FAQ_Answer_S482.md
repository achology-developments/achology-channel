NEEDS FROM CHAT: nothing; for your record. Code, Branch 1 of S562 (for the new main session, local_5a6f4d85), 23 November 2026, theme 0.708.442.

# SHIP: the Courses page's How Courses Run column reads 329, 327, 330 (answers ANSWER__Courses_Page_Swap_One_FAQ_Answer_S482)

- **The change:** template-courses.php, the questions block's How Courses Run card: 332 out, 330 in ("What's inside an Achology course module?", published). The other eight are kept: Where to Begin 399, 402, 400; Paying and Access 341, 333, 249. Commit d728bce0 on main. Fetched right before the deploy (main unchanged); deployed from a clean copy, server, zip and version proved at 0.708.442.
- **Read back on the build site:** /courses/ shows How Courses Run as "How do Achology courses work?", "How long do Achology courses take to complete?", "What's inside an Achology course module?". 332's question ("...Masterclasses and practitioner courses?") is no longer on the page.
- **Page gate rerun on /courses/ at 0.708.442:** 43 passed, 5 failed, 8 for review, 22 carved out. The same five as at 0.708.438 and 0.708.439 (SHIP__Courses_Page_Simplified_Goal_Links_Three_Questions_S562), none from this change: boundary-owner (the Explore More button's 12 padding read as the edge, the space measures 48), supporting-line (the FAQ heading 21 on a phone), rank-math 86 under 90, icon-registry (the course card's guarantee badge, 28 copies) and dsrd6-record (open sections).
- 332's own Help answer title still carries the word. As your answer says, that is yours to rule separately.

DOCUMENT TYPE: ship.

*No em or en dashes in this file; checked before writing.*
