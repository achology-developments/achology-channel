> Disposition, Chat S480, 23 Nov 2026: written into DSRD 9 section 47.5; archived. No board card moved.

**DOCUMENT TYPE:** Ship brief, not a page spec.
**Date:** 2026-11-22. **Session:** S553 (Branch A, theme). **Theme version:** 0.708.394, deployed to achologytest.com.

# SHIP: the section bar on the Membership page (Membership improvement 1)

**What changed.** The course pages' own section bar (course-page.css .snav and course-page.js, reused unchanged, as Kain ruled at S551) now sits under the Membership banner. It sticks under the site header, marks the block in view, and a click glides to that block's heading, 24 under the bar. On a phone it scrolls sideways with the course bar's soft edges. Eight labels: Overview, Includes, Live Events, Your Week, Your Path, Reviews, Pricing, FAQs. Four are the course bar's own labels for the same jobs (Overview, Reviews, Pricing, FAQs); the other four are the names in Kain's improvement map. The Path band gained an id so its label has somewhere to land, and each block lands clear of the bar when the page opens on its address.

**Why.** Kain's improvement 1 (previews/membership-page/audit-s551/reach.html): "A Slim Guide That Follows You Down the Page".

**Needed from Chat.** If Chat would rather word the four Membership-only labels (Includes, Live Events, Your Week, Your Path), they are one list in previews/membership-page/build.py (SNAV); Code places any change.

**Files.** data/membership-page/main.json, previews/membership-page/build.py, membership.css, style.css. Commit 2d101bec.
