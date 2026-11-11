> CHAT DISPOSITION, S465 late postbag (11 November 2026): WAITS ON Chat's main session reading lesson 1 in the manager inbox (on Backlog: Chat); this side session is not allowed to open the mail. Section 4 and the rest are answered in RULING__Course_Page_Scores_Free_Lessons_And_Kains_Answers_S465.md in FROM Chat, section 2.

**For Chat. What this needs from you:** read manager+freelessons1@achology.com's lesson 1 in the manager@achology.com inbox and say whether it reads right, and note that its "watch the lesson" link answers 404 until the free lesson pages are released. Code, theme session S502 (course page), 11 November 2026.

DOCUMENT TYPE: report of finished work. Not a page spec.

# DONE: the course page's free six lessons sign-up sends to Kit (point 8)

Authority: Kain's word tonight, RULING__Connect_The_Free_Lessons_Form_The_Emails_May_Still_Change_S498: "by all means, set it up, but the content themselves might change slightly." Built to BRIEF__Course_Page_Free_Six_Lessons_Form_And_Lesson_Pages_Through_Kit_S460, sections 2 and 3, and DSRD 4 sections 5.1 and 5.2. Theme 0.708.015, commit 32916eb5, deployed from a clean copy and proved (local, server and zip agree).

## 1. What was built

- The two boxes on all 28 course pages (the free lessons block and the footer's copy) now send to the site, and the site tells Kit. No Kit script loads on a course page.
- Nothing a reader sees changed. Same fields, same tick box, same button, same thank-you line ("Thank you, {name}. Your first lesson is on its way to your inbox."). The one new line shows only if sending fails: the workbook form's "That didn't go through. Please try again." The form keeps what was typed.
- The site side is course-kit.php, on the workbook form's pattern and Kit connection: a fresh token, a hidden trap field, the tick required, twenty asks an hour per network address. Nothing typed is kept on the site.
- What Kit receives: first name; course_name, course_link, course_cover (the square artwork made into a JPG for Outlook), course_checkout and course_price from DSRD 4, free_lessons_link, lesson 1 to 6 names from the lecture data and lesson 1 to 6 stills; the last two words of each name tied. Tags: Website Course Free Lessons and the course's own tag. Sequence 2965491.
- The emails' words and template live in Kit only. Karen can change any email there with no change in the theme, as Kain's ruling asks.

## 2. The test (11 November 2026, UTC)

One real sign-up, as asked, on course 001's published page in WebKit, signed out.

| Check | Result |
|---|---|
| Address used | manager+freelessons1@achology.com, first name Kain |
| Unticked box, on the page | stopped, "Please tick the box to get your lessons.", nothing sent |
| Unticked box, asked of the server directly | refused, 400, why "tick" |
| Ticked and sent, 22:12:56 | the site answered ok; the thank-you line showed |
| Kit, read back | subscriber 4383883886, every field above filled for course 001; both tags; in sequence 2965491 at 22:12:59 |
| Lesson 1 | Kit records it sent at 22:14:00, about a minute after asking |
| The email's cover picture | answers 200, a JPG |

## 3. Not done, said plainly

- The brief's test on three courses (one in another school) was not run. The main session asked for one real sign-up; more would put more test addresses in Kain's Kit list.
- Whether lesson 1 reads right, greets by name and shows its still: Code cannot see the inbox. Yours to read, as with the workbook test.
- The free lesson pages at /free-lessons/1/ to 6/ are not built (Kain's ruling keeps them waiting on his frame). Every lesson email's link to its lesson answers 404 until they are.

## 4. A second course asked for while the first is running (the brief asks this to be named)

Kit keeps one set of fields per person. A second course's sign-up overwrites them, and Kit does not restart the sequence for someone already in it. So the emails still to come carry the second course, and the first course's lessons stop where they were. Both course tags stay. Nothing was built for it; it is yours to rule if it matters.

OWED BACK: your read of lesson 1 in the inbox.

*No em or en dashes in this file; checked before writing.*
