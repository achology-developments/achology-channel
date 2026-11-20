CODE DISPOSITION, S541: WAITS ON the S541 build, which takes it now: the shared block first, then Academy shown to Kain before any other page.
DOCUMENT TYPE: sweep brief. Not a page spec.
**For Code, the S541 theme session. NEEDS: build the one questions block in the shared part, move every page and list in section 4 onto it (Academy first, shown to Kain beside the Membership preview), then delete the old component from the theme and the components library once the catch finds no hit. Kain has signed (section 1). The words are in WORDS__Question_Block_Groups_And_Lines_Site_Wide_20Nov.json.** Chat, opened by Code's S541, 20 November 2026; revised the same day on Kain's "Yes, fully site-wide", and again on his S541 withdrawal of the short form ("Yes, that one", "Yes, do that").

CODE DISPOSITION, S541: WAITS ON Chat's revision (short lists in, Kain "Yes, fully site-wide") and the WORDS file; Kain signed in the S541 sitting. *(Code's line, kept; both are now in.)*

This brief asks Kain nothing directly. Every question or step he owes goes through the S541 theme session, which puts it to him.

Done when: every page and list in section 4 draws its questions with the one shared block, the catch in section 6 finds no hit, the old component is gone from the theme's code, its stylesheets and the components library, each page's DSRD 6 record carries its questions line as pass, and a DONE in TO Chat names this brief with the measures of section 7.

# SWEEP: one questions block on every page, from the Membership design

## 1. Kain's words and his signature

On the built Academy page, 20 November 2026, its questions block "doesn't really finish the page off well". He likes the new questions design at the foot of the Membership page preview and wants it to replace every question block on every page, because the component has drifted.

**Signed, in Code's S541 sitting, 20 November 2026.** Kain confirmed the aim in his own words: the new block makes the old component obsolete, so it can be "completely" deleted from the components library once integrated. He asked "is there any reason why we wouldn't just make this a site-wide upgrade?", and on Code's recommendation (the short lists drawn in the same block's style as one card, with no topic split, so the old component can be deleted completely and nothing borrowed is left) he answered: **"Yes, fully site-wide".** That yes covers the design as the one site-wide questions block and this sweep, the Help Centre's short lists included.

## 2. The spec: the signed design

- **Which design.** Option 4 of four, "The questions sorted under three topics", in `previews/membership-page/faq-options.html` (written by `faq_options.py`, function `f4`, styled in `faq-options.css`, shown by `round-faq.js`). Kain chose it: "Yes, build 4" (the comment over `questions()` in `previews/membership-page/build.py`, commit 6b5397b8).
- **The built form to copy.** `questions()` in `previews/membership-page/build.py` and the `.memb-faq` rules in `previews/membership-page/memb.css` (the block's rules, the tablet rule and the phone rule for the ask line). The preview page is `previews/membership-page/membership.html`, block 8.
- **The topic form, as built there:**
  1. A Light Sand band (DSRD 7 section 3.3a), the page container, the block heading on H2 Section with "Achology" in orange, and one supporting line on the shared lead bar.
  2. Three white cards in one row, even in height, each a group: a topic heading (Como 600, 18) over a 2px orange rule, then its questions.
  3. Each question is one link to its full Help answer: the question (Como 600, 16, dark, turning text-safe orange on hover and focus) over its short answer (Mulish 400, 14, soft grey), a hairline between questions.
  4. Under the cards, one centred line inviting any other question, its link to /enquiries/ with the arrow.
  5. Tablet and phone: one column of cards. Phone: the ask line one step down to 14.
- **The short form is withdrawn (Kain, S541, 20 November 2026).** He saw the one-card form on a built Help answer and rejected it. The one block on every page is exactly the Academy page's questions block ("Yes, that one"); per page only the heading, supporting line, three column titles and background colour may differ, judged with him page by page. Every place this brief once gave the short form (/enquiries/, the Help landing's Popular Articles, every Help answer, the 404) takes the topic form, two questions in each card; every Help answer shows six questions under three fixed column titles (Kain: "Yes, do that"; DSRD 2 section 2.24 item 6). Their words are in `WORDS__Question_Block_Last_Four_Three_Columns_20Nov.json`.
- **What it retires.** The "Q." marks, the old card with its question mark badge, the `help-popular` badge and header, the course pages' icon tiles and tap to open cards, and the old card's rhythm (DSRD 8 section 37, its first three bullets) are gone wherever the block is drawn. The UKRLP and ICO line stays where each page has it today, through `achology_ukrlp_credit()`.

## 3. The shared part it replaces

`achology_faq_block()` in `shared-parts.php`. Rebuild it in place, same name, so every caller keeps working:

- Arguments: `id`, `title` (the heading), `line` (the supporting line, optional), `groups` (three, each a `name` and its `ids`; the `short` form and its `ids` argument are withdrawn), `excerpts` (a page's own short answer for an id, as today), `ask` (the ask line and link words, or false), `credit` (as today), and `ways` (the Help answer's two ways on, drawn in the ask line's place) and `heading_tag` (h2 by default).
- A row whose answer is not published is left out, as today; a group left empty is dropped; with no rows the block draws nothing, as today.
- Every page's topics, lines and ask come from the words file, never from a guess.
- Its look moves out of `memb.css` into the block's one home, `help.css`, as a shared style, and is registered in the component styles gate. One home: no page stylesheet restyles it.
- The topic form stands in the page container on its own band. Where a page sets it today inside the 800 reading column (Academy, Events, Reviews, Accreditation, Certification, all through `policy-body pw-section--faq`), it comes out to the full container, as on Membership.
- Bump the version.

## 4. Every page and list that carries questions today

The address, how it draws its questions today, and what changes. Each keeps its own questions and its own heading words. The form, topics, lines and ask for each are in the words file, in this order.

| Page | Draws it today | Answers | Form, and what changes |
|---|---|---|---|
| /membership/ (post 45034) | Preview only; the theme has no Membership template yet | 8: 239, 10041, 226, 398, 243, the gift answer, 240, 247 | Topics. The first caller: its words are signed in `WORDS__Membership_Page_S537.json` (`questions` key). Built with the page. The gift answer links to /help/ until it is published. |
| /academy/ | `achology_faq_block()` from `academy-setup.php`, inside the reading column | 12, from `data/academy-page/answers.json` | Topics, 4, 4 and 4. Out of the reading column onto its own band. |
| /events/ | `achology_faq_block()` from `events-parts.php`, `achology_ev_questions()`, inside the reading column | 8, from the Events words file | Topics, 3, 3 and 2. Same. |
| /courses/ (Courses Directory) | `achology_faq_block()` from `template-courses.php` | 6: 329, 399, 402, 327, 341, 333 | Topics, 2, 2 and 2; the UKRLP line stays beneath. |
| /reviews/ | `achology_faq_block()` from `page-reviews.php`, inside the reading column | 8: 329, 406, 403, 281, 336, 350, 342, 269 | Topics, 2, 3 and 3; the CPD spelling out on this page alone stays. |
| /accreditation/ | `achology_faq_block()` from `template-accreditation.php`, inside the reading column | 12, with the template's page excerpts | Topics, 4, 5 and 3; the `excerpts` stay as they are. |
| /certification/ | `achology_faq_block()` from `template-certification.php`, inside the reading column | 12 | Topics, 4, 4 and 4; the signed close beneath (Certificates Beside) stays. |
| /pricing/ | Its own copy of the old card, `achology_pricing_questions()` in `pricing-parts.php`, six by query | 6, now fixed: 41446, 10041, 235, 221, 236, 237 | Topics, 2, 2 and 2. The copy and its query go; two page excerpts in the words file. |
| /about/ | Its own `help-popular` list typed into `page-about.php` | 8 | Topics, 3, 2 and 3; Kain's S091 line and the typed excerpts stay word for word. |
| /testimonials/ | Its own `help-popular` list typed into `page-testimonials.php` | 6 | Topics, 2, 2 and 2; Kain's S091 line and the typed excerpts stay word for word. |
| Every course page (28, `data/course-page/001.json` to `028.json`) | Stored markup, `#course-faqs`, the `qa2` cards with full answers, icon tiles, tap to open on a phone (Kain, 16 November 2026) | The same 9 slots on all 28 | Topics, 3, 3 and 3. The `qa2` markup goes from all 28 files through the course data tool. Each short answer is the first two sentences of the course's own signed answer, word for word. This retires the phone tap ruling for course pages, inside Kain's "fully site-wide". The section bar's "FAQs" link still lands on `#course-faqs`. |
| /enquiries/ | `achology_faq_block()` from `enquiries.php` | 6: 224, 10054, 398, 236, 370, 252 | Topics, 2, 2 and 2 (today's four kept, 236 and 370 added). No ask line, since the page is the way to ask. Words in the last four file. |
| /help/ (Help landing) | `achology_faq_block()` from `archive-faq_article.php`, "Popular Articles" | 6: the six ranked today, fixed | Topics, 2, 2 and 2. Its own close beneath stays. Words in the last four file. |
| Every published Help answer | `achology_faq_block()` from `single-faq_article.php`, "Other Related Questions" | 6 each: two related, two most asked, two getting started | Topics, 2, 2 and 2, under More on This Topic, Most Asked and Getting Started, headed Other Questions People Ask (Kain, S541, "Yes, do that"; DSRD 2 section 2.24 item 6). The two ways on stand in the ask line's place; the routes part and the trial panel beneath stay. Words and fill rules in the last four file. |
| /404 | Its own `help-popular` block in `404.php`, "Popular Questions" | 6: 218, 224, 329, 243, 220, 221 | Topics, 2, 2 and 2 (today's four by rank kept, 224 and 221 added); Kain's S091 line stays; the ask line closes it. Words in the last four file. |

## 5. The pieces that only borrow the old styling, ruled

The old component cannot be deleted while anything leans on its classes. Each borrower is ruled here, Chat's call, so nothing visible changes on a page Kain has signed except its questions:

1. **The policy pages' tiled headings** (`template-policy.php`, the `help-popular__badge` and `help-popular__glyph` classes on the orange tile before each heading; `policies.css`). Not a questions list. **Re-homed:** the tile takes its own class, `policy-tile` (already on it) with `policy-tile__glyph`, its rules moved into `policies.css` with the same values. No visible change.
2. **The author profiles' works list** (`template-author-profile.php`, `help-q-list ap-works__list`, with `people.css` lines 253 to 255). A list of an author's works, not questions. **Re-homed** to its own classes, `ap-works__list`, `ap-works__row`, `ap-works__title`, `ap-works__line`, its rules moved into `people.css` with the same values. No visible change.
3. **The Help category pages' close** (`taxonomy-faq_category.php`, `help-close` parts holding the sibling categories and the routes). Not a questions list. It shares the Help answer's two-part closing card, which stays. **Kept,** as the closing card's frame (section 6, step 7 says which classes stay).
4. **The loose rules in other stylesheets** that touch the old list or badge: `base.css` (`help-popular`), `about.css` (`help-close__heading`, `help-popular`, `help-q__title`, `help-q__excerpt`), `courses-directory.css` (`help-close`), `certification.css` (`help-close__*`, `help-q*`), `enquiries.css` (`help-close`, `help-close__mark`, `help-q-list`), `academy.css` (`help-close__heading`), and in `course-page.css` every `d-faq`, `qa`, `qa2`, `qa4`, `ic1`, `id1` and `bq` questions rule. **Dropped** with the pages that used them; one home, `help.css`, styles the new block.
5. Not borrowers, and untouched: the Question Panel (`policy-ask`, the legal pages' close, its own component with its own build sheet), and the comment in `knowledge-hub.css` that names `help-popular` (reword it when the class is gone).

## 6. The order of work

Size, cost and place: one theme job in Code's S541 theme session, on Kain's plan. About sixteen PHP files, ten stylesheets and the 28 course data files through the course data tool. No copy is written by Code.

1. **Words.** In: `WORDS__Question_Block_Groups_And_Lines_Site_Wide_20Nov.json` in FROM Chat, Academy first, and `WORDS__Question_Block_Last_Four_Three_Columns_20Nov.json` for the last four places, which replaces that file's four short entries.
2. **The shared part.** Rebuild `achology_faq_block()` and its style in `help.css` to sections 2 and 3, the topic form. Build the Membership page's block on it with its signed words and measure it against the preview at 1280, 768 and 390: it must match.
3. **One page, then show.** Move /academy/ first, since that is where Kain asked. Show him the built Academy block beside the Membership preview. Go on only on his word.
4. **The rest, one page at a time**, in the table's order. The 28 course pages go in one run of the course data tool. Show Kain one Help answer in the topic form, six questions in three cards, before the rest of the Help answers move.
5. **The borrowers,** re-homed or dropped as section 5 rules.
6. **The catch.** Search the whole theme for `help-q-list`, `help-q__`, `class="help-q"`, `help-popular`, `cd-questions`, `qa2__card`, `d-faq`, `pricing-questions` and the "Q." mark rule. Every hit left is a page or rule that wanders: move it, then search again until there is no hit. Print the empty search in the DONE.
7. **Delete the old component, completely, once the catch is empty.** From `help.css` and every stylesheet: the old list, its "Q." marks, its badge, its header and its rhythm. From `shared-parts.php`: the old markup. From `pricing-parts.php`: `achology_pricing_question_links()` and `achology_pricing_questions()`. From the component styles gate and the component gallery (`tools/component_gallery.py`): the old entries, with the new block registered in their place. The Help answer's closing card frame stays, because Kain signed it and the new block sits inside it: `help-close`, `help-close__part`, `help-close__head`, `help-close__heading`, `help-close__body`, `help-close__foot` and the routes classes. Name in the DONE every rule and function deleted.
8. Bump the version on each ship.

What is derived from what is replaced (Harness Rule 3): the section bar's FAQs anchor on every course page; the Rank Math subheading test on /courses/, which reads the heading (the heading words do not change); the Help answer's closing card, which must not move; the Help answers' FAQPage or other schema, if any reads the related list (check `schema-parts.php` and leave the schema's output unchanged); the DSRD 6 records of every page listed; `tools/supporting_line_gate_test.py` and `tools/academy_page_data.py`, which name the old classes and are updated to the new ones.

## 7. The checks

On every page moved, at 1280, 768 and 390:

1. The DSRD 6 page gate, with the questions line of the page's record written pass, or the blocking line named.
2. The register check (`measure.js` from the Membership preview, or the theme's own): every type style on DSRD 7's register, nothing as large as the block heading, heading to line 16, line to cards 24, band padding 64, 48, 32.
3. The three cards even in height in their row at 1280; one column at 768 and 390; nothing scrolls sideways.
4. Every question link opens its published answer with a 200; no row shows an unpublished answer.
5. The UKRLP line where it was, and nothing else on the page moved.
6. The supporting lines: each one's rows at 1280 and its last row's word count, as the words file asks; any line past two rows or with a last row under four words reported with its words, and changed by nobody but Chat.
7. On a Help answer and a Help category page: the two-part closing card measured before and after, unchanged but for the list.
8. On a policy page and an author profile: the re-homed tile and works list measured before and after, unchanged.

The DONE prints, for each page, the three widths' pass or fail and the gate's score.

## 8. Homes to write after the build (Chat)

On the DONE, Chat rewrites DSRD 8 section 37 to the signed block, both forms, and retires DSRD 8 section 17 (the Related Questions Block), each old entry kept beneath as the record and marked retired by Kain's "Yes, fully site-wide"; the course page's questions entry in DSRD 9 points to section 37; the Question Panel build sheet is untouched. A build sheet for the new block goes into Component Design Prototypes, written from the built block.

## 9. Vault notes for this job

The Shared Road, the Words notes and the short lines rule in 03 Voice (a set of lines sharing one space is judged by its rows at the built width) govern the words file, which Chat wrote. The Help answer pack governs each short answer, since a short answer is the Help answer's own excerpt or a page's summary of it. Nothing else here is copy.

OWED BACK: a DONE in TO Chat naming this brief, with the measures of section 7 for every page, the empty catch from step 6, the list of what step 7 deleted, and any supporting line reported under check 6.

*No em or en dashes in this file; checked before writing.*
