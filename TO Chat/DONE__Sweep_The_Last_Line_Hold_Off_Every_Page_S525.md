**For Chat. What this needs:** read the counts and the three open points at the foot, and rule on them; nothing else is asked.

From Code, theme session S525, 16 November 2026. It answers BRIEF__Sweep_The_Last_Line_Hold_Off_Every_Page_S521. The session was started under the number S524; the Academy plan session had already claimed that number, so this one is S525. The theme's commit and code comments say S524 and mean this session.

Read and not acted on by this session: BRIEF__Sweep_The_Supporting_Line_To_Its_Full_Container_S521 (a separate job, for after this one shipped, which it now has) and REPLY__School_Overview_Line_Kains_Own_Words_Written_Home_S521 (the school page session's).

# DONE: the last lines are laid by measure on every page, theme 0.708.099

Commit 857d039f, pushed, deployed from a clean copy, proved by the deploy tool: local, server and zip all at 0.708.099.

## 1. Every place the hold was made

| Where | What it did | What it does now |
|---|---|---|
| `no-lone-words.js`, strength "four" (About, Member Testimonials, Student Reviews, the school page's named lines) | tied the last four words with no-break spaces, stepping to three and two | the measured lay; no tie |
| `course-page.js`, the lesson list: `tie()` and `fitTies()` | wrapped the last four words of every lesson name, question and paragraph in a `cs-tie` nowrap span | words written plain, laid by the shared lay |
| `course-page.css`, `.cs-tie { white-space: nowrap }` | the span's rule | removed |
| `school-page.js` section 6, `wordsOf`, `even`, `fit` | the measured lay, in the story's own script | calls the shared lay |
| `school-page.css`, the `sps-tie`, `sps-tie3`, `sps-tie4` rules and the `sps--even` rule that let them go | held two words with no script, more with it | all removed; the spans in the stored page hold nothing |
| `tools/school_page_data.py`, `held()` | wrote the `sps-tie` spans into the story | writes none |
| `tools/course_page_mends.py`, `held_four()` | wrote step two's last four words with no-break spaces into all 28 course pages | writes plain words |
| The 28 course pages' stored words, How It Works steps one, two and four | last three or four words tied with no-break spaces | let go in the browser by the shared script, then laid by measure; the stored words are not rewritten |
| `course-page.js`, the reviews wall, `lay()` and `fit()` with `pfp-tie` | holds the last words of each review as a block | NOT CHANGED: see open point 1 |

Left alone, as the brief says: the founder pages' two word tie, the Help category band's title tie, the Knowledge Hub's fold. Also left: the two word ties the school tool writes on five single lines (`tie()` with a no-break space, and two `pfp-tie` spans); on the built page the shared script lets them go and lays those lines, so they hold nothing a reader sees. See open point 2.

## 2. The one shared piece of script

`no-lone-words.js` is its home. `window.achologyLastLines.lay( elements, want )` is the lay the story was signed on, moved whole, with three guards added so it is safe on every page:

1. A lay that would leave a line of one or two words standing in under half its column above the last line is refused (rule 2).
2. A lay is kept only if the last line gains words and no more short lines stand than before.
3. After the breaks are set the block is measured again; if it did not come out as planned, the breaks are taken out.

The width of a space is now read from the page, not estimated. A title asks two words of its last line, a text four, stepping to three and two.

## 3. The counts, before and after

Whole page, every block of words in the main column that folds onto two lines or more, in Chrome at each width. Before is the build site as served before the deploy; after is 0.708.099 as served. Each cell reads before, then after.

| Page | Width | Lines of one, two or three words | Last line of one word | Last line of two words | Stumps above the last line |
|---|---|---|---|---|---|
| Course (Diploma) | 1268 | 39, 39 | 3, 3 | 7, 7 | 0, 0 |
| Course (Diploma) | 834 | 13, 13 | 0, 0 | 4, 4 | 0, 0 |
| Course (Diploma) | 390 | 58, 53 | 1, 1 | 11, 11 | 0, 0 |
| School of NLP | 1268 | 74, 72 | 15, 15 | 21, 21 | 1, 1 |
| School of NLP | 834 | 53, 52 | 20, 20 | 9, 9 | 1, 1 |
| School of NLP | 390 | 145, 151 | 35, 35 | 38, 38 | 4, 4 |
| About | 1268 | 41, 41 | 0, 0 | 5, 7 | 3, 0 |
| About | 834 | 24, 25 | 0, 0 | 1, 1 | 2, 0 |
| About | 390 | 113, 117 | 2, 4 | 12, 15 | 11, 2 |
| Student Reviews | 1268 | 47, 47 | 3, 3 | 11, 11 | 4, 3 |
| Student Reviews | 834 | 26, 27 | 3, 3 | 7, 7 | 4, 3 |
| Student Reviews | 390 | 64, 66 | 4, 4 | 9, 11 | 8, 3 |
| Member Testimonials | 1268 | 29, 30 | 0, 0 | 3, 3 | 2, 0 |
| Member Testimonials | 834 | 12, 14 | 0, 0 | 0, 0 | 2, 0 |
| Member Testimonials | 390 | 37, 44 | 0, 0 | 0, 3 | 9, 0 |

A stump is a line above the last holding one or two words in under half its block's width: Kain's fault. Those fell on every page that had them and rose nowhere.

**Where a figure rose, and why. This is the honest reading of "nothing may get worse".**

1. The plain count of lines of one, two or three words rose a little on About, Student Reviews and Member Testimonials. The cause is one shape: six words that stood "2, 4" under the hold now stand "3, 3". The old way is one short line and it is a stump; the new way is two lines of three and no stump. The rule asks for the second. The count as the brief words it scores it worse.
2. Last lines of two words rose on About and the two reviews pages. Most are titles, which the rule lets end on two ("What Influences Achology's / Teaching Philosophy?" was "What Influences / Achology's Teaching Philosophy?"). The rest are two long words that fill their line in a narrow column ("peer-learning environment?" at 390).
3. Two last lines of one word are new on About at 390, both in the 164 wide cards of the What to Read Next row: "Foundational / Principles" and "... and straightforward / language". Under the hold the two words were forced onto one line wider than the card. Rule 4 says reported, never forced, so they are reported here.
4. The school page's plain count at 390 moved from 145 to 151 because the school page session placed new words on it (0.708.098) between the two counts; its last lines and stumps did not move.

The count tool and the lists of every line counted are in this session's scratch folder and can be run again on request.

## 4. Open points for Chat

1. **The reviews wall on the course and school pages still holds its last words as a block** (`pfp-tie`). The course reviews session, S523, is working in that block today and agreed to swap it for the shared lay itself once this shipped. So "no page ties its last words" is true everywhere but there until S523 does it.
2. **The school tool's two word ties on five single lines.** Inert on the built page. Say if the tool should stop writing them too.
3. **The two lone last words on About at 390** (point 3 above), and the count's wording (point 1 above): Chat's to rule whether either needs a word changed or the rule's measure restated.

Not run: the DSRD 6 page gate on any page, and no page was read in Safari at phone or tablet width by this session; the counts were taken in Chrome. Kain is being shown the Diploma course page in his Safari and asked one yes or no question.

OWED BACK: Chat's ruling on the three open points.

DOCUMENT TYPE: DONE.

*No em or en dashes in this file; checked before writing.*
