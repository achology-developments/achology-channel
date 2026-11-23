**DOCUMENT TYPE:** Ship brief, not a page spec.
**Date:** 2026-11-23. **Session:** S553 (Branch A, theme). **Theme version:** 0.708.396, deployed to achologytest.com.

# SHIP: the Includes tiles lead somewhere (Membership improvement 3)

**What changed.** On /membership/, the tiles that name a place on the site now lead there: Unlimited Live Sessions, Structured Mentorship, Daily Discussions and Skills Workshops go to /events/; Every Workbook goes to /learn/workbooks/. The tile's title is the link and ends on the site's text link arrow; the whole tile answers a click; on a hover the tile lifts 3 and the arrow moves 3; a keyboard focus rings the tile in orange. No title gains a line and no tile changes height at 1440, 1024 or 375. Seven Full Courses, One-to-One Coaching and Worldwide Networking stay as they were (no page of their own; the main session's ruling, which also kept Seven Full Courses off the gift page because that page offers one course, not seven). The white tiles already carried the soft warm ground the audit asked for.

**Also in this version.** The bold openings of improvement 2 are now an optional field of the opening block in its builder (previews/membership-page/build.py), switched on by a page's own leads; the other 36 pages give none and are unchanged. The built page is identical.

**Files.** data/membership-page/main.json, previews/membership-page/build.py, membership.css, style.css. Commit 8c68dedd.

**Needed from Chat.** Nothing.
