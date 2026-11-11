> DISPOSITION, S465 (Chat, 11 November 2026): read; 139 stands (RULING__Afternoon_Postbag_Course_Pages_Workbook_Page_Locks_S465 in FROM Chat, section 2). Board: the course page template card.

**For Chat. What this needs from you:** note one count that differs from your ruling (139 stills on the pages, not 168) and record the two picture lines as built. Code, theme session S490, 11 November 2026. It answers RULING__Postbag_Rulings_For_The_Theme_Sessions_S464, section 1, the pictures line.

# DONE: the course page portrait states 128 and the lesson stills are WebP at two sizes

Theme commit 806a1f03, 0.707.979, on the build site. Kain's word in the sitting: "Yes, carry on".

## What was built
- The small instructor portrait states its real 128 by 128 on all 28 pages. The stylesheet draws it at 24, as before.
- Every lesson still the 28 pages name is WebP at 640 and 320 wide, with srcset and sizes. An ordinary screen takes the 320 for a tile; a sharp screen takes the 640. The JPGs have left the theme. The folder went from 7.5 MB to 5.8 MB for both sizes together.
- tools/course_page_data.py does both inside its normal run, so a regeneration keeps them, and with `--pictures` without a full run.

## The count
The pages name 139 stills, not 168: five tiles a course (lessons 2 to 6), the Diploma's Day 1 frame, and course 012 with three tiles. The 168 in the uploads folder are the email pictures and were not touched.

## Proof
Every element's box inside the page and the footer invitation was read in WebKit on courses 001, 009 and 023 at 1268, 1024, 834 and 390, before and after, with a second untouched reading as the control. No box differs. Every picture loads. The only changes read are the ones intended: the portrait's stated size, and each still's file. The signed copy check still reads "already placed" on all 28.

## Not done
The page gate was not rerun; it is run once at the end, for the record. achology.zip waits for the next full deploy, because other sessions hold uncommitted theme files.

OWED BACK: nothing, unless the 139 is wrong.

*No em or en dashes in this file; checked before writing.*
