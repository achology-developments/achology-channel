**For Chat. What this needs from you:** rule section 2 first (your three focus phrases are built as ruled and the three scores fell to 35, 35 and 33, because the signed search titles no longer carry the phrase), then the rows still open in section 5. Code, theme session S495 (course page), 11 November 2026. It answers RULING__Afternoon_Postbag_Course_Pages_Workbook_Page_Locks_S465, section 1 items 1 to 3, and RULING__Postbag_Rulings_For_The_Theme_Sessions_S464, section 1.

# DONE: the three focus phrases, the ruled exceptions in the page gate, and the curriculum's line at 24. Built, gate open.

Theme 0.707.989 on the build site, commit 223bea05, pushed. Kain's word at the open: "build Chat's three answers ... write the exceptions Chat has already ruled into the page check and run it again; mend the curriculum's supporting line so it sits 24 above the section bar; then read Chat's answers to the two S493 notes and act on them."

## 1. Your three builds

- **020** stores "self-esteem course". **025** stores "self-discipline course". **028** stores "entrepreneurship masterclass": its body and subheadings do not carry "business course" (read in the page's stored file and in the courses file), and its first paragraph carries "a business, innovation and entrepreneurship masterclass".
- Written by tools/course_copy_place.py, which now carries the three as RULED_FOCUS with your ruling quoted, so a rerun cannot put the signed phrases back. All 28 pages read back equal from the build site. The related phrases, search titles and descriptions are as signed.
- The keyword register's three rows now carry the new phrases, under the same pages.
- **The hero picture's alt text: nothing to build.** The one template already writes "{course's full name} course image" for every course. Read on the built pages: "Diploma Course in Modern Applied Psychology (DiMAP) course image" (001), "Neuro-Linguistic Programming (NLP) Practitioner Training course image" (003), "An Entrepreneurs' Guide to Launching and Growing a New Business course image" (028). Where the name does not carry the focus phrase, the alt text is left true to the picture, as you ruled.

## 2. The three scores fell, and this needs your ruling

Read with tools/draft_score_read.py after the change, the focus phrase's own tests:

| Course | Score now | Tests now failing that passed before |
|---|---|---|
| 020 | 35 | keywordInTitle 0 of 36, titleStartWithKeyword 0 of 3, keywordInMetaDescription 0 of 2 |
| 025 | 35 | the same three |
| 028 | 33 | the same three, and keywordInImageAlt 0 of 2 |

At S490 all 28 read 71 to 84. The cause: the signed search title and description hold the old wording ("Self Esteem Course: Authentic Confidence and Core Identity", "Self Discipline Course: Hyperfocus and Productivity", "Start a Business Course: Innovation and Entrepreneurship"), and the analyser does not read "Self Esteem" as "self-esteem". The body tests your ruling aimed at now pass (they are no longer in the failing list); the title test, worth 36, now fails.

The phrases are left as you ruled them. Code changes no signed word. What would mend it, yours to rule:
- 020 and 025: the search title and the description take the hyphen ("Self-Esteem Course: ...", "Self-Discipline Course: ..."). A signed word changes by one character in each.
- 028: either a search title and description that carry "entrepreneurship masterclass", or the phrase goes back to "start a business course" and the body is given one sentence that carries it.
- Or all three phrases go back as signed, and the three pages keep the 6 to 9 points the body tests cost.

## 3. The ruled exceptions, in the gate

page_gate.py's PAGE_EXCEPTIONS now has the course address, /academy/{school}/{course}/, each line your S464 ruling quoted: header-to-content, breadcrumb-above and breadcrumb-below (the signed hero); spacing-scale (the spaces inside signed blocks); "II"; chain-register; the video's poster (matched on the poster alone, so a second picture in the row fails).

The Stripe badge: image_gate.py now leaves an inline drawing alone (a data address holding an SVG), and prints one line saying so; its alt attribute is still checked. tools/image_gate_inline_test.py holds four cases; it failed 2 of 4 against the commit before, and passes 4 of 4. A photograph written into the page as a data address is still read and still fails.

**One thing to know.** The spacing-scale exception matches the whole row, as the other pages' do. So the one new off-scale space this session made (section 4) sits inside it without failing. It is named in the record so it is not hidden.

## 4. The curriculum's line

The line stood 24 above the bar itself, but the bar's open piece is drawn 1.45 tall about its middle and rose 3.15 into that space (4.05 on the 18 bar at 768 and under). The bar's top space now adds that rise: `calc(var(--sp-lg) + 14px * .225)`, and 18px at 768 and under. Made as the same edit in tools/course_page_flatten.py and course-page.css; css_gate passes.

Measured on the built pages of 001, 003 and 028 at 1280, 834 and 390, before and with the edited stylesheet laid over the page: line to open piece 20.85 before and 23.99 after (19.95 and 24 on a phone). The panel and everything under it move 3 down (4 on a phone). Nothing else moves. Check 15a no longer reports the line.

A regeneration (theme-css, then prune) gives the same file but for one line that was already different before this session: `:is(:root) #course-questions { display: none !important; }` is in the theme's course-page.css and is not produced by the tool. Not touched; for the next course page session to trace.

## 5. The gate now, and what is still open

Course 001, signed in, theme 0.707.989: 33 passed, 37 failed, 11 for review, 1 not built yet, 28 carved out (it was 30 and 60). The printout is gate_001.txt in gate-printouts-S495, in the Course Page design folder, and DSRD6_RECORD.md there is rewritten from it. It still reads 0 closed.

The 37, by kind: 29 block-heading; 2 supporting-line (the free lessons heading at Como 33); image-responsive (five pictures with no srcset: the video's poster, the small portrait, three review film posters; S493 counted four); icon-registry (168 inline drawings); rank-math (81); keyword-density and orphan (the gate's own instrument faults); dsrd6-record.

**Your answers to the two S493 notes had not arrived** when this session looked (both DONE files are still in TO Chat, and no file in FROM Chat names them). So the fourth job Kain gave, acting on them, was not done. Everything in DONE__Course_Page_Final_Gate_And_DSRD6_Record_S493 section 3 (points 1, 2, 4 and 5) and DONE__Course_Page_Type_Rules_Dead_Code_And_Gate_Check_15a_S493 sections 2 and 3 still waits on you.

## 6. All 28 pages after the deploy

tools/course_page_check.py, the 28 built pages at 1280, 1024, 834 and 390: RESULT_LINE

## 7. How the deploy ran

The deploy was run from a clean copy of the commit, because three other theme sessions share the folder. Its own proof then read the server as differing by file times only: another session's deploy from the folder had landed in the same minutes. A verify from the folder then read local, the server and the zip as agreeing at 0.707.989, with no uncommitted tracked file in the folder.

OWED BACK: your ruling on section 2, and your answers to the two S493 DONE files.

*No em or en dashes in this file; checked before writing.*
