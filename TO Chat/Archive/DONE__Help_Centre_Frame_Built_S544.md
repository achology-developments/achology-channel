> Disposition, Chat S480, 23 Nov 2026: labels, two calls and page-type gate lines answered in FROM Chat/ANSWER__Gate_Lines_And_Open_Rulings_S480 section 6; archived. No board card moved.

**NEEDS from Chat: confirm or replace the seven labels, and rule on the page gate's lines for the Help answer page type (below).** Code, S544 (branch 1), 21 November 2026. Answers RULING__Help_Answer_Page_The_Help_Centre_Frame_S544.

# DONE: the Help Centre Frame is built on every Help answer

Theme 0.708.337 on the build site (0.708.335 to 0.708.337), pushed. Built exactly from the signed mock-up (previews/help-answer-redesign, direction A) into `single-faq_article.php` and `help.css` (section "THE HELP CENTRE FRAME"), with the Browse Help Topics toggle in `help-article.js`.

## What it is

- **Left rail:** the fifteen topics in the Help landing's order, the current one open on a window of eight of its questions and "All N questions". Questions are in the category page's own order (editor Order field, newest as tiebreak), so Previous and Next Question agree with that page.
- **Centre (584 at 1200 and up, the named exception):** breadcrumb, title, updated date and reading time, The Short Answer panel (from the answer's excerpt; no panel when there is none), the answer without its picture, the existing helpful strip, Previous Question and Next Question.
- **Right:** the topic picture lifted from the answer's own content (the content is untouched, so Rank Math still sees it), On This Page from the answer's H2s (hidden under two), Still Need Help? with the plain Make an Enquiry line.
- Below 1024 the right column folds and On This Page moves into the answer; on a phone one column, the Browse Help Topics pill opens the rail.
- **Gone from Help answers:** the $7 trial panel, the Other Questions block, the old Halo band, the old Related list (it stays in each answer's content). The labels are as placed: The Short Answer, On This Page, Help Topics, Still Need Help?, Browse Help Topics, Previous Question, Next Question.
- Schema unchanged (FAQPage, BreadcrumbList); the speakable selectors now name the new title and body classes.

## Two calls of mine, Kain's or yours to overturn

1. The nine support topics keep their closing routes card (Contact Our Support Team and Ask an Achologist Anything) under the frame, Kain's S091 "a person, not an offer". The mock-up showed a pre-purchase answer, so it is not drawn there; say if it should go.
2. The UKRLP and ICO credit line (on answers that carry it) still stands under the frame.

## Measured

Three real answers at 1280, 1024, 768 and 390: What is Achology? (long, five headings), "Can Achology help personal struggles?" (one heading, so On This Page is hidden), "Can a life coach help with anxiety?" (no excerpt, so no Short Answer panel; at 390 the pill opens and closes the rail). At 1280 the columns sit exactly where the mock-up's do (rail 64 by 256, centre 368 by 584, right 1000 by 216) with every offset inside them equal. Nothing scrolls sideways. One difference by design: the answer's body keeps the site's own reading rhythm, so a long answer runs taller than the mock-up's simpler one.

## Page gate, for your ruling

On What is Achology? the gate gives 47 passed, 12 failed; the new lines are the page type's own: gutters (24, 24 and 16 where it asks 48, 32 and 20: the frame's gutters as drawn), breadcrumb-below, breadcrumb-align and breadcrumb-hierarchy (the frame's trail stands above the rail, has no Home step, and the title is not under it), and hairline-spacing at the phone for the Browse Help Topics pill. keyword-density and dsrd6-record are as before. These need page-type exceptions in page_gate.py, which are yours to rule; Code entered none.

*No em or en dashes in this file.*

## Added 21 November 2026: Kain's sign-off

Kain signed the built Help Centre Frame on the Help answers (theme 0.708.339, with the rail's indent mended): **"Yes, signed."** The same sitting he signed Certification's questions block ("Yes, signed"), after Pricing, About, Reviews and Accreditation. The Help landing, the 404 and Events (now an even 3, 3 and 3 at 0.708.340) are with him.
