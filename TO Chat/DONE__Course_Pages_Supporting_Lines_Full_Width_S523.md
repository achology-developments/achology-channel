DONE: the course page family's half of BRIEF__Sweep_The_Supporting_Line_To_Its_Full_Container_S521. Three points for Chat at the foot.

# Course pages: no supporting line carries a width limit of its own (commit 23358db7)

**Kain, 16 November 2026, in the course page sitting:** "Yes, do the sweep." His ruling is the brief's: the line under a heading runs the full width of the container its heading stands in.

## What was found (step 2 and step 4 of the brief, course pages only)

Measured in WebKit on the Diploma and the Mental Health Practitioner Diploma at 1920, 1440, 1280, 1024, 834 and 390, before and after.

| Block | Words | Rows at 1440 | Before | After |
|---|---|---|---|---|
| What You Will Learn | 11 | 1 | runs its 616 column; an 800 limit written, never taking effect | the same, no limit written |
| How the Course Works | 16 | 1 | full width | unchanged |
| The Course Curriculum | 17 | 1 | full width | unchanged |
| What Students Say | 14 | 1 | the heading's own box held at 720, the line with it; an 800 limit written | box and line at the block's full 1,104; still one row |
| Enrol in This Course | 39 | 2 | full width (Kain's own words) | unchanged |
| Try the First Six Lessons | 21 | 2 | its own half of the row beside the two figures (rule 4), a 540 limit written | the same half, no limit written |
| Questions People Ask | 18 | 1 | full width | unchanged |

No line gained or lost a row at any of the six widths on either course. The one change a reader can see is at tablet width (834), where the free lessons line was held to 540 inside a 770 container and now runs the full 770.

## What was built

One rule in the course page stylesheet: on a course page no supporting line, and not the reviews heading's box, carries a maximum width.

## Not yet on the build site

The commit is pushed, but it has no version bump and is not deployed. The school page session held an uncommitted bump in the theme's version file at that moment, and Code does not commit another session's file. That session was asked to carry this commit in its ship in hand; the lines are verified on the build site after that.

## For Chat

1. **What You Will Learn stands over one of two columns** (616 of 1,104). Rule 3 says a heading and its line stand over both. That is a change to the layout of a block Kain signed, so it was NOT made; its line is 11 words on one row. Chat's call whether it is put to him.
2. **The top block's line is 27 or 28 words on three rows** in its 560 column (four on a phone). It is the top block's own line, not a block heading's supporting line, and was not touched. Reported, as rule 5 asks.
3. **At 1024 the free lessons line stands on three rows** in its half of the row (470). At 1280 and up it is two.

*No em or en dashes in this file; checked before writing.*
