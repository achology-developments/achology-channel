> Chat S494, 26 Nov 2026: read. Chapters 2 to 5, 10 and 11 pass; search words now in effect on / (Chat read the live title and description). Chat's reader chapters 1, 6, 7 (human half) and 8 written as one line on Backlog: Chat. Archived.
# DSRD 6 RECORD: Home

**Page:** home
**Template:** front-page.php
**Theme version at last update:** 0.708.490

Copy this file into that page's own design folder as `DSRD6_RECORD.md` and fill it in. One record per page, per DSRD 6 §0: "Every page has one record file, named `DSRD6_RECORD.md`, living in that page's own design folder."

**The `Page:` line above is load bearing.** The completion gate finds a page's record by reading that line, not by guessing from folder names. A record without it cannot be found, and the gate reports the page as having no record at all. (Home is the front page, address `/`; the gate keys it as `home`, which is what the line above names.)

## How to fill a line

Every line reads exactly one of four states, and carries the date it was written:

| State | Write | Means |
|---|---|---|
| Pass | `pass, YYYY-MM-DD` | Met |
| Fail | `fail, YYYY-MM-DD, {what failed}` | Not met. The page is not ready |
| Recorded exception | `exception, YYYY-MM-DD, {reason}, approved by Kain` | Genuinely does not apply. Never skipped silently |
| Not run | `not run` | Nobody has checked yet. The page is not ready |

**A page is ready only when no line reads fail or not run** (DSRD 6 §0).

## Separation of duties, and it is not optional

DSRD 6 §0: Code writes the machine lines, Chat writes the human-reading lines, and whoever presents the page to Kain writes his lines after his sitting. The builder of a page never writes the judgement lines for his own build. So **Code fills only the rows marked machine.** The others read `not run`.

## The chapters

| # | Chapter | Runner | State |
|---|---|---|---|
| 1 | Copy standards | machine + human reader | not run |
| 2 | Page structure and headings | machine | pass, 2026-11-25, [machine, theme 0.708.490] page_gate v9 on the build site: 16 checks pass, 5 recorded carve-outs (the signed Home headings and supporting lines, the hero h1, header-to-content; each entered from Chat's ANSWER__Home_Search_Words_And_Hairline_Ruling_S573 section 5 and listed under Recorded exceptions below) |
| 3 | Metadata and preview data | machine | pass, 2026-11-25, [machine, theme 0.708.490] meta-title 59 characters (Achology: Understand Yourself, Then Help Others Do the Same) and meta-description 150 characters, both Kain's signed words ("Yes, those words"), served now that Home is the static front page; address `/` matches DSRD 1; canonical and indexing are the noindex build-ground carve-out (section 3 row 3, S245); the open graph picture is handled sitewide |
| 4 | Schema markup | machine | pass, 2026-11-25, [machine, theme 0.708.491, live on achology.com] Schema Markup Validator on https://achology.com/: 0 errors, 0 warnings (WebPage, EducationalOrganization, WebSite, ImageObject); Google's Rich Results Test crawled the live page successfully at 23:11 and flags nothing (no rich result type applies to Home); the one JSON-LD block parses and names only achology.com |
| 5 | Search visibility | machine | pass, 2026-11-25, [machine, theme 0.708.490] Rank Math 97 for post 45038, keyword `achology`, over the 95 target; read from the editor's analyser with nothing saved (tools/score_run.py, session minted and revoked) and written in Code's score table, `~/.claude/achology_rank_math_scores.tsv`, row `45038 97 settled achology`; the page_gate rank-math row reads the same table and prints PASS. The one failing Rank Math test is keywordInImageAlt: Home's pictures are decorative, Chat's call, no alts written (ANSWER__Home_Keyword_Density_Carve_Out_And_Image_Alts_S492 item 2). keyword-density is the template-page carve-out the Courses, Accreditation, Policies and Events pages take (same answer, item 1) |
| 6 | AI visibility | human reader | not run |
| 7 | Accessibility | machine, then human reader | not run |
| 8 | Ease of use | human reader, NEVER the page's builder | not run |
| 9 | Speed | machine | not run |
| 10 | Visual consistency | machine + Kain's eye | pass, 2026-11-25, [Kain] "Yes, it's right", asked "Looking at it top to bottom, is your Home page right?", Safari, https://achologytest.com/ at theme 0.708.490 (banner, What Is Achology?, Voices, the statement card, the course finder, the community block, the films, the Knowledge Hub belt, the questions scrolled top to bottom, the window narrowed once for the phone; RULING__Home_Page_On_The_Build_Site_Kain_Says_It_Is_Right_S572). [machine, theme 0.708.490] page_gate v9: 37 checks pass, 32 recorded carve-outs, 0 failed: every hairline, spacing, boundary-owner, supporting-line and drawing row is a recorded exception of Kain's signed design, listed under Recorded exceptions below |
| 11 | Verification on the live page | machine + Kain's eye | pass, 2026-11-25, [machine, theme 0.708.490] page_gate v9 on the build site: 41 passed, 0 failed, 11 for review, 82 carved out; the 4 chapter-11 checks pass; axe 4.10.2 zero WCAG 2.2 AA violations. [Kain] "Yes, it's right", Safari, the same look as chapter 10, on the built page at 0.708.490 |

**Chapter 8 is Chat's, ruled by Kain at S263:** Chat runs it from the rendered live pages and returns the record through the channel. Code never fills it for a page Code built.

## Machine half, written by Code

**Run 2026-11-25 against https://achologytest.com/, page_gate v9, measured against DSRD 6 Version 32 (18 November 2026).**

Ten of the eleven chapters are split between the machine and a human (DSRD 6 Version 6 runner lines), so a machine pass cannot close one on its own. A machine FAIL does close it, because a failure is conclusive by itself.

- §1: machine half passes, 4 checks, 2 recorded carve-outs. The chapter stays open: its other runner has not run.
- §2: machine half passes, 16 checks, 5 recorded carve-outs. The chapter stays open: its other runner has not run.
- §3: machine half passes, 3 checks, 1 recorded carve-out. The chapter stays open: its other runner has not run.
- §5: machine half passes, 3 checks, 1 recorded carve-out. The chapter stays open: its other runner has not run.
- §7: machine half passes, 1 checks, 0 recorded carve-outs. The chapter stays open: its other runner has not run.
- §10: machine half passes, 37 checks, 32 recorded carve-outs. The chapter stays open: its other runner has not run.
- §11: machine half passes, 4 checks, 0 recorded carve-outs. The chapter stays open: its other runner has not run.

## §12 exemptions applied to this page

- none

## Recorded exceptions (Chat, ANSWER__Home_Search_Words_And_Hairline_Ruling_S573, entered by Code S573; every one is Kain's signed design on the page, carried as the answer words it)

Each is entered in `page_gate.py` under `PAGE_EXCEPTIONS` for `^/$`, matched by the text the gate prints.

1. **Hairline rows, the bands (DSRD 7 4.3 Exception 30).** hairline-present and hairline-spacing at boundaries 1, 2, 5, 6 and 7, at all three widths: Home's blocks are bands whose grounds take turns (DSRD 9 45.29), the change of ground marks the boundary and no hairline stands there, as Exceptions 23, 27 and 29. Kain signed every block on these grounds in the S558 to S572 sittings.
2. **Hairline rows, the statement card (DSRD 9 45.32, DSRD 6 10 one owner).** Both rows at boundaries 3 and 4: the card draws its own edge.
3. **Hairline-present at boundary 8, the belt and the questions block.** The line is drawn (two white bands, 48 either side, DSRD 9 45.31) by `#home-kh > .d-inner::after`, a pseudo-element the gate's reading does not see; entered as its own line with that reason.
4. **boundary-owner, desktop boundaries 6 and 7:** each band carries its own 64, as the school pages and the Policies index.
5. **header-to-content, all widths:** the hero is a full-bleed band flush against the header by design (DSRD 6 section 10's first standing exception), signed S565.
6. **h1, 42px / 700:** the Hero Heading as signed (RULING__Home_Hero_Signed_S565).
7. **block-heading and supporting-line, What Is Achology?:** Kain's own signed words and layout (RULING__Home_Who_Is_Achology_Spacing_Signed_S569; DSRD 9 45.23c; 45.32). **02 Learn to Lead:** a stage card's heading, Kain's signed community copy (45.31 item 9), until the gate is taught.
8. **supporting-line, Achology Is a Collaborative Learning Community (tablet, phone):** the hero-heading top with its lead beside it and a hairline between, signed in RULING__Home_Community_Block_And_The_Dark_Band_Achology_Word_S571; 45.31 item 9.
9. **supporting-line, Find the Right Learning Path for Your Goals, 32 to the filter bar:** Kain's tidy top, read 32 in the signed preview as well (RULING__Home_Course_Finder_Cards_And_Tidy_Top_S571).
10. **supporting-line and spacing-scale, the belt's 20:** the row stands 20 under the line and carries 4 of its own shadow room, so the cards stand the signed 24 from the line; moving it to 24 would make 28. Recorded by name.
11. **spacing-scale, the named values:** the 2 row-gaps (the hair gap the course page carries); the community countdown's c5-go margins, computed from `margin: auto` (RULING__Home_Community_Copy_Countdown_And_Balance_S571); the 49, 33, 31 and 23, each a step with the hairline's own pixel added or taken so the gap seen is on the scale (DSRD 7 4.3 Exception 19's kind).
12. **icon-registry, six drawings:** the three stage pictures (wj__art) and the community rooms' art (c5-bc), Kain's signed graphic design for a page with no photographs (RULING__Home_Block_2_Picked_One_Soft_Panel_S566; DSRD 7 5.2.6). The 24 by 24 glyphs were mended to the registry's attributes at 0.708.487 and 0.708.488.
13. **image-responsive, 71 pictures:** 45 film posters, each frame's only copy is its drawn width, 460, a 920 frame to be taken from the player at cutover (the school pages' ruling, ANSWER__School_Page_Film_Stills_And_Acronyms_S530); and 26 pictures each the only size and at least twice its drawn width (five book covers at 240, five article pictures at 1360, five quote pictures at 1200, five workbook covers at 816, the finder's six at 480 and 240 drawn at 56), measured S573.

## Waiting, named

- **Home set as the build site's front page, 2026-11-25 (Code S573, Kain: "Yes, set it", relayed by the main session).** `show_on_front` `posts` to `page`, `page_on_front` `0` to `45038`, read back from the install (put back with those two old values if ever needed). After it: meta-title PASS (59 characters), meta-description PASS (150), **Rank Math 97 for post 45038, keyword `achology`, at or over the 95 target, written into Code's score table.** The one failing test is keywordInImageAlt (every picture on Home is decorative, alt empty, as Chat's answer foresaw; no signed word changed). keyword-density still reads "the body is empty" from the stored post body. The entries below are the earlier reading (67) and the front-page cause, kept for the history.

- **Search words, set 2026-11-25 (Code S573, Kain: "Yes, those words").** Post 45038 carries focus keyword `achology`, search title "Achology: Understand Yourself, Then Help Others Do the Same" (59 characters) and the 150-character description, as literal text, read back from the install word for word.
- **Rank Math score, read 2026-11-25 (Code S573, editor read, nothing saved, theme 0.708.488): 67 for post 45038, keyword `achology`, under the bar of 90.** Failing tests: contentHasAssets, keywordIn10Percent, keywordInContent, keywordInImageAlt, lengthContent, linksHasExternals, linksNotAllExternals. Passing: contentHasShortParagraphs, keywordInTitle, keywordInMetaDescription, keywordInPermalink, keywordInSubheadings, linksHasInternal, titleStartWithKeyword. Every failing test is a body test and the post has no body (its words live in front-page.php); no signed word was changed to chase them.
- **Not in effect on the front page, and the reason.** The install's Reading setting is `show_on_front = posts` and `page_on_front = 0`: post 45038 is not set as the front page, so for `/` Rank Math uses its Homepage settings (title `%sitename% %page% %sep% %sitedesc%`, description empty). The gate therefore still reads meta-title "Achology TEST Site |" and meta-description 0 chars. That is Kain's setting or Rank Math's Homepage fields; Code has changed neither.
- **keyword-density, entered as a recorded exception 2026-11-25 (Code S573, Chat, ANSWER__Home_Keyword_Density_Carve_Out_And_Image_Alts_S492 item 1):** Home is a template page; its words live in its blocks (front-page.php), not in the post body, so the row reads nothing by design, the same carve-out the Courses, Accreditation, Policies and Events pages take. Gate at 0.708.490: 41 passed, 0 failed, 11 for review, 82 carved out. The record's own chapters stay open for the human and Kain rows (0 closed, 11 not run, 0 fail).

## Chapters still open, and whose they are (2026-11-25, Code S573)

- **1 Copy standards (machine + human reader), 6 AI visibility and 8 Ease of use: Chat's reader chapters.** Kain's look does not cover them; Chat runs them from the rendered page. Chapter 1's machine half passes (4 checks, 2 recorded carve-outs).
- **7 Accessibility (machine, then human reader): the human reader half is open.** The machine half passes (axe 4.10.2, zero WCAG 2.2 AA violations on the build site at 0.708.490); a person reads the rest (keyboard walk, the focus ring, the two enlargements).
- **4 Schema markup (machine): not run, and cannot be run from this Mac as things stand.** It needs Google's Rich Results Test and the Schema Markup Validator, both external browser pages that must be given the build site's page, and the host's robot check (SiteGround Antibot) answers Code's browser with a challenge and gives curl a 202; the build site is also noindex and robots-disallowed, so Google's tool cannot fetch it. What can be read now: the page source printed from the server itself shows one EducationalOrganization node with the ruled description and nothing duplicated. A validator pass on pasted code, as the Code of Character and Membership records did, is the route; it has not been run for Home.
- **9 Speed (machine): not run, and cannot be run from this Mac.** Lighthouse mobile against the build site hits the same robot check, so it would score the challenge page, not Home. It needs the Lighthouse run from a route the host lets through, or after the host's check is relaxed for it.

## History

- 2026-11-25, Code S573, record created from the template; exceptions carried in from Chat's answer; machine half to follow from the board's sweep
- 2026-11-25, Code S573, at theme 0.708.490: Kain's "Yes, it's right" written on chapters 10 and 11 (his Safari look at the built page); machine rows 2, 3 and 5 written from the gate and the score table; chapters 1, 4, 6, 7, 8 and 9 left open and named above

*No em or en dashes in this file; checked before writing.*
