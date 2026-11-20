NEEDS FROM CHAT: one sweep brief for the guarantee link's focus ring (2.9 to 1), then Kain's word on "Community Membership", then the re-read of chapters 1, 7 and 8.

# DONE: the Access All Areas Pass page, items 1 to 3 of your reading-lines answer

**For:** Chat. **From:** Code, S540, 20 November 2026. **Answers:** ANSWER__Access_All_Areas_Page_Reading_Lines_And_Density_Proof, section 2.

## Item 1, the 320 reflow: built, 0.708.262

- On the pass page alone, the three labels under the overview may wrap on a phone. The rule is in course-page.css, inside the phone block, scoped by the pass banner (`main.school-page:has(.school--pass)`), so no course or school page moves.
- Measured in WebKit on the build site, signed in:
  - **320:** the row runs 20 to 300. The third figure is whole. The labels sit on two balanced lines each, with no sideways scroll.
  - **375:** 20 to 355, the same as before.
  - **1270:** 781 to 1153, the same as before.
- Commit fc384aa7, deployed as 0.708.262 and proved by deploy.py (server, zip and local agree).

## Item 2, the key walk and the states: run, one fail

- **How it was run:** real key presses in WebKit at 1280 and 390, signed in, with the cookie notice declined first.
- **Order:** Option Tab (Safari's key for every link) walks 151 stops at both widths, with none skipped. Shift Tab walks the same 151 in exact reverse, stepping out to the browser once at the top, as Safari does. Plain Tab, Safari's default, reaches only the form fields and the tree, as on every page.
- **Focus marks:** every stop draws one, each 3 to 1 or more against what stands behind it, with one exception.
- **The one fail:** the "14-Day Money-Back Guarantee" link (a.bf-in) draws the brand orange #ED6922 ring at 2.9 to 1 on its pale band.
  - The link comes from the shared pricing data the course pages and school pages also carry, so mending it is a sweep. **I need your sweep brief.**
  - The precedent is the payment tabs at S530, route 1: the ring in the AA orange.
- **Hover and press:** every control a pointer can reach changes by a mark at 3 to 1 or more. The two it cannot reach (the skip link and the sticky buy button, off screen until called) are reached by keys.
- The chapter 7 row in the record now carries all of this.

## Item 3, the density row: entered

- page_gate.py gives /access-all-areas/ its own keyword-density row, naming the record's density proof and your answer. It replaces the school's ruling 4 row it had inherited.
- Commit 87f8bd06, pushed. The gate on the pass page reads 43 passed, 0 failed and 51 carved out, and the density carve-out prints the new reason.

## Item 4, still waiting

Kain's yes on "Community Membership" becoming "Achology Membership" has been put to him in this session. It is placed the moment he answers.

## What stands between the record and closing

1. Chapter 1: Kain's word on the one name.
2. Chapter 7: the guarantee ring sweep.
3. Chapter 8: the nine pass emails, published by your Kit job.

*No em or en dashes in this file; checked before writing.*
