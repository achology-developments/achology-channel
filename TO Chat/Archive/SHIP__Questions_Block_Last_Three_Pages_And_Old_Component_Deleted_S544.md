> Disposition, Chat S480, 23 Nov 2026: record; archived. No board card moved.

**NEEDS from Chat: nothing yet; the full DONE for the sweep follows when the 127 short answers and Kain's looks are in.** Code, S544 (branch 1, questions sweep), 21 November 2026.

# SHIP: the questions block on Enquiries, the Help landing and the 404, and the old component deleted

Theme 0.708.329 and 0.708.330 on the build site.

## What changed and why

- **0.708.329.** /enquiries/, /help/ (Popular Articles) and the 404 now draw the signed three-column block, from `WORDS__Question_Block_Last_Four_Three_Columns_20Nov` (headings, lines, column titles and ids exactly as given). Each is fitted to its own page edges in `help.css`: Enquiries on the form's content edges (gutter 24, 32, 40), the Help landing on its own frame (the generic rule), the 404 in its 800 column as the Help answer stands. Measured at 1280, 768 and 390: three cards even in height at 1280, one column below, nothing sideways. Kain's looks go through the starting session.
- **0.708.330.** The old one-card component is deleted: the old branch of `achology_faq_block()` (it now only calls `achology_questions_block()`), the short form and its `ids` argument, `achology_faq_star_icon()`, the old rules in `help.css`, `about.css`, `base.css`, `certification.css`, `courses-directory.css`, `enquiries.css`, `people.css`, `policies.css`, `pricing.css`, `reviews.css` (117 selectors), and the old rise scripts in `about.js`, `enquiries.js`, `help-landing.js`, `certification.js`, `policy-doc.js`. Three borrowers were re-homed to their own classes with the same values: the Help category page's list (`help-cat-q`), the author profiles' works list (`ap-works__*`) and the founder pages' heading tile (`policy-tile`). Proved unchanged: computed-style fingerprints of each borrower at 1280 and 390, and of the questions block on About, Reviews, Pricing, Certification and a Help answer at 1280, identical before and after.

## Left, and why

- The `qa2` course-card rules in `course-page.css` and `course-page.js`, and the course tools, are dead (course data holds none). They are in branch 3's files, so I have asked branch 3 to delete them with its own change.
- `.d-faq` stays: the school pages' Knowledge block uses it as its ground (the school session's file).

*No em or en dashes in this file.*
