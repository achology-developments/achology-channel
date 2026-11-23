What this needs from Chat: nothing; a record of a ship.

**DOCUMENT TYPE:** Ship brief, not a page spec.
**Date:** 2026-11-23. **Session:** S556 (Branch E, theme). **Theme version:** 0.708.399, deployed to achologytest.com.

# SHIP: the reviews block's phone swipe rows reach the keyboard

**What changed.** On a phone (under 768) the one reviews block gathers its films into one row and its written reviews into another, each swiped sideways. The row of written reviews held nothing a keyboard can reach, so a keyboard user could not scroll it (axe scrollable-region-focusable, serious, found by the page gate on /about/ at 0.708.398; WCAG 2.1.1). Both swipe rows now take a place in the Tab order while they scroll, with the site's own focus ring, by the same keyboard-reach rule the course pages' lesson tiles already use (course-page.js, S481). On a computer, where the rows do not exist, nothing changes. Nothing a reader sees changes.

**Where it reaches.** Every page that carries the one reviews block: the seven school pages, the 27 course pages, the Access All Areas Pass, Membership (whose one row keeps its one column, so it has no swipe row) and /about/.

**Checked on the build site at 0.708.399.** /about/ and /academy/mindfulness/ at 390, loaded at 390 and loaded at 1440 then narrowed to 390: both swipe rows carry tabindex 0, the reviews row takes focus and shows the focus ring (orange on /about/, the school's own colour on Mindfulness); at 1440 there are no swipe rows. Main session's go-ahead (S552).

**Files.** course-page.js, style.css. Commit d7f602c7.

**Needed from Chat.** Nothing. The About record's accessibility line for this is closed by the next gate run there.
