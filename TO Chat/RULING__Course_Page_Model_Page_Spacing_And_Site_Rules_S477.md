RULING, for Chat: Kain's yes on the course page's evened spaces, shipped at theme 0.707.931 on all 28 course pages. Needs from Chat: write section 1's corrections home in DSRD 7 and the course page signed spec, and rule on section 3's four gaps, which Kain cannot see and Code will not decide.

**Theme session S477, 11 November 2026. Ship brief and ruling in one file.**

## 1. What Kain said yes to, and what shipped

Code measured the built course page whole (courses 001, 019 and 023 at 1280, 1024, 834 and 390) and showed Kain the plain faults as one Before and After in the Change Viewer. The question put to him, in the main course page session: "Shall the course page review put the evened spaces onto all 28 course pages?" Kain: "yesw" (a yes with a slip of the finger, carried word for word by that session).

Built at 0.707.931 (theme commit efd4e3cb; rules in tools/course_page_flatten.py, so a regenerate keeps them):

1. **The space under a block's supporting line is 24 at every width**, as DSRD 7 section 3.3 already says ("16px under the block heading and 24px above whatever follows the line"). It was 32 on the certificate block, 48 on the curriculum (32 on a phone), 32 on the reviews, 64 on pricing and 32 on the questions. No change to the standard; five blocks brought onto it.
2. **The questions block sits on Light Sand**, not the cool off-white. DSRD 7 section 3.3a rule 6: "The cool off-white #F3F4F4 and the warm cream #FDFAF8 stop being section grounds", and rule 5: white cards sit on the tint. **One correction for Chat:** 3.3a's "Where it is built" line for the course page preview says "questions white, close sand". The cards turned white at pick 291 and the close left the page at pick 296, so the built run is: description white, outcomes sand, certificate white, curriculum sand, reviews white, pricing sand, free lessons dark, questions sand.
3. **The free lessons title sits 16 over its line** like every other heading (it was 24). On a phone that block's bands, and the space between the Diploma card and the bundle card, step from 48 to 32, as section 4's mobile reduction says.
4. **Two small texts brought over the contrast floor:** the three labels under the video to the soft grey #5E6B75 (they were the mid grey at 12px, 3.2 to 1), and the bundle rows' saving pill words to the text-safe orange #B8460F (4.1 to 1 on the pill's tint).
5. **A part reached with the Tab key is kept clear of the buy bar** (the page scrolls it into the clear).

Measured after, on the build site, the three courses at four widths: heading to line 16 and line to what follows 24 on every block. css_gate passed on course-page.css. The page gate still cannot read a draft (asked in ASK__Course_Page_Built_Into_The_Theme_Seven_Things_Owed_S472). Recorded as pick 305 in the course page PICKS.md.

## 2. The one figure still off the rule, and why

The free lessons block keeps 48 between its supporting line and the Day 1 band. Kain signed that block as three bands 48 apart (picks 286 to 289). Code puts it to him alone, next, with a recommendation to keep it as that block's recorded exception to 3.3.

## 3. Four gaps in the standard this page exposed (for Chat; nothing a visitor could see, so not put to Kain)

1. **Line height.** DSRD 7 names a line height per role, but this one page draws 14px Mulish at five line heights (19.6 to 22.4), 16px at three and 12px at five. Wanted: one line height per size for small text.
2. **Text on dark.** White text is drawn at eleven strengths (0.56 to 0.9). Section 1.1 names roles on light grounds; it needs two or three named strengths on the brand dark.
3. **The focus mark.** It is drawn seven ways on this page (2px orange at 2, 3 or 4 off; 3px dark; a white inset ring; 3px peach). Section 5.3 says a ring radius "never had a rule to follow"; the ring itself has no rule either.
4. **Small capital labels** are spaced three ways (0.48, 0.96 and 1.44px) against section 3.1's Overline row (0.08em).

## 4. Decisions still to be put to Kain, one at a time, each to become a rule

Card corners (12, 16, 20 and 24 on one page, against 5.3's cards 12 and panels 16); how a small white card is edged (three ways today); text on a phone (3.0's phone rule says headings 21 and reading text 14, the page keeps 24 and 16); how wide a supporting line runs (616, 720, 800 and full width). Each yes will arrive as its own line added to this file.

## 5. Also new in the theme

tools/course_page_measure.py: reads a built course page whole and writes every block's spaces, every text style, every edged box, every control, contrast under AA, motion left under reduced motion, the heading order and each Tab stop's focus mark. It reads; it changes nothing. The site-wide standards session has the same findings.

OWED BACK: Chat's corrections to DSRD 7 3.3a's course page run, and a ruling on each of section 3's four gaps.

*No em or en dashes in this file; checked before writing.*
