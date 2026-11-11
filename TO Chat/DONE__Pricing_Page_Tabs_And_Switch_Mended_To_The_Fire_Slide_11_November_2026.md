**CARRIED (Chat, Session 464, 11 November 2026):** not yet acted on; the session closed for length on Kain's yes. It is Session 465's first act.

**For Chat. What this needs:** one read, and your call on the two points in section 4. Code, theme session, 11 November 2026 (the pricing page review sitting; session id caad3927).

DOCUMENT TYPE: DONE

# DONE: the pricing page's course tabs and payment switch mended to the Fire Slide standard (theme 0.707.960)

## 1. What Kain asked

He opened this sitting for one job: review the pricing page top to bottom, list every improvement, then make them with him. He was given a list of 23 and said "Yes, start" to the first group, the broken buttons.

## 2. What was wrong, measured in WebKit on the build site

The course tabs were drawn twice. The S209 sliding orange underline (theme commit 8cd05e45, 2 November) was still on the page, and the button family (commit 89ecf430, 3 November) had added its sliding fire frame on top. The tabs had no padding, so the frame hugged the words and stood proud of its track. On a phone the three tabs stacked inside one tall rounded shape. The payment switch stood 36 tall with 16 each side beside tabs 44 tall.

## 3. What was built (commit fbc340b5, deployed, version 0.707.960)

DSRD 7, the button family, Tabs and switches: Fire Slide (pick 7), quoted: "One pill track (999, 1px hairline #EEEDED, 4 inside); tabs Como 14/600, 40 tall, 18 each side ... A tab row never wraps: on a phone it slides sideways inside itself. It covers the Courses sort, the pricing tabs and plans".

- Both rows are now one pill track with 4 inside, each member 40 tall with 18 each side (pricing.css).
- The S209 underline is out of the markup, the stylesheet and the script. The dark chosen plan rules are out too; they were already overridden by the family.
- A row wider than its column slides sideways inside itself, and a pressed tab is brought into view; the page itself never moves (pricing.js).
- The tab row's column gap is 16 in place of 24, so both tracks share one line in the 1008 column, as Kain asked at S209.

Proof, read on https://achologytest.com/pricing/ at 0.707.960: at 1268 the tracks are 702 and 283 wide, 48 tall, on one line; the sliding frame's box equals the chosen member's box after each press; with all 28 courses showing the frame is hidden and returns on Back to Categories; aria-pressed follows each press; no sideways page scroll at 1268, 834 or 390; css_gate passes on pricing.css.

## 4. Two points for Chat

1. At tablet width (834) the tab row is 702 wide in a 674 column, so the last tab's end is cut by 28 until the row is slid. That is the standard as written. Say if the pricing page should take a named exception there.
2. The prototype in the Pricing Page folder now shows the old tabs. Its re-export as APPROVED is already a theme queue line; it will be made from the page once this sitting's list is finished and Kain has read the page.

3. Added later the same sitting, from a page gate run on /pricing/ at 0.707.965 (48 passed, 15 failed, 13 for review): the accessibility scan names one link, "Read the refund policy" in the membership terms line (class bf-in), under axe's link-in-text-block rule. The link is drawn to Kain's pick 12, the faint line at 25 per cent (buttons.css section 4), so the fix is not this page's to make: every in-sentence link on the site is drawn the same way. Say whether it is a recorded exception for the standard, or whether the faint line's strength goes back to Kain. The scan's other line is the cookie plugin's own button, already job R1.

The deploy check reported one file not this session's as differing on the server, template-accreditation.php; it belongs to the Accreditation session and was left alone.

OWED BACK: Chat's call on section 4 point 1.

*No em or en dashes in this file; checked before writing.*
