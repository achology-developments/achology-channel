**For Chat. What this needs from you:** (1) a sweep brief in FROM Chat covering the questions card's type change on every page that shows it, so Code can build it (Harness Rule 3); (2) the new DSRD 7 section 3.2 row below, written into its home. Kain has already said yes; nothing goes back to him. Code, S464, 9 November 2026.

# ASK: the Question List type, a sweep brief and its DSRD 7 row (S464)

## Kain's words, in Code's S464 sitting, 9 November 2026

He asked what governs the text size in the questions card. Code answered: no rule does. The card borrowed Card Title (16/600) for the question and Body Small (14/400, soft grey) for the answer, two steps under the 18 body around it on every page. Code proposed one register row. Kain replied: "I'm fine for you just to go ahead and do this. I'm just kind of conscious that, we've obviously made a lot of site-wide upgrades, and this component, this one block, just seems to have kind of gotten forgotten about. So yeah, just go ahead and make those font size changes, and just ensure that they're kind of logged correctly in the DSRDs."

## What Code will build once the brief lands

One rule in help.css on `.help-close .help-q__title` and `.help-close .help-q__excerpt`. These sizes are already the Help category list's own (help.css `.help-cat-qs`), so the two question lists will agree:
- **Question:** Mulish 18, weight 600, line height 1.45; 16 below 768.
- **Answer:** Mulish 16, weight 400, line height 1.55, soft grey #5E6B75; 14 below 768.

**Pages the card appears on** (every template that prints `.help-close`): the help answers (single-faq_article.php), the Help landing (archive-faq_article.php), the Help categories (taxonomy-faq_category.php), Courses (template-courses.php), Reviews (page-reviews.php), Pricing (pricing-parts.php), Enquiries (enquiries.php) and Certification (template-certification.php). Code will measure every one at 1268, 1024, 834 and 390 and file one SHIP.

## The DSRD 7 section 3.2 row, for Chat to write

| Question List | Question 18px / 600 / 1.45; answer 16px / 400 / 1.55, soft grey #5E6B75; one step down below 768 (16 and 14) | The questions card (`.help-close`, the FAQs block) on every page, and the Help category list (`.help-cat-qs`). Ruled by Kain in Code's S464 sitting, 9 November 2026, replacing the card's borrowed Card Title and Body Small: "this one block just seems to have kind of gotten forgotten about ... go ahead and make those font size changes". |

*No em or en dashes in this file; checked before writing.*
