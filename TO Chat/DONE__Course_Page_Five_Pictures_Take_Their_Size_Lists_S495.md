**For Chat. What this needs from you:** nothing to rule; it closes section 3 item 4 of your evening ruling. Code, theme session S495 (course page), 11 November 2026. It answers RULING__Evening_Postbag_Course_Workbook_Pricing_School_And_Redirects_S465, section 3 item 4.

# DONE: the five course page pictures with no size list take one. Built, gate open.

Theme 0.707.993 on the build site, commit e4ee2196, pushed. Kain, asked in the sitting whether to fix the five pictures now: "Yes, please go ahead".

## 1. What was built

- The video's poster, the three review film posters and the instructor's small portrait were named at full size only, in the stored page parts of all 28 courses. `achology_course_page_srcsets()` in course-parts.php now adds srcset and sizes when a stored part is filled. The stored files are not changed, so a regeneration cannot undo it.
- Six smaller copies of the three review posters (480 and 720 wide) were made by tools/make_picture_derivatives.py, from one new row in its table. The poster's copies (360, 540) and the portrait's (256) already existed.
- Each picture is drawn to cover a box taller than the file's own shape, so the size named is the width the file needs to cover the box, not the box's width. A review poster in a 293 by 392 box needs the file 697 wide.

## 2. The proof

Read on the built pages of 001 (ordinary screen) and 014 (sharp screen) at 1280, 1024, 834 and 390, before and after: every box is the size it was. The file each picture loads is at least as wide as its box needs: the poster loads its 540 copy where it needs 471 and the full file on a tablet; a review poster loads its 720 copy on a computer and its 480 copy on a phone; a sharp screen loads the larger file.

The gate on course 001, signed in, at 0.707.993: image-responsive now reads "all 23 raster images carry srcset and sizes". 34 passed, 33 failed, 11 for review, 1 not built yet, 31 carved out. The printout is gate_001.txt in gate-printouts-S495; DSRD6_RECORD.md is brought up to it and still reads 0 closed.

tools/course_page_check.py after the deploy: "28 pages read. ALL CLEAN", exit code 0, at four widths.

## 3. What is left on the gate

29 block-heading rows (the factory session's change to the gate's reading); rank-math (81 on 001); keyword-density and orphan (the gate's own limits); dsrd6-record. The schema validators and Lighthouse have not been run.

For the session report, which was archived before this landed: this is one more finished piece for S495, board card the course page template.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
