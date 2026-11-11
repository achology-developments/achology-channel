> CHAT DISPOSITION, S465 late postbag (11 November 2026): DONE. Written into DSRD 8, the Browse More decisions, row 9, and DSRD 9 section 37; noted in RULING__Course_Page_Scores_Free_Lessons_And_Kains_Answers_S465.md in FROM Chat, section 5.

**For Chat. What this needs from you:** write Kain's ruling home (the Browse More block's family standard and the Component Registry row, where the S130 size is written), since it replaces his S130 pick on four page kinds. Code, theme session S500, 11 November 2026.

**DOCUMENT TYPE:** ruling. Not a page spec.

# RULING: Browse More's titles are one size up, 18

## 1. Kain's words

On the built workbook page, with a picture of the block: "on this second block, which is down at the bottom, the browse more ecology workbooks block, I'm just wondering if you're happy with the text size. Of the workbooks that gets, you know, pointed through to". Told the titles measure 16 and that Code would lift them: "Yes, show me". Shown four settings in the Change Viewer on a workbook, an article and a quote page, and told that 16 was his own S130 pick and why he made it: "Yes, build 1".

## 2. What it replaces

The heading face at 16, weight 500, his ruling at S130 ("Type 1: the heading typeface, one size smaller"), made against an article's last lines because at 18 the heading face read larger than the writing's 18. The stylesheet's note keeps that history and adds this ruling under it.

## 3. The round

previews/browse-more-s500 in the theme, mp/round-1.js: 1 One Size Up (Code's recommendation), 2 Same Size Bolder, 3 The Writing's Lettering, 4 Two Sizes Up. Proved by tools/viewer_proof.py before it opened (11 measured, 0 failed). He chose 1.

## 4. Built (theme 0.708.013, commit 1d990871, deployed)

- The shared list's titles (`.qp-more .qp-more__link` in knowledge-hub.css) are the heading face at 18, weight 500. One rule, so it holds on workbook, article, book note and quote pages.
- On the workbook page the list is 600 wide where it was 528, so the longest title still sits on one line beside the covers.
- No word changes. Nothing else moved.
- Read back on the build site in WebKit: the workbook page at 1440 (six titles, each on one line) and at 390 (each on two lines, no sideways scroll); an article and a book note at 1440 and a quote page at 834 (six titles, each on one line). css_gate passes both stylesheets.

## 5. One thing for you

The list's lead line and heading did not change. If a family document states the title size as 16, it now disagrees with the build until this is written home.

OWED BACK: the ruling written home.

*No em or en dashes in this file; checked before writing.*
