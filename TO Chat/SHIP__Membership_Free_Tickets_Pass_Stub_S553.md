**DOCUMENT TYPE:** Ship brief, not a page spec.
**Date:** 2026-11-22. **Session:** S553 (Branch A, theme). **Theme version:** 0.708.389, deployed to achologytest.com.

# SHIP: the free event tickets carry the Boarding Pass lines (Membership improvement 4)

**What changed.** The four free event tickets in the dark events band (the Academy page's band, which the Membership page draws from the same stored block) now carry the Events page Boarding Pass's own lines: under the time, the open lock with the event's access word ("Free", read from the event's own record, no new words); on the soonest ticket, above the event name, the pass's own countdown ("Starts in 14 hours, 27 minutes"), worked out on the visitor's clock and refreshed every half minute. Every ticket keeps one height at computer and tablet width.

**Why.** Kain's improvement 4 (previews/membership-page/audit-s551/reach.html): "Free Events as Real Tickets", merge the Academy band's tickets and the Events page's pass into one ticket. The tickets already had the pass's notched stub; this gives them the pass's Free line and countdown, so the two are one design. Nothing was redrawn: no new shape, stamp or chip.

**Pages it reaches.** /academy/ and /membership/ (one stored band).

**Files.** academy-setup.php, academy.css, academy.js, style.css. Commit 5bc4f483.

**Needed from Chat.** Nothing.
