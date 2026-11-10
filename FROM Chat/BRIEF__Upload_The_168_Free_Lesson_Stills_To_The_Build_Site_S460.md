Needs: Code uploads 168 ready-made pictures to the build site at one fixed address pattern, then tells Chat they load. Kain's yes, 10 November 2026, evening. Small job, open next in either session.

# BRIEF: upload the 168 free lesson stills to the build site (Chat, S460)

## Why
The six free lessons emails in Kit (sequence "Website Course Free Six Lessons", built and approved by Kain) show each lesson as a still with an orange play button. Kit can only show a picture that has a web address. The stills exist only on Chat's computer, so Kain's test emails show blank boxes. Chat has no upload key on this computer; you do.

## The files
In the project folder: Course Page design folder, then "Six Lessons Emails S460", then "Upload These 168". 168 JPGs, 640 x 360, about 40 KB each, named `achology-free-lesson-{course number, three digits}-{lesson 1 to 6}.jpg` (for example `achology-free-lesson-001-1.jpg`). Each is the course page's own teaching still from previews/course-page-s208/img/lessons/640 (lesson 1 of course 001 uses the alt2 frame Kain picked) with the play disc and the lesson's real running time laid on by `tools/still.py` beside them. Course 012 lessons 5 and 6 had no still in that folder, so those two use the video's own Vimeo frame. Do not remake or recompress them.

## What to do
1. Copy all 168, unchanged, to `wp-content/uploads/free-lessons/` on the build site (a plain folder, not the media library, so no WordPress page or attachment is made).
2. Check every one answers 200 with `image/jpeg` at `https://achologytest.com/wp-content/uploads/free-lessons/achology-free-lesson-{ccc}-{n}.jpg`.
3. Report to TO Chat: the count that answer 200, and any that do not.

## Not in this job
The course page form, the free lesson page the play button opens, and filling Kit's fields per course come in the main six lessons brief that follows. At launch the address moves with the site; note it then.

## Done when
168 of 168 answer 200 at the pattern above, and your report is in TO Chat. Chat then fills the Diploma's six `lesson_n_still` fields on the test address and resends Kain's test.
