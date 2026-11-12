**For Chat. What this answers:** BRIEF__Place_The_Signed_School_Page_Words_S465 (NLP's slots), RULING__School_Page_Students_Films_And_Practise_Words_Signed_S466 and RULING__School_Tree_Words_And_Click_Mark_Written_Home_S468 line 1. Code, school page theme session, S520, 12 November 2026, theme 0.708.067 and 0.708.069, on the build site.

**DONE for the School of NLP.** tools/school_page_data.py now reads these from SCHOOL_WORDS_SIGNED_S465.json alone; no word is typed in it:

1. The banner sentence, What This School Teaches (its line, the four paragraphs, Who This School Is For), the Choose a Course line, the line under the course list, the enrolment promise above the payment options and the Six Free Teachings line.
2. Practise What You Learn: the new supporting line, the three signed headlines, each card's five lines, and the closing line. The heading and the small labels are untouched.
3. What Students Say: the new supporting line and NLP's three films, Jon Frost (929544626, 0:32), Brian Boyle (1033838593, 0:21) and Bea Fernandez Garcia (929543780, 2:00), each with Achology Member and the country, the Testimonials page's own 460 poster, and the course page's film card unchanged. A click opens the right Vimeo number (read at 390 for Brian Boyle).
4. The STAND_INS block is out of the tool (your S468 line 1); it checks the five index words are in the file and stops if one is missing. The retired tree keys were already gone from the file and nothing in the theme reads them.

**Read back.** Every signed slot read from the built page data against the file: 0 fails (all 14 lines, 3 cards by 8 parts, 3 films by name, line and number). On the build site at 1280, 834 and 390: no signed line ends on one, two or three words (20 blocks measured at each width), no sideways overflow, the three films show with their times.

**The last-line rule.** The first build ended 6 lines short at 1280 (the old two-word hold). no-lone-words.js now has an optional `only` list per page, and the school page's entry holds the last four words (then three, then two) of just its signed lines; the story, chooser, tree and reviews lay their own and are not reached. No other page's entry changed.

**Film lengths.** The Testimonials page's data holds none and Vimeo's public lookup withholds them, so each was read from the player (getDuration) embedded in a page on the site's own domain; the 21 lengths for all seven schools are held as a measured table in the tool (FILM_SECONDS), ready for step 2.

**Owed to you, not built.**
1. **The six free teachings' own names.** The signed six for NLP (The NLP Communication Model and so on) are not the lessons the block shows today (Day 1 is Welcome to NLP Practitioner and Course Introductions, with stills, minutes and questions taken from the course data), and I found no lecture in the course data under these titles. Only the supporting line is placed. Which lecture is each of the six, so each can take its still, its minutes and its question?
2. **The footer invite** carries its own sentence ("We will send you six free teachings from this school, one a day for six days, each with its own workbook."), which is site-wide and differs from free_line; left as it is.
3. **The nine questions** have no block on the school page since the S504 ruling, so those signed answers and the questions line are not placed (DSRD 9 section 44 points them to the course pages).
4. **The other six schools** stay as step 2 (built from this data when the NLP page's blocks are settled).

**Not yet done.** Kain has not yet looked at the placed words and films on the page. The page's DSRD 6 gate was not run in this sitting (the school page's close). Poster pictures are 460 wide (the Testimonials page's own); they are soft only on a high-density screen at the widest card.

*No em or en dashes in this file; checked before writing.*
