DISPOSITION (Chat, Session 478, 20 November 2026): for the record; record now CLOSED. Archived.

NEEDS: nothing from Chat to go on. For Chat's record: the pass page's gate result, its new DSRD 6 record, the Kit route as built, the film field choice, and one heading Code matched differently from the addendum's words.

# DONE: the Access All Areas Pass page, its gate and its Kit route

**Answers:** ANSWER__Access_All_Areas_Page_Gate_Rulings_And_Kit_Route and its addendum ANSWER__Access_All_Areas_Page_Three_More_Gate_Rows. Theme 0.708.256 on the build site, 19 November 2026.

## 1. The gate on /access-all-areas/

**42 passed, 1 failed, 14 for review, 51 carved out.** The one fail is rank-math: post 45036 has never been scored, and Kain rescores in one click. Every carve-out names Chat's ANSWER or its addendum after the school ruling's own words. The record line reads "1 closed, 10 not run, 0 fail", the reader lines being Chat's and Kain's.

What was placed in page_gate.py:
- `^/access-all-areas/$` takes the school route's rows: header-to-content, the breadcrumb pair, content-width 1104, icon-registry, chain-register and keyword-density. The pass's own rows are the film picture's lazy rows (film-pass.webp), the six long lines matched on heading and count, the capitals, the tree line's 32 at three widths, and the three stills.
- From the addendum: Master, the price card promise's three sentences, and the tutorials row's negative gap at desktop only.
- In COMPONENT_SPACING_EXCEPTIONS, the tick panel's auto margin. Checked first: the later `.pn-bx .pn-f2__ticks` rule (course-page.css line 1304) sits on another card, not the pass's.

**One call Chat may overturn: the school route's tutorials row.** The addendum named the school heading as "Sample Six Instructional Tutorials From This School". The school pages now print "Explore Six Sample Tutorials from This School", so Code matched the heading the pages carry. The row is otherwise as ruled: desktop only, negative gap only.

**The school row, proved:** a rerun on /academy/neuro-linguistic-programming/ printed the tutorials row as a CARVE-OUT at desktop. That run caught the page with its stylesheet unloaded, while another session was deploying, so its other counts are not a reading of the page and are not reported.

**Seen on the school pages, not this session's work:** the schools now carry reworded headings and new film picture names, so their older SCHOOL_HEADING_ROWS no longer match. The gate shows about 15 fails a school, among them the Who line, history line, tree line and practise line rows, the capitals rows, the 32 under the tree, and film-{school}.webp lazy. Those rows belong to the school page session, which owns the rewording. Code has not touched them.

**A note on git:** a commit of Code's, a7a32083, carried two of the school page session's working files with it (school-page.css and previews/school-page-s482/proxy.py). That session's next commit, 3f455d2d, builds on it, so nothing is lost. Only the commit's label is wrong.

**After Kain's rescore (19 November 2026, theme 0.708.258): 43 passed, 0 failed, 14 for review, 51 carved out.** Rank Math 94 on post 45036, focus keyword "access all areas pass", read from the install and written to Code's score table. The robot check refused the score reader's browser, so the number is the stored rank_math_seo_score, read over SSH after Kain's recalculate, as at S530. The keyword-density proof owed after the rescore is still owed: Rank Math's own density test was not read, for the same reason.

## 2. The record

DSRD6_RECORD.md, in the Access All Areas Page folder. Every machine line is filled. Every reader line reads not run, and Code has marked none of them.

## 3. The Kit route (school-kit.php and course-kit.php, 0.708.256)

- The form accepts `school=pass`. The pass takes the shared tag 25962820, its own tag 26174497 and sequence 2978957. The seven schools keep 2974053.
- The six come from schools.json in the signed day order, named by school and day (pgd 6, lc 5, cbp 1, nlp 1, pc 6, miw 1), so no lesson is retyped. A missing lesson or workbook stops the send and names what is missing.
- Fields: school_name "Academy of Modern Applied Psychology"; school_link and free_teachings_link both /access-all-areas/.
- **The film field, on both routes:** teaching_N_film is now written as Chat preferred, each lesson's own teaching page on its school's route, /academy/{school}/free-teachings/{n}/. For a school, that is its own six.
- Every PHP file parses on the server's own PHP.

**The test sign-up, made on Kain's "Yes, make it", 19 November 2026, 22:36 UTC,** through the page's own form in a real browser, as manager+schooltest-pass@achology.com (first name "Pass Test"). The read-back:
- the form shows its thank you line, "Thank you, Pass Test. Your first lesson is on its way to your inbox.";
- the subscriber (Kit id 4397465433) carries tags 25962820 and 26174497 and no school tag;
- the subscriber is in sequence 2978957, added 22:36:15;
- all 27 fields are filled: the three page fields, then the six names, stills, workbooks and films in the day order above, from Humanistic (pgd 6) to Mindfulness (miw 1).

The subscriber is left in place. Email 1 waits on Chat's publishing of the sequence.

*No em or en dashes in this file; checked before writing.*
