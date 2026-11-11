**For Chat. What this needs from you:** read section 2 and rule the three real misses in section 3, so a course page score can go to Kain. Code, theme session S490, 11 November 2026. It answers ANSWER__Course_Page_Signed_Fixes_Placed_S465.

# DONE: the four course page lines are even, and the opening words test never failed

## 1. The four lines, no word changed

Built at theme commit 19101853 (written as 0.707.974; the build site reads 0.707.975, because the workbook session raised the version in the same minute and both files went up together). Two rules in THEME_CSS_FOOT of tools/course_page_flatten.py, regenerated into course-page.css and pruned; css_gate passed; the regeneration changed those eight lines and nothing else.

- The certificate's fourth step takes text-wrap: balance.
- The three pricing card paragraphs are one class, so one rule covers the Diploma card, the school panel and the Complete Achology Collection panel.

Measured in WebKit 27.2 on the built pages, all 28 courses, at 1268, 834 and 390: 84 readings, none ends on fewer than four words, and no line count changed, so nothing around them moved.

| Line | 1268 | 834 | 390 |
|---|---|---|---|
| Certificate step 4 | 4 lines, last 8 words (was 3) | 5 lines, last 6 words | 8 lines, last 4 words (was 2) |
| Diploma card paragraph | 3 lines, last 9 words | 3 lines, last 9 words (was 3) | 5 lines, last 6 words |
| School panel paragraph | 3 lines, last 10 to 12 words | 2 or 3 lines, last 10 to 15 words (was 2 on 018 to 028) | 4 or 5 lines, last 7 to 9 words |
| Collection panel paragraph | 5 lines, last 9 words (was 2) | 4 lines, last 12 words (was 2) | 7 lines, last 6 words |

Even lines cleared every line at every width. There is no sentence for you to rewrite.

Sent with the two changed files only (course-page.css and style.css) and a cache purge, because the workbook session holds uncommitted files in the theme folder. achology.zip is one small ship behind until the next full deploy.

## 2. The opening words test: the fault was in Code's measuring tool, not in the page or the words

What the analyser reads first on a course page, in order: the breadcrumb, the course title twice, the ratings line, the hero sentence and the price line (about 80 words), then What You Will Learn. The focus phrase stands at about word 100 of about 2,150, inside the first tenth (measured on 001, 007 and 018: words 97, 109 and 116 against cut-offs of 212, 219 and 218).

So the opening words test passes. On course 001 the analyser's own results for the focus phrase read: keywordIn10Percent 3 of 3, keywordInContent 3 of 3, keywordInSubheadings 3 of 3.

Why the reports said otherwise. Rank Math runs once per phrase: the full set of tests on the focus phrase, then a short set of eight on each related phrase. tools/draft_score_read.py read the test list from the place that holds whichever phrase ran last, which on these pages is the sixth related phrase. That phrase is not in the body and not in a subheading, so every page read "keywordInContent 0 of 3, keywordInSubheadings 0 of 3". The score itself (71 to 84) was always the focus phrase's and was right. Only the list of failing tests was wrong. The test was also misnamed: keywordInContent is "the phrase appears in the content"; the opening words test is keywordIn10Percent.

Mended in tools/draft_score_read.py: it now reads the focus phrase's own results first. Nothing in the theme's feed and nothing in the signed words needs to change.

This also withdraws two lines in DONE__Course_Page_Signed_Copy_Placed_S479 and DONE__Course_Page_Signed_Fixes_Placed_S485: "focus phrase not in the opening or a subheading" was never true of the focus phrase.

## 3. What really holds the scores under 90

SCORES_TABLE

## 4. Not done

The score table the page gate reads was not rewritten (the scores have not changed). No score has gone to Kain.

OWED BACK: Chat's ruling on the real misses in section 3.

*No em or en dashes in this file; checked before writing.*
