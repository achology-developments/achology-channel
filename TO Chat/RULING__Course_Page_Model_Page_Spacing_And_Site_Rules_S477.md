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

The free lessons block keeps 48 between its supporting line and the Day 1 band. Kain signed that block as three bands 48 apart (picks 286 to 289).

**Settled, 11 November 2026 (pick 306): held as signed, a named exception to section 3.3 for this one block; Kain may overturn.** Kain typed no answer. The main course page session, which is running the sessions for him, held the block as signed because keeping it changes nothing he approved. Code had built the closer version as a preview (round mp-2), looked at it in WebKit and recommended the same: at 24 the block's two figures sit on top of the sign-up panel and its three even bands are lost. Nothing was built. For DSRD 7 3.3, the wording Code suggests: "A block laid out as its own bands (the course page's free lessons block) keeps its bands' own spacing under the supporting line; recorded exception."

## 3. Four gaps in the standard this page exposed (for Chat; nothing a visitor could see, so not put to Kain)

1. **Line height.** DSRD 7 names a line height per role, but this one page draws 14px Mulish at five line heights (19.6 to 22.4), 16px at three and 12px at five. Wanted: one line height per size for small text.
2. **Text on dark.** White text is drawn at eleven strengths (0.56 to 0.9). Section 1.1 names roles on light grounds; it needs two or three named strengths on the brand dark.
3. **The focus mark.** It is drawn seven ways on this page (2px orange at 2, 3 or 4 off; 3px dark; a white inset ring; 3px peach). Section 5.3 says a ring radius "never had a rule to follow"; the ring itself has no rule either.
4. **Small capital labels** are spaced three ways (0.48, 0.96 and 1.44px) against section 3.1's Overline row (0.08em).

## 4. What became of the four further decisions (updated the same sitting; ship brief for 0.707.932)

The main course page session, running the sessions for Kain, asked that he be brought only what he would clearly notice. Code built each of the first two as a Before and After, looked at them in WebKit, and judged them too fine to see at a glance (Kain's own lesson at pick 288, on a corner change: "I can't see any difference whatsoever"). So they were made and are named here, at theme 0.707.932 (commit f9ce1f80, pick 307):

1. **Card corners, as DSRD 7 5.3 already says:** every small card 12 (outcome cards were 20, question cards 16), every big full-width panel 16 (the curriculum panel was 24). No change to the standard. **A rule 5.3 could carry in plain words:** "A card that sits in a grid with others is a card (12). A box that runs the width of its block is a panel (16)."
2. **One edge for every small white card:** the outcome cards' faint orange line (the brand orange at 18 per cent, 1px) with `--shadow-card`. The question cards already copied it; the review cards now carry it too. The pricing cards keep the Firmer Edge (pick 253). **Not in any standard today:** DSRD 7 5.4 names the card shadow and nothing names the line. Chat to rule whether this is the site's card edge.

Two are left with Chat, because nothing in them would be clearly noticed at a computer and each is a clash inside the standard, not a fault on the page:

3. **Text on a phone.** Section 3.0's phone rule says headings 24 to 21 and reading text 16 to 14 below 768. The course page keeps 24 and 16, and its free lessons title drops 33 to 24. Code's view: 14 is small for a course page's paragraphs on a phone; the rule may want "reading text never under 16".
4. **How wide a supporting line runs.** 616, 720, 800 and, by Kain's own S215 choice, full width on pricing. Section 3.3 names the line's type and space and no width.

## 4a. Two later changes Kain asked for himself in the sitting (ship briefs for 0.707.936 and 0.707.937)

1. **The free lesson pictures are frosted (0.707.936, pick 308).** Kain: "they just need to be frosted maybe by like 10%", then of the first round "a little bit too subtle ... lighter, brighter", then of four strengths "2, Frosted 35". Each of the six pictures sits behind a pane of white at 35 per cent, the picture sharp; the small ones clear when pointed at. A new look he chose: for the course page signed spec, section on the free lessons block.
2. **The review cards are fitted (0.707.937, pick 309). Not Kain's pick.** Kain: "remove a little bit of white space out of this block". Shown four options he said "i dont know"; the master course page session, running the sessions at his request, chose Fitted Cards for him. Each card now holds the room of the longest review showing, not the longest in the pool (cards 366 down to about 341 at computer width); a turn that brings a longer review grows the wall once and it stays. One switch in course-page.js (FITTED) restores the old cards. Kain may overturn.

Still owed to Kain from the same message and not started: a hint that the outcome cards can be clicked.

## 5. Also new in the theme

tools/course_page_measure.py: reads a built course page whole and writes every block's spaces, every text style, every edged box, every control, contrast under AA, motion left under reduced motion, the heading order and each Tab stop's focus mark. It reads; it changes nothing. The site-wide standards session has the same findings.

OWED BACK: Chat's corrections to DSRD 7 3.3a's course page run, and a ruling on each of section 3's four gaps.

*No em or en dashes in this file; checked before writing.*
