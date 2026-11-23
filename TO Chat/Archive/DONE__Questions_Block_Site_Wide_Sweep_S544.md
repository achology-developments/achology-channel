> Disposition, Chat S480, 23 Nov 2026: written into DSRD 8 section 37 and the Achology Content Standard Part 18 rule 7 (Version 36); archived. No board card moved.

**NEEDS from Chat: write the question standard and the one block into their homes (DSRD 8 section 37, Content Standard), rewrite the Help answers' Getting Started pair only if you wish, and mend or confirm the two Help answers whose bodies still hold dashes (below).** Code, S544 (branch 1), 21 November 2026. Answers SWEEP__Question_Block_Site_Wide_From_The_Membership_Design_20Nov, WORDS__Question_Block_Last_Four_Three_Columns_20Nov, WORDS__Help_Short_Answers_127_20Nov and WORDS__Question_Standard_Site_Wide_Review_21Nov.

# DONE: the questions block site-wide, the old component deleted, the short answers placed

Theme 0.708.334 on the build site (ships 0.708.329 to 0.708.334; see SHIP__Questions_Block_Last_Three_Pages_And_Old_Component_Deleted_S544 and RULING__Question_Standard_Helpful_Questions_Site_Wide_S544).

## What is done

- **The last four places** on the one block: /enquiries/, the Help landing, the 404 and every Help answer, from your words. Each page is fitted to its own page edges (rules in `help.css`). Kain signed Enquiries; the Help landing and 404 were remended on his word (stray hairline, orphan close panel folded into the block's ask line, spacing, the band runs to the footer).
- **Kain's standard** (RULING filed): your review is placed on /pricing/ (three columns of four), /about/, /reviews/, /events/, /accreditation/, /certification/ and the 404, ids, titles, topics and lines exactly as you gave them. The nine one-question retitles (329, 330, 331, 320, 312, 10042, 400, 393, 41428) and 291's excerpt are on the install; slugs, bodies and schema names read the new titles (checked on 329).
- **The 127 short answers:** 125 set on the build site (0 empty of those 125). Two are not, see below.
- **The old component deleted**, completely: the old branch of `achology_faq_block()` (it now only calls `achology_questions_block()`), the short form with its `ids` argument and `q-cards--short`/`q-band--short` rules, `achology_faq_star_icon()`, and 117 selectors across `help.css`, `about.css`, `base.css`, `certification.css`, `courses-directory.css`, `enquiries.css`, `people.css`, `policies.css`, `pricing.css`, `reviews.css` (every `.help-q-list`, `.help-q*`, `.help-popular*`, `.cd-questions`, `.pricing-questions` rule), plus the old rise code in `about.js`, `enquiries.js`, `help-landing.js`, `certification.js`, `policy-doc.js`. `achology_pricing_question_links()` was already gone; `achology_pricing_questions()` now only calls the block. Three borrowers were re-homed with the same values: the Help category page list (`help-cat-q`), the author works list (`ap-works__*`), the founder heading tile (`policy-tile`).
- **The catch**, printed empty: a search of the whole theme (PHP, JS, CSS; not the course data, previews or cloud folders) for `help-q-list`, `help-q__`, `class="help-q"`, `help-popular`, `cd-questions`, `pricing-questions` finds no hit. Not yet empty, and not mine to touch: `qa2__card` and the qa2 tap-to-open code in `course-page.css`, `course-page.js` and four course tools (dead, course data holds none; branch 3 owns the files and will hand them over after its video ship), and `d-faq`, which the school pages' Knowledge block still uses as its ground (school session).
- **Proof nothing visible moved:** computed-style fingerprints of the Help category list, author works list and founder tiles at 1280 and 390, and of the block on About, Reviews, Pricing, Certification and a Help answer at 1280, identical before and after the deletion.
- **Academy:** page gate at 0.708.333: 48 passed, 0 failed, 10 for review, 73 carved out; the questions line is written in its DSRD6_RECORD.md.

## Measures (1280, 768, 390)

Enquiries, Help landing, 404 and Pricing measured at all three: cards on the page's own content edge, three even cards at 1280, one column below, nothing sideways. About, Reviews, Events, Accreditation and Certification checked structurally at 1280 (even cards, every row has its short answer). Supporting lines: Enquiries 1 row at 1280, 2 at 768, 4 at 390; Help landing 1, 1, 2; 404 1 row at 1280 and 768, 2 at 390; Pricing 1 at 1280; none over two rows at 1280.

## Not done, and why

- **Two Help answers, 39306 can-a-life-coach-help-with-anxiety and 39303 become-a-certified-life-coach:** your mended bodies (WORDS__Help_Two_Bodies_Dashes_Mended_21Nov) are not installed. The publishing gate refuses a page that still holds dashes, so it cannot clear the very change that removes them; the way out is a clearance under Kain's ruling, which the main session has been asked to put to him. Their excerpts wait for the same reason.
- **Chat's pages 350:** the Membership session's CPD excerpt for 350 is its to set.
- **Kain's looks** on About, Reviews, Events, Accreditation, Certification, Pricing and the 404 go through the main session one page at a time.

*No em or en dashes in this file.*
