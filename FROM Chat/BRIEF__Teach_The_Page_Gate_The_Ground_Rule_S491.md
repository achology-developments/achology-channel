> CODE DISPOSITION, S573: WAITS ON a factory session (gate work); this is a theme session and does not take it. Its S573 Home exceptions (the hairline halves, boundary by boundary) are the lines it will retire, listed in TO Chat/DONE__Home_Gate_Rows_Entered_And_Mended_S573.
For Code, a factory session (gate work): what this needs: teach `page_gate.py` Kain's site-wide ground rule, so a hairline is required only between two blocks of the same ground and a change of ground needs none.

Done when: `hairline-present` and `hairline-edges` in `page_gate.py` (both copies, the theme's and the factory's) pass a boundary where the ground changes with no line, and still fail a boundary between two blocks of one ground that has no line; the hairline halves of Exceptions 23, 27, 29 and 30 are retired from PAGE_EXCEPTIONS and from each page's DSRD6_RECORD.md with their spacing values kept; the list in step 1 is in TO Chat; and a gate run over every built page reads the same count of FAIL rows as before or fewer.

**DOCUMENT TYPE:** brief from Chat, Session 491, 25 November 2026. Answers TO Chat/RULING__A_Change_Of_Ground_Replaces_The_Hairline_Site_Wide_S572. Nothing here goes to Kain.

## The rule (Kain, Code's S572 sitting, 25 November 2026: "Yes, colour is enough")

Written home in DSRD 7 section 4.3, at the head of the section ("The ground rule, site-wide"), with Exception 30 after Exception 29. Read both whole before you start. In short: where two blocks have different grounds (white, Light Sand #FBF9F6 or the brand dark #354149, DSRD 7 section 3.3a), the change of ground marks the boundary and no hairline is drawn. Where two blocks share a ground, the hairline stays. The rule is about presence only. The spacing each page signed does not change.

## Steps, in order

1. **List first, change nothing yet.** Run the gate's boundary reading over every built page and list each page where a hairline is drawn between two blocks whose grounds differ. Kain said "nothing on any page looks different". If a page is on the list, removing its line changes how it looks, so that page is shown to Kain before and after on the rendered page and is not changed silently. Put the list in TO Chat as a DONE file. If the list is empty, go on to step 2 at once.
2. **Teach the rows.** In `page_gate.py` (the theme's and the factory's), make `hairline-present` and `hairline-edges` read the two blocks' grounds at each boundary: different grounds, no line wanted and a line is not a failure either way until step 1's list is settled; same ground, a line wanted as today. How the gate reads a block's ground (computed background of the band, not the class name) is yours to choose; say which in the DONE file.
3. **Retire the hairline halves** of Exceptions 23 (Certification), 27 (school pages), 29 (Policies index) and 30 (Home) from PAGE_EXCEPTIONS and from each page's DSRD6_RECORD.md. Their spacing values (64, 48 and 32, and the banner holding the trail) stay as recorded. Check Exception 25 (the Pricing page's bands): if it says the same thing, retire its hairline half too and say so in the DONE file. Keep Exception 30's statement card boundary, which is the card's own edge, and its two like-ground boundaries that keep a line (DSRD 9 45.31).
4. **Run the gate** over every built page. Report the count of FAIL and EXCEPTION rows before and after.
5. Run your usual gates on the changed files before calling them ready.

## Ask-Code

If a page's ground cannot be read as one of the three grounds (a photograph or pattern behind a block, for example), do not guess a rule: list the page in the DONE file and Chat rules.

*No em or en dashes in this file; checked before writing.*
