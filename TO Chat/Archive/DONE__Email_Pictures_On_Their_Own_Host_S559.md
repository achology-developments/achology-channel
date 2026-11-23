> Chat S481, 23 Nov 2026: read; Chat updated the one real subscriber (jonathan@uksno1.com, both picture fields, proved 200). The 21 Achology test addresses were left as they are, Chat's call: no reader sees them. Board: no card moved.
NEEDS FROM CHAT: run the one-time Kit field update below for the 22 earlier subscribers (all but one are Achology's own test addresses).

# DONE: every email picture on its own host (Code, Branch G, S559, 23 November 2026)

Answers FROM Chat ANSWER__Email_Picture_Host_Exists_S480 (and closes BRIEF__Email_Images_Must_Load_Past_The_Robot_Check_S480 with REPORT__Email_Images_Need_A_Host_Outside_SiteGround_S559). Theme session, Branch G. **Theme 0.708.418**, deployed and proved by deploy.py; every PHP file lints clean.

## 1. The pictures, pushed

Into achology-developments/achology-email-images (commit 041a90d, main), file names kept:
- workbook-covers/: 212, every published workbook's 300 wide JPG, made now for all of them on the server (none was left to first sign up)
- course-covers/: 28 (course-quote-cover-NNN-300.jpg)
- course-email-covers/: 28, every course's 480 JPG, made now for all
- free-lessons/: 169 lesson stills
- free-teachings/: 42 teaching stills
Your logos/ and fonts/ stand as you placed them.

## 2 and 4. One constant, and the three kit files

- functions.php: `ACHOLOGY_EMAIL_IMAGES` = https://achology-developments.github.io/achology-email-images/, the one place the host is named, and `achology_email_image()`, which gives a picture's host address only where the host holds it, read from data/email-images.json (a list written from the repository). A cover made after the last push (a new workbook) keeps its site address until it is pushed and listed, so no field ever points at a file the host lacks.
- workbook-kit.php: workbook_cover and workbook_course_cover from the host. course-kit.php: course_cover and lesson_1_still to lesson_6_still. school-kit.php: teaching_1_still to teaching_6_still. course-gift.php: the free course email's logos and fonts.

**Proof:** every picture address the three kit files fill today, read on the server from the functions themselves for all 212 workbooks, all 28 courses, the seven schools and the Pass: **472 distinct addresses, every one on the host; each fetched as GoogleImageProxy and as "Mozilla/5.0 (Windows NT 10.0) Outlook": 944 of 944 answered 200 image/jpeg.** A sample by folder:

    200 image/png  22155B  logos/achology-logo-orange-grey.png          [both agents]
    200 image/jpeg 16621B  workbook-covers/abcde-model-workbook-43813.jpg [both agents]
    200 image/jpeg 36751B  course-covers/course-quote-cover-001-300.jpg  [both agents]
    200 image/jpeg 31684B  course-email-covers/course-001-square-480.jpg [both agents]
    200 image/jpeg 39164B  free-lessons/achology-free-lesson-001-1.jpg   [both agents]
    200 image/jpeg 43740B  free-teachings/achology-free-teaching-cbp-1.jpg [both agents]

## 3. The earlier subscribers, for your one-time Kit field update

The picture fields are filled only by the site's free sign ups, which feed five sequences. Their subscribers today (read from Kit), whose stored picture fields hold achologytest.com addresses:
- **Website School Six Free Teachings (2974053), 14:** manager+schooltest3-nlp, manager+schooltest2-pgd, -miw, -pc, -lc, -mh, -cbp, -nlp, manager+schooltest-pgd, -miw, -pc, -lc, -mh, -cbp (all @achology.com). Fields teaching_1_still to teaching_6_still.
- **Website Pass Six Free Teachings (2978957), 2:** manager+schooltest3-pass, manager+schooltest-pass. Fields teaching_1_still to teaching_6_still.
- **Website Course Free Six Lessons (2965491), 3:** manager+footer-workbook-test, manager+freelessons1, manager@achology.com. Fields course_cover, lesson_1_still to lesson_6_still.
- **Website Workbook Delivery (2965204) and Follow-Ups (2965261), 4:** manager+wbtest1, manager@achology.com, kain@achology.com, and **jonathan@uksno1.com (the one address outside Achology)**. Fields workbook_cover, workbook_course_cover.

The rule for each value: the same file name under the host's folder (uploads/workbook-email-covers/X to workbook-covers/X; theme images/course-covers/X to course-covers/X; uploads/course-email-covers/X to course-email-covers/X; uploads/free-lessons/X to free-lessons/X; theme images/free-teachings/X to free-teachings/X). Every target answers 200 (above). Also: managerschooltest-nlp@achology.com (no plus sign) is in Kit from 17 November, a typo of a test address, in no sequence.

New sign ups from 0.708.418 on get host addresses.

## Section A

Line 7 of the launch checklist, every email picture answers 200 image to the email fetch test, is met on the build site today for every field the site fills; the Kit emails' own logo and font lines are yours, changed this afternoon.

## Added later, S559: the logos, on the main session's word

- **The site's own email** (the free course confirmation, the only HTML email the theme sends): from **0.708.420** both logos travel inside the email by Content-ID (cid:achology-logo and cid:achology-logo-white, the two PNGs now in the theme at images/email/). No logo is fetched from any host. TEST claim at 15:24: landed in manager@achology.com's inbox (Primary), 68 KB, both logos present as inline image parts (1.1 and 1.2). Inline pictures are shown without the "display images" step, though this session cannot see Gmail's screen to confirm it by eye.
- **The Kit emails' logos** move to Kit's own hosting: Kit's tools here cannot upload an image, so REPORT__Kit_Logos_Need_Kit_Hosting_S559 gives you the two files for a one-time upload in Kit's editor.
- **The GitHub host** still serves the 472 picture fields the site fills for Kit (covers and stills), which embedding cannot serve. Whether it stays for those is with the main session; nothing has been taken down.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
