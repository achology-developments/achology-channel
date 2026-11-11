> CHAT DISPOSITION, S465 night postbag (11 November 2026): DONE. Written into DSRD 7 section 3.3 with the width exception; the line stays 18 on a phone; answered in RULING__Night_Postbag_For_The_Theme_Sessions_S465.md in FROM Chat, section 2.3.

**For Chat. What this needs:** note in DSRD 7 section 3.3's "Where it is built" that the pricing page's three section lines are on the component. Code, theme session, 11 November 2026 (session id 6b3d208d).

DOCUMENT TYPE: ruling. Not a page spec.

# RULING: the pricing page's supporting lines take Lead with Bar

Kain asked whether the pricing page has "our font and spacing rules applied". The read against DSRD 7 section 3.3 found the three lines under the section headings at Mulish 16/400 in soft grey with no bar (RULING__Pricing_Page_Membership_Band_And_The_Free_Tier_Leaves_S489, section 3). Shown as one switch in the Change Viewer (the theme's previews folder, pricing-s489, round-lb.js; proved by viewer_proof.py). His pick: "Yes, build it".

**Built:** theme 0.707.996, commit 445edb03, on https://achologytest.com/pricing/. The three lines carry the shared lead-bar class from base.css. The page's own stylesheet adds only the read colour and 24 above the course list's controls; the payment menu inside the schools line inherits its sentence's type. Read on the build site at 1268 and 390, equal to the round: 18/500 in brand dark, the bar outside the column and the words on the heading's edge, 16 above and 24 below, no sideways scroll.

**Two things for you:**
1. The lines run the page column's full width, 1008, past the 800 your S464 line gives. That is Kain's own S126 ruling for this page's lines, written in pricing.css: capped at 800, his line wrapped by one word. Each line fits on one line at 1268.
2. On a phone the component keeps 18, where section 3.0's phone rule would step 18 to 16. It is the component as built on every page that carries it; for you to say whether the rule or the component gives way.

**Still owed from the same read:** the two bands' ground against section 3.3a (one switch for Kain), and the small text line heights and overline spacing (Code's, by machine).

OWED BACK: the line in DSRD 7 section 3.3, and your answer to point 2.

*No em or en dashes in this file; checked before writing.*
