**DISPOSITION (Chat, Session 467, 12 November 2026): ACTED ON.** Section 3 ruled in line 9 of FROM Chat/RULING__Postbag_Answers_S497_To_S513_S467. Board: course page card read at close. Archived.

**For Chat: read this against the 28 built course pages. What this needs:** one ruling on six lesson questions that now run past their row on a phone (section 3), and nothing else. Code, theme session S509, 12 November 2026, a side run started from the course page session S498 on Kain's "yes" to it.

DOCUMENT TYPE: done. Answers BRIEF__Place_The_354_Signed_Lesson_Questions_On_The_Course_Pages_S465.

This file asks Kain nothing.

# DONE: the 354 signed lesson questions are on the course pages

## 1. Built

- Theme 0.708.043, commit db5f3698, deployed (local, server and zip agree).
- tools/course_copy_place.py gains one step, place_questions. It reads `questions` from COPY__Course_Lesson_Questions_Final_S465.json in FROM Chat (or its Archive) and nothing else from it. It runs on its own with `--questions`, and after the signed copy on a plain run, so a regeneration followed by the one command brings every signed word back.
- Each question goes into its own lesson's row of the curriculum data on its page (data/course-page/NNN.json), keyed by lesson number. Every page row is paired with data/lectures name for name before anything is placed; one mismatch stops the whole run.
- Where the lesson is the one the free lessons strip shows (Day 1), the strip's question changes too. That is one line: 002 lesson 1.
- Karen's course master and data/lectures are untouched.
- Apostrophes: every lesson question on the pages already writes them straight (175 straight, none curly), so the file's straight ones went in as signed.

## 2. Your three checks, and the read-back

- Check 1: 354 questions, 354 names, the same keys; every name equals the page's lesson name for that number. 0 differ.
- Check 2: none of the 354 equals the question on the page before. 0 equal.
- Check 3: longest 97 characters, shortest 18.
- Read back from all 28 built pages, signed out, one page a second, twice: **354 signed questions equal to the file under their own lesson names; 1,792 other lessons show exactly the question they showed before; 0 changed; 0 faults.** No old question of the 354 is printed anywhere else on any page.

## 3. How they set (WebKit, at 1268, 834 and 390)

Each question was set in a copy of a real question line on its built page, written as the page script writes it (it holds the last four words together), old words and new.

- At 1268 and 834: none runs past its row. 16 take two lines at 1268 where the old took one, and 12 at 834; all sit as the other two-line questions do.
- At 390: 19 take three lines where the old took two (002-006, 002-016, 002-028, 002-034, 004-055, 004-072, 004-095, 004-108, 004-136, 004-152, 006-034, 006-045, 008-012, 012-029, 013-103, 015-057, 019-012, 019-036, 026-018).
- **At 390, 18 run past the right edge of their row, because their last four words held together are wider than the 228 line.** 12 of them did so with the old words too (001-024, 001-091, 001-131, 001-150, 003-123, 003-132, 003-144, 007-096, 007-115, 009-061, 009-087, 013-048), and five other lessons' old words did (003-011, 004-046, 004-143, 014-038, 021-009). **Six are new: 001-034, 002-012, 003-106, 004-136, 004-152, 007-036.** It is the page script's holding rule more than the words: before the placing, 17 lessons did it. Two ways out, neither built: you mend the six words, or the theme holds two words on a phone instead of four (a visible change, so it goes to Kain through the main session as a yes or no).

OWED BACK: your read of the 28 pages, and a word on section 3.

*No em or en dashes in this file; checked before writing.*
