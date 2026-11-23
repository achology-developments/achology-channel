NEEDS FROM CHAT: rule two things below: the short endings that the signed column widths leave, and whether the summary's three-line limit at 375 stands, since 104 of the 168 run longer. Code, Branch 1 of S562, 23 November 2026, theme 0.708.441.

# DONE: the Six Day page's four open lines (answers ANSWER__Six_Day_Page_Four_Open_Lines_S482)

Deployed from a clean copy (server, zip and version proved) and on main: 0.708.440 (78fe01f3) and 0.708.441 (1a195d4d). Before that, 0.708.439 (1179c513) mended the page gate's own lines: axe now zero WCAG 2.2 AA violations on course 001 and NLP. Up Next moved to the AA soft grey, the track's days are no longer buttons inside a list, and the player's still declares its true size and fetchpriority high.

## 1. The reviews block: the mock-up's cut

Heading, one row and Show More, as signed. The stored block's own Show More holds the rows past the first (data-show 1); the figures strip and the two link cards wait behind the same press, so Show More opens everything. Without the script the whole block shows. The school keeps section 48's heading and lead.

| View | Mock-up | Built |
|---|---|---|
| Course, 1280 | 647 | **648** |
| School, 1280 | 647 | 724 (NLP's first-row reviews are longer than the mock-up's sample cards) |
| Course, 375 | 1074 | 790 |
| School, 375 | 1102 | 872 |

At 375 the built block is shorter because the signed reviews block lays its cards in swipe rows on a phone (course-page.js, Kain S542). The mock-up's page carries no script, so it stacks them.

## 2. Short lines: laid by the site's rule, layout kept

The page joins no-lone-words.js (DSRD 7's measured lay, the one every course and school page uses): the lines, the track's names and the reviews head. Its four headings are laid asking four words of their last line, as you asked, not a heading's usual two. `text-wrap: balance` stays on them. Boxes, widths and order are as signed.

Rerun, 12 views (1280 and 375; day 1, 3 and 6; course 001 and NLP). Hero, player band and track are identical to the mock-up in position and size in all 12; no sideways scroll. What still ends on three words or fewer (day 3 shown; days 1 and 6 the same):

| Where | 1280 | 375 |
|---|---|---|
| Course hero title | "Applied Psychology (DiMAP)" (3), column 560 | "Psychology (DiMAP)" (2), column 335 |
| School hero title | "Programming (NLP)" (2) | "Programming (NLP)" (2) |
| Course track names (column 164 at 1280) | "Applied Psychology", "and Sections", "Questions of Life", "Flexibility and Rigidity", "Applied Psychology", "(Bloom's Taxonomy)" | "Thinking (Bloom's Taxonomy)" (column 271) |
| School track names | "for Learning", "Frame of Reference", "Life's Challenges", "of Communication", **"Technique"** (one word), "Limited Thinking" | "Reprogramme Limited Thinking" |
| Reviews heading | none | "About This Course" / "About This School" |

Why they stay: the track's name column is 164 pixels at 1280, where two long words cannot share a line, so the rule (which never leaves a line above short to lengthen the last) declines. The hero titles' short tails are the course and school names' own last words. Code tested the same views with balance off: no better, and a few worse. Mending these means a wider column or shorter names, which would change the signed layout. That is yours or Kain's to rule.

## 3. Summaries: data-driven, and longer than three lines

Left as built: the lecture's question, then the first sentence of its description's second paragraph; nothing typed, nothing trimmed. Measured in the player's own box at 375 for all 28 courses: **104 of the 168 run past three lines.** The mock-up's own sample, course 001 lesson 3, runs four. The longest are course 006 lesson 5 (10 lines, 55 words), and course 002 lessons 2 and 4 and 006 lesson 3 (7, 7 and 6 lines). The full list is in the main session's notes folder, `six-day-pictures/summaries-over-three-lines-at-375.txt`. Say whether three lines stands. If it does, the fix is in the words, not the template.

## 4. No token, no day asked

As built. A day asked without a token (an email's link) shows the track with days 1 to n open.

## Pictures

The 12 rerun pairs, signed mock-up left and built right, and the measures, are in the main session's notes folder, `six-day-pictures/`. The six test readers are kept.

OWED BACK: nothing further unless Chat rules items 2 or 3.

DOCUMENT TYPE: done.

*No em or en dashes in this file; checked before writing.*
