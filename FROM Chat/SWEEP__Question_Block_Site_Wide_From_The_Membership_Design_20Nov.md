CODE DISPOSITION, S541: WAITS ON Kain's one signature, put to him in the S541 sitting.
**For Code, the S541 theme session. NEEDS: Kain's signature first, put to him by you, on two things in one yes: (1) the Membership page's questions design, option 4 Sorted by Topic, is the one questions block for the whole site; (2) this sweep brief and its page list, with the Help Centre held out as section 5 recommends. Nothing in section 6 is built before that yes. Then: build the block once in the shared part and move every page in section 4 onto it, in the order of section 6.** Chat, opened by Code's S541, 20 November 2026.

This brief asks Kain nothing directly. Every question or step he owes goes through the S541 theme session, which puts it to him.

Done when: every page in section 4 draws its questions with the one shared block, no page on the build site draws a questions list of its own, each page's DSRD 6 record carries its questions line as pass, and a DONE in TO Chat names this brief with the measures of section 7.

# SWEEP: one questions block on every page, from the Membership design

## 1. Kain's words and the order agreed

On the built Academy page, 20 November 2026, its questions block "doesn't really finish the page off well". He likes the new questions design at the foot of the Membership page preview and wants it to replace every question block on every page, because the component has drifted. Code agreed the order: Kain signs that design as the one site-wide block, Chat writes this sweep brief (Harness Rule 3: a change across pages runs only under a signed sweep brief from FROM Chat naming its pages), Code builds it once in the shared part and catches the pages that wander.

One thing to check with Kain when you put the signature to him. The relay that opened this session described the Academy block as "three white cards: Choosing a Plan, What You Get, Pay and Cancel". Those are the Membership design's three topics, not the Academy page's. The Academy page today draws the flat list of twelve answers from `data/academy-page/answers.json` in the old card. Show him both on screen, the Academy page as built and the Membership preview's block, so his yes is to the right one.

## 2. The spec: the signed design

- **Which design.** Option 4 of four, "The questions sorted under three topics", in `previews/membership-page/faq-options.html` (written by `faq_options.py`, function `f4`, styled in `faq-options.css`, shown by `round-faq.js`). Kain chose it: "Yes, build 4" (the comment over `questions()` in `previews/membership-page/build.py`, commit 6b5397b8).
- **The built form to copy.** `questions()` in `previews/membership-page/build.py` and the `.memb-faq` rules in `previews/membership-page/memb.css` (the block's rules, the tablet rule and the phone rule for the ask line). The preview page is `previews/membership-page/membership.html`, block 8.
- **Its anatomy, as built there:**
  1. A Light Sand band (DSRD 7 section 3.3a), the page container, the block heading on H2 Section with "Achology" in orange, and one supporting line on the shared lead bar.
  2. Three white cards in one row, even in height, each a group: a topic heading (Como 600, 18) over a 2px orange rule, then its questions.
  3. Each question is one link to its full Help answer: the question (Como 600, 16, dark, turning text-safe orange on hover and focus) over its short answer (Mulish 400, 14, soft grey), a hairline between questions.
  4. Under the cards, one centred line inviting any other question, its link to /enquiries/ with the arrow.
  5. Tablet and phone: one column of cards. Phone: the ask line one step down to 14.
- **What it retires.** The "Q." marks, the single card with its question mark badge, and the old card's rhythm (DSRD 8 section 37, its first three bullets) are gone wherever the block is drawn. The UKRLP and ICO line stays exactly where each page has it today, through `achology_ukrlp_credit()`.

## 3. The shared part it replaces

`achology_faq_block()` in `shared-parts.php` (the `help-close cd-questions` markup, its look in `help.css`). Rebuild it in place, same name, so every caller keeps working:

- Arguments: `id`, `title` (the heading), `line` (the supporting line), `groups` (three, each a `name` and its `ids`), `excerpts` (a page's own short answer for an id, as today), `ask` (the ask line and its link words), `credit` (as today).
- A row whose answer is not published is left out, as today; a group left empty is dropped; with no rows the block draws nothing, as today.
- A page that passes `ids` with no `groups` draws one block whose groups come from the page's words file, never from a guess. Until a page's groups are in its words file, that page stays on the old block and is not moved.
- Its look moves out of `memb.css` into the block's one home, `help.css`, as a shared style, and is registered in the component styles gate. One home: no page stylesheet restyles it.
- The block stands in the page container on its own band. Where a page holds it today inside the 800 reading column (Academy, Events, Reviews, Accreditation, Certification, all through `policy-body pw-section--faq`), it comes out to the full container, as on Membership.
- Bump the version.

## 4. Every page that carries a questions block today

The address, how it draws its block today, and what changes. Each page keeps its own questions and its own heading words. Each gains three topic names and a supporting line, which are Chat's words (section 6, step 1).

| Page | Draws it today | Answers | What changes |
|---|---|---|---|
| /membership/ (post 45034) | Preview only; the theme has no Membership template yet | 8: 239, 10041, 226, 398, 243, the gift answer, 240, 247 | The first caller: its groups, line, excerpts and ask line are signed in `WORDS__Membership_Page_S537.json` (`questions` key). Built with the page. The gift answer links to /help/ until it is published. |
| /academy/ | `achology_faq_block()` from `academy-setup.php`, inside the reading column | 12, from `data/academy-page/answers.json`; heading "Practical Answers Before You Begin" | Out of the reading column onto its own band; groups and line from Chat. |
| /events/ | `achology_faq_block()` from `events-parts.php`, `achology_ev_questions()`, inside the reading column | 8, from the Events words file, 344 holding any unpublished row | Same. |
| /courses/ (Courses Directory) | `achology_faq_block()` from `template-courses.php` | 6: 329, 399, 402, 327, 341, 333; heading "FAQs About Our Online Psychology Courses" | Groups and line from Chat; UKRLP line stays beneath. |
| /reviews/ | `achology_faq_block()` from `page-reviews.php`, inside the reading column | 8: 329, 406, 403, 281, 336, 350, 342, 269 | Same; the CPD spelling out on this page alone stays. |
| /enquiries/ | `achology_faq_block()` from `enquiries.php` | 4: 398, 224, 252, 10054 | Four answers cannot fill three even cards. Chat either adds two signed answers or the page keeps the old block: Chat rules this in the words file. |
| /accreditation/ | `achology_faq_block()` from `template-accreditation.php`, inside the reading column | 12, with Chat's page excerpts for 10014, 10016, 295, 10021 and six more | Same; the `excerpts` stay as they are. |
| /certification/ | `achology_faq_block()` from `template-certification.php`, inside the reading column | 12: 10024, 294, 297, 300, 314, 315, 306, 303, 316, 321, 41428, 307 | Same; the signed close beneath (Certificates Beside) stays. |
| /pricing/ | Its own copy of the old card, `achology_pricing_questions()` in `pricing-parts.php`, six answers by query from two Help categories | 6, by query | The copy goes; the page calls the shared block with six fixed ids and groups from Chat. |
| /about/ | Its own `help-popular` list in `page-about.php` (DSRD 8 section 17) | 8, typed into the template, Kain's line "Click on the links below for common questions about who we are." | The typed list goes; the page calls the shared block with the eight post ids. |
| /testimonials/ | Its own `help-popular` list in `page-testimonials.php` | 6, typed into the template | Same. |
| Every course page (28, `data/course-page/001.json` to `028.json`) | Stored markup, `#course-faqs`, the `qa2` cards: nine buyer-intent questions with their full answers, an icon tile each, opening on a tap on a phone (Kain, 16 November 2026) | 9 per course | The `qa2` markup goes from all 28 files and the shared block draws the nine, three to a group, each linking to its Help answer as "Read the full answer" does today. This retires his phone tap ruling for course pages; say so to him with the signature. The nine short answers and the three topics are Chat's words. The section bar's "FAQs" link still lands on `#course-faqs`. |

Pages with no questions block, so not touched: the seven school pages and the Access All Areas Pass page (Kain ruled questions off the school page; the knowledge tree stands there), the free teaching pages, the policy pages (their tiled headings borrow the badge only), the author profiles (their works list borrows the list class only), and the Help category pages (their close lists categories, not questions). The site has no front page template yet.

## 5. The Help Centre: held out, Chat's recommendation

Three more lists are questions lists, but they belong to the Help Centre's own design, not to a page's foot:

- every published Help answer's "Other Related Questions" (`single-faq_article.php`, exactly four by DSRD 2 section 2.24 item 6, inside the two-part closing card Kain signed at S110 and S181);
- the Help landing's "Popular Articles" (`archive-faq_article.php`, six by rank);
- the 404 page's "Popular Questions" (`404.php`, four by rank).

Chat recommends they stay as they are: each holds four to six questions with no topics, the Help answer sits in the 800 reading column, and the four related answers change answer by answer, so three topic cards would stand half empty. Put it to Kain inside the one signature: if he wants them in too, they come in a second sweep brief with their own rule for a short list.

## 6. The order of work

Size, cost and place: one theme job in Code's S541 theme session, on Kain's plan. About fourteen PHP files, `help.css`, and the 28 course data files through the course data tool. No copy is written by Code.

1. **Words first (Chat).** Chat writes `WORDS__Question_Block_Groups_And_Lines_Site_Wide_20Nov.json` into FROM Chat: for each page in section 4 after Membership, its three topic names with their ids, its supporting line, its ask line, and for the course pages the nine short answers and the three topics for the nine question spine. Run through Chat's own gates. Code moves no page before its words are in.
2. **The shared part.** Rebuild `achology_faq_block()` and its style in `help.css` to section 2 and 3. Build the Membership page's block on it with its signed words and measure it against the preview at 1280, 768 and 390: it must match.
3. **One page, then show.** Move /academy/ first, since that is where Kain asked. Show him the built Academy block beside the Membership preview. Go on only on his word.
4. **The rest, one page at a time**, in the table's order: events, courses, reviews, enquiries, accreditation, certification, pricing, about, testimonials, then the 28 course pages in one run of the course data tool.
5. **The catch.** Search the theme for `help-close__heading`, `help-q-list`, `help-popular`, `qa2__card` and `cd-questions` outside the Help Centre files of section 5. Every hit left is a page that wanders: list it in the DONE and move it.
6. Bump the version on each ship.

What is derived from what is replaced (Harness Rule 3): the section bar's FAQs anchor on every course page; the Rank Math subheading test on /courses/, which reads the heading (the heading words do not change); `help.css` rules shared with the Help answer's closing card, which must not move it; the DSRD 6 records of every page listed.

## 7. The checks

On every page moved, at 1280, 768 and 390:

1. The DSRD 6 page gate, with the questions line of the page's record written pass, or the blocking line named.
2. The register check (`measure.js` from the Membership preview, or the theme's own): every type style on DSRD 7's register, nothing as large as the block heading, heading to line 16, line to cards 24, band padding 64, 48, 32.
3. The three cards even in height in their row at 1280; one column at 768 and 390; nothing scrolls sideways.
4. Every question link opens its published answer with a 200; no row shows an unpublished answer.
5. The UKRLP line where it was, and nothing else on the page moved.

The DONE prints, for each page, the three widths' pass or fail and the gate's score.

## 8. Homes to write after the build (Chat)

DSRD 8 section 37 is rewritten to the signed design, with sections 17's list and 37's old bullets kept beneath as the record, and the course page's questions entry in DSRD 9 points to it. Chat writes these on the DONE.

## 9. Vault notes for this job

The Shared Road and the Words notes govern the words of section 6 step 1, which Chat writes. The Help answer pack (17 Packs) governs each short answer, since a short answer is the Help answer's own excerpt or a page's summary of it. Nothing else here is copy.

OWED BACK: a DONE in TO Chat naming this brief, with Kain's words on the signature, the measures of section 7 for every page, and the list from step 5.

*No em or en dashes in this file; checked before writing.*
