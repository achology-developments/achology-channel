# SHIP: The Courses Page, Simplified, Linkable by Goal, Three Questions a Card (S562)

Shipped 23 November 2026 at theme 0.708.438 (main 20b76bce, branch courses-review/s562), on Kain's "Yes, ship it" after he saw the built page in the Change Viewer (previews/courses-review-s562/round-2.js, viewer_proof PASS). Deployed by deploy.py from a clean worktree: server, local and zip agree. Carried forward unchanged by the next deploy (0.708.439 live at the check below).

What shipped, from RULING__Courses_Page_Purpose_And_Improvements_S562:
1. Simplified. Every S180 extra off (torchlight, grain and foot glow, counting overline, answers cascade, hairline glint, spring press, tick draw, follow-along bounce and nudge, focus pull, Best match shine, ring pulse); Courses Rise In kept. Sort words 16 either side (8 on a phone) inside the button family's tab frame; the instruction line under the answers removed; the page foot is the questions band's 64 (48, 32), not 96 (scoped to /courses/).
2. /courses/?goal=WORD[,WORD] opens the page with those goals ticked. Fifteen fixed link words in template-courses.php, sent to the main session.
3. Three questions a card on /courses/ only: 399, 402, 400 / 329, 327, 332 / 341, 333, 249 (Chat's picks).
Also: the questions' hidden hover arrow taken out of the line on /courses/, so a full last line leaves no blank row.

Checked on the live page at 1440 and 375: goal ticked from the address, heading "Courses Best Aligned With Your Goals", instruction line gone, 3/3/3 questions, sort padding 16/8, foot 68/36 (the band's 64/32 plus the footer's 4 stripe), only cdRise moving, no script errors. Built mode also judged at 1024 before the ship.

Page gate rerun on /courses/ at 0.708.438: 43 passed, 5 failed, 8 review, 22 carved out. None of the five comes from this change:
- boundary-owner, desktop boundary 1 (results to questions band): the Explore More button's own 12 padding read as the last edge; the space measures 48 as wanted. Unchanged by this ship.
- supporting-line, phone: the questions band heading at 21 on a phone, the band's own phone size (help.css), unchanged.
- rank-math 86 under 90, keyword 'achology courses': read from the install; template copy is not what Rank Math scores.
- icon-registry: the course card's guarantee badge drawing (28 copies), the card component's.
- dsrd6-record: the page's DSRD 6 record has open sections.

For Chat:
- DSRD 7 5.2.1's square-check entry names the instruction line under the goals, which is gone; the icon is no longer used on /courses/.
- The 96 foot came from the shared .cd-credit margin inside .q-band; other pages ending on the questions band may carry it. Fixed for /courses/ only.
- The hidden arrow's blank row is the shared questions block's (help.css .q-link__q::after); fixed for /courses/ only, worth a site-wide look.
- DSRD 7 4.3 Exception 15's "12 between the answer tiles" still stands; nothing else in it changed.
