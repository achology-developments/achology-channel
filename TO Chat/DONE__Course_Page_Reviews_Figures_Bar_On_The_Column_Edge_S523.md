**For Chat. What this needs:** one line written home wherever the course page's reviews block is recorded (DSRD 8 or 9): the figures bar follows DSRD 7 section 4.4 from 1040, by Kain's pick below. Nothing in DSRD 7 changes; this is the rule applied, not an exception. Code, S523, 15 November 2026.

# DONE: the reviews' figures bar stands outside the column, its figures on the column edge, all 28 course pages, theme 0.708.080

Kain, at What Students Say on his walk of the Diploma page: "when there's a bar like that, we typically have it sitting slightly outside of the container." Measured before: the bar's box stood on the column edge and its first figure 45 in. Four ways shown in the Change Viewer (round-8.js, previews/course-outcome-cue-s498/mp: The Figures on the Column Edge, Slightly Outside, Further Outside, No Box); he chose the first: "Yes, build 1". PICKS 323.

Built in course-page.css to DSRD 7 section 4.4, quoted: "a 32px (`--sp-xl`) bleed each side ... with matching 32px inner padding" and "The bleed switches on at min-width 1040px ... Below 1040px the bleed is off and the panel sits flush with the column." From 1040 the bar is 32 outside the column each side with 32 inside, the bar's own 1 edge counted in the 32, and its four figures are set from the left, each 32 clear of its divider. Under 1040 the bar is as it was.

Read on the build site in WebKit at 1440, 1280, 1040, 1024, 834 and 390 on the Diploma and the Mental Health Practitioner Diploma: at 1440, 1280 and 1040 the first figure's mark stands exactly on the heading's left edge (168, 88 and 48) and the bar stands 32 outside each side; at 1024, 834 and 390 the bar is unchanged; no page is wider than its window. The NLP school page carries no such bar and is untouched. Commit dee25e1d; local, server and zip agree at 0.708.080.

Changed, gate open: the course page's DSRD 6 record and Chat's Safari read are not passed, so the course page is not called finished.

OWED BACK: the one line written home.

*No em or en dashes in this file; checked before writing.*
