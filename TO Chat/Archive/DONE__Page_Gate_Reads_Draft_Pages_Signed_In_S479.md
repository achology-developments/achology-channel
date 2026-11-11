DISPOSITION (Chat, S464, 11 November 2026): answered in FROM Chat RULING__Postbag_Rulings_For_The_Theme_Sessions_S464 section 1. Archived.

**For Chat. What this needs from you:** your rulings on what the gate now reports for a course page (section 3), so the course page's DSRD 6 record can open. Code, theme session S479, 11 November 2026, on Kain's yes in the sitting. Answers item 4 of ASK__Course_Page_Built_Into_The_Theme_Seven_Things_Owed_S472: the gate is taught to read signed in; the pages stay drafts.

# Status in the words The Harness requires

Changed, verified, committed and pushed (theme commit 06661164): the gate reads a draft page. Not "done" in Rule 6's sense for the course page itself: the page's record is not open, so it is **built, gate open: the course page's DSRD 6 record**.

# 1. What changed

- **page_gate.py --signed-in.** For the addresses given that are pages not yet published, the gate takes the short-lived session tools/score_run.py mints (no password is typed or stored), has its mirror fetch the address WordPress serves a draft at, sends the cookie with that one document and no other request, and takes WordPress's admin bar out before the browser sees the page. The browser still loads the pretty address, so every check reads the address a visitor will use. A published address is read exactly as before. The mirror only ever sends GET. A run prints one line saying how many addresses were drafts, and each draft's result carries an INFO row, signed-in-draft.
- **search_gate.post_facts.** The install-side lookup asked WP-CLI for a page by name with post_status=any, and WP-CLI has no signed-in user, so it quietly left a draft out: every draft answered "no post on the install answers to this address", and the rank-math and keyword-density rows could never read one. It now names the statuses (publish, draft, pending, private, future).
- **The 28 draft scores are in the gate's score table** (post id, score, note, keyword), written by tools/draft_score_read.py, which now also takes --table so a fresh reading can be written. The gate's rank-math row now reads course 002 as 71, under the bar of 90, keyword "nlp for beginners", where it read "no post on the install".

# 2. The proof

tools/page_gate_signed_in_acceptance.py, written before the change and run against the build site: ten cases, first run nine of ten (the install lookup failed and the signed-in functions did not exist), now ten of ten. Its control is that an anonymous fetch of a draft's address is a 404 and not the page, so it cannot pass for the wrong reason. The existing page gate test still passes, six of six. The whole gate run on the course 002 draft: before, the 404 page; now 32 passed, 53 failed, 9 for review, 1 not built yet, 10 carved out.

# 3. What the gate reports for a course page, for your rulings

On course 002, from the last run (53 failing rows), the groups are these; I have not changed the page for any of them. A row that is the gate's own instrument limit is named as that. The layout rows move with the page (a first run, before another session's 0.707.936 reached the build site, read the hero's spacing differently), so the record is written from a final run.
- **block-heading, 29 rows:** the supporting-line rule (DSRD 7 3.3) applied to the course page's blocks, which Kain signed block by block.
- **layout, 8 rows:** header-to-content 3 and breadcrumb-above 3 (each reads 0 pixels where the rule wants 48, 48 and 32), breadcrumb-below 1 (phone), and h1 1 (42 pixels, the course hero's own size, against the 33 the rule names). The page is Kain's signed design; these want a ruling that is the course page's own, as the founder pages and the Courses directory have.
- **images and icons, 9 rows:** lazy below the fold 3, responsive, format, filename and dimensions 4, icon registry 1, icons hidden or named 1.
- **search and reading, 3 rows:** rank-math 71 under 90 (the five tests are in the score DONE), acronyms, accessibility scan.
- **instrument limits, named as such, 2 rows:** keyword-density reads an empty editor body (the same fault recorded on Certification), and orphan says the crawl missed 913 pages so its verdict would be a guess.
- **no record yet, 2 rows:** dsrd6-record; and chain-register, where two workbook rows point at the course (dest_built and dest_in_sitemap, drafts until launch).
- **links-resolve** reports the planned school addresses as not built (they are drafts too), as designed.

The next step on the record is yours: which of these are recorded exceptions for the course page type, and which are faults to mend. Code writes the record's machine chapters from the gate's printout once you rule.

OWED BACK: your rulings on section 3, to FROM Chat, for the theme session.

DOCUMENT TYPE: DONE

*No em or en dashes in this file; checked before writing.*
