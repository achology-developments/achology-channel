# DONE: A7, Kit subscriber pictures moved off achologytest.com (S566, Branch A7)

**Result: line A7 passes.** Every picture address in every Kit subscriber field, and every picture address the theme's field-filling code can write, answers 200 with an image type to both `curl -A "GoogleImageProxy"` and `curl -A "Mozilla/5.0 (Windows NT 10.0) Outlook"`. No address still fails.

## What I found

- The theme code needed no change. Branch G (S559, commit cd3c1624) already made `course-kit.php`, `school-kit.php` and `workbook-kit.php` write the github.io address for any file listed in `data/email-images.json`, and the live build site runs theme 0.708.460, which has it. So no theme commit, no version bump and no deploy were needed from this branch. Version left at 0.708.460.
- What still failed was old stored values: 22 Kit subscribers (all internal test sign-ups, manager+...@achology.com and kain@achology.com) held 129 picture values on achologytest.com, written before S559.

## Theme code proof (run on the build site with wp eval, nothing sent to Kit)

- `achology_free_lessons_kit_fields()` for all 28 courses: 196 picture fields (course_cover plus lesson 1 to 6 stills), 0 not on github.io.
- Manifest coverage: 28 square covers, 28 course quote covers, 168 course lesson stills plus 1 more in free-lessons (169 listed), 42 free-teaching stills (every file in images/free-teachings), 212 workbook covers (equals the 212 files in uploads/workbook-email-covers on the live site, none missing).
- Newest real sign-up (school teachings, subscriber created 2026-11-23) already stored github.io still addresses, which is the test sign-up proof. No new sign-up was made, to keep Kit clean.

## Host check (all pictures in the manifest, excluding fonts)

481 addresses, both user agents: 479 x 200 image/jpeg, 2 x 200 image/png (the logos). 0 failures.

## Kit rewrite

- Read all 1,282 subscribers (all states, 13 pages of 100) with fields. Picture fields are course_cover, lesson_N_still, teaching_N_still, workbook_cover, workbook_course_cover.
- Dry list: 129 values on achologytest.com across 22 subscribers (102 teaching stills, 18 lesson stills, 3 course_cover, 3 workbook_cover, 3 workbook_course_cover). Every one had a same-named file on the host. Two query-string forms (`?v=3`, a .webp cover) for manager@achology.com were mapped to the host's .jpg.
- Run: bulk_update_subscriber_custom_field_values in two batches (100 and 29). 129 updated, 0 failures.
- Read-back: the list endpoint served a stale copy right after the write, so I read back with get_subscriber on 5 subscribers (manager@achology.com, manager+freelessons1, managerschooltest-nlp, manager+schooltest-cbp, manager+wbtest1; kain@achology.com also read directly). All picture fields are github.io addresses. The list read also showed github.io for the 100-row batch subscribers.
- Other non-picture fields (workbook_link, course_link, school_link, teaching_N_film and so on) still point at achologytest.com by design; they are page links, not pictures, and change at launch.

## Curl printout: every distinct picture address now in any Kit field (58), Google | Outlook | file

200 image/jpeg | 200 image/jpeg | course-covers/course-quote-cover-006-300.jpg
200 image/jpeg | 200 image/jpeg | course-email-covers/course-001-square-480.jpg
200 image/jpeg | 200 image/jpeg | course-email-covers/course-007-square-480.jpg
200 image/jpeg | 200 image/jpeg | free-lessons/achology-free-lesson-001-1.jpg
200 image/jpeg | 200 image/jpeg | free-lessons/achology-free-lesson-001-2.jpg
200 image/jpeg | 200 image/jpeg | free-lessons/achology-free-lesson-001-3.jpg
200 image/jpeg | 200 image/jpeg | free-lessons/achology-free-lesson-001-4.jpg
200 image/jpeg | 200 image/jpeg | free-lessons/achology-free-lesson-001-5.jpg
200 image/jpeg | 200 image/jpeg | free-lessons/achology-free-lesson-001-6.jpg
200 image/jpeg | 200 image/jpeg | free-lessons/achology-free-lesson-007-1.jpg
200 image/jpeg | 200 image/jpeg | free-lessons/achology-free-lesson-007-2.jpg
200 image/jpeg | 200 image/jpeg | free-lessons/achology-free-lesson-007-3.jpg
200 image/jpeg | 200 image/jpeg | free-lessons/achology-free-lesson-007-4.jpg
200 image/jpeg | 200 image/jpeg | free-lessons/achology-free-lesson-007-5.jpg
200 image/jpeg | 200 image/jpeg | free-lessons/achology-free-lesson-007-6.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-cbp-1.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-cbp-2.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-cbp-3.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-cbp-4.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-cbp-5.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-cbp-6.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-lc-1.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-lc-2.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-lc-3.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-lc-4.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-lc-5.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-lc-6.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-mh-1.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-mh-2.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-mh-3.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-mh-4.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-mh-5.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-mh-6.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-miw-1.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-miw-2.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-miw-3.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-miw-4.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-miw-5.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-miw-6.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-nlp-1.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-nlp-2.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-nlp-3.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-nlp-4.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-nlp-5.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-nlp-6.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-pc-1.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-pc-2.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-pc-3.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-pc-4.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-pc-5.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-pc-6.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-pgd-1.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-pgd-2.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-pgd-3.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-pgd-4.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-pgd-5.jpg
200 image/jpeg | 200 image/jpeg | free-teachings/achology-free-teaching-pgd-6.jpg
200 image/jpeg | 200 image/jpeg | workbook-covers/managing-expectations-workbook-42728.jpg

Totals: GoogleImageProxy 58 x 200 image/jpeg; Outlook agent 58 x 200 image/jpeg.

Counts: 22 subscribers rewritten, 129 values, 58 distinct addresses live in Kit, 481 on the host, 0 failing.
