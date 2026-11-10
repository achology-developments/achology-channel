> CODE DISPOSITION, S474: WAITS ON the course page theme session (the Certification and Accreditation theme session read its head when it arrived mid-session and acts on none of it).
Needs: Code makes the course page free lessons form send each reader into Kit's six lessons series, and builds the free lesson page each email opens. Theme session. Kit is already built. Opens after BRIEF__Upload_The_168_Free_Lesson_Stills_To_The_Build_Site_S460.

# BRIEF: the course page free six lessons form and the free lesson pages (Chat, S460)

Rulings: DSRD 4 section 6.4b and the form row in section 5.1 (Kain, Session 460 branch, 10 November 2026: "Yes, this shape", the emails approved in his words); DSRD 2 section 2.6 block 2. The signed block design is BRIEF__Course_Page_Block_4_Free_Six_Lessons_S458 in the Course Page folder.

## 1. What already exists in Kit (built by Chat through Kit's connector)
- Sequence "Website Course Free Six Lessons", id 2965491: lessons 1 to 6 (lesson 1 at 0 hours, then daily), day 7, day 14 (live); day 44 to follow. Sender manager@achology.com, Text only template, 11:00 Europe/London, repeat on.
- Tags: `Website Course Free Lessons` (25695128) and one per course, `Website Free Lessons: {ccc} {slug}` (25695129 to 25695156, course 001 to 028).
- Custom fields the emails read: course_name, course_link, course_cover, course_checkout, course_price, free_lessons_link, lesson_1_name to lesson_6_name, lesson_1_still to lesson_6_still. (lesson_n_question and lesson_n_summary exist but are unused; leave them empty.)
- A TEST sequence 2965970 holds a copy for Kain's inbox checks; leave it alone.

## 2. The form (replaces the email-only box in the signed block)
- Fields in order, as the workbook form (DSRD 4 section 5.1): "Your first name", "Your email address", a tick box that must be ticked reading "Send me the six lessons and Achology's emails.", then the signed button "Send Me the First Six Lessons". The rest of the block stays exactly as signed.
- Server side, never a client-side key: create or update the subscriber with first name and the fields below, apply both tags, add to sequence 2965491. Use the same Kit connection the workbook form uses.
- After submit: the signed sent state ("Thank you. The six lessons will come to your inbox, one a day.").

## 3. The values the site sends, per course
- course_name: DSRD 5 name. course_link: the course page address. course_cover: the course's square artwork (`images/courses/course-{nnn}-square-480`, sent as a JPG or PNG copy so Outlook shows it). course_checkout and course_price: DSRD 4 section 1.1.
- free_lessons_link: `https://{site}/academy/{school}/{course}/free-lessons/` (ending in a slash; the emails add `1/` to `6/`).
- lesson_n_name: lessons 1 to 6 of `data/lectures/{slug}.json`, verbatim.
- lesson_n_still: `https://{site}/wp-content/uploads/free-lessons/achology-free-lesson-{ccc}-{n}.jpg` (uploaded by the stills brief).
- Every text value has a non-breaking space between its last two words (Kain's rule: no line of one, two or three words).

## 4. The free lesson page
- Route `/academy/{school}/{course}/free-lessons/{n}/` for n = 1 to 6, noindex, no sitemap entry, never expiring.
- It plays that lesson's Vimeo video (the lesson videos are hidden on Vimeo and embed only on Achology's domain). Map lessons 1 to 6 of each course to their Vimeo ids from the Vimeo library export in the course master folder; titles carry the lesson number in several forms (`001 ...`, `SHP 001`, `2020 FUNCBT 01`, `HYPN0001`, `COU01`).
- Its look waits on a Penpot frame Kain signs (his ruling of 3 November 2026: no signed frame, no build). Build the route, the data and a bare working player now so the emails' links resolve; Chat brings the frame.

## 5. Test
A real address requests the Diploma from the build site: lesson 1 arrives within minutes, greeting by first name, with the still, and the picture opens `/free-lessons/1/` which plays the lesson; Kit shows both tags and all fields; an unticked box stops the form. Name back how you handle a second course requested while the first is still running.

## Done when
Section 5 passes on three courses (one with a different school), and a report with the evidence is in TO Chat.
