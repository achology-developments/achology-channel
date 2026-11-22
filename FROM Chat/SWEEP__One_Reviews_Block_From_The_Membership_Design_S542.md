CODE DISPOSITION, S542: DONE. Built by S545 at 0.708.350 on the seven schools, the Pass, 27 courses and Membership; DONE__One_Reviews_Block_From_The_Membership_Design_S545 in TO Chat; course 005 carried by ASK__Course_005_Reviews_Block_S545.
**NEEDS, for Code's S542 theme session: build one shared reviews block from Membership's design, show Kain the one block on a school page beside Membership with the words file's four headings and lines as one set, and put him the two questions in section 8; on his word, move every page in section 4 onto it, then delete the old wall's foot links and its phone ordering rules once the catch in section 6 finds no hit. Kain has ruled (section 1). The words are in WORDS__Reviews_Block_Headings_Lines_And_Control_S542.json.** Chat, opened by Code's S542, 20 November 2026.

DOCUMENT TYPE: sweep brief. Not a page spec.

This brief asks Kain nothing directly. Every question or step he owes goes through the S542 theme session, which holds him in Safari and puts it to him.

Done when: every page in section 4 draws its reviews with the one shared block and its row count, the catch in section 6 finds no hit, each page's DSRD 6 record carries its reviews line as pass, and a DONE in TO Chat names this brief with the measures of section 7.

# SWEEP: one reviews block on every page, from the Membership design

## 1. Kain's words and his ruling

From `TO Chat/RULING__One_Reviews_Block_From_The_Membership_Design_S542.md`, Code's S542 sitting, 20 November 2026. On the schools' block: "keep that 2 rows deep, with the 3rd row optional". Of Membership's: "make a component out of this ... with options to present 1 row, 2 row, 3 rows, or even 4 rows", each page with "the appropriate reviews and videos", a visitor seeing two rows and opening the third by a press. He set aside Code's four-option round with "you're proposing something completely different for the schools page. Do you think that's wise?" To "Shall I make Membership's reviews block the one standard, two rows on the schools?": **"Yes, do that".**

That yes covers the look as Membership's, the per page row count, the one control, the two link cards replacing the text links, and the phone's swipe kept. It does not yet cover the four headings and lines as a set (he asked that they be agreed) or the row counts on the course pages and the Pass: section 8.

## 2. The spec: the signed design

- **Which design.** Membership's block 6, "The School Block" (Kain's "Yes, build 1", 20 November 2026, `round-voices3.js` option 1).
- **The built form to copy.** `members()` in `previews/membership-page/build.py` and the `.memb-voices`, `.memb-wall`, `.memb-vid`, `.memb-rv`, `.memb-who` and `.memb-way(s)` rules in `previews/membership-page/memb.css`, block 6 and the block's lines in the tablet and phone rules. It is itself built on the school block's parts (`pfp` in `course-page.css`), so the shared block keeps those parts and adds Membership's.
- **The block, top to foot:**
  1. The head: `pf-head pfp-head`, the heading on `d-title` with "Achology" in orange, the supporting line on the shared lead bar. Words per kind from the words file.
  2. The figures strip, `pfp-figs`: each page keeps its own four figures exactly as today (the schools theirs, the courses theirs, the Pass its own, Membership the Student Reviews page's four).
  3. The rows. Each row is one film beside two reviews, three across in Membership's `memb-wall` grid. The film stands first in every row, as on Membership. Today's school and course wall steps its film across the columns (film, review, review; review, film, review; review, review, film); that stepping goes, and each film keeps the same two reviews it sits with today: row 1 is film 1 with reviews 1 and 2, row 2 film 2 with reviews 3 and 4, row 3 film 3 with reviews 5 and 6. Chat's call, since it is what "Membership's design the standard" draws; Kain sees it in the side by side and may overturn it.
  4. The control, only where a page holds more rows than it shows: section 3.
  5. The two link cards, `memb-ways` (Membership's `memb-way` card: icon disc, title, line, orange arrow disc), in place of the two `pf-foot pf-foot--two` text links. Words and order from the words file.
- **The cards inside a row keep their own faces.** A student review keeps the school card exactly (`pfp-rv`: mark, stars, verified mark, date, course label, the larger words for a short review, and the Cards That Turn button "Next review" with its `pf-pool`). A member story keeps Membership's (`memb-rv`: the pull as its headline, photo, badge, level, profile link). The film keeps `pfp-vid` with its time, name and place. Membership's spoken line under its film (`memb-vid__say`) is drawn only where a page holds that film's line; no school, course or Pass film holds one today (section 8, question 2).
- **Tablet, 768 to 1023:** Membership's rule. Two columns; each row's film runs the full width over its two reviews.
- **Phone, under 768:** a block of more than one row keeps the schools' two swipe rows (`course-page.js`, "TWO ROWS TO SWIPE ON A PHONE", Kain, 16 November 2026, pick 325): every film of every row, held ones included, in one row to swipe, every review in a row beneath. No control on a phone. A block of one row (Membership) keeps its signed one column. The two cards stack, as on Membership.
- **Each page keeps its own films and reviews, in their order today** (Kain's ruling, point 2). Nothing is drawn from another page's set.

## 3. The control

- Drawn between the last row shown and the two cards, centred, only at 768 and up, only where the page's rows exceed its count.
- A `button`, never a link, from the button family: `btn btn-secondary`, the same variant as the page's other secondary buttons, measured beside one of them before Kain sees it. No new style.
- Words: "Show More Reviews and Videos" (words file, with why it names both). Its visible words are its spoken name. `aria-expanded="false"` and `aria-controls` naming the held rows.
- One press opens every held row. The button then leaves the page, and focus moves to the first card of the first opened row. No "Show Fewer".
- The held rows are hidden by the script only, so without the script every row shows and nothing is lost. The held films' posters stay `loading="lazy"`.
- On opening: run the wall's card fitting again (`equalise()` and the last lines lay in `course-page.js`), since a hidden card measures nothing.

## 4. Every page and its row count

| Page | Data today | Rows held | Rows shown | Control |
|---|---|---|---|---|
| The seven schools (`data/school-page/` cbp, lc, mh, miw, nlp, pc, pgd) | 3 films, 6 reviews, pool of 12 | 3 | **2** (Kain's ruling) | Yes |
| The 28 course pages (`data/course-page/001.json` to `028.json`) | 3 films (the same three members on all 28), 6 of the course's own reviews, pool of 7 | 3 | **2, recommended** (section 8, question 1) | Yes |
| Course 005 | 3 films, **1 review**, pool empty | see the note | see the note | see the note |
| The Access All Areas Pass (`data/pass-page/parts.json`) | 3 films, 6 reviews, pool of 12 | 3 | **2, recommended** (section 8, question 1) | Yes |
| /membership/ (post 45034; the preview until its theme template is built) | 1 film, 2 member stories | 1 | **1** (Kain's ruling) | No |

**Course 005.** It holds one review and an empty pool, so it cannot fill even one row of one film beside two reviews. Code reads 005's course name and its count in the review bank (`previews/course-page-s208/design`) and reports both in its first reply to Chat. If the bank holds six or more verified reviews for that course, the course data tool places them as on the other 27 and 005 takes the course count. If it holds fewer, Chat rules 005 on the count Code reports; until then 005 keeps its block as it is today. Kain is not asked about this.

## 5. The shared part

- One PHP function in `shared-parts.php`, `achology_reviews_block()`, drawing sections 2 and 3 from arguments: `id`, `kind` (school, course, pass or membership, which picks the words), `figures`, `rows` (each a film and two reviews, in order), `show` (1 to 4), `pool` (the turning reviews, or none) and `ways`. A row missing a film or a review is left out; with no full row the block draws nothing.
- The 36 stored pages carry the block as markup in their data files today. The three data tools (`tools/school_page_data.py`, `tools/course_page_data.py`, `tools/pass_page_data.py`) write it from the shared part's markup, so a later run of any tool cannot put the old wall back. `two_ways_on()` and `REVIEWS_FOOT` in `course_page_data.py`, which write the two text links, are rewritten to the two cards.
- The look has one home: the `pfp` rules stay in `course-page.css`, and Membership's `memb-wall`, `memb-vid`, `memb-rv`, `memb-who` and `memb-way` rules move beside them as the block's shared rules, renamed to the block's own prefix, registered in the component styles gate. `memb.css` keeps none of them. No page stylesheet restyles the block.
- Bump the version on each ship.

## 6. The order of work

Size, cost and place: one theme job in Code's S542 theme session, on Kain's plan. One shared part, one stylesheet's rules moved, `course-page.js`, three data tools and the 36 data files through them. No copy is written by Code.

1. **Words.** In: `WORDS__Reviews_Block_Headings_Lines_And_Control_S542.json` in FROM Chat.
2. **The shared part** to sections 2, 3 and 5. Build Membership's block on it first and measure it against the preview at 1280, 768 and 390: it must match, since it is the signed design.
3. **One school, then show.** Build one school page (cbp) on it, two rows shown and the third held. Show Kain that page beside the Membership preview, both at computer and phone width, with the four headings and lines as one set, and put him the two questions in section 8. Go on only on his word.
4. **The rest:** the other six schools, the Pass, then the 28 course pages in one run of the course data tool (005 as section 4 says).
5. **The catch.** Search the theme and the 36 data files for `pf-foot--two`, `class="pf-go"` inside `#course-members`, "Read All Student Reviews", "Watch Student Testimonials", the old course line "Reviews and films from students", the phone ordering rules `.pfp-wall>:nth-child(` in `course-page.css`, and `memb-wall`, `memb-way` and `memb-vid` left in `memb.css`. Move every hit, search again until none is left, and print the empty search in the DONE.
6. **Delete,** once the catch is empty: the `pf-foot--two` rules (`course-page.css`, about line 2075) and the `.pf-go` rules if nothing else draws them (search first; leave them if anything does), and the phone `nth-child` ordering rules, which the row markup makes wrong. Name in the DONE every rule and function deleted.
7. Bump the version on each ship.

**What is derived from what is replaced (Harness Rule 3), each checked:**
- `course-page.js`: the phone gather (it reads the wall's children by class; with rows it must read the cards inside the rows, held rows included, and put each back in its row above 767); `equalise()` and the last lines lay (they skip hidden cards, so run again on opening); the Cards That Turn pool (it turns only cards shown; a card in a held row joins once opened); the figures count up (unchanged).
- `tools/image_gate_hidden_ancestor_test.py` and `image_gate.py`: a held row hides its film poster from view at load. The gate must read a held row as content a press reveals, not as a hidden image; the test file's S510 note on course 005 says how the gate reads hidden ancestors today.
- `tools/course_page_check.py`, `tools/course_page_flatten.py`: read the wall's markup; update to the rows.
- The section bar's link to `#course-members` on the course pages: the block keeps that id.
- The no-break ties (`pfp-tie`) in the school heading and line: kept on the same words.
- The DSRD 6 records of the seven schools (closed today, S542), the Pass (closed S540) and the course pages: the reviews line is run again and written pass, or its blocking line named.
- `tools/supporting_line_gate_test.py`: run on the four lines.

## 7. The checks

On every page moved, at 1280, 768 and 390:

1. The DSRD 6 page gate, with the reviews line of the page's record written pass, or the blocking line named.
2. The register check (`measure.js` from the Membership preview, or the theme's own): every type style on DSRD 7's register, nothing as large as the block heading; heading to line, line to figures, figures to rows, rows to control and control to cards each measured against Membership's built block, and the control measured beside the page's other secondary button.
3. At 1280: the rows shown match the table in section 4; each row three across, film first, its three cards even in height. At 768: each row's film over its two reviews. At 390: the two swipe rows holding every film and every review, no control, nothing scrolling the page sideways.
4. The control: pressed by mouse and by keyboard (Enter and Space); every held row opens; the button leaves; focus lands on the first opened card; the opened cards are fitted (no review cut, no band of white above a name); "Next review" turns on an opened card.
5. Without the script: every row shows and no control is drawn.
6. The two cards: each opens its page with a 200; hover, focus ring and phone stack as on Membership.
7. Each page's films and reviews are its own and in today's pairs: listed per page in the DONE, before and after.
8. The supporting lines: each one's rows at 1280 and its last row's word count, as the words file asks; any line past two rows or with a last row under four words reported with its words, and changed by nobody but Chat.
9. Nothing else on the page moved: the blocks above and below measured before and after.

The DONE prints, for each page, the three widths' pass or fail and the gate's score.

## 8. The questions for Code to put to Kain, in the side by side

Each answerable yes or no; one at a time, as his rule asks.

1. "Shall the 28 course pages and the Access All Areas Pass show two rows with the third behind the press, as on the schools?" Recommended yes: they carry the same three films and six reviews as a school, and one family reads one way (Kain's rule, standardise the family).
2. "Shall the school, course and Pass films stay without a spoken line under them, as today?" Recommended yes: Membership's line is Alec Wells's own spoken words, and no other film has its words written down; writing them means transcribing each recording, which can follow after launch if he wants it.

Then the words: the four headings and lines in the words file shown as one set on the two pages, for his signature. Three of each are signed already; the one new line is the course line, with its reason in the file. Any change he asks for comes back to Chat.

## 9. Homes to write after the build (Chat)

DSRD 8 holds no entry for this block today (section 14 is the Review Card, section 22 the Review Archive). On the DONE, Chat writes a new DSRD 8 entry for the reviews block from the built block and Kain's ruling, points section 14 to it for the card inside the rows, and points the course page's reviews entry in DSRD 9 to it. A build sheet goes into Component Design Prototypes, written from the built block.

## 10. Vault notes for this job

The Shared Road, the Words notes (04 Words: A Link Is On The Name Of The Thing; No Em Or En Dashes; the word lists) and the short lines rule in 03 Voice govern the words file, which Chat wrote. The reviews and the members' words are their own and are never changed (The Blueprint, A Quote Is Never Changed). Nothing else here is copy.

OWED BACK: a DONE in TO Chat naming this brief, with course 005's count from the review bank, Kain's answers to section 8, the measures of section 7 for every page, the empty catch from step 5, the list of what step 6 deleted, and any supporting line reported under check 8.

*No em or en dashes in this file; checked before writing.*
