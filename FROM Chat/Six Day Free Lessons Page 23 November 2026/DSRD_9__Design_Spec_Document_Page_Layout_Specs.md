# ACHOLOGY.COM — Design Spec Document (Page Layout Specs)

*Single source of truth for every confirmed Achology.com page layout: category hub, listing page, individual article page, About page timeline, and the course-page accreditation block. Design foundations are in DSRD 7. Component anatomy is in DSRD 8. Production implementation notes for all page templates are in the Production Implementation Notes document. DSRD 6 — The Page-Readiness Standard — is the go-live gate that confirms each built page matches its locked layout in this document (DSRD 6 §2), commanded open by standing rule 15.*

## Document-Level Standards

Three standards govern every page layout specified in this document. All are held canonically in the vault and in DSRD 2 §0; this document expresses them structurally, never restates them. Each applies to every layout specified or unlocked from its adoption onward; locked layouts (§20–§24) are checked against them at their next unlock, not reopened for them.

**The product-framing layer.** A selling-page layout carries the slots its product's positioning record fills, so the chosen frame is expressed structurally rather than re-decided per page: the header names what the product is in the record's chosen market category; a who-it-is-for placement carries the best-fit student; comparison and alternatives sections are laid out to perform the record's honest alternatives map; and each quantified proof point sits beside the value claim it supports. The record itself is held in DSRD 4 (per DSRD 2 §0.1); this document owns only its structural expression.

**The per-page message lens.** Every page layout expresses the StoryBrand (SB7) message lens in its section order: the header answers the grunt test at a glance (what is offered, how it helps the reader, what to do next); empathy appears before proof; where a page carries a plan, it is visible before the direct call to action; and call-to-action placement matches the page's buyer-readiness stage. The lens and its part mapping per page type are held in the vault and in DSRD 2 §0.2.

**The ethical-influence layer.** A page layout places its influence elements where the reader's state needs them, so the trust sequence is expressed structurally rather than improvised per draft: proof and expertise placements (student numbers, ratings, instructor track record) sit early in the section order, where the reader is still deciding whether this is credible; genuine stakes and the direct call to action sit late, where the reader is deciding whether to act; the strongest claim's placement carries its honesty-against-interest pairing beside it — the genuine limit or fair alternative laid out before the claim, not after; the first ask in the section order is the small, voluntary step (a download, a sample, a saved quote) before the enrolment decision; and no layout carries a pressure device — countdown machinery, stock counters, or urgency banners — unless the scarcity behind it is genuine and its source named. Every influence element a layout slots exists because the smuggler test passed at specification; the pass itself is held in the vault and in DSRD 2 §0.3.

**The composition standard.** Every page layout in this document is derived before it is designed: the page type's job is named as one action by one reader, the reader's arrival and required states are established, the changes between them are listed in the reader's own language, ordered by dependency, and each is assigned a block. A layout's `Page Structure (top to bottom)` list is the output of that derivation, and each entry names the change its block carries, so a later reader can test any block against the job it does rather than against taste. The derived order is also the mobile order — wider viewports may group blocks side by side but never reorder them. The derivation runs once per page **type**, never per instance; where a single instance needs a block the others do not, it is specified as a named optional slot in the type's layout. The methodology is held in the vault and run by `page-composition`; this document owns only the resulting block maps.

A layout locked before this standard was adopted (§20–§24) is checked against it at its next unlock, and any block found to carry no change is reported to the director as a finding, never removed unilaterally.

---

## 20. Category Hub Page Layout (LOCKED S220; RE-CHECKED AGAINST THE CURRENT FOUNDATIONS, S313)

### 20.0 The S153 to S154 redesign: direction D, the editorial front (Kain, Code's S153 and S154 theme sittings; recorded by Chat, S414)

**Status (rewritten S423).** Kain chose every part below from rendered options and **approved the page as a whole at Code's S155 theme sitting** ("it's going to be time for you to build these seven pages"). Code built it for all seven categories at 0.707.161 (S157) and refined it in Safari with Kain to 0.707.213 (S158). This section, with section 20.0c, is the page's layout, and **sections 20.1 to 20.8, 20.10 and 20.13 below are superseded** and kept as the record. Where section 20.0c and the list below differ, section 20.0c is the later ruling and wins. The approved prototype and its build sheet, with every value, are in the Category Hub Page folder; this section records what Kain ruled and why, and names no file inside the folder (standing rule 24). The folder also holds the two research files the directions came from.

**Why it was redesigned.** Kain, looking at the built page in Safari: "I don't know what I'm here for." He asked for research into the best category pages on major publishing sites, then "direction first, best effort design and structural layout, and then we get into molecular details last." The five Part 2 questions of the S378 reconciliation are parked until the layout is settled.

**The direction (D, the editorial front, chosen from four).** Kain: "we can't offer anyone a guided path ... editors picks ... is an easy front door into other articles." No section per content type, and no empty sections.

**Top to bottom, as ruled:**
1. **The head: a dark band, not a hero.** The brand dark band, full width, 480 deep. Left: the trail; "Knowledge Hub Category" in small text above the title (Kain's addition); the title at 42 over a faint Achology bubble mark; one sentence saying what the page is for (the purpose line, section 20.0a); then one bar of four links with icons, Articles, Book Notes, Quotes and Workbooks, each opening the grid on its kind. Right, seven of twelve columns: eight authors from the subject's own book notes, one large and six small, each with the book of theirs the Knowledge Hub holds, no heading over them, sitting 48 from the trail's top line and 48 above the band's foot. Kain: "I am now very, very happy with the Hero Banner. That looks perfect."
2. **The categories bar (S154, "follows you").** A slim dark strip straight under the band: the label "Categories", then all seven categories spread evenly, the current one in light orange with a white Achology bubble behind it at 6 per cent. It pins under the site menu as the reader scrolls. No "All" link. Kain: "They're not subjects, they're categories"; every label says Categories.
3. **The lead row.** The latest article across two thirds, its words centred. Beside it, in the last third, **The Editor's Picks**: a soft panel (#F7F7F6, radius 12, 20 inside) with a quill before the heading and Kain's line under it, "A selection of our editor's favourite reads.", one line on desktop. Four picks, each a small picture with its title in Como 14, two lines at most; no "Article" label and no author name.
4. **The grid.** On a full-width grey plate, a one-line bar: a search box (drawn only, until the site search page exists) beside a joined bar of icon filters, the chosen one dark. Under it a dense four-column grid of 48 cards, newest first, every article and book note labelled with its kind, the four column feet levelled. Book note tiles on this page show the cover as a real book on a soft studio floor (S154, option 5 of eight). Then, 48 below, the link "Explore More Knowledge Hub Articles" to the Articles listing.
5. **The topics,** 48 above the footer. The subject pills at the foot are gone; the categories bar carries them.

**Hairlines (Kain, S153: "as a minimal, as a basic standard").** One site hairline, 48 above and 48 below, between every part; section headings lose their own under-line. This ends the S313 exception 3 for this page once the redesign is built.

**Four departures from DSRD 7, ruled by Kain on rendered options, scoped to this page:** the trail to the title is 32, not the article hero's 48; under the last line of the band to its foot is 64, not section 4.3 rule 3's 48; the title is 42 (the type scale's homepage hero size); and a small label sits above the title, which the article page ruled out at S150.

**Empty kinds are hidden.** Where a category holds no quotes or no workbooks, its link and filter do not show (Kain, S154: "hidden please").

**The cards on this page follow the site-wide card rule** in DSRD 8 (S154): word count and reading time, never a pen name.

**Still open:** Kain approved the whole page at S155 and Code built the tablet and phone layers at S157; what remains open is listed at the foot of section 20.0c (S423).

### 20.0a The purpose line, seven subjects (Chat, S414; RETIRED S158)

**Retired (Kain, Code's S158 sitting; written S423).** The seven lines below are replaced on all seven pages by one subheading in Kain's own words: "All articles in this category are consolidated in one place, making it easier for you to find your next read." The seven are kept as the record.

One sentence under the title saying what the page is for, not what the subject is (Kain, S153). One frame for all seven so the band reads the same everywhere, under 120 characters, two lines in the band's column. "Articles and book notes" rather than all four kinds, because a subject with no quotes or workbooks hides them (section 20.0), and the line must never promise what the page does not hold.

- **Psychology:** Our articles and book notes on how people think, feel and behave, all in one place, so you can find your next read.
- **Helping People:** Our articles and book notes on helping other people well, all in one place, so you can find your next read.
- **Mental Wellness:** Our articles and book notes on looking after your inner world, all in one place, so you can find your next read.
- **Motivation:** Our articles and book notes on what drives you and keeps you going, all in one place, so you can find your next read.
- **Personal Growth:** Our articles and book notes on growing through self-awareness and wise choices, all in one place, so you can find your next read.
- **General Interest:** Our articles and book notes on wider ideas for living a wise and self-directed life, all in one place, so you can find your next read.
- **Wisdom for Life:** Our articles and book notes on thinking clearly and living well, all in one place, so you can find your next read.

### 20.0b Who chooses the Editor's Picks (Chat's call, S414; Kain may overturn it)

**Added S434 (Chat's call, 20 October 2026, answering Code's S176 DONE; Kain may overturn it).** The same rule holds for the Quotes lists and the Workbooks lists as for the Book Notes lists: their Editor's Picks are chosen by hand, by Chat, in the same picks field the book notes use, and until four have been chosen for a list it shows its four newest. No list ever chooses its own picks by score or by date once a hand-chosen set exists.

**The picks are articles only (Kain, Code's S158 sitting: "yes"; written S423).** A book note's upright cover cannot sit in the panel's landscape thumbnail without its title being cut. The empty-field fallback is the four newest articles after the lead. Code replaced every book note in the seeded picks on the build site at S158 and kept the original lists in `RULING__Subject_Page_Audit_Fixes_S158` so any can be put back.

The picks are chosen by hand, never by a rule, because the panel's own line promises "our editor's favourite reads". Each subject page carries a field for its four picks that Kain or Karen can change in the page editor (owner operation, section 5 of the Project Instructions). Chat proposes the first four for each subject; Kain sees them on the built page and keeps or swaps them. If the field is ever empty, the panel shows the four newest articles after the lead article, so the page never shows a gap.

**The Book Notes lists' Editor's Picks follow the same rule (Chat's call, S433, on Code's S174 ship note; Kain may overturn it).** They are chosen by hand: four per subject, in a field on each subject that Kain or Karen can change, the same as the articles' `ach_picks`. Chat proposes the first four for each subject, and Kain keeps or swaps them on the built page. If the field is empty, the list shows the four newest book notes after the lead.

**Later word on the Book Notes lists' picks (Kain, Code's S178 theme sitting, 21 October 2026; written by Chat, S440).** The picks are still chosen by hand as above, but what each pick shows and how the four are arranged is now ruled in section 20.0g: each pick shows the book's name and the words "Read the book note", and the names in a row take the same number of lines, hand-chosen picks included.

### 20.0c What Kain ruled after S154: the page as built for all seven (Code's S155, S157 and S158 theme sittings; written S423)

Each line names the sitting. Every value is in the build sheet in the Category Hub Page folder (its "Decided in S155" and "Decided in S157" rows); the frozen prototype still shows the S154 wall, and its fold-back is owed (the close-out sitting).

**The Editor's Picks panel (S154 close).** Titles in Como 14, two lines at most, centred against each picture; the soft panel (#F7F7F6, radius 12, 20 inside); a quill before the heading, no square, as tall as the heading's letters; heading "The Editor's Picks" and the line "A selection of our editor's favourite reads." in Kain's words.

**The categories bar (S154 close).** A white Achology bubble behind the current category, the small one, centred, at 6 per cent. On a tablet and a phone the seven names scroll sideways beside their label (S157).

**The grid, item 4 above, as now built:**
1. **The kinds are mixed (S157).** Each kind keeps its own newest-first order and the two are interleaved: the kind a category holds fewer of takes at least one place in every row of four where it has enough, spread evenly down the wall in a fixed rotation (third, first, fourth, second place). The same on every load, never random.
2. **Quotes are on the wall (S157).** A category's wall shows the quotes filed in it plus every quote sharing one of its topic tags; the five content attribute tags never count. No quote is moved and no address changes. At most one quote a row, and **no author takes more than two quotes on a wall, the authors taking turns** (Kain: it must not read as "the Kain Ramsay show").
3. **A quote tile is the quote's own baked card picture (S157)**, with the card body under it: the label "Quote Article" and "{n} Words · {n} Minute Read". Only a quote whose picture is baked is used.
4. **Every card's label carries its kind's icon (S157)**, 16 pixels, link orange, before the label.
5. **45 to 48 cards a wall (S157).** An oldest card is left out only if that levels the four column feet by 24 pixels or more.
6. **One Know Your Psychology card (S157),** the generic KYP logo stretched across a white card at one fixed size, linking to the Knowledge Hub home page, placed only where a column's free space holds it at that size, at most one, never squeezed in.
7. **Columns: four on a desktop, three on a tablet, two on a phone (S157).**
8. **The search box reads "Search the Knowledge Hub" (S157);** it searches nothing until the site search page exists.
9. **The tabs above the grid show true totals (S158),** the Quotes tab counting every quote that belongs to the category under rule 2. **No foot buttons under the wall (S158):** the S154 "Explore More Knowledge Hub Articles" link and the S158 per-kind buttons are both removed.

**Empty kinds (S157).** A kind is hidden only where the category truly holds none. Quotes show on every wall under rule 2. Workbooks have no wall tile yet.

**The topic block, item 5 above, as now built (S158).** One block of tags, the same on all seven pages: 31 topics, then the five kinds of article as "Research-Based Articles", "Deep Exploration Articles", "Beginner-Friendly Articles", "Practical Exercise Articles" and "Professional Practice Articles" under "Or read by kind". Every tag 56 tall, one corner, one gap; every row runs edge to edge at every width; equal widths in a row; cream for topics, tinted orange for the kinds; the bubble clipped inside its tag on hover. Heading "Explore the Achology Knowledge Hub by Topic" (S155, Kain's words), with no under-line. This replaces the S155 feature and nine picture tiles and the S158 warm-fade tiles. The per-category topic lists of DSRD 2 section 1.3.3 no longer drive this block; they still drive the quote pool.

**The bottom panel: a learning path, destination first (S155).** The dark card with the diploma in front of a student at his computer, and a grey panel headed "Take Your Learning Further" with the line "Whether you're exploring a topic for the first time or ready to delve into human psychology, Achology offers a clear next step in your learning.", on a stone mountain with a very faint path. Its four steps and the dark card's three ticks are Kain's words (build sheet). Step two links to the workbooks page; step three to the courses page; **step four's course is chosen by hand per category** in an editable field (a practitioner course that counts towards the Achologist title), falling back to the first course of the category's course block. Psychology is set to DiMAP.

**Speed (S157 and S158).** Book covers on the wall draw WordPress's own 200 by 300 copy, with automatic sizes off on this page only; each wall's built data is saved and cleared whenever a piece, category or tag changes.

**Still open, each with who closes it:**
- Chat places or rules DSRD 4 section 5.1's workbook offer for category hubs, now that step two of the learning path links to the workbooks page.
- Chat proposes step four's course for the six other categories, and the dark card's button words for a course that is not a diploma (Code drafted "Explore the Course").
- Chat confirms the three kind names Kain did not name (Beginner-Friendly, Practical Exercise, Professional Practice) and whether "Deep Exploration" replaces "Deep Dive" beyond this block.
- Chat rules, for the listing page, whether a category's quote list includes quotes that share its topics.
- The S159 page gate: Code fixes six template faults (picture sizes, face descriptions, lazy loading, hidden icons, cover formats); five items wait on a ruling, the hairlines, the 42 title and the breadcrumb spacing with Kain's eye (the "Categories" label's contrast closed at S173, section 20.0d), and acronyms in card titles with Chat (`REPORT__Subject_Page_Gate_S159`).
- The close-out sitting: the seven DSRD 6 records, Chat's Rank Math words, and the prototype fold-back.
- Chat records the quote card on the wall (rules 2 and 3 above) in DSRD 8 section 6.0.
- After the page closes, Kain and Chat decide which of its parts become their own components (the categories bar, the Editor's Picks panel, the levelled card wall, the real-book tile).

**Why this section was re-checked, and the one finding that is not a tidy-up.** It was locked before the nine-step type scale (DSRD 7 §3.0, Kain S056), the hairline block-separator standard (DSRD 7 §4.3, Kain S224), the supporting-line grey ruling (S280), the signed card system, and the body face (Kain, Code S085). Locked is not the same as current. Every correction below is conformance to a standard Kain has already ruled, on the same ground as the S280 pass.

**The finding, and Kain's ruling on it (S313).** This page has four block boundaries and draws a line at none of them, where DSRD 7 §4.3 ruling 1 says every boundary on the site carries one. It was put to him rendered: the same page twice, tabbed, with the line as the only variable. **He ruled the page as it is, with no lines.** It is now a named exception at DSRD 7 §4.3, exception 3, scoped to this page alone, on the ground that each section already opens with the section header's own hairline and a second line ninety pixels away makes the page read as ruled paper. **The boundary is still marked; it is marked by the section header.**

**Two things deliberately not corrected, and named rather than left looking settled:** the tablet and phone sizes in §20.14, which belong to the responsive rule DSRD 7 §3.0 records as still open and Kain's on a render; and the prototypes, which are pre-Mulish and are re-cut under the S311 ruling.

The category hub page is the main landing page for each of the 7 Knowledge Hub categories (e.g. /learn/psychology/). One shared template, populated ×7. Each page surfaces 5 items per content type (1 featured + 4 standard) across 4 content sections (Articles, Book Notes, Quotes, Workbooks), plus a tag browsing strip. Locked prototype: `category-hub-psychology-v9.html`.

**Rise in turn plays on this page's wall and on the kind lists, for all subjects and for each subject, the Quote Articles wall included (Kain, Code's S179 theme sitting, 22 October 2026; shipped 0.707.439; written by Chat, S441).** The cards arrive one after another as they scroll into view, by the shared card's rule. The rule and its record live in DSRD 8 section 41; this line only says the wall carries it.

### 20.0d The light palette, colour only (Kain, Code's S173 theme sitting, 19 October 2026; written by Chat, S431)

**Kain's ruling, in his words.** "Could you just literally copy the exact structural layout of the page, including use of images and everything else? Without changing anything? ... literally just a change in color. That, that's it. No new redesign, don't need anything redesigned." Then, on the rendered page in Safari: "Yes, ship the colour-only Soft Light to all seven category pages." And on the first build, which had added lines, an underline, a fill, a hover, an edge and a shadow: "this needs to be like for like ... you cannot change any design element on this page ... I want the design elements mirrored one hundred percent like for like."

**What changed (theme 0.707.281, corrected at 0.707.282 and 0.707.283).** Every block, size, picture and the tilted Achology bubble of the page in 20.0 and 20.0c are unchanged. Only the dark grounds take the light palette of the article's S162 Soft Light hero (section 22.15): the head band is warm cream, the categories bar white, the topic band warm cream, the learning path's course card warm cream; words and labels move to the dark, the soft grey and the AA-safe orange. The current category's bubble in the bar shows in its own orange (drawn white, it vanished on the white bar). The one text change on cream: the course card's rating star takes the AA-safe orange (it fell to 3.0 on cream; Kain allowed text on the cream to change). Every value is in the build sheet's section "Decided in S173" in the Category Hub Page folder; the approved prototype exported from the live page at 0.707.283 replaces the S154 one, and the folder's README names both.

**How Kain got there.** Four whole directions were rendered on the real Psychology page and opened in Safari: Soft Light with the article's own hero, Article Twin, Gallery White and The Bubble. He chose Soft Light, then ruled it down to colour only. The other three were not chosen.

**Side effect, measured.** The "Categories" label now passes contrast, which clears the page gate's one accessibility failure on this page. The open item in 20.0c that waited on the label's contrast is closed by this.

**Proof.** Every element of the page and its ::before and ::after were compared with the colour block on and off, on all seven pages: the only difference that is not colour is the bubble's filter, white to its own orange.

**The rule for the next page brought to the light palette (Code, from the sitting):** each dark ground to the warm cream, each colour on it to its light counterpart at the same strength, nothing added.

### 20.0e The parts standardised across the subject page and the Articles lists (Kain, Code's S174 theme sitting, 19 October 2026; written by Chat, S433)

**Status.** Kain chose every part below from rendered options on the build site in Safari. The subject page and the eight Articles lists (section 21.0) now share one set of parts, built as shared helpers in the theme (0.707.300 to 0.707.319). Where this section and sections 20.0c or 20.0d differ, this section is the later ruling and wins. Every value and class name is in the build sheet's "Decided in S174" and the approved prototype `PROTOTYPE__Subject_Page_S174_APPROVED` (taken at 0.707.319) in the Category Hub Page folder; its README names it.

- **The line under every subject page's title:** "All articles in this category are centralised on this page, making it easier for you to find your next insightful read."
- **Colour: Warm with a Dark Bar** (Kain chose it from four strategies, then four corrected ones: "I think what we need is a real consistent colour strategy"). Cream for every band and panel; the brand dark Categories bar; white for anything sitting on a band. This replaces 20.0d's white Categories bar and the off-white tried earlier in the sitting (0.707.318). Warm Sand was tried and dropped: "it's not on or part of our design system."
- **The Categories bar's bubble** shows only on the selected category and on hover ("It should only be there on hover, to highlight which category has been selected"), in its own light orange at its S155 strength.
- **The way back (Kain, Code's S176 theme sitting, 20 October 2026, 0.707.371 to 0.707.373; written by Chat, S436).** The Categories bar's own label reads "All Categories" and is a link: on a list it goes to that type's whole list (Articles, Book Notes, Quotes or Workbooks), and on a subject page it goes to the Knowledge Hub front page. It is quiet at rest and orange on hover and where you are, with no bubble. This holds on every Categories bar in the Knowledge Hub, and replaces 20.0's "No All link" and the separate "All" item Kain approved and then revised in the same sitting. Measured by Code in WebKit on ten pages at two widths.
- **The four kind buttons:** one slim line, icon beside word, even room each side (design 4 of four); two by two on tablet and phone.
- **The Editor's Picks:** an aligned list with a hairline between items (design 1 of four), and no reading time in this block.
- **The topics block: Four Doors, Folder presentation.** It replaces the 31-topic block, which Kain found "very, very noisy". After four directions, a map and four presentations: "four doors is phenomenal ... very navigatable", then the Folder presentation: "Very clean, very simple." Its titles and lines are Kain's, quoted in the build sheet. "The topics block is locked in." The four family icons in the S390 brief are not used; the Folder presentation carries none. Recorded as a component in DSRD 8 section 12.7.
- **The bottom section: Snug refined.** Kain kept the same parts and asked for them sharpened ("I'm quite happy keeping what we have in place ... sharpen and neaten this up"), with the review's stars beside the name. Desktop height went from 822 to 721 (0.707.319).

**The page check's open items, settled (Chat, S433, on Code's S174 ASK; Kain may overturn any of them).** Code fixed four items himself: the picks' picture sizes, the page numbers' contrast, the lazy Know Your Psychology card and the two DSRD 6 records' page lines. The seven others:
1. The nine learning path drawings (the mountain and the four step pictures, approved by Kain at S155) are artwork, not interface icons. They join DSRD 7 section 5.2.6's artwork group outside the registry.
2. Short forms inside the Four Doors topic names (CBT, NLP, IQ) are destination titles, and DSRD 6 section 1's card-title paragraph covers them.
3. The picture file `how-irresponsibility-leads-to-personal-disempowerment-v2.webp` loses its version number. That's the factory's job: rename the file and its record.
4. The old address `/achology/knowledge-hub/articles/` gets a permanent redirect to `/learn/articles/` in the redirect map (DSRD 1). That's Code's job, on the Redirect Strategy card.
5. The 40 workbook rows whose sitemap chain breaks wait while the workbooks are held (Kain, S432, newsroom scope decision 7). The check reports them as held, and the factory fixes them when the workbooks resume.
6. The single-size theme pictures (the seven author faces, the course cover, the Know Your Psychology logo) get sized copies and a srcset before launch. That's a Backlog: Code line.
7. The newest article's picture keeps `fetchpriority="high"` and loads first. It is the largest picture above the fold on desktop, which is the page's main view. On a phone it sits below the fold and loads early anyway, which costs one picture. This is a recorded exception in DSRD 6 section 9.

The DiMAP's address under the neuro-linguistic programming school path matches DSRD 1 section 2 (Site Hierarchy) and its section 11 redirect rows, so it is not changed.

### 20.0f The list and subject page header: the words sit to the faces, and the faces warm on hover (Kain, Code's S178 theme sitting, 21 October 2026; written by Chat, S438)

**The words sit to the faces (Option 3; built 0.707.405 and 0.707.406).** Kain asked what the best graphic designer in the world would say was wrong with the header: the words hung at the foot of their column with a dead gap under the breadcrumb, and the words and the faces shared neither a top nor a foot. Of four rendered options photographed on the all-subjects and Psychology Book Notes lists he chose Option 3: the words start one step (48) under the breadcrumb; the four kind buttons stand on the foot of the faces; the space between the paragraph and the buttons takes the difference and never drops below 24. On computer and tablet wherever the words sit beside the faces; on a phone they stack and nothing changes. Held by rule to bands that carry the faces, so All Tags (signed, no faces) and the tag pages (their own header) are unchanged. Reach: the 32 lists and the 7 subject pages, 39 pages, measured in WebKit at 1280, 834 and 390. Recorded as a KAIN'S CHOICE line in BUILD_SHEET__Articles_Listing_S174. Code's file: RULING__List_Header_Words_Option_3_S178, in the channel Archive.

**The faces turn half colour with a touch of warmth on hover, people only, this header only (Option 4; built 0.707.408).** Kain's scope, in his words: "Only the images where the pictures are actual people and only within this type. Or design of hero. That is it." Nothing else is touched: not inside articles, book notes or quote pages, nowhere else on the site, no universal image rule. The look, from four rendered warmth options: "Option 4, please ... At rest is brilliant. Option 4, upon hover, fantastic." At rest the faces stay black and white; on hover, half their real colour with a touch of warmth (about half the warmth of Immanuel Kant's portrait in colour), never full colour. Applies to the faces panel ("The minds you will meet here") on the Book Notes and Quote Articles lists and the subject pages; the Articles and Workbooks lists' header shows article pictures, which keep full colour on hover. Recorded as a KAIN'S CHOICE line in BUILD_SHEET__Articles_Listing_S174. Code's file: RULING__Header_Faces_Warm_On_Hover_Option_4_S178, in the channel Archive.

**The one title size reaches here too (S178):** the subject page and list titles are 33 at every width (section 34.13), retiring the subject page build sheet's recorded departure at 42.

### 20.0g The Book Notes lists' Editor's Picks: the book's name, Read the book note, and rows that share a line count (Kain, Code's S178 theme sitting, 21 October 2026; written by Chat, S440)

**Status.** Two rulings of one sitting, both about the Editor's Picks on the eight Book Notes lists (sections 20.0b and 20.0e). They change nothing on the Articles lists' or the Quote Articles lists' picks. Where this section and 20.0e's "an aligned list with a hairline between items" differ for a Book Notes list, this section is the later ruling and wins.

**The fault, in Kain's words.** The picks' titles "wrap onto three or four lines ... This looks scrappy and creates such a volume of just unattractive white space on the page. We need a solution so that all of these titles are ... ideally three lines long ... across every single book notes page." And, on the book's name alone: "I don't know what I'm going to be clicking through to ... we need some rules for copy ... that will allow us to not surpass three lines of text."

**The pick: the book's name and "Read the book note" (Option 4; built 0.707.411, commit 87752610).** Kain chose from four rendered wording options: "Option 4, please, Claude. That's perfect. Looks absolutely brilliant." The rule as built: each pick shows the book's name only, which is the book note's title before its colon, at most two lines, and then one small orange line, "Read the book note", with an arrow. A pick is never more than three lines. The wording "Read the book note" is Kain's pick from the rendered options, not drafted copy. Checked in WebKit on all eight Book Notes lists at 1280, 834 and 390: every pick is two or three lines, the full spacing check run again on the eight finds nothing new (the four shared faults named in the session stand, untouched), and every wall ends level. Recorded as a KAIN'S CHOICE line in BUILD_SHEET__Articles_Listing_S174.

**The rule: the names in a row take the same number of lines (built 0.707.413, commit d3b0036a, and 0.707.414).** Kain, in his words: "if we were to segment this block as in the top two books and the bottom two books ... The top line must be either both two lines of title or both one line of title. And the same applies to the bottom ... this is about a rule of the books actually get placed there, which must be governed by their title consuming one or two lines on the page ... This is about us minimizing white space. Or dead space. And fundamentally imbalance."

As built: each Book Notes list carries up to eight candidates, newest first. The page measures each name at the reader's own width and shows the newest four that pair, in two rows of two, or in one row of four on a tablet. Without the script, the four newest show, as before. Checked in WebKit at 1280, 834 and 390: seven of the eight lists pair at every width, and the full spacing check run again on the eight finds nothing new, with the walls level.

**Chat's ruling on the question Code left open: do hand-chosen picks have to obey the rule? (Chat's call, S440; Kain may overturn it.)** Yes. The rule exists to remove dead space and imbalance, so how a pick was chosen makes no difference to whether it applies. A Book Notes list's four picks, whether the newest four after the lead or the four chosen by hand under section 20.0b, are shown in rows whose names take the same number of lines. How the theme brings a hand-chosen set to that is a technical choice for Code.

**General Interest cannot obey it yet.** It has only five book notes, so its four candidates cannot be paired by their names. It is the one list of the eight that does not pair, and it fixes itself when more General Interest book notes are published; the fill plan in ASK__Fill_Every_Knowledge_Hub_Grid_171_Pieces_S176 counts it short. Until then it is a known shortfall in the content, not a different design for that list.

### 20.0h One wall for the whole Knowledge Hub, and the quote card family (Kain, Code's S179 theme sitting, 22 October 2026; written by Chat, S442)

Kain asked for every masonry wall in the Knowledge Hub to be standardised before any more polishing: "on the homepage, we've got three columns. On the category pages, we've got four ... we need to standardize as many parts of this entire knowledge hub as we can." Code measured every wall on the build site at 0.707.439 (front page 3, 2, 1 columns; subject pages 4, 3, 2; kind lists 4, 3, 2 with the logo card; topic pages 3, 2, 1; the search results a plain list; two quote card designs; three layout scripts) and proposed this section's wall, 20.0c "The grid", as the one wall. Kain: "This now addresses that problem. Great. Go to work."

**The one wall, on every Knowledge Hub page that carries a wall:**
1. **Columns:** 4 on a computer, 3 on a tablet, 2 on a phone. The front page and the topic pages change to this.
2. **Cards:** a full wall holds 48 (the front page and the subject pages); a paged list 24 a page with page numbers; a topic page 6 of each kind with View all.
3. **Mixing:** the front page and the subject pages mix the kinds; the lists and the topic pages hold one kind per wall.
4. **Spreading:** whichever kind is fewer on that wall is spread evenly so no two of it touch, whichever kind that is (it replaces 20.0c rule 1's assumption that book notes are the fewer; on Mental Wellness articles are).
5. **Quotes on mixed walls:** at most one a row, at most two from any one person, until there are more quote authors.
6. **The Know Your Psychology logo card on every wall:** one at a column foot where there is room, so every wall ends level. The front page gains it. (The search results page is the exception: Kain ruled the logo off it, section 38.9.)
7. **Every card rises in turn and lifts under a pointer** (DSRD 8 section 41).
8. **One piece of code lays out every wall,** not three.

**The quote card is the card itself (Kain, S179).** Kain asked for the quote card family to be designed properly rather than patched ("make all three different types of card look excellent"). Code designed four directions from Kain's signed quote card and showed every design in every shape on one page: 1 The print, 2 The card itself, 3 The mount, 4 The deck. Code recommended 1. Kain: "genuinely like option number two, the card itself ... It's really cutting edge. And looks less tabby." So every quote card on every wall is the signed quote card itself, nothing around it: the cream canvas, the outline quote marks (the closing mark gives way to the reading line), the portrait toned matt orange at 22 per cent, the words in the heading font, the name beneath, the Wise Quotes logo top right beside the words, and "Read This Quote Article" with its arrow at the foot inside the canvas. Three shapes: the wall card and the list card upright, growing with their words; the wide card at the signed 1200 by 630 proportions. The quote page's own card and the downloaded picture are unchanged. Reach: the mixed walls (front page, seven subject pages), the Quote Articles lists (all and per subject), the topic pages' quote walls, and the quote page's Browse More cards. This supersedes rule 3 of 20.0c (the quote tile as the baked picture with a card body under it) once the sweep lands.

**Still open:** whether the search results page stays a plain list in best-match order rather than a wall (Code's recommendation, put to Kain in the sitting; his answer is not in the file). Section 38.9 records the search page as signed with its own two-across list.

**How it lands.** One sweep brief, signed by Kain, builds the one wall and the quote card on every page named; until it lands, no session polishes a wall on its own page. The rule's home for the shared part is DSRD 8 section 41.

**Built at 0.707.498 (Kain, Code's S180 theme session, 25 October 2026; written by Chat, S445).** Shown photographs of the front page, Mental Wellness, the Quote Articles list and the Break Negative Thinking topic page, new beside current, at 1280, 834 and 390, Kain asked "Shall I put the new walls on the website?" and answered: "yes". That is his sign-off of the built wall and of option 2, The card itself, as built. One layout script (kh-subject.js section 3) now lays out every wall marked data-wall, replacing the subject wall's masonry, the Quotes list's Spotlight script and the topic page's copy in kh-tag.js. Every wall runs 4, 3 and 2 columns, and the topic pages move from 3, 2 and 1. The Know Your Psychology logo card stands on every wall but search, one at a column foot; where no column has room, the other columns' cards take up the rest (Kain, S174), from one template, achology_kh_wall_logo_tpl(). The fewer kind on a mixed wall and the quotes (at most one a row) are kept apart; a finished wall that still breaks either rule has the breaking card swap places and is laid again, best of thirty. Every quote card on every wall is achology_kh_quote_card_html(), Kain's signed card itself, upright at least 4 by 5 (withdrawn at S183: the upright card now fits its words, see the quote card rulings below) and wide at 1200 by 630. Measured in WebKit on 76 pages and 381 walls at three widths: before, 347 walls broke the standard; after, in the preview, 375 of 381 meet every rule, with no overlaps, every foot level within 1px and one logo each. Reach: the front page, the seven subject pages, the 32 kind lists, the 36 topic pages and their 144 view-all pages. Not reached, by ruling: the search page (section 38.9) and the quote page's Browse More, which Kain ruled a plain list of titles (section 22.16a). The "Still open" question above is closed by section 38.9's sign-off: the search page stays a plain list. The one wall has landed, so the "How it lands" sentence no longer holds any session back.

**A known limit.** Rule 4, that no two of the fewer kind touch, cannot always be met where the fewer kind is over a third of the wall. Personal Growth (18 book notes of 48) keeps 2 to 7 touching pairs depending on width, Wisdom for Life 3 on a phone, and the front page 1. The wall keeps them as few as it can find. This is recorded as a limit of rule 4, not a fault.

**Still owed by Code:** the fold-back into the Knowledge Hub wall's design folder (prototype and build sheet), and the rulebook's next repeated part (DSRD 8 section 41), proposed to Kain on rendered options.

**Quote cards fit their words, and a quote card is never stretched to level a wall (Kain, Code's S183 theme main session, 26 October 2026; written by Chat, S446).** Kain, on the front page wall: "it's like you have a standardized length for each quote card. So there's literally a gap underneath the quote ... There's like literally dead space inside of the actual quote images." Shown the signed shape and the cards fitting their words as two tabs: "Yes, tab 2. Make the quote cards fit their words on every wall."
1. **The upright quote card fits its words.** No fixed 4 by 5 shape; the S180 record's "upright at least 4 by 5" is withdrawn. The wide card keeps the signed 1200 by 630. The card is otherwise unchanged (cream canvas, mark, toned portrait, words, name, logo, Read This Quote Article at the foot). Live 0.707.557.
2. **A quote card is never stretched to level a wall while another card in its column's run can take the height.** Live 0.707.556; on the front page and the seven subject pages no quote card is stretched at 1280, 834 or 390, and every foot is level within 1 px.
3. **On a wall of quote cards only (the Quotes lists), a card stretched to end the wall level centres its words,** the spare space even above and below (Kain: "yes"). Live 0.707.560, measured equal on every stretched card at 1280, 834 and 390.

### 20.0i The workbook card on the Knowledge Hub walls, and the workbooks lists' lead panel and Editor's Picks (Kain, Code's S466 theme sitting, 9 November 2026; written by Chat, 10 November 2026)

Kain: "I think what we might be better off doing with the workbook cards is just creating them to essentially match book note cards". Shown four whole options in the Change Viewer, he answered "Option 3, Comb Bound". On the build site at 0.707.864 to 0.707.868.

1. **A workbook on a wall is its own card, never the article tile.** It is the signed book note card's shape (DSRD 8 section 6.2: cream shelf #F7F4EF with the floor band from 78%, 16 above and below, the floor shadow, label with icon, title, body padding 16), with one difference, the picture.
2. **The label reads Workbook,** with the workbook icon (file-pen).
3. **The picture is the workbook's featured image, the whole page** (the PDF's page 1, US Letter, 816 by 1056, ratio 0.773), never cropped. It faces the reader, 176 high, with a comb binding down its left edge, on the shelf; corners 2, 4, 4, 2; shadow 0 2px 6px at 28 per cent of the brand dark.
4. **Under the title, the workbook's own one-sentence description** (its excerpt) in the book note's grey description line (Kain, "Option 2, Description"). No word count and no reading time: a workbook has neither (0.707.865).
5. **A title word too long for a phone card breaks** rather than running out of the card (`overflow-wrap:break-word`).
6. **One-off values, annotated in kh-subject.css:** picture height 176; the comb ring drawing 18 by 11, repeated down the edge from 6 below the top to 6 above the foot, overhanging the sheet by 6; a 6 optical nudge so the overhang stays centred on the shelf; corners 2, 4, 4, 2; the shadow above.
7. **The workbooks lists' lead panel takes the Latest Book Note panel's stance** (Kain, "Option 1, Same Stance", 0.707.867): the same dark ground (#1A242B), soft focus (blur 14, saturation .95, opacity .75) and wash, the same turn (rotateY -16, perspective 900), corners 2, 5, 5, 2 and lift shadow (0 22px 44px at 50 per cent black); the page 70 per cent of the panel high to a 320 maximum (240 between 1024 and 1100), 9 per cent from the right; the cover's own picture, blurred, where the bookshelf picture stands; the comb binding drawn for a dark ground down the page's left edge; no word count. On a phone the page sits on top, 220 high, turned 12, the wash darkening downwards.
8. **The workbooks lists' Editor's Picks are their names alone** (Kain, "Option 4, Titles Only", 0.707.868): in full, 16 on 1.4 (the Card Title step), no picture, spread evenly down the cream panel with the list's own hairlines and padding, the panel keeping the lead panel's 440 height. A workbook's page is never cropped to a strip anywhere in the list.

Not changed: the book note card, the article tile, the quote card, `.card--workbook` in cards.css, and every other place a workbook cover is drawn. Source: TO Chat RULING__Workbook_Card_Comb_Bound_On_The_Knowledge_Hub_Walls_S466 and SHIP__Workbook_Card_Comb_Bound_0.707.864_S466, now in the channel Archive.

### 20.1 Page Structure (top to bottom)

1. Sticky header (DSRD 8 §18)
2. Breadcrumb (§20.3)
3. Hero section (§20.4)
4. Category pill strip (§20.5)
5. Articles section — featured LEFT (§20.6, featured card DSRD 8 §6.5)
6. Book Notes section — featured RIGHT (§20.6, featured card **DSRD 8 §6.8**). *(Pointer corrected S313: this read §6.2, which is the standard book note card. §6.8 is the featured book note card, ruled and filed at S261. The same stale pointer was corrected once already at S268 in §22, and it had not been swept here.)*
7. Quotes section — featured LEFT (§20.6, featured card DSRD 8 §6.6)
8. Workbooks section — featured RIGHT (§20.6, featured card DSRD 8 §6.7)
9. Tag browsing strip (§20.8)
10. Rainbow stripe + footer (DSRD 8 §19)

### 20.2 Vertical Rhythm

| Transition | Gap | Value |
|-----------|-----|-------|
| Header bottom to breadcrumb | 48px | var(--sp-2xl) |
| Breadcrumb to 'Category' overline | 12px | Hero padding-top |
| 'Category' overline to H1 | 4px | Tight label-title pair |
| H1 to counts subtitle | 10px | Supplementary data |
| Counts subtitle to intro copy | 16px | var(--sp-md) |
| Intro copy to category pills | 24px | var(--sp-lg) |
| Category pills to the first section | **48px, no line (Kain, S313)** | DSRD 7 §4.3, exception 3 |
| Section to section | **48px, no line (Kain, S313)** | DSRD 7 §4.3, exception 3 |
| Section header to card grid | 20px | Below the section header's own hairline, which is inside the DSRD 8 §23 component and keeps its own values under §4.3's carve-out |
| Last section to footer | 64px | var(--sp-3xl) |

**The boundaries carry no hairline, and that is Kain's ruling rather than an omission (S313).** It was put to him on two whole rendered pages, tabbed, with the line as the only variable, and he took the page without lines. **Each section already opens with the section header's own rule**, so a separator as well puts two lines within about ninety pixels of each other and the page reads as ruled paper. It is registered at DSRD 7 §4.3 as exception 3 and scoped to this page alone; the gate reports it as a named carve-out, never a silent pass.

**One row did change: the pills-to-first-section gap was 40px**, which is not a value on the 8px spacing scale at all. It becomes 48, the page's own dominant rhythm, with no line.

*Hero internal spacing keeps its asymmetric 4/10/16px progression, untouched: those are gaps inside one block, not boundaries between two, and §4.3 does not reach them.*

### 20.3 Breadcrumb Component

- **Format:** `Home` icon `ChevronRight` Learn `ChevronRight` [Category Name]. *(Corrected S378: this read "Home icon, Home, Learn". The house icon is the Home link and no word follows it; the trail was signed as built by Kain at S090, DSRD 8 §25.)*
- **Home icon:** Lucide `Home`, 13px, mid grey (#8A9199), inline with first breadcrumb segment (DSRD 7 §5.2)
- **Separator:** Lucide `ChevronRight`, mid grey (#8A9199). Replaces ' > ' text character for cross-browser consistency (DSRD 7 §5.2).
- **Font:** Mulish, the 12 step, 400 (Caption style, per DSRD 7 §3.2). *(Corrected S313 from 13px, which is not a step; the approved S056 override maps 13 to 12.)*
- **Colour:** **Soft grey #5E6B75 on the links, mid grey #8A9199 on the separators.** Current page (category name) is brand dark (#354149), not linked. *(Corrected S313: the 2026-07-13 contrast audit moved every breadcrumb link site-wide to soft grey because a link is text a reader reads, and left the separators on mid grey because they carry no meaning. This row still read mid grey throughout.)*
- **Links:** 'Home' links to `/`, 'Learn' links to `/learn/`
- **Spacing:** 48px below header bottom edge (var(--sp-2xl))

*Provides a visual anchor at the start of the breadcrumb trail. Same 13px size as stats icons on cards — consistent icon scale across the design system.*

### 20.4 Hero Section

**Layout:** White background, left-aligned text. No search bar in the hero (category hubs are browsing pages, not search pages; the site search stays reachable from the header on every page, DSRD 1 §7.4, S366).

**Overline:**

| Property | Value |
|----------|-------|
| Text | 'Category' |
| Font | Como 11px/600 |
| Transform | Uppercase |
| Letter-spacing | 0.08em |
| Colour | Mid grey (#8A9199) |

**H1 (Category Name):**

| Property | Value |
|----------|-------|
| Font | Como, the 33 step, 700 (H1 Page Title, per DSRD 7 §3.1). *(Corrected S313 from 32px, which is not a step; the same correction §22.4's H1 took at S302 and §21.2's took this session.)* |
| Colour | Brand orange (#ED6922) |
| Line-height | 1.2 |

*Orange H1 ties visually to the active category pill below (D11). Strong wayfinding signal — the visitor immediately knows which category they're in.*

**Counts Subtitle:**

| Property | Value |
|----------|-------|
| Font | Mulish 14px/400 |
| Colour | **Soft grey (#5E6B75).** *(Corrected S313 from mid grey: these counts are links a reader reads and clicks, and DSRD 7 §1.1 forbids mid grey for anything a reader needs. Same correction as §21.2's count line.)* |
| Content | '[X] Articles · [X] Book Notes · [X] Quotes · [X] Workbooks' |
| Links | Each count links to its content type listing page (e.g. /learn/psychology/articles/) |

*Counts appear at two levels: hero subtitle (all 4 content types at a glance) and section headers (individual counts where they matter). Making hero counts clickable adds utility with zero visual cost (D15, D16).*

**Intro Copy:**

| Property | Value |
|----------|-------|
| Font | Mulish, the 16 step, 400. *(Corrected S313 from 17px per the approved S056 override, which maps 17 to 16.)* |
| Colour | Brand dark (#354149) |
| Line-height | 1.6 |
| Max-width | 880px |

*880px max-width ensures 3-sentence intros consistently land at ~4 lines on desktop. All 7 category intros confirmed at 60–70 words for uniform hero height across category hubs. See §20.9 for confirmed copy.*

**Hero spacing (D17):**

| Transition | Gap |
|-----------|-----|
| Overline to H1 | 4px |
| H1 to counts subtitle | 10px |
| Counts subtitle to intro copy | 16px |

*Asymmetric 4/10/16 rhythm — each gap noticeably wider than the last.*

### 20.5 Category Pill Strip

Horizontal row of 7 pills, one per Knowledge Hub category. Provides direct category-to-category navigation below the hero.

| Property | Value |
|----------|-------|
| Layout | Horizontal flex, gap 8px, wraps on mobile |
| Active pill | Brand orange (#ED6922) background, white text |
| Inactive pills | Off-white (#F3F4F4) background, brand dark (#354149) text |
| Hover (inactive) | Background shifts to brand orange at 10% opacity |
| Font | Como, the 12 step, 500. *(Corrected S313 from 13px, which is not a step.)* |
| Padding | 8px 16px |
| Border-radius | 20px |
| Links | Each pill links to /learn/{category}/ |

*Category pills solve a gap the mega menu does not: the Knowledge Hub dropdown has content-type tiles (Articles, Book Notes, etc.) but no category links. Pills give visitors direct category-to-category access without returning to the mega menu (D3).*

### 20.6 Content Type Sections

Four sections, each with an icon-led section header (§20.7) and a grid of 5 cards (1 featured + 4 standard).

**Grid Pattern (D9):**

- 5 items per section: 1 featured (2-column span) + 4 standard (1-column each)
- Grid: 3 columns desktop, 2 tablet, 1 mobile. Gap 24px.
- Row 1: featured card + 1 standard card. Row 2: 3 standard cards.
- Featured cards alternate left/right down the page (zigzag):

| Section | Featured Position | Featured Card Type |
|---------|------------------|-------------------|
| Articles | LEFT (columns 1–2) | Featured article card (DSRD 8 §6.5) |
| Book Notes | RIGHT (columns 2–3) | Book note horizontal layout (DSRD 8 §6.2) |
| Quotes | LEFT (columns 1–2) | Featured quote card (DSRD 8 §6.6) |
| Workbooks | RIGHT (columns 2–3) | Featured workbook CTA card (DSRD 8 §6.7) |

*Zigzag alternation prevents four identical grids and creates visual movement down the page. Each featured card reflects its content type personality: editorial horizontal (articles), cover-led horizontal (book notes), elevated typography (quotes), dark CTA (workbooks) (D9, D10).*

**Standard cards** use the corresponding DSRD 8 §6 card design: article card (DSRD 8 §6.1), book note card vertical (DSRD 8 §6.2), quote card (DSRD 8 §6.3), workbook card (DSRD 8 §6.4).

**Content ordering:** Newest first — permanent rule (DSRD 7 §17.3). Featured card is always the most recently published item in that content type for the current category.

### 20.7 Section Header Component

Reusable component used above each content type grid and the tag browsing strip on category hub pages.

**Layout:** Horizontal flex, items centred vertically. Icon + title group on left, 'View all →' CTA on right.

**Icon Container:**

| Property | Value |
|----------|-------|
| Size | 36px × 36px |
| Background | `rgba(237,105,34,0.07)` (brand orange at 7% opacity) |
| Border-radius | 10px |
| Icon | 18px SVG, outline stroke, brand orange (#ED6922), centred |

**One page departs from that box, and only above the phone: the article page (Kain, at Code's S082, on a screenshot).** His words: the header was completely disjointed, and the top of the top line of text and the bottom of the bottom line must align within the icon box sitting before it. **A 36px box against a 50.6px two-line text block cannot align by any placement**, so on that page the box is stretched to the row's own height, its width written as the same sum, 50.65, with a **24px** mark inside it.

**Above the phone only**, because below it the supporting line wraps further and a square box would reach 90px. **Scoped to the article page**, so the same header on the category hubs and the listing pages still carries the 36px box. Whether the site-wide pattern follows belongs to the section header component's own sitting, and is not decided here.

**Section Icons (see DSRD 7 §5.2 Icon Registry for canonical Lucide names):**

| Section | Lucide Icon |
|---------|-------------|
| Articles | `Newspaper` |
| Book Notes | `NotebookPen` |
| Quotes | `Quote` |
| Workbooks | `FilePen` |
| Tags | `Tags` |

**Title:**

| Property | Value |
|----------|-------|
| Font | Como 22px/600 (section header custom size) |
| Colour | Brand dark (#354149) |
| Count | In parentheses after title. Mulish 14px/400, mid grey (#8A9199). E.g. 'Articles (142)' |

**Subtext:**

| Property | Value |
|----------|-------|
| Font | Mulish 14px/400 |
| Colour | Mid grey (#8A9199) |
| Gap | 2px below title |

*Subtext is category-specific and content-type-specific — 28 unique lines total (7 categories × 4 content types). See §20.10 for confirmed copy.*

**View All CTA:**

| Property | Value |
|----------|-------|
| Font | Como 14px/600 |
| Colour | Brand orange (#ED6922) |
| Format | 'View all [Content Type]' + Lucide `ArrowRight` (DSRD 7 §5.2) |
| Hover | Arrow nudges right 3px (per DSRD 7 §5.1 ghost button) |
| Position | Right-aligned, vertically centred with title |

**Hairline:**

| Property | Value |
|----------|-------|
| Border | 1px solid #EEEDED |
| Position | Below section header |
| Padding-bottom | 16px (above hairline) |
| Grid gap below | 20px (hairline to first card) |

### 20.8 Tag Browsing Strip

Follows the four content type sections. Uses the same section header component (§20.7) with the Tags icon.

**Section header copy:**
- Section title: "Explore by Topic"
- Section subtext: "Browse related topics across the Knowledge Hub"

| Property | Value |
|----------|-------|
| Tags per category | Psychology 12; every other category 8–10 — the count that wraps the strip to two clean rows on desktop |
| Layout | Wrapping flex row, gap 8px |
| Pill font | Como, the 12 step, 500. *(Corrected S313 from 13px, which is not a step.)* |
| Pill padding | 8px 16px |
| Pill border-radius | 20px |
| Pill background | White |
| Pill border | 1px solid #EEEDED (light grey at rest) |
| Pill text | Brand dark (#354149) |
| Pill hover | Border-colour switches to brand orange (#ED6922). Background remains white. |
| Links | Each pill links to /learn/tags/{tag-slug}/ |

*Tags are drawn from the confirmed 36-tag taxonomy (DSRD 1 §5). Psychology's twelve are 10 outcome/problem + 2 content attribute, and every category carries exactly two content-attribute tags (D5, D18). The seven confirmed strips are DSRD 2 §1.3.3's.*

### 20.9 Confirmed Hero Intros (7 Categories)

All 7 category hero intro texts are 3 sentences each, ~60–70 words. Consistent length ensures uniform hero height across all category hubs.

**Psychology:**

Psychology explores how people think, feel, behave, and make sense of the world around them. The articles, book notes, quotes, and workbooks in this category unpack the ideas, patterns, and principles that shape human experience. From classic psychological theories to practical everyday insight, this collection is here to help you better understand yourself, other people, and what it means to be human.

**Helping People:**

Helping people well calls for empathy, good judgment, practical people skills, and an understanding of what others genuinely need in life. The articles, book notes, quotes, and workbooks in this category explore the principles and practices that support human development. From communication and connection to coaching and mentoring, this collection is here to help you become more effective with people.

**Mental Wellness:**

Mental wellness comes from fortifying your inner world with honesty, humility, and greater self-awareness. The articles, book notes, quotes, and workbooks in this category explore the habits, perspectives, and practices that support emotional balance and resilience. From managing stress to building stronger mental foundations, this collection is here to help you care for yourself wisely and live with greater stability.

**Motivation:**

Motivation is about understanding what drives action, sustains effort, and keeps people moving forward with purpose. The articles, book notes, quotes, and workbooks in this category explore the mindset, discipline, and clarity that support meaningful progress. From overcoming inertia to staying focused on what matters, this collection is here to help you build momentum and follow through with intention.

**Personal Growth:**

Personal growth begins with self-awareness and deepens through reflection, wise choices, and consistent action over time. The articles, book notes, quotes, and workbooks in this category explore the attitudes, habits, and inner disciplines that support lasting personal development. From building confidence to growing in maturity and clarity, this collection will help you become more intentional in how you live.

**General Interest:**

General Interest brings together ideas and resources that support Achology's wider purpose of helping people live wise and autonomous lives. The articles, book notes, quotes, and workbooks in this category explore themes that do not fit into any one single category. From thought-provoking perspectives to enlightening philosophical ideas, this collection is here to help you reflect deeply and learn broadly.

**Wisdom for Life:**

Wisdom for Life explores the timeless principles that help people think clearly, live responsibly, and respond well to life. The articles, book notes, quotes, and workbooks in this category gather insights that support better judgment, perspective, and self-knowledge. From everyday challenges to deeper questions of meaning, this collection is here to help you live with greater awareness, maturity, and good sense.

### 20.10 Confirmed Section Subtexts (28 Lines)

One line per content type per category. These sit below the section heading in each content type block (§20.7).

| Category | Section | Subtext |
|----------|---------|---------|
| Psychology | Articles | Clear, thoughtful articles on psychological ideas and the forces that shape human experience. |
| Psychology | Book Notes | Useful notes from psychology books on how the mind, behaviour, and human nature really work. |
| Psychology | Quotes | Timeless psychology-based quotes on thought, emotion, behaviour, identity, and human nature. |
| Psychology | Workbooks | Practical workbooks for exploring psychological ideas and applying them in your everyday life. |
| Helping People | Articles | Grounded articles on relationships, communication, and the people skills for supporting others. |
| Helping People | Book Notes | Useful notes from books on building influential relationships, earning trust, and helping people. |
| Helping People | Quotes | Thought-provoking quotes on helping others with empathy, wisdom, presence, and awareness. |
| Helping People | Workbooks | Practical exercises for bolstering how you coach, mentor, or respond to other people's needs. |
| Mental Wellness | Articles | Thought-provoking articles on emotional well-being and habits that support a calmer inner life. |
| Mental Wellness | Book Notes | Enlightening notes from mental wellness books on resilience, self-care, and emotional balance. |
| Mental Wellness | Quotes | Encouraging quotes on self-knowledge, awareness, emotional IQ, and finding inner balance. |
| Mental Wellness | Workbooks | Practical exercises for building inner-resilience, self-awareness, and healthier mental habits. |
| Motivation | Articles | Enlightening articles on what drives action, builds momentum, and keeps purpose alive daily. |
| Motivation | Book Notes | Useful notes from motivational books on purpose, discipline, consistency, and follow-through. |
| Motivation | Quotes | Thought-provoking quotes on purpose, effort, persistence, and staying the course with resolve. |
| Motivation | Workbooks | Practical exercises for clarifying your priorities, strengthening self-discipline, and taking action. |
| Personal Growth | Articles | Insightful articles on self-awareness and the self-disciplines that enable lasting inner growth. |
| Personal Growth | Book Notes | Useful notes from personal growth books on character, confidence, and living with intention. |
| Personal Growth | Quotes | Reflective quotes on self-knowledge, wiser choices, and growing through life with intention. |
| Personal Growth | Workbooks | Practical workbooks to help you self-reflect honestly, choose wisely, and grow sustainably. |
| General Interest | Articles | Wider-ranging articles on ideas that support wiser living, deeper reflection, and perspective. |
| General Interest | Book Notes | Useful insights from books that offer fresh perspectives, insight, and much to think about. |
| General Interest | Quotes | Thought-provoking quotes on life's meaning, perspective, and the art of living life reflectively. |
| General Interest | Workbooks | Practical exercises for encouraging deep self-reflection and engaging with life's big ideas. |
| Wisdom for Life | Articles | Thoughtful articles on living wisely and meeting life with maturity, integrity, and perspective. |
| Wisdom for Life | Book Notes | Enlightening notes from books on meaning, character, discernment, and the art of living well. |
| Wisdom for Life | Quotes | Timeless quotes on wisdom, perspective, self-awareness, and living in a fully responsible way. |
| Wisdom for Life | Workbooks | Practical exercises for applying practical life principles and wisdom to life's everyday decisions. |

### 20.11 Decision Register (18 Decisions)

*A log, not the specification: this register records what was decided for this page and when. The operative spec is the section body above — where the two differ, the body governs.*

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Hero: white background, left-aligned, no search bar | No hero search bar; the header search serves every page (DSRD 1 §7.4, S366). Category hubs are browsing pages, not search pages. |
| D2 | Section headings: plain content type names with subtext for all 4 sections | Unified rhythm across all sections. 28 lines of subtext copy confirmed in-session. |
| D3 | Category cross-navigation: horizontal pill strip below hero | Mega menu has content-type tiles, not category links. Pills give direct category-to-category access. |
| D4 | Workbooks section: featured CTA card (2-col span) for free workbook + standard cards | Keeps section rhythm consistent while giving email capture the prominence it needs. |
| D5 | Tag browsing strip: wrapping pill row, 8–12 per category, editorially curated | Tags already locked in DSRD 1 SS5. No new planning needed. Visual treatment resolved in prototype. |
| D6 | Content ordering: newest first (PERMANENT). Popularity metric KILLED. | Primary discovery is Google, LLM citations, and tag/category URLs. Popularity metric adds complexity with negligible benefit. |
| D7 | Listing page sort: Newest (default) + A-Z as secondary option | Cheap to build, useful for visitors looking for a specific title. |
| D8 | Vertical rhythm: 48px section-to-section, 40px pills-to-first-section, 20px subtext-to-grid | Spacious-over-busy. 48px is the dominant rhythm. Hero internal spacing tighter (4/10/16px asymmetric). |
| D9 | Alternating featured cards: Articles LEFT, Book Notes RIGHT, Quotes LEFT, Workbooks RIGHT | Zigzag prevents four identical grids. Each featured card reflects its content type personality. |
| D10 | Featured card treatments: article=horizontal editorial, book note=§6.2 horizontal, quote=wider+22px, workbook=dark CTA | Each content type has its own visual personality at the featured level, not just a bigger version of the same card. |
| D11 | Hero overline 'Category' in mid grey, H1 category name in brand orange | Strong wayfinding signal. Orange ties visually to the active category pill below. |
| D12 | Hero intro max-width expanded from 720px to 880px | Ensures 3-sentence intros consistently land at ~4 lines on desktop. |
| D13 | Home icon added to breadcrumbs (13px house outline, mid grey) | Visual anchor at start of breadcrumb trail. |
| D14 | Icon-led section headers with 36px tinted container, title+count+subtext grouped, hairline below | Creates editorial structure. Each content type has a distinct icon. Counts in parentheses after title. |
| D15 | Counts appear at two levels: hero subtitle (all 4) + section headers (individual) | Hero gives scale at a glance. Section headers give specifics where they matter. |
| D16 | Hero subtitle counts are clickable links to listing pages | The data is already there — making it clickable adds utility with zero visual cost. |
| D17 | Hero spacing: overline-to-H1 4px, H1-to-subtitle 10px, subtitle-to-intro 16px | Asymmetric rhythm (4/10/16) reinforces hierarchy. Each gap noticeably wider than the last. |
| D18 | Psychology tag strip: 12 tags (10 outcome/problem + 2 content attribute) | Broadest category gets the most tags. Wraps to clean two rows on desktop. |

### 20.12 Confirmed Search Descriptions and Page Titles (7 Subjects; Kain, S381)

The meta description of each subject page, written by Kain at S381 on Chat's drafts from the §20.9 intros. Each is under 155 characters and opens on the subject's name or its keyword. Set in Rank Math's own description field on each `kh_category` term, never in the WordPress term description (the theme reads that as a fallback intro). Workbooks are left out until the first workbook publishes; add them then.

| Subject | Search description |
|---|---|
| Psychology | Psychology articles, book notes and quotes on how people think, feel and behave, from classic theories to practical insight into human behaviour. |
| Helping People | Enlightening articles, book notes and quotes on the topic of helping people, communication, coaching, mentoring, and positively influencing others. |
| Mental Wellness | Mental wellness articles, book notes and quotes on self-awareness, managing stress and building resilience, so you can develop yourself wisely. |
| Motivation | Motivation articles, book notes and quotes on what drives action, how to overcome inertia, stay focused, and how to follow through with intention. |
| Personal Growth | Personal growth articles, book notes and quotes on self-awareness, confidence, maturity and the habits that help you live life more effectively. |
| General Interest | General interest articles, book notes and quotes on the big ideas that fit no single category, from thought-provoking perspectives to philosophy. |
| Wisdom for Life | Wisdom for life: articles, book notes and quotes on thinking objectively, living responsibly and meeting life's everyday challenges with good sense. |

**The seven page titles (Kain, S381, on Chat's drafts: "Yes, they are perfect!").** Set in Rank Math's SEO title field on each `kh_category` term, replacing the default "%term% Archives". Each opens on the subject's name and stays under 60 characters with " | Achology" added.

| Subject | Page title |
|---|---|
| Psychology | Psychology: How People Think, Feel and Behave |
| Helping People | Helping People: Coaching and Communication |
| Mental Wellness | Mental Wellness: Managing Stress and Resilience |
| Motivation | Motivation: Why We Act and How to Follow Through |
| Personal Growth | Personal Growth: Confidence and Better Habits |
| General Interest | General Interest: Big Ideas Worth Thinking About |
| Wisdom for Life | Wisdom for Life: Think Clearly, Live Responsibly |

**The seven focus keywords (Kain, S431, on Chat's recommendation).** Each page's focus keyword is its own subject name, in lower case, set in Rank Math's focus keyword field on each `kh_category` term. Each title and description above already opens on that name, so every placement check passes without changing the approved words. All seven are claimed in the keyword register (content type subject-page, address `/learn/{slug}/`, 19 October 2026, S431). Kain knows general interest and wisdom for life are weak as search terms and ruled them anyway: the pages exist for navigation.

| Subject | Focus keyword |
|---|---|
| Psychology | psychology |
| Helping People | helping people |
| Mental Wellness | mental wellness |
| Motivation | motivation |
| Personal Growth | personal growth |
| General Interest | general interest |
| Wisdom for Life | wisdom for life |

**Set on the install (S431).** None of the seven titles or keywords had been set when Code read the install at S173; the titles fell back to "%term% Archives". Chat sends all three fields to Code's theme session in one RULING at S431; Code sets them and re-runs the DSRD 6 record.

### 20.13 Prototype Reference Files

Desktop prototype: `category-hub-psychology-v9.html` — ninth iteration, locked at V9. Single portable HTML file with Como fonts (all 8 weights via base64 injection), CSS-only image placeholders, all spacing values matching this specification. Psychology category used as the reference implementation. No external dependencies except Google Fonts (Mulish; the prototype is re-cut against the S085 body face under the S311 ruling).

Responsive prototype: `category-hub-responsive-review.html`. Full three-breakpoint design locked. Covers all phone and tablet behaviour specified in §20.14. Lightweight version: `category-hub-responsive-review-lightweight.html`.

### 20.14 Phone and Tablet Responsive Behaviour (LOCKED)

Three breakpoints per DSRD 7 §4.1: mobile (<768px), tablet (768–1023px), desktop (≥1024px).

**Page container padding**

| Breakpoint | Padding |
|-----------|---------|
| Desktop (≥1024px) | 0 48px |
| Tablet (768–1023px) | 0 32px |
| Mobile (<768px) | 0 20px |

**Hero section**

| Element | Tablet | Mobile |
|---------|--------|--------|
| H1 (category name) | 28px | 26px |
| Intro copy | 16px | 15px, max-width 100% |
| Counts subtitle | 14px | 13px |

**Category pill strip**

Wraps to multiple rows at all narrow widths. No horizontal scroll. Gap 8px maintained.

**Section header**

At desktop and tablet: title group left, "View all →" CTA right — inline on the same row.
At mobile (<768px): "View all →" CTA drops to a new row below the title group, indented 48px to align with title text (past icon + gap).

**Card grid collapse**

| Breakpoint | Columns |
|-----------|---------|
| Desktop (≥1024px) | 3 columns |
| Tablet (768–1023px) | 2 columns |
| Mobile (<768px) | 1 column |

**Featured cards (spanning behaviour)**

At desktop: featured card explicitly placed at columns 1–2 (LEFT) or 2–3 (RIGHT). Standard card fills the remaining column.

At tablet (2-column grid): featured card spans both columns (full width). Standard card from row 1 drops to row 2 and pairs with the next standard card. Featured-RIGHT cards use CSS `order: -1` to pull to the top of the grid.

At mobile (1-column grid): all cards full width, stacked vertically. Featured cards appear first in source order or via `order: -1` on RIGHT-positioned featured cards.

**Featured article card (§6.5) — horizontal collapse**

At tablet: stays horizontal (image left, content right). Image width reduces to 38%.
At mobile: flips to vertical (image top 200px, content below). Image fills full width.

**Featured book note card (§6.2 horizontal) — horizontal collapse**

At tablet: stays horizontal. Cover panel width reduces to 36%.
At mobile: flips to vertical (cover panel top 200px, content below).

**Featured workbook CTA card (§6.7) — horizontal collapse**

At tablet: stays horizontal. Image area width reduces to 36%.
At mobile: flips to vertical (image area top 180px, content below).

**Featured quote card (§6.6) — no horizontal element**

Vertical at all breakpoints. Simply spans full width at tablet and mobile.

**Tag browsing strip**

Wraps naturally at all breakpoints — no horizontal scroll. Same 8px gap maintained.

*Production implementation notes for this component/page are in the Production Implementation Notes document.*

---

## 21. Knowledge Hub Listing Page Layout (LOCKED S220; RE-CHECKED AGAINST THE CURRENT FOUNDATIONS, S313)

Single shared template covering 32 pages: 28 category-specific (7 categories × 4 content types, URL pattern `/learn/{category}/{content-type}/`) and 4 cross-category (URL pattern `/learn/{content-type}/`). Confirmed at prototype V10.

**Why this section was re-checked and what it means.** It was locked before four things the site now runs on: the nine-step type scale (DSRD 7 §3.0, Kain S056), the hairline block-separator standard (DSRD 7 §4.3, Kain S224), the supporting-line grey ruling (S280), and the body face (Kain, Code S085). **Locked is not the same as current.** Every correction below is conformance to a standard Kain has already ruled, taken on the same ground as the S280 pass: no new visual choice was made here, and none was his to make twice. The corrections are made in the section body, which is where this document's own note at §21.10 says the operative specification lives.

**Three things are deliberately NOT corrected here, and each is named rather than silently left.** The tablet and phone type sizes below sit off the nine-step scale, and **the responsive rule is one of the two type rulings still open** (DSRD 7 §3.0): re-deriving them here would be taking a decision that is Kain's on a render. The prototype is pre-Mulish and is re-cut under the S311 ruling. And nothing in this section has been seen rendered since these corrections, so it goes to Kain's eye in Safari before it is called done.

### 21.0 The S174 redesign of the Articles and Book Notes lists (Kain, Code's S174 theme sitting, 19 October 2026; written by Chat, S433)

**Status.** Sections 21.1 to 21.7 below are superseded for the eight Articles lists, the eight Book Notes lists and, since the S175 and S176 sittings, the eight Quotes lists, and are kept as the record. The Workbooks lists and the per-book lists still follow them until Kain sees them.

**The Articles lists take the subject page's parts (0.707.284 to 0.707.317).** Kain, on the old list: "This is not a design that I've approved ... apply the same level of design effort to this articles page as what you have done to the categories page ... give me four options." He chose option A of four, Category Twin, built on the real page. The eight lists (`/learn/articles/` and the seven `/learn/{subject}/articles/`) draw, in order: the band with the seven subjects, the Categories bar, the latest article with The Editor's Picks, the search plate with Newest and A to Z, the wall, the Four Doors topics block and the learning path. They share the parts and colour of section 20.0e. Build instruction: `PROTOTYPE__Articles_Listing_S174_APPROVED` (0.707.317) and `BUILD_SHEET__Articles_Listing_S174` in the Listing Page folder.

**Words on the Articles lists (Kain's).** The all-subjects line: "All of Achology's reads are centralised on this one hub page, making it easier to find your next insightful read." The seven subject lines are his text, word for word, in `achology_kh_section_subtexts` (quoted in the build sheet). The orange line reads "Knowledge Hub", and the lines under the title say "reads" where the title already says Articles. His rule for the title: "when the category name is more than just one word, lose the word articles in the title ... it's already in the breadcrumbs." So Helping People, Mental Wellness, Personal Growth, General Interest and Wisdom for Life show the subject name alone, and their lines say "articles".

**The Book Notes lists (0.707.333, corrected at 0.707.334).** Kain chose each part from rendered options:
- **The lead:** the newest book note's cover in front of the bookshelf picture, softly focused under a dark wash (option 4 of four).
- **The band panel:** "The minds you will meet here", the authors' faces as on the subject page, in place of Browse by Subject. A subject's list fills to seven faces from the other subjects.
- **Beside the lead:** The Editor's Picks, four covers two by two, each cover whole, title beneath (option B). Chosen by hand, as section 20.0b says.

**Search titles and descriptions (Kain, S433: "Yes, that's the shape. Do all eight." and "Yes, switch all eight to Where Can I Find.").** Each list is a collection of articles, so its title asks the question the page answers: where to find good articles on its subject. People search for this almost word for word ("where to find psychology articles", AnswerSocrates, Google Suggest, US, 19 October 2026). Each description answers it at once: right here. Each title opens on its focus keyword, then asks the question in the searcher's own words: "{Subject} Articles: Where Can I Find Good Ones?" (Kain, S433: "Yes, switch all eight to the keyword-first pattern"). Nobody types "where can you find", and the keyword first passes Rank Math's keyword-at-the-start check. Titles are 48 to 56 characters (448 to 531 pixels, under Yoast's 600) and descriptions 131 to 142, each answering both halves of the title: where (right here, every one) and good (our editor's picks of the best) (Kain, S433: "Yes, use these eight descriptions and send them to Code"). The title is set in full with no site name added, because the site name already shows above every Google result. These replace "Articles Archive" on all eight. How Kain got there: he turned down subject-plus-promise titles, one standard line for all eight, and topic questions, because each one described the subject rather than what the page is.

| List | Address | Search title | Search description |
|---|---|---|---|
| All subjects | `/learn/articles/` | Applied Psychology Articles: Where Can I Find Good Ones? | Right here. Every article Achology publishes, across seven subjects from motivation to mental wellness, with our editor's picks of the best. |
| Psychology | `/learn/psychology/articles/` | Psychology Articles: Where Can I Find Good Ones? | Right here. Every psychology article Achology publishes, on how people think, feel and behave, with our editor's picks of the best. |
| Helping People | `/learn/helping-people/articles/` | Helping People Articles: Where Can I Find Good Ones? | Right here. Every Achology article on helping people, on communication, coaching and mentoring, with our editor's picks of the best. |
| Mental Wellness | `/learn/mental-wellness/articles/` | Mental Wellness Articles: Where Can I Find Good Ones? | Right here. Every mental wellness article Achology publishes, on self-awareness and emotional health, with our editor's picks of the best. |
| Motivation | `/learn/motivation/articles/` | Motivation Articles: Where Can I Find Good Ones? | Right here. Every motivation article Achology publishes, on what drives people to act and follow through, with our editor's picks of the best. |
| Personal Growth | `/learn/personal-growth/articles/` | Personal Growth Articles: Where Can I Find Good Ones? | Right here. Every personal growth article Achology publishes, on self-awareness, confidence and maturity, with our editor's picks of the best. |
| General Interest | `/learn/general-interest/articles/` | General Interest Articles: Where Can I Find Good Ones? | Right here. Every general interest article Achology publishes, on big ideas, perspectives and philosophy, with our editor's picks of the best. |
| Wisdom for Life | `/learn/wisdom-for-life/articles/` | Wisdom for Life Articles: Where Can I Find Good Ones? | Right here. Every wisdom for life article Achology publishes, on thinking clearly and living responsibly, with our editor's picks of the best. |

**Set on the build site at 0.707.499 (Code's S180 theme session, 25 October 2026; written by Chat, S445).** The eight titles and descriptions in the table above are set word for word on each list's first page, through the Rank Math filters as the front page's are, with no site name or separator added. Code read all eight back from the served pages and they match. The focus keyword is not set, because these lists are theme routes with no post, so Rank Math has no field to hold one (DSRD 7 section 4.3, Exception 11). Still owed from the S433 ruling: the redirect, the sized pictures and the book note picks field (theme), and the picture rename and the accent (factory).

**Search titles and descriptions for the eight Quotes lists and the eight Book Notes lists (Kain, S448, 27 October 2026: "yes", on the full table shown in Chat).** The same shape as the eight Articles lists above: the subject first, then the searcher's question, answered at once in the description ("Right here"), with no site name added. The Book Notes lists say "Book Summaries" because that is the phrase people search for. All sixteen replace "Quotes Archive" and "Book Notes Archive". Set word for word through the Rank Math filters on each list's first page, as the Articles lists are; no focus keyword, since these are theme routes with no post (DSRD 7 section 4.3, Exception 11).

| List | Address | Search title | Search description |
|---|---|---|---|
| Quotes, All subjects | `/learn/quotes/` | Applied Psychology Quotes: Where Can I Find Good Ones? | Right here. Every quote Achology publishes across seven subjects, each with a written response on what it means, and our editor's picks of the best. |
| Quotes, Psychology | `/learn/psychology/quotes/` | Psychology Quotes: Where Can I Find Good Ones? | Right here. Every psychology quote Achology publishes, each with a written response on how people think, feel and behave, and our editor's picks. |
| Quotes, Helping People | `/learn/helping-people/quotes/` | Helping People Quotes: Where Can I Find Good Ones? | Right here. Every Achology quote on helping people, each with a written response on listening, coaching and mentoring, and our editor's picks. |
| Quotes, Mental Wellness | `/learn/mental-wellness/quotes/` | Mental Wellness Quotes: Where Can I Find Good Ones? | Right here. Every mental wellness quote Achology publishes, each with a written response on stress, resilience and self-awareness, and our editor's picks. |
| Quotes, Motivation | `/learn/motivation/quotes/` | Motivation Quotes: Where Can I Find Good Ones? | Right here. Every motivation quote Achology publishes, each with a written response on what drives action and follow-through, and our editor's picks. |
| Quotes, Personal Growth | `/learn/personal-growth/quotes/` | Personal Growth Quotes: Where Can I Find Good Ones? | Right here. Every personal growth quote Achology publishes, each with a written response on confidence, maturity and better habits, and our editor's picks. |
| Quotes, General Interest | `/learn/general-interest/quotes/` | General Interest Quotes: Where Can I Find Good Ones? | Right here. Every general interest quote Achology publishes, each with a written response on big ideas and philosophy, and our editor's picks of the best. |
| Quotes, Wisdom for Life | `/learn/wisdom-for-life/quotes/` | Wisdom for Life Quotes: Where Can I Find Good Ones? | Right here. Every wisdom for life quote Achology publishes, each with a written response on thinking clearly and living well, and our editor's picks. |
| Book Notes, All subjects | `/learn/book-notes/` | Book Summaries: Where Can I Find Good Ones? | Right here. Every book Achology has summarised across seven subjects, each with its key ideas and what to take from it, and our editor's picks of the best. |
| Book Notes, Psychology | `/learn/psychology/book-notes/` | Psychology Book Summaries: Where Can I Find Good Ones? | Right here. Every psychology book Achology has summarised, each with its key ideas on how people think, feel and behave, and our editor's picks. |
| Book Notes, Helping People | `/learn/helping-people/book-notes/` | Helping People Book Summaries: Where Can I Find Good Ones? | Right here. Every book on helping people Achology has summarised, each with its key ideas on listening, coaching and mentoring, and our editor's picks. |
| Book Notes, Mental Wellness | `/learn/mental-wellness/book-notes/` | Mental Wellness Book Summaries: Where Can I Find Good Ones? | Right here. Every mental wellness book Achology has summarised, each with its key ideas on stress, resilience and self-awareness, and our editor's picks. |
| Book Notes, Motivation | `/learn/motivation/book-notes/` | Motivation Book Summaries: Where Can I Find Good Ones? | Right here. Every motivation book Achology has summarised, each with its key ideas on what drives action and follow-through, and our editor's picks. |
| Book Notes, Personal Growth | `/learn/personal-growth/book-notes/` | Personal Growth Book Summaries: Where Can I Find Good Ones? | Right here. Every personal growth book Achology has summarised, each with its key ideas on confidence, maturity and habits, and our editor's picks. |
| Book Notes, General Interest | `/learn/general-interest/book-notes/` | General Interest Book Summaries: Where Can I Find Good Ones? | Right here. Every general interest book Achology has summarised, each with its key ideas on big questions and philosophy, and our editor's picks. |
| Book Notes, Wisdom for Life | `/learn/wisdom-for-life/book-notes/` | Wisdom for Life Book Summaries: Where Can I Find Good Ones? | Right here. Every wisdom for life book Achology has summarised, each with its key ideas on thinking clearly and living well, and our editor's picks. |

**The Quotes lists (Kain, Code's S175 and S176 theme sittings, 19 and 20 October 2026; written by Chat, S434 and S436).** The eight Quotes lists (`/learn/quotes/` and the seven `/learn/{subject}/quotes/`) take the same parts as the Articles and Book Notes lists, with three parts of their own that Kain chose from rendered options on the build site: the Editor's Picks as whole share cards and the Quote Article Anatomy panel (0.707.351 to 0.707.353), the band showing "The minds you will meet here" with his seven faces, and the quote wall, settled round by round in the S176 sitting (0.707.354 to 0.707.373). The words on all eight are his: the heading "Quote Articles", and the line "Quote Articles are as their title suggests: written responses to timeless, wise, and thought-provoking quotes." Build instruction and every measure: `BUILD_SHEET__Articles_Listing_S174` in the Listing Page folder, its Quotes sections. The Quotes lists keep 24 cards a page as DSRD 7 section 17.1 rules (Kain's yes, S436), and he signed off the Quote Articles list on the real page at 0.707.373. The eight Quotes lists' search titles and descriptions are settled (Kain, S448; the table above).

**S178 (Kain, Code's theme sitting, 21 October 2026; written by Chat, S438).** The list header takes Option 3 (the words start 48 under the breadcrumb, the kind buttons stand on the foot of the faces) and the faces panel warms to half colour on hover, people only: both in section 20.0f, which this section shares. The list titles are 33 at every width (section 34.13).

### 21.1 Page Structure (top to bottom)

1. Sticky header (DSRD 8 §18)
2. Breadcrumb (§21.3)
3. Mini hero (§21.2)
4. Content-type pill strip + sort toggle — unified control bar (§21.4)
5. Hairline transition (§21.5)
6. Card grid (§21.6)
7. Numbered pagination (DSRD 7 §17.1)
8. Rainbow stripe + footer (DSRD 8 §19)

### 21.2 Mini Hero

- **H1:** "[Category] [Content Type]" (e.g. "Psychology Articles") — Como, the 33 step, 700, brand orange #ED6922, line-height 1.2. *(Corrected S313 from 32px, which is not a step on the nine-step scale; the same correction §22.4's H1 took at S302.)*
- **Count:** "[X] [Descriptive Label]" — Mulish 14px/400, **soft grey #5E6B75**, margin-top 6px. Labels per content type: "In-Depth Articles", "Original Book Notes", "Enlightening Quotes", "Practical Workbooks" (see DSRD 7 §17.1). *(Colour corrected S313 from mid grey: this is a supporting line under a heading, which is exactly what Kain's S280 ruling moved to the soft grey, and DSRD 7 §1.1 forbids mid grey for anything a reader needs.)*
- **Intro:** 1 sentence — category-specific from §20.10 subtexts, or cross-category text from DSRD 2 §4.3. Mulish, the 16 step, 400, brand dark #354149, line-height 1.6, max-width 880px, margin-top 18px. *(Corrected S313 from 17px per the approved S056 override, which maps 17 to 16.)*
- **No overline** — category name is part of the H1
- **Hero container:** max-width 1200px, padding 20px 48px 0. The 880px intro measure sits inside it, which is the pattern DSRD 7 §4.1 already names for the category hub: the frame is 1200, the prose inside it is 880

### 21.3 Breadcrumb

Reuses §20.3 breadcrumb component.

- **Category-specific pages:** `Home` icon `ChevronRight` Learn `ChevronRight` [Category] `ChevronRight` [Content Type]
- **Cross-category pages:** `Home` icon `ChevronRight` Learn `ChevronRight` [Content Type]
- *(Corrected S378: both rows read "Home icon, Home, Learn". The house icon is the Home link, per the trail Kain signed as built at S090, DSRD 8 §25.)*

### 21.4 Content-Type Pill Strip + Sort Toggle (Unified Control Bar)

- **Layout:** flex row, justify-content space-between, align-items centre
- **Left group:** content-type pills (Articles, Book Notes, Quotes, Workbooks) — each links to `/learn/{category}/{content-type}/`
- **Right group:** sort toggle pills (Newest, A-Z)
- **All pills share:** Como, the 12 step, 500, 8px 16px padding, 20px border-radius. *(Corrected S313 from 13px, which is not a step; the approved S056 override maps 13 to 12.)*
- **Content-type active:** brand orange bg, white text
- **Content-type inactive:** off-white #F3F4F4 bg, brand dark text
- **Content-type hover:** brand orange at 10% opacity bg
- **Sort active:** brand orange bg, white text
- **Sort inactive:** off-white #F3F4F4 bg, **soft grey #5E6B75** text. *(Corrected S313 from mid grey: a pill label is a control label a reader reads, and the 2026-07-13 contrast audit already made exactly this correction to the inactive pagination pills.)*
- **Sort hover:** brand orange at 10% opacity bg, brand dark text

### 21.5 Hairline Transition

- 1px solid #EEEDED
- Max-width 1200px, centred
- **48px above and 48px below on desktop and tablet, 32px and 32px on phones (corrected S313).** This is a boundary between two page-level blocks, so DSRD 7 §4.3 governs it: one measurement, every page, every block boundary. It previously carried 24px above and 20px below, which §4.3 ruling 2 names outright as a defect rather than a variant, because a page-local spacing value is what that standard exists to remove. The element carrying the line owns the whole measurement, and the blocks either side contribute zero

### 21.6 Card Grid

- **Columns:** per DSRD 7 §17.1 — 3 desktop (≥ 1024px), 2 tablet (768–1023px), 1 mobile (< 768px) (per DSRD 7 §4.1)
- **Gap:** 24px (var(--grid-gap))
- **Card type per content type:** article card DSRD 8 §6.1, book note card DSRD 8 §6.2 (vertical), quote card DSRD 8 §6.3, workbook card DSRD 8 §6.4
- **No featured cards** on listing pages — featured cards are category hub (§20) only

### 21.7 Hero Vertical Rhythm

| Transition | Spacing |
|-----------|---------|
| Header bottom → breadcrumb | 48px (var(--sp-2xl)) |
| Breadcrumb → H1 | 20px |
| H1 → count | 6px |
| Count → intro | 18px |
| Intro → pill strip | 24px (var(--sp-lg)) |
| Pill strip → hairline | **48px (corrected S313, DSRD 7 §4.3)** |
| Hairline → first card row | **48px (corrected S313, DSRD 7 §4.3)** |

*The two hairline measurements were 24px and 20px. They are the one place this page set its own values against a site-wide standard ruled after it was locked, and §4.3 ruling 2 requires the page to inherit rather than keep a local variant. Every other row above is untouched: they are internal hero rhythm, not block boundaries, and §4.3 does not reach them.*

### 21.8 Prototype Reference Files

Desktop prototype: `listing-page-psychology-articles-v10.html` — tenth iteration, locked at V10. Single portable HTML file with Como fonts (all 8 weights via base64 injection), CSS-only image placeholders, all spacing values matching this specification. Psychology Articles used as the reference implementation. No external dependencies except Google Fonts (Mulish; the prototype is re-cut against the S085 body face under the S311 ruling).

Responsive prototype: `listing-page-responsive-review.html`. Full three-breakpoint design locked. Covers all phone and tablet behaviour specified in §21.9. Lightweight version: `listing-page-responsive-review-lightweight.html`.

### 21.9 Phone and Tablet Responsive Behaviour (LOCKED)

Three breakpoints per DSRD 7 §4.1: mobile (<768px), tablet (768–1023px), desktop (≥1024px).

**Page container padding**

| Breakpoint | Padding |
|-----------|---------|
| Desktop (≥1024px) | 0 48px |
| Tablet (768–1023px) | 0 32px |
| Mobile (<768px) | 0 20px |

**Mini hero**

| Element | Tablet | Mobile |
|---------|--------|--------|
| H1 | 28px | 26px |
| Count | 14px | 13px |
| Intro copy | 16px | 15px, max-width 100% |

*Type scale reductions mirror the category hub hero pattern (§20.14). H1 stays Como/700; count stays Mulish/400; intro stays Mulish/400. Only size reduces.*

**Four of these six sizes sit off the nine-step scale (26, 13, 16 is a step, 15), and they are deliberately not corrected here (S313).** The responsive rule is one of the two type rulings DSRD 7 §3.0 records as still open, waiting on its own rendered options for Kain's eye. Re-deriving them on paper would take a decision that is his, so they stand as built and are named here as owed to that ruling rather than left looking settled.

**Control bar — unified pill strip + sort toggle (§21.4)**

At desktop and tablet: single flex row, space-between. Content-type pills left, sort toggle right. No changes from desktop spec.

At mobile (<768px): two rows.
- Row 1: content-type pills (Articles, Book Notes, Quotes, Workbooks) — flex-wrap allowed, 8px gap
- Row 2: sort toggle (Newest, A–Z) — right-aligned via `justify-content: flex-end`
- Gap between rows: 10px

*At 375px viewport the full pill strip and sort toggle cannot fit in a single row. Two rows preserves all controls without truncation or horizontal scroll. Tablet (768px+) fits comfortably in a single row.*

**Card grid collapse**

| Breakpoint | Columns |
|-----------|---------|
| Desktop (≥1024px) | 3 columns |
| Tablet (768–1023px) | 2 columns |
| Mobile (<768px) | 1 column |

*Standard cards (§6.1–6.4) are all vertical-stack layouts — no internal reflow needed at any breakpoint. They simply fill the grid column width.*

**Pagination**

At desktop and tablet: full numbered row. 40×40px pills, 10px border-radius, 6px gap. Como 14px/500.

At mobile (<768px): compact truncated. Pill size maintained at 40×40px. Page range shows: ← [first] ··· [current−1] [current] [current+1] ··· [last] →. Ellipsis rendered as `···`, styled at mid grey, pointer-events none.

*At 375px with 20px gutters (335px usable), the compact 7-element row fits within the available width. Full numbered range would overflow.*

**Spacing reductions at mobile (DSRD 7 §4.1 token reductions)**

| Transition | Desktop/Tablet | Mobile |
|-----------|---------------|--------|
| Header bottom → breadcrumb | 48px (var(--sp-2xl)) | 32px |
| Pagination above | 48px (var(--sp-2xl)) | 32px |
| Footer above (last content → rainbow stripe) | 64px (var(--sp-3xl)) | 48px |

*All other listing page spacing values (hero internal rhythm, pill strip gaps, hairline margins, card grid gap) are unchanged across breakpoints.*

### 21.10 Decision Register (5 Decisions)

*A log, not the specification: this register records what was decided for this page and when. The operative spec is the section body above — where the two differ, the body governs.*

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Mini hero type scale reduces at tablet (H1 28px, intro 16px, count 14px) and mobile (H1 26px, intro 15px, count 13px) | Mirrors §20.14 category hub hero pattern exactly. Maintains visual hierarchy at narrow widths. |
| D2 | Control bar at mobile: two rows — content-type pills row 1, sort toggle row 2 right-aligned, 10px gap | Single-row space-between layout breaks below 768px. Two rows keeps all navigation controls visible and accessible without horizontal scroll. Tablet keeps single row. |
| D3 | Pagination at mobile: compact truncated (first · current±1 · last with ellipsis). 40×40px pill size maintained. | 40×40px pills fit the compact range within 335px mobile usable width. Truncation follows the first/current±1/last pattern — always shows anchors (first + last) and immediate context (current ±1). **Widened (Kain, Code's S178 sitting, 22 October 2026; written S442):** on every Knowledge Hub page this truncation now holds at every width whenever a run is longer than seven pages, centred, the current page an orange circle; DSRD 7 section 17.1 is the home. |
| D4 | Spacing reductions: header→breadcrumb 48→32px, pagination above 48→32px, footer above 64→48px at mobile | Follows locked DSRD 7 §4.1 sp-2xl and sp-3xl mobile reduction rules. No bespoke overrides — system tokens handle it. |
| D5 | Standard cards (§6.1–6.4) require no internal reflow at any breakpoint | All four standard card types are vertical layouts. They collapse cleanly via grid column reduction. No internal layout decision needed — confirmed by prototype review. |

*Production implementation notes for this component/page are in the Production Implementation Notes document.*

---

## 22. Individual Article Page Layout (LOCKED)

**THE THREE READING PAGES, S149 AND S150 (Kain, live with Code in Safari, theme 0.707.110 to 0.707.120; recorded by Chat S405 from RULING__The_Reading_Pages_Sitting_S149 and RULING__The_Hero_Label_In_The_Date_Line_S150, channel Archive).** These bind the article, the book note (section 32) and the quote page (section 40) alike, and where they and an older line in any of the three sections disagree, these govern. The values live in the design folders' prototypes and build sheets (Code's fold-back, Rule 14); this note records the rulings.

1. **The contents box is the rail (0.707.110).** Heading Como 24, 600, the dark, no spaced capitals; a count line Mulish 12 soft grey, 4 under it; section names Mulish 14, 400; numbers Como 12 orange (book notes and quote pages only; articles carry none); a hairline down the list's left edge in the site hairline; the current section an orange stretch on the rail with its name orange at 600; sections read draw soft grey. The pill rows are gone. Supersedes the contents card in section 22.5a. Kain turned down a grey card ("just creates even more crush").
2. **The mark behind the contents (0.707.110).** One large Achology bubble at 7%, tilted, half off the block's foot to the right, cropped by the block. Tab 3 of four: "I absolutely love it ... happy to lock that in".
3. **The date line is one standard on all three pages:** Mulish 14, 400, white at 85%, links included. Supersedes the S115 book note override of 16 and 500.
4. **The type link in the date line (S150, 0.707.120; supersedes S149's "Visit Knowledge Hub").** The orange label above the hero title is removed on all three pages. The date line ends with the type's link to its list, same tab, the date line's link style: "Articles at Achology" (/learn/articles/), "Wise Quotes at Achology" (/learn/quotes/), and on book notes View on Goodreads then "Book Notes at Achology" (/learn/book-notes/). Tab 1 of four. Supersedes the S130 label above the title.
5. **One hero for the three pages, from 1280 wide (0.707.115).** Title 16 above the summary, summary at 1.6 leading, date line 16 under it; the picture runs from the breadcrumb's line to the date line's (the article picture and quote square crop to fill; the book cover keeps its shape, sized from the height; supersedes the quote page's S146 lift of 35); the breadcrumb is held to the words' width on their left edge. Below 1280 the heroes keep their earlier layouts; that band is still open.
6. **The consistency audit (0.707.111).** Book note links take the article's quiet underline (32% orange, 3 below, full on hover). On book notes and quote pages the panel's line beside the contents is the site hairline with 48 either side (supersedes S115's 32; articles keep no line there, S148). The panel's grey #E1E5E5 becomes the site hairline (contents lines, open and close ring, share circles).
7. **Author article titles (0.707.112).** The question at 700, the series ending after it ("His Biography, Ideas and Life Works") at 500, the book note's own pair. Verified on 51 of 51.
8. **The quote page's Download, Share and Copy row (0.707.110).** Gap 32 (was 24); dividers in the site hairline (supersedes S146's mid grey, section 40 item 2); Download no longer bold.
9. **Related Further Reading** is gone from quote pages at every width, phones and tablets included, as Kain ruled at S146.

**Kain's verdict on the three, S405 in Chat:** apart from the editorial sweep, the article, book note and quote page templates are "good to go".

**THE S150 SITTING, WHOLE-DOCUMENT PASS (Kain, live with Code in Safari, Code's S150, theme 0.707.121 to 0.707.135; recorded by Chat S408 from RULING__The_Hero_Picture_Speech_Bubble_And_Line_S150, RULING__Author_Articles_Open_The_Panel_With_Their_Own_Picture_S150, RULING__Author_Article_Portrait_Takes_The_S147_Treatment_S150, RULING__The_Rest_Of_The_S150_Sitting and REPLY__Book_Note_Closing_Line_Live_S150).** The label ruling above (item 4) belongs to the same sitting. These continue the numbering and govern where any older line in sections 22, 32 and 40 differs; each older line they touch carries a pointer to them. Widths below are Code's own: the sitting worked from 1200 wide up, and item 5 above says 1280 for the one hero. The two figures are not reconciled by any record read this session; which is right for the hero is Code's to state in his next ruling file, and the band below the stated width is still open (item 10 below).

10. **The hero picture is cut to a speech bubble, with a line behind it (0.707.121).** Kain, on the band's ground: "so neat ... really impressive"; on the picture over it: "just dropped ... dumped there. It's like no effort has gone into designing this". Four rendered tabs on all four page types (into focus, mounted print, layered orange line, speech bubble), then "I actually really like the speech bubble ... the speech bubble with the layered line, like an integration of both." Round three, after he asked for the book note's line and the other pages' line to be standardised: "That's actually much, much neater." As built, from 1200 wide up: on the article, the author article and the quote page the picture is cut to the Achology speech bubble outline (the mark's outer shape, no inner letter), 216 wide at the right of its column, the book note's book footprint. On all four pages a thin orange line in the same bubble shape sits behind the picture or the book, the same size and shifted 40 left and 24 down; the gap from the words to the line is the same column gap on every page. The book note's book is unchanged and its line follows the book's own size (verified on four book notes including a taller cover). Everything stays inside the band (the S146 rule). **The three loose Achology bubbles behind the hero picture are removed** on the quote page, the book note and the article. This supersedes the S146 three-bubble ruling (section 40 item 1), the S147 one (section 32 item 3) and the S148 one (section 22.14 item 1). The author photograph's three bubbles in the writing are a different thing and stand (section 32 item 13; section 40 item 5). **Below 1200 wide the hero is still open**, and was named by Code as the next job of the sitting; Chat takes whatever he rules as one later edit.
11. **Author articles open the side panel with their own picture (0.707.122).** Kain: "especially on the articles, as I kind of scroll down the page, on the book authors articles, we have the Know Your Psychology block above the table of contents. It would be great if that could just be the article image. Because the table of contents isn't as broad as what many of the other articles are." On an author article (a title ending "His, Her or Their Biography, Ideas and Life Works", 51 of 51 on the build site) the band that opens at the top of the panel once the hero scrolls away showed the article's own picture, 256 square, above the contents; every other article kept the S148 Know Your Psychology picture there. **The panel's order was then superseded by item 13 below**: the picture now rests at the panel's foot, and Know Your Psychology has left the panel on every article. This narrows section 22.14 item 5 and then ends it.
12. **The author's portrait in an author article takes the book note's treatment (0.707.125).** Kain, on the photo floated left beside the second paragraph: "give that the same treatment that you would do with any other image across the other articles. In that position". The book note and the quote page already gave the picture in that position his S147 choice (tab 3 of four): the photo 224 wide and a 32 strip on its right holding three Achology bubbles, large at the top corner, medium at the photo's foot, turned, small between. Author articles now carry the same, at the same values (section 32 item 13), from 768 wide up; on a phone the photo keeps its plain, centred look.
13. **One side panel on articles, author articles and quote pages (0.707.128 to 0.707.132).** Kain: "keep the table of contents floating at the top right ... as soon as the hero banner is out of view through scroll the image ... rises in", and on articles: "the image maybe gets locked to the bottom of the right-hand bar ... it sits in the bottom corner of the viewing screen ... until it hits that hairline". As built, from 1200 wide on screens 760 tall or more: the contents at the top, ending at their last item, then the site hairline with 48 under it; the page's own picture at the foot of the screen once the hero has gone, never closer than the 48 under the hairline, and left out where it cannot fit. On articles and author articles that picture is the speech bubble and its line, 216 wide. **Know Your Psychology leaves the panel on every article** (this supersedes section 22.14 item 5 and the Know Your Psychology lines in the S112 round above, the side column paragraph and its table row, so far as the panel is concerned). On quote pages Kain: "replace the know your psychology logo with the book or the course image ... then the view the book on Amazon link must change and become View this Course on Achology": the panel carries the quote's source cover, the book's for the 75 book quotes and the course's for the 201 course quotes; the author's picture leaves the panel ("we can lose the author image"; it stays in the hero); book quotes keep "View the Book on Amazon" and course quotes take "View this Course on Achology" to the course page; Know Your Psychology leaves the quote panel's foot. The quote page's cover has no decoration behind it (Kain: "for books and courses that pop in ... they don't have background decoration") and is the book note panel's cover exactly, 256 by 357 with the book's own shadow (Kain: "I did not ask you to make them different I just said keep them the same").
14. **Subtitles: two lines on articles, author articles and quote pages, three on book notes (0.707.127).** Kain: "put in place a rule that restricts the subtitle of each article from crossing over onto three lines ... it's just kind of skewing the images", then on book notes: "because books are naturally deeper images it's okay, in fact it would actually be preferable if all subtitles carried over on three lines". From 1200 wide the article and quote page subtitle runs the words' whole column (800) instead of the S112 measure of 55ch; measured in the real font, all 390 articles and 276 quote pages now take two lines (237 ran to three before). Book notes take a 768 measure, the width that lands most on three. **The two lines are balanced (0.707.133).** Kain: "a rule ... that would make it more likely for the two lines to be as equal in length as possible"; the browser's balanced wrapping on the article and quote page subtitle (677 and 674 pixels on the mindfulness article).
15. **The book note stays as it is (Kain, S150): "as one stated rule ... the book note must remain as it is and it cannot change".** He then changed it on his own word twice, items 16 and 17 below, and the closing line at item 19.
16. **The book note panel's cover and button sit at the foot of the screen (0.707.135).** Kain, on the Boundaries book note: "the buy book button is positioned incorrectly on the right side panel (it should sit on the bottom via scroll)". The book note keeps its own panel otherwise; only the cover and its button sit at the foot of the screen, as on the quote page.
17. **The book note's five headings are replaced again (Kain, S150; the new five are at section 32.7).** Theme live from 0.707.133, page by page; the 150 bodies are not yet changed.
18. **Boundaries (boundaries-cloud), on Kain's report and his "yes" to download.** The cover file was the wrong book's (Boundaries in Dating). It is now the current edition's cover (994 by 1500, from its Amazon listing) and the image's sizes were regenerated. Still owed with the publishing clearance: a new file name for the cover (browsers keep the old picture for a year under one address) and the Amazon link and ISBN moved to the current edition, 0310351804 (the 2008 edition's address answers Page Not Found). The record's `source_book_author` reads "Henry Cloud" only; the book is by Henry Cloud and John Townsend, and the record is corrected to both when the 150 bodies move.
19. **The book note standfirst's closing line (Kain, S407; built 0.707.133).** "Keep reading to decide if this book deserves a spot on your shelf." It replaces the S102 fixed sentence at section 32.3 and section 32.9 item 1. Across all 150 book notes, measured in the real font at the 768 measure: 112 run to three lines, 29 to two, 8 to four and 1 to five. The nine past three are Man's Search for Meaning, Money Master the Game, The Science of Being Well, Boundaries, Open When, Before Happiness, The Stoic Challenge, Critique of Practical Reason and Mothers Who Can't Love. The line count is Kain's eye in Safari, not decided here; it turns on the summaries' length, not the theme.

**Carried by Code, not done at S150:** the hero below 1200 wide; the fold-backs of the three design folders into prototype and build sheet (Rule 14); the Listing page and Category hub faults; and Kain's yes or no on the Know Your Psychology picture at the article foot on tablets and phones, and whether Know Your Psychology should come back at the foot of the article panel.

Single-column editorial layout for individual Knowledge Hub articles (e.g. /learn/psychology/articles/self-awareness/). One shared template across all ~500 articles. Prototype file: `article-page-self-awareness-v2.html`.

**THE S148 SITTING GOVERNS WHERE IT DIFFERS (Kain, live with Code in Safari, S148; written S404).** Eight rulings took the quote page's and book note's components onto the article page; they are recorded in §22.14 and govern any line below that says otherwise.

**FIVE SUPERSESSIONS TAKEN AT S268, on Kain's approval.** This section was locked before each of the rulings below, and in every case the later ruling governs. The corrections are made in the section body, which is where this document's own note at §22.12 says the operative specification lives. The page's own signed spec is being written in the Article Page folder under Knowledge Hub Design Prototypes, and seven further items on this page are open with Kain.

| # | What this section said | What now governs | Where the later ruling lives |
|---|---|---|---|
| 1 | Two course cards, in a two-column grid | Three at desktop, two side by side at tablet, two stacked on a phone | DSRD 1 §3.4, which records that its own row said two until S253 and was corrected. §32.1 of this document already carries the same three-at-desktop ruling for the book note page (Kain, S252) |
| 2 | Courses tag-matched from the same category | The page reads its `lead_tag` field and fills the slots from that tag's mapped course list, topping up from the next tag and skipping duplicates. Never from the category, never by hand | DSRD 1 §5.7, ruled S253 and tightened S255 |
| 3 | Compact cards at DSRD 8 §6.8 | The compact card is DSRD 8 §6.9. §6.8 is the featured book note card. The same stale pointer in DSRD 2 §1.5 is corrected in the same pass | DSRD 8, read S268 |
| 4 | The author name links to "the author page" | The byline names the Achology pen name or instructor who wrote the piece and links to their profile at `/about/instructors/{slug}/`. The source author is a different person with a different page at `/learn/authors/{slug}/` | DSRD 1 §3, which distinguishes the two senses of author explicitly |
| 5 | The signature block carries a one-line bio | The bio comes from the people registry in the theme, never written into a page and never carried in an upload file | The same rule already ruled for the book note page at DSRD 2 §1.6 |

**THE PAGE IS SIGNED, AND A SECOND ROUND OF SUPERSESSIONS CAME WITH THE SIGNING (Kain, at Code's S082, on the rendered live page in Safari, one variable at a time).** His words before the final tidy: "I am 100% happy with this template page now." Where a section below carries an S082 ruling, that ruling governs and the older text beneath it is kept as a record rather than deleted, so a reader meeting the old shape in an old file can recognise it.

| What changed | Where it is written |
|---|---|
| The foot is reordered: the course row above the reading row, and the page closes on the site's own enquiries panel | §22.1 |
| The category pill's stylesheet rules, still shipping after the pill went at S080, are deleted | §22.4 |
| The contents and share card, every value in it, and the 36% width fault it exposed | §22.5a, new |
| The author signature block's off-white band is withdrawn on this page | §22.7 |
| Related Further Reading becomes a list of links, with new copy in Kain's own words | §22.8 |
| Explore Related Learning Paths takes new copy in Kain's own words, and becomes Discover Related Learning Paths | §22.10 |
| The Where next panel comes off this page, with the back-link consequence measured | §22.10a |
| The section header's icon box stretches to its two-line text, on this page only | §20.7 |
| Five icon keys registered, and the heading-mark size and colour rules | DSRD 7 §5.2.1 |
| The course card's picture box takes the artwork's own ratio rather than a fixed height | DSRD 8 §7.1 |

**Two machine lines on this page's readiness record still fail, and neither belongs to this template.** Both are component work: a meta description written into the specimen article's own content record, and a contrast rule failing on nodes inside the course card and the site header. They are recorded at DSRD 8 §7.7 and are not this page's to close.

**A THIRD ROUND OF SUPERSESSIONS, FROM CODE'S S108 TO S110 SITTINGS WITH KAIN IN SAFARI (folded S357).** The page changed shape at S110. Where a subsection below carries an S108 to S110 note, that note governs and the older text is kept as a record. The one block standard for every article-type page (Kain, S109: "one design standard that we can apply to all block components in all article type pages") governs this page, the book note, the quote page, the help answer and every Knowledge Hub template still to be built; it is recorded in full immediately below this table and summarised here: the top of the page carries the trail, the title, one plain sentence at reading size, the reading bar, then the writing, and nothing else; a picture earns its place only by telling the reader something the words cannot; the reader reaches the first sentence without scrolling; every block sits in the reading column, one gap owned once, three text sizes, no repeated string above the writing, one job one component drawn once, nothing empty, heading then content then one action.

| What changed | Where it is written |
|---|---|
| The page opens on the Knowledge Hub hero band (`kh-hero`, DSRD 8 §28), not on a breadcrumb over a title on white; the band holds the trail, an overline, the title, the standfirst, the writer line and the article's picture at the right, all on the 880 column | §22.3, §22.4 |
| The 1104 hero width is retired on this page; the whole page has one left edge at 880 | §22.2, §27 |
| The featured image is the band's ground and an object in it; the 880 by 420 banner is gone | §22.5 |
| The meta line is the shared reading bar (DSRD 8 §26): writer, date, reading time, joined at the left, no word count, no Listen control on this type | §22.4 |
| The S082 contents and share card is replaced by the S110 contents card (DSRD 8 §27), floated right beside the writing with the share row as its footer | §22.5a |
| The section divider is a quarter finer and thirty per cent shorter | §22.2, S085 ruling 6 |
| The space under the page title is 8 where the reading bar follows, 24 where reading text follows | DSRD 7 §4.3 |

**The one block standard for every article-type page (Kain, Code's S109 sitting; the file is `RULING__One_Block_Standard_For_Every_Article_Page_S109`). Governs the article, the book note, the quote page, the help answer and every Knowledge Hub template still to be built.** Kain's words: "I simply want one design standard that we can apply to all block components in all article type pages", and "i am so tired of trying to guess with you". Four things he settled first, each a yes: the job of the top of the page is that a reader decides in a few seconds whether the piece is for them; the top carries where they are, what this is, one plain sentence saying what they get, then the facts that say what it costs them, then the writing; a picture earns its place only by telling the reader something the words cannot; a reader reaches the first sentence of the writing without scrolling.

*Part one, the top of every article-type page, in this order and nothing else above the writing:* the trail, in the reading column, aligned with the title; the title at the page-title step, on white or in the band, never on a picture; one sentence at reading size and reading colour, never caption-sized and never grey; the facts, which is the reading bar; then the writing. The page's own picture sits beside those words, never behind them, and only where it says something (the cover on a book note, the card on a quote page; nothing on a help answer or an article whose picture is decoration). Test: at a laptop's first screen, unscrolled, the first sentence of the writing is readable.

*Part two, the eight rules every block obeys:* (1) one column, every block in the reading column, spanning the page only where Kain has ruled that one by name; (2) one gap, owned once, the same value everywhere, every hairline 48 above and 48 below; (3) three text sizes, the page title, the block heading, the reading text, nothing between; (4) a picture earns its place or is not there; (5) no block repeats what the page has already said, no label repeating the trail, no second name beside the title; (6) one job, one block, drawn once, the same job on two page types is one component; (7) nothing to show means nothing drawn, no empty frame or placeholder; (8) every block runs heading, then content, then its one action. The tests: a block outside the column names its ruling; the gap between any two blocks measures the ruled value with one side declaring zero; no rendered size is off the scale; no string appears twice above the writing; two page types drawing one job share one class; no rendered block is empty. **The gate takes rule 2 first (Chat's call, S357):** the one-gap test is the fault that produced the S109 sitting and the one the existing rows do not yet measure; rule 3 is already held by `css_gate.py`. **Rule 3's three sizes are now named numbers (Kain, Code's S111 foundations sitting; recorded S357): the page title at 33 (28 on a phone), every heading at 24 whether it sits inside the writing or opens a block, and the reading text at 18 on 1.75, in a column of 800 with 16 between paragraphs.** DSRD 7 §3.1, §3.2, §4 and §4.1 hold each value; this page and every reading page reads them from there. Bringing the four built page types into line with part one is a sweep, started only on a signed brief; the reading bar on all four (S109) was its first part, and the S111 values landed on the article, the book note and the help answer at Code's S112.


**A FOURTH ROUND OF SUPERSESSIONS, FROM CODE'S S112 SITTING WITH KAIN IN SAFARI, ONE CHANGE AT A TIME ACROSS A FULL DAY (folded S358). Theme 0.377.0.** The S111 sweep was started and the article page turned into a redesign. Kain at the close: *"This page is unique. I've never seen an article page anything like this before."* **Where the third round above and this round disagree, this round governs**, and the third round's text is kept as the record of what stood when it was written. The largest reversal is the page's grid: S110 put everything on one 880 left edge, and S112 puts the whole page back on a two-column grid.

**The grid, which is the ruling that matters most.** One set of vertical lines governs the banner, the writing and the foot. The hero's words sit directly above the writing and share its width; the hero's picture sits directly above the side column and shares its width. **Content area 1104 (`--container-hero`), reading column 800 (`--container-article`), gutter 48, side column 256 (`--container-rail`).** All tokens; the rail is new at S112 and is derived rather than chosen, so the day the reading column moves the rail moves with it (DSRD 7 §4.1).

**The furniture left the reading column.** The contents card and the share row used to sit inside the writing, and inside it they had only two possible shapes, both wrong: floated, they cut the line beside them to 47 letters against the article's 87; full width, they blocked the top of the page. They now sit in a column of their own beside the writing, which takes no width from it.

**The side column, top to bottom:** **(S150 note: the picture, the Know Your Psychology mark and the panel's order below are superseded by the note at the head of section 22, items 11 and 13; Know Your Psychology has left the article panel.)** the article's picture, square, appearing as the banner leaves; the contents; and the Know Your Psychology mark held to the foot of the screen and linking to `/learn/`. Those three travel as one panel the height of the screen. Below them, at the foot of the column, the six related-reading links and one way out. The type in that column is one typeface, three sizes, one leading per size, and one label treatment for both lists.

| What changed at S112 | Where it is written |
|---|---|
| The page returns to the 1104 grid with an 800 reading column and a 256 rail; the S110 one-left-edge-at-880 ruling is superseded | §22.2 |
| The hero joins that same grid. Widening one without the other had put the writing 152px left of the hero | §22.4 |
| The byline leaves the hero. The author stays in the page's structured data and at the foot | §22.4, §22.7 |
| The standfirst takes a measure of 55 letters and a size of 21, the step above the body | DSRD 7 §4.1, the measure rule |
| The two cards inside the writing stop floating and move to the rail | §22.5a |
| The contents card becomes a panel: no fill, no border, no padding, heading down a step | §22.5a, DSRD 8 §27 |
| The share row moves from the panel to beside the author, then into the author's own row: small, square, aligned on his bottom line | §22.5a, §22.7 |
| The author card loses its sentence and stacks the role under the name, **on every hub page type** | §22.7 |
| An orange line divided the writing from the rail, then became a grey hairline running the full height of the writing, **because orange should mean one thing** | §22.2 |
| The Know Your Psychology mark joins the rail, becomes the generic artwork, then the full-width panel image, then pins to the foot of the screen and links to `/learn/` | §22.10 |
| Related Further Reading moves into the rail as a labelled shelf of six, dressed in styles the column already had | §22.8 |
| The background marks are switched off on this page. Kain's own approved design, switched off in one line, not deleted | DSRD 7 §14.1 |
| The dark course card comes off the page entirely | §22.10 |
| The course block takes Kain's new words: **"Want to Take Your Interest Further?"** over **"Explore related courses and deepen your understanding with insights you can use in everyday life."** | §22.10 |
| The trial panel takes Kain's new words, given earlier the same day | DSRD 8, the trial panel |
| The page now ends: writing, author with the share marks on his own line, two courses drawn from the article's own tags, footer | §22.1 |

**The template is signed and the specimen page is not publishable, and those are different things (Code, S112).** `page_gate.py` returned 40 passed and 12 failed on the rendered page. The failures are almost all content, not layout: a dead link, four acronyms used before being spelled out, a keyword at 0.30 per cent against a 1.0 floor, no DSRD 6 record on file, and a Rank Math score older than the page. Recorded here so the template's approval is never read as the page's readiness.

**One rule, two hosts (Code, S113).** Forty seven selector lines inside the S112 rebuild's media block in `knowledge-hub.css` read `:is(.kh-article__body, .bn-body)`. **The rail's rules exist once and reach both page types**, so a future ruling on the rail reaches the book note without anybody remembering to copy it. §32 records that the book note's reading area **is** the article's, not a copy of it.

### 22.1 Page Structure (top to bottom)

**SUPERSEDED AT THE FOOT BY CODE'S S112 SITTING (folded S358).** The page now ends: article body, author signature block with the share marks on his own line, the course row of two drawn from the article's own tags, footer. The contents card, the share row and Related Further Reading are no longer items in this vertical order at all: they sit in the side rail beside the writing (see the fourth round above). The list below is kept as the record of the S082 order.

**Reordered by Kain at Code's S082, on the rendered page in Safari, and signed there ("I am 100% happy with this template page now"). This order supersedes the one below it and is the operative list.**

1. Sticky header (DSRD 8 §18)
2. Breadcrumb (§22.3)
3. Hero (§22.4)
4. Featured image (§22.5)
5. Article body (§22.6)
6. Author signature block (§22.7)
7. Hairline, 1px #EEEDED, 48px margin top and bottom
8. Explore Related Learning Paths, the course row (§22.10)
9. Hairline, 1px #EEEDED, 48px margin top and bottom
10. Related Further Reading (§22.8)
11. Source Block (§22.9)
12. The closing enquiries panel (DSRD 8 §16), the site's own shared component with its copy unchanged from the pages already running it
13. Rainbow stripe and footer (DSRD 8 §19)

**What the reorder changes, named so nothing is lost.** The two halves of the foot are inverted: the course row now sits above the reading row rather than below it. **The source block stays beside Related Further Reading**, because this section has always treated those two as one zone and Kain's order did not name it; that placement was Code's call and is overturnable on sight. **The Where next panel is off this page** and §22.10a records what that costs. The hairline before the closing panel was asked for in the same sitting and is item 12's own top edge.

*The superseded order, kept as a record: author signature, hairline, Related Further Reading, source block, hairline, Explore Related Learning Paths, the Where next panel. Item 12 of that list was added S282 to correct it against §22.10a; both are now history.*

### 22.2 Content Column Width

**SUPERSEDED BY CODE'S S112 SITTING (Kain, live in Safari; folded S358). The page is two columns on one grid, not one column at 880.** Content area 1104, reading column 800, gutter 48, side rail 256. The hero's words share the reading column's width and the hero's picture shares the rail's, so banner, writing and foot obey one set of vertical lines. **A grey hairline runs the full height of the writing, dividing it from the rail.** It was an orange line first and Kain changed it, on the reasoning that orange should mean one thing on this site. The 880 figure everywhere below this paragraph reads 800 from S357 and the one-left-edge ruling reads as the record of what stood between S110 and S112.

*The S110 text, kept as the record:*

**Unified 880px column for the reading.** All the page's reading sits in a single 880px max-width column: the hero's information panel, the article body, and all post-article sections. No width transitions within the reading. **The 1104 exception below is retired (Kain, S110, on the rendered page: "bring the breadcrumbs and the container into the 880 size. So essentially the entire article and this container is all at one left edge"). Everything inside the hero band, the trail included, now begins on the 880 column; the band itself still runs the full width of the screen.** *The retired text, kept as the record:* the hero block and the breadcrumb were the ruled exception and sat at 1104px, pulled 112px outside the column, so that the logo, the breadcrumb, the hero block and the title all began at the same point (Kain, S085 ruling 4; approved on the rendered page at three widths at Code's S096). That was correct while the page had a wide picture block to align to; it has none now. *This paragraph read "Only the breadcrumb sits at 1200px page container width" until S337. The 1200 was never what the build did; corrected first to the reading column and then, within the same session, to 1104 on reading this page's own hero ruling.*

*Single column width eliminates visual jitter. The reader's eye never has to readjust to a wider or narrower container mid-page.*

*880px is no longer this page's own choice. It is the container width for every content page on the site, ruled by Kain at S085 and held at §27, and it is not put to him again on any template.*

**The S085 hero standard, recorded here at S337 now that Kain has confirmed it on the real page.** Eight things were ruled across a long sitting at Code's S085, and Code's own filing said plainly that none of them should reach a document until Kain had seen them in the theme rather than in a captured preview with injected CSS, because "he cannot make accurate design decisions from an inaccurate representation". **That confirmation is Code's S096 sitting**, where Kain saw the built page at desktop, tablet and phone and said "Thats perfect Claude, yes, i'm totally happy with this". What the rulings say, and where each one now lives:

| S085 ruling | Where it stands |
|---|---|
| 1. The hero block is 1104, the reading column stays 880 | **Superseded S110**: the article took the shared `kh-hero` band and everything in it sits on the 880 column (§22.2). The book note had already moved to 880 at Code's S102 (§32.2). The S081 top grid this ruling shaped is deleted from the theme, superseded rather than wrong, with the reasons written at the rules that carried it |
| 2. The hero block's shape is the standard, not its contents | Live. Both pages carry a rectangular block holding a picture and an information panel, with the reading beneath; only the split differs, because a book cover is portrait and an article banner landscape |
| 3. The article banner is 680 image, 400 panel, 24 gap, title on the whole 1104 line | **Superseded S110**: the banner is gone; the page opens on the shared band (§22.4) |
| 4. The breadcrumb sits on the hero block and aligns with the logo | **Superseded S110** on this page: the trail sits inside the band on the 880 column (§22.3, §27) |
| 5. The meta line's contents | **Superseded in placement, not in contents**, by Kain at Code's S088: it moved out of the hero to the head of the writing (see §22.4). Its word count comes from the body and its read time from that count, so the two cannot drift. **Superseded again at S109 and S110:** the line is the shared reading bar (DSRD 8 §26), under the title inside the band; on this page it carries the writer, the date and the reading time joined at the left, with no word count, because the contents card carries the count |
| 6. A section divider on the same line as every heading, filling the space to its right | Live, built as `achology_heading_dividers()`. **Amended S110 (Kain: "reduce the decorative lines thickness by 25%. Also, shorten its total length by 30%")**: the line is 0.75 rather than 1, and it stops 30 per cent short of the room the heading leaves, by a spacer inside the rule measured on the rule's own basis so it is exactly 30 on every heading; it hides itself where the room left is under 138. Outside feedback proposed removing it altogether and Kain kept it, finer and shorter. The glyph that once opened it was typed into every H2's text and is drawn by the stylesheet since S108. It draws on the article, the book note, the quote page and the help answer. **This does not contradict D1 in §22.11**, which removed a *standalone* divider sitting between zones. A rule on a heading's own line and a rule in the gap between blocks are different objects; D1 removed the second and ruling 6 added the first |
| 7. The course card narrows to 350, the Know Your Psychology mark inside it to 280 | Live |
| 8. The book note hero takes all of the above | Live; §32 carries the book note page |

**One thing in that S085 file was withdrawn by Code himself and is worth keeping, because the lesson outlives the detail.** He had reported the article page's pinned title and contents links as a fault and stripped the inline widths in his preview. They are not a fault: they are `knowledge-hub.js` implementing Kain's own heading balancer, which splits a two-line heading so about 65 per cent sits on the top line. It ran once at load against the real width, so widening the column with injected CSS afterwards left the old pin in place and made a working behaviour look broken. **The stale number was an artefact of the instrument, not a property of the page**, and a ruled behaviour of Kain's was stripped to make an overlay look right.

### 22.3 Breadcrumb

**Inside the hero band, on the 880 reading column, sharing the page's one left edge (Kain, S110, on the rendered page; theme 0.290.0). Measured after deploy: trail, title, summary, writer line and body all start at 280 on desktop, 32 on tablet and 20 on mobile.** The band restates the trail's colours for its dark ground, as components.css already did; the component itself stays sealed.

*Superseded, kept as the record:* it reused the §20.3 breadcrumb component, **on the hero block at 1104px, aligned with the logo** (Kain, S085 ruling 4). It read "at 1200px page container width" until S337. It was never at the 1200px page frame. §27 carries the site-wide rule.

*The breadcrumb width conflict carried on the board card was closed the wrong way, and that is now corrected. §27 was amended at S281 to read "The breadcrumb is the exception on every page type: it sits at the 1200px frame", citing this row, §22.2, DSRD 7 §4.1 and the built theme, and the four were declared in agreement. **They were not: the build has never put the trail at the frame on any page.** Kain ruled at Code's S090, on three whole live pages in Safari, that the build is right and the documents are wrong. Corrected here and at §27 at S337. The lesson worth keeping is that four sources were read as agreeing without any of them being measured against the rendered page.*

- **Format:** `Home` icon `ChevronRight` Home `ChevronRight` Learn `ChevronRight` [Category] `ChevronRight` Articles `ChevronRight` [Article Title]
- **Current page:** Article title is brand dark (#354149), not linked
- **Spacing:** 48px below header bottom edge (var(--sp-2xl))

### 22.4 Hero

**Superseded at S162 and S163 by §22.15 (the Soft Light hero).** Everything below in this subsection is kept as the record of what stood before.

**The page opens on the Knowledge Hub hero band, `kh-hero` (DSRD 8 §28), ruled by Kain at S110: "apply exactly the same hero styling to the article page. It's what we have to the book note page."** The band runs the full width of the screen; everything in it sits on the 880 column. It holds, in this order: the trail; an overline naming the page type and category; the title at the 33 step; the article's own written summary as the standfirst (the same summary every listing card already carries; nothing drafted); the writer line, which is the shared reading bar, directly under the summary; and the article's picture as an object at the right of the column, the same picture washed almost out as the band's ground. The columns stack below 1024, picture below the words. The reading bar's hairline comes off inside the band, because the band's bottom edge is that line; the body supplies the 48 beneath. The overline repeats the category, which Kain deleted as a pill at S080 because it cost a line; in the band it costs no line and matches the book note, and it goes if he reads it as the pill returning. His words on the band: "it's kinda perfect. It's exactly what we're looking for. It's simple."

*Superseded, kept as the record:* 880px column. Left-aligned text. No search bar, no background colour.

**The category pill is gone (Kain, S080), and its stylesheet rules went with it at S082.** No template has emitted it since S080, and fourteen declarations plus a hover state were still being sent to every reader until the S082 tidy pass deleted them, proved by serving the before and after stylesheets to the same page and comparing every computed style at nine widths. The table below is kept as a record of what it was, and nothing renders it.

**Category Pill (REMOVED S080; rules deleted S082):**

| Property | Value |
|----------|-------|
| Font | Como 12px/600 |
| Transform | Uppercase |
| Letter-spacing | 0.08em |
| Colour | Brand orange (#ED6922) |
| Background | Brand orange at 8% opacity |
| Padding | 4px 12px |
| Border-radius | 20px |
| Link | `/learn/{category}/` |

**H1 (Article Title):**

| Property | Value |
|----------|-------|
| Font | Como, the 33 step, 700 (corrected S302: this row read 36px, which is not a step on the nine-step type scale Kain ruled at S056 and is not what the theme renders; `base.css` sets `h1` to `--text-33` at 700. The scale governs and nothing may sit between its steps) |
| Colour | Brand dark (#354149) |
| Line-height | 1.2 |
| Margin-top | 16px below category pill |

**Meta Line: SUPERSEDED at S109 and S110 by the shared reading bar (DSRD 8 §26).** One component on all four Knowledge Hub page types, `achology_reading_bar()`, under the title inside the band. On this page it carries the writer (photograph, Written by, the author's name), the date and the reading time, joined at the left, with nothing at the right and no word count. The quote page's S108 exception below is superseded with it: the narrator's credit has gone from the bar, so the writer's name is back on every type. The two paragraphs and the table beneath are kept as the record.

**Meta Line (MOVED OUT OF THE HERO, Kain at Code's S088, on the rendered page: "place this above the opening paragraph title, within the main article container").** The strip now sits at the head of the writing, above the opening paragraph title, inside the main article container, on both the article and book note pages. The book note's meta line carries no "Achology Publications". The hero placement below is superseded; shipped in theme v0.118.0.

| Property | Value |
|----------|-------|
| Font | Mulish 14px/400 |
| Colour | Mid grey (#8A9199) |
| Format | '22 March 2026 · Kain Ramsay · 8 min read' |
| Separator | ' · ' (middle dot with spaces) |
| Author name | 500 weight, linked to the writer's profile at `/about/instructors/{slug}/`, brand orange on hover (corrected S268; the row read 'linked to author page', which does not distinguish the byline from the source author's hub at `/learn/authors/{slug}/`, per DSRD 1 §3) |
| Placement | Head of the writing, above the opening paragraph title, within the main article container (Kain, S088; supersedes 'Margin-top 8px below H1' in the hero) |

**One registered exception, the quote page (Kain, S108, ruled on the rendered page).** On a quote page the meta line carries no author name. His words: "So that names aren't competing with names, we just move Frederick's name out of the article info bar and just leave his name in the article author card underneath the article." The writer is still credited, in the signature card at the foot.

*Why the exception is needed.* The quote page is the one page carrying two names within a few lines of each other: the listen bar's "Read by Declan Fitzpatrick" sits directly above the strip, so the reading credit and the writing credit collide. The article page keeps its author, because it has no clash to resolve. The exception is the quote page's alone and does not travel.

### 22.5 Featured Image

**SUPERSEDED at S110.** The article's picture is the hero band's ground, washed almost out, and an object at the right of the band's 880 column (§22.4). It carries `alt=""` in both places: it is atmosphere, unlike the book note's cover, and a screen reader announcing one decorative image twice is worse than not announcing it; its authored alt stays on the attachment for every place the picture is information. No picture block sits above the writing. The table below describes a block that no longer exists and is kept as the record.

| Property | Value |
|----------|-------|
| Width | 880px (full content column) |
| Height | 420px |
| Border-radius | 12px |
| Object-fit | cover |
| Prototype | CSS gradient placeholder (per achology-prototypes skill) |
| Margin-top | 24px below meta line |

*In production: composite banner image (author portrait + book cover) from the image production system (DSRD 7 §12).*

### 22.5a The Contents And Share Card (ruled across Code's S082, each value on the rendered page)

**SUPERSEDED at S110 by the contents card, DSRD 8 §27 (Kain: "I like A, the Editorial index please claude").** The card now floats right beside the writing at the book note's own numbers (300 wide, 40 across, 32 beneath, bleeding into the gutter above 1040, full width on a phone), so it stays available as the reader scrolls; its label reads ARTICLE NAVIGATION PANEL, its heading Table of Contents, its line under the heading the section count and the word count, its toggle a round plus and minus, and the share row sits inside it as its footer under a rule. The S081 top grid that held this card is deleted from the theme. Everything below is the S082 record.

The card in the page's top grid, carrying the Table of Contents and the Share this Article controls beside the opening of the writing. Every value below was settled in one sitting, one variable at a time, on the real page in Safari.

**Its width is 36% of the column, and it had never been there.** Asking for it to be narrowed found a fault rather than a preference. The top grid ran `1.45fr 1fr`, and its own comment claimed that gave about 320, the width the card had been ruled to. Measured: 880 less the 24px gap is 856, and 856 over 2.45 is **349**. The card had been 32px wider than its ruled width since the grid was built, and the arithmetic was never checked against a render. **The grid is `1.7fr 1fr`, which lands at 317, against 36% of 880 being 316.8.**

**A mark sits before each heading, on the same line as the words.** Built first as a rule above the heading carrying the Achology bubble, which was the wrong reading of what Kain asked for, and corrected in the same sitting on his words: place them on the same line before the actual text. The bubbles are replaced by real registry marks, `list-ordered` before Table of Contents and `share-2` before Share this Article (DSRD 7 §5.2), both at 0.85em and both in the AA-safe orange.

| Element | Value |
|---|---|
| Table of Contents heading | Como, the 24 step (up one from 21), with 24px of air beneath it |
| Share this Article heading | Como, the 18 step, keeping its 16px beneath |
| Contents numbers | 14px, the title's own size (up from 12), with **tabular figures** so every title starts at the same point down the list |
| Share circles | 28px (down from 32, so the card could narrow), on the 10 per cent orange wash |
| Marks inside the circles | 14px and 16px (down from 16 and 18) |
| Every mark and label in the block | The AA-safe orange #B8460F. One orange in the block |

**Why the numbers moved, in Kain's words:** the two are not currently aligned with each other and this is visually obvious. They were already on the same baseline. **Two sizes on one line read as a misalignment whatever the baselines do**, which is the general lesson and not a fact about this card.

**Why the share circles were quieted by size rather than colour.** They were tried white with bubble-orange marks and rejected on sight ("revert back to what they were please"), so the wash and the AA-safe orange came back and the marks inside came down instead. **On that pale ground the AA-safe orange already sits close to the 3:1 floor DSRD 6 §7 gates against**, so lightening it would have bought subtlety by failing the scan.

**One idea that lived for one version, recorded so it is not proposed again as new.** Kain asked for the opening five words of the article to be set larger in the heading face, saw it rendered, and ruled the same sitting: undo this completely. The function, its call and its stylesheet rule came out together.

### 22.6 Article Body

| Property | Value |
|----------|-------|
| Font | Mulish 17px/400 |
| Line-height | 1.75 |
| Colour | Brand dark (#354149) |
| Width | 880px content column |
| Margin-top | 32px below featured image |

**Heading Styles:**

| Element | Font |
|---------|------|
| H2 | Como 24px/600, brand dark, margin-top 32px, margin-bottom 16px |
| H3 | Como 20px/600, brand dark, margin-top 24px, margin-bottom 12px |

**Blockquote:**

| Property | Value |
|----------|-------|
| Border-left | 3px solid brand orange (#ED6922) |
| Padding-left | 20px |
| Font-style | Italic |
| Colour | Soft grey (#5E6B75) |

**In-body links:** Brand orange, underline on hover.

**Which body sections carry a heading (ruled S292, Kain).** The article's six sections do not all carry an H2. The Opening Hook and the Close run **unheaded**: the hook is the intro paragraph directly under the H1, and the close is a short forward-looking wrap. The four middle sections, The Idea, Why It Matters, Going Deeper, and Putting It Into Practice, each carry their own reader-facing H2, with reader-facing H3s allowed inside Going Deeper.

The reasoning, recorded so the question is not reopened from cold: a heading above the hook makes the reader read a label before the sentence written to catch them, and a heading above the close announces the ending. The trade accepted is a four-item on-page contents list rather than six. *(The clause that used to follow this sentence imagined the article page one day gaining the travelling shelf; the shelf was retired at S085 and the article page carries its contents list in the top grid instead, §22.5a.)*

This settles an open build note that had stood in the `book-derived-article` skill, which stated the behaviour in prose, then declared it unconfirmed, then deferred it to this section, which did not cover it. The skill now carries the same ruling and the build note is deleted.

**The six-section shape above is the book-derived article's, and it does not govern every article type (ruled S302, Kain).** The four middle sections it names, The Idea, Why It Matters, Going Deeper, and Putting It Into Practice, are the book-derived template's own sections. The S292 ruling was written into this page-level section as though it governed the page rather than the type, and an instructor-attributed article read against it appears to fail a standard that was never its own. It does not: the instructor article's structure is the Hook-Book-Look-Took arc as a reflective essay (DSRD 2 §3.7 and the `instructor-article` skill), whose understanding movement may run to more than one reader-facing H2, so five to seven headed sections is the correct output rather than a deviation.

**The instructor-attributed article's close carries its heading.** Rendered for Kain at S302 on I13 at the full 880px column, both ways, with everything else on the page held still. He ruled the heading kept. So the unheaded-close rule above holds for the book-derived article and is reversed for the instructor article, and the reasoning behind each is different: a book-derived article's close is a short forward-looking wrap that a heading would announce, where an instructor article's close is a distinct reflective task the reader is being handed, which earns its own heading and its own place in the on-page contents.

**Its heading text is fixed: "What Could You Do With These Ideas?" (ruled S302, Kain).** It is the same wording on every instructor article, replacing "What to Do With This" wherever that stands. A question addressed to the reader rather than a label describing the section, which is what the section actually does.

### 22.7 Author Signature Block

**The off-white band is withdrawn on this page (Kain, at Code's S082, ruled on four renders of the whole page in tabs: the band gone, the card at half width, the block removed entirely, and the page as it was).** His words: "The band goes, a simple and clean solution. Much better!!" The ground, the 10px corner and the 20px padding come off; the portrait, name, role and bio all stay, and the portrait comes to 44px. The block went from 92px tall to 47 without losing anything in it.

**Extended to the book note page and moved onto the component (Kain, at Code's S088, on the rendered page: "look the band on the book note template too please claude, so we can consistency across all templates").** The band is withdrawn everywhere the block renders. Only two pages carry it, so the rules moved onto the component in people.css; the two pages no longer differ. This supersedes the scoping paragraph that stood here from S082, which read the withdrawal as this page only.

*The superseded card treatment, kept as a record of what was withdrawn: off-white ground var(--color-off-white) #F3F4F4, 10px border-radius, 20px padding, 52px avatar.*

| Property | Value |
|----------|-------|
| Background | None on this page (withdrawn S082) |
| Border-radius | None on this page (withdrawn S082) |
| Padding | None on this page (withdrawn S082) |
| Layout | Flex row, 16px gap between avatar and text |
| Margin-top | 32px below last body element |

**Avatar:**

| Property | Value |
|----------|-------|
| Size | 44px circular (corrected S082 from 52px, with the band) |
| Background | Brand dark gradient |
| Fallback | Author initials (Como 18px/600, white) |
| Border-radius | 50% |

**Text Group:**

| Element | Style |
|---------|-------|
| Author name | Como 15px/600, brand dark, linked to the writer's profile at `/about/instructors/{slug}/`, brand orange on hover (corrected S268, same ground as §22.4) |
| Bio line | Mulish 13px/400, soft grey (#5E6B75), single line, **read from the people registry in the theme** (S268). It is never written into a page and never carried in an upload file, the same rule already ruled for the book note page at DSRD 2 §1.6 |

**The mid-body writer photograph: instructor-attributed articles only (Kain, at Code's S116; scope corrected at Code's S117, written here S362).** Kain ruled at S116 that the writer's photograph also appears inside the body, mid-writing, on the instructor articles and on Karen's twelve, and on nothing else. The S116 build tested only whether the `author` field resolved to a real person, which every bylined article does, so 167 published pages (51 author biographies, 116 field-authority articles) briefly carried an editorial pen-name's portrait mid-body. Kain found it live on the Albert Ellis biography. Code fixed it at theme 0.426.0: the block now fires only where `article_type` is `instructor-attributed`, the value both instructor articles and Karen's twelve share and no other type carries. Verified live on one page of each kind. The signature block above is untouched by any of this: it renders at the foot of every article regardless of type, and always has.

### 22.8 Related Further Reading

**WHERE IT NOW SHOWS, AND THE SIDE PANEL'S RULES (Kain, live with Code in Safari, S146 and S147; recorded by Chat S401 from RULING__The_Quote_Page_Sitting_S146, RULING__The_Contents_Rail_S146, RULING__The_Quote_Page_Design_Principles_For_Every_Hub_Page_S146 and RULING__The_Book_Note_Page_Sitting_S147, channel Archive).** The quote page carries no Related Further Reading at any width (theme 0.707.82): Explore More Quote Articles does that job there, and Kain ruled two blocks offering the same action side by side make no sense. The book note carries none at any width either (0.707.90): Explore More Book Notes does that job there. **The article keeps it.** On every article-type page the side panel travels the whole article: its last item comes to rest 48 above the first hairline that closes the reading, measured from its last item, never its screen-high box; every contents highlight is the same width, the section names still folding by the S081 rule (0.707.67); the column's vertical edge carries on down to the hairline the panel rests on; the panel's square picture shares the cover column; and a link in a side list has one hover rule, colour only (underlines belong to links inside running text). Where the panel stands beside a row-based block, its list matches the rows line for line. One side effect is open, named in §32: the "all articles from this book" line (S361) rode inside this list and no longer shows on book notes.

Between the two hairlines, **below the course row** (§22.1, reordered S082). Section header plus a list of links. Positioned above the source block (§22.9) within the same zone.

**The compact card row is gone (Kain, at Code's S082, on the rendered page).** It is now a plain list of links, **three columns of three at desktop, two columns of three at tablet, and four links only on a phone**, verified at all three widths. Nine, six and four.

**What that supersedes, and one question it kills rather than answers.** The card row and its S302 count of three both go, because a list of names is not a compact card and adjusting the count would have been answering a question that no longer exists. **The three-or-two question the S081 sitting left open is dead**, and so is the measured fault that reopened it, every real title truncating at three cards, which cannot happen in a list.

**Section Header:** Reuses §20.7 section header component, with the icon box stretched to the two-line text on this page only (see §20.7).

| Property | Value |
|----------|-------|
| Icon | Lucide `Compass` (DSRD 7 §5.2), 24px inside the stretched container |
| Title | 'Related Further Reading' — Como 22px/600, brand dark |
| Subheading | **'Click on the links below for more reading on this fascinating topic.'** — Mulish 14px/400, mid grey. Kain's own words, written in the S082 sitting and copied character for character. It supersedes the registered line, which said "cards" after the cards had gone |

**Link List:**

| Property | Value |
|----------|-------|
| Layout | Three columns of three at desktop, two columns of three at tablet, four links only on a phone (Kain, S082, verified at all three widths). Supersedes the two columns of four he ruled at S081 the day before |
| Row spacing | A grid row gap, never padding on the links themselves. **The padding was the fault:** 10px on each link ran the block's box past its last line of text, so the white above the closing hairline read as 58 where every other block reads 48, and the same 10px pushed the first link 30px from its heading against a registered 20. The box measured clean and the page looked wrong, which is why only Kain's eye caught it |
| Content | Mixed: articles, book notes and quotes together (ruled by Kain, S272). Selection stays tag-driven. Supersedes 'tag-matched articles from the same category', which contradicted the cross-linking register at DSRD 1 §6.1 and §6.2 |
| Gap below | 24px before the source block |

**A way back and a way forwards sit beneath the nine links (Kain, at Code's S088, on the rendered page).** Two links in his own labels: **'More Articles in this Category'** and **'Browse the Whole Knowledge Hub'**, with the `arrow-left` icon (DSRD 7 §5.2) on the way back. **No hairline between the nine links and the two arrows**, his words: "please lose the hairline between the 6 links and the forward and back arrows." The nine-link count itself was ruled in the same S088 sitting: he first said the foot gave too many options, corrected a proposal of three or none to six, saw six rendered, and ruled nine; the complaint was four competing blocks, not the links. Shipped in theme v0.118.0.

*The superseded card row, kept as a record: compact cards per DSRD 8 §6.9, three at desktop, two side by side at tablet, two stacked on a phone, 16px gap, ruled S302 and rendered at three, four and six with real titles.*

### 22.9 Source Block (three cases, ruled S302; two variants ruled S268 superseded)

**Ruled by Kain at S302, on the three cases rendered as complete bottom blocks with real content.** The block answers one question, where this article came from, and there are exactly three answers:

| The article came from | The block shows |
|---|---|
| **A chapter of a book** (book-derived articles, author biographies with a source book) | The book, linking to its book note. Anatomy below, unchanged |
| **A lesson from a course** (video-derived articles) | The course the lesson came from, linking to the course page. Overline reads "From this course" |
| **Neither** (everything else: field-authority, buyer-intent, instructor-attributed, author biographies with no source book) | **Nothing. The block is not rendered at all.** The reader goes from Related Further Reading straight to the hairline and the course row |

**The school variant is removed (Kain, S302).** §22.9 carried a school variant from S268, on the reasoning that an article with no source book would otherwise carry no link to its own school. Kain ruled that an article that comes from a course points at a course, and that a school is not a thing a reader buys or enrols in: sending them to a school page sends them to a directory. **This also closes the icon registry gap** the S268 ruling left open, where the school variant and the course row directly below it would both have shown the graduation cap: with no school variant there is no second glyph.

**Why the third case renders nothing rather than a substitute (ruled S302, on two rendered options).** The alternative shown was lifting the lead-tag's first course out into its own block above the row. Rendered, the same course appeared twice within one screen, because the Explore Related Learning Paths row (§22.10) is already filled from the same lead tag by the same rule (DSRD 1 §5.7). **The row alone does the work.** An article with no source is not missing anything: the reader still gets three tag-matched courses immediately below.

**This is what the deleted fallback was hiding.** Until S302 the template rendered a hardcoded example book, Tasha Eurich's *Insight*, whenever `source_reference` did not resolve, so every third-case article showed another author's book as though it were deliberate. The fallback is deleted and this ruling is what stands in its place.

Horizontal card below Related Further Reading, within the same hairline-bounded zone. **The approved prototype for the book case is `RULING__Article_Source_Block_State_B_S268.html` in the Article Page folder under Knowledge Hub Design Prototypes.**

**Two states were rendered and rejected at S268 and remain rejected.** An instructor variant repeated the person the §22.7 signature block introduces a few centimetres above.

**Shared anatomy, both variants**

| Property | Value |
|----------|-------|
| Background | Off-white (#F3F4F4) |
| Border-radius | 12px |
| Layout | Flex row: image panel left, content right. Stacks below 768px, panel full width above the text |

**Book Cover (left), book variant:**

| Property | Value |
|----------|-------|
| Width | 140px |
| Background | Brand dark (#354149) |
| Content | Book cover image, centred |
| Prototype | CSS placeholder with brand dark bg |

**Content (right), book variant:**

| Element | Style |
|---------|-------|
| Overline | 'Book Note' — Como 11px/600, uppercase, brand orange, 0.08em letter-spacing |
| Title | Book title — Como 17px/600, brand dark, linked to book note page |
| Author | 'by [Author Name]' — Mulish 13px/400, soft grey |
| Description | 1–2 sentence summary — Mulish 14px/400, brand dark, line-height 1.6 |

**Watermark:**

| Property | Value |
|----------|-------|
| Icon | Lucide `BookMarked` (DSRD 7 §5.2) |
| Opacity | 0.05 |
| Position | Decorative, within content area |

*Links reader to the book note page, which has the complete "All articles from this book" and "All quotes from this book" collections (DSRD 2 §1.6).*

### 22.10 Explore Related Learning Paths

**Above the second hairline and directly beneath the author signature block** (§22.1, reordered S082). Section header plus course card grid.

**Section Header:** Reuses §20.7 section header component, with the icon box stretched to the two-line text on this page only (see §20.7).

| Property | Value |
|----------|-------|
| Icon | Lucide `GraduationCap` (DSRD 7 §5.2), 24px inside the stretched container |
| Title | **'Ready to Take Your Learning Further?'** — Como 22px/600, brand dark. Kain's own words, live with Code at Code's S147, theme 0.707.93, on every reading page (recorded S403). The chain: 'Explore Related Learning Paths' (S082 original) → 'Discover Related Learning Paths' (S082) → 'Want to Expand Your Understanding?' (S088) → 'Want to Take Your Interest Further?' (S112, recorded in the §22 table above) → the S147 words |
| Subheading | **'Explore related courses to deepen your knowledge and build on the insights introduced in this article.'** — Mulish 14px/400, mid grey. Kain's own words, S147, copied character for character, read back live on a book note and an article. **The sentence is identical on the article, book note and quote pages, deliberately:** Kain kept "this article" for book notes and quote pages at S147, as he had refused Code's 'book note' edit at S088 ("please accept the copy i gave you"). Supersedes the S112 line 'Explore related courses and deepen your understanding with insights you can use in everyday life.' and the S088 line 'If you liked this article, these course options could be the next step in your learning journey.' |

**The count-in-the-copy warning is retired with the S082 line.** The superseded subheading stated the count of two out loud; the S088 sentence states no number, so the copy and the card count can no longer contradict each other. The two-card count below is unchanged.

**Course Card Grid:**

| Property | Value |
|----------|-------|
| Card type | Full DSRD 8 §7 course cards |
| Count | **Two at every width (ruled by Kain, S302, on the real signed course card rendered at two and three inside the 880px column, with DSRD 5 figures).** Two side by side at desktop and tablet, two stacked on a phone. Supersedes the three-at-desktop count corrected in from DSRD 1 §3.4 at S268 |
| Why two | Two reasons, both seen rendered. **Room:** the course card carries a school line, an 18px title, a three-item stats row, a price with its guarantee pill and two buttons, and at a third of 880px the title and the button pair break up. Half the column holds all of it. **Relevance:** most lead tags map fewer than three courses. `learn-life-coaching` maps two, `learn-hypnotherapy` maps one (DSRD 1 §5.5), so the third slot is usually topped up from a less relevant tag, making it the weakest recommendation on the page by construction. Two also reads as a choice rather than a menu |
| Relationship to §22.8 | The reading block below is a list of links rather than a row of cards (rewritten S082), so the two no longer compete for the same shape. The earlier three-against-two comparison between them is history |
| Note on DSRD 1 §3.4 | §3.4's three-at-desktop count is the course card's grid **on the 1200px frame**, and it stands there. The article page is the exception, because its course row sits inside the 880px reading column (§22.2). The COMPONENT_DATA file for the course card records `columns_desktop_min_1024: 3` for the same reason and is not contradicted: that is the component's own default grid, not this page's |
| Layout | Grid within 880px, at the DSRD 7 §4.1 tiers |
| Gap | 24px |
| Selection | The page's `lead_tag` field, filled from that tag's mapped course list per DSRD 1 §5.7, topping up from the next tag and skipping duplicates (corrected S268; this row read 'tag-matched courses from the same category', which predates §5.7) |

### 22.10a Closing "Where next?" Panel (RULED OFF THIS PAGE, Kain S082; the S272 ruling below is superseded)

**The Where next panel is off the article page.** Kain reordered the foot at Code's S082 and the page closed on the site's enquiries panel (DSRD 8 §16). **At S088 the trial panel replaced the enquiries panel on both content pages**, as one shared block, ruled by Kain on the rendered page; his word for what he wanted was "token", and the copy and picture are his. The enquiries panel itself is unchanged and still closes About, Reviews, Testimonials and the Founders' Letter. **Our People and the sixteen instructor profile pages left that list at Code's S097** (theme v0.161.0, on Kain's instruction given on a screenshot of the block): both now close on the trial panel too, which is the same `achology_warm_room()` component carrying different words, so the shape, the column and the boundary above it did not move. His reason, recorded because it generalises: a person's profile ends better on an invitation in than on a support desk, and the enquiries route is already in the footer of every page on the site. The S088 sitting also set the foot standard in his own words: three blocks under the body on every content page (the two course cards, Related Further Reading, the trial panel), with the page types differing at the hero and nowhere else; the grey "Next possible steps after this Book Note" block is retired, its copy preserved in the S088 channel ruling. This section is kept as the decision record, because the panel's row 1 carried a rule and the rule's fate needs to be readable rather than inferred.

**What that cost, measured before it was called a cost.** Row 1 was recorded here as closing the source-author back link DSRD 1 §6 requires of every article, quote and book note, which this page had nowhere else. **That row has never rendered on any article on the site.** It wants the source author, which DSRD 1 §3 defines as a different person from the byline, and no field on an article carries one; §3.4 says the label is assigned at production and nothing does it. The rule was already unmet, so removing the panel does not make it more so. **Where the back link lives when the field exists stays an open question on the page's build sheet**, which already owns exactly that question and is the right home for it. It was not answered by guessing.

*The superseded S272 specification, kept as a record.*

Below the course cards, closing the page. The locked layout ended the page on the course card grid; Kain ruled on two rendered options of the whole page foot and took the panel. The Book Note page closes the same way after his S249 ruling, for the same reason: a foot of card grids alone reads as junk, three named rows do not.

| Property | Value |
|----------|-------|
| Component | The "Where next?" panel, DSRD 8 §13, plain off-white variant (not the §13.5 image backdrop the Book Note page uses) |
| Width | The 880px article column |
| Top margin | `--sp-3xl` 64px from the course card grid, the component's own default |
| Rows | Three, in this order: **1.** everything from the article's source author, linking that author's Knowledge Hub hub page. **2.** the article's topics. **3.** the free community tier. |
| Row 1's purpose | It closes the source-author back link DSRD 1 §6 requires of every article, quote and book note, which this page had nowhere else |
| Copy | **Approved by Kain, S282**, rendered in the page foot at 1200, 768 and 390. Title: `Where next?` Lead: `Three places to take this idea next.` Row 1: `Everything from {Author}` / `Book notes, quotes and articles drawn from their work.` Row 2: `Explore this article's topics` / `Follow the ideas in this piece across the Knowledge Hub.` Row 3: `Join the Achology Gateway` / `Free access to the events calendar, the coaching board and the community discussions.` |
| Approved prototype | The Article Page folder, under Knowledge Hub Design Prototypes. **Filed S282**: the S272 ruling named this folder and no prototype was in it. |

### 22.11 Elements Removed

The following elements were evaluated and intentionally excluded from the article page template:

| Element | Decision | Rationale |
|---------|----------|-----------|
| Tag pills | D3: removed entirely | Tags serve low-intent browsing — better placed on listing pages and category hubs where the browsing mindset is active |
| "More From This Book" section | D4: removed | This content belongs on the book note page, which already has "All articles from this book" and "All quotes from this book" as confirmed components (DSRD 2 §1.6). Source book callout links readers there. |
| Standalone section divider | D1: removed | Tag pills (with hairline border-top) and source book callout (off-white background) provide sufficient visual separation through colour shift alone. Hairlines used as zone separators instead. |

### 22.12 Decision Register (10 Decisions)

*A log, not the specification: this register records what was decided for this page and when. The operative spec is the section body above — where the two differ, the body governs.*

| # | Decision | Rationale |
|---|----------|-----------|
| D1 | Section divider removed | Colour shifts (off-white, hairlines) provide sufficient separation without a standalone divider |
| D2 | Unified 880px reading column | Single column width eliminates visual jitter. The hero block and breadcrumb are the ruled 1104px exception (S085, confirmed S096); corrected S337, this cell read "Only breadcrumb sits at 1200px". |
| D3 | Tag pills removed entirely | Tags serve low-intent browsing — better on listing pages and category hubs |
| D4 | "More From This Book" removed | Belongs on book note page. Source book callout links readers there. |
| D5 | Source Book + Related Further Reading merged into one zone | Reduces post-article sections from four to two hairline-bounded zones |
| D6 | Related Further Reading positioned above source book | Section header + compact cards first, source book callout below. 24px gap. |
| D7 | "Next Learning Steps" renamed to "Explore Related Learning Paths" | Subheading: 'Find practical learning opportunities that build on the ideas explored in this article.' |
| D8 | Author in two positions: meta line + signature block | Meta line for quick attribution. Signature block for identity and bio at end of article. |
| D9 | Lucide selected as icon library | ISC licence, free commercial use, consistent stroke weight. See DSRD 7 §5.2. |
| D10 | Icon registry task created | All 58 icons selected and registered in DSRD 7 §5.2. |

### 22.13 Prototype Reference File

Locked prototype: `article-page-self-awareness-v2.html` — second iteration, locked at V2. Single portable HTML file with Como fonts (all 8 weights via base64 injection), CSS-only image placeholders, all spacing values matching this specification. "Self Awareness" article used as the reference implementation. No external dependencies except Google Fonts (Mulish; the prototype is re-cut against the S085 body face under the S311 ruling).

*Note: Locked prototype covers desktop only. Mobile/tablet responsive behaviour (single column, full-width images) applies per DSRD 7 §4.1.*

*Production implementation notes for this component/page are in the Production Implementation Notes document.*

### 22.14 The S148 Article Page Sitting (Kain, live with Code in Safari, S148, theme 0.707.99 to 0.707.108; written S404 from `RULING__The_Article_Page_Sitting_S148`)

Kain's direction: carry over the components already approved on the quote page and the book note page, with their rules; nothing new designed. Each line below governs where an earlier line of §22 differs. Page used: `/learn/general-interest/articles/is-mindfulness-evidence-based/`.

1. **Bubbles behind the hero picture:** the quote page's three, at its sizes, from 1024 wide up (0.707.99). **Superseded S150 (0.707.121): the three loose bubbles are gone and the picture is cut to a speech bubble with a line behind it; see the note at the head of section 22, item 10.**
2. **The foot takes the quote page and book note structure** (0.707.101): under the signature, a list of six (or three, or none) articles from the same category, in the quote page's markup and S130 rules, with a contents entry. **Related Further Reading (§22.8) is off the article page at every width.** The side panel runs down to the list's closing hairline.
3. **The list's words are Kain's own** (0.707.103): heading "Browse More Achology Articles", with "Achology" in orange; line "Each article answers a popular question people ask online, helping you choose what to read next."
4. **No section numbers on articles** (0.707.104), neither in the contents list nor above the headings: an article's sections are not steps. Book notes keep theirs (§32).
5. **The side panel opens with the Know Your Psychology picture** (0.707.106), linked to the Knowledge Hub home page, with no hairline under it, in place of a second copy of the article's own picture. The picture at the panel's foot is removed. The "Visit the Knowledge Hub" button tried at 0.707.105 came out with it. **Superseded S150 (0.707.122, then 0.707.128 to 0.707.132): Know Your Psychology has left the article panel altogether, and the article's own picture, the speech bubble and its line, rests at the panel's foot; see the note at the head of section 22, items 11 and 13.**
6. **The contents list scrolls inside its own box** when longer than the screen (0.707.105), so the panel never runs past the foot of the screen; with item 5 the panel fits a 900-tall laptop screen whole.
7. **Quote pages are unchanged** by this sitting (checked live by Code).
8. **An article with no picture of its own takes its course's picture in the writing** (0.707.108): the S130 rule the instructor articles follow (course cover, the full course name, "Bestselling Achology Course") with the quote page's S147 bubbles, at the second paragraph of the second section. Author biographies and instructor articles keep their own pictures. This is the Achology Content Standard's named exception (p) to Part 13 rule 1 (Kain, S404). The course name on the picture follows the Standard's Part 9 rule 1 and Part 13 rule 3: its link sits on the course's short name.

**Owed by Code (Rule 14 fold-back):** the Article Page folder's prototype and build sheet brought to this state in a theme session. **Not general:** none of these eight changes a token or a site-wide rule, so DSRD 7 is untouched.

---

### 22.15 The Soft Light hero and its page changes (Kain with Code, theme sessions S162 and S163, 13 October 2026; built 0.707.234 and 0.707.235; written S423 from RULING__Hero_Direction_Soft_Light_Picked_S162, RULING__Hero_And_Section_Title_Simplifications_S162, RULING__Tablet_And_Phone_Hero_S163 and SHIP__Hero_Soft_Light_S163)

**This subsection governs the article, book note and quote page.** Where §22.4, §32.3 or §40 say otherwise, this wins; their older text stays as the record. The workbook takes the same family with its own differences (§37.6). It replaces the S161 hero standard's dark band and speech bubble (RULING__One_Hero_Standard_For_The_Four_Content_Types_S161 section 2); that ruling's lengths (title 50 to 60 characters, subtitle 150 to 170) and its 984 frame stand. Kain's words: "A. Soft light. We found it ... It brings them all together ... One hundred percent."

**1. One hero, direction A, Soft Light (`achology_kh_hero()`).**
- The band is warm cream (`--color-warm-cream`) with a hairline foot. Title in Como, brand dark, its ending one weight lighter; subtitle in brand dark; facts in orange link colour.
- The article's picture and the quote page's portrait dissolve into the band with no frame and no speech bubble, laid in with multiply, at about half strength, faded in from the right and from below, drawn far enough right that nothing dark sits behind the subtitle (worst-case contrast behind the subtitle 6.1 to 8.6 from 1024 up; 4.5 is the minimum).
- The book note stands its cover (the book component, straight, never tilted) on a faint bookshelf that fades into the cream from the right.
- **The quote page's hero is the article's** (Kain: "just lose the quote completely. And just let the banner be the banner. Same as the article."): the faded portrait, with no quote, slip or card in the band. The quote appears once, in the card under the band.
- **What lives in a hero:** breadcrumb, title, subtitle and the date line. Article: the faded picture. Book note: the cover, and "View on Goodreads" in the date line. Quote: the faded portrait. Nothing else: no author line, no audio player, no share buttons, no type label, and no buttons at any width.

**2. The date line ends on the word count (`achology_facts_line()`, shared with the Help answer's reading bar).** Article: "1 October 2026 · 7 Min Read · 1,294 words". Book note: the same, with "View on Goodreads" before the count. Quote: "24 September 2026 · 4 Min Read · 700 words". The count is the contents panel's own number, read and never typed. "Articles at Achology", "Book Notes at Achology" and "Wise Quotes at Achology" leave the line; the breadcrumb still links to each type's list.

**3. The frame (Kain approved, S162: "I 100 per cent approve the container width").** The content frame is 984: the reading column 680 at 18, a 48 gap, and the floating side panel 256, which stays. The page container is 1080 (984 plus two 48 gutters). See §27's S423 amendment.

**4. Section titles and the contents panel.** *(The contents panel part is superseded by 22.15a item 1, S163; the section title bubbles stand.)*
- No numbers anywhere: the small orange numbers above section titles on book notes and quote pages are removed, and so are the contents list's 01, 02 numbers.
- A faint Achology bubble mark (about 12 per cent strength, 60 by 46) stands behind the first word of every section title, centred on it and reaching a little out past the writing's left edge, on all three types. Built as a server-side wrap of each title's first word; a title that opens with a tag is left as it is.
- The contents panel loses its "8 sections · 1,294 words" line, its bottom hairline, its rail and its watermark. The entry being read carries a small faint bubble (about 30 wide) behind its first word, kept inside the panel, in place of the orange bar (option "Behind", chosen by Kain from four rendered).

**5. The foot runs full width with no side panel (Kain, S162).** *(Partly superseded by 22.15a items 3 and 4, S163: the panel runs down to the two paths again, and the foot is the two paths.)* The side panel ends where the reading ends, its last item (the Amazon button on book notes and quote pages) at the reading's foot. The author row, "Explore More ..." and "Ready to Take Your Learning Further?" with its course cards then run the whole 984. This reverses Kain's S146 ruling that the quote page's panel floats down to the closing hairline; the small number above "Explore More ..." goes too.

**6. Tablet and phone (Kain, S163: "yes").**
- 1024 to 1099: the desktop hero with its object column narrowed from 312 to 260, so the words keep about 640.
- Below 1024, one column: the breadcrumb; then the picture in its own row (200 tall on a tablet, 168 on a phone), dissolving into the cream on every side, or on a book note the cover on its faint shelf; then the title, subtitle and date line. Nothing is drawn behind the words below 1024 (contrast 10.1).
- Phone: title 28, subtitle 18, gutter 20. Tablet: gutter 32, and the band's top space 48 (§26).
- Below 1200 the book note's Amazon and author-site buttons, and the quote page's Amazon or course button, sit in the side panel's strip under the contents, where from 1200 up they already sat.

**7. The listen bar is off every quote page** (Kain, decision K10, S422), measured gone at five widths at 0.707.234. Help answers still carry it until Code's backlog line 26 is done.

**8. Two page gate lines, settled by Chat at S423 (reversible; Kain may overturn).** breadcrumb-below: a recorded exception for these three heroes (§26). content-width: 1080 is added to the gate's widths as a standard, because it is Kain's own S161 and S162 frame (§27).

**Open, for Kain's next step (Code's S163 note):** from 1024 to 1199 the hero's words start at the page gutter while the writing starts further in; the first item of his alignment audit of the other components on these pages.

### 22.15a The side panel, contents and foot, and the reading lines (Kain with Code, theme session S163, 13 October 2026; built 0.707.236 to 0.707.240; written S423 from RULING__Side_Panel_And_Foot_S163, SHIP__Side_Panel_And_Foot_S163 and RULING__Contents_Lines_And_Foot_Conversation_S163)

Governs the article, book note and quote page. Where 22.15 says otherwise, this wins. Approved state: `previews/panel-s163` in the theme folder.

**1. The table of contents is the Drawn Bubble** *(Superseded at S164 by the Ring, §22.15b item 1; kept as the record.)* (Kain: "option one, the drawn bubble, is really, really nice ... let's lock that in", the orange a bit more subtle). The contents sit in a true Achology speech bubble (cream, with the logo's curved tail). Its outline draws itself in soft orange as the reader moves through the writing; a white card glides to the section being read; sections already read turn soft grey. The S162 small bubble behind the current entry is gone. The section title bubbles in the writing stay (Kain: "it breaks the page up ... it just makes the page warmer"). The heading "Table of Contents" and the mark are centred on one line at 22px, filling the bubble's inner width (0.707.239).

**2. Both reading lines are 1px and identical** (Kain: "both lines need to be the same"; 0.707.240): the line under the site menu (Kain S147, was 2px) and the line drawn round the contents bubble, the same orange, the same fill as the reader scrolls.

**3. Articles carry their course's cover and button in the panel.** The course is the first of the row the page's own tags fill, so it matches the foot's course path; the cover is drawn as the book note's; the button is the quote page's own "View this Course on Achology". An article with no matched course keeps its picture.

**4. The side panel runs down to the hairline above the two paths, on all three types** (Kain: "the right-hand column could just extend right down to the hairline"). The author row and "Explore More" sit in the 680 reading column beside the panel. This partly reverses 22.15 item 5 (the S162 full-width foot) and restores Kain's S146 rule on all three types.

**5. The foot is the two paths, in place of the two course cards** (Kain: "option one, two paths, is absolutely stunning. This finishes the page off absolutely perfectly"). The workbook thank-you page's block is now one shared piece (`achology_two_paths()`) on both pages. On a content page the course's first point ends at its count ("175 instructional tutorials."). The count is read from each course's curriculum file, never typed, on both pages.

**6. Open, not built: "The Conversation."** *(Settled at S164 and S165: see §22.15b items 2 to 4.)* Kain chose "The Conversation" from five designs (`previews/paths-s163`) as the next form of the two paths: the course and the community as two speech bubbles, words drafted by Claude for him to tweak. Still to settle with Kain: what is fixed and what is read automatically, the one page-type word, which course shows when a page has no matched course, and whether the lesson count and ratings appear. Code renders four presentations first. Until it is signed, item 5 stands, and this subsection gains its standard when it is.

### 22.15b The Ring contents panel and the close of the content pages (Kain with Code, theme sessions S164 and S165, 13 October 2026; built 0.707.241 to 0.707.253; written S424 from RULING__Table_Of_Contents_S164, RULING__Conversation_Foot_Standard_S164, RULING__Close_Soft_Tile_And_Real_Pages_S165, and the S164 and S165 ship notes)

Governs the article, book note and quote page. Where 22.15 or 22.15a says otherwise, this wins. The workbook thank-you page keeps the two paths (§22.15a item 5).

**1. The contents panel is the Ring (S164; built 0.707.249 and 0.707.250; replaces the Drawn Bubble of §22.15a item 1).** Kain found the panel "a little bit clunky, bulky ... it doesn't look visually spectacular". He chose the Progress Card, then the Ring after the second round ("your use of fonts and text sizes and spacing just isn't good"), then the Header Band after the third, and cut its "Section 3 of 8" line ("just have the percentage read").
- The card is white with a hairline border, the panel radius and the card shadow.
- The band across its top is cream. It holds "Table of Contents" in the heading face at 21, "N% read" in orange beneath it, and on the right a 56px ring that fills to the share read, with "current/total" in its centre.
- Two numbers, one source: the share read is the header reading line's own calculation, so the two always agree. The section is the panel's own current section.
- One row per section, the title at 15/1.45 under hairlines, with an 18px status mark at one indent: a tick on orange for read, an orange ring for the current section, an empty circle for sections to come. Three tones: read in mid grey, current in dark at 600, to come in soft grey.
- Below 1200 the ring stands down and the open and close control sits inside the band. Folded on a phone, the card is the band alone.
- Lives in knowledge-hub.js section 0c and kh-band.css section 4. The S163 Drawn Bubble drawing is removed.

**2. The close of the content pages (S164; built 0.707.241 to 0.707.243; replaces the two paths at the foot of the article, book note and quote page, §22.15a item 5, and answers item 6).** Two bubbles side by side and level, tails down and outward ("very clean, that's brilliant"), one for the course and one for the community.
- **Kain's words, one line each on desktop:** the heading "Ready to Further Your Learning?" and the line "You've finished this {type}. Choose how you'd like to continue: on your own or with like-minded others?" These replace the heading "Keep the Conversation Going" and its subtitle in Code's first build. {type} is "article", "book note" or "quote".
- **Fixed words (0.707.241, unchanged unless Kain says):** the labels "Study it on your own" and "Talk it through with others"; the community name "Live Learning in the Achology Community", its description, its facts (Live every day, Mentorship, Free coaching) and its button "Explore Membership". The course button reads "Explore This Course".
- **Read from the page, never typed:** the course is the page's best-matched course, the same as the side panel's. Its name, its approved description (data/courses.json hero_description), its cover artwork, its lesson count and its ratings. The facts sit on one line ("the facts are really good").
- **Video and Live (0.707.242 and 0.707.243).** No books: Kain ruled a book beside a tile "completely inappropriate", and a diploma course "is a course", the community "a membership subscription". The course is a lesson ready to play: its own course-card artwork (images/courses/course-NNN-540.webp) in a player with a play button, a progress line and the lesson count. The community is a session happening now: Kain's group picture (no text), a Live tag and three participant tiles. Both use the same frame. The background wash and the drawn community cover are retired.
- **The mirror:** both bubbles share one grid of six rows, so each row starts level on both sides. The community words are written to the course words' lengths.
- **Reading and spacing:** the words read from the left; the tails turn in toward each other; more room above the footer.
- **No course matched:** the community bubble stands alone, centred, as the two paths did. The DiMAP fallback is still Kain's open choice (§22.15a item 6); it was not raised in the sitting and nothing was changed.
- Lives in `achology_close_conversation()` in knowledge-hub-parts.php and section 7 of kh-band.css; images/close-community-bg.webp.

**3. The close's icons are Soft Tile (S165; built 0.707.253).** A graduation cap beside the course title and speech bubbles (Lucide messages-square, now in the theme's icon registry) beside the community title, each in a softly tinted rounded tile. Built from previews/conversation-s164 round 8, option 1, Code's recommendation. Kain's instruction to stop the option pages was taken as the go-ahead.

**4. Open, put to Kain and not changed (S165):** the page gate's block-heading check wants each supporting line at 12 to 25 words. The community line, in Kain's own words, is 31; the course line, read from the course, is 28. Kain rules whether the gate bends or the lines are cut. **Settled (Kain, S165, "yes"; written S425 from SESSION_REPORT__S165):** the close and the Ring are LOCKED, and Kain's words stay as written. The block-heading check's 12 to 25 word band is a recorded exception for the close's two supporting lines (community 31 words, Kain's own; course 28, read from the course).

**5. Work goes into the real theme, not option pages (Kain, S165: "can we turn this into like real pages now, please? ... real theme pages. And can you please stop pushing more design systems?").** For the page sweep, changes go straight into the real theme and are shown on the real pages in Safari; Kain objects if he wants a change. This matches The Shared Rules section 1, Version 14 (build the best version, show it rendered, change on objection), so Chat's call at S424 is that it is not a widening and The Shared Rules are not changed.


### 22.15c The panel logo, no picture no button, the cover over the panel, and the close's tiles (Kain with Code, theme session S166, 14 October 2026; built 0.707.257 to 0.707.276; written S425 from RULING__Panel_Logo_And_No_Picture_No_Button_S166, RULING__Hero_Cover_Centred_Over_The_Contents_Panel_S166 and SESSION_REPORT__S166)

Governs the article, book note and quote page. Where 22.15, 22.15a or 22.15b say otherwise, this wins. Each item was built, shown on the real page in Safari and approved by Kain.

1. **No picture, no button ("set in stone", 0.707.265).** On a wide screen, where the side panel's picture cannot fit (kh-aside--nofit, from 1200 wide), its button (View this Course on Achology, View the Book on Amazon) is left out too. Kain: "it's pointless having that button if it's not showing the image." Phones unchanged: both show.
   - **Every width (Kain with Code, theme session S167, 15 October 2026; built 0.707.279; written S425 from RULING__No_Picture_No_Button_Every_Width_And_Quote_Download_S167).** The rule holds at every width where the panel's picture is left out, mobile and tablet included: the S163 rule that showed the strip's buttons below 1200 is removed, so the button shows only where its picture does (1200 wide and 760 tall and up). Below 1200 these pages carry no Amazon or course button in the panel; the course still appears in the close. Prototypes: PROTOTYPE__Article_Page_S167_APPROVED, PROTOTYPE__Book_Note_Page_S167_APPROVED, PROTOTYPE__Quote_Page_S167_APPROVED.
2. **The contents list stays at 15, with 8 above and below each row (0.707.265).** A trial at 14 was reversed on his word; RULING__Table_Of_Contents_S164 stands.
3. **The Know Your Psychology panel logo (0.707.266 to 0.707.276).** Where the cover or picture cannot fit, one Know Your Psychology logo fills the column's width under the contents, shown only where it fits whole, never on a phone. On all three page types (this supersedes Kain's S132 word that the book note draws no Know Your Psychology mark). Colours only from the page (Kain: "a brand consistency thing"): KNOW brand orange, YOUR soft grey #5E6B75, PSYCHOLOGY brand dark #354149, the bulb orange; one logo, images/knowledge-hub/kyp-page.webp. It links to the page's own course, else its best-matched course (the same as the panel's course button), else the Knowledge Hub. Two faint circular orange ripples open from behind its centre to invite the click: border 22.5%, fill 3%, one every 1.5 seconds, reaching about 250 across; none where the reader asks for less movement; no separate touch dot.
4. **The book note's cover is centred over the contents panel (0.707.257 and 0.707.258).** From 1200 wide the cover's centre and the panel's centre line up and both end at the same right edge; below 1200 the cover stays centred in its own column. Only the book note has a cover.
5. **The close's six tiles (0.707.259 to 0.707.263).** Built from Karen's whole pictures (folder "Bottom Page Options Block"), in one near-neutral warm tone (dark #2c2a28 to cream #f6f3ef) with one 1px fine white edge; the picture address carries a version tag so browsers fetch it fresh. Kain: "That's actually perfect."
6. **Signed off as wholes on the real page:** the article (what-is-self-understanding, 0.707.263: "I'm totally happy to sign this page off. As a whole now, it's perfect.") and the book note (the-tao-of-fully-feeling, 0.707.276, top to bottom). The quote page (why-rigid-thinking-holds-you-back) was approved through part 3 and is not yet signed.
7. **The order of work (Kain, S166):** agree the final templates of the article, book note and quote page; then finish the workbook page; then a session to make the theme as clean as it can be.

### 22.16 The four Knowledge Hub single pages are one family (Kain, Code's S179 kh-page-family theme session, 22 October 2026; written by Chat, S442)

Governs the article, the book note, the quote page and the workbook page together (sections 22.15 to 22.15c and 37.6 to 37.8). The signed workbook page is the reference. Kain ruled one item at a time, Before and After on the four real pages at computer, tablet and phone widths. Code's audit found these already one shared piece and the same on all four: the top band, the contents panel below 1200, the reading type, the foot hairlines, the close, the Browse More block, and the author row on the three that have an author.

**The parts.**
1. **Browse More heading:** all four read "Browse More Achology {Kind}", Achology in orange: Workbooks, Articles, Book Notes, Quote Articles. Each kind keeps its own supporting line; the contents entry follows the heading. Kain: "yes".
2. **The close names the workbook:** "You've finished this workbook." The other three already named themselves. Kain: "yes".
3. The share row's screen reader label names its page (Share this Article, Book Note, Quote). Code's own, invisible.
4. Settled by Kain's earlier rulings and not reopened: the faint bubble behind headings in the writing (22.15 item 4) and the small tile on the workbook's own sections (37.8 touch 4); Browse More beside the side panel on the three (22.15a item 4) and full width on the workbook (37.7 item 3); no author row on the workbook.

**The movement (the workbook's signed touches, carried to all four).**
1. The author row, Browse More and the close rise gently into place as they arrive (the workbook's touch 10, the same values). Kain: "yes".
2. The picture behind the top band drifts more slowly than the page, at 0.3 of the scroll: the shelf on a book note or workbook, at every width; the faded picture on an article or quote page, from 1024 wide only, because below that nothing sits behind the words (22.15 item 6). Kain: "That is absolutely stunning ... All pages take the slower drift."
3. The book note's cover in the band lifts 6 under the pointer, as the workbook's does (touch 8). Kain: "Yes, Claude."
4. The picture in the writing lifts 6 under the pointer, whatever it shows: course cover, author photograph, the workbook's source cover. Kain: "standardize this. Throughout every single article that carries an image in that spot ... universal."
5. A Browse More row answers the pointer as one: its mark or cover lifts 3, its words turn orange, its arrow slides forward 4. Kain: "yes".
None plays under reduced motion; without scripts every block shows.

**Built once** (0.707.455, 0.707.459 and 0.707.461): one movement set in the shared band stylesheet and script, the workbook's own copies removed; the spacing check found the book note's author row 32 under its writing against 48 on the other three, and it was fixed. Measured at 1280 and 390 on the three published pages and the Karpman workbook: no console error, no sideways scroll, nothing moves under reduced motion.

**Kain's forward notes, banked (not yet work).** On the drift: "This is just a beautiful standard that I think could just become site-wide." Code's survey of fifteen page kinds: the drift fits where a picture or faint mark sits behind a band's words, never on words or on anything clicked. Knowledge Hub first: the front page (shipped 0.707.437), the subject and list pages (the list family round), the Help Centre and Help answers. Later, a round of its own: About, Student Reviews, Testimonials, Courses and the page-not-found page. Not: search, Pricing, Browse by Topic. Kain, to that plan: "yes, please do claude". He also said the drift could reach the course and school pages when they are built.

**Still to come:** the walk-through in Safari and Kain's one sign-off for all four, then the four list kinds by the same method (bands, headers and other parts only; walls and cards belong to section 20.0h).

### 22.16a Browse More and the close's backdrop on the four pages (Kain, Code's S179 kh-page-family theme session, 22 October 2026; built 0.707.492 and 0.707.494; written by Chat, S445)

Kain on the walk-through: "the pages are very, very nice ... they look like a family now". He then ruled the Browse More block part by part, after turning down several rounds as patchwork: "This should just be a really simple gateway ... Article names presented really neatly."

1. **Kain's own four lines under the heading,** one line each on a computer. Workbook: "Achology workbooks explore a single, thought-worthy idea and help you apply it in daily life." Article: "Achology articles explore real questions people ask and offer thoughtful, practical answers." Book note: "Achology book notes summarise key ideas from books, helping you decide what to read next." Quote: "Achology quote articles explore popular quotations and consider what they mean in daily life."
2. **No icon beside the heading or in the rows.** Kain: "too many icons ... You can't have the same icon next to the title as what you have next to the article names."
3. **Article, book note and quote page: the six pieces by whole page title.** One column, in the block's signed S130 type and spacing: Como 16 at 500, 16 above and below each row, a hairline between rows and none under the last, the arrow at the right. Kain: "Why don't you please just use actual article names?"
4. **Workbook: the titles beside a stack of workbooks.** The list is just wider than its longest title, so each arrow sits close. Beside it the next three workbooks are stacked: their real covers, or the Achology workbook cover drawn by the theme where a workbook has none yet, three different covers. They are squared up at rest and fan under the pointer, with the four steps' S178 movement. "Browse All Workbooks" sits under the stack as the site's orange button. On a computer the stack rises 20 into the space beside the heading's line, and the block is no taller than the list. Kain: "that's actually really good ... build it, get this done. We're done with these pages."
   **On the workbook page each title's ending is a small note (Kain, Code's S500 workbook page sitting, 11 November 2026; theme 0.708.024; written home by Chat, Session 465, night).** Every workbook title ends the same way ("Free Worksheet"), so the six rows read alike. Told that whole titles were his own S179 choice, and shown four ways (Name Only, Code's recommendation; Shortest; Quiet Ending; Ending as a Note), Kain chose: "4 Ending as a note please". Each title is cut at its last colon: the name is the link's words in the list's own lettering, and the ending is a small quiet note at the right before the arrow, the writing's face at 14 in soft grey, under the name on a phone. No word is written or changed, and a screen reader still hears the whole title. A title with no colon prints whole. The note reads the post's own title, never its search title. Workbook pages only: articles, book notes and quote pages keep item 3's whole titles.

Built at 0.707.492. Measured on the three published pages and the Karpman workbook at 1280, 834 and 390: one line per title on a computer and a tablet, 32 under the heading, 48 (32 on a phone) to the next hairline, no icons, every image loaded, no overflow and no console error. The spacing check of the four pages' foot passes at all three widths. Section 22.16's parts item 1 (each kind keeps its own supporting line) now means Kain's four lines above, and its movement item 5 now means the row's words turning orange and the arrow sliding, because the rows carry no mark.

**The close, Ready to Further Your Learning, takes the Open Page backdrop (the same sitting; built 0.707.494).** Kain: "the only bit of the page that just feels out of touch ... the cream one has an orange trim around it, and they look like speech bubbles ... Don't redesign, don't restyle. It's literally just the backdrop." Four backdrops were shown: Soft Cream, White Cards, Open Page and One Panel. Kain: "3, open page, that's perfect, Claude. That's great, build it, thank you." The speech bubbles, their orange trim and both tails are gone. The two cards sit on the page 64 apart, with a hairline between them on a computer. The community's words are in the page's dark and its labels in the link orange. Pictures, words, buttons and layout are unchanged, on all four content pages. This supersedes the bubble shape in section 22.15b item 2.

**Reach.** The quote page's Browse More is a plain list of titles by this ruling. So the one wall brief's line putting "the quote page's Browse More cards" in its reach (section 20.0h) is overtaken, and the one wall did not reach it (0.707.498, section 20.0h).

### 22.16b The four content pages are signed off as one family (Kain, Code's S179 kh-page-family theme session, 22 October 2026, at theme 0.707.496; written by Chat, S445)

Kain walked the four real pages in Safari: the article what-is-self-understanding, the book note the-tao-of-fully-feeling and the quote page why-rigid-thinking-holds-you-back on the build site, and the Karpman workbook in the local copy of main. Asked "Do you sign off the article, book note, quote and workbook pages?", he answered "yes". Earlier the same sitting, on the last block: "We're done with these pages, build it, thank you."

**What he signed:** the family parts and the five movements (section 22.16); Browse More and the close's Open Page backdrop (section 22.16a); and the close's community icon matched to the course icon (0.707.496), which changes section 22.15b item 3's community glyph. The ships: 0.707.455, 0.707.459, 0.707.461, 0.707.463 (the flag button, switched on at 0.707.464 and 0.707.465), 0.707.492, 0.707.494 and 0.707.496.

**What is not in it:** the four list kinds, which join Kain's consolidation pass (the one wall, the new quote card and the shared parts) rather than a separate round. The page gate records (DSRD 6) for the four page types were not rerun in that session, so each page type's record stays open until they are.

This closes section 22.16's "Still to come" first half (the walk-through and the one sign-off). It also completes the quote page's sign-off left open at section 22.15c item 6.

## 23. About Page Timeline — "The Achology Story" (STRUCTURE LOCKED)

The About Page Timeline tells Achology's story across 13 milestones from 2012 to 2025/26. It is section 5 of the About page, sitting below "The Thinking that Drives Achology" cards and above "In Our Students' and Members' Words". The component is built from five elements stacked vertically: a heading and lede that ride inside a pinned frame, a dark stage carrying an odometer, an era chart and a live counter, a fixed-height window through which the 13-milestone timeline scrolls, a terminus line, and a four-figure statistics panel beneath the window. Era is the organising principle — five named eras walk visually from brand dark to brand orange, mirroring the company's trajectory.

**Lock status note:** This section describes the component as built and approved with Kain on 22 July 2026, in `page-about.php`, `about.css` and `about.js` at theme v0.35.x. The built page is authoritative. Structural anatomy, scroll behaviour, the era system, milestone copy, spine and dot alignment are LOCKED. Where this specification and the built template ever disagree, the template is correct and this section is the thing to fix.

**Mechanics unlocked and changed (Kain, Code's S209 sitting, 2 November 2026; written home by Chat 19 at S452).** Kain said yes to rows 1, 2, 3, 4, 6 and 7 of a seven-row board on the whole Story, and no to row 5, the closing line as a statement with a button. His yes overturns this section's lock on the scroll mechanics. The era system, the milestone copy, the spine and the dot alignment stay locked. Built at theme 0.707.723 and 0.707.724 (`about.css`, `about.js`), and read back at 1440 by 1200, 1440 by 900, 1280 by 700, 834 by 1050 and 390 by 760:
1. The four-number band leaves the pinned frame for its own frame after the story; without script it stays in place. The reading window is clamp(220px, 100vh minus 620px, 640px) on a computer and clamp(220px, 100vh minus 600px, 560px) under 1024.
2. On screens 768 wide and up but under 960 tall, the lede steps aside, the chart takes the right 62 percent of a slimmer card and the running count sits bottom left under the era, so the story pins.
3. Each year is set in the heading font at 24, brand dark, in its own 96px column from 768 up.
4. The four timeline counts are small pills, 14 on an orange wash, hugging their words.
6. A row of the five era names under the stage, each in its era's colours, moves the story to that era; the era being read is ringed.
7. Under 768, a slim dark bar under the menu shows the year and era being read while the story is on screen; it is decorative and hidden from assistive readers.

The same sitting also moved the student count under the chart inside the dark card on phones only (under 768). The About page's signed spec carries all of this in its section 5a.

### 23.1 Outer Wrapper & Container

- **Inner wrapper:** max-width 880px (`--container-article`), centred horizontally
- **Background:** #ffffff (white)
- **Body font stack:** 'Mulish' with a system sans fallback stack (per DSRD 7 §3; the previous serif fallback retired with the face at S085)
- **Body text colour:** #354149 (brand dark); descriptive body copy uses soft grey #5E6B75 (per D10)
- The component extends the policy page frame (`.policy-page`, `.page-container`, `.article-container`), and its styles load from `about.css`, enqueued only on `/about/` after `policies.css`

### 23.2 Header Block

The heading and lede sit **inside** the pinned frame, so they remain on screen while the timeline scrolls beneath them.

- **Heading:** "The Achology Story"
- **Lede:** "Like all great educational institutions of our time, Achology boasts a unique origin story. Thirteen milestones across five eras, from the world's first video-based psychology course to a worldwide learning community 695,578 students strong."

### 23.3 The Dark Stage

A dark panel directly above the window. It repaints continuously as the reader scrolls, always reflecting the milestone currently at the reading line.

Four elements:

| Element | Behaviour |
|---|---|
| **Odometer** | Digit strips animating the enrolled-student figure for the current point in the story. At rest: `5,000` |
| **Era chart** | A hand-authored inline SVG with five era segments, 13 milestone dots and a moving era flag |
| **Era name and dates** | Repaints to the current era. At rest: `Origins`, `2012 to 2014` |
| **Live counter** | Labelled `Students & Active Members Enrolled` |

The stage replaces the three-cell student enrolment bar specified before this rewrite. The student-count progression it existed to show is carried by the milestones themselves (2017, 2021, 2022, 2025/26) and by the odometer.

### 23.4 The Pinned Window

The timeline runs inside a fixed-height window that holds still on screen while the story scrolls through it.

- **Pin mechanism:** `position: sticky` on the frame
- **Track movement:** the timeline track translates upward one pixel for every pixel of page scroll — the story moves through the window at 1:1
- **Reading line:** 96px inside the window. As each milestone crosses it, that milestone is marked reached and the dark stage repaints to its year
- **Window height:** `clamp(260px, calc(100vh - 703px), 510px)` at desktop; `calc(100vh - 674px)` at tablet
- **Flat fallback:** where the frame cannot fit the screen, `about.js` adds `.is-flat` and the whole block lies flat as a plain scrolling list. Measured at build: flat is false at 1440×1000 and 768×1024, true at 390×844

There are no era filter tabs and no filter behaviour. The eras appear as static group headings within the scrolling track, and `data-era` attributes remain on the group containers as structural markers only.

### 23.5 Era Colour System

Five named eras. Colours walk from brand dark (Origins) through slate-grey hybrids (Growth, Expansion) into burnt orange (Evolution) to full brand orange (Community) — visually mirroring the company's arc from origins to community. Set inline in `page-about.php` as `--era` values and consumed by `about.css`.

| Era slug | Display tag | Dates | Era colour |
|---|---|---|---|
| `origins` | Achology Origins | 2012 to 2014 | #354149 |
| `growth` | The Growth Years | 2015 to 2017 | #4d6672 |
| `expansion` | The Expansion Years | 2019 to 2020 | #8A9199 |
| `maturity` | The Evolution Years | 2021 to 2023 | #c05a1a |
| `community` | Community Development | 2024 to 2026 | #ED6922 |

Internal slugs remain `origins | growth | expansion | maturity | community` in the markup; the visible tag for the `maturity` era reads "The Evolution Years".

### 23.6 Timeline Spine

- **Width:** 2px
- **Colour:** #ED6922 (brand orange), 0.35 opacity
- **Position:** left of the milestone rows at every width, aligned with the dot column
- **Length:** spans the full height of the timeline track

### 23.7 Milestone Block Anatomy

Every milestone is a single left-aligned row: dot on the spine at the left, content to its right. There is no alternating layout at any width.

**Content elements (top to bottom inside each milestone):**

| Element | Style |
|---|---|
| Era tag (uppercase pill) | 11px / weight 700 / padding 3px 10px / border-radius 4px |
| Year badge | 12px / weight 700 |
| Stat number (landmark milestones only) | 36px / weight 700 / heading font |
| Stat label (follows stat number) | 13px / soft grey #5E6B75 |
| Title | 17px / weight 600 / brand dark #354149 |
| Description | 15px / soft grey #5E6B75 (`--color-soft-grey`) |

### 23.8 Per-Era Milestone Styling

| Era | Dot fill | Year badge | Tag background | Tag text | Stat colour |
|-----|----------|-----------|----------------|----------|-------------|
| Origins | #354149 | #354149 | #e8eaeb | #354149 | — |
| Growth | #4d6672 | #4d6672 | #eaeeef | #354149 | #4d6672 |
| Expansion | #8A9199 | #6b7680 | #f0f1f2 | #354149 | — |
| Evolution | #c05a1a | #c05a1a | #fce8d9 | #7a3606 | #c05a1a |
| Community | #ED6922 | #ED6922 | #fde8d5 | #7a3606 | #ED6922 |

### 23.9 Dot Variants

Two dot styles signal milestone significance.

| Variant | Size | Border | Used for |
|---|---|---|---|
| Standard | 16×16px | 3px solid #ffffff | Default milestone |
| Large | 20×20px | 3px solid #ffffff | Landmark milestones — 2017, 2021, 2022 |

All dots are filled with their era colour (per §23.8) and have border-radius 50%. There is no dashed variant.

### 23.10 Terminus Line

The timeline closes on a single sentence rather than a helper line and button.

- **Copy:** "695,578 mature learners from around the world have brought the Achology story this far. Will you join them?"
- **Link:** "join them" → `/membership/`

### 23.11 Statistics Panel

Four figures in a panel below the window.

| Figure | Label |
|---|---|
| 4.66 | Average Course Rating |
| 175,162 | Total Student Ratings |
| 216 | Countries With Students |
| 28 | Total Number of Courses |

### 23.12 The 13 Confirmed Milestones

Year, era, dot variant, stat, title and description are locked as built. Inline link targets are shown in brackets.

#### 2012 — Origins (standard dot)
- **Title:** The world's first video-based psychology course, published on Udemy
- **Description:** [Kain Ramsay → /about/instructors/kain-ramsay/] records and publishes the world's first video-based psychology training programme, taking a subject usually reserved for lecture halls and private clinics and putting it in front of anyone with an internet connection. The foundation of what would later become Achology is laid in this single, quiet decision.

#### 2014 — Origins (standard dot)
- **Title:** The Achology learning platform was first founded with 12 courses included
- **Description:** The Academy of Modern Applied Psychology opens with 12 on-demand courses, built on the conviction that psychological education belongs to anyone prepared to study it seriously, whatever their background. What began as a single course becomes a platform with a curriculum, a clear direction and a name.

#### 2015 — Growth (standard dot)
- **Title:** Curriculum expands to 17 interlinked psychology-based e-learning courses
- **Description:** The curriculum deepens into 17 interlinked e-learning courses, each designed to reinforce the others rather than stand alone, so understanding compounds with study. Students no longer simply buy a course; they enter a coherent body of work with a grounded, deliberate order to it.

#### 2016 — Growth (standard dot)
- **Title:** Live ONLINE skill and competency development training workshops begin
- **Description:** Achology begins running live, real-time online group workshops for skill and competency development, connecting students across time zones who had until now studied alone. It is the first expression of the principle that comes to define the academy: psychology is learned in dialogue, with and through other people.

#### 2017 — Growth (large dot)
- **Stat:** 100,000 / Students & Active Members Enrolled
- **Title:** A landmark year for Achology: global scale, platform growth & partnerships
- **Description:** Achology passes 100,000 enrolled students, begins building its own bespoke learning management system, and launches an exclusive Skilled Helper course with [Prof. Gerard Egan → /about/instructors/gerard-egan/], one of the field's most respected voices. In five years, a single Udemy course has grown into a global teaching platform with infrastructure and a faculty of its own.

#### 2019 — Expansion (standard dot)
- **Title:** Diploma in Modern Applied Psychology launched (Achology's flagship course)
- **Description:** The [Diploma in Modern Applied Psychology → /courses/] launches and gains global popularity, offering a structured route through psychological principles, from first theory to practised competence. DiMAP gives the academy its centre of gravity: one flagship course that carries the whole approach and sets its standard.

#### 2020 — Expansion (standard dot)
- **Title:** COVID-19 pandemic accelerated the acceptance of online learning worldwide
- **Description:** The pandemic moves the world's classrooms online, and demand for flexible, remote learning rises sharply as millions seek ways to keep studying. Achology's platform, built for exactly this kind of learning years before it became necessary, demonstrates that it can meet the moment at scale, without loosening the standards it had set.

#### 2021 — Evolution (large dot)
- **Stat:** 350,000 / Students & Active Members Enrolled
- **Title:** Community learning system upgraded, with better tools for discussion and practice
- **Description:** Achology's collaborative learning environment receives significant upgrades, giving students better tools for discussion and practice. Scale arrives in the same season: 350,000 students are now enrolled, and the community becomes the place where what they study is practised with other people.
- **Corrected S364 (Kain's ruling).** This entry said Achology was "recognised with CPD accreditation" from the CPD Standards Office and that its standards were "now independently examined". Kain confirmed the 2021 accreditation happened but was a paid product from a privately owned company that examined and guaranteed nothing, and that Achology is not accredited by it today. The claim was removed so the timeline does not overclaim (PRD criterion 8); the inline link to /accreditation/ went with it. The 2024 SoMAP entry carries the real verification story. Briefed to Code through FROM Chat at S364.

#### 2022 — Evolution (large dot)
- **Stat:** 500,000 / Students & Active Members Enrolled
- **Title:** Half a million students reached worldwide, and the curriculum expands to 25 courses
- **Description:** The student database passes a landmark half-million students as the curriculum expands to 25 courses, including 8 in-depth practitioner-level training programmes designed for those intending to work with others. Taken together, the academy now teaches at almost every level, from a first curiosity about human behaviour through to serious, accountable professional practice.

#### 2023 — Evolution (standard dot)
- **Title:** Launch of Achology version 2 community portal with new 28-course curriculum
- **Description:** An AI-supported, platform-wide upgrade delivers the version 2 community portal and a new 28-course curriculum, the most substantial rebuild the academy has undertaken. The learning experience is reconstructed around the evolving needs of a growing, global membership rather than patched at the edges, with every course reviewed, resequenced and brought into a single coherent structure.

#### 2024 — Community (standard dot)
- **Title:** The Society of Modern Applied Psychology founded, raising integrity standards in the field
- **Description:** Master Achologists found the [Society of Modern Applied Psychology → https://thesomap.org, new tab], an independent body created to raise the standards of training and practice across the field, and to define what competent practice requires. The Society maintains the competency development framework accredited graduates complete. The academy's graduates now hold the profession they trained for to a higher bar than the one they found.

#### 2025 — Community (standard dot)
- **Title:** Achology makes a full migration to Circle.io, finding its permanent online home
- **Description:** Achology completes a full migration to Circle, giving its learning system, its events and its community a single, permanent and properly integrated home after years spread across separate platforms. For the first time, everything the academy does lives in one place, with the functionality needed to scale internationally and the stability to support members through years of study rather than weeks.

#### 2025 / 26 — Community (standard dot)
- **Stat:** 695,578 / Students & Active Members Enrolled
- **Title:** An Eldership team established, and FREE learning is made available to the public
- **Description:** An eldership team of senior Achologists is established to guide the community and safeguard the standards it has built, and [free group discussions and skill events → /free-events/] are opened to the general public, with no membership required. It is the earliest expression of the wider social impact that future generations of Achology graduates will carry into the world, and a statement of what the academy believes learning is for.

### 23.13 Responsive Behaviour

Three breakpoints per DSRD 7 §4.1: mobile (<768px), tablet (768–1023px), desktop (≥1024px).

The layout is single-column-left at every width. What changes across breakpoints is the pinned window, not the milestone layout.

| Breakpoint | Behaviour |
|---|---|
| Desktop (≥1024px) | Window pinned. Height `clamp(260px, calc(100vh - 703px), 510px)` |
| Tablet (768–1023px) | Window pinned. Height `calc(100vh - 674px)` |
| Mobile (<768px) | `.is-flat` applies — the block lies flat as a plain scrolling list, no pin, no window |

Verified at build across all three: desktop 1440, tablet 768, phone 390.

### 23.14 Decision Register

*A log, not the specification: this register records what was decided for this page and when. The operative spec is the section body above — where the two differ, the body governs.*

| # | Decision |
|---|---|
| D1 | The built page supersedes the previously locked structure. The pinned scrolling window, single left spine, dark stage, terminus line and statistics panel replace the centred alternating spine, student enrolment bar, era filter tabs and founder's-letter CTA. Kain's ruling, S213, on the built and approved page of 22 July 2026. |
| D2 | Body text grey throughout the timeline is #5E6B75 (~5.4:1 contrast, passes WCAG AA), not #8A9199 (~3:1, fails). This remains a system-wide brand-palette question — other locked components likely use #8A9199 where #5E6B75 belongs; the text-colour roles in DSRD 7 §1 should be locked and existing components audited before more page templates are built. |
| D3 | **The About page's member story posters and phone step (Kain, Code's S514 sitting, 12 November 2026).** The five posters are re-made with the question along the foot ("Yes, build 3"), the same files as the Testimonials page (§30.4); this closes About list D item 6's re-export. Below 768 every Como part on the page steps one down and the Mulish reading text stays ("Yes, build 2"; DSRD 7 §3.0); the community stages and figure row keep their own exception. |

### 23.15 Source of Truth

The built template is the reference: `page-about.php`, `about.css` and `about.js` in the theme repository. There is no separate prototype file for this component; the design was iterated in `previews/about.html` and extracted into theme files in the same session.

*Production implementation notes for this component/page are in the Production Implementation Notes document.*

### 23.16 The About page redraw is signed and built (Kain, 23 November 2026, "Yes, build it"; built at theme 0.708.397 and 0.708.398; written by Chat, Session 480, from RULING__About_Page_Redraw_Signed_S552, SHIP__About_Page_Redraw_S556 and SHIP__About_Hero_Banner_S544)

Kain was shown the whole redrawn About page in Safari (previews/about-redraw-s544/about.html?opt=1) and said: **"Yes, build it."** His yes covers the page block by block, and the page now runs in this order, which replaces the position this section gives the timeline for the page as a whole (the timeline itself, sections 23.1 to 23.15, stands as the Story block):
1. **The Cream Hero banner with the film.** The course page hero's warm cream band, running to the window's edges with a hairline foot, the breadcrumb inside it; the words on the left and the Achology film (Vimeo 708764177, on Kain's about-intro thumbnail) on the right, with the Academy's faces wall behind it. Kain picked option 1 of four in the Change Viewer on 22 November. The heading is About Achology, with the film's label "So, What Is Achology?" over the picture (his correction: "Just the text. So, What Is Achology? ... That's not an appropriate place to put in a sentence."); the sentence is Chat's, from ANSWER__About_Banner_Words_S544; the button is Read the Achology Story.
2. **The section bar:** Overview, The Story, Five Aspects, The Founders, Ten Ways, FAQs, Where to Begin.
3. **Block 1, "Achology: What It Is, and Who It's For," as Answer Tabs:** one reading column, the chosen tab off-white with a 3 orange bar, with The Thinking that Drives Achology beneath.
4. **The Story,** in the Academy history component (sections 23.1 to 23.15 above and DSRD 8 on the story scroll).
5. **The Five Aspects films** as the school pages' one reviews block (DSRD 8 section 44), its cards alternating film, review, film / review, film, review (Kain's words: "Video review, video review, video review"), two rows shown and the third behind the control.
6. **The founders,** on sand.
7. **Ten Ways as Feature and Nine:** the flagship dark card with the DiMAP picture, then nine cards three by three.
8. **The questions,** three cards of four, the third Recognition and Trust (Chat's ANSWER__About_Questions_Third_Card_S544; the one block, DSRD 8 section 37).
9. **Where Would You Like to Begin?**

Every word is the page's own, carried unchanged. **How it is built.** No markup was retyped: tools/about_page_data.py lifts the signed preview whole into data/about-page/main.json, and page-about.php prints it through about-setup.php, which draws the questions block and Where to Begin from their one homes. **Proved before it shipped:** compare_built.py read every element of all nine blocks on the built page against the signed preview in WebKit at 1440, 1024, 768 and 390 and in every state (each answer tab, the films control, a story chapter, the phone's swipe rows), with 0 differences and identical page heights; the check was shown able to fail. The schema (AboutPage, Organization, BreadcrumbList, VideoObject) is unchanged. The page's Rank Math title, description and focus keyword (post 184) are unchanged; the score is Kain's one-click rescore. **Gate:** page_gate at 0.708.398 read 42 passed, 59 failed, 29 carved out; the fifty-seven lines that are the signed Academy band design read by the old ruled-column rules are answered in ANSWER__Gate_Lines_And_Open_Rulings_S480 section 1 (eleven groups). The one real fault of the page's own, the answer tabs' list items breaking the tab roles for a screen reader, was mended at 0.708.398 with no visible change. One line belongs to the shared reviews block, not to this page: on a phone its row of written reviews scrolls sideways with nothing a keyboard can reach (course-page.js), raised with the main session.


---

## 24. Course Page — Standard Accreditation Block (CONTENT + PLACEMENT CONFIRMED)

**The course page's structure (Kain, Code's S208 sitting, 2 November 2026: "Yes, these ten"; written by Chat, S453):** every course page is ten blocks inside six steps, each answering one visitor question once, and this certificate block is block 8, at the Fit step. The full structure lives in the course page signed spec, section 3b, in the Course Page design folder.

**The course page's later rulings (Kain, Code's course page sittings S208 to S212, 2 to 8 November 2026; written by Chat, S459).** Each is written whole in the course page signed spec, section 3e, and only named here: the hero, signed at theme 0.707.748 ("Yes, signed"), is that spec's design home for block 1; block 2, What You Will Learn, has one purpose, to tell the visitor what they will understand and be able to do by the end and whether the course is for someone like them, in five slots the same on all 28 pages ("Yes, agreed"); the Course Spine, block 3, is signed (pick 188); the six free lessons move after Three Ways to Buy and before the questions ("Yes, after pricing"), and this certificate block still sits directly before Three Ways to Buy; Three Ways to Buy is The Chooser in Dark Summary ("Yes, Dark Summary"); block 6, the students block, is The Voices Wall, Even and Exact ("Yes, Even and Exact"), its figures from DSRD 5 section 1 and its written review counts from the full Udemy export until DSRD 5 carries them; and nothing on the course page links out to the Knowledge Hub (pick 200), whose reach over the home hub line and the authority plan's down links is on the Decisions for Kain list. The page's block spacing, 64, 48 and 32, is DSRD 7 section 4.3 Exception 22. **The pricing block, Three Ways to Buy (Kain, Code's course page sittings S214 to S216, 9 November 2026, picks 236 to 245; written by Chat, S461).** What is ruled: the structure is Three Plans, the course, its school bundle and the Access All Areas Pass (pick 238); the block sits on the brand dark with its faint bubble pattern (picks 240 and 243; DSRD 7 section 3.3a records it); the cards are simple, with no artwork (DSRD 7 section 3.3a); Equal Weight, One Label (no "Best value"), Name Line, Tight Dollar and Even Lists are standard (pick 241), with the trust bar centred and hairlines between its parts (pick 242); **on every course page the school card shows its bought-apart total struck through, computed by DSRD 4 section 1.2's own rule and checked against its stated saving, and each card has a payment chooser between In full and each monthly plan read from that product's checkout** (pick 245, Kain: "Is there a reason why you aren't showing the saving? ... we could have a toggle"). A chosen monthly plan shows the product's DSRD 4 price as its total, never the instalment multiplied (DSRD 4 section 1.1). What is not ruled: the card design itself. Kain rejected the S215 rounds and four new directions from S216 (Three Columns, Course First, The Price List, The Comparison; previews/course-page-s208, pn1 to pn4) wait on his pick; the pick is written here when made. Records: SESSION_REPORT__S214_Course_Page_Pricing_Voices_Wall, RULING__Course_Page_Pricing_Simple_Cards_On_The_Dark_S215 and SESSION_REPORT__S216_Course_Page_Pricing_Four_Directions in the channel.

**The pricing block and the free lessons block are signed (Kain, Code's course page sitting S217, 9 and 10 November 2026; written home by Chat branch, 10 November 2026).** This settles "what is not ruled" in the paragraph above. Each is written whole in the course page signed spec, section 3f, and only named here. **The pricing block** ("Yes, signed", pick 282; picks 246 to 281): Course First (pick 246), on Light Sand (pick 249); one Diploma card, its left half brand dark with a living neuron and the Orange Sweep, its right half the Receipt with the grey-track tabs, the rolling price, the membership box, Due Today, the site's standard main button "Enrol in this Course" and the guarantee pill, and its foot the Edge to Edge strip of plain logos; under it one bundle card of two rows, the school bundle and the Access All Areas Pass, each opening a panel built from the Diploma card's own parts, with the bundle's checkout button and linked course lists. **The free lessons block** ("Yes, signed", pick 289; picks 284 to 288): The Player, after the pricing block and before the questions, with a first name, email and consent box sign-up (DSRD 4 section 5.1, form 6). **The offer placement** (pick 283): no $7 offer on a course page; the closing free lessons band goes and the site footer's top half carries the free lessons invitation on course pages only (DSRD 4 section 8; DSRD 8 section 19). The grey track is DSRD 7 section 5.1's named exception; the block's ground is DSRD 7 section 3.3a's. Both blocks are the standard for all 28 course pages; preview only until the theme build. Records: RULING__Course_Page_Diploma_Card_Segment_Walk_S217 and SESSION_REPORT__S217_Course_Page_Segment_Walk in the channel; every pick in Kain's words is the theme's previews/course-page-s208/PICKS.md.

**The introduction video card and the one reviews block (Kain, Code's S542 and S544 sittings, 20 and 21 November 2026; written by Chat, Session 480).** The card under the course page's introduction film is signed on all 28 course pages (theme 0.708.346): the teaching picture and its play button, with one foot joined under them reading View This Course's Introduction Video on the left and the course's own running time on the right, and no time on the picture, no heading above and no sentence under. Kain: "Yes, foot only", "Yes, all 28", then "Yes, it's signed" on the built card. It is written whole in DSRD 8 section 45, including the phone call Code built, which Kain may overturn: below 768 the foot steps one step down (title 14, time 12) by the site's own phone rule and stays outside the course page's 24 and 16 exception. The students block, block 6, is now the one reviews block of DSRD 8 section 44: two rows show on the course pages, the third sits behind the control Show More Reviews and Videos, and the two link cards Read All Student Reviews and View All Member Testimonials close it ("Yes, two rows", 21 November). Its line is Chat's: "Reviews from students who have taken this course, along with videos of members sharing what they've gained." The look of block 6 is therefore the one block's, replacing The Voices Wall, Even and Exact, while its figures and its review counts stay as ruled above. Course 005 is ruled (Chat, Session 480): its two other bank reviews are read against the review builder's rules; if both pass it draws the one block, and if either fails it keeps the old wall until it has six reviews. Course 005's page does not carry the one block until then.

One standard block, identical across all 28 course pages. Added S186. Carries the recognition and CPD trust content deliberately removed from the nine-question block (S185; DSRD 2 §3.8).

**Shortened to four lines on the course page (Kain's ruling, S320).** The three elements below all stay, stated as briefly as they can honestly be stated: the two certificates, one line saying that buying a course does not confer accredited status, and SoMAP plus the UKRLP registration. The fuller treatment, including the can-and-cannot list the live school page carries well, stays on the school page and the accreditation page. On a page where someone is deciding to buy, a long recognition block stops clearing the objection and starts arguing with the sale.

**Its position changed at S320.** It is now block 7 of nine, and the standalone CPD Journey Context block that used to precede it is retired from the course page, its one necessary line absorbed into element 2 below. The full course-page block order is DSRD 2 §2.6 and the governing record is the agreed shape document in the Course Page design folder. Visual anatomy is designed and locked in DSRD 8 when the course-page build begins; this section fixes content, placement, and behaviour only.

### 24.1 What the Block States (3 Elements, Fixed Order)

1. **The accreditation relationship.** Achology's certification is independently verified by The SoMAP (the Society of Modern Applied Psychology), Achology's third-party accreditation verification partner. Achology is also a UKRLP-registered training provider (PRN 10099815).
2. **The two certificates, stated honestly (corrected S364 on Kain's ruling).** Completing the course earns a Certificate of Course Completion. Completing that course's required skill development sessions as well earns the course's Certificate of Achievement. The Certificate of Achievement is per course; it is not a member level. The member levels (Achologist to Master Achologist) are the accreditation pathway and are explained on the accreditation page. The block never implies the course purchase alone confers accredited status. *Until S364 this element said the Certificate of Achievement was earned through the CPD pathway, progressing from Achologist to Master Achologist; Kain ruled that wrong.*
3. **Routes out.** One primary internal link to `https://achology.com/accreditation/` (the full pathway explanation); one secondary external link to `https://thesomap.org` (opens in a new tab, per the site-wide external-link standard, DSRD 3).

### 24.2 Placement

**Superseded S320.** It previously sat between the CPD Journey Context block and the Three-Tier Pricing Comparison block. Under the nine-block course page it is **block 7**, sitting between Members Talking (block 6) and Three Ways To Buy (block 8), so it still completes the recognition story immediately before the page's final decision point. The CPD Journey Context block no longer exists on this page.

### 24.3 Standardisation

Identical on all 28 course pages: same wording, same links, no per-course variation. Copy is written once at the course-page copy stage to house-copy-standards (base voice, no em-dashes); any change is a single-source change applied site-wide.

### 24.4 Source References

Decision: S185 (DSRD 2 §3.8). SoMAP name and role: PRD criterion 6; DSRD 9 §23.12. Certification routes: DSRD 2 §2.16. UKRLP PRN 10099815: DSRD 2 §2.16 / DSRD 3 schema table.

---

## 25. Quiet Text-Led Pages — Reading Column Rule (LOCKED, Kain 2026-07-16; amended S281)

Every quiet text-led page (the seven legal policies, the policies index, /about/code-of-ethics/, /about/manifesto/, and any future calm reading page) places ALL of its content — page header, body, closing panels, and the breadcrumb — inside its reading column, centred within the 1200px page container. **The breadcrumb is not an exception, per §27 as corrected at S337 on Kain's S090 ruling.** This paragraph named it as the exception and put it at the 1200px frame until then.

**Which reading column, resolved S085.** This section read "the 880px article column" for all ten of these pages until S281, when it was amended to record the 620px prose column Kain ruled at Claude Code's S062 for seven of the ten. **Kain retired that column at S085: all ten pages on this template use the 880px reading column.** The question of which seven he had named is closed with it, and nothing is owed from Code on that list. §27 holds the ruling, and the reason the 620px column is recorded there rather than deleted.

**The alignment consequence, stated so it is a decision and not an accident:** the header and footer chrome (logos, nav) sit at the 1200px page container's edge; the reading column is centred and narrower, so the content's left edge does NOT align with the logos. This is by design — reading comfort owns the column, the chrome owns the frame. Content never chases the chrome edge, and no page may left-align its reading column to the logo.

Template mechanics: `page-container > article-container` (template-policy.php, single-faq_article.php and siblings). Nothing about this rule is per-page; a page either is a quiet text-led page and uses the column, or it is not.

**The founder pages' picks, one round at a time (Kain, Code's S181 founder pages sitting, 26 and 27 October 2026; on the build site at 0.707.597 to 0.707.616; written by Chat, S447).** The founder pages are the Manifesto, the Code of Ethics and the Founders' Letter. Each pick was shown alone in the shared Change Viewer, Before and After; his words for each are in previews/founder-touches-s181/PICKS.md in the theme.
1. **Reading Size** ("Yes, option 1, Reading Size."; 0.707.601): the writing 18 on 1.75; the opening line 21 on 1.55 from 768, 18 on a phone.
2. **The reading line** ("Yes, switch the reading line on for the founder pages."; 0.707.597): the site's one reading line, the Knowledge Hub line (DSRD 8, the reading line, and COMPONENT_REGISTRY.md).
3. **The Thin Edge on Related Questions** ("Yes, give the founder pages' Related Questions the Thin Edge."; 0.707.606): the founder pages join the site's one question edge in help.css.
4. **Lists one size smaller than the writing** (Kain to Code's S184 main session: "make that smaller text without thinking"): list items 16 on 1.7.
5. **The opening, Buttons Under the Words** ("Yes, option 3, Buttons Under the Words."; 0.707.616), on the Manifesto and the Code of Ethics only. From 1024 the handbook no longer floats over the first section. The opening is a grid: the title, date and opening line on the left with the handbook's buttons under them; a 208 wide handbook on the right; the opening's line running the full width under both; then the first section at full width, its heading on one line. Below 1024 nothing changes. DSRD 7 section 4.3 Exception 2 no longer covers these two pages.

**The statue pinned, and the Code of Character bar moved up (Kain, Code's S185 theme session, 27 October 2026; on the build site at 0.707.618; written by Chat, S447).** Kain: "Number 2 above the heading. So I think that's fine for the manifesto page." On the Code of Ethics: "we need the code of character and conduct gray block moved up above to code's two layers of integrity", with the statue "better placed behind the principles that shape the standards"; on the result, "This is really good, Claude." On a computer only (the statue stays hidden below 1024), the Aristotle bust is pinned behind one section of each page, its bottom right corner at the section's right edge, its base 48 behind the top of the section's closing grey panel, its top 32 above the section's line, at 9% with soft faded edges (DSRD 8 section 12.4 carries the values). On the Code of Ethics the Code of Character and Conduct bar now closes "The Principles That Shape the Standards", above "Two Codes, Two Layers of Integrity", and that section hosts the statue; the old host at the foot ("An Ethical Framework...") keeps its line and has no bust; no word changed, template-policy.php changes the order. On the Manifesto the host is unchanged ("Our Commitment to the Code of Ethical Practice"), with the new placement. Spacing re-checked on the build site: page_gate's 32 spacing lines pass. Code owes the prototype export at sign-off.

**The founder pages' later picks (Kain, Code's S186 and S188 theme sessions, 27 October 2026; on the build site at 0.707.619 to 0.707.635; written by Chat, S449).** Each was shown as four rendered options, or as a row on one board, and Kain's words are in the theme session's channel rulings.
1. **No table of contents, in any form** (round 10): "No, take the table of contents out. It is not appropriate for these pages." The founder pages are information pages, not articles.
2. **One warm cream section on each page** (round 11; 0.707.619): "yes warm cream ... just have one block on that page." It sits behind the writing's second section, or its first plain section where the second holds a grey box: Founders' Letter "How Achology Actually Began", Manifesto "What the Manifesto Is and Why It Matters", Code of Ethics "Two Codes, Two Layers of Integrity". Never behind a grey box, the statue, the signature or the closing panel. policies.css section 14. On the Manifesto the opening's hairline goes (0.707.620).
3. **A heading tile before every section heading** (round 12; 0.707.621): the Related Questions tile with an icon, the icon's left edge on the column edge and the tile reaching 9 past it. The icon is matched by words in the heading in template-policy.php; a heading with no match has no tile. policies.css section 15.
4. **The pages close on More About Achology** (round 14; 0.707.622 to 0.707.624): the warm cream Where Next panel with the bubble, four cards, the page in hand left out. Heading "More About Achology" and subtitle "Read more about who we are, what we stand for and the people who learn with us." are Kain's approved words. The card words are the About page's own. Related Questions, the "Ready to Start Training as an Achologist?" box and the white cards' icons are gone, so pick 3 of the S181 list above (the Thin Edge on Related Questions) no longer applies. policies.css sections 16 and 17.
5. **The words went through the Content Standard** (Kain's yes, S186): Chat rewrote them, Kain signed all three on one page at S448, and Code placed them at 0.707.626 with no word changed. On the Founders' Letter the callout sits before the first section's second paragraph (0.707.627 to 0.707.630).
6. **The Code of Ethics training's six topics are numbered** (round 15; 0.707.631): "Yes, option 2, Numbered." Numbers 01 to 06 in the house orange, two columns from 768, one on a phone. policies.css section 19.
7. **The S188 board's eight yeses** (0.707.632 to 0.707.635): the Rogers quote in the full-width quote panel directly under "The Principles That Shape the Standards"; the Letter's sign-off as the compact signature card with Kain's own photograph cropped to both founders' faces and brightened; every box 48 from the words around it where no hairline stands between; no heading, opening line, topic name or card line ending on one word alone; the Manifesto title folding on a phone; the founders' photograph at full strength under the opening on a phone; the handbook and its buttons at full column width on a phone; the More About Achology cards lined up along their tops. Rows 4 and 8 would suit every Where Next panel and heading site-wide; that reach is put to Kain when the shared parts are reviewed.
8. **The Founders' Letter carries no quote callout** (rounds 16 and 17; 0.707.639): "Take it out, delete it, remove it, let it be gone forever." Its signed line ("Nobody can grow on another person's behalf ...") is struck from the Letter's copy. Never proposed again. The quote panel stays for the Code of Ethics' Rogers quote.
9. **The More About Achology cards say more** (0.707.641; Kain: "Those are absolutely perfect"): Achology's Code of Ethics, "The unconventional Code of Ethics training at the heart of our accreditation process"; Member Testimonials, "Hear directly from the students and members who have learned and grown with Achology"; The Achology Certification Pathway, "How to become certified with Achology, step by step through our five-level pathway" (five levels, as REF 1 section 3 holds). The Manifesto, Founders' Letter and Watch the Training cards keep their words. Only this panel changed; the About page's cards and the header's navigation cards are unchanged.
10. **The Founders' Letter photograph stands 256 wide on a computer** (round 18, "Option 1, Smaller Photo."; 0.707.647), so it ends level with the line under the opening words and the first heading sits 48 below it. The About page keeps 320.
11. **One Code of Ethics paragraph is Kain's own words** (0.707.651), under "What the Framework Is and Why It Matters": "Members are encouraged to read the Ethical Framework for Skilled Helpers and Practitioners of Applied Psychology regularly and know it well before working with anyone. A standard you live by each day serves you better than one you consult only after something has gone wrong."

**One board for a whole-page review (Kain, S186 and S188, 27 October 2026).** When every remaining improvement on a page is found at once, it comes to Kain as one board in the shared Change Viewer: one row per visible improvement, each with a plain sentence, Before and After on the real page, and three answers, Yes, No and Show me options. A row marked Show me options goes back to the four-option round. Dead code and stylesheet tidying are proved by machine and never put to him. Kain: "Yes, please go ahead."

**Still open on the founder pages:** the site-wide Rank Math rescore (the Letter read 84 and the Code of Ethics 89, from the editor, before the new words could count), Kain's sign-off of the three pages, and Code's design folder export of the picks.

**The legal policy pages take six rulings (Kain, Code's S203 theme main session, 1 and 2 November 2026; on the build site at 0.707.685 to 0.707.702; written by Chat, S452).** Kain made the Privacy Policy the exemplar for every legal policy page, and Code named six improvements that could reach them all. The eight pages on the policy template that these rulings reach are the Privacy Policy, Terms and Conditions, Cookie Policy, Refund Policy, Trust Statement, Disclaimers, Accessibility Statement and How We Write. The three founder pages do not take them. Each was shown in the shared Change Viewer as four rendered options, and his words are in the theme session's channel rulings.
1. **The writing is 18** ("Yes, 18"; 0.707.685), after a Before and After on the Cookie, Refund and Trust pages. The writing on every page of the policy template is 18 on 1.75, as the founder pages (Reading Size, item 1 above); lists stay 16; headings, tables, quotes and the endnote are unchanged. The rule is scoped to the template by the class `policy-page--doc` on its main, so the About, Reviews, Testimonials and 404 pages, which share the family's styles, do not move.
2. **The sections are listed under the opening** ("2 List under opening"; 0.707.696, 0.707.697, corrected at 0.707.700 and 0.707.701). Of Side Panel, List Under the Opening, Pinned Bar and Number Rail he chose the second. Under the opening stands "On This Page" in the article page's Table of Contents look (knowledge-hub.css `.kh-aside`, loaded on these pages), on the warm cream, one entry per section heading, two columns from 768. Each entry jumps to its section and lands clear of the menu. The list is built from each page's own headings, so no list is typed by hand, and a page with under four headings carries none. The founder pages carry none (their own ruling, item 1 of their later picks above). Corrected the same sitting after Kain said "it's kind of pushed too far in": the article panel's marker slot, link inset and reading track are removed, so the section names start under the heading and both columns read alike; from 1040 the cream box bleeds 32 each side with 32 inside, the inset panel of DSRD 7 section 4.4, so its label, heading and first column sit on the page's left edge; below 1040 the box is flush. Read on the build site: Privacy 20 entries, Terms 15, Cookie 9, Refund 14, Trust 8, Disclaimers 15, Accessibility 10, How We Write 9.
3. **The reading line and the back-to-top circle** ("Line and Circle"; 0.707.698). Of Line and Circle, Line Only, Circle on a Phone and Back to the List he chose the first. The site's one reading line (reading-line.js, Kain S147 and S181) runs along the menu's foot and fills as the page is read, now on every page of the policy template. The About page's orange back-to-top circle (Kain S237) shows at every width once the reader is past the On This Page list, gliding to the top (jumping for a reader who asks for less motion). The circle's rules live in one home, components.css; the About page keeps only its own phone rule.
4. **Ruled Sections** ("Ruled Sections"; 0.707.699). Of Ruled Sections, Numbers in Tiles, Ruled and Tiled and Orange Edge he chose the first. Every policy page that lists its sections rules them with the family's own section line (policies.css `.policy-body--ruled`, as the founder pages and the Policies index carry it): a hairline between numbered sections with 48 above and 48 below, 32 on a phone (DSRD 7 section 4.3). The rule also learns that a table can close a section, as the Privacy Policy's lawful basis table does. The founder pages are unchanged.
5. **The pages close on Other Policies, Where Next Cards** ("Where Next Cards please"; 0.707.702). Of Index Cards, Where Next Cards (Code's recommendation), Link Chips and Previous and Next he chose the second, then: "apply the same design rules as what you've applied to policy navigation panel on the top ... in terms of how the thing's positioned on the page". At the foot of every page that lists its sections stands the site's Where Next panel (`achology_routes_grid`, two across in its soft box, no icons, tops level as on the founder pages) under the heading "Other Policies", confirmed by Chat as the final words. It holds the other legal policies, each card the Policies index's own row and signed line (`achology_policy_index_rows()`), less the page in hand and How We Write; the How We Write page shows all seven. It is placed as the On This Page panel is: from 1040 the box reaches 32 out each side so its heading and the cards' left edge sit on the page's left edge, and below 1040 it is flush. Links stay in the same tab. Read on the build site: Privacy shows the six others, Refund six without itself, How We Write all seven.
6. **The Rank Math exception on five pages** ("yes"). On /policies/, Cookie, Refund, Trust Statement and Accessibility Statement the two content tests that Kain already set aside for articles at S449 (content length and pictures in the content) are set aside, and the other tests pass in full. The rule is written in DSRD 6 chapter 5, item 11.

7. **The pages close on the Question Panel** ("1 please - this looks good"; 0.707.703, `template-policy.php` and `policies.css`). From four closes Kain chose the Question Panel, then asked for it to be designed rather than dropped in. From four designs (Side by Side, Code's recommendation; White Card; Dark Band; Orange Edge) he chose the first. The page's own closing line is split in two: "Questions about this policy?" is the heading, and "Get in touch with our support team and we'll be glad to help." is the line beneath it. It carries "Get in Touch" to /help/ as the site's orange button, in the warm cream panel with a soft orange speech tile. It sits side by side from 768 and stacked on a phone, placed as the On This Page and Other Policies panels are. It replaces the plain closing line on every page that lists its sections, while a page whose partial sets its own closing line keeps that line. Read on the build site on all eight legal pages.

**Signed off (Kain, Code's S203, 2 November 2026).** After the sign-off checks and a look in Safari, Kain said "I'm 100% happy with these pages" of all eight. Code fixed one fault on the way, at 0.707.704 and 0.707.705: Other Policies now takes the ruled-section rule (hairline, 48 above and below, 32 on a phone), and the three panels share one inside measure.

**Not yet ruled.** One of the improvements remains, built once for all eight pages: the "In short" box. Its words are Chat's, three or four plain lines per page on what the policy means for the reader, and they come to Kain on the page.

---

## 26. Header-to-Content Spacing Rule — SITE-WIDE (LOCKED, Kain 2026-07-16)

The first content row of EVERY page (the breadcrumb where one exists, otherwise the page's first element) sits exactly **48px (`--sp-2xl`) below the site header** on desktop and tablet, easing to **32px (`--sp-xl`) below 768px**. No page invents its own value.

This generalises the spacing already locked for the Knowledge Hub (§20.2, §22.3) to every page type. Aligned on 2026-07-16, when an audit found four different values in production CSS:

| Page type | Was | Now |
|-----------|-----|-----|
| Knowledge Hub (hub, listing, article) | 48px (locked) | 48px — unchanged, the reference value |
| Policy template (7 legal pages, index, quiet about-pages) | 64px | 48px (policies.css §1) |
| /help/ (landing, category, article) | 32px | 48px (help.css) |
| Author profiles (.ap-crumb) | 44px (magic number) | 48px (people.css) |

Mechanics vary per template (page padding vs breadcrumb margin) — the RESULT is what is locked: 48/32 from header bottom to first content row. Any new page type inherits this rule on arrival.

**Recorded exception, S423 (Chat, from Code's S163 page gate run; Kain may overturn): the Soft Light hero on the article, book note and quote page (§22.15).** The gate's breadcrumb-below line (48 to the next thing) does not apply to these heroes. On the desktop the picture or cover's top meets the breadcrumb's foot (the roof Kain locked at S161), and the gap from the breadcrumb to the title is 48. On a tablet and phone the picture row sits between the breadcrumb and the title. The top space above the breadcrumb is still 48 on desktop and tablet. The workbook thank-you page carries the same kind of carve-out (Kain, S160).

---

## 27. Page Width Rule — Reading Column vs Showcase Frame (LOCKED, Kain 2026-07-16; third width added S062, corrected S281; third width retired by Kain S085)

**AMENDED S386: the reading column is 800px, not 880px.** The token `--container-article` has been 800 since the article page sitting at Code's S112, and every page built on it, articles and all policy pages included, renders at 800. Kain ruled at Code's S135, asking for one standard for every policy page decided by eye and never revisited: "Yes, 800 for all policy pages is settled for good." The build was right and this section was wrong. **Wherever this section says the reading column is 880px, read 800px.** The sentence test, the two-width rule and the showcase frame at 1200px are unchanged. The page gate (`page_gate.py`, `CONTENT_WIDTHS`) accepts 800.

**AMENDED S423: a third page container, 1080, for the Knowledge Hub reading pages.** Kain approved the 984 content frame at Code's S161 and S162 sittings ("I 100 per cent approve the container width"): the article, book note and quote page sit in a 984 frame (reading column 680 at 18, a 48 gap, side panel 256), inside a 1080 page container (984 plus two 48 gutters). This is his ruling on rendered pages, which is the only way this section allows a new width. It governs those three page types and the workbook page when built; every other reading page keeps 800. The page gate's `CONTENT_WIDTHS` takes 1080 (Code, from FROM Chat at S423). See §22.15.

**The one edge (Kain, Code's S161 sitting, 13 October 2026; written S438).** Kain's words: "All text on the entire page must rest up against one line ... Text cannot on any page in this knowledge hub or any page in this site ever align up against two different columns or two different container edges." Measured on the deployed article at 1440: the logo, breadcrumb, titles and writing start at one left edge and the content and the Sign In button end at one right edge, so the site holds one frame. Every page and every future build is held to it: a band, panel or block that narrows the words to a second edge breaks this rule, and the 984 frame above was chosen so the one edge holds in every option. The header and footer never change; only the content takes the frame.

The site has **two page content widths**, and one test decides which a block gets: **if it is sentences, it sits in the 880px reading column; if it is cards or imagery, it uses the full 1200px frame (`--container-page`).**

**880 is the container width for every content page on the site, and it is not put to Kain again.** Ruled by him at Claude Code's S085, in session, on the rendered book note sitting, choosing Route C. His words: "we must have consistency across all knowledge hub article pages ... container width cannot be questioned again across the other quote and workbook pages that we havent worked on yet ... 880 is the standard, exactly the same as what the help articles and policy pages should be." That covers every template not yet built, the quote page and the workbook page included: they are specified and built at 880 from the start, and width is never offered as a page-level choice. A third width does not return by judgement, and no builder reopens this.

| Width | Token | What uses it |
|---|---|---|
| 1200px | `--container-page` | The showcase frame: card grids, imagery, and page chrome. **Not the breadcrumb:** the trail aligns with its own page's leading edge, which is the content column on every page (the hero case retired: the book note at S102, the article at S110; see the bullet below) |
| 880px | `--container-article` | The standard reading column: Knowledge Hub articles, /help/ articles and category pages, the quiet about-pages |
| 960px | `--container-article`, reset on the page | A page-level reset, not a third site-wide width (added by Chat, S461, on Code's S464 gate record): Our People and the author pages (§33.5), Reviews, About and Testimonials, and the pathway page /certification/ (Kain, S464, "Yes, build 960"), banner included. /accreditation/ shares certification.css but not its frame: its width is Kain's to rule when it is designed. The page gate's `CONTENT_WIDTHS` takes 960 for these pages |

**The 620px prose column is superseded, and it was not an accident.** Kain ruled it at Claude Code's S062, in Safari, on four rendered options, for seven of the ten pages on the policy template, and it was a readability standard for the densest prose on the site. His S085 ruling retires it: those seven pages move to 880px, which makes their lines about forty per cent longer. It is recorded here rather than deleted for two reasons: so a reader meeting 620 in an old file or an unswept stylesheet knows what it was and that it no longer governs, and so the change reads as a decision Kain took rather than a fault being corrected. Code shows him one policy page at 880 on the rendered page before sweeping all seven, which is the normal practice for a visible change and not a reopening.

**`--container-quote` (540px) is not a page width.** It is the text measure inside the featured quote card, a component value that happens to be registered in `base.css` beside the page containers. It is named here only so a future reader counting tokens does not mistake it for a fourth page width.

**The correction made at S281, and why it was needed.** This section read "exactly two content widths" and "no third width may be introduced" until S281. That was true when written and stopped being true at S062, when Kain ruled the 620px prose column by eye. The document had not caught up with a decision he had already made properly, which is the only kind of contradiction worth fixing quietly: nothing about the site was wrong, only the record of it. The absolute prohibition is replaced by the real rule, which is that a new width is his ruling on rendered options and never a builder's judgement. **S085 closes the sequence:** Kain retired the 620px column himself, so the site is back to two content widths, this time by his ruling rather than by a document's assumption.

- **Reading pages** — /help/ articles, /help/ category pages (a question list is text you read), the seven legal policies, the policies index, the quiet about-pages, Knowledge Hub articles: header, body and lists live in the page's 880px reading column (§25 mechanics: `page-container > article-container`). **The breadcrumb is not an exception to the frame rule and never was, and it has two cases.** Where a page has no hero block, the trail **aligns with that page's own content column**: measured by Code at S090 on the Privacy Policy at 1280 (left 330, width 620, matching the writing beneath it) and on the Policies index, About and Reviews at 1440 (all left 280, width 880, all matching). **Where a page carries a hero block the trail sits inside it, on the same content column: the book note since Code's S102 (§32.2), the article since S110 (§22.3). The 1104 case is retired on both, so the trail aligns with the content column on every page, and there is one case, not two.** **The content column itself is 800 from Kain's S111 ruling (DSRD 7 §4.1), and every 880 written in this document as the reading column is read as 800 from S357; the number in the older lines is the record of what stood when they were written.** *The retired text, kept as the record:* where a page carried the ruled hero block, the trail sat on it, at 1104px, aligned with the logo (Kain, S085 ruling 4; approved on the rendered page at three widths at Code's S096), which was the article page and the book note page. **In neither case is it at the 1200px page frame.** Kain ruled it at S090 in his own words: "yes, it holds, please correct the document." **This bullet, and several other sentences in this document, said the trail was the exception on every page type and sat at the 1200px frame.** That reading was written at S281 to resolve an apparent conflict and it resolved it the wrong way: the build never did it on any page. Corrected S337. What makes each page read as one column is exactly this alignment, and on the two hero pages the thing it aligns to is the hero block rather than the reading.
- **Showcase pages** — card-grid pages such as the /help/ landing, the Learn hub grids, course/bundle card layouts: the grid and its chrome use the 1200px frame. Centred hero TEXT on these pages still reads at the column width (880px), because it is sentences.
  - **Our People was listed here until S300 and is not a showcase page.** The built and approved page sits in a reading column, and the sentence test agrees with the build: the page is biographies. **Corrected S398: that column is 960px on this page, a page-level token reset ruled by Kain by eye at Code's S145, matching Reviews, About and Testimonials (§33.5); it is not the 800 standard reading column and not a third site-wide width.** Its card sections are two-across *inside* the column, not a frame-width grid (§33.5, §33.8). Corrected when §33 was written from the built page; the page itself never changed.
  - **The Certification page (/certification/) sits in the same 960 frame, banner included (Kain, S464, 8 November 2026, in Code's sitting; written by Chat, S459).** Its signed S364 spec set the 800 reading column; the new banner's certificates ran past it, and the wider banner frame had been a builder's unasked call. Put to him as a choice, Kain said "Yes, build 960", built as one page-level reset of the reading-column token, as people.css does for Our People, at theme 0.707.821. Measured on the build site at 1268, 1024, 834 and 390: the banner, the cards, the questions and the trial panel share both edges at every width. Like Our People, it is a page-level reset, not a third site-wide width. A page's frame is Kain's decision, put to him as a choice, never set by a builder in passing. Record: RULING__Certification_Page_Frame_Is_960_S464 in the channel Archive.
- **Closing CTA panels** (`.help-contact` and kin) share the width of the page they close (amended same day, Kain 2026-07-16): the reading column on reading pages (/help/ articles and category pages), the full frame on showcase pages (the /help/ landing).

Aligned on 2026-07-16, when an audit found three widths in production:

| Block | Was | Now |
|-------|-----|-----|
| /help/ article, policies, about-pages | 880px (locked, §25) | 880px — unchanged, the reference |
| /help/ category page (breadcrumb, hero, question list) | 1200px frame | 880px column (taxonomy-faq_category.php) |
| `.help-hero` centred text (landing + category) | 820px one-off | 880px column (help.css) |

The round-7 locked alignment survives by construction: category-page list rows keep their left edge on the breadcrumb ruler line, because breadcrumb and list moved into the column together. Clicking from a category page into an article no longer shifts the text edge. Any new template applies the sentence test on arrival; theme v0.29.0.

---

## 28. 404 Page Layout (STRUCTURE LOCKED)

The 404 page serves any URL matching nothing. It is a wayfinding page, not an error page (Kain, 2026-07-19): its job is to route a lost visitor onward, so nothing on it announces a fault. It is built from four elements stacked vertically in the reading column — breadcrumb, page header, a six-door "Where next?" panel, and a Popular Questions block — and nothing follows them but the footer.

**Lock status note:** This section describes the page as built in `404.php` at theme v0.35.x. Structural anatomy, copy, the six doors and their destinations, the two deliberate absences, and the three scoped styling rules are LOCKED. The Popular Questions source is ruled at §28.8 (live query, S247); the build fix is with Claude Code.

### 28.1 Frame and Inherited Styling

The page has **no stylesheet of its own**, no inline `<style>` block, and no `style` attribute anywhere. It borrows two stylesheets.

- **Root element:** `<main id="main" class="policy-page policy-page--404">` → `.page-container` → `.article-container` (the 880px reading column, per §25 and §27)
- **From `policies.css`:** the whole `.policy-page` frame — §1 shell, §2 breadcrumb, §3 header, §9 "Where next?" rows — plus a §12 block scoped to `.policy-page--404`
- **From `help.css`:** the question-door component
- **Watermark:** the 420px three-bubble mark, attached by `components.css` §3 to `.policy-header::before` (per DSRD 7 §14.1)
- **Icons:** Lucide, stroke 1.75, from the registry in DSRD 7 §5.2 — House, Compass, GraduationCap, BookOpen, LibraryBig, Tag, ChevronRight, CircleQuestionMark

### 28.2 Breadcrumb

Two items, per DSRD 1 §9.

- A link to the home page whose content is the Lucide House icon, `aria-label="Home"`
- A ChevronRight separator, `aria-hidden="true"`
- Current-page text, plain, not a link: **"Page not found"**

### 28.3 Page Header

Three stacked lines. This element hosts the bubble watermark.

- **Overline:** "Find your way"
- **H1:** "Oops! You're on a page that no longer exists."
- **Lead:** "Don't worry! We want to help you find what you're here for. Whatever led you to this page, and wherever you were headed, getting access to all of Achology is just a click away. Everything else is where it should be."

### 28.4 "Where next?" — Six Doors

A heading, a lead line, then six full-width link rows using the `.policy-next` component (`policies.css` §9). Each row is an icon on the left, a two-line text block — bold name over grey description — and a ChevronRight on the right. Rows are driven by a `$ach_doors` array; every href is built with `home_url()`.

- **H2:** "Where to instead?"
- **Lead:** "Here are some popular pages that people visit."

| # | Name | Description | Links to | Icon |
|---|---|---|---|---|
| 1 | Go to the homepage | Start from the front door | `/` | House |
| 2 | Learn about Achology | Who we are and what we stand for | `/about/` | Compass |
| 3 | Explore Achology's schools | Seven schools of applied psychology | `/academy/` (was `/academy/schools/` until Kain's ruling of 16 November 2026, section 45) | GraduationCap |
| 4 | Browse Achology's courses | All 28 courses in one place | `/courses/` | BookOpen |
| 5 | Browse the Knowledge Hub | Articles, book notes, quotes and workbooks | `/learn/` | LibraryBig |
| 6 | Explore Achology pricing | What membership includes, and what it costs | `/pricing/` | Tag |

### 28.5 Popular Questions

The `/help/` popular block (`help.css`), reused wholesale. A header row of a circular badge holding a CircleQuestionMark glyph beside an H2, then four question rows — bold question title over a one-line grey excerpt, each with a ChevronRight.

- **H2:** "Popular Questions"

| # | Question | Excerpt | Links to |
|---|---|---|---|
| 1 | Where should I start with Achology? | Where you start depends on your situation and goals. | `/help/getting-started/where-should-i-start-with-achology/` |
| 2 | What makes Achology different from other online learning platforms? | Courses sit inside a live community, so skills are practised with real people. | `/help/achology-basics-and-identity/what-makes-achology-different/` |
| 3 | What are the seven schools of Achology? | Seven learning paths, one for each tradition of applied psychology. | `/help/achology-basics-and-identity/seven-schools-of-achology/` |
| 4 | Do I need prior qualifications to study at Achology? | No prior qualifications, psychology credentials, or academic background are required. | `/help/getting-started/prior-qualifications-needed-achology/` |

**Nothing follows this block** — no search box, no closing CTA, no images beyond the CSS watermark. Then the footer.

### 28.6 Scoped Styling Rules

Three rules only, all in `policies.css` §12, all scoped to `.policy-page--404`. Everything else is inherited unchanged.

| # | Rule | Why |
|---|---|---|
| 1 | `.policy-next { margin-top: 0; }` | Zeroes the panel's own 64px so the header's 48px governs |
| 2 | `.policy-header { padding-bottom: 43px; }` | An optical correction: a box-true 48px reads as roughly 53px against the panel's exact 48px below. 43px of padding puts the ink-to-line distance at 48px. Not a drifted token — 404 only |
| 3 | `.help-popular` gets 48px top margin, a 1px hairline top border and 48px top padding | The about-pages' scoped separator never reaches this block |

### 28.7 Two Deliberate Absences

Both are locked, and both are documented in the template itself.

**No search box.** The theme has no search template, so a search would land on the `index.php` fallback — a worse dead end than this page. This absence stands until a search template exists; when one is built, revisit this section rather than adding a box ad hoc.

**No "404" or "error" wording in visible copy.** Nothing on the page reads as the site being broken. Those strings appear only in the docblock and the class name. This is what "wayfinding page, not an error page" means in practice, and it governs any future copy change here.

### 28.8 Popular Questions Source (RULED S247)

The four questions in §28.5 were hardcoded at v0.35.x, with nothing in the template marking them as provisional. This is the pattern the `/help/` landing decision of 2026-07-03 explicitly rejected, because re-slugged articles leave baked links rotting; the sibling template `archive-faq_article.php` follows that decision correctly with a live query.

**Ruled (Kain, S247): the block is served by the same live query the `/help/` landing uses.** The four hardcoded links are removed and the questions are picked up automatically, per the 2026-07-03 decision. The provisional-marking fallback considered at S213 is dropped. The fix travels to Claude Code in the S247 brief. The block's visual layout is locked and does not change.

### 28.9 The search field under the lead (Code's S180 theme session, 25 October 2026; theme 0.707.499 and 0.707.500; written by Chat, S445)

Built to part 5 of BRIEF__Build_The_Site_Search_Results_Page_To_DSRD_9_Section_38_S375. The search results page's own field, the DSRD 7 section 5.5 control at 44 high, sits under the page header's lead, 24 below it. It carries the approved words "Search the Knowledge Hub" and "Search". The page loads only the field's stylesheet. Because a field now ends the header, the header's 43px optical correction (section 28.6, rule 2), made for the lead's text ink, is gone and the header is back to the 48 token (0.707.500). Measured: 48 above and below the line on a computer and a tablet. The search template now exists (section 38), so section 28.7's first absence and the words "no search box" in section 28.5 are superseded by this section, and the lock note at the head of this section no longer covers that absence. Open for review, not changed: on a phone the page keeps 48 where DSRD 7 section 4.3 says 32, as it did before this change, because the page's own stylesheet scopes the phone tier past the 404.

*Production implementation notes for this page are in the Production Implementation Notes document.*

---

## 29. Reviews Page Layout (APPROVED AND BUILT, Kain by eye, Code S053)

The reviews page is the written record: the 4,517 curated written reviews held in the Notion Review Bank and shipped in-theme as `data/reviews.csv.php`. One page, one instance, live at /reviews/. It is **not** the testimonials page (§30), which carries prerecorded member video.

Composed at S221 through `page-composition`, against the Document-Level Standards above; then designed live in Safari with Claude Code and approved whole by Kain on the live page (Code S053, theme v0.55.1): "this page is absolutely perfect." The signed record is the frozen approved page with the page spec beside it, both in the Verified Student Reviews Page folder under Proof + Funnel Design Prototypes; where that record and this section disagree, the record is correct and this section is the thing to fix. Approved is not done: the DSRD 6 gate, the schema decision and the Rank Math metadata remain with Code (§29.7). Rewritten S262 from the S053 page spec.

---

### 29.1 The job

**This page exists to get a prospective student who is checking Achology out to carry on to the course or school they were already considering.**

One action, one reader. The action is *continue to the course or school page* — not *buy*. The reviews page removes doubt; the course page closes.

**Subordinate job:** to be the page that answers "is Achology any good" for search engines and AI assistants. This adds requirements — real indexable review text, depth, and per-review markup — but it never reorders the page. Where the two jobs would disagree on order, the primary job decides.

---

### 29.2 The reader's arrival state

Built from the reviewers' own language across the 4,517-row review set. Percentages are of that set. Assumptions are labelled as assumptions, per the composition standard.

| # | What is true on arrival | Basis |
|---|---|---|
| A1 | They are mid-decision, not browsing — they searched "Achology reviews" or followed a link from a course or pricing page | **Assumption.** No analytics exist for a page not yet built. Confirmed after launch from Search Console query data |
| A2 | Many have no psychology background and describe themselves as beginners | Evidenced — beginner and "new to this" language recurs across the set |
| A3 | Many are weighing Achology against other courses they have already taken | Evidenced — 148 reviews (3.3%) explicitly compare against other courses or training |
| A4 | A large share want to help other people professionally — coaching, counselling, helping | Evidenced — the largest outcome theme in the set at 671 reviews (14.9%) |
| A5 | Some are testing this against formal academic study | Evidenced — 95 reviews (2.1%) reference university, degree, accreditation or formal training |
| A6 | Some already know the courses from Udemy | Evidenced — 60 reviews (1.3%) name Udemy directly |
| A7 | They doubt an online, self-paced psychology training is legitimate | **Assumption — the weakest-evidenced line here, and deliberately marked.** Every review is written by someone who already bought, so the doubting non-buyer is absent from this evidence by definition. Confirmed only from support questions or a live exit survey |

---

### 29.3 The required state, as changes

Each change is one sentence in the reader's voice. This list is the page's entire content brief.

| # | Change |
|---|---|
| C1 | "I now know this is a large body of review, not a handful." |
| C2 | "I now know it stretches back over a decade, so this isn't a recent push." |
| C3 | "I now know these are people all over the world, not one small pocket." |
| C4 | "I now believe these are real students, because I can see names, dates, courses and criticism." |
| C5 | "I now know I can narrow this down to the thing I actually care about." |
| C6 | "I now know what people with my concern actually said." |
| C7 | "I no longer worry the good reviews were hand-picked, because I can read the critical ones." |
| C8 | "I now know I can check any of this myself rather than take a summary on trust." |
| C9 | "I now know exactly where to go next." |

**Completeness check run:** the routing/teaching check (five questions — where am I, what is here, is this the right place for me, why should I trust it, where do I go next). This page routes and evidences; it does not sell, so the four selling frameworks were not the applicable test. The check surfaced C8, which the evidence alone had missed: a reader who cannot verify a claim independently treats the whole page as marketing.

---

### 29.4 Page Structure (as built and approved, S053)

The order as approved on the live page. This is also the mobile order: wider viewports may group blocks side by side but never reorder them.

| # | Block | Change it carries | Component status |
|---|---|---|---|
| 1 | Sticky header | site furniture | DSRD 8 §18 (LOCKED) |
| 2 | Breadcrumb: Home > Student Reviews | site furniture | DSRD 1 §9 |
| 3 | **Hero** | orientation; copy is Kain's own words (S052) | `.policy-header--doc` with `.policy-header--portrait` |
| 4 | **Global impact block** | C1, C2, C3 | One component `.gi`: intro, world map, markers, country panel, four figures. Decision history DSRD 8 §21; built |
| 5 | **The archive**: intro, control bar, live count, masonry grid, batching | C4, C5, C6, C7, C8 | Decision history DSRD 8 §22; review card DSRD 8 §14; control bar values are the DSRD 7 form-control standard; built |
| 6 | **Gateway** | C9 | `achology_routes_grid()`, reused from About; nine rows, not ten (S054 ruling, below) |
| 7 | **Enquiries panel** | C9 | `achology_warm_room()`, DSRD 8 §16, reused from About |
| 8 | Site-wide footer | site furniture | DSRD 8 §19 (LOCKED) |

**As rebuilt in Code's S141 and S142 sittings (Kain's rulings, recorded S393).** Four things about this table moved, and each is his.

1. **The reading column is 960** (theme 0.707.6). Kain chose C of four rendered widths (800, 880, 960, 1104) on the page itself: "yes, go with C please". Two review cards sit across, each about 470 wide at 1440 (452 at 1024), which keeps his S053 two-across ruling and ends the reviewer names cutting short. It is one scoped rule in `reviews.css`, annotated as a one-off; the site-wide article column stays 800. About and Testimonials were widened to the same 960 at 0.707.18 (one rule in `components.css`) so the shared gateway can only render one way.
2. **Block 4 is the dot world and block 5's header is rebuilt.** Decision history at DSRD 8 §21.3 and §22.2. The archive's batch is 32, not 50.
3. **Block 6 is the rebuilt Ten Ways gateway** (DSRD 8 §36, `achology_site_gateway()`), which replaced `achology_routes_grid()`. The S054 exclusion of the Watch Member Testimonials row below was set at this page's call site before the rebuild; Code states in his fold-back whether the page still omits that row.
4. **Block 7 is the FAQs block**, not the enquiries panel (DSRD 8 §37, `achology_faq_block()`). Its heading is "FAQs About the Achology Learning Experience" and it carries eight help answers (IDs 329, 406, 403, 281, 336, 350, 342, 269) with the registration credit line beneath. The Member stories block (the Five Aspects videos) is removed from Reviews and stays on Testimonials; the hero's Watch Testimonials button is the route there. The hero's primary button is Read the Reviews.

**The page was signed off by Kain in Code's S142 sitting** ("this page is actually pretty much perfect"). Code built its last structural edits over the page gate intake lock on Kain's direct instruction, and said so in his report. The closing brief carries a DOCUMENT TYPE line reading "not a page spec" (S392), which the intake wall reads; it carries no PAGE GATE line because it adds no block, value or copy.

**Two block changes from the S221 composition, both Kain's rulings at S053.** One: the standout reviews block is removed from this page, not deferred. His words: "I know that we might have agreed on some standard reviews, but I don't think they need to be incorporated into this page. I think what we have in this page is more than enough." The Featured flag and the standouts treatment stay specified for the course-page and school-page review blocks, which is where he pointed them. Two: the page closes on the About gateway and the enquiries panel, not the DSRD 8 §13 "Where next?" panel the composition named.

**The gateway carries nine of the shared set's ten rows (Kain, ruled directly in Code's S054 session; recorded here S265).** The Watch Member Testimonials card is excluded from this page: Kain saw it live, had not approved it, and ordered it off. The exclusion is implemented at the page's own call site in `page-reviews.php`; the shared `achology_site_routes()` set is untouched, because that ten-row set also feeds the About gateway and editing the set to satisfy one page would silently change another (DSRD 3 §2.6). Shipped and verified live at v0.60.6: the card is absent from `/reviews/` and still present on `/about/`. How the row got there is recorded as a lesson rather than a fault: nobody chose it; the page rendered the shared set and inherited the row. A page rendering a shared row set inherits every future addition to that set unapproved.

**The trust masthead of the S221 composition dissolved rather than being built.** C1 and C2 are carried by the global impact block's intro and figures; no separate masthead exists.

**The review card is the atomic unit of the archive.** It carries C4 by itself, every time it appears. Per DSRD 4 §14.4 it shows: review text, review title, star rating, first name plus surname initial, the word Verified, review date, and course. No per-review country.

**The archive's mechanics (ruled S053):** masonry grid, two columns at desktop and tablet, one below 600px, constant 24px gaps, plain CSS grid as the no-script fallback; batches of 50 appended in place on a real link, every review reachable by following links; default order striped across the star bands in proportion to their size, computed at import, a filtered view returning to newest first. The reasons and verification live in the signed record; DSRD 8 §14.5 and §22 carry the component-side record.

**Kain's S514 looks on this page (Code's About, Testimonials and Reviews sitting, 12 November 2026, each chosen in the Change Viewer).** Cards under 440 wide put the name above and drop the footer picture ("Yes, build 1"; DSRD 8 §14.2 item 5 and §14.4). The translation control stays the quiet orange link, "Translate this text" shut and "Hide translation" open ("Yes, build 1"; DSRD 8 §14.2 item 6). Below 768, every Como part steps one down and the Mulish reading text stays ("Yes, build 2"; DSRD 7 §3.0, the phone rule's named exception).

---

### 29.5 Both closing tests — run and reported

**Test 1 — every block carries a named change.** Passed for blocks 3–7. Blocks 1, 2 and 8 are site furniture present on every page; they are declared here as carrying no page-specific change rather than removed, matching the treatment in §20.1. No block was found that carries no change and no justification. Re-run S262 against the as-built order: still passes.

**Test 2 — every change has a block.** Passed. C1–C9 are each assigned above, and no change is carried off-page. Re-run S262: the standout block's removal moved C6 wholly onto the archive, whose search, filters and full text carry "what people with my concern actually said" directly.

---

### 29.6 Decisions closed (S221 and S239)

**1. Theme tags are visible on this page, and on this page only.** DSRD 4 §14.4 holds that theme tags are an internal routing label never shown to the reader. That rule was written for reviews appearing *as social proof on other pages*, where the tag works invisibly to pull matching quotes onto the right page. The reviews page is the one place a reader browses reviews as the content itself, where 4,517 unfiltered items is a wall nobody reads. §14.4 gains a scoped exception naming this page; the rule stands unchanged everywhere else. *Kain, S221.*

**2. All 4,517 reviews are shown, including the 3.0–3.5 star band.** The distilled set is tiered "Displayable" (4,060 rows, 4.0–5.0 stars) and "Insight" (457 rows, 3.0–3.5 stars). The tier boundary is exactly the star rating and nothing else — it is not a quality judgement. Showing only the Displayable tier would put a wall of 4- and 5-star reviews under a stated 4.66 average, with nothing on the page explaining why the average is not 5. The 3-star reviews are among the most considered writing in the set. Both the page's credibility and its value to an AI assistant asked whether Achology is any good depend on the critical reviews being present and findable. *Kain, S221.*

**3. Star rating is a filter control, not just a display value.** Follows from decision 2: a reader who can deliberately choose to read the 3-star reviews is being invited to check rather than asked to trust. This is what carries C7.

**4. The platform-era reviews show unedited (Kain, S239; typographic normalisation permitted, Kain, S262).** The 60 reviews naming Udemy and the ~526 addressing the instructor in the second person display verbatim: no trimming, no rewording, no exclusion. The page's claim is "every review since 2014, unedited", and the platform mentions are provenance, proof the record is real. This closes S221 open item O5. Amended S262 on Kain's ruling: typographic normalisation is permitted across all 4,517 reviews, meaning sentence-initial capital letters, a terminal full stop where a sentence carries none, and whitespace, and nothing else. Words are never added, removed or changed, acronyms in reviewers' own words stand at every mention (the DSRD 6 s1 carve-out), and the amendment exists so the record reads as cared-for text rather than a words dump while staying every reviewer's own words. The normalisation runs as a scripted pass with a dry-run report and a sample for Kain's eye before anything is applied (commissioned S262).

**5. The review card is locked (Kain, S239).** Full anatomy in DSRD 8 §14, every value approved by eye on rendered cards carrying live bank data. Includes the review title (the reviewer's own words, lightly trimmed; production rule in DSRD 8 §14.5) and the course signpost footer with each course's DSRD 1 URL baked at import.

**6. Standouts are chosen by size (Kain, S239).** The Featured set renders in the locked card scaled per the §6.6 featured-quote language; exact values in DSRD 8 §14.5. This closes the standout-treatment question deferred at §29.8. The standout source is the hand-picked Featured flag in the live bank, data source `collection://24b47674-bb62-4992-bdc7-0d1a10183f76`, verified live at S239 (closes O2).

**7. The map band is commissioned (Kain, S239).** The page carries DSRD 4 §14.2 Variant 1 beneath the trust masthead; the placement and the accurate-geography requirement are recorded at DSRD 4 §14.2 (closes O3).

**8. The archive control bar (Kain, S239).** One compact bar: keyword search first, then Theme, Course, and Rating dropdowns, with a plain hint line beneath teaching by example, and a live results count line above the grid whose number is real. Values travel in the signed page spec.

**Decisions ruled at S053, on the live page (recorded S262). These complete and partly supersede the list above.**

**9. The standout reviews block is removed from this page** (§29.4). Supersedes decision 6's placement here; the Featured flag, the standout source and the treatment stay specified for the course-page and school-page review blocks. The scaling half of decision 6 had already been withdrawn by Kain at S240: standouts render at normal card size wherever they appear.

**10. The map band became the global impact block.** Decision 7 commissioned DSRD 4 §14.2 Variant 1; what was built and approved is one component (`.gi`) carrying intro, map, markers, country panel and four figures together. Decision history at DSRD 8 §21.

**11. The grid is masonry, two across.** Constant 24px gaps, each card snapping under the shortest column. Supersedes the plan's three-across equal-height grid: on this data, equal heights put a 256px review inside a 1046px card, and Kain rejected both the stretched grid and per-card heights.

**12. The batch is 50**, appended in place on a real link, so every review stays reachable with no scripting. Was Code's 24.

**13. The default order is striped across the star bands**, each band laid across the whole archive in proportion to its size, newest first within its band, computed at import. This is how decisions 2 and 3 survive mixing: the critical band appears throughout rather than sorting to the end. A filtered view returns to newest first.

**14. Every control bar value is settled.** Kain ruled at S053 that no candidates remain and the page is final; the values became the site's first form-control standard, written at DSRD 7 (S262).

---

### 29.7 Still open, and the page's remaining definition of done

| # | Open item | Where it goes |
|---|---|---|
| O1 | Which themes surface as visible filter labels, and their exact wording. Working set rendered and not objected to at S239 (eight, benefit-led: Coaching and helping; Practical application; Relationships; Career growth; Self-awareness; Confidence; Wellbeing; Purpose; teaching quality and value stay internal). The Theme dropdown and the review card titles are unbuilt until the Cowork tagging pass supplies `review_theme` and `review_title` values; the renderers already accept them. Closes by eye at that point, then records in DSRD 4 §14.4 | Kain's eye when the tagging pass lands; DSRD 4 §14.4 |
| O2 | CLOSED S239: see §29.6 decision 6, and its S053 supersession at decision 9 | — |
| O3 | CLOSED S239: see §29.6 decisions 7 and 10 | — |
| O4 | The schema plan, given no star rich snippets are available for self-hosted reviews about one's own organisation. **Not owned by this document**: schema ownership was settled at S219 and per-page-type schema lives in DSRD 10. With Code to decide and state | Code, next session; DSRD 10 |

The page's remaining definition of done, held by Code: the DSRD 6 gate with its per-chapter record, the schema decision (O4), and the Rank Math metadata (title, description and og:type answered by Chat at S261, in Code's inbox).

---

### 29.8 The design session happened live in Safari

Every question this subsection once deferred was settled by Kain's eye on the live page across Code's S052 and S053 sittings, under the standing rule 16 Safari surface. The settled answers live in the signed record and the component entries: the masthead dissolved (§29.4), the review card at DSRD 8 §14, the control bar as the DSRD 7 form-control standard, the map inside the global impact block (DSRD 8 §21), mixed star bands by the striped order (§29.6 decision 13), and batching as load-more on real links (decision 12).

---

### 29.9 Components this layout commissioned, as they resolved

| Component | Resolution |
|---|---|
| Review card | Built and locked. Prototype and build sheet in the Card System folder; decision history DSRD 8 §14 |
| Trust masthead | Dissolved at S053 into the hero and the global impact block; never built |
| Filter bar | Built. Prototype and build sheet in the Form Controls folder under Component Design Prototypes; its values are the site's form-control standard at DSRD 7 |
| Country map (Variant 1) | Superseded: built as the map band inside the global impact block, DSRD 8 §21 |
| Global impact block | Built (not in the S221 list; emerged in the Safari sittings). Decision history DSRD 8 §21 |
| Review archive | Built. Decision history DSRD 8 §22 |

*Recorded for `component-library`.*

---

## 30. Testimonials Video Page Layout (COMPOSED — NOT YET LOCKED)

The testimonials page carries prerecorded member video: 46 videos, ten named members answering the same five questions on camera (nine answered all five; one answered Q4 only). Source of truth is the Notion "Testimonial Videos" database (`9beec85f-6eaf-49e5-be77-273b19351632`); the 46 Vimeo URLs live there and are not copied around. It is **not** the reviews page (§29), which carries written review.

Composed at S221 through `page-composition`, against the Document-Level Standards above. Nothing here is a visual decision — appearance is deferred (§30.8). **This map was written before Claude Code's build landed, so it can serve as the yardstick that build is audited against (rule 13).**

---

### 30.1 The job

**This page exists to get a hesitating visitor — one already being pointed here from a course, membership or sales page — to commit to studying with Achology.**

One action, one reader. Unlike the reviews page, this page **closes** rather than routes. It is the highest-trust human proof on the site and the page a course or sales page links out to when a visitor is nearly there but unsure. The action is *commit* — begin the enrolment or membership step the referring page was offering.

**Subordinate job:** to be indexable proof for search and AI assistants, via transcripts and per-video schema. This earns real E-E-A-T but never reorders the page. Where the two would disagree, the primary job — closing a hesitating visitor — decides.

*Note the deliberate contrast with §29. Reviews removes doubt and hands off; testimonials removes doubt and asks for the decision. That is why the two proof pages are composed separately rather than sharing one structure.*

---

### 30.2 The reader's arrival state

These visitors are further down the path than reviews-page visitors — they have been sent here by another Achology page, not found by a cold "reviews" search. Arrival is inferred from that referring context and from the member answers themselves; assumptions are labelled.

| # | What is true on arrival | Basis |
|---|---|---|
| A1 | They are near a decision and were sent here to help them make it — a course, membership or sales page pointed them here | **Assumption**, but a strong one: this is the page's stated role in DSRD 4 (course pages and the membership page link to `/testimonials/`). Confirmed after launch from referral-path data |
| A2 | They have read the claims already and now want to see whether real people say the same unprompted | **Assumption** from the page's position late in the funnel |
| A3 | They doubt that a self-paced online psychology community delivers what a structured or in-person one would | Inferred — the member answers repeatedly address exactly this doubt (Q3 is about the value of a collaborative peer-learning environment) |
| A4 | They wonder whether people "like them" belong here | Supported — the ten members span countries (Scotland, Chile, Netherlands, N. Ireland, England, Italy) and walks of life; the international spread is real, consented data |
| A5 | They are wary of scripted, cherry-picked testimonial reels | **Assumption**, and the one the whole page design answers: unscripted people answering the same fixed questions is the counter to it |

---

### 30.3 The required state, as changes

Each change is one sentence in the reader's voice. This is the page's entire content brief.

| # | Change |
|---|---|
| C1 | "I now understand what this page is: real members, unscripted, all answering the same honest questions." |
| C2 | "I now see and hear a real person, immediately — not a logo or a star rating." |
| C3 | "I now know what someone like me would say to a person standing exactly where I am." |
| C4 | "I now believe the community itself, not just the courses, is where the value is." |
| C5 | "I now know what people actually gained, in their own words." |
| C6 | "I now see these are real, different, named people from all over — not actors, not a type." |
| C7 | "I now trust this is unscripted, because ten people answer the same question and none of it is polished the same way." |
| C8 | "I now know the exact step to take, and I'm ready to take it." |

**Completeness check run:** the page **sells**, so the four banked selling-frameworks were the applicable test — not the routing check used for reviews. Findings, and how the structure answers each:
- *Problem named / stakes visible (SB7):* the reader's hesitation is the problem; the page never states it aloud but answers it — leading with Q4 (§30.4) puts their own unspoken question first. **Present.**
- *Value understood (Value Equation):* C4 and C5 carry the dream outcome and its likelihood in members' own words. **Present.**
- *Objections and risk answered (Cialdini):* C7 answers the "this is staged" objection through unscripted convergence; social proof is the page's entire mechanism. **Present.**
- *Position clear against alternatives (Dunford):* C4 positions the collaborative community against self-paced-alone and against formal/in-person study — the alternatives A3 names. **Present.**
- The check **surfaced C1** — without a framing intro the reader meets a wall of video with no idea why the same faces recur; the frame is what makes the repetition read as honesty rather than filler.

---

### 30.4 Page Structure (top to bottom)

The derived order. This is also the mobile order — wider viewports may group side by side but never reorder. **Leading with Q4 is a derived decision, not a preference:** Q4 ("what would you say to anyone thinking about studying with Achology?") is the exact question in the hesitating reader's head (A1, A2), so C3 must land before the fuller picture, and ten people converging on it is the page's strongest single move.

| # | Block | Change it carries | Component status |
|---|---|---|---|
| 1 | Sticky header | — site furniture | DSRD 8 §18 (LOCKED) |
| 2 | Breadcrumb | — site furniture | DSRD 1 §9 |
| 3 | **Framing intro** | C1 | **New — short copy block** |
| 4 | **Hero video** (single, opens the page) | C2 | Video player + transcript; see §30.9 |
| 5 | **Q4 section** — "what would you say to anyone thinking about studying with Achology" | C3 | Question-headed video group |
| 6 | **Q1 section** — how have you benefited | C5 | Question-headed video group |
| 7 | **Q2 section** — the main lesson that added most value | C5 | Question-headed video group |
| 8 | **Q3 section** — value of a collaborative peer-learning environment | C4 | Question-headed video group |
| 9 | **Q5 section** — the five things you value most about the community | C4, C5 | Question-headed video group |
| 10 | **Primary CTA** | C8 | Existing CTA pattern — inherits the referring page's offer |
| 11 | Site-wide footer | — site furniture | DSRD 8 §19 (LOCKED) |

**Carried by the whole, not one block:**
- **C6** (real, different, named people) is carried by every video showing its person's name and country — country **is** shown here (unlike §29), because these are named people who consented on camera. It is a property of the video group, not a separate block.
- **C7** (unscripted) is carried structurally by the five-question spine itself: the same question answered ten different ways is the proof. No block asserts "these are unscripted" — the format demonstrates it.
- **Transcripts** sit beneath every video (C5's indexable form and the accessibility win). Deliberately **not** a mini-article per video — 46 near-duplicate texts would be thin content; the transcript is supporting text on the one rich page.

**The CTA repeats without a new change (rule 9).** The job's action — commit — may be placed wherever a reader becomes ready: a quiet instance after the Q4 section for the reader already convinced, and the primary instance at block 10. Same action both times, never a different exit.

**Kain's S514 looks on this page (Code's About, Testimonials and Reviews sitting, 12 November 2026, each chosen in the Change Viewer).** The five question buttons keep their own lines: each is its own white card with its hairline, the track ring is gone, and the fire frame slides between them ("Yes, build 1"; DSRD 7 §5.1). The member story posters are re-made from a clean still of each film under the brand orange wash, with the question along the foot over a soft dark edge, the face clear and the play badge in the centre; each question reads exactly as its caption ("Yes, build 3"; built at 1280 with 320, 480, 640 and 960 copies, theme 0.708.057; source previews/audit-s514/poster.html). Below 768, every Como part steps one down and the Mulish reading text stays ("Yes, build 2"; DSRD 7 §3.0).

---

### 30.5 Both closing tests — run and reported

**Test 1 — every block carries a named change.** Passed for blocks 3–10. Blocks 1, 2, 11 are site furniture, declared as carrying no page-specific change (as §20.1, §29.5). No block carries no change without justification.

**Test 2 — every change has a block.** Passed. C1–C5 and C8 map to blocks; C6 and C7 are carried by the video group and the question spine respectively, named above rather than given a block of their own — because inventing a "these are real / these are unscripted" block would *assert* what the format already *demonstrates*, which is weaker.

---

### 30.6 Decisions and recommendations at S221

**1. Section order: Q4 → Q1 → Q2 → Q3 → Q5.** Derived (§30.4), and matching Code's own recommendation in the agreed plan. Q4 leads because it is the reader's own question; Q1/Q2 give the fuller benefit picture; Q3/Q5 carry the community-value change (C4) that answers the reader's deepest doubt (A3), placed later where they are weighing commitment.

**2. Country is shown per video.** Consented on-camera data about named people — no integrity problem, and the international spread is an asset (C6). This is the deliberate opposite of the reviews-page rule (§29, no per-review country) and the difference is sound: there the country would be an inferred guess about a private person; here it is a fact the person gave.

**3. No mini-article per video.** 46 short near-duplicate texts is thin content Google penalises. Transcripts live as supporting text on the one page. *Recommended.*

---

### 30.7 Still open — carried, and the ones Code is mid-build on

| # | Open item | Where it goes |
|---|---|---|
| O1 | The hero video pick, and any "Featured" picks. **No selection exists** — the Featured flag is unused across all 46. *Recommended:* the hero is a strong Q4 answer, so the very first thing the reader sees is someone answering their own question | Decide with Kain |
| O2 | The transcript pipeline, proven on **one** video before scaling to 46. Vimeo may already hold auto-transcripts; else the audio is transcribed. **This is a build task — likely what Code is on now** | Claude Code; confirm which route |
| O3 | Whether the ten per-person "member story" articles are built later. The page is complete without them; the door is open once transcripts exist. *Recommended:* defer — ten rich articles later, not now, and never the 46 thin ones | Backlog-with-trigger (trigger: transcripts complete) |
| O4 | How the 46 videos' data reaches the theme at build, Notion staying source of truth. Ties directly to O5 — the schema field source and the display data source should be **one** decision, not two | Decide with Kain; route to DSRD 10 |
| O5 | **VideoObject schema field source.** Code flagged (note 2026-07-22) that the theme holds only Vimeo ID + poster — no per-video title, description, upload date or duration, all of which Google requires. The printed question on each thumbnail can serve as `name`. *Recommended:* one ACF field group (title, description, upload date, duration, Vimeo ID, poster) mirroring how Person and FAQ-audio schema already work, fed from the Notion export — so display data and schema data arrive by the same route. **This is the real decision behind O4** | Decide with Kain; DSRD 10 §9 gains VideoObject rows |

---

### 30.8 Deferred to a design session

- How the hero video sits above the five sections without dwarfing them
- How a question-headed group of up to ten videos is laid out — grid, row, or stack — without becoming a wall
- How a transcript sits beneath its video: open, collapsed, or on demand
- How name + country presents on each video
- The click-to-play poster treatment (plumbing mirrors the About videos — Vimeo, click-to-play so the page stays fast; Code's domain)

---

### 30.9 New components this layout commissions

| Component | Needed by | Status |
|---|---|---|
| Question-headed video group | Blocks 5–9 | New. But **check the About page member-stories block first** (`.about-proof__strip`, `.proof-card*`, `.about-video-lightbox*`, DSRD 8 §12.2) — it is the first built instance of testimonial video + Vimeo lightbox and is flagged there as a reuse candidate for exactly this page. Promote it, don't build a second |
| Hero video | Block 4 | New — may be the same player as the group, sized up |
| Transcript block | Beneath every video | New |
| Framing intro | Block 3 | New — copy block, likely no new component |

*Recorded for `component-library`. The member-stories reuse candidate is the key note: this page is the second use that promotes it (DSRD 8 §12.3 procedure). No visual decisions taken here.*

---

## 31. Policies Index Page Layout (LOCKED, Kain S236)

The Policies index at /policies/ is the gateway into every document that governs Achology. Its job: get a visitor who is checking whether Achology can be trusted to open the policy that answers their question. It routes; it never sells. It is a quiet text-led page under section 25 (the 880px reading column) and section 27 (the sentence test), rendered through the policy template family. The card treatment is the built page's existing pattern and is the authority; this section locks the block order and what each block is for.

### 31.1 Page Structure (top to bottom)

1. Sticky header (DSRD 8 section 18)
2. Breadcrumb: Home icon, chevron, "Policies" (DSRD 1 section 9)
3. H1 plus lead paragraph: says what the page is at a glance
4. Governance paragraph: the quotable answer to how Achology governs itself (who owns it, what rules bind it, that everything is published openly)
5. Hairline
6. Group heading "Our Legal Policies", then the seven policy cards in white, in this order: Privacy Policy, Terms and Conditions, Cookie Policy, Refund Policy, Trust Statement, Disclaimers, Accessibility Statement
7. Hairline
8. Group heading "Our Training Standards", then three cards on the warm cream with an orange top edge: The Achology Manifesto (links to /about/manifesto/), Code of Ethics (links to /about/code-of-ethics/) and How We Write (links to /policies/how-we-write/), as section 31.4 sets out
9. The More About Achology block: the warm cream block that closes the three founder pages, with its own title, lead and four cards (section 31.4)
10. Rainbow stripe plus footer (DSRD 8 section 19)

This is also the mobile order. Nothing on the page sells: it carries no closing CTA panel and no sales content, because the page's job ends when the reader picks a document, and the More About Achology block only routes to the founders' pages and the certification pathway.

### 31.2 Card anatomy

Each card carries the document name, one plain description line saying what the document covers and when a reader would need it, a chevron right, and the ghost word behind the text (the one word the document is about, specified at DSRD 8 §12.6; desktop and tablet only). The whole card is the link. The card's visual values are the built page's locked pattern; where this section and the built page ever disagree on a visual value, the built page is correct and this section is the thing to fix. Verified against the shipped page (theme v0.36.49) at S238: the built order matches 31.1 exactly.

### 31.2a The card band: the cards bleed to 944 (RULED, Kain S090, on the whole rendered page in Safari)

**The nine cards take the DSRD 7 section 4.4 inset panel width, 944px**, the 880 reading column plus a 32px bleed each side, with matching 32px inner padding. Nothing was designed for this: it is the locked mechanism applied to a page that did not yet follow it, and the Policies index is now a named user of it in DSRD 7 section 4.4.

**Kain asked for it in his own words:** "on the Achology's Policies and Standards page, please apply our principle that lets cards sit outside the container be applied to the different policy cards." **He approved it looking at the whole page in Safari:** "Yes, it does. Its possibly the best looking policies page I've ever seen."

**What it fixed, measured before and after on the live page.** Every heading and paragraph on the page starts at 280 at desktop. Each card also started at 280 and carried 24px of its own padding, so the words inside a card began at 305: **the page had two left edges 25px apart.** The card now reaches 32px further out on each side and holds 32px inside, so its words land back on 280.

| Width | The card | The page's writing | Sideways scroll |
|---|---|---|---|
| 1440 | left 248, width 944 | h1 at 280; card text at 281 | none |
| 1039, just under section 4.4's boundary | left 80, width 880 | h1 at 80, width 880, flush | none |
| 390 | left 20, width 350 | flush with the h1 | none |

**The 1040 boundary is section 4.4's own and was not chosen here.** Below it the bleed is off, so nothing changed on a phone or a tablet. Shipped v0.120.0 to v0.121.0 and read back on the live page at all three widths.

### 31.2b The header copy, given whole by Kain in session (S090)

Both paragraphs are his own words, placed verbatim in the template and read back off the live page. **The first paragraph was replaced by Kain's own S203 words (section 31.4), set verbatim as shown here; the second is his S090 wording.** The page carries no excerpt, so the template default is what every visitor reads.

> This page outlines the policies and standards that govern Achology, including our legal policies, business practices, and the values we uphold as a training organisation. Our policies are transparent and publicly accessible, so you always know where you stand with us.

> Achology is owned and run by its remaining original founders, Kain and Karen Anne Ramsay, through two registered companies in Scotland, UK. Achology adheres to best practices for public trading and is supported by seven legal policies, a Manifesto, and a Code of Ethics that oversee its online teaching and mentorship activities. All these documents are available on this page, written in clear language for anyone to review at any time, whether or not you are an Achology member: someone who has joined the private learning community at community.achology.com.

**One punctuation substitution, made openly and told to him in session.** His second paragraph arrived with an em dash before "someone who has joined". His own S222 ruling at DSRD 2 section 3.0 bans it anywhere in Achology copy with no exception, and the gate refuses a file containing one, so it is a colon, which that same sentence already used. Not one word changed, and he can overturn it.

**Two outbound links, in the second paragraph only, at his instruction.** "two registered companies in Scotland, UK" goes to the Companies House record for SC697126, opened and read back before shipping, its heading reading ACHOLOGY TRANSACTIONS LTD.; "best practices for public trading" goes to tradingstandards.uk, the Chartered Trading Standards Institute, which the Disclaimers page already links for this exact idea. Both carry `target="_blank"`, `rel="noopener"` and a visually hidden "opens in a new tab".

**Two things found by reading the page back rather than by any gate.** The links first shipped in the browser's default blue with a heavy underline, because `.policy-header__copy` sits in `.policy-header` rather than `.policy-body` and was therefore outside every link rule on the page; it had never carried a link, so nothing had ever exposed that. The locked site-wide body-link treatment was extended to it verbatim in v0.120.3, with no new value chosen. **And DSRD 7 section 1.0 asks for a visible outbound marker on external links, which no policy page carries.** The only sized marker in the theme is the book note's, and inventing a second is a visual decision and therefore Kain's, on a render, under standing rule 16. **That is the one thing still open on this page.**

### 31.3 Copy ownership

The approved copy (H1, lead, governance paragraph, both group headings, and all nine description lines) is recorded in the signed spec `SPEC__Policies_Index_Locked_Layout_And_Copy.md` (S236, channel; updated S238 to the as-built copy after Kain replaced the lead and governance wording in the build session) and lives in the theme's policy content partial as built. Ruled S236: the gateway lists all nine governing documents, the two standards documents keeping their /about/ addresses.

### 31.4 The five S203 rulings (Kain, Code's S203 theme main session, 2 November 2026; on the build site at 0.707.689 to 0.707.695; written by Chat, S452)

Kain asked Code, at his sign-off look at /policies/, how the page could be improved. Code named the list (ten identical boxes, a long scroll on a phone) and the empty width on a computer. Every pick below was shown as four rendered options in the shared Change Viewer, and his words are in the theme session's channel rulings. The page lists ten documents: seven legal policies and three training standards.
1. **Two Groups, Two Tones** ("Two Groups, Two Tones"; 0.707.689, `policies.css`). Of Two Across (Code's recommendation), Numbered Contents, Words That Show and Two Groups, Two Tones, he chose the last. The legal policies keep the white card with the 1px hairline. The training standards (the Manifesto, the Code of Ethics and How We Write) take the warm cream and a 3px orange top edge, kept on hover, with the ghost word a step stronger on the cream. Words, links, order and the card band (section 31.2a) are unchanged.
2. **Reading Size and Larger Cards** ("Reading Size and Larger Cards"; 0.707.692, scoped to the index by `.policy-page--index`). The second intro paragraph is at the reading size the policy pages now use, 18 on 1.75 (section 25); each card's name is 18 and the line under it 16 on 1.55. No word, colour or spacing between blocks changes.
3. **The opening paragraph is Kain's own words** (0.707.693, `template-policies-index.php`), set verbatim and read back on the build site word for word: "This page outlines the policies and standards that govern Achology, including our legal policies, business practices, and the values we uphold as a training organisation. Our policies are transparent and publicly accessible, so you always know where you stand with us." The page's excerpt branch (an owner override) is unchanged and the page carries no excerpt. The same sitting, the Code of Ethics card's line is his words, set verbatim (0.707.695): "The standards of character and behaviour that practising Achology members pledge to uphold."
4. **The faint word behind the title** ("Policies behind the title"; 0.707.694). Of Policies Behind the Title, Standards Behind the Title, Policies on the Right and Two Marks he chose the first. The word "policies", drawn by the theme's own tools/policy_header_images.py in Como Bold at the faint orange the policy pages use (Kain, S135, option 2), sits behind the title from 1024 wide, exactly as every policy page carries its own word. It is an `<img>` with the alt text "Achology Policies: the page's title word set in faint Achology orange", so search engines read it as the page's picture.
5. **The page closes on More About Achology** ("1 More About"; 0.707.691). Of More About Achology (Code's recommendation), Ready to Further Your Learning?, the membership band and both closes together, he chose the first. After the two groups stands the warm cream More About Achology block that closes the three founder pages, with its own title, lead and four cards: the Founders' Letter, Achology's Code of Ethics, Member Testimonials and the Certification Pathway. The Manifesto card is left out, as it was in the option he chose, and no word is new. The block's rows live in one home, `achology_policy_more_about()` in shared-parts.php, which the founder pages and the index both call (DSRD 3 section 2.6). The Code of Ethics page, which calls the same function, still shows its own four (the Founders' Letter, the Manifesto, Testimonials and its training).

The page reads 85 in Rank Math (335 words, no picture in the content) under the exception in DSRD 6 chapter 5, item 11. The faint word is now a picture in the content, so the picture test should pass on a rescore; the score is Kain's one-click rescore, and the exception stays recorded until it is taken.

### 31.5 The redesign is signed on its whole-page preview (Kain, 23 November 2026, "Yes, sign it"; built at theme 0.708.401 and 0.708.402; written by Chat, Session 480, from RULING__Policies_Index_Redesign_Signed_S552 and SHIP__Policies_Index_Redesign_S555)

Kain asked for the main policies page to be brought back in step with the rest of the site. Shown the whole Policies index preview (previews/policies-index-s555, commit 453e6623), he said: **"Yes, sign it."** **Where sections 31.1 to 31.4 describe the 880 reading column, the hairlines between groups, the row cards, the ghost words and the word behind the title, this section wins.** What his yes covers:
1. **The frame and rhythm.** The site's 1200 frame, every block on the same left edge as the Academy, Help and Pricing pages. Light Sand and white bands take turns at 64, 48 and 32 with no hairlines between them, and the banner carries the trail (the spacing is DSRD 7 section 4.3 Exception 29).
2. **The banner,** Light Sand, two columns. Left: the title, Chat's 84-character line (ANSWER__Policies_Banner_Line_84_S552, one row at 1440) and three facts in the course heroes' icon rail (Seven Legal Policies, Registered in Scotland, UK, Free for Anyone to Read). Right: a small fanned stack of three of the page's own documents, white cards with their icons, beside the words on a tablet and dropped on a phone. No portrait.
3. **The text band,** "Who Runs Achology, and the Standards We Keep", with its line, then Kain's facts in Chat's two paragraphs (ANSWER__Policies_Index_Banner_And_Intro_S552), each in its own card. The card pair is the shared `.intro-pair` (policies.css section 22, which the Presuppositions page also uses): body 16 under the 18 lead, ending level at 1440 and 1024. Both outbound links stay (Companies House, tradingstandards.uk).
4. **The documents,** the ten, in the Help landing's category card with an icon square, in their signed order: the legal seven three then four across, the standards three keeping their orange top edge.
5. **The block standard.** Every block opens with a Como 24/600 heading and a Lead with Bar line, using Chat's one-line leads (ANSWER__Policies_And_Presuppositions_One_Line_Leads_S552). More About Achology opens the same way.
6. **Removed on his signature, on this page only:** the per-card ghost words (S043) and the word "policies" behind the title (S203). The old row-card rules went with them.

Files: template-policies-index.php, policies.css (sections 21 and 22), shared-parts.php (six Lucide icons: cookie, rotate-ccw, handshake, info, accessibility, landmark), style.css. **Proof:** the built page against the signed preview at 1440, 1024 and 375, zero differences; page_gate at 0.708.402, 53 passed and 18 failed (15 band lines, the site-wide chapter 7 line, Rank Math at 85 under the S203 exception, and keyword density from template words), answered in ANSWER__Gate_Lines_And_Open_Rulings_S480 section 2; axe zero violations; all 14 links answer 200; css_gate PASS; local, the server and the zip agree.

### 31.6 The Governance page is signed as built (Kain, 23 November 2026, "Yes, sign it off"; theme 0.708.427; written by Chat, Session 481, from RULING__Governance_Page_Signed_S561 and SHIP__Governance_Page_S561)

**This section replaces 31.5 for this page, and wins over 31.1 to 31.5 wherever they differ.** Branch D's redesign at 0.708.417 was rejected by Kain ("butchered"); the page went back to the 0.708.402 layout and was then made a signpost on his words: "this page just needs to be a signpost". Shown the whole page on the build site at 0.708.427 and asked "Shall I sign the Policies page off as done?", he said: **"Yes, sign it off".** What his yes covers, top to bottom:
1. **Title:** "Achology Governance: Policies, Standards and Legal", his name for the page. The schema name follows it.
2. **Banner:** the title, Chat's line, and the four most-read documents (Privacy, Terms, Refund, Cookie) as Fire Ring pills. No picture and no fact rail.
3. **Our Legal Policies:** the seven legal policies in the one row list (name, one line, chevron), on white, 64 between groups.
4. **Our Training Standards:** the Manifesto, the Code of Ethics, the Code of Character and Conduct (added at his yes, its line cut from the page's own signed Rank Math description) and How We Write.
5. **More About Achology:** the Founders' Letter, Member Testimonials and the Certification Pathway.
6. **The S043 ghost word** is back behind every row from 1248 up, at its measured sizes, with four new words: conduct, letter, members and certified.
7. **Who Runs Achology:** Chat's one-company paragraph (ANSWER__Privacy_Joint_Controller_Removed_S552 section 3) once, at the foot, at the 800 reading width, and the fixed UKRLP line under it.
8. **Questions About Our Policies:** the site's one questions block, three cards of four published Help answers. Its own ask line replaced the earlier "Ask us" line.
**Out of this page on his signature:** the fanned document stack, the fact rail, the two intro paragraph cards, the Help category cards and the orange-topped standards cards (31.5 items 2 to 4). Exception 29 (DSRD 7 section 4.3) is re-read against this layout by Code. **Open:** Kain's one-click Rank Math rescore.


---

## 32. Book Note Page Layout (ARRANGEMENT RULED S085; HERO RULED S102; REBUILT ONTO THE ARTICLE'S LAYOUT AT S113; TAKES THE QUOTE PAGE'S STRUCTURE AT S147)

**S149 and S150: the three reading pages share the rail, the date line, the type link and one hero. Read the note at the head of section 22 first; it governs where it touches this section. The S150 sitting changed this page in four places: the hero's bubbles (item 10 there), the panel's cover and button at the foot of the screen (item 16), the five body headings (§32.7) and the standfirst's closing line (item 19; §32.3, §32.9 item 1).**

**THE BOOK NOTE TAKES THE QUOTE PAGE'S STRUCTURE (Kain, live with Code in Safari on Words That Change Minds, Code's S147; recorded by Chat S401 from RULING__The_Book_Note_Page_Sitting_S147, channel Archive). Theme 0.707.83 to 0.707.92.** Where this note and an older line below disagree, this note governs.

1. **Explore More Book Notes** sits after the signature's hairline, the quote page's block, markup and S130 rules: six, three or none; two columns from 768; other book notes in the same category, newest first. A sixth contents entry names it. Its line, in Kain's words: "Each Book Note highlights a book's key ideas, helping you to decide which one to read next." Each line opens with the book's own cover, 56 wide, then the book's title, then "A book by {author}" in grey (0.707.92, Kain's new layer of transparency: the books are not presented as written for Achology; the wording is Code's first draft, live for Kain's correction).
2. **No Related Further Reading at any width** (§22.8). The side panel, with the cover, travels to the hairline closing Explore More Book Notes and rests 48 above it. From 1200 up, on screens 760 tall or more, the cover and the Amazon button lock to the foot of the screen.
3. **Three Achology bubbles behind the hero cover,** the quote page's sizes, from 1200 up, trimmed by the band so nothing scrolls sideways. **Superseded S150 (0.707.121): the three bubbles are gone; a thin orange speech bubble line sits behind the book, following the book's own size, shifted 40 left and 24 down; see the note at the head of section 22, item 10.**
4. **Numbered section headings:** each heading in the writing carries the contents' number (01 to 05) as a small orange label, hidden from screen readers (0.707.87).
5. **The reading progress line is a site standard (0.707.89):** a 2px brand-orange line on a hairline-grey track over the header's bottom hairline, on articles, book notes and quote pages, and on workbooks when the workbook page is built (§37).
6. **A STANDING RULING, never reopened:** the reading column's width and the body text size are the same on every content type and are not changed. Kain, S147: "we can't go playing around with font size ... this is standardized across the entire website ... no changes here at all, must remain as it is." Measured at 1440: 800 wide at 18px on the book note and the quote page alike. For the same reason a drop cap and a tint of the book's colour are set aside: both touch the type scale or the brand colours.
7. **Ratings as a visual: dropped.** Kain's v0.167.21 ruling makes the Essential Reading badge the rating's only visible mark; the Goodreads score is never shown.
8. **Open with Kain:** whether the "all articles from this book" line moves into Explore More Book Notes; and whether the three shapes that need new words per book note (a key ideas box under the opening, one pull quote per long section, numbered takeaway cards) are commissioned. Code builds the shapes only once words exist.
9. **The list covers fail three image lines** (the size suffix in the filename, JPG, no srcset), joining the hero cover's existing JPG and budget fails. WebP copies of every book cover belong to the Image and Icon Optimisation card (Chat, S401).

**THE LATER S147 RULINGS AND THE DESIGN SIGN-OFF (Kain, live with Code in Safari, Code's S147, theme 0.707.93 to 0.707.98; recorded by Chat S403 from RULING__The_Goodreads_Link_And_Course_Block_Words_S147 and RULING__The_Book_Note_Is_Finished_And_The_Quote_Course_Picture_S147, channel Archive).** These were made after the sitting file above was archived and amend the note above where they touch it.

10. **The book note page is finished, as a design.** Kain at 0.707.96: "this booknote page is ... finished now, Claude. Um, one hundred percent." This closes the page's design sittings (the second Safari look and the open items at §32.9 are closed by his word). It is his design sign-off, not a closed DSRD 6 record: the record still carries its machine lines (keyword density, acronyms, image formats on the media library covers, the record's own not-run chapters).
11. **View on Goodreads in the date line (0.707.93).** The third fact after the date and the reading time, in the date line's grey, orange on hover, opening the book's own Goodreads page in a new tab, built from the book's ISBN (the schema's sameAs). A book without an ISBN shows nothing (142 of 150 published book notes hold one). No Goodreads score is shown anywhere and a third-party score never enters the page's own rating markup; item 7 above stands. Chosen by Kain as a link only, tab 1 of four, "as just another layer of credibility".
12. **The section numbers sit above the headings (0.707.94).** Item 4 above is amended: the small orange label sits on its own line, 8 above the heading words, never beside them. Kain, on the beside version: "That's just not what we agreed."
13. **The author photograph in the writing carries the hero's three bubbles in miniature (0.707.95 to 0.707.98).** Book notes only, portraits only, from 768 up; on a phone the photo keeps its plain, centred look. First tab 1 of four at 0.707.96 ("very, very strong ... it really brings the page to life"), then refined at 0.707.98 to tab 3 of four when Kain saw the bubbles had shrunk the picture and pushed it down: the picture 224 wide with its top the figure's top, on the paragraph's first line, the figure 256 wide, the bubbles in the 32 strip at its right (96, 48 turned at the picture's foot, 22 between), the caption the picture's width. The values live in the Author Photo component's build sheet (prototype v2); this section records the ruling only.
14. **The course block's words on every reading page (0.707.93), Kain's text:** "Ready to Take Your Learning Further?" over "Explore related courses to deepen your knowledge and build on the insights introduced in this article." He kept "this article" for book notes and quote pages too. §22.10 carries the words; this line records that the ruling was made on the book note.
15. **A named page-gate exception.** The block-heading check flags "Book" and "Note" as mid-sentence capitals in Kain's approved line under Explore More Book Notes (item 1 above, "Each Book Note highlights ..."). His capitals stand, "Book Note" being a name. Recorded here as the exception; the gate reads it as a note on this page.

16. **The section numbers are one orange on all three reading pages (Kain, live with Code in Safari, Code's S149, theme 0.707.109, tab 1 of four; recorded by Chat S405 from RULING__The_Section_Numbers_S149, channel Archive).** Kain: "The small numbers before each section heading are inconsistent in colour and format across all three templates." On book notes and quote pages the small number above each heading and the contents' numbers are the label orange (`--color-orange-link`). The contents' last entry, Explore More, carries its number above its heading too. Articles carry no numbers, unchanged from §22.14 item 4. A fault fixed on the way: the book note numbers had drawn dark grey, not the orange approved at S147, because a colour name set only inside the side panel resolved to nothing outside it. §40 item 7 carries the quote page's half.

**THE BOOK NOTE TAKES THE ARTICLE'S LAYOUT, BLOCK BY BLOCK (Kain, live in Code's S113 sitting on the rendered pages; folded S358). Theme 0.381.0.** His instruction: *"Could I ask you first to be really thorough, please? Do literally a section by section comparison of the book notes page up against the article page."* Both pages were then walked block by block in a live browser at 1440 and **every edge read off the rendered page rather than out of a file**. Nine differences were found, eight closed, one put to Kain and answered at S358. **Where this round and anything below it disagree, this round governs**, and the older text is kept as the record.

**The reading area of this page IS the article's, not a copy of it.** Forty seven selector lines inside the S112 rebuild's media block in `knowledge-hub.css` read `:is(.kh-article__body, .bn-body)`, so the rail's rules exist once and reach both page types. A future ruling on the rail reaches this page without anybody remembering to copy it. The page therefore inherits DSRD 9 §22's fourth round whole: the 1104 grid, the 800 reading column, the 48 gutter and the 256 side rail.

| # | The difference found | What now governs |
|---|---|---|
| 1 | The reading bar sat at the top of the writing, a screen below the title | It sits in the hero directly under the lead, where Kain put the article's at S110 |
| 2 | The bar still carried the writer's photograph and name, on a page whose author card at the foot already carries both | Removed, on Kain's S112 ruling for the article. The argument is passed empty; the component itself is untouched |
| 3 | The lead was a step below the body: 16 over a 46-letter measure, against the article's standfirst at 21 over 55 | Both now render 693px. **This overturns Kain's own S249 approval of 46**, and says so in the stylesheet: his S112 ruling is the later word on the same question |
| 4 | There was no way to share a book note at all | A share row at the foot, landing at 716 to 968, the article's own position exactly |
| 5 | The side panel drew a second share row, so the marks appeared twice | The call passes `panel`, which is what the article has passed since S112 |
| 6 | Related Further Reading printed twice: six in the rail and nine at the foot, four of them the same books | The full-width block is off, on the article's own S112 ruling. The rail shelf of six is the only one |
| 7 | The foot sat on a different left edge entirely: three left edges on one page, the foot at 320 while everything above had moved to 168 | All five foot edges now read the article's set: 168, 168, 716, 168, 168 |
| 8 | The $7 membership panel was still drawn here | **Off, on Kain's word in the sitting ("yes").** This was the last content page still drawing it, so the two page types now end identically: writing, author with the share marks on his own line, two courses, footer |
| 9 | The cover did not follow the reader. The article's picture opens at the top of the rail once the hero scrolls away; the book note's cover left with the hero and never came back | `achology_article_aside()` takes an optional picture and the book note hands in its cover. **The cover variant keeps 2:3 at 256 by 384 rather than being cropped square**, because cropping a jacket to a square cuts the title off the one picture whose job is to show it. A caller passing nothing is untouched |

**The band's ground: ruled and closed (Kain, S358).** The article's hero band is the article's own picture washed almost out, so every article's banner takes its colour from its own subject. **The book note's band keeps the shared bookshelf photograph**, the same file on all of them. Kain was asked whether the book note should take its ground from the book's own cover instead and ruled no: *"the article page rules are different."* Two page types, two deliberate rules. The drawn book cover work is unblocked by this and does not change the band.

**One property had to be repeated, and the reason is recorded so nobody deletes it.** `.bn-body { display: flow-root }` earlier in `book-note.css` carries one class and so does the shared `:is()` selector, so the later sheet won on source order and the grid's `display` never landed while its columns did. One line of `display: grid` sits in `book-note.css` for that reason alone. **Found by measuring the deployed page, not by reading the file.**

The individual Book Note page, at `learn/{kh_category}/book-notes/{slug}`. One template serves all 598 notes. Every value below was approved by Kain by eye, on a rendered full page, across the S249 and S250 design sessions.

**Status, changed at S343, on Kain's S102 evening sitting with Code (5 September 2026).** The hero is ruled. Kain looked at the built page at desktop, tablet and phone in Safari through thirteen ships (theme v0.167.14 to v0.167.26) and approved the hero and its Essential Reading badge as built at v0.167.26, in his words: "Thats perfect work claude - thank you!!!" (`RULING__Kain_Approves_The_Book_Note_Hero_And_Badge_As_Built_At_v0_167_26_S102`). What he ruled is written into §32.3 (the hero, its stack and its three responsive tiers), §32.4 (the badge repeated at the head of the last section) and §32.9 item 1 (the rating's only mark on the page is now the badge). The headline pattern he set the same evening is already at §32.8. **Still open after the sitting:** the reading zone's vertical rhythm and block margins (§32.4), the Share this Article block, the primary button's destination (§32.3), the Goodreads line's home, and the contents-list highlight (§32.9 item 8). Those remain the second-look sitting's.

**Status, changed at S085.** Kain ruled V3 on the rendered sitting at `achologytest.com/book-note/book-note-sitting.html`: the travelling shelf is retired and the page takes the article page's own pattern at 880px. **The arrangement is ruled; the layout and the spacing inside it are not.** His words were exact: "V3, both, although we need to talk through improving the final layout and spacings". So this section is no longer a complete go-live spec. The structure rows below carry V3; the vertical rhythm, the block margins and how the two moved blocks sit against the writing are a Safari sitting with Code on the real page, and none of it is written here until that sitting has run. The foot of the page was not reached in the same sitting and is unruled. The copy and metadata formulas (§32.7, §32.8) are untouched by all of this and stand as locked. The approved page and its developer brief live together in the Book Note Page folder, under Knowledge Hub Design Prototypes in the Achology Website Pages folder; where the page and this section disagree, the page is correct and this section is the thing to fix.

**The page's job (Kain, S249):** hand the reader the heart of one book, help them decide whether to read it, and offer an Achology.com course as the practical next step. Two next steps, not one.

### 32.1 Page structure (top to bottom)

1. Sticky header (DSRD 8 §18)
2. Hero, full bleed (§32.2)
3. Reading zone: one 880px column, no shelf (§32.4). Two blocks sit inside the writing, in the article page's own places: a Table of Contents at the top, and one course card after the first section, filled by the tag rule at DSRD 1 §5.7 and never hand-picked (Kain, S085, V3)
4. Author signature block (as DSRD 9 §22.7, band withdrawn S088)
5. The courses block: **the words at §22.10 ("Ready to Take Your Learning Further?" since Code's S147; "Want to Expand Your Understanding?" from S088 to S112)** over the one sentence Kain gave for every content page (§22.10), **two course cards, filled by the tag rule at DSRD 1 §5.7**. *The S252 ruling below (three cards at desktop, two below) is superseded by S088's three-block foot standard, on which the course row is the two cards; kept as the record.*

   | Tier | Columns (DSRD 8 §7.0, unchanged) | Cards (S252, SUPERSEDED S088) |
   |---|---|---|
   | Desktop, 1024px and up | 3 | 3 |
   | Tablet, 768 to 1023px | 2 | 2 |
   | Phone, below 768px | 1 | 2, stacked |

   The third card is withdrawn below 1024px in CSS. Without that, three cards leave an orphan on a two-column tablet row and a three-deep stack on a phone.

   **DSRD 8 §7.0's columns need no amendment.** Its 3 / 2 / 1 was already correct and already built in `cards.css` as `.product-section__grid`; no template had ever used it. The S050 build wrote its own two-column grid instead, rendering each card at 540px against a card designed at roughly 368px, which is the stretching Kain saw. The row now takes the specified grid untouched: 352px at desktop, 406px at tablet, 335px at phone, with no horizontal scroll at any width.

   *Recorded as a defect report as well as a ruling, because half of this needed no ruling at all: an open specification needed applying.*
6. Related Further Reading, nine links, with the way back and the way forwards beneath and no hairline between (§22.8, Kain S088)
7. The closing trial panel (DSRD 8 §16, the trial variant; §22.10a) **was taken off this page at S113**: Kain's "yes" in Code's sitting, on the same ground as the article at S112, because the footer carries the same $7 offer fifty pixels below it, and the built page sets `'trial' => false` accordingly. **Corrected S394 on the drift sample, which found this item and §32.6 still describing the panel as live.** *The "Next possible steps" panel that stood here is retired, §32.6.*
8. Rainbow stripe and footer (DSRD 8 §19)

**The foot is the S088 standard, corrected here at S341.** Kain's words at S088: three blocks under the body on every content page, the two course cards, Related Further Reading and the trial panel, with the page types differing at the hero and nowhere else. Code's S102 read of the built page against this section (`REPORT__DSRD_9_Section_32_Read_Against_The_Built_Book_Note_Page_S102`) found the build carrying exactly that foot while this section still described the S249 foot: three cards, two hairlines and the retired panel. The document was wrong and the page was right, per this section's own head note. Items 4 to 8 above now read as built. **One thing the read found that no ruling names: a "Share this Article" block inside the writing.** It is recorded here as present on the built page and unruled; whether it stays is for the second-look sitting.

**The S249 "Nothing else" ruling stands in spirit and is superseded in letter.** Kain ruled at S249, on the rendered page, that the article card grid, the quote card grid and the related book note cards were removed: the page was offering twelve options at its foot and reading as junk. At S088 he set the three-block foot above, which Related Further Reading's nine links are part of. **DSRD 2 §1.6 predates this ruling and is corrected to match.**

### 32.2 Container: no exception, 880px like every other content page

**SUPERSEDED BY S113 (folded S358): the page is the article's two-column grid.** Content area 1104, reading column 800, gutter 48, side rail 256, exactly as §22.2 now reads, because this page's reading area is the article's own rules rather than a copy of them. The 880 single column below is the record of what stood between S085 and S113.

**The 1200px exception is retired (Kain, S085).** It was granted at S249 only to give the travelling shelf a second column, and V3 retires the shelf. The page's writing now runs in the single 880px column at §22.2, with no width transitions, exactly as the article page does. §27 holds the ruling and the standard.

The hero stays full bleed with its own inner grid (§32.3). **The breadcrumb bar and the hero grid both sit on the 880px column (`--container-article`, `margin-inline: auto`), the same two declarations the reading column carries (Kain, S102 sitting, theme v0.167.14; his words: "bring the breadcrumbs and all of the heros content into the same width of container that the rest of the page sits in"; his eye after the ship: "the hero looks much better like this").** Measured on the deployed page at 1440: breadcrumb, hero grid and reading column all at x 280, 880 wide; at 1024 all three at x 72. *Until S343 this sentence placed the breadcrumb on the hero block at 1104px, aligned with the logo (Kain, S085 ruling 4; §27), and before S337 at the 1200px frame.* The band and its wash stay full width.

**What this settles beyond this page.** The book note page and the article page are now the same shape: same width, same two supporting blocks, in the same places. The Knowledge Hub reads as one design rather than a family of near-relations, and the quote page and the workbook page inherit that pattern rather than being offered their own version of it.

### 32.3 Hero

**Six values below disagree with the built page, and none is ruled here (S341).** Code read every hero value off the rendered page at 1440px at his S102 (`REPORT__DSRD_9_Section_32_Read_Against_The_Built_Book_Note_Page_S102`): the grid's first column renders 256px not 288; the grid gap 64px not 48; the grid's top padding 32px not 48 (with 48 on the hero itself above the breadcrumb); the hero's bottom padding 48px not 64; the overline 12px not 11; the standfirst and the body 16px not 17. The photograph, the wash character for character, the H1, the cover's ratio, radius and shadow, and the rating in words all match. Which side is right is a visual decision and is taken only by Kain's eye on the real page, so it goes to the book note page's second-look sitting in Safari with Code (the Book note page template: second look card), not onto this paper. The values below stand as written until that sitting, per this section's head note. **Amended S343.** Kain's S102 evening sitting was his eye on the whole hero at three widths, and he approved it as built at v0.167.26, so the page he approved carries the built values on all six (cover 256, gap 64, grid top 32, hero bottom 48, overline 12, standfirst 16). Code framed the sitting as ruling only what Kain raised, so the six are not recorded here as ruled; **the tables below now carry the built values as measured, each marked, and the second-look sitting confirms them on the page rather than re-deciding them from this paper.** Chat's reading at S343, overturnable.

**Corrected S410 (Chat, while writing the page's build sheet):** two values in this subsection were superseded at Kain's S116 sitting with Code (recorded at DSRD 8 section 31) and the S150 approved prototype carries the S116 values: **the hero badge is deleted whole** (the badge appears once, in the last section, section 32.4), together with the standfirst's 42ch cap and the button row's 152 clearance; and **the phone cover is capped at 240 wide, not 320**. The S102 text below is kept as the record; where it describes the hero badge or the 320 cover, the page and the sheet (`BUILD_SHEET__The_Book_Note_Page.md`, Book Note Page folder) govern.

**Four more rulings on this hero, S132 (Kain, in Safari with Code, options rendered as Harness Rule 7 asks). Recorded in full at DSRD 8 §28; named here rather than restated, per standing rule 24.** Desktop: the cover now starts level with the top of the breadcrumb, so the breadcrumb and the words share the left column and the cover owns the right column from the band's top edge (theme 0.659.0), which changes the grid description below. Tablet and phone: the breadcrumb runs on one line, the book sits lower, and the Amazon button sits directly under the cover rather than beside the words (theme 0.660.0). No Know Your Psychology mark on book notes; it stands unchanged on articles and quote pages (theme 0.661.0). The desktop cover stays 256px, confirmed rather than changed. A fault found in the same sitting, not a ruling: the cover's spare height was stretching the breadcrumb's box, so a flexible fourth grid row now takes the surplus (theme 0.661.1). **The property tables below have not yet been re-measured against these five changes; that re-measure is Code's, next time this page is opened in a factory session.**

**And the S115 refinements to this hero (Kain, Code's S115 sitting, theme 0.406.0 to 0.411.0; recorded in full at DSRD 8 §28, folded S382; pointer added S385).** The date line takes the author line's size and weight; the heading is composed from the book and the author's name with the stored title untouched, and the separate author line under it goes; the folded-heading rule is corrected for it and an author's name never breaks across two lines; a heading of three lines or more never ends on a stranded word; the lighter half of the heading begins after the colon; the closing paragraph steps down one size. **Read the "Author line" row in the table below with this in mind:** the separate author line is gone from the hero, the author now sits in the heading.

Full bleed. Background: `images/bookshelf-book-notes.webp`, `background-position: center 22%`, `background-size: cover`. This is Kain's own photograph (its master lives in the Book Note Page folder's `Page Images`), chosen by him at S249 over an invented eight-tone colour palette, on the principle that the page should carry brand imagery rather than colours conjured for it.

One gradient wash over the image, an annotated one-off per DSRD 7 §4.5:

`linear-gradient(100deg, rgba(53,65,73,.93) 0%, rgba(53,65,73,.86) 46%, rgba(53,65,73,.62) 100%)`

The rgb values are brand dark #354149. Corrected in session from two different hand-typed colours that were neither brand dark nor each other; the correction is the reason the value is written out here in full rather than described.

**The fade is the book note's, not the family's (Code, S108; recorded S357).** It lets the shelves show beside the title. The quote page takes the same band with no fade, because it puts content (the quote card and the More Quotes column, DSRD 8 §30) in the bright corner, and photographed, white text sat on pale spines. The article page's band takes its ground from a token with this photograph as the fallback, and uses the article's own picture (§22.4).

**The same image and wash appear again behind the closing panel (§32.6),** deliberately, so the page is topped and tailed with one motif. Kain's design decision.

| Property | Value |
|---|---|
| Container | Breadcrumb bar and hero grid at 880px, `--container-article`, centred (Kain, S102, v0.167.14). The band and its wash stay full bleed |
| Grid columns | Cover, then 1fr. The cover measures 256px on the built page at 768 and up (this paper held `--bn-cover-w` 288px; built value, see the note above). **Two columns hold down to 768** (Kain, S102, v0.167.23: "snap all of the text to sit next to the book image"); at 767 and under the grid is one column, cover above the writing |
| Grid gap | 64px on the built page (this paper held `--sp-2xl` 48px; built value) |
| Grid padding-top | 32px on the built page, with 48 on the hero above the breadcrumb (this paper held 48; built value) |
| Hero padding-bottom | 48px on the built page (this paper held `--sp-3xl` 64px; built value) |
| Breadcrumb padding-top | `--sp-lg` 24px |
| Phone cover, 767px and under | Centred in the column, capped at 320px wide, 2:3 (Kain, S102, v0.167.24 and v0.167.25; supersedes the S086 256 cap). At 390 it measures 320 by 480 at x 35, 15 clear each side. Named by Code, not acted on: the uploaded covers are small (this page's is 316px wide) and have never been through the pipeline's book-cover slot, so they read soft on a retina screen at any size; a cover run for the factory, not a theme edit |

The cover: 2:3 aspect ratio, `--bn-cover-radius` 4px, `--shadow-cover`. Both are named values new at S249 and are defined with the component at DSRD 8.

The stack to its right, in order, each with its margin-bottom:

| Element | Type style (DSRD 7 §3) | Colour | Margin-bottom |
|---|---|---|---|
| Overline `Book note category · {Category}` (wording Kain, S102, v0.167.15) | Como Overline, 600, 0.08em, uppercase; 12px on the built page (this paper held 11) | #F5A05C | `--sp-md` 16px |
| H1, `{Book}: Summary and Key Ideas` (§32.8) | Como **H1 Page Title 33px/700**, line-height 1.15, **and no letter-spacing** (corrected S355) | white | `--sp-sm` 8px |
| Author line, `Book Authored by {author}`, linked; renders only when the record names an author (Kain, S102, v0.167.16) | Mulish 16px/500 (Kain, S086: "the same sized font please"; this paper held Lead Paragraph 19px/500) | white 70%, 1px underline at 3px offset, hover #F5A05C | `--sp-lg` 24px |
| Standfirst: `post_excerpt`, then one space, then the fixed sentence **`Keep reading to decide if this book deserves a spot on your shelf.`** on every note whatever its rating (Kain, S407; built 0.707.133; replaces the S102 sentence "Essential reading for all Achologists.", Kain, v0.167.21) | Mulish Article Body, line-height 1.75; 16px on the built page (this paper held 17); max-width 46ch, **42ch on a badged desktop page** so its last lines clear the badge | white 85%; the fixed sentence in the standfirst's own type and colour | `--sp-xl` 32px |
| Button row: the two buttons, and on tablet and phone the badge as the row's last member (below) | DSRD 7 §5.1, padding 12px 24px, radius 10px, flex gap `--sp-md`; on a badged desktop page the row keeps 152px clear on the right, a second button wrapping onto its own row | see below | none |

**No rating label, no scale words and no ticks anywhere in the hero (Kain, S102, v0.167.17 to v0.167.21).** The words "Achology rating" left the page at v0.167.17 on his spoken word ("lose the words Achology rating on the page"). The per-step sentences ("Highly recommended reading for all Achology members" and its siblings) lived for one ship and were replaced by the single fixed sentence at v0.167.21 on his typed word: "For simplicity, just use Essential reading for all Achologists." He named this as a change on the plan and asked that Chat be told so. The record field, the master column and the importer still carry `achology_rating`; on the page it now decides one thing only, whether the badge appears (§32.9 item 1). **S407 note: the single fixed sentence of v0.167.21 was itself replaced by Kain at S407 with "Keep reading to decide if this book deserves a spot on your shelf." (built 0.707.133); the sentence quoted above is kept as the record of the S102 ruling.**

**The Essential Reading badge (Kain's own design; S102, v0.167.18 to v0.167.26).** A 1080px square transparent PNG Kain designed himself: a hexagonal seal, orange border on brand dark, the Achology mark over "Book Notes", an orange band reading "Essential Reading" with a check, five yellow stars beneath. Its master is in the Book Note Page folder's `Page Images`; it went through the image pipeline at the square slot, 128 and 256 wide, into the theme's `images/knowledge-hub/`. **It renders only where `achology_rating` is `essential-reading`** (eight of the 65 live notes at S102); the other two steps show no badge and no other mark. Alt text is empty on purpose: the standfirst states the fact in words and the badge is its visual seal. The five stars stay on Kain's word (v0.167.19: "keep the badge as it is"), which supersedes the "never as stars" half of §32.9 item 1.

| Tier | Where the badge sits | Size |
|---|---|---|
| Desktop, 1024px and up | Absolutely positioned in the hero grid's bottom right corner, its foot on the grid's foot and its right edge on the container's right edge (v0.167.19). The standfirst caps at 42ch and the button row keeps 152px clear so nothing runs under it | 128px |
| Tablet, 768 to 1023px | The button row's last member, static, pushed to the row's right edge by an auto margin, the Amazon button centred against it: the container's bottom right corner (v0.167.26, superseding v0.167.23's placement beside the button) | 96px |
| Phone, 767px and under | The same placement as tablet, at the right end of the button row under the centred cover (v0.167.24). Where a note has two buttons they wrap and the badge takes the right end of the last row | 88px |

Measured on the deployed page at v0.167.26: at 1440 the badge sits at x 1032 to 1160 with its foot on the cover's foot; at 768 its right edge is 0 from the grid's right edge, its foot 0 from the grid's foot, and the button's centre is on the badge's centre; at 390 the same corner at 88. No horizontal overflow at any width.

**The primary orange button is `Learn About this Author`** and links to the author's own website (`author_website_url`). **The secondary outline button is `Get this book at Amazon`.** Kain's ruling, S249: the author is the prominent call to action in the banner. Both are external and take DSRD 7 §1.0 in full.

**No affiliate disclosure sentence.** Removed at S249: the button label says it. **No page-count or reading-time line.** Removed at S249: no fields exist and no columns are being added for one line.

The author link resolves to `/learn/authors/{author_slug}/`; the button resolves to `author_website_url`. Both are new CSV columns ruled at S249. The slug is never derived from `source_book_author`, because names like "Bessel van der Kolk" and "Viktor E. Frankl" do not sanitise predictably.

**`author_website_url` is withdrawn, ruled by Kain S336, and this leaves the primary button without a destination.** Code found at S090 that the field is read by the template, guards that button, and is held by no column in the master and no field in any book note record. It has therefore never been populated on any live book note. Kain ruled at S336 that it is deleted rather than sourced: filling it is 620 books by hand and again for every book added, and Achology now has 51 author biographies of its own, so an external site is the weaker destination as well as the dearer one.

**Where the primary button points instead is not settled here, deliberately.** The obvious answer, the Achology author hub, duplicates the author-name link a few lines above it in the same hero, and the hero is a rendered page Kain approved at S250. It is a visual decision on his own approved work, so it goes to a Safari sitting on the book note page with the options rendered tabbed (standing rule 16), and nothing in this hero changes until then. **Until it is ruled, the hero stands exactly as built**, which costs nothing, because the button has never had a destination.

**`goodreads_url` is withdrawn in the same ruling and is derived instead** from the ISBN the master already carries, at `https://www.goodreads.com/book/isbn/{isbn}`, so the Goodreads rating stops printing as a claim with no source. The guard becomes the ISBN rather than a stored URL, and a book with no ISBN prints its rating unlinked, exactly as today. Two checks were sent to Code before either change is built: whether that Goodreads route still resolves, tested on three real ISBNs, and how many master rows carry an ISBN at all.

**The page title is one size on every Knowledge Hub page (ruled by Kain, S108; recorded S355).** His question, asked with three page types open in Safari at once: is the article heading the same size font in each type of post? It was not. The quote page and the article page set the title at the 33 step; the book note set it at 42. **Every Knowledge Hub page type sets its H1 at the 33 step**, whatever the page looks like around it: the quote page, the article, the book note, and the workbook page when it is built.

**The tracking goes with the size, and this is the part a document usually misses.** The `-0.01em` belongs to the 42 step, where it stops large capitals drifting apart. At 33 the H1 step carries none. Keeping the tracking would leave this page's title set differently from the other two while appearing to match, which is worse than the original fault because it looks fixed.

**Why the fault existed.** The scale in `base.css` names the 33 step "H1 Page Title" and the 42 step "Hero Heading". They are two different roles. The book note has a page title that happens to sit inside a hero band, and it had taken the band's setting rather than its own. **Nothing in the written record would have surfaced this**: each page's own spec was internally consistent, and only putting them beside each other showed it.

**It is enforced rather than remembered.** `page_gate.py` checks every page's H1 against its `H1_SIZE` constant, so the rule reaches the workbook template before that template is written. Code found at S108 that the constant had read 32 since S056, when Kain's own ruling moved the scale to 32 to 33 and `base.css` was corrected but the gate was not; a real 33 missed a stale 32 by exactly the 1.0 tolerance and passed. **A check that passes the right answer for the wrong reason also passes the wrong answers either side of it.** Corrected to 33.

**One thing this does not settle:** whether the book note's hero should still be a hero at all, now that its title is the same size as an article's. That is a visible design question, so it is Kain's on a rendered page.

### 32.4 Reading zone

One 880px column (`--container-article`), no grid and no second column (Kain, S085, V3). The vertical rhythm, the block margins, and how the Table of Contents and the course card sit against the writing are deliberately not written here. They are Kain's on the rendered page at the spacing sitting with Code, and recording them now would put half a decision on the page as though it were a whole one.

The left column renders `post_content` at DSRD 7's Article Body style: Mulish 17px, line-height 1.75, brand dark #354149. H2s are Como 24px/600 with 32px above and 16px below. A blockquote takes the registered Pull Quote style: Mulish 18px/400 italic, line-height 1.6, 3px brand orange left edge, 20px padding-left. No new type styles were created for this page.

**The badge appears a second time, at the head of the last section (Kain, S102, v0.167.22; his eye: "great").** On an Essential Reading note the same badge is inserted directly after the H2 of heading 5 (§32.7), found by the same `sanitize_title()` id the contents list and the anchors read, and floated right so the section's first lines run round it: 128px square, the writing's 40px gutter on its left, 16px beneath, and a 4px top margin so its top sits on the top of the first line's type rather than its line box (measured: a difference of 0 at 1440 and at 390). On a phone it is 96px with a 24px gutter, leaving the lines beside it at least 230px of the 350 column. `loading="lazy"`, alt empty, for the same reasons as the hero badge. Kain's typed instruction: "place the badge up against the right side of the container in the final section 'What are Your Next Learning Steps?' and just align the top of the badge with the top of the top line of text."

### 32.5 The travelling shelf (RETIRED, Kain S085)

**The shelf is gone.** The narrow column that carried the book cover, the `Get this book at Amazon` button, the `See the related course` button and the contents list down the right of the page is retired with the 1200px container that existed to hold it.

**Its contents are not redistributed by this document.** The contents list becomes the Table of Contents at the top of the writing (§32.1), and it stays hardcoded in the template rather than parsed from the body, which the locked five headings (§32.7) still make possible. Where the buy decision and the course now sit is part of the spacing sitting, not a paper decision taken here.

**Two arrangements were built, seen and passed over**, recorded so they are not proposed again: the cover and Buy button in a box out in the left margin (V4), and the same box inside the writing with the words wrapping around it (V5).

**One consequence outside this document, now closed (S313).** The shelf's own anatomy at DSRD 8 §20, and the three-tier responsive spec at DSRD 8 §20.4 written around it, were orphaned by this ruling. Both are now marked retired and void in that document, kept whole as the decision record so a reader meeting the `.shelfp` class family in an old stylesheet or prototype knows it is dead rather than missing. **One token goes with them:** `--bn-shelf-w` 264px is dead and leaves `base.css` when Code next opens it; the three hero tokens beside it stand.

### 32.6 The closing panel (RETIRED S088; the trial panel that replaced it came off at S113)

**Retired by Kain at S088, on the rendered page**, with the three-block foot standard (§32.1, §22.10a): the page closes on the shared trial panel, DSRD 8 §16's trial variant, whose copy is Kain's (second paragraph ruled S341). **Superseded at S113: the trial panel itself then came off this page, as it came off the article at S112 (Kain, "yes"), so the page now ends on the author signature, the two courses and the footer, as the S113 comment in the built template records (see §32.1 item 7).** The "Next possible steps after this Book Note" panel below was the only block of the four that existed on one page type, and it went for that reason. Its copy is Kain's own words and is preserved here and in `RULING__The_Content_Page_Foot_Is_One_Standard_S088` so it is recoverable. *Corrected S341 on Code's S102 read; this subsection described the panel as live until then.*

*The superseded S249 specification, kept as a record:*

The DSRD 8 §13 "Where next?" panel, used as specified, with one approved change: **its background is the bookshelf image and the §32.3 wash instead of `--color-off-white`,** so its title renders white and its lead white at 78%. The three row cards stay white and untouched, so the component's own contrast is unaffected. Annotate the background in place naming Kain and S249.

The copy is Kain's own words, verbatim, and is not edited:

**Title:** Next possible steps after this Book Note
**Lead:** Three ways to deepen the integration of ideas inside the Knowledge Hub.

| # | Row name | Row description | Destination | Icon (DSRD 7 §5.2) |
|---|---|---|---|---|
| 1 | Browse the Articles that have been inspired by this book | Each article focuses on a core idea from this book and explores it thoroughly. | the book's own article set | `BookOpen` |
| 2 | Explore our interpretation of Quotes taken from this book | We do quotes differently. We reflect on them carefully and discuss them in full. | the book's own quote set | `Quote` |
| 3 | Read the other Book Notes we have written in this category | We might inspire your next book buying decision, or simply inspire you, period. | `/learn/{kh_category}/book-notes/` | `LibraryBig` |

**Row names carry no counts, deliberately:** a hardcoded "five articles" is wrong the day a book has four.

**Rows 1 and 2 resolve to the two per-book listings, ruled S251:** `/learn/{kh_category}/book-notes/{slug}/articles/` and `/learn/{kh_category}/book-notes/{slug}/quotes/`. Both are registered in DSRD 1 §2.4 and both render through the DSRD 2 §1.4 listing template with the filter changed from category to source book. The gap that stood here is closed; nothing invents an address.

### 32.7 The five body headings (LOCKED; SUPERSEDED S115, RECORDED S360; SUPERSEDED AGAIN S150, RECORDED S408)

**From 22 October 2026 the fifth heading below is replaced by "A Question That Deserves an Honest Answer", and an unheaded Hook precedes the first heading, by the book note standard, "A Book Note Runs Hook, Book, Look and Took Under Five Locked Headings and Ends on One Honest Question", in The Newsroom Vault's Shapes folder (Kain's yes, 22 October 2026, Session 440; written by Chat).** The five headings now in force are: What This Book Is Saying; The Author's Background and Perspective (with Authors' for more than one author); What Could This Book Mean for Society?; What You Could Learn From the Book; and A Question That Deserves an Honest Answer. Because the travelling shelf's contents list is built in the theme from these headings, Code changes the template when the first rewritten book note lands, as a line on Backlog: Code says. The Session 150 five below stay as the record.

**The five headings now in force (Kain, S150, live with Code in Safari; agreed with Kain in the sitting ("yes") from his own proposal, with two fixes; recorded by Chat S408 from RULING__The_Rest_Of_The_S150_Sitting item 6).** Every book note carries these five H2s, in these words, in this order. No H3s. No sixth section.

1. What This Book Is Saying
2. The Author’s Background and Perspective (“Authors’” on a book with more than one author; five on the build site)
3. What Could This Book Mean for Society?
4. What You Could Learn From the Book
5. What Might Your Next Learning Steps Be?

**How they stand in the build, at S150 (Code):** the theme carries the new five (live from 0.707.133) with an S150-only fallback that keeps the old list on any page whose body still carries the old headings, so no contents link breaks; the import check (`tools/book_note_import.py`) and the heading tool (`tools/book_note_headings_S314.py`) carry the new five. **The 150 book note bodies are not yet changed.** They wait on a publishing clearance: the S150 run of `publish_gate.py` was measuring 403 pages (the host firewall refused the Chrome 120 identity the tools presented; fixed in commit 0dc5d3b) and was stopped, and Code's S151 stopped it again before it finished. When the clearance runs and the bodies carry the new five, the fallback is removed. Until then the page and the install disagree on purpose, and that is not drift. The book note master records and the `book-note` skill carry the new five from S408.

**The S115 five below, now superseded, kept as the record.** The text from here to the end of this section describes the S115 ruling and everything before it.

The S115 five, in these words, in this order:

1. The Argument at the Heart of the Book
2. The Background the Author Comes From
3. Practical Applications Beyond the Book
4. What this Might Possibly Mean for You
5. What Your Next Learning Step Could Be

**All five superseded at once, Kain, live in Code's S115 sitting in Safari, on the rendered book note page (`RULING__Kains_Five_Book_Note_Headings_S115`).** He judged the earlier five as read out loud: "some of them just read a little bit arrogant ... a little bit presumptuous rather than inviting. I'd like them to read just in a slightly more inviting and broader, yet more compelling frame." He wrote these five himself over four passes, each measured in the rendered contents panel rather than judged on the page alone: they hold to the same working limit as before, about 38 characters at the panel's 256px width (the fourth heading is the longest at 38). **The fourth heading arrived carrying a question mark, the only one of the five to; put to him rendered, he ruled "drop the question mark", so all five read as statements.** This reverses part of S314's own change below, which had added question marks to headings 3 and 4; nothing is inconsistent, it is simply a later ruling on the same two headings. Two readings were put to him and kept on purpose rather than missed: "Might Possibly" in heading 4 is a hedge stated twice, raised three times and kept each time; "Learning Step" in heading 5 carries the assumption the reader is on a course, one of his three original objections, and he put it back deliberately in his final pass.

**The order this supersession runs in is the reverse of S314's, and deliberately.** S314 moved the install and the drafted records together, in one pass. This time nothing changes in the theme, the importer's locked headings list, or `content_gate_standards.json` until every one of the 99 currently published book note records carries the new five in its body, because `content_gate` refuses a record whose body does not hold exactly the locked five in exactly this order; changing the theme or the gate first would fail all 99 at once. The records move first (Cowork, sequenced by Chat, briefed S360), then the five strings in `single-book_note.php` and the gate standard (Code), then a re-import or in-place update of the 99 (Code). Until the records carry the new five, this section's headings and the live install's disagree on purpose, and that is not drift.

**The five superseded by this ruling, kept as the record, exactly as S322 kept heading 5's earlier wordings below.**

| Wording | Ruled | Superseded by |
|---|---|---|
| 1. What this Book is Actually Saying | Kain, S314 | S115 |
| 2. Where the Author is Coming From | Kain, S314 | S115 |
| 3. What Could this Mean for Society? | Kain, S314 | S115 |
| 4. What You Can Take From the Book | Kain, S314 | S115 |
| 5. What are Your Next Learning Steps? | Kain, S088 (the fourth wording that sitting; corrected into this section S322) | S115 |

**Heading 5's own earlier history, kept exactly as S322 recorded it, since it was ruled four times before S115 made it five for five.** It was ruled four times on one day at Code's S088 sitting, and the fourth wording (the row above) was the live one until S115. Kain judges a heading by seeing it on the real rendered page in Safari, never by reading it here, so each wording was built and deployed before it was replaced. That is the method rather than churn. The other four headings are unchanged from S314.

**Where the live wording is read from.** Code's `RULING__Heading_Five_Was_Ruled_A_Fourth_Time_And_Never_Filed_S089` reads it from three places in the build that agree: the importer's locked headings list, the template's section list, and the theme commit of 31 August 2026 carrying it.

**The superseded wordings, kept as the record.** Each was live and built before it was replaced.

| Wording | Ruled | Superseded by |
|---|---|---|
| Where you could take this next | Before S314, sentence case throughout | S314 |
| Where Could Further Exploration Lead You? | Kain, S314 | The S088 sitting |
| What's Left For You to Explore? | Kain, in the S088 sitting | The fourth wording, an hour later in the same sitting |

**One further wording was live inside the S088 sitting and is not written here**, because no file read this turn records its exact words. Code's S089 ruling states heading five was ruled four times that day; three of the four are above and the fourth is the live one.

**Why this section carried the wrong heading between S320 and S322, recorded rather than quietly fixed.** Two Code ruling files in the same channel folder disagreed about which wording was live, the older one was read, and this section was corrected to the third wording while the build already carried the fourth. Nothing in the build was ever wrong. **A ruling file states a value at the moment it was written; where two disagree, the build is read and the later file wins.**

**Changed at S314 on Kain's ruling.** The previous headings used sentence case throughout and heading 5 read "Where you could take this next." Kain moved to title case and rewrote heading 5 deliberately: the open question form leaves the reader with an open loop rather than an instruction, which he wants on every book note. Headings 3 and 4 also gained question marks. The change applies to every book note going forward and to the 51 already drafted, corrected in the same pass Code and Kain use to confirm the book note template in Safari.

**The install and the records move together.** Sixty five book notes are live. One carries the ruled wording; the rest move on Kain's word. The drafted records in the Content Records folder are corrected to the live wording in the same pass, because a rebuild from uncorrected records reverts the install, which is what happened to the biography titles at S306.

**The state of those records, read by Code at S089 and recorded here rather than assumed.** All 108 record files in the book note folder of Content Records carry the original sentence case headings, and not one carries any later wording. So the sweep is the whole set at once, to the wording above, and not a partial correction from S314.

They arrive inside `post_content` from the CSV; the template does not render them. They are locked because the Table of Contents and its anchors depend on them being identical across 598 pages. The list moved out of the retired shelf at S085 (§32.1, §32.5) and the dependency moved with it, unchanged.

**These supersede the internal production names** in DSRD 2 §3.1 and in the `book-note` skill (A Spoiler for the Book, Author's Perspective, Societal Application, Personal Application, Provocative CTA), one for one in order. The skill's own build note named this as an open page-design point; S249 closes it.

### 32.8 Titles and metadata (SEO title and H1 by Kain's S102 pattern; keyword and description by stage 0, Kain S341)

**The Rank Math SEO title takes one pattern: `{Book}: Summary and Key Ideas | Achology`** (Kain, in Code's S102 sitting, 5 September 2026, on four options rendered in text on the same book; his words: "go with number 1 please"; filed as `RULING__Kain_Chooses_The_Book_Note_Title_Pattern_Summary_And_Key_Ideas_S102.md`). The book's name comes first because it is the focus keyword and the title must carry it verbatim. Two mechanical tiers: where the full pattern runs past 60 characters the ending `| Achology` drops (`{Book}: Summary and Key Ideas`, 12 of the 65); where even that passes 60, the shortest tier is `{Book}: Summary`. Where a book carries a long subtitle, the `{Book}` slot carries the keyword's own form of the name, which is what the record's keyword already is. Applied to 62 of the 65 published notes at S102; three (`free-will-sam-harris`, `emotional-leonard-mlodinow`, `nature-emerson`) waited on a keyword decision, taken at S342 (their keywords take the form `{book} by {author}` so a natural title can carry them verbatim; recorded in the keyword register and filed to Code the same session).

**How this sits with the S341 ruling below, corrected the same evening.** S341 retired the fixed S249 formulas for the title, the title tag and the description in favour of each note's own stage 0 demand check. Kain's S102 rulings narrow that twice: the SEO title takes the pattern above, and, ruled later the same evening on three rendered samples in Safari, **the page headline (`post_title`, the H1) takes the same pattern without the `| Achology` ending**, `{Book}: Summary and Key Ideas`, a question-mark title taking no colon, applied by Code to all 65 and read back (`RULING__Kain_Sets_One_Headline_Pattern_For_The_Book_Notes_S102.md`; his words: "yes, the page headline, which is what will show up in search in the knowledge hub, ie, what each article is actually called"). What the stage 0 check still decides is the focus keyword and the description. Recorded this way by Chat at S342 as the reading that lets Kain's rulings stand together; overturnable.

*What S341 ruled, kept in place because it still governs the description and the keyword (its title and H1 clauses are superseded by the two S102 rulings above):*

**Every book note's title, title tag and description are decided by its own stage 0 demand check, never by a formula** (Kain, S341, on Code's S102 read of the built page and his report that none of the 65 published notes replaces an old page). The reason: a title fixed in advance cannot be a question people actually ask, and the site's standing rule is that every title is a proven question (standing rule 14; the rank-math-90 skill's stage 0; DSRD 2 §0.0). The 65 published notes, drafted at S086 before stage 0 existed, carry the bare book title as H1 and `{book title} book summary` as focus keyword on 62 of them; all 65 take a fresh demand check, commissioned to Cowork at S341, and each title and keyword follows what its check finds. What the check must produce is the rank-math-90 skill's, not this section's.

*The superseded S249 formulas, kept as a record because "Understanding" was chosen from thirty candidates and the reasoning may be wanted again:*

**H1 formula:** `Understanding {Book Title}: Key Ideas`. This is `post_title`. "Understanding" was chosen by Kain from thirty candidates because it holds true across all 598 books, claims no credential, passes no verdict on the book, and is short enough to leave the book title loudest. "A Guide to Understanding" was considered and rejected: it is the phrase the study-guide sites own.

**Title tag ladder.** The longest rung that fits 60 characters wins. No brand suffix. Run mechanically at CSV build; no human chooses per book.

1. `{Book Title} by {Author}: Summary, Insights and Key Ideas`
2. `{Book Title} by {Author}: Summary and Key Ideas`
3. `{Book Title}: Summary and Key Ideas`
4. `{Book Title}: Summary`

"Summary" stays on every rung because it is the only word in this field with real search demand. The competitive finding behind the formula (S249): SparkNotes, SuperSummary, Four Minute Books, Growth Summary and Daily Stoic all use book title plus "Summary" or "Key Lessons", and none of them claims a discipline. Search Console cannot inform this: the live property covers only the 192 help URLs.

**Meta description formula:** `A considered reading of {Author}'s {Book Title}: what the book argues, where {Surname} was coming from, and what you can take from it.`

### 32.9 Open items: seven of the nine closed; two reopened at S085

Seven of the nine items listed here at S249 are closed. Two of them, numbers 8 and 9, were closed against the travelling shelf and reopened when Kain retired it at S085. **This section is no longer a complete go-live spec**; see Status at the head of §32.

| # | Item | How it closed |
|---|---|---|
| 1 | Where the two ratings appear | **Superseded S102, written S343.** `achology_rating` now decides one thing on the page: whether Kain's Essential Reading badge renders, in the hero and again at the head of the last section (§32.3, §32.4), on the top step only. The label `Achology rating`, the scale's words per step and the ticks are gone from the page (v0.167.17 to v0.167.21); the five stars are on Kain's own badge by his design and his word (v0.167.19). Every standfirst ends with the one fixed sentence whatever the rating (the S407 sentence "Keep reading to decide if this book deserves a spot on your shelf."; the S102 one is superseded). **Consequence, named so nothing is built on the old assumption:** the scale's three steps are no longer distinguishable on the 57 Recommended and Highly Recommended pages; the record carries them, the page says nothing. Whether the scale is read anywhere else on the site (a hub card, a list, a filter) is a new decision, not made by this ruling. *The S250 wording, kept as the record: renders in the hero as `Achology rating · {value}`, in the editorial scale's own words and never as stars.* `goodreads_rating` rendered in the travelling shelf as `Rated {value} on Goodreads`, an external link; **with the shelf retired at S085, where that line now sits is part of the spacing sitting and is not written here** |
| 2 | The fallback when `book_cover_image` is empty | A template-generated brand dark panel carrying the book title in Como, so the hero never breaks. S250 |
| 3 | The OG image | DSRD 7 §15.1's existing Book Note template is adopted unchanged. S250 |
| 4 | Whether the second course card is tag-generated | Superseded S255. Every course card on the page is filled by the tag rule at DSRD 1 §5.7, and `primary_recommended_course` is retired: it was never populated on any of the 620 master rows and §5.7 postdates it. The note's fifth section names whichever course the rule puts in card one. Closed S250, superseded S255 |
| 5 | The course section's subline | Set verbatim at S250: `Thought-provoking courses that expand on the concepts in this book.` **Superseded S088:** Kain gave one heading and one sentence for both content pages and refused the one edit Code made to it ("please accept the copy i gave you"), so the book note carries the article page's sentence, deliberately (§22.10). Code's S102 read confirms the build carries it |
| 6 | The author bio line | Pulled verbatim from the people registry (`people-setup.php`), never written into a page. The invented line is removed. S250 |
| 7 | What the closing panel does at launch | Dissolved rather than answered at S250, then **void at S088**: the panel is retired (§32.6) |
| 8 | Whether the contents list highlights the section being read | **Reopened S085.** It was built as scrollspy against a shelf pinned beside the text, and the shelf is retired. Whether a Table of Contents at the top of the writing highlights anything at all is part of the spacing sitting |
| 9 | Tablet and phone | **Superseded S085; the hero's tiers ruled S102.** The three-tier spec at DSRD 8 §20.4 was written around the shelf. With one 880px column at every width, the page inherits the article page's own responsive behaviour for the reading zone. The hero's own three tiers were ruled by Kain in Safari at S102 and are written at §32.3: two columns hold to 768, one column with a centred 320 cover under it, and the badge's three states |

**The one dependency that stood outside the nine** is also closed: rows 1 and 2 of the closing panel now have addresses (§32.6, DSRD 1 §2.4, S251).

*Production implementation notes for this page will be in the Production Implementation Notes document once the build runs.*

---

### 32.10 The hero from S162 and S163

The book note takes the Soft Light hero and its page changes in §22.15 and §22.15a, and the Ring contents panel and the close of §22.15b (S164 and S165), (S163: the Drawn Bubble contents, the panel down to the two paths, the two paths foot) whole. Its own differences: the cover (the book component, straight, never tilted) stands on a faint bookshelf fading into the cream; "View on Goodreads" sits in the date line before the word count; below 1200 the Amazon and author-site buttons sit in the side panel's strip under the contents. Where §32.3 says otherwise, §22.15 wins.

## 33. Our People Page Layout (APPROVED AND BUILT, Kain by eye, Code S062 and S076)

The Our People page introduces every person who writes and teaches for Achology: the management team, the guest instructor, the community eldership, and the editorial squad. One page, one instance, live at `/about/instructors/`. It is **not** an Author Hub (DSRD 1 §2.4), which covers the external authors the Knowledge Hub writes *about* and lives at `/learn/authors/{slug}/`. Two different pages doing two different jobs, and DSRD 1 §2.2 carries the distinction in writing because it has been confused before.

Designed live in Safari across Claude Code's S062 and S076 sittings and approved whole by Kain by eye, under the standing rule 16 Safari surface. Every value below was read from the built theme at v0.81.0 and reported by Code at his S076; none of it is invented for this document. Where the built page and this section disagree, the built page is the ruling and this section is the thing to fix.

**This section was written after the page, at S300, and that is recorded rather than smoothed over.** It was owed from S062 and never started, and the board card was marked Done while this half was unwritten. A page approved by eye with no written layout is a page nobody can audit and nobody can rebuild.

---

### 33.1 The job

**This page exists to make a visitor who is weighing Achology up trust the people behind it enough to carry on into the academy or the Knowledge Hub.**

One action, one reader. The action is *carry on* — not *buy*. The page removes the "who actually are these people" doubt; the course, school and article pages do the rest.

**Subordinate job:** to be the destination every Knowledge Hub byline resolves to (DSRD 1 §3, writing author). This adds one requirement — every pen name and instructor whose name appears on the site appears here — but it never reorders the page.

---

### 33.2 The reader's arrival state

No analytics exist for a page that is not yet public, so most lines here are assumptions and are marked as such, per the composition standard. The evidenced lines are read from the site's own link map, not from behaviour.

| # | What is true on arrival | Basis |
|---|---|---|
| A1 | They arrived from the footer's "Achology People" link or from a byline on a Knowledge Hub piece | Evidenced from the link map: DSRD 1 §13.2 column 1, and the byline rule at DSRD 1 §3 |
| A2 | Where they came from a byline, they want one person, not fourteen | Evidenced — the byline names a person and links here |
| A3 | They are mid-decision about Achology itself, not about a single course | **Assumption.** Confirmed after launch from Search Console and internal referrer data |
| A4 | They expect a corporate team page and are ready to be unimpressed by one | **Assumption** |
| A5 | They do not know the difference between an Achology instructor and an author the Hub writes about | **Assumption**, and the reason DSRD 1 §2.2 carries the distinction |

---

### 33.3 The required state, as changes

Each change is one sentence in the reader's voice. This list is the page's entire content brief.

| # | Change |
|---|---|
| C1 | "I now know who runs this, and they are named people rather than a brand." |
| C2 | "I now know a recognised authority in this field teaches here." |
| C3 | "I now know there is a body of experienced people around it, not one man." |
| C4 | "I now know who writes the content I have been reading." |
| C5 | "I can read as much or as little of any of them as I want." |

Ordered by dependency: who leads, then who vouches, then who surrounds, then who writes.

---

### 33.4 Page structure (top to bottom)

Four people sections, in this order. **The order is the page's meaning**, and it changed at Code's S076 on Kain's instruction: the eldership moved above the editorial squad.

| # | Block | Heading | Who | Change carried | Treatment |
|---|---|---|---|---|---|
| 1 | Breadcrumb | — | — | orientation | 1200px frame (§27) |
| 2 | Page header | *none* | — | orientation | title, intro, the Read the Founders' Letter button, and the picture; its own phone treatment. Added S384 from Code's S102 pre-sitting report: this row was missing, though the block has been on the built and approved page throughout |
| 3 | Management team | Achology Management Team | Karen A. Ramsay, Kain Ramsay | C1 | rows (§33.6) |
| 4 | Guest instructor | *none, by Kain's S062 ruling* | Prof. Gerard Egan | C2 | grey panel (§33.7) |
| 5 | Community eldership | Achology Community Eldership Team | six elders | C3 | cards (§33.8) |
| 6 | Editorial squad | The Achology Editorial Squad | eight pen names | C4 | cards (§33.8) |
| 7 | Closing trial panel | *carried in the component* | everyone | invitation in | `achology_trial_panel()`, DSRD 8 §16 |

**Block 7 was added at S337, after Code shipped it at his S097 (theme v0.161.0).** This table listed five blocks and named no closing block at all, so the page's own structure section was silent on how it ends. It ends on the trial panel: the same block every article, book note and help answer closes on, in the same `achology_warm_room()` component the enquiries panel used, so the shape, the reading column and the 48px hairline above it are unchanged and only the words, the picture and the button destination differ. Ruled by Kain at Code's S097 on a screenshot of the block, in his words: replace this with the same block we place at the bottom of all articles. **The same applies to the sixteen instructor profile pages**, which took the change in the same act, and §22.10a carries the site-wide list of what the enquiries panel still closes.

**Volume falls as the page descends** (Kain, S062). The people who lead the academy are read, the guest instructor is met, the eldership and the editorial squad are scanned. That is why one page carries three treatments rather than one, and it is C5 expressed structurally rather than written into copy.

**The sections are addressed in CSS by position, not by classes of their own**, because the template builds them from a list and their order is the meaning: `nth-of-type(-n+2)` is the rows, `nth-of-type(2)` is the guest panel, `nth-of-type(n+3)` is the cards. **If a fifth people section is ever specified, that block is what has to be revisited, deliberately.** (Block 7 above is the closing panel, not a people section, and sits outside those selectors.) Recorded here so a later builder does not add a section and find two treatments silently wrong on a page nobody thought they had touched.

---

### 33.5 Width and spacing

**AMENDED S398: the page's content sits in a 960px column, not the 880 (read 800) reading column.** Kain ruled it by eye at Code's S145 (4 October 2026), shown four tabs of the page (800 as it was, 960, 1104 full width, 1104 with the groups three across) and choosing 960, the same column he ruled for Reviews, About and Testimonials at S141 and S142. Built in theme 0.707.63 as a token reset on this page only (`.pp-page { --container-article: 960px }` in `people.css`), so the header, the groups, the closing panel and the guest panel's outward step move together; measured live at 1920, 1440, 1280, 1024, 768 and 390, centred at 960 where the screen allows and narrower below, no overflow. The breadcrumb sits in the same column, per §27 as corrected at S337. *Until S398 this sentence read "the 880px reading column"; until S337 it put the breadcrumb at the 1200px frame.* Header-to-content spacing is §26's site-wide 48px desktop and tablet, 32px below 768px. Neither is restated in values here; both are read from their own sections.

**The seventeen individual Our People pages take the same 960px column (Kain, Code S146, theme 0.707.65).** Kain's words: "Please make all of the 'our people' individual pages the same container width as the main our people page." Done as the same one-line token reset on the individual page template; measured live on all 17 pages at six widths, no sideways scroll. Recorded here at S398 from Code's RULING S146.

**A correction to §27 follows from this and is made rather than left standing.** §27's showcase-pages bullet listed Our People among the card-grid pages using the 1200px frame. The built and approved page uses the reading column, and §27's own sentence test agrees with the build: this page is biographies, and biographies are sentences. The bullet is corrected and the page is unchanged. Named as Claude's call at S300, overturnable by Kain.

---

### 33.6 Treatment 1 — the rows (sections 2 and 3)

| Element | Value |
|---|---|
| Grid | One column, `row-gap: 0` |
| Separator | Drawn **between** rows (`li + li` border-top), never around them, so a rounded hover is not cut by a line at its foot |
| Card | `padding: 24px`, `margin: 0 -24px`, `border-radius: 12px`, hover fill `--color-off-white` |
| Portrait | **128px** circle |
| Name | **24px**, weight 600 |
| Role | **16px**, `--color-orange-link`, `margin-top: 4px` |
| Biography | **16px**, `line-height: 1.7`, `--color-dark`, shown in full, never clamped |

**The role line is one size across both row sections**, ruled by Kain at S062: the guest panel's subline had to match Karen's and Kain's, so theirs grew from 12px and his shrank from 18px, meeting at 16px, which is a step on the approved scale.

---

### 33.7 Treatment 2 — the guest panel (section 3 only)

Sits inside treatment 1 and adds a tint. Built to DSRD 7 §4.4's full-bleed panel rule; nothing here is invented for this page.

| Element | Value |
|---|---|
| Background | `--color-off-white` |
| Corner | `border-radius: 12px` |
| Padding | **32px** |
| Ceiling | At **1040px and above**, `max-width: calc(880px + 2 × 32px)` = **944px** — the reading column plus a 32px bleed each side |
| The row inside | Contributes **no padding of its own**. One set of padding, not two |
| Heading | **None.** With one person in the panel a heading repeats the line beneath it, so his name takes its size instead, at **28px** |
| Hairline | The row's hairline is removed; the panel's own edge is the boundary |

**The caution that has to travel with this panel, because it was got wrong once and Kain caught it on the rendered page:** the panel is centred by the page's auto margins, so widening its ceiling is the whole mechanism. Setting `margin-inline` instead replaces those auto margins and slides the panel 112px left while still measuring the correct width. **Measuring width alone does not catch it. Position has to be checked too.**

---

### 33.8 Treatment 3 — the cards (sections 4 and 5)

Ruled by Kain at S296, in Code's S076 sitting, on a rendered before-and-after comparison.

| Element | Value |
|---|---|
| Grid | **Two columns**, `gap: 24px` (`--grid-gap`), collapsing to one column at **1023px and below** |
| Card | White, `1px solid --color-hairline`, `border-radius: 12px` (`--radius-card`), `--shadow-card`, `padding: 28px 24px 24px`, `height: 100%` |
| Hover | `--shadow-card-hover` and `translateY(-3px)`, both withdrawn under `prefers-reduced-motion` |
| Row arrow | Hidden on cards |

**The card's internal layout:**

```
grid-template-columns: auto minmax(0, 1fr)
column-gap: 16px      row-gap: 2px      align-items: start

  portrait  | name          <- 72px circle, spans rows 1 and 2
            | role
  biography (full width, row 3, margin-top 16px)
```

- Portrait **72px**, `grid-row: 1 / span 2`
- Name **21px**, row 1, `align-self: end`
- Role row 2, `align-self: start`
- Biography spans **both columns**, row 3, **no clamp**
- `.pp-card__text` takes `display: contents`, so its three children become items of the card's own grid. **No markup change, source order untouched, so a screen reader reads it exactly as before**

**Two across, not three.** Three cards in the 880px column give each 277px, which breaks the longer names onto two lines and the roles onto three, and the rows stop lining up. Rendered both ways before choosing.

**Why the card layout changed, recorded because the spec should hold it.** The portrait used to sit *above* the name in a column, which left the biography whatever height remained and clamped it to three lines — so all fourteen cards stopped mid-sentence on an ellipsis. Kain saw it and asked for the name and role to sit level with the top of the portrait, as one design across every card. **It is not a new arrangement:** it is the phone layout he approved at S062, promoted to every width, so the change *deleted* the 767px block that used to hold it rather than adding a second design. The page now has one card shape where it had two and a rule to switch between them. Measured on the rendered page at 1440px, before and after: the biography needed **105px** and was given **63px**; it now gets all 105, and the card is **247px** tall against **287px**. More words in less height.

---

### 33.9 The one stack-point exception this page carries

`.pp-card` wraps at **640px**, which is **approved stack-point exception 4 of 5** under DSRD 7 §4.5 as amended at S252, approved by Kain. Named here so a later audit reads it as a ruling rather than as an arbitrary breakpoint.

---

### 33.10 Tokens

This page introduces no new tokens. 12, 14, 16, 18, 21, 24 and 28px are `--text-*`. Spacing 16 / 24 / 32 / 48 is `--sp-md` / `--sp-lg` / `--sp-xl` / `--sp-2xl`. Card grid gap is `--grid-gap` (24px), card corner `--radius-card` (12px), reading column `--container-article` (880px).

---

### 33.11 Decision register

*A log, not the specification: this register records what was decided for this page and when. The operative spec is the section body above — where the two differ, the body governs.*

| # | Decision | Ruled |
|---|---|---|
| 1 | Volume falls as the page descends: three treatments on one page, not one | Kain, S062 |
| 2 | The guest panel carries no section heading; his name takes 28px instead | Kain, S062 |
| 3 | The role line is one size, 16px, across both row sections | Kain, S062 |
| 4 | `.pp-card` wraps at 640px — stack-point exception 4 of 5 | Kain, S252 (DSRD 7 §4.5) |
| 5 | The card's portrait sits level with the name and role; the biography spans the card and is never clamped | Kain, S296, on a rendered before-and-after |
| 6 | Two cards across, not three | Kain, S296, rendered both ways |
| 7 | The eldership section sits above the editorial squad | Kain, Code S076 |
| 8 | The links field is withdrawn: none of the six elders has a link to give | Kain, S296 |
| 9 | The acronym rule does not apply to a role line, anywhere on the site | Kain, Code S076 — filed as `RULING__The_Acronym_Rule_Does_Not_Apply_To_Role_Lines_S076.md`, and written into DSRD 6 §1 at S299 |
| 10 | Benjamin Lockwood's `line` field stays as written | Kain, S299 — raised at Code's S076, closed. Do not reopen from cold |
| 11 | The page and the sixteen profile pages close on the trial panel, not the enquiries panel | Kain, Code S097, on a screenshot of the block. Shipped as theme v0.161.0; written into §33.4 and §22.10a at S337 |
| 12 | Isabella S. Whitmore's and Jackson P. Hartley's role lines both read "Buyer Questions Specialist" | Kain, S337. Both read "TAYA Copywriting Specialist" before. Code raised Isabella's only; Jackson was found carrying the identical line in DSRD 2 §2.14 and ruled the same way in the same turn, because the two write the same thing. **This does not touch decision 9.** The change was made because no visitor knows the phrase behind the letters and spelling it out would not help them either, so it is a plain-language change and not an acronym-rule change. Kain refused the matching change to his own role line and closed it to both sides: his reads "CTO" and stays "CTO", and it is not raised again |
| 13 | The page's column is 960px, a token reset on this page only; the 800 column was too narrow on a wide screen | Kain, Code S145, by eye in Safari on four tabs. Written into §33.5 and §27 at S398 |
| 14 | The seventeen individual Our People pages take the same 960px column | Kain, Code S146 (theme 0.707.65). Written into §33.5 at S398 |
| 15 | Kain rewrote four pieces of the page's copy himself in the Safari sitting: the header paragraph ("Every Achology project is guided by specialists..."), Karen A. Ramsay's paragraph (final form opens "Karen shapes the learning environment's direction, keeping it honest, human, and caring as it grows."), Kain Ramsay's paragraph and Prof. Gerard Egan's paragraph. The theme's people registry is the strings' only home (decision 9 precedent); the exact words stand in Code's `RULING__Kain_Edits_The_Our_People_Words_S146.md`, TO Chat Archive | Kain, Code S146 (header at 0.707.64, paragraphs at 0.707.65). Recorded at the S398 close; DSRD 2 §2.14's bio shape is unchanged |

---

### 33.12 Still open, and the page's remaining definition of done

| # | Open item | Where it goes |
|---|---|---|
| O1 | The DSRD 6 per-chapter record for this page. Approved by eye is not the same as gated | Code, with the record returned through the channel |
| O2 | Whether the person card earns its own DSRD 8 entry. It is used on two sections of one page and has no decision-history entry today; its values live here | `component-library`, next time the library is walked |

**The links field, if it ever returns:** the shape was reasoned through and built before Kain withdrew it. It is recorded in `BRIEF__The_Six_Eldership_Biographies_S296.md` Part Two and is not rebuilt from scratch.

---

### 33.13 The signed record

The page was ruled in Safari, so the signed record is Code's export of the approved page with its build sheet beside it, in the Our People page folder. Per standing rule 24 this section names the folder and stops; the folder's own README says what is inside it. Where that record and this section disagree, the record is correct.

*Production implementation notes for this page live in the Production Implementation Notes document.*

---

## 34. Tag Landing Page Layout (SHAPE RULED S313; LOOK RULED, Kain S390; RECONCILED AGAINST DSRD 2 §1.8 THE SAME SESSION)

One shared template covering the 36 tag landing pages at `/learn/tags/{tag-slug}/` (DSRD 1 §2.4; the 36 slugs are locked at DSRD 1 §5.6). **It had no layout specification anywhere until this session.** The anchor document carried it as a deferred open question and the board card carried it as the one page type with nothing written, deliberately last in the order so the gap held nothing else up.

**One correction to how this section was written, kept at the top because it is the more useful lesson.** It was first drafted without DSRD 2 §1.8 open, and that section had specified this page's contents long before. Four choices here contradicted it. Three were reconciled in the same session, one went to Kain rendered, and §1.8 now carries the supersessions in place. **Content is DSRD 2's and layout is DSRD 9's, and neither is written without the other open.**

| What §1.8 said | What governs now |
|---|---|
| Mixed-type content cards, one set | Four labelled groups. **Kain's S313 ruling supersedes it** |
| Course cards near the top | Course cards at the foot. **Kain's S313 ruling**, on the two positions rendered |
| Filter by content type and by category | No filters. Follows from the grouping: the groups are the filter |
| Pagination, 24 per page | None. Follows from the grouping: four capped groups have nothing to paginate |
| Related tags, 3 to 5 that co-occur | **Unchanged, and it closes an open item this section had wrongly left open** |

### 34.1 The job, and what makes it different from a listing page

**A listing page answers "show me one kind of thing from one subject area." A tag landing page answers "show me everything the site holds on this one idea, wherever it sits."** That difference decides the whole layout. A listing page is filtered to one content type and one category; a tag page is filtered to neither, and cuts across all four content types and all seven categories at once.

So the §21 listing template does not serve it. Two of that page's own blocks have no meaning here: its content-type pill strip links to `/learn/{category}/{content-type}/` addresses that a tag page has no category for, and its H1 names a category and a content type it does not have. **This is a page in its own right, and it reuses §21's parts rather than its shape.**

**One thing it has that no listing page has: it sells.** DSRD 1 §6.1 assigns the Mapped Courses Callout to tag landing pages, and §5.7 gives it up to three course cards, filled from the page's own tag through the tag-to-course mapping, **never chosen by hand**. A tag page therefore recommends the courses that teach the exact thing the reader is reading about, which is the strongest commercial fit of any Knowledge Hub page type.

### 34.2 Page Structure (top to bottom)

**Ruled by Kain, S313, on two whole rendered pages, tabbed, with the grouping as the only variable.** He took the grouped page over the single mixed grid.

1. Sticky header (DSRD 8 §18)
2. Breadcrumb (§34.3)
3. Hero: H1, count, intro (§34.4)
4. Sort toggle (§34.5)
5. Hairline
6. **Articles group** (§34.6)
7. **Book Notes group** (§34.6)
8. **Quotes group** (§34.6)
9. **Workbooks group** (§34.6)
10. Hairline
11. **Discover Related Learning Paths, three course cards (§34.7). At the foot, after all four groups: Kain's S313 ruling on the two positions rendered whole, superseding DSRD 2 §1.8's near-the-top placement.** The trade he weighed: near the top every reader sees them, at the foot only readers who reach the end do, and those readers are warmer
12. Hairline
13. Related Topics (§34.8)
14. Rainbow stripe and footer (DSRD 8 §19)

**Why grouped rather than one mixed grid.** The alternative was a single grid, newest first, with content-type pills filtering it in place. Both were built as whole pages on the same tag with the same twelve pieces and put to Kain side by side. **The grouped page won.** The reason it wins is worth recording because it is the same reason the category hub is grouped: a reader arriving on a tag has come for a subject, not for a stream, and four labelled groups let them go straight to the kind of thing they want. A mixed grid makes them scan past three kinds of card to find the fourth, and the count of each kind is invisible until they have scrolled the lot.

**What the ruling costs, named rather than hidden.** A group with nothing in it does not render, so a thinly covered tag shows two groups instead of four and the page is shorter. That is correct behaviour rather than a fault: an empty labelled group advertises an absence. **But a tag close to the 36-tag governance floor could render with a single group of two cards**, which reads as a stub. The governance rule at DSRD 1 §5.1 already guards this from the other end, retiring or merging any tag under ten pieces after six months, so the two rules meet. This is named here so nobody meets a thin tag page and treats it as a layout failure.

### 34.3 Breadcrumb

Reuses the §20.3 breadcrumb component. Trail per DSRD 1 §9: `Home > Learn > Tags > [Tag Name]`. The tag name is the current page, brand dark, not linked. 48px below the header.

**`Tags` is a real link and its destination is the all-tags index page**, which is one of the two index pages still to be specified. **Until that page exists the segment renders as plain text rather than a broken link**, per DSRD 1 §6.4 rule 5: a link is written only where the target exists.

### 34.4 Hero

| Element | Value |
|---|---|
| H1 | The tag name exactly as DSRD 1 §5.6 registers it. Como, the 33 step, 700, brand orange #ED6922, line-height 1.2 |
| Count | The real number of pieces carrying this tag, across all four types and all seven categories. Mulish 14px/400, soft grey #5E6B75, 6px below the H1 |
| Intro | One or two sentences describing what this topic covers and that it is drawn from across the whole Knowledge Hub. Mulish, the 16 step, 400, brand dark, line-height 1.6, max-width 880px, 18px below the count |
| Container | 1200px, the prose inside it at 880px, the pattern DSRD 7 §4.1 already names for the category hub |

**No overline and no category pill strip.** The page belongs to no category, which is the point of it, and an overline reading "Tag" tells a reader nothing the breadcrumb has not already said.

**The intro copy exists and is approved. It is DSRD 2 §1.3.4, the 36 confirmed tag descriptions, approved by Kain at S238.** Sentence case with proper nouns only capitalised, every one written to a 138 to 148 character band so all 36 render at a uniform visual length, 155 the hard ceiling, counts machine-verified before approval. **They already do double duty as each tag page's meta description and the visible line beneath its heading**, which is exactly this field. Nothing is owed and nothing is written fresh.

**Recorded because it cost time this session.** This section first said the copy was owed and its home could not be located. It was in the content document all along, under tag curation, where content copy belongs. **The failure was looking in the wrong document rather than a gap in the project**, and the correction is written here rather than quietly made so the same search is not run again from cold. **A stand-in line was used in the render Kain ruled on, and he was told so at the time**; the shape he ruled does not depend on the words, and the approved line replaces the stand-in at build.

### 34.5 Sort Toggle

The §21.4 control bar's right-hand group only: two pills, `Newest` and `A to Z`, right-aligned. Same values as §21.4 in every respect, including the S313 colour correction to the inactive pill.

**The content-type pills are not on this page.** They were on the option Kain did not take, where they filtered a mixed grid. With the content grouped, the groups themselves are the filter and a second set of controls doing the same job is clutter.

### 34.6 The Four Content Groups

Each group is a §20.7 section header followed by a card grid. **The section header component is used exactly as the category hub uses it**, with its own hairline beneath the title, its live count in parentheses, its supporting line, and its `View all` control on the right.

| Property | Value |
|---|---|
| Order | Articles, Book Notes, Quotes, Workbooks. Fixed, every tag page, never re-ordered by volume |
| Icon | Per content type, from the §20.7 register: `newspaper`, `notebook-pen`, `quote`, `file-pen` |
| Title | The content type name, with the live count for this tag in parentheses |
| Supporting line | One line per type, 12 to 25 words per DSRD 7 §3.3 |
| Cards | The standard card per type: DSRD 8 §6.1, §6.2, §6.3, §6.4. **No featured cards**, which are the category hub's alone (§21.6 holds the same rule) |
| Grid | 3 desktop, 2 tablet, 1 phone, 24px gap, per DSRD 7 §4.1 |
| Items shown | The most recent per type, with the rest reached through `View all` |
| Empty group | Does not render. No header, no empty state, nothing |
| Boundary between groups | 48px, no hairline, on the same ground as the category hub's exception (DSRD 7 §4.3, exception 3): each group already opens with the section header's own rule |

**Where `View all` goes is an open question, named rather than guessed.** A content type filtered to a tag has no address today: the site has `/learn/{category}/{content-type}/` and `/learn/{content-type}/`, and neither carries a tag filter. Either the control links to the cross-category listing for that type, which loses the tag and is therefore a worse answer than it looks, or a new address is needed. **Not decided here.** Until it is, the control does not render, per the same rule the breadcrumb follows.

**How many items each group shows is open too.** The category hub shows five per section, one featured and four standard, but that page has featured cards and this one does not. **It is a decision on the rendered page with real content, not a number chosen on paper**, and it is Kain's at the same sitting that settles the spacing.

### 34.7 Discover Related Learning Paths

Section header plus **up to three course cards**, DSRD 8 §7.

**The courses are never chosen by hand.** DSRD 1 §5.7: this page's own tag is its lead tag, and the slots fill from that tag's mapped course list in the order §§5.2, 5.3 and 5.5 write it. Where the tag maps fewer than three courses, the page shows fewer; it does not top up from another tag, because on this page type there is no second tag to top up from.

**Three slots here, against two on an article page**, and the difference is deliberate: this page runs in the 1200px frame rather than an 880px reading column, so three course cards sit at the same width the course card was approved at rather than being squeezed.

**Content attribute tags map to no courses** (DSRD 1 §5.1, §5.4). On those five tag pages, this whole block does not render. Named because five of the thirty six pages behave differently and a builder meeting the first one should know it is correct.

### 34.8 Related Topics

Section header plus a wrapping row of tag pills, the §20.8 pill treatment exactly. Links to other tag landing pages.

**Which tags appear is settled, and this section was wrong to call it open.** DSRD 2 §1.8 component 9 already specifies it: **three to five tags that most often co-occur with this one**, a derivation applied by machine, never a hand-picked list per page. Found on the S313 reconciliation.

### 34.9 Pagination

**None on this page, and it follows from the grouping rather than being its own decision.** DSRD 7 §17.1 lists tag landing pages among the pages it governs, and DSRD 2 §1.8 component 8 specified 24 per page; both were written when this page was assumed to be one flat listing. **With four capped groups there is nothing to paginate**, and depth is reached through each group's own `View all`, once that control has an address. DSRD 7 §17.1 is owed the correction; DSRD 2 §1.8 took it at S313.

### 34.10 What is settled and what is open

**Settled by Kain at S313:** the page is grouped by content type rather than a single mixed grid, the three course cards sit at the foot rather than near the top, and the block order at §34.2 follows from both.

**Settled by reconciliation against DSRD 2 §1.8 the same session, no ruling needed:** no content or category filters, no pagination, and Related Topics derived from co-occurrence.

**Open, each one named rather than filled in:**

| # | Open item | Whose, and how it closes |
|---|---|---|
| 1 | ~~The 36 tag description lines for the hero intro~~ | **CLOSED S313.** They exist and are approved: DSRD 2 §1.3.4, ruled by Kain at S238. See §34.4 |
| 2 | How many items each group shows | Kain's eye, on the rendered page with real content |
| 3 | ~~Where each group's `View all` links to~~ | **CLOSED S390, decided by Chat as a structural call.** No `View all` control renders on a tag page, because no tag-filtered address exists and linking to the cross-category listing would drop the tag. Each group instead shows up to six cards (two rows of three), so a reader can see more without leaving the topic. The control returns only if a tag-filtered listing address is ever built. Six is a starting value; Kain confirms it by eye at the spacing sitting (item 2) |
| 4 | ~~Which tags fill Related Topics~~ | **CLOSED S313.** DSRD 2 §1.8 component 9: three to five by co-occurrence |
| 5 | The vertical rhythm and every internal spacing value | Kain's at the spacing sitting on the rendered page, the same way the book note page's are held open at §32 |
| 6 | Phone and tablet behaviour | Follows the §21.9 pattern, confirmed on a render, not written here |

**Three things stand between this specification and a built page: items 2, 3 and 5**, and two of the three close at one rendered sitting with Kain.

*The render Kain ruled on is the tabbed two-option file produced at S313; its card copy was written for the render and is not real content, which he was told before he ruled. The ruling is about the page's shape, which does not depend on the words.*

---

### 34.11 The Thread, as Kain settled it in the S177 sitting (20 October 2026; written home by Chat at the S436 close, 21 October 2026)

Kain chose The Thread from four rendered whole-page directions, then settled its hero (The Line Begins, six canonical stops), its line (Grey Line, Orange Rings), its banner (Soft Picture, no stop ever faded), the page below the banner (Living Thread with one pause, View All buttons, two-line section lines, the courses heading Take Your Learning Further) and the menus (The Dark Bar Changes), and ruled that each tag page's heading and line are his own S177 title and line. Code's ruling file is carried here whole so nothing is lost in paraphrase; the sections above it that it supersedes (34.4 hero, 34.5 to 34.8) are read with it. Building into the tag template waits on the All Tags page sign-off.

#### RULING: the tag landing page is The Thread (S177)

Kain, S177 theme sitting, 20 Oct 2026, on four rendered whole-page directions (previews/kh-tag-s177/index.html: Family Twin, Topic Tone, Side Index, The Thread), each shown on a full tag (Build Confidence) and a thin one (Start & Grow a Business). Code recommended Family Twin; Kain chose **The Thread** (option 4): "Actually really like the option 4, The Thread ... it just shows a natural progression through all different types of content right through to courses."

What it is: the groups in their fixed order (Articles, Book Notes, Quotes, Workbooks) and then Discover Related Learning Paths, joined by one orange line down the left, each group a numbered station with its kind's icon in a circle and a large faint number; the courses are the last station on a warm cream plate; Related Topics as the All Tags Soft Watermark tiles after the line. Six cards per group, three across, two on tablet, one on phone.

**Still open (Kain, same message):** the hero banner. He wants it to align more with the colour and style of the rest of the Knowledge Hub. Code brings four rendered hero directions on The Thread for his pick.

OWED BACK: the build sheet and DSRD 9 section 34 write-home once the hero is chosen.

**Hero, same sitting:** Kain chose **The Line Begins** (previews/kh-tag-s177/hero.html, tab 4) from four rendered heroes: the warm band, the counts as the thread's own circles on a line that runs across them and drops into the page. "We can go with the line begins ... very, very neat." Two asks in the same words: (1) the line more subtle, not so thick; (2) the stops use the full canonical terms, six of them: **Articles, Book Note Articles, Quote Articles, Workbooks, Relevant Courses, Relevant School**. Code brings four rendered treatments of line weight and stop spacing for his pick.

**Line treatment, same sitting:** Kain ruled out Beads and Close Together ("definitely no"; he likes the stops filling out the screen) and is torn between **Fine Orange** and **Quiet Grey**. Code brings four further treatments between those two, each with the stops spread evenly, for his pick.

**Line treatment, final pick, same sitting:** Kain chose **Grey Line, Orange Rings** (previews/kh-tag-s177/line2.html, tab 4; built as line6): the six stops spread evenly across the band on a 1px soft grey line, each stop's circle with a fine 1px orange ring; the thread down the page in the same grey with the same orange rings on its stations. "Let's go with grey line, orange ring ... it looks very, very, very good."

**Words on the tag page (Kain, same sitting):** each tag page's heading is Kain's own title and its line is his own S177 line (RULING__All_Tags_Tile_Lines_Are_Kains_Own_Words_S177), the same as on its All Tags tile; DSRD 2 section 1.3.4's older descriptions are superseded on this page. Related Topics tiles carry his titles and lines too. Previews rebuilt with them (line6-full and line6-thin are the chosen page).

**SETTLED, ready to build into taxonomy-kh_tag.php once the All Tags page is signed off:** The Thread; The Line Begins hero with the six canonical stops; Grey Line, Orange Rings.
OWED BACK: the build sheet and DSRD 9 section 34 write-home.

*No em or en dashes in this file; checked before writing.*

**Not yet settled (Kain, same sitting):** the banner as a whole. Kain keeps the line and circles (Grey Line, Orange Rings) and the Categories bar, but "something's not quite right" with the banner; he asked for four options of real graphic design excellence. Drawn as previews/kh-tag-s177/banner.html: Station Zero, Soft Picture, Framed Panel, The Deck. WAITS ON his pick.

**Banner, final pick, same sitting:** Kain chose **Soft Picture** (previews/kh-tag-s177/banner.html, tab 2): the warm band; the family label, the larger title and his line on the left; the topic's newest article picture in soft-focus black and white fading in from the right (the first course's picture when a topic has no article yet), fading away above the stops; the six stops on the Grey Line, Orange Rings below. "I really like the soft picture ... very, very neat indeed." **And no stop is ever faded:** a stop with nothing in it yet (Workbooks today) shows at full strength, because every category will be covered for launch. "Actually, I really like this page. It's actually very nice."

**SETTLED, ready to build into taxonomy-kh_tag.php once the All Tags page is signed off:** The Thread; The Line Begins with the six canonical stops; Grey Line, Orange Rings; the Soft Picture banner; no faded stops; Kain's own titles and lines. The chosen page is previews/kh-tag-s177/banner2-full.html and banner2-thin.html.
OWED BACK: the build sheet and DSRD 9 section 34 write-home.

*No em or en dashes in this file; checked before writing.*

**The page below the banner, same sitting (Kain, from four rendered options in previews/kh-tag-s177/body.html):** Kain chose **Living Thread** together with **The Pause**. His asks, in order:
1. Living Thread: the line fills from grey to orange as you read down the page, but the orange more subtle: the same weight as the grey line, in a light orange.
2. The Pause: he loves it; a small number of pauses down the page (the same one or varied, within the rules).
3. Every section (Articles, Book Note Articles, Quote Articles, Workbooks when there are some, the courses, Related Topics) gets a way to go through to everything of that kind on this topic. No tag-filtered address exists today (DSRD 9 34.10 item 3), so this needs one.
4. Each section's description sits in two lines, the top line a word shorter than the bottom, capped so it never runs to three.
5. Perhaps a Know Your Psychology logo, without overdoing the page.
6. The course heading: he remembers a different heading with a subtitle used elsewhere on the site; Code to find it.

**Below the banner, final shape, same sitting:** Kain chose version 1 of previews/kh-tag-s177/final.html: the small "View All" button on the right of each section heading, and **one pause only** ("one was kind of impactful, two is just too much"), with the line ending on the small Know Your Psychology logo. Also confirmed in the same build: the subtle light orange fill at the grey line's weight, two-line section lines (top shorter), the courses heading "Take Your Learning Further" with its subject-page line.
**Open:** three menus stack while scrolling (site menu, Categories bar, the following stops bar); Kain: "three menus is just kind of silly". Code brings four ways to fix it.

**Menus, same sitting:** Kain chose **The Dark Bar Changes** (previews/kh-tag-s177/menu.html, tab 1): no separate following bar; the dark Categories bar pins as on every list page, and once the reader is past the banner it changes into the six stops, filling light orange as they read. Never more than the site menu and one bar. "Definitely go with the dark bar changes ... very, very, very nice indeed."
**And the foot of the page (same message):** the line runs on past the courses straight into Related Topics as its last stop, and the page ends there; the Know Your Psychology logo goes; the foot of the page tidied, since this is a navigation page. Then fine-tuning to make it visually spectacular.
**Built into the preview (Code, same sitting):** the line runs past the courses into Related Topics as its last stop (its own circle, its "View All Topics" button) and ends there; no Know Your Psychology logo anywhere on the page, including the thin topic's grid; the dark bar's stops are the six of the banner (Relevant School added). The page as it stands: previews/kh-tag-s177/page-full.html and page-thin.html. The site footer is unchanged (it is the locked footer every page shares).

**Kain on the page as a whole (same sitting):** "this infrastructure now is totally spot on"; what remains is "a little bit of wow". First: the buttons. He wants one button strategy for the whole site, different kinds for different jobs, and named the effect he saw: on hover a white circle appears inside the right of the button, and the button inches towards the pointer as it approaches. Code drew a three-kind family (Doing: enrol, trial; Exploring: View All; Reading: Read This, View topic) in four directions on the tag page (previews/kh-tag-s177/buttons.html: Circle Reveal, The Disc, The Sweep, Quiet Links). WAITS ON Kain's pick. Whichever he picks is a site-wide component: it needs its home in the component record (DSRD 8) before any page outside the tag page takes it.

**Buttons, same sitting:** for this page and pages like it, Kain chose **Quiet Links** (previews/kh-tag-s177/buttons.html, tab 4) for the navigation links: the words with a small orange-ringed arrow and an orange underline that draws in on hover ("more subtle, for pages of this nature"), kept consistent through the Knowledge Hub. **No other button on the site is touched for now:** the course cards' buttons, the topic tiles' links and the quote cards stay exactly as built. A site-wide button strategy is for a focused button session some other time, before or after launch; **not a board card** (Kain's words: "Don't make it a board card item. I'll remember").
**The settled page:** previews/kh-tag-s177/page-full.html and page-thin.html.
**The footer (Kain, same sitting):** not part of this page's work and not to be touched, the $7 trial band included. His "tidy up the footer" meant the bottom of the page, which is done: the line ends in Related Topics and the page ends there.

*No em or en dashes in this file; checked before writing.*
**Related Topics tiles (Code, same sitting):** they take the All Tags page's tiles exactly as that page now draws them (its S177 redesign: pattern panel, icon disc, coloured edge), laid three across, two on tablet, one on phone, as on the All Tags page. When the All Tags tiles change, the tag page's Related Topics follow.

**Last look, round two (Kain, same sitting):**
1. Each section's count after its title (Articles (20), Book Note Articles (18), Quote Articles (19), Workbooks) in orange and a link (to that kind's View All), no underline.
2. The Pause: "do your best design work on this one component"; balanced and visually spectacular; give it the features of a real quote card, tied to the actual quote card picture from the quote page it comes from, with its actions (share, download, email or whatever the quote page offers).
3. The quiet "Read This" link: the arrow must not leave its circle on hover, and the orange arrow on an orange circle (above all on the dark band) loses itself; reimagine the link and its arrow movement, on light and on dark.
4. Related Topics carries the All Tags page's line: "Choose a topic that matters to you, and find every article, book note, quote and workbook written on it." (Kain's words, the Browse by Topic page.)

**The Pause, same sitting:** Kain chose **The Card on the Table** (previews/kh-tag-s177/pause.html, tab 1): words on the left, the quote's real card picture on the right with Download, Share and Copy and the Read link. **No name on the left:** the card already carries the speaker, and the words on the left are the article's title, which a pen-name author wrote, not the speaker (Kain, again, as on the Quotes lists). He asked for four more versions of it that are visually spectacular, not "words in an image, dumped on a block".
**The Card on the Table, look (same sitting):** Kain chose **Its Own Light** (previews/kh-tag-s177/table.html, tab 4): the band is the card's own picture, blurred and darkened; the sharp card in front with its reflection; it lifts on hover ("brilliant"). Not yet right: the left-hand side's layout, and the bold orange line under the article title. Code brings four versions of the left side.
**The Pause, final (same sitting):** Kain chose **Matched to the Card** (previews/kh-tag-s177/light.html, tab 3): Its Own Light, with the words lined up to the card's top edge and the actions (Download, Share, Copy) and Read link to its bottom edge, divided by a faint line; the title a size smaller, no line under it, warming to light orange on hover. The full page as it stands: previews/kh-tag-s177/page-full.html and page-thin.html.

**SIGNED OFF by Kain, S177, 20 October 2026:** "Yes, Claude. Sign this one off. Let's get this one built into the site across all tag pages. This is great." The settled page is previews/kh-tag-s177/page-full.html and page-thin.html; the build into taxonomy-kh_tag.php is the theme session's, after the All Tags page is signed off.

*No em or en dashes in this file; checked before writing.*

**Page count for the build (measured on the build site, S177, 36 tag pages read one a second):** 36 tag pages (one template; each already has its address, and gets the new design). New "view all" pages, one per tag and kind that has pieces: 99 today (Articles 32 tags, Book Notes 35, Quotes 32; Workbooks none yet, up to 36 more when workbooks publish). Learn Hypnotherapy has no pieces at all today; Start & Grow a Business has one.
**Code's technical call for the build (SEO):** the 36 tag pages are indexed and each needs its Rank Math title, description and focus keyword (Chat's copy; Kain's 36 S177 lines can serve as the descriptions). The view-all pages are lists of pieces already indexed elsewhere: noindex, follow, with a templated title, so they add no metadata work and no thin pages to search.


### 34.12 The tag pages are signed off as built on the site (Kain, Code's S178 sitting, 21 October 2026; written home by Chat at the S437 close)

Kain, on Build Confidence and Start and Grow a Business at theme 0.707.401 on the build site: "Yes, Claude, totally sign those pages off. Very, very happy with the design. Let's go. Let's do this. Let's get them on the site." What he signed: the 36 tag pages built to section 34.11, measured identical to the signed previews in WebKit at 1440, 834 and 390, and the 144 view-all pages at /learn/tags/{tag}/{kind}/ (Articles, Book Notes, Quotes, Workbooks; noindex, follow; titled "{Kind} on {Topic}"; 24 a page; an empty one says "{Kind} for this page are being prepared."). Shipped at 0.707.399 to 0.707.401 (Code's SHIP__Tag_Pages_The_Thread_0.707.400_S178, archived in the channel with this block written home). Kain's 36 titles and lines now live in one place in the theme, read by the All Tags page, each tag page's heading, line and search description, and the Related Topics tiles.

Code's calls, overturnable: the Pause takes the first of the six quotes shown whose words suit a card (80 to 160 characters); a group shows View All only when it holds more than its six, and its count is always a link; the view-all Quotes keep every card small; a topic with nothing published yet takes its own family's topics as Related Topics; the tag page's search description is Kain's line, and the older section 1.3.4 descriptions in DSRD 2 are no longer read on this page.

The spacing check (section 0 of DSRD 6, ruled the same sitting) ran on the view-all page: its station to Related Topics gap measured 112 and 152 against the signed 64, fixed at 0.707.401 so page numbers sit inside the station and draw only when there is a second page. Left alone and named: the 48 above the page numbers on a phone, the page numbers' own value shared with the signed list pages.

Still owed by Chat on the tag pages card: the Rank Math title and focus keyword for each of the 36 tag pages (until then each carries Rank Math's default, "{Tag} Archives"), the redirect plan, and the reader halves of the tag page's DSRD 6 record (chapters 1, 6, 7 and 8). Open for Kain: the list family's shared band lines the record fails (title 42 against DSRD 7's 32, and the banner spacing), which need an exception recorded in DSRD 7 or a change he sees, not a quiet fix.

### 34.13 One title size on every list and navigation page, and the tag pages' family line under the description (Kain, Code's S178 theme sitting, 21 October 2026; written by Chat, S438)

**One title size (0.707.403).** All 76 list and navigation pages (the 32 lists, the 7 subject pages, All Tags, the 36 tag pages, and the tag view-all pages that share their banner) set the page title at 33, the site's one title size (DSRD 7 section 3.0), at every width. Kain approved it on the rendered before and after: "That actually looks a little bit neater ... slightly smaller text." This retires the subject page build sheet's recorded departure (title at 42) and the open band-lines question carried on the tag page and All Tags records since S177.

**The tag pages' family line sits under the description.** With the title at 33, the orange family line ran longer than the title on 20 of 36 tag pages on a computer. Kain ruled the cause: the family phrases were written as All Tags section headings and "are too long to have above a page heading or a page title", so the answer is positioning, not resizing, wrapping or new words. Shown four tag pages, one per family, with the line removed and with it moved, he chose the move: the order is breadcrumb, title, description, family line (still the link to its group on All Tags). "Exactly as I saw."

**Phone spacing.** On a phone the breadcrumb sits 32 below the header (section 26); 48 below the breadcrumb at every width; the topics band 32 above and below on a phone.

**Gate after the change.** Chapter 2 passes on all five list and navigation records; All Tags chapter 10 passes; chapter 11 runs in Firefox and passes. Four proposed exceptions (no hairlines on the lists and subject pages by the signed design; the breadcrumb instrument carve-out; the tag banner's picture reaching the header; two icon-registry lines) wait on Kain's yes in Code's sitting and are then recorded in DSRD 7 section 4.3 (SHIP__KH_Shared_Title_And_Breadcrumb_0.707.403_S178, in TO Chat until then). Fold-back: the theme's previews folder, kh-shared-s178 and kh-tag-line-s178; the tag page build sheet's "Decided in S178" line. Code's file: RULING__Tag_Page_Family_Line_Under_The_Description_And_One_Title_Size_S178, in the channel Archive.

**Rise in turn plays on every topic page's three kind walls and its view-all pages (Kain, Code's S179 theme sitting, 22 October 2026; shipped 0.707.439; written by Chat, S441).** The cards arrive one after another as they scroll into view, by the shared card's rule. The rule and its record live in DSRD 8 section 41; this line only says the wall carries it.

### 34.14 The 36 tag pages' search titles and focus keywords (Kain, S448, 27 October 2026: "Yes"; written by Chat, S448)

**Why.** Every tag page is indexed (section 34.11), and until now each one's search title fell back to Rank Math's default, "{Tag} Archives", which reads as machine-made and tells a searcher nothing. The search title is the blue line in a Google result; the heading on the page does not change.

**The standard they follow.** The title standard Kain agreed at S448 for every kind of page: a question a real person would ask, at most 60 characters, with the searched phrase inside it, every word earning its place. Each phrase was checked in Google's suggestions (UK, 27 October 2026), and each focus keyword was checked against the keyword register so no tag page chases a phrase an article already holds; that is why the CBT, NLP, hypnotherapy, mindfulness, life coaching, counselling, emotional intelligence and purpose pages ask the question they do. Kain wrote the CBT and NLP titles himself, spelling out the full name. The Deep Dive title was changed the same evening, on Kain's yes, because its first version carried "deep dive", a machine tell the Content Standard always fails; Deep Dive names a kind of article rather than a subject, so no phrase for it has real search demand, and the title is the plainest question a reader would ask. Lengths run 32 to 54 characters; they need not match, because Google shows them one at a time and cuts anything past about 60.

**How they are set.** In Rank Math's SEO title and focus keyword fields on each `kh_tag` term, word for word, with no site name or separator added (as the eight Articles lists, section 21.0, Kain's S433 ruling). The descriptions stay as approved at S238 (DSRD 2 section 1.3.4). The 144 view-all pages stay noindex, follow with a templated title (section 34.11). The 36 focus keywords are claimed in the keyword register (content type tag-page, S448).

| Tag | Address | Search title | Focus keyword |
|---|---|---|---|
| Achieve Your Goals | `/learn/tags/achieve-your-goals/` | How do you actually achieve your goals? | achieve your goals |
| Beginner-Friendly | `/learn/tags/beginner-friendly/` | Psychology for beginners: where do you start? | psychology for beginners |
| Break Negative Thinking | `/learn/tags/break-negative-thinking/` | How do I stop negative thinking taking over? | stop negative thinking |
| Build Confidence | `/learn/tags/build-confidence/` | How do you build confidence that lasts? | build confidence |
| Build Mental Resilience | `/learn/tags/build-mental-resilience/` | How do you build mental resilience when life is hard? | build mental resilience |
| Build Self-Discipline | `/learn/tags/build-self-discipline/` | How do I build self-discipline and stick with it? | build self-discipline |
| Communicate Effectively | `/learn/tags/communicate-effectively/` | How do you communicate effectively with people? | communicate effectively |
| Achology Long Reads | `/learn/tags/deep-dive/` | Where can I find in-depth psychology articles? | in-depth psychology articles |
| Emotional Intelligence | `/learn/tags/develop-emotional-intelligence/` | How can you improve emotional intelligence? | improve emotional intelligence |
| Find Your Direction | `/learn/tags/find-purpose-and-direction/` | How do you find direction in life when you feel lost? | find direction in life |
| Grow Self-Awareness | `/learn/tags/grow-self-awareness/` | How do I become more self-aware? | become more self-aware |
| Help Others Grow | `/learn/tags/help-others-grow/` | How do you help people grow without taking over? | help people grow |
| Improve Relationships | `/learn/tags/improve-relationships/` | What really helps to improve relationships? | improve relationships |
| Build Social Confidence | `/learn/tags/improve-social-confidence/` | How do I build social confidence and feel at ease? | build social confidence |
| Increase Productivity | `/learn/tags/increase-productivity/` | How can I be more productive without burning out? | be more productive |
| Lead With Impact | `/learn/tags/lead-with-impact/` | What does it take to be a good leader? | be a good leader |
| Understand CBT | `/learn/tags/learn-cbt/` | What exactly is Cognitive Behavioural Therapy? | what exactly is cognitive behavioural therapy |
| Learn Counselling | `/learn/tags/learn-counselling/` | How do you learn counselling skills? | learn counselling skills |
| Learn Hypnotherapy | `/learn/tags/learn-hypnotherapy/` | Does hypnotherapy work, and how is it done? | does hypnotherapy work |
| Learn Life Coaching | `/learn/tags/learn-life-coaching/` | What is life coaching, and how does it help? | what is life coaching |
| Learn Mindfulness | `/learn/tags/learn-mindfulness/` | What is mindfulness really about? | what is mindfulness |
| Understand NLP | `/learn/tags/learn-nlp/` | Does Neuro-Linguistic Programming really work? | does neuro-linguistic programming really work |
| Manage Stress & Anxiety | `/learn/tags/manage-stress-and-anxiety/` | How do you manage stress and anxiety day to day? | manage stress and anxiety |
| Master Your Mindset | `/learn/tags/master-your-mindset/` | How do you change your mindset when it gets in the way? | change your mindset |
| Navigate Life Changes | `/learn/tags/navigate-life-changes/` | How do you cope with big life changes? | big life changes |
| Overcome Feeling Stuck | `/learn/tags/overcome-feeling-stuck/` | Why do I feel stuck in life, and how do I move on? | feel stuck in life |
| Overcome Self-Doubt | `/learn/tags/overcome-self-doubt/` | How do I overcome self-doubt and trust myself? | overcome self-doubt |
| Practical Exercises | `/learn/tags/practical-exercise/` | Which psychology exercises actually help in real life? | psychology exercises |
| Practice Mindfulness | `/learn/tags/practice-mindfulness/` | How can I be more mindful in daily life? | be more mindful |
| Professional Practice | `/learn/tags/professional-practice/` | What makes a good counsellor, coach or helper? | what makes a good counsellor |
| Research-Based | `/learn/tags/research-based/` | Looking for evidence-based psychology you can trust? | evidence-based psychology |
| Start & Grow a Business | `/learn/tags/start-and-grow-a-business/` | How do you start and grow a business that lasts? | start and grow a business |
| Strengthen Your Bond | `/learn/tags/strengthen-your-partnership/` | How do you keep a relationship strong for years? | keep a relationship strong |
| Support Mental Health | `/learn/tags/support-mental-health/` | How can I support mental health in everyday life? | support mental health |
| Understand Your Mind | `/learn/tags/understand-your-mind/` | How does the mind work in everyday life? | how does the mind work |
| Unlock Personal Growth | `/learn/tags/unlock-personal-growth/` | How do you grow as a person, year by year? | grow as a person |

## 35. All Tags Index Page Layout (SHAPE RULED S313; LOOK RULED, Kain S390)

**35.0a Doors and Tiles, and Soft Watermark tiles (Kain, S176 theme sitting, 20 October 2026; written S434).** Kain chose, from four rendered options, that the All Tags page is Doors and Tiles: the twin list shell, the Four Doors at the top as jump links with topic counts, then each family as its own band headed by its door with its topics as tiles four across, two on tablet, one on phone. For the tiles he chose Family Tone and then its Soft Watermark variation: each family its own soft tone and coloured top edge, the topic's icon whole inside the tile, large and very faint behind the words, centred on the right. Each tile carries one overview sentence of about 120 characters that follows on from its name; the 36 sentences are new page copy and wait on the Newsroom's gate before the News Team writes them. The detail and Kain's words are in BUILD_SHEET__All_Tags_Index_Page_S390.

**35.0b On a phone, the topics show their names, and the category strip fades (Kain, Code's S189 Safari afternoon, 27 October 2026; 0.707.649; written by Chat, S449).** Of four options at phone width: "Yes, option 1, names beside the icons on a phone." Below 768 the topic quilt is two columns, each topic a row with its coloured icon tile and its own existing title beside it, so nobody taps blind; from 768 up it is unchanged. On the Knowledge Hub category strip, of four: "Yes, option 1, the soft fade on the category strip." Below 768 the subjects fade softly as they slide towards the All Categories label, so none is cut at the strip's edge; the label and the computer strip are unchanged. Still open, a fault fix for the next theme session: the All Tags page scrolls sideways at 320.

One page at `/learn/tags/` (DSRD 1 §2.4, address added S313). **It had no address and no layout until this session.**

### 35.1 Why the page exists

**Two reasons, and the first is structural rather than editorial.** Every tag landing page's breadcrumb reads `Home > Learn > Tags > [Tag Name]` (DSRD 1 §9), and until S313 the `Tags` segment pointed at nothing, because no page lived there. A breadcrumb segment with no destination is either a dead link or a lie about the site's shape. This page is what closes it.

**The second is the reader.** Thirty six topics are the site's cross-cutting discovery layer (DSRD 1 §5), and a reader could only ever reach one by being handed it from a piece they were already reading. There was no way to see what the site covers and choose.

**One page, not two.** This section replaced a two-page plan. **Confirmed for good by Kain at S177 (RULING__Author_Pages_Cut_Permanently_S177): no author page at /learn/authors/, not now, not later; the biography stays an ordinary article; the S176 shopping list row is struck. The link to /learn/authors/{slug}/ named at 2318 and the Author Hub comment in the theme are a theme queue item.** **The all-authors index was killed by Kain at S313**, because there is no author page type to index: he ruled at S306 that biographies publish as ordinary articles and no author hub exists or will. It had survived on the board from before that ruling. DSRD 1's breadcrumb table, indexing register and sitemap list were all struck of author hub rows in the same pass.

### 35.2 Page Structure (top to bottom)

1. Sticky header (DSRD 8 §18)
2. Breadcrumb: `Home > Learn > Tags`, the §20.3 component
3. Hero: H1, count, intro (§35.3)
4. Hairline
5. **Outcomes**, 16 topic cards (§35.4)
6. **Problems**, 9 topic cards
7. **Approaches**, 6 topic cards
8. **Kinds of Reading**, 5 topic cards
9. Rainbow stripe and footer (DSRD 8 §19)

**The four families are DSRD 1 §§5.2 to 5.5, renamed for readers and not in the taxonomy.** Outcome tags become **Outcomes**, problem tags **Problems**, modality tags **Approaches**, content attribute tags **Kinds of Reading**. The taxonomy's own names are internal; a reader meeting "modality tags" as a heading learns nothing. **The internal names do not change and this is a display rule only.**

**Boundaries between families carry no hairline**, 48px of white, on the same ground as the category hub's exception (DSRD 7 §4.3, exception 3): each family opens with a section header carrying its own rule.

### 35.3 Hero

| Element | Value |
|---|---|
| H1 | `Browse by Topic`. Como, the 33 step, 700, brand orange |
| Count | The live number of registered tags. Mulish 14px/400, soft grey, 6px below |
| Intro | Two or three sentences naming the four families and what each one is for. Mulish, the 16 step, 400, brand dark, max-width 880px, 18px below |
| Container | 1200px frame, 880px prose inside it |

**The line under the H1 (Chat's call, S437, 21 October 2026; Kain sees it on the page).** Under the S176 and S177 shell (section 35.0a) the intro row above is superseded by one line of about 15 to 25 words in Kain's style, as Code asked at S177: "Every topic is a thread running through the Knowledge Hub. Follow one, and find every article, book note, quote and workbook written on it." (24 words). It carries Kain's name for the tag page, The Thread (section 34.11), and identifies the Knowledge Hub by what it holds, which is the page's one Achology term (DSRD 6 section 1). Sent to Code as RULING__All_Tags_Hero_Line_Every_Topic_Is_A_Thread_S437; Kain changes it if he objects when he sees it built.

### 35.4 The Topic Card (ruled by Kain, S313, on two whole rendered pages, tabbed, with the card against a plain list as the only variable)

**He took the cards.** Each topic is a card carrying its name, one sentence saying what the topic is about, its live piece count, and a control into its tag landing page.

| Property | Value |
|---|---|
| Grid | 3 desktop, 2 tablet, 1 phone, 24px gap, per DSRD 7 §4.1 |
| Title | The tag name exactly as DSRD 1 §5.6 registers it. Como, the 16 step, 600, brand dark |
| Description | One sentence. Mulish 14px/400, soft grey, line-height 1.5 |
| Count and control | Separated by a hairline inside the card. The count in Mulish 13px soft grey on the left, the control in brand orange on the right |
| Link | The whole card links to `/learn/tags/{slug}/` |
| Shell | The §6.0 card family shell: 12px radius, hairline border, `--shadow-card` |

**What the ruling costs, named rather than hidden.** The list showed all 36 topics in about one screen. **The cards take roughly four.** Kain chose the longer page knowingly, on both rendered in front of him, and the reason the cards win is that this page's job is to help someone who does not yet know what they want. A name alone serves the reader who already knows; a name plus a sentence serves the reader who does not, and that is who arrives here.

**It also creates a real dependency, and this is the important consequence.** The card is only worth its extra length if the sentence on it is good. **Thirty six description lines are now load-bearing on this page**, where on the list they were optional.

**That copy exists and is approved: DSRD 2 §1.3.4, the 36 confirmed tag descriptions, ruled by Kain at S238.** It is the same copy §34.4 uses on the tag landing page's own hero, so the two pages share one piece of writing rather than two, and a change to a description changes both pages at once.

**One thing to check on the render rather than assume.** Those lines were written to a 138 to 148 character band, for a meta description and a full-width line beneath a heading. **On a card at a third of the frame that is roughly four lines of text**, which may be more than a browsing card wants to carry. Whether the card shows the description whole, clamps it, or takes a shorter form written for this one slot is Kain's on the rendered page. **Nothing is shortened on paper**: the approved copy is used as it stands until he says otherwise.

**A card is not built without its sentence.** The approved copy exists, so this is a guard rather than a live risk: where a description is ever missing, the topic still renders, with its name, its count and its control, and no placeholder text. A card carrying invented copy is worse than a card carrying none.

### 35.5 What is settled and what is open

**Settled by Kain at S313:** the page exists, it lives at `/learn/tags/`, it groups the topics into four reader-facing families, and each topic is a card rather than a line.

| # | Open item | Whose, and how it closes |
|---|---|---|
| 1 | ~~The 36 description sentences~~ | **CLOSED S313.** DSRD 2 §1.3.4, approved by Kain at S238. See §35.4 |
| 2 | Whether the card carries the full approved line, clamps it, or takes a shorter form | Kain's, on the rendered card. The approved line is used whole until he rules otherwise |
| 3 | ~~The four family names as reader-facing headings~~ | **CLOSED S390, decided by Chat.** Outcomes, Problems, Approaches, Kinds of Reading. Kain sees them in place on the rendered page and can change any of them then; they were not put to him as words on their own |
| 4 | ~~Each family's supporting line~~ | **CLOSED S390, decided by Chat, 12 to 25 words each per DSRD 7 §3.3.** Kain sees them in place on the rendered page and can change any then. Outcomes (17): "The changes people come to psychology for, and the ideas and skills that help them get there." Problems (16): "Everyday difficulties people bring to psychology, and the ideas and skills that help with each one." Approaches (18): "The methods and schools of thought behind applied psychology, explained so you can see how each one works." Kinds of Reading (19): "The kinds of reading the library offers, whatever the subject, so you can choose how you want to learn." Worded without naming individual tags; not yet checked against DSRD 1 §5.6 |
| 5 | ~~Whether the families are ordered as above or by size~~ | **CLOSED S390, decided by Chat.** Meaning-first order stands (Outcomes, Problems, Approaches, Kinds of Reading). Size order would move with every new tag; this one never does |
| 6 | Vertical rhythm and internal spacing | Kain's at the spacing sitting on the rendered page |
| 7 | Phone and tablet behaviour | Follows the §21.9 pattern, confirmed on a render |

**Not a complete go-live specification.** The shape is ruled and the copy exists; the finish is not settled. Every remaining item closes at one rendered sitting with Kain.

**LOOK RULED, Kain S390 ("yes"), on both pages rendered whole at 1280, 834 and 390 in Chat's side panel.** The topic card is registered new in its build sheet and goes to DSRD 8 on Code's build. Piece counts, quotations and workbook cards in the render were stand-ins and were named as such. The count under each topic card is Mulish 12 where section 35.4's table said 13, to sit on the nine step scale (DSRD 7 section 3.0). Still open: the four family icons (not registered), and the spacing sitting.

*The counts in the render Kain ruled on were invented and he was told so before he ruled; the real counts come from the database at build time.*

---

### 35.5b The 36 tile lines and titles are Kain's own words (S177, 20 October 2026; written home by Chat at the S436 close, 21 October 2026)

Kain wrote all 36 tile lines himself in the S177 sitting and they are built in as written at 0.707.377, with his own tile titles at 0.707.378. His rule: no line may grow. DSRD 2 section 1.3.4's S238 descriptions are superseded on the All Tags tiles and on the tag pages by these lines. Code's ruling file follows whole. Still owed: the hero line under Browse by Topic (ASK__All_Tags_36_Tile_Lines_And_The_Hero_Line_Kain_Asks_S177, hero half).

#### RULING: the All Tags tile lines are Kain's own words (S177, 20 October 2026)

Kain wrote all 36 himself in the S177 sitting (relayed by the S176 theme session). Built in exactly as written at 0.707.377, on the build site at /learn/tags/. One change, with his approval and no longer than his original: Learn CBT spells the term out, 116 characters against his 119. His rule: no line may grow; a full term goes in only if other words come out.

##### His lines, by tag (as built)

1. understand-your-mind (tile title in his list: Understand Your Mind): Explore how thoughts, beliefs and habits shape your experience, and develop a clearer understanding of yourself and others.
2. build-confidence (tile title in his list: Build Confidence): Develop genuine self-confidence through greater self-awareness, practical competence and trust in your own judgement.
3. develop-emotional-intelligence (tile title in his list: Emotional Intelligence): Learn to understand emotions, recognise what influences them and respond more wisely to yourself and others.
4. improve-relationships (tile title in his list: Improve Relationships): Build healthier relationships through honest communication, mutual understanding, greater trust and everyday consideration.
5. find-purpose-and-direction (tile title in his list: Find Your Direction): Understand what matters most to you, clarify your priorities and make choices that give your life greater direction.
6. achieve-your-goals (tile title in his list: Achieve Your Goals): Learn to set worthwhile goals, establish clear priorities and develop the discipline to turn intentions into consistent action.
7. lead-with-impact (tile title in his list: Lead With Impact): Develop the self-awareness, communication skills and sound judgement needed to lead others with integrity and confidence.
8. build-mental-resilience (tile title in his list: Build Mental Resilience): Strengthen your ability to handle pressure, respond to setbacks and remain steady through life's inevitable difficulties.
9. practice-mindfulness (tile title in his list: Practice Mindfulness): Develop greater awareness of your thoughts, feelings and conduct through honest reflection and present-moment understanding.
10. help-others-grow (tile title in his list: Help Others Grow): Develop the listening, questioning and helping skills that support others in building understanding and making their own progress.
11. support-mental-health (tile title in his list: Support Mental Health): Understand common mental health challenges, develop supportive habits and learn to respond to others with care and respect.
12. communicate-effectively (tile title in his list: Communicate Effectively): Learn to express yourself clearly, listen with understanding and handle everyday conversations with honesty and respect.
13. grow-self-awareness (tile title in his list: Grow Self-Awareness): Recognise your thoughts, motives, habits and blind spots, and understand how they influence your choices and behaviour.
14. master-your-mindset (tile title in his list: Master Your Mindset): Understand how your beliefs and thinking habits influence your life, and learn to question assumptions that get in your way.
15. increase-productivity (tile title in his list: Increase Productivity): Strengthen your focus, establish meaningful priorities and develop consistent working habits without neglecting your wellbeing.
16. unlock-personal-growth (tile title in his list: Unlock Personal Growth): Develop greater self-understanding, sounder judgement and the habits that support meaningful personal growth over time.
17. overcome-self-doubt (tile title in his list: Overcome Self-Doubt): Understand where self-doubt comes from, question limiting beliefs and develop confidence grounded in genuine self-knowledge.
18. manage-stress-and-anxiety (tile title in his list: Manage Stress & Anxiety): Explore the thoughts and circumstances behind stress and anxiety, and develop more considered ways of responding.
19. break-negative-thinking (tile title in his list: Break Negative Thinking): Recognise unhelpful thinking patterns, question assumptions and develop more accurate, balanced ways of understanding life.
20. navigate-life-changes (tile title in his list: Navigate Life Changes): Approach periods of uncertainty and transition with greater clarity, practical judgement and confidence in your next steps.
21. build-self-discipline (tile title in his list: Build Self-Discipline): Strengthen your ability to keep commitments, practise consistency and follow through on what matters, even when it's difficult.
22. strengthen-your-partnership (tile title in his list: Strengthen Your Bond): Build a stronger partnership through honest communication, mutual respect, deeper understanding and everyday commitment.
23. start-and-grow-a-business (tile title in his list: Start & Grow a Business): Explore the practical skills, sound decisions and personal qualities needed to build and sustain a worthwhile business.
24. overcome-feeling-stuck (tile title in his list: Overcome Feeling Stuck): Understand what may be keeping you stuck, reconsider unhelpful patterns and identify practical ways to move forward.
25. improve-social-confidence (tile title in his list: Build Social Confidence): Develop greater ease in social situations through self-understanding, better communication and genuine interpersonal confidence.
26. learn-nlp (tile title in his list: Understand NLP): Explore the principles and practices of Neuro-Linguistic Programming, including their applications, limitations and evidence.
27. learn-cbt (tile title in his list: Understand CBT): Understand how thoughts, feelings and behaviours interact, and explore the methods of Cognitive Behavioural Therapy.
28. learn-life-coaching (tile title in his list: Learn Life Coaching): Explore the principles, communication skills and practical approaches that help people make informed choices and meaningful progress.
29. learn-counselling (tile title in his list: Learn Counselling): Understand the foundations of counselling, including attentive listening, empathy and responsible approaches to supporting others.
30. learn-hypnotherapy (tile title in his list: Learn Hypnotherapy): Explore how hypnotherapy is practised, its proposed mechanisms, evidence, limitations and applications in supporting change.
31. learn-mindfulness (tile title in his list: Learn Mindfulness): Understand mindfulness as a process of honest self-reflection, developing self-awareness, insight and personal responsibility.
32. research-based (tile title in his list: Research-Based): Explore psychological ideas through published research, established theories and careful consideration of the available evidence.
33. practical-exercise (tile title in his list: Practical Exercises): Work through practical exercises, reflective questions and structured activities that help turn understanding into action.
34. deep-dive (tile title in his list: Deep Dive Articles; renamed Achology Long Reads by Kain at S448, 27 October 2026, because "deep dive" is a machine tell the Content Standard always fails; its All Tags family heading becomes "Long Reads and Styles" and the family line "Long Reads and Styles of Editorial Copywriting"; the web address stays /learn/tags/deep-dive/): Examine a subject in detail, exploring its underlying principles, important distinctions and practical implications.
35. beginner-friendly (tile title in his list: Beginner-Friendly): Discover clear, accessible introductions to unfamiliar subjects, with straightforward explanations and no prior knowledge required.
36. professional-practice (tile title in his list: Professional Practice): Explore the skills, judgement, ethical responsibilities and personal qualities involved in effective helping practice.

*Four lines changed on 17 November 2026 (Kain, Chat's seat: "Yes, sign them.") to take out words the Content Standard bans: the Master Your Mindset search title and description, the Overcome Feeling Stuck description and the Understand NLP description. Chat read the 36 tag pages back on the build site the same day: 36 of 36 answer, each with its own question title. Replacements are word swaps only; the reading page is READING_PAGE__Four_Tag_Page_Lines_S472 in the Tag Landing Page folder.*

##### Titles: Kain's own, on the tiles (0.707.378, his word "use the titles that I give you")

All 36 tiles show his titles. The tags themselves keep their registered names and web addresses (shown on the tiles only, so nothing moves). The eight that differ from the registered names: 3 Develop Emotional Intelligence (his: Emotional Intelligence); 5 Find Purpose & Direction (his: Find Your Direction); 22 Strengthen Your Partnership (his: Strengthen Your Bond); 25 Improve Social Confidence (his: Build Social Confidence); 26 Learn NLP (his: Understand NLP); 27 Learn CBT (his: Understand CBT); 33 Practical Exercise (his: Practical Exercises); 34 Deep Dive (his: Deep Dive Articles). 9 Practice Mindfulness stays, his word.

##### Fit, measured in WebKit on the build site

Tablet (834): all 36 in three lines. Phone (390): 28 in three, 8 in four (Help Others Grow, Support Mental Health, Overcome Self-Doubt, Break Negative Thinking, Improve Social Confidence, Learn Life Coaching, Learn Mindfulness, Beginner-Friendly). Desktop (1280), four tiles across: none in three; 7 in four, 29 in five. Nothing is shortened: the four-line cut was removed so every word shows. Code's earlier estimate in the ASK (about 33 characters a line) was wrong; the measured desktop tile holds about 26.

OWED BACK: the lines written home, and the hero line options.

*No em or en dashes in this file; checked before writing.*


### 35.6 The All Tags page is signed off (Kain, Code's S178 sitting, 21 October 2026; written home by Chat at the S437 close)

Kain's words: "Yes, I do, Claude. I sign the all tags page off. Brilliant work. Thank you very, very much." What he signed: /learn/tags/ on the build site at theme 0.707.398: Doors and Tiles with Family Tone and Soft Watermark (S176), the Topic Quilt with the Pointer Card, School Colours and Pointer Tiles three across (S177), his own 36 titles and lines (section 35.3 below), Chat's hero line under Browse by Topic (0.707.394, the banner levelled at 0.707.395), Tap to Preview on touch screens (0.707.396), the Faces Veil logo card (0.707.397) and the spacing check (0.707.398). Each was his pick from rendered options or his direct instruction, and each is written as KAIN'S CHOICE in the All Tags Index Page build sheet.

Tap to Preview, his choice from four rendered options (Tap to Preview, Named Squares, Family Shelves, Word Quilt): on any touch screen the quilt is unchanged; the first tap on a square marks it in its family colour and shows that topic's Pointer Card under the quilt, full width; a tap on the card, or on the same square again, opens the topic; the computer view is untouched. This answers the hindrance Chat's chapter 8 reading found, that on a phone the quilt was 36 icons with no words. Faces Veil, his choice from four: the book authors' faces from the Knowledge Hub front page banner, black and white, in three rows across the Know Your Psychology logo card under a cream veil that clears round the logo; the logo unchanged; no logo cards on a phone. Whether the other Knowledge Hub walls' logo cards follow is not decided; one page at a time.

The spacing check at 0.707.398, measured in WebKit at 1280, 834 and 390 against DSRD 7 section 4 and 4.3 and the signed Articles list banner, corrected the page's own rules in place (summary to the four kinds 24; buttons 8 apart, inset 16; quilt to key 24, key gaps 8 and 24; family heading to its line 8; tile and quilt card inset 24, 16 on a phone; buttons to quilt 48 on a tablet and 32 on a phone; hairline gaps 32 on a phone) and left alone, as shared with signed pages, the band's 48 top and 64 foot, the title to summary 16 and the rainbow line above the footer. Speed, measured: the server answers in about 0.3 s, the phone page loads in under a second, and a quilt square answers the mouse in well under 0.1 s. Chapter 8 of the DSRD 6 record is re-read on the built page at Chat's next walk.

## 36. Pricing Page Layout (APPROVED, BUILT AND PUBLISHED: Kain with Code in Safari, S121 to S128; recorded S380)

**Where the page's truth lives now.** Kain built this page block by block with Code in Safari across eight theme sessions (S121 to S128), starting from his own design package, and published it at S127 (page 36845, `/pricing/`). Per standing rule 19 and the S257 precedence, **the approved prototype in the Pricing Page folder is the signed record**, exported by Code after every ruling; this section is the decision history only. Sections 36.1 to 36.3 below still stand (the job, the arrival state, the changes). Sections 36.4 to 36.6 are the S365 derivation, kept as history and superseded by 36.7 onward. Prices, savings, names and checkout addresses are read from DSRD 4 and DSRD 5 at build, never from the package and never from here (Kain, S365).

**History of the S365 derivation.** Kain supplied a full prototype and handover pack for this page, in the Pricing Page folder, and ruled that it replaces the block order below. Two things below still stand because the package agrees with them: the Courses list is a short price list, not 28 full cards, and every price and checkout link is copied from DSRD 4.

One page, one instance, at `/pricing/` (PRD Pr1.19). Composed at S365 through `page-composition`, against the Document-Level Standards above. **Structure only.** Kain ruled at S257 that the page's look waits until the bundle, Access All Areas and membership cards are signed in their Safari sitting with Code, because the page is mostly those cards; this section fixes what the page carries and in what order, which does not change when the cards' look does. Prices, savings and checkout URLs are read from DSRD 4 section 1 at build, never from here. The page's design folder is the Pricing Page folder under Homepage + Commercial Design Prototypes.

### 36.1 The job

**This page exists to get a visitor who is weighing Achology up to choose the way of buying that fits them, and go to its checkout or its own page.** The four ways are one course, one school bundle, everything (the Access All Areas Pass), and membership; the free membership tier (DSRD 4 section 1.6's Free Membership) is the way in for anyone not ready to pay.

### 36.2 The reader's arrival state

| # | What is true on arrival | Basis |
|---|---|---|
| A1 | They broadly know what Achology is and are now asking what it costs | **Assumption.** They arrive from the header, a course page's Three Ways To Buy block, or a help answer that routes cost questions here (DSRD 2 section 2.24 item 7). Confirmed after launch from analytics |
| A2 | They are comparing ways to pay more than comparing courses | **Assumption,** grounded in the page's own job; the course comparison is the courses directory's job (DSRD 2 section 2.3) |
| A3 | Price, refunds and "is there a cheaper way in" are live worries | Evidenced: price and refund are two of the seven spine questions on every course page (DSRD 2 section 3.8) |
| A4 | Many read on a phone | **Assumption.** Confirmed after launch |

### 36.3 The changes, in the reader's voice

1. "I can see the four ways to buy, and roughly what each costs and includes."
2. "I believe these prices are for something many people value."
3. "I can find the price of the exact course or school I'm thinking about, and act on it."
4. "I know what membership gives me and what it costs after the $7 month."
5. "I see Access All Areas as the best value if I am serious, and the fastest route to Master Achologist" (DSRD 4 section 9.2).
6. "I know I can start free before I pay anything" (required wherever the $7 trial appears, DSRD 4 section 11).
7. "I no longer worry about losing my money or being locked in."
8. "I know whether I can pay in instalments."
9. "I know buying a course does not by itself make me accredited" (the honesty-against-interest pairing; PRD criterion 8).
10. "My remaining questions about upgrading, the $7 trial and cancelling are answered."

### 36.4 Page Structure (top to bottom; this is also the mobile order)

| # | Block | Change carried | Component |
|---|---|---|---|
| 1 | **Page heading** with the Trust Line beneath it | 2 | Trust Line, DSRD 4 section 14.2 variant 3, figures from the figure register |
| 2 | **Four ways in, side by side:** one course, one school, everything, membership; each a one-line statement of what it includes (courses, and months of community) and a "from" price, each linking down to its block below. Under the four, one line: not ready to pay, start free, to the free membership signup | 1, 6 | **New block, to be designed** |
| 3 | **Price lists, two tabs:** Courses, then School bundles. The Courses tab is a **short price list** (ruled by Kain, S365): each of the 28 courses as one row carrying its name, its price and the two actions (Learn More to the course page, Enrol Now to its Circle checkout), grouped under the three learning routes (DSRD 4 section 2, a partition of 28). The School bundles tab carries the seven bundle cards | 3 | Courses tab: **new component, the course price row, to be designed and signed.** Bundles tab: bundle card, DSRD 8 section 8 |
| 4 | **Product section block:** Monthly, Annual, Access All Areas, in that order, under its heading. The Monthly card sits with the start-free line beside it | 4, 5, 6 | Product section block, DSRD 8 section 11 |
| 5 | **Questions, opening in place:** can I upgrade; what happens after the $7 trial; can I cancel; what if it is not right for me (the course guarantee, the Access All Areas guarantee, and no refunds on subscriptions, stated plainly); can I pay in instalments; does buying a course make me accredited (one line, linking to the certification page) | 7, 8, 9, 10 | Question list pattern as used on the course page (DSRD 2 section 2.6 block 9) |

**The action repeats without a new change:** each product carries its own buy button where the reader meets it. No other exit is offered.

### 36.5 The two closing tests

**Every block carries a named change:** yes, all five. **Every change has a block:** yes, all ten.

**Removed against DSRD 2 section 2.8's earlier list:** the separate "What's included at each tier" block. Its change is carried by block 2 and by each card's own contents, so a separate block would say it a third time.

### 36.6 What is settled and what is open

**Settled by Kain at S365:** the Courses tab is a short price list, not the 28 full course cards, because on a phone 28 cards put the membership and Access All Areas cards far down the page, and the full cards already live on the courses directory. This supersedes DSRD 4 section 3.1's Tab 1 wording.

| # | Open item | Whose, and how it closes |
|---|---|---|
| 1 | The look of the whole page, blocks 2 and 3 included | Kain's, by eye, after the bundle, Access All Areas and membership cards are signed (S257) |
| 2 | Whether the Courses tab keeps DSRD 4's school and topic filter now it is a short list | Kain's, on the rendered list |
| 3 | The instalment answer's wording | Waits on Code confirming the real Circle and Stripe terms (the same fact DSRD 2 section 2.6 block 8 waits on) |
| 4 | The Access All Areas guarantee's terms | DSRD 4 section 1.3 says 100% money back but names no window; confirmed before the answer is written. **Closed 10 November 2026 (Chat branch):** the window is the signed Refund Policy's 14 days, now written in DSRD 4 section 1.3 |
| 5 | All copy | Written with Kain, per standing rule 19 |

**Not excluded by oversight:** the $399 DiMAP Course Upgrade (DSRD 4 section 1.1b) is not on this page; it is not among the products PRD criterion 3 requires the site to sell.

### 36.7 The page as built and ruled (top to bottom; the mobile order)

Read from Code's S121 to S128 session reports and the ruling files they name. Kain's own verdict governs the register: "this is just a pricing page. It's not a sales page" (S128).

| # | Block | Change carried (36.3) | Ruled |
|---|---|---|---|
| 1 | **The top panel:** the opening band with Kain's price-tag artwork, his own heading copy and three statement segments; the Chooser, four choice cards in his own words (one course, one school, everything, membership), each with its own colour on the price; his three guarantee statements, each linked to the help answer that proves it | 1, 7 | S121, S122 |
| 2 | **The course index:** nine course rows showing on load and a View All 28 Courses control that opens the rest (confirmed by Kain, S381, as the page he wants; the filed S123 ruling's "all 28, no expand control" is superseded), each row showing its full price and what it costs a month on one line; three category tabs in Kain's labels; an All Payment Options menu (replacing the budget filter and the 84-figure price grid); no search box | 3, 8 | S123, S124, S126 |
| 3 | **The schools grid:** seven artwork cards, courses on the face of each card as ruled hairline rows, the struck price as a faint diagonal, the same payment options menu, and the **Access All Areas Pass as the eighth card** (the seven schools listed with a bar in each school's colour, Kain's own drawing and three lines); all eight open on the reader's choice | 3, 5, 8 | S124, S125, S126, S128 |
| 4 | **The membership block**, arranged Under: Kain's heading and line, two actions, his inclusion lines (four removed at S128 as selling copy), and the free tier strip | 4, 6 | S126, S128 |
| 5 | **Questions:** the help article's own closing card, listing six real answers from the two price categories of the help section, in place of written answers on the page. **From 12 November 2026 the block stands Side by Side with the card off, on this page only (Kain, Code's S503 sitting, pick 13, section 36.9); the six answers and the shared question row are unchanged** | 7, 8, 9, 10 | S126, S503 |
| 6 | **The ending:** four doors, as the top panel's own cards, each pointing out to its product's page | the action | S126 |

### 36.8 The rulings, where each is recorded

Every ruling is filed as its own RULING file in the channel Archive, and folded by Code into the prototype. **S121:** the opening band; Kain's heading copy; one text line (site-wide, now DSRD 7 section 4.4a); four options minimum (The Harness). **S122:** the Chooser as the layout; his copy for the four choice cards; the cards' colour and design; the card line type with two copy changes; the opening band's artwork to the words' height; nine rulings on the top and the search bar. **S123:** the course index and the monthly figures; eleven rulings on the course block (including DSRD 7 section 5.5's form control type); the S121 separator width reversed (DSRD 7 section 4.4a). **S124:** the artwork card for the seven schools; ruled rows inside the card; his words for the school bundles heading; the card head and course list tightened; the banner audited and its gap closed; Payment Options replacing the budget box and price grid; the school cards taking the payment options menu. **S125:** the pass as the eighth card; the struck price as a faint diagonal; one footer on the school card with the seal; the footer as one set of three; the membership as a marked row on every school bundle; the plan menu renamed Pricing Options; quiet, with the plan control in his sentence; his replacement line for the schools block. **S126:** Ribbon for the pass drawing and Lift for the block of eight; the membership block Under; the questions block replaced; the four doors ending; the page approved as good enough to build. **S127:** eighteen rulings in one file; money for the saving and one width for its two lines; grouped for the page's rhythm; quiet for the peak and the pass button renamed; the page confirmed as drawing right as a real page. **S128:** the AA-safe control orange (`--color-orange-action` #C85015) on the last three controls and every primary button site-wide; the school cards open on the reader's choice; four membership lines removed.

### 36.9 What is open on this page

| # | Open item | Whose, and how it closes |
|---|---|---|
| 1 | The DSRD 6 record: §2, §3 and §5 failed and §1, §6, §7's hand half, §8 to §11 not run at S128 | Code runs them once the search values Chat sent at S380 are typed in; Chat runs the reading chapters |
| 2 | The four pages it links to do not exist: `/courses/`, `/academy/schools/`, `/access-all-areas/`, `/membership/` | Their own cards |
| 3 | The Circle and Stripe confirmations: currency and tax, included membership renewal, refund terms per product, instalment terms and rounding | Code, from the live checkout |
| 4 | Whether the free Circle tier carries a schema offer, and its name | **Closed S381 (Chat):** yes, an Offer named "Free Membership" at 0.00, DSRD 4 section 1.6's product name |
| 5 | Whether the page prints a visible breadcrumb, and DSRD 1 section 9's rows for the top-level commercial pages | Kain, by eye on the rendered page, tabbed, in his next Safari sitting with Code (asked S381) |
| 6 | Kain's line under the closing block | **Closed S127 (found S381):** Kain sent his own heading and line at S127 ("Our Curriculum is Designed to Help You Understand - You!"), built as typed; recorded in `pricing-parts.php` at the block |
| 7 | The course index | **Closed S381:** Kain confirmed the live page (nine rows and View All 28 Courses) is what he wants; row 2 of section 36.7 corrected |
| 8 | The membership card's inclusion list and this page's list differ | **Closed S381:** on purpose. Kain, S128: "this is just a pricing page. It's not a sales page." The page carries four lines, the cards the full list |

**36.9 Kain's rulings in Code's S209 sign-off walk (2 November 2026; written home by Chat, S453).**
- **The breadcrumb is added** (Kain: "Yes, add it."): the site's signed trail, Home then Pricing, word for word the BreadcrumbList the page already emitted, 48 below the header (32 on a phone) and 48 to the opening panel, starting on the title's edge. Built at theme 0.707.774 and 0.707.775. Pricing was the only built page without one.
- **The prices count up together** (Kain: "1, Count Up Together", option 1 of four): the four prices in the opening panel count up from nothing as the panel comes into view, over 1.3 seconds, slowing as they land, each ending on its own true text, held at final width so nothing moves; reduced motion and no script show the true prices. Built at theme 0.707.776, pricing.js. Further effects come one round at a time and are written here as Kain picks them.
- **Copy points (Chat's rulings, S453):** the closing block's heading and supporting line are Kain's own words from S127 (row 6) and stand as typed, so the gate's dash and supporting-line readings there are recorded exceptions, not faults. The choice cards' lines take sentence case ("For your first 30 days", "trial" in lower case mid-line), as card lines do across the site. "Senior and Master Achology members" in the free sign-up paragraph is Kain's own wording, placed at S448 as the pathway's levels; it stands, and Chat's R8 is closed.

**36.9 Pricing is signed off (Kain, Code's S209 sitting, 3 November 2026, theme 0.707.787; written home by Chat, S456).** Kain walked the page block by block and closed it in one word: "finished." Chapters 10 and 11 of its DSRD6_RECORD.md are written as pass, page_gate run at 0.707.787. His picks, each from four rendered options in the Change Viewer unless noted:
- **The breadcrumb,** Home then Pricing, on the title's edge (his yes; 0.707.774 to 0.707.787).
- **The four opening prices count up together** (Count Up Together; 0.707.776).
- **The Smooth Lift** on the opening cards, the school cards and the two membership plan cards (0.707.777 and 0.707.783).
- **The course table:** school marks under every course, the tabs with a sliding orange underline, and a Pay in full, Pay in 3, Pay in 5 switch on one line with the tabs. Kain signed the block as built: "As it is on the page right now. Change nothing else" (0.707.778 to 0.707.781). The button family sweep (DSRD 7 section 5.1) repainted these tabs and the switch at 0.707.788 without changing their size or place.
- **The school pictures Rise In** (0.707.782).
- **The page closes on the Knowledge Hub learning block,** as About does, in place of the repeat of the opening cards (his yes; 0.707.784 to 0.707.786). achology_pricing_help() stays in the theme, uncalled.
- **The Membership Plans card** reads "$7 trial" and "For your first 30 days" (0.707.781).
- **Turned down:** the savings shine, all four options ("they throw out the pricing design").

**Still open on Pricing, none changing the design:** the two pricing questions whose Help answers have empty excerpts, so they show no answer line; and the learning block's four unnamed inner spaces under Exception 21. Sentence case on the card lines is closed by the copy point above. The Rank Math lift from 78 to the page bar of 90 is owed by Chat (NOTE__Founder_And_Pricing_Rank_Math_After_Rescore_S203).

**36.9 Pricing reopened for a design review (Kain, Code's S489 theme sitting, 11 November 2026; written home by Chat, S465).** Kain reopened the look he signed at S209, for this page, on his own word: "I want you to look at this whole page now. Through the lens of the world's greatest web designer, graphic designer, I want you to review the entire page's layout, the design, the structure, use of spacing, and I want you to literally list what it is you would recommend." Each change is shown to him one at a time and written here as he picks it.
- **Links (Kain, same sitting):** "all internal links should open in the same tab. And all external links should open in a new tab. Just be a site-wide rule." This is DSRD 7 section 1.0 as written; the S125 new-tab ruling for the school, course and membership links on the cards no longer stands. Built at theme 0.707.986.
- **Pick 1, the four opening cards' buttons are quiet:** shown as one switch in the Change Viewer, Kain said: "I'm going to say yes to that, Claude." Each is the button family's outline button, so the buy buttons lower down are the page's only solid ones. Sizes and card heights unchanged. Built at theme 0.707.990.
- **Pick 2, the opening block is a hero that holds the breadcrumb (written by Chat, Session 465, evening).** Kain's own idea: "there's a lot of blocks, backgrounds, hairlines, right down this page ... It doesn't feel that smooth ... should we make this a hero? That incorporates the breadcrumbs." Shown as one switch in the Change Viewer, against the Certification page's signed hero band: "Yes, build it". The block's ground runs edge to edge from the site header down, with the breadcrumb on it; no rounded corners; the title one step under the breadcrumb; no hairline between the band and the course list; the Achology mark shown whole, where his S127 ruling had the panel's edge cut it. No word, card or size inside the block changed. Built at theme 0.707.992. This replaces the S209 breadcrumb placement above (48 to the opening panel).
- **Pick 3, the membership block is a band, and the free tier strip leaves the page.** Of the band: "Yeah, that's actually much better ... which I totally buy into, I really agree with your recommendation." The block's ground runs edge to edge to match the hero, with no rounded corners and no hairline above or below. In the same ship the Join Free bar came out on his ruling that the free Circle tier is ending (his words are in DSRD 4 section 1.6). Row 4 of section 36.7 therefore loses "and the free tier strip", and open item 4 of section 36.9, the free tier's schema offer, falls with it: the theme queue line for a Free Membership offer is withdrawn. Built at theme 0.707.995.
- **Pick 4, the three section lines take Lead with Bar:** "Yes, build it". Built at theme 0.707.996; the type and the width exception are in DSRD 7 section 3.3.
- **Pick 5, the two bands stand on Light Sand:** "Yes, build it". Built at theme 0.707.997; the run of grounds and its two recorded exceptions are in DSRD 7 section 3.3a, the dropped hairlines in section 4.3, Exception 25.
- **The Pass card's overline** is on the 0.08em rule (theme 0.707.998), a fault fix.
- **Pick 6, Quiet is live again on the school cards.** At S127 Kain chose Quiet: the seven school cards' buttons outlined, so the Pass card keeps the only solid button in the block of eight. The button family's rollout outweighed that paint and it was later removed as dead, so all eight had been solid since, including on the page he signed at S209. Shown the loss as one switch: "Yes, build it". Built at theme 0.708.001. Code's proposal of the Pass as its own full-width band is withdrawn: Kain saw the Pass at full width three ways at S127 and turned them down for Quiet, and it is not offered again.
- **Kain's ask for the next pricing sitting (his words at the S489 close):** "we've got obviously select the [Achology] course interests you, and that's really neat. But I'm just wondering if there might be a slightly neater way of presenting that. All the different options when the visitor kind of clicks. Also, the cards. The 8 different cards. I just wonder if there's any kind of visual improvements you would make to those cards as well. Maybe we can explore all of this in the next session." So the next sitting explores two blocks, the course list and the block of eight cards, each idea shown rendered, one decision at a time, after Code reads the rulings written beside their rules in pricing.css.
- **The third sitting's three picks (Kain, Code's S501 sitting, 11 November 2026; written by Chat, Session 465, evening).** *The course list changes softly:* "Yes, build it". Pressing a course kind or View All 28 Courses brings the courses in one after another, and pressing a way to pay fades the prices to the new figures, on the page's own Smooth Lift ease; reduced motion keeps the instant swap (theme 0.708.011). *The three course kinds stand stacked on a phone:* "Yes, build it"; the named exception is in DSRD 7 section 5.1 (on the build site at 0.708.013). *A course row warms under the pointer:* "Oh, I see what you mean, actually. Oh, yeah. Forget that. Much better. Yeah, that's much better. Yep, go for it. Build it." The row under the pointer takes Light Sand, bled one step past the column each side, the course name turns to its link orange, and the name's link covers the whole row, the price end included (theme 0.708.014). No word, figure, size or space changed in any of the three. Still to be shown: a card's course list easing open, and the facts under a school name never starting a line with a dot on a phone.
- **The last three picks (Kain, Code's S501 and S503 sittings, 11 November 2026; written by Chat, Session 466).** *A card's course list eases open:* "Yes, build it". The eight cards' course lists ease open and shut in a third of a second on the Smooth Lift's ease; the disclosure stays native, as his S128 ruling keeps it, and reduced motion or no script gets the snap (theme 0.708.016). *The facts under a school name never start a line with a dot on a phone:* "Yes, build it". Each fact carries its dot in a fixed slot at its left, clipped where it would start a line; the Pass card keeps its own mechanism, and its 3 extra height is his Grow ruling (S127), not a fault (theme 0.708.023). *The four top cards stand two by two on a phone:* "I'm going to say, yes, Claude". From 390 wide up the four opening cards stand two by two with their rows level; below 390 they stack, because View Membership does not fit a narrower card (theme 0.708.025). **Two sizes in it are recorded exceptions for this block on a phone (Chat's call, Session 466; Kain may overturn):** the price at 21 where it is 28 elsewhere, and the button's words at 12 where the family's are 14, both steps of the scale. The block sizes itself to its own width by a container query, not a screen breakpoint, so DSRD 7 section 4.5's two breakpoints stand untouched; Chat names container queries as allowed in section 4.5 (Backlog: Chat).
- **The gate's recorded exceptions on this page (Chat's calls, Session 465, evening; Kain may overturn).** The four opening cards' name and price are card text, not a heading with a supporting line. The learning block's line under "Where Would You Like to Begin?" is recorded for the component wherever it renders. "LIVE" in the membership list is a word in capitals for emphasis, as LIFETIME, ANY TIME, ALL and FREE already are on this page (DSRD 6 section 1). The eight SAVE labels keep 0.04em, because Kain's Grow ruling (S127) sized each struck price to the saving's own width. Small text on 1.6 and 1.4 keeps its line height inside the blocks Kain signed.
- **Pick 13, the questions stand Side by Side with their heading, and the Help card comes off (Kain, Code's S503 sitting, 12 November 2026; written by Chat the same day, in a side session of that sitting).** Walking the page in Safari, Kain asked Code to look at the block "from your best graphic design perspective and suggest an improvement", and said of it as it stood: "a little bit, I don't know, clunky, dry, bland, not quite so fitting with the rest of the page." Shown four looks for the block in the Change Viewer as one set of alternatives, he said: "Side by Side, yes". On a computer the heading stands in the left third on the page's column edge and the six questions run down the right two thirds as open rows, with the one faint hairline between them; under 1024 the heading stands above the rows. The words, the six questions, their order, the Q. mark and the row's movement under the pointer are untouched. **This replaces his S126 choice, that this block wear the Help article's own closing card, for this page only.** Every rule is scoped to this page's block, so the Help pages keep their card, and the Component Registry's row for the shared question row is unchanged. The three looks he did not pick (Open Rows, Two Columns in the Card, Sand Strip) stay in the round folder as previews and are not on the page. Built at theme 0.708.041. One fault inside the build was found when the block was photographed and mended before his word on the page: the first question stood 16 under its heading, where the round he picked from had them level (theme 0.708.044).
- **Pick 14, every heading has the same air above it (Kain, the same sitting).** Kain: "There seems to be a little bit inconsistent spacing down this page". Shown the mend as one switch in the Change Viewer: "yes, I choose even space round the sand bands as you recommend." A sand band, and the block after a band, take outside only what is left once the band's own inside space is counted. Measured on the build site: 96 above every heading at 1268 and 834, and 64 at 390, where the band headings had 144 and 88. Built at theme 0.708.042, in the pricing stylesheet only.
- **The questions heading stands without a supporting line (Chat's call, the same side session; Kain may overturn).** The block is a listing of answers that describe themselves, as the help hub headings are, so DSRD 7 section 3.3's rule 1 lets the heading stand alone. The gate's four failing rows at computer width were the check reading the first question's answer line as a supporting line; that is mended in the check, as section 3.3 now says, and no exception is recorded for this page.

**36.9 Kain's word on the whole page after the design review (Kain, Code's S503 sitting, 12 November 2026, theme 0.708.044; written home by Chat the same day).** The page was put in front of him in Safari on the build site with picks 1 to 14 built, and with two pictures of the questions block as built. Asked "Does the pricing page look right to you now?", Kain said: "Yes, it's right". This is his word on the look of the page as reopened at S489, and it stands beside his S209 "finished". It is written in the page's DSRD6_RECORD.md, chapters 10 and 11, by Code, who presented the page. It does not mark chapter 2 of that record: chapter 2 closes when the mended check is run on the page and the questions heading reads as a listing, and Code then cuts the approved prototype at the version served.

---

## 37. Workbook Page Layout (STRUCTURE WRITTEN S366; BAND AND CAPTURE RULED, Kain in Code's S152 sitting; CONTENT REBUILT, Kain with Chat, S411)

**S411 reconciliation, read first.** Kain rebuilt the page's content with Chat at S411, under `page-composition`, in DSRD 2 section 1.7, which now owns the job, the arrival state, the five changes, every section's standard and the approved Ladder of Inference words. Code's S152 sitting ruled the band, the three buttons, the side panel and the email card (DSRD 8 section 39). Where 37.1 to 37.5 below differ from those two, they are superseded and kept as the S366 record. The page order is now:

1. Sticky header (DSRD 8 section 18).
2. **Hero (band):** breadcrumb; H1 to DSRD 2 section 1.7's title standard; subtitle to its subtitle standard (two lines at most); the date line; the "Get Your Free Workbook" button; the workbook cover on the right inside the container.
3. **What Is [the idea]?**
4. **How This Workbook Helps You Learn**, with two or three inside pages of the workbook shown as pictures.
5. **What [the idea] Is Used For.**
6. **Where This Workbook Comes From**, with the course image left-aligned to the container, its top level with the first line of the second paragraph (Kain, S411).
7. **The email card** (DSRD 8 section 39 item 4): email only, the workbook emailed, never downloaded.
8. **Side panel:** the contents pinned at the top; the cover and the unframed email box at the foot (DSRD 8 section 39 item 3).
9. **"Browse More Achology Workbooks"** (Kain, S411), in place of the related workbooks shelf and of S152's "Browse More Achology Articles"; placeholders until more workbooks exist.
10. Two course cards (section 22.10), as every content page.
11. Rainbow stripe and footer (DSRD 8 section 19).

No Related Further Reading and no Know Your Psychology mark (S152). **After the form:** the reader lands on the thank-you page, one page for every workbook that knows which was requested (DSRD 2 section 1.7). Its layout is ruled in the S159 sitting (Kain with Code): one column at 960, a cream hero with three steps, a bridge of blocks before the two paths, the two paths as one split panel with identical cards, and the About page's gateway block at the foot. The full ruling and the order of blocks are in DSRD 2 section 1.7 (the thank-you page, S159).

**Open:** the email card's words and the consent box (Kain with Code, Chat's recommendation in DSRD 2 section 1.7); how the inside pages are shown; the Kit wiring and its cookie question (DSRD 3 section 6.5, settled by the S381 plain form).

**Added S438 (Kain, Code's S160 sitting).** The Ladder of Inference workbook (post 40321) is filler, a stand-in for building and testing; the page is finished on one of the ten improved workbooks once Kain has signed it, and Code then builds all ten (DSRD 2 section 1.7). Kain's S161 layout rulings for this page (RULING__Workbook_Page_Title_Subtitle_And_Layout_S161, in the channel Archive) are written here when he finishes the design with Code; until then the S411 order above stands as the record.

**The S366 record follows.**

**Added S401 (Kain's site standard, Code's S147):** the workbook page carries the reading progress line every content page carries (§32, item 5), and the reading column's width and body text size are the same as every other content type (§32, item 6).

One template serves every workbook landing page, at `/learn/{category}/workbooks/{slug}/` (DSRD 1; PRD Pr1.4). Written S366 from DSRD 2 §1.7 (the components) and §3.4.2 (the body), onto the content page standard the article and book note now share (§22, §32, Kain S112 and S113). **Structure only.** Kain rules the look on Code's rendered page in Safari (his S366 instruction for new page work), with any choice shown as options, tabbed. First real content: the Karpman Drama Triangle workbook record (Cowork, S347).

### 37.1 The job

Hand the reader one free workbook for practising an idea they already half know, in exchange for their email, and show them where to learn it properly.

### 37.2 The reader's arrival state

Arrives from search on a "free" plus topic phrase, or from the companion article. Knows the idea by name, wants to do something with it, is wary of handing over an email for nothing.

### 37.3 The changes, in the reader's voice

1. "This is the exercise I was looking for, and it is free." (hero, cover)
2. "I can see what I would actually be doing." (body, What's inside)
3. "Giving my email is worth it." (the capture block)
4. "If I want the full idea, I know where it is." (companion line, source book, courses)

### 37.4 Page structure (top to bottom; also the phone order)

1. Sticky header (DSRD 8 §18)
2. **Hero**, the content page hero (§22, as the article): breadcrumb, H1 (the workbook page's own title, carrying "free", DSRD 2 §1.7), category and tag pills. **The workbook cover sits in the hero** where the book note carries its jacket.
3. **Reading zone**, the article's own (§22 fourth round: 1104 grid, 800 column, 256 side rail). The body is DSRD 2 §3.4.2's five parts, in order.
4. **What's inside**, the list of the workbook's sections (DSRD 2 §1.7 item 7), placed straight after the body's second part, "What the exercise asks of you".
5. **The capture block**, directly after the body's capture line (§3.4.2 part 4): Kit form, email field and one button, released download on submit (DSRD 3 §3.1, placed by shortcode, never auto-inserted). **It also sits in the side rail**, under the cover that follows the reader (the §32 row 9 mechanism), so the form is in reach at every scroll point. One form, two placements. Design is Kain's on the render.
6. **Source book callout**, only when the workbook comes from a named book (§1.7 item 9), one line with the book note link.
7. **Side rail shelf:** 2 to 3 related workbooks from the same category or tags (§1.7 item 10), in the rail's shelf position, replacing Related Further Reading on this page type.
8. Share row at the foot, the article's position.
9. **Two course cards**, the words at §22.10 ("Ready to Take Your Learning Further?" since Code's S147), filled by the tag rule (DSRD 1 §5.7), as every content page.
10. Rainbow stripe and footer (DSRD 8 §19).

**No author block.** The body is the base voice with no pen name (DSRD 2 §3.4.2). **No trial panel**, matching the article and book note after S113.

### 37.5 What is settled and what is open

**Settled by this section:** the block order above, which follows DSRD 2 §1.7 and the S113 content page standard. It supersedes §1.7's own foot (its "Explore Related Learning Paths" is the two course cards; its schema line belongs to DSRD 3).

**Open, all for Kain on the rendered page:** the hero with a workbook cover in it; the capture block's look in the body and in the rail; the related workbooks shelf. **Open before the first form goes live, not before the render:** whether Kit's script waits for cookie consent (DSRD 3 §6.5); it is decided when Code wires the live form.

---

### 37.6 The hero from S162 (Kain with Code, theme session S162)

The workbook is part of the Soft Light family (§22.15): warm cream band, its cover standing straight on a faint bookshelf fading into the cream, and the email box (white field, burnt-orange button) and privacy line in the hero. **Its banner has no date line for now** (Kain: "take it out for now, then we'll figure out where we're going to place that once we get back to designing this actual page"): no date, reading time or "Practical Workbooks". Where that line lives is open, for the workbook page's design. The workbook has no theme template yet; the rest of §22.15 applies when it is built, unless Kain's workbook sitting rules otherwise. **The thank-you page's two paths block (S163)** is now the shared `achology_two_paths()` used by the content pages too; its course lesson count is read from the course's curriculum file, never typed (it read 175, the DiMAP's count, for every course before).

### 37.7 The workbook page as Kain ruled it in the S178 sitting (Code, theme session S178, 21 October 2026; written by Chat, S438)

Ruled by Kain on the rendered page in Safari, the real template in a local Playground on the Karpman record (test content only; no workbook is published on the build site). Branch theme/workbook-s178, not deployed at S438. Built from the record, not a new choice: the band is the S162 Soft Light hero (section 37.6), warm cream, the cover on a faint shelf, the email box and privacy line under the subtitle, no date line, the family's 984 frame; the title breaks after the colon at every width (DSRD 2 section 1.7, S161).

Kain's rulings, in his words, in the order made:
1. **Tablet band:** "that's a terrible use of space". On a tablet the title and subtitle on the left, the book on its shelf on the right from the breadcrumb's foot to the subtitle's foot, the email box and privacy line the band's full width under both. The phone keeps its stack.
2. **The close shows both paths:** "There should be two"; the course path is the workbook's own source course (DSRD 2 section 1.7).
3. **The right-hand column must not run over or under the full-width parts:** it is the S161 round ten column, the cover with the email box under it, held at the screen's foot and stopping at the column's end; Browse More and the close then run the full 984.
4. **No privacy line under the right-hand column's button:** "I want it removed. No arguments, just take it out." The band and the dark email card keep theirs.
5. **The In short note and the Used For notes take the Ruled Paper dressing** ("I actually really like ruled paper"), from four shown tabbed (Ruled Paper, Washi Tape, Folded Corner, Sticky Note), with two changes on all five notes: the pin sits on the paper, not on its top edge; and each Used For note reads as one sentence after its number ("1." then the text on the same line). The In short note's words are unchanged ("the top card is just spot on").
6. **The email card:** its own spacing restored to the approved S152 card's (8 under the heading, 16 under the line, 12 above the privacy line), its field and button the band's size.
7. **How This Workbook Helps You Learn:** "heavier text at the bottom and lighter text at the top. This is not good design practice"; the four step captions are 16 in the soft grey, a caption to each step's name and lighter than the lead above; balanced lines, a 32 gutter.

The spacing check (DSRD 6 section 0, S178) run at 1280, 834 and 390 in WebKit: the hairlines between parts are back (48 above and below, 32 on a phone); the cover is exactly roof to foundation in the band; the tablet Where This Workbook Comes From panel wraps its words round the cover. Owed: the sign-off line once Kain gives it, and the Workbook Page design folder's record. Code's file: RULING__Workbook_Page_S178, in the channel Archive. The S161 layout rulings (section 37's S438 note above) are folded into this section when the design is finished.

### 37.8 The workbook page is signed off, its ten finishing touches, and the fanning sheets (Kain, Code's S178 theme sitting, 21 October 2026; written by Chat, S440)

This carries on from section 37.7, which recorded the S178 rulings up to the page being judged. Everything below was ruled by Kain in the same sitting, on the rendered page in Safari: the real template in a local Playground on the Karpman record, which is test content only. Each of the ten touches was shown Before and After with its movement played. Branch theme/workbook-s178, its last commit the Fan on Hover stack.

**The sign-off.** Kain: "Yes, Claude, I sign off the workbook page. It is absolutely magnificent." He signed everything in section 37.7, the ten touches below, and the four steps' sheets as stacks of pages that fan gently, each page behind a different design. This is the sign-off line that 37.7 said was owed.

**What shipped, and when.** The page shipped as theme 0.707.412 (commit bb4a23dc on main, deployed and verified: local, server and zip agree, and the PHP lint is clean on the server). Section 37.7 recorded the branch as not deployed at S438; it has since shipped. On the build site the page is drawn on the Ladder of Inference draft only (post 40321, which is filler: Kain, S160), seen through the workbench key. No workbook is published. The band is the family's own `achology_kh_hero()`, which gained an `after` slot for the email box; the article, book note and quote pages are unchanged, checked on the build site. The spacing check (DSRD 6 section 0) was run at 1280, 834 and 390: 48 between parts (32 on a phone), 64 around the band (48 on a phone), no overlaps while scrolling and no console errors.

**The ten finishing touches.** Kain asked for ten improvements "that would make this page visually spectacular", naming the floating Where This Workbook Comes From box first. His answer on seeing them played: "Yes, Claude, this is brilliant. I would really like to take all 10 ... The after option literally brings this page to life." All ten were taken:
1. Where This Workbook Comes From is its own full-width warm cream band, with a hairline at its top and its foot, no box and no hairlines around it.
2. There is no hairline above the email card: a box stands on its own space.
3. The right-hand cover and email box arrive once the band has scrolled away, and ride just under the header, so there is no doubled cover and no empty column.
4. What [the idea] Is Used For takes its section mark, as every other section heading does.
5. The workbook's sheets straighten and lift under the pointer, and open full size on a click.
6. The four-step path draws itself as it arrives: the dashed line first, then each number.
7. The notes settle onto the page as they arrive, the pin last.
8. The band's shelf drifts slower than the page, and the book lifts under the pointer.
9. The workbook in the email card opens a little, like a book, under the pointer.
10. Each block rises gently into place as it arrives.

None of the movement plays for a reader who asks for reduced motion, and without scripts every block simply shows.

**The four steps' sheets are stacks of pages that fan under the pointer.** Kain: "because the workbook actually typically contains multiple pages per section, it'd be great if this part of the page could reflect that ... if I can see one page, stacked upon other pages, I'm going to automatically assume this is quite a comprehensive resource ... they're actually genuinely going to be comprehensive resources." Four ways were shown on the page: Neat Stack, Fanned, Thick Pad and Fan on Hover. Kain chose **Fan on Hover**, with two changes: "I need the background pages to all be different ... each of the background pages to all be a different design", and "the fanning out to be a little bit more subtle". So each step's sheet has two pages behind it, squared up at rest and fanning gently under the pointer. Each of the eight is laid out as that step's kind of page (teaching, reflection questions, the exercise, discussion questions), drawn by the theme, so every workbook has them with no extra files.

**The same ten-touch exercise runs next on the other three content pages.** Kain: "take this exact same task to all other of the three article pages. Once you've locked this in." The same exercise, ten touches each, is to be shown played out Before and After on the article page (section 22), the book note page (section 32) and the quote page (section 40), in that order, in a new theme session. Those three sections record their own touches when Kain chooses them; nothing is recorded for them here.

**The tidy, after the sign-off (shipped 0.707.415).** Kain, on signing the page: "run this page ... through the full gate. I want you to run spacing checks. I want you to check the code. Clear out any dead code. If there's anything you need to compress, tidy up. I want you to do all of this without coming back to me and asking for any more permission to do so. I want this page and all the back-end code made absolutely immaculate ... absolutely beyond lightweight." Code did it and shipped it as 0.707.415, deployed and pushed:
- `workbook.css` (34 KB) and `workbook.js` (3 KB) hold the workbook's own rules and behaviour and load on workbook pages only, so every other Knowledge Hub page stops downloading them.
- `book-note.css` (70 KB) no longer loads on the workbook, because nothing in it renders there.
- The old dark band's rules, unused by any template since the workbook joined the Soft Light band, are removed from `book-note.css`, `knowledge-hub.css` and `quote.css`, about 16 KB in all, with one note left where they stood. `single-workbook.php` is tidied, and the CSS gate passes all five sheets.
- Proved, not assumed: the workbook page was compared element by element against the signed version at seven widths, with nothing that renders changed. A book note, a quote page, an article and the Book Notes list were each loaded with the old and the new sheets at 1440, 1024, 834 and 390, with zero differences in any computed style, and the same check catches a planted one-property change. The theme's `css_deletion_proof.py` could not run, because its mirror served a page as a download; that is named for the theme queue.

**The page's DSRD 6 record is opened, with its machine half owed.** The record is in the Workbook Page design folder. Kain's half of chapters 10 and 11 is recorded there as his sign-off words above; his live-page half waits on the first signed workbook on the build site. Owed by Code: the page gate run on the workbook (the Ladder draft), the record's machine half, the workbook's structured data and the Kit form. The field names the template reads (`workbook_subtitle`, `workbook_parts`, `workbook_step_pages`, `source_course`) still wait on ASK__Workbook_Page_Field_Names_The_Template_Reads_S176. The thank-you page's two tight inner values (step label to text 4; the path card's line to name 0) are left as signed, pending Kain's call on re-checking signed pages.

**The side panel is The Dark Card (Kain, Code's S494 workbook page sitting, 11 November 2026; written home by Chat, S465).** Of the old column (cover, name, email, tick box, button) Kain said: "it just doesn't look designed. It doesn't look polished. It looks scrappy, especially with the tick box". From four designs in the Change Viewer he chose the third: "The Dark Card please ... it actually ties in with a secondary opt-in block further down the page. So, that's perfect. These two opt-in cards are now a family." As built at theme 0.707.991, from 1200 wide only: the cover and the request sit in the page's own dark bookshelf card, the one under Where This Workbook Comes From, with the same picture and wash laid top to bottom; radius 16; the cover 160 wide and centred; white fields; white words beside the tick box; the orange button; the tick box under the fields' icons; the parts 16 apart; still sticky. The fields, the button and the form's words and order (DSRD 4 section 5.1) are unchanged. **The two dark opt-in cards are one family (Chat's call):** a change to either is shown to Kain on both, and the One Line round for the foot card shows him the pair.

**Where This Workbook Comes From is Words First, with the cover level with the words (Kain, Code's S494 workbook page sitting, 11 November 2026; written home by Chat, Session 465, evening).** Kain, asking for a whole-page audit: "where this workbook comes from block, just seems a little bit imbalanced to me". On four designs in the Change Viewer: "that actually looks a little bit better, to be honest with you. Words first, your recommendation's good." Then, of the cover: "the image kind of sits aligned with the top of the title, which is great, but it doesn't sit aligned with the bottom of the last paragraph on a desktop." Shown the cover levelled with the last paragraph: "Yes, build it". As built at theme 0.707.999: the heading and the words stand on the page's left edge; the course cover closes the block on the right, in front of the faint mark; the cream band stays; the cover's shadow is the quiet picture shadow. From 1200 wide the cover starts level with the heading and ends level with the last paragraph, its width found by workbook.js between 200 and 320, nothing cropped; with no script it is 240 wide. From 1024 to 1199 the cover is 240 on the right; from 768 to 1023 it floats right and the words wrap round it; on a phone the words come first and a 120 cover closes the block. No word changed. **The two workbooks whose words run longest (Chat's call):** on 84 of 86 the cover ends level with the last paragraph; on two it stands at its largest and ends 45 above it. A factory read names the two. Where either's words run past the length DSRD 2 section 1.7 gives this part, Chat brings them inside it under the workbook pack, with Kain's signature; where they are inside it, the 45 stands.

**The parts under the In Short note are Two by Two (Kain, Code's S500 workbook page sitting, 11 November 2026; written home by Chat, Session 465, evening).** Kain, on the built Karpman page: "This block just looks, it's just words dumped on a page. It doesn't really seem to be doing much for the page. I'm just wondering if there's a way we could make that a bit more visually impressive." On four designs: "Yes, Claude, I do like the 2x2 ... It's just all very, very samey ... I'm definitely drawn towards the 2x2, but it's still not quite right." Shown Two by Two with four switches, two of them on: "Yes, build it". As built at theme 0.708.007 and 0.708.009: the block's opening sentence is the site's Lead with Bar, by its class; the parts stand in two columns, each under a thin line that starts with a short orange piece; each name on its own line in the heading face at 21; each sentence the page's quieter text, 16 on 1.6 in soft grey; a lone last part runs the full width; one column on a phone. The parts carry no numbers, because an idea's parts are not always steps. Turned down: orange names and bigger names. No word changed.

**One space above the footer (Kain, the same sitting).** "There's quite a lot of spacing. Just above the footer", then, to fixing it and bringing the four designs above: "Yes, do both". Built at theme 0.707.994; the rule and the family fix for articles and quote pages are DSRD 7 section 4.3, Exception 26.

**The gate's recorded exceptions on the workbook page and its thank-you page (Chat's calls, Session 465; Kain may overturn).** From the afternoon: the breadcrumb space under the hero Kain signed; NLP in another workbook's card title; the 32 under Browse More's line, which on a computer the gate reads as 12 to the covers that rise beside the line, the list itself standing 32 under it; the thank-you page's four spaces from S160; and centred blocks keeping their centred line. Added this evening, on Code's S500 report: the Como 33 headings (28 on a phone) of the shared closing block, "Ready to Further Your Learning?" (Kain, S164), and of the thank-you page's two blocks (Kain, S160); and the spaces inside those signed blocks and How This Workbook Helps You Learn (19 from heading to line, 28 to 29 from its line to the step pictures, and 48, 32 on a phone, from line to block). Each is inside a block Kain signed, on the same ground as the course page's free lessons heading (DSRD 7 section 3.3) and its fourteen spaces. Nothing moves. **Lapsed for How This Workbook Helps You Learn (Chat, Session 465, night, on Code's S500 board):** that block is now left-aligned on Kain's word, with its line as the Lead with Bar and 16 and 24 declared on the scale, so its centred-line and spacing exceptions come out and the gate reads it as any block. The exceptions for Ready to Further Your Learning and the thank-you page stand. **The closing block's Live tag and Lessons chip keep their padding of 5,** DSRD 7 section 4.3 Exception 19 ("a tag's drawn padding"), entered at the gate for the component wherever it renders. **WordPress's own size copies of an upload** (names ending as "-768x994") are not editor resize suffixes: the gate judges the upload's own name (Chat's call, Session 465, night).

**The 86 workbook pages' scores (Code's S496 read, 11 November 2026; written by Chat, Session 465, evening).** 49 pages read 91 and 37 read 85. All 86 miss Rank Math's content length test, which is never met by padding (DSRD 6 section 5 item 11). The 37 also miss the focus phrase in the address, and an address is never changed to pass (Kain, S051). Sixteen of the 37 are the named set Kain ruled on 4 November 2026 ("stay as they are", DSRD 6 section 5 item 11). The other 21 are not covered by that ruling, which says no other page inherits it; whether they stay as they are was put to Kain. **He answered the same evening (Code's S498 sitting, 11 November 2026): "Yes, leave the 21".** All 37 stay as they are at 85; no address, phrase or word is changed to gain the point (DSRD 6 section 5 item 11). **And his sitting on the 86 workbook pages waits until the workbook page's look is settled:** "Yes, wait". **Browse More's titles are one size up, 18** (Kain, Code's S500 sitting: "Yes, build 1"; theme 0.708.013; the Browse More rules are section 22.16a, since DSRD 8 holds no Browse More table). **Each title's ending is a small note** (Kain, the same sitting: "4 Ending as a note please"; theme 0.708.024; section 22.16a item 4).

**The lower dark card is One Line from 1200 wide (Kain, Code's S500 workbook page sitting, 11 November 2026; theme 0.708.018 to 0.708.020; written home by Chat, Session 465, night).** Kain asked at the open for "the lower dark card shown beside the side panel as a pair", then "Yes, show me"; on two switches in the Change Viewer, with One Line as Code's recommendation: "Yes, One Line". From 1200 wide the card's name, email and button are one white bar, as the hero, with the tick box on a quiet line under the bar's first icon. The fields, the button, the tick box and every word are the signed ones. Below 1200 the card is 680 wide and a bar would leave the email field too narrow, so there the card stands as it was. The template writes the button before the tick box in this card, as in the hero. **Below 1200 the card is to show the button first and the tick box under it, as the hero does at every width (Chat's call, Session 465, night; put to Kain as one Before and After in his walk of the page, and his to overturn),** so the order the eye meets and the order a keyboard meets are one at every width. The side panel keeps the tick box, then the button.

**The workbook page board (Kain, Code's S500 workbook page sitting, 11 November 2026; theme 0.708.026; written home by Chat, Session 465, night).** Kain asked for the items to be taken together: "Is there any way that we could take all of the items at the same time? ... This is just taking like a long time here." Offered one board with each row built as Code recommended: "yes". On the board he ruled four things in one message, each built:
1. **How This Workbook Helps You Learn on a phone, each step one row:** "on a phone, that learn should just be in the same line as the actual round number. That would allow us just to drop a little bit of white space. Maybe make the block a little bit neater." A 96 sheet at the left, the number disc (32) and the step's name on one line beside it, the sentence under them, read from the left. The block is 1,119 tall on Karpman where it was 2,305.
2. **That block's heading and line on the left edge at every width:** "In terms of the second heading on the left, yeah, let's just go with that." The line is the Lead with Bar, by its class. The four steps keep their centred captions on a computer and a tablet.
3. **On a phone, the course picture and its button centred, the picture larger:** "on a phone, that they explore this course call to action. We might as well kind of probably centralize that. With the course image, and you might as well kind of make that larger too." The picture is 200 wide and centred, Explore This Course centred above it.
4. **On a phone, the lower dark card centred, its cover larger:** "And then get your free workbook. I might as well increase the size of the workbook, and essentially centralize all that as well." The cover 180 wide, the heading and line centred, the fields and button the full width as before.
No word changed. The empty space beside the In Short note was measured and left off the board: the side panel waits only while the top form is on screen, and a fix moved it by 50 to 90 of scrolling.

**The lower card's order below 1200 is kept (Kain, Code's S506 workbook page sitting, 12 November 2026; theme 0.708.039; written home by Chat, Session 465, night).** Shown as one Before and After in the Change Viewer with the question "Below a computer's width, the lower card's tick box sits under the button, as it does in the top form. Keep it?", Kain said: "Yes, keep it". Below 1200 the lower dark card shows the button, then the tick box under it, as the hero does at every width; the one order rule is out of workbook.css. The call above is no longer Chat's: it is his.

**The finished workbook page is signed off (Kain, Code's S506 workbook page sitting, 12 November 2026; theme 0.708.039; written home by Chat, Session 465, night).** On the Karpman workbook page, open in his Safari, after a walk of every block from the title to the footer and the phone layout, Kain said: "Yes, signed off". He was told first that four lines of the page's record stay open and need nothing from his eye. His yes covers the page's look as built since the S178 sign-off, each part his own pick and each written above: the One Line hero (S486); the side panel as The Dark Card and Where This Workbook Comes From as Words First (S494); the parts under In Short as Two by Two, Browse More's titles at 18 with each ending as a small note, the lower dark card as One Line from 1200, the steps as rows on a phone, the learn heading on the left, the course picture and the lower card centred on a phone (S500); and the lower card's order below 1200 (S506). It is the page's look, not the record's close: DSRD 6 section 0 holds the page until no line of its record reads fail or not run. **The approved render is now `PROTOTYPE__Workbook_Page_S506_APPROVED.html`** in the Workbook Page design folder, cut by the theme's fold-back tool at 0.708.039 (The Harness, Rule 14). The S178 render, `PROTOTYPE__Workbook_Page_APPROVED/`, is moved to that folder's Archive (Chat's call): it shows a page Kain has since changed in many places, and a builder reading it would build the old page.

**The five supporting line readings of How This Workbook Helps You Learn (Chat's call, Session 465, night, on Code's S506 gate run; Kain may overturn).** With the block's exceptions lapsed, the gate read 19 from heading to line where 16 is declared, and 19.7 to 22.4 from the line to the step pictures where 24 is declared. Nothing on the page is off the scale: the heading stands in one 36 tall row with the block's icon, and the row's foot is 16 above the line; the step pictures are tilted 2 degrees (Kain, S161), and the gate read to a raised corner. So nothing on the page moves and no exception is written. The gate's reading is mended instead, as DSRD 7 section 3.3 now says: a heading that shares its row with a mark is measured from the foot of the row, and what follows the line is measured to its box as laid out, before any tilt or lift drawn on it.

## 38. Site Search Results Page Layout (COMPOSED AND APPROVED, Kain in Chat's side panel, S375; SIGNED OFF on the build site at theme 0.707.481, Kain, Code's S178 kh-search side session, 22 October 2026, section 38.9)

One template serves the site search results page, the page every search box on the site lands on (DSRD 1 §7, rewritten S366: one search, the whole site). It has two states, results and no results, and Kain approved the look of both on the S375 renders, tabbed, at desktop, tablet and phone widths (standing rule 16). The two approved prototypes are in the Search Results Page folder inside Knowledge Hub Design Prototypes; that folder's README names them. The page is `noindex, follow` (DSRD 1 §10). Its address is WordPress's own search address, `/?s={term}`, served by a `search.php` template (Chat's call, S375, because a query is not a permanent URL and DSRD 1 §1's rules govern permanent URLs only; overturnable).

**How search behaves is not in this section.** Scope, weighting, exact-name-first, synonyms, misspellings, the dropdown preview and the no-results log all live at DSRD 1 §7 and are not restated here. This section owns only how the page is laid out.

### 38.1 The job

Get someone who typed a word or two to click the one page they meant.

### 38.2 The reader's arrival state

Arrives from any search box on the site (header, /learn/ hero, /help/, the 404) having just typed something. **Assumption, labelled:** most searches are one to three words, often a course name, an abbreviation (CBT, NLP) or a problem word (Baymard's 2026 search benchmark on query types; Achology's own no-results log does not exist until launch, DSRD 1 §7.5). They expect the search-engine shape: their words at the top, a list below.

### 38.3 The changes, in the reader's voice

1. "That is what I typed, and I can fix it here." (the field, pre-filled)
2. "I can see how many there are." (the count line)
3. "I can narrow this to the kind of page I want." (the pills and the sort)
4. "I can tell which one I meant, and why it matched." (the result row: type label, title, snippet)
5. "There are more if I need them." (pagination)

No results: 1. "Nothing was found, and I have not missed it." 2. "It might be my spelling, and here is the fix." 3. "I can browse instead." 4. "I can take something away anyway." 5. "I can ask a person."

Both tests run (page-composition, rule 10): every block below carries one of these changes, and every change has a block.

### 38.4 Page structure, results state (top to bottom; also the phone order)

1. Sticky header (DSRD 8 §18), carrying the site search field per DSRD 1 §7.4.
2. **No breadcrumb.** A results page is not a place on the site map (DSRD 1 §9 mirrors the URL hierarchy, and this page has none).
3. **The search field**, pre-filled with the query, in the 880px measure at the 1200 frame's left: the DSRD 7 §5.5 field (44px, Mulish 14, 10px radius, hairline border, search glyph inset 16px) with the §5.1 primary button at the field's height as its Submit, reading "Search". 48px below the header, per DSRD 7 §4.3 ruling 5.
4. **The count line**, 16px below the field: "{N} results for "{term}"", Mulish 14, soft grey #5E6B75, the number and the word "results" at weight 600 in brand dark. Singular "1 result".
5. **The control bar**, 24px below the count, the listing page's own unified bar (§21.4): left, the type pills All, Articles, Book Notes, Quotes, Workbooks, Help, Courses, Pages; right, the sort pills Most Relevant, Newest. Same pill values as §21.4 (Como 12/500, 8px 16px, 20px radius; active brand orange with white text; inactive off-white). The Category filter DSRD 1 §7.2 names is carried by the type pills' second row only when a Knowledge Hub type is selected; on All it is not shown, because help answers, courses and pages have no Knowledge Hub category (Chat's call, S375; overturnable). Phone: two rows per §21.9.
6. **Hairline**, 48/48 (32/32 on phones), DSRD 7 §4.3.
7. **The results**, one column, 880px measure, 16px between rows. **Approved: option B, the full-width row with a snippet** (Kain, S375, from two tabbed options; option A, the mini card grid, is kept in the prototype as the loser). Each row is the locked mini card (DSRD 8 §6.9) stretched to the column: 96px thumbnail left, then the type label (Como 11/600 uppercase, AA-safe orange #B8460F), the title (Como 16/600, brand dark, two-line clamp), and one new element, **the snippet**: Mulish 14/400, line-height 1.5, soft grey, two-line clamp, 6px under the title, the matched excerpt with the matched words in weight 600. No watermark at this width. The row is one link to the page.
   - **Type labels and thumbnails by page kind.** Article, Book Note, Quote, Workbook: exactly §6.9. Three new kinds, proposed by Chat and approved on the render: **Course** (thumbnail: the course's school colour, DSRD 5, with the `graduation-cap` glyph in white), **Help** (off-white thumbnail with the `circle-question-mark` glyph in brand orange), **Page** (off-white with `file-text` in brand orange; used for school, commercial and policy pages). These three labels are added to the mini card's label set in DSRD 8 §6.9 at the next unlock, and this line is that section's pointer until then.
   - Rank order is SearchWP's relevance (DSRD 1 §7.1); this section does not group results by kind.
8. **Numbered pagination**, DSRD 7 §17.1 and §21.9 (compact on phones), 48px above (32 on phones), 10 results per page.
9. Rainbow stripe and footer (DSRD 8 §19), 64px above (48 on phones).

### 38.5 Page structure, no-results state (top to bottom; also the phone order)

Blocks 1 to 3 as above, then:

4. **The not-found line**, 24px below the field (the page-title spacing, DSRD 7 §4.3): "We couldn't find anything for "{term}"" as the page's H1, Como 24/700 (the one H2 size, DSRD 7 §3.1, used here as the H1 because the page title is a sentence, not a name; Chat's call, overturnable on the Safari read). Kain's S366 words.
5. **The hint line**, 16px below, Mulish 18 body: **"Did you mean {corrected term}? Or try a shorter phrase."** when SearchWP can supply a correction (the corrected term is a link that runs the corrected search), otherwise **"Check the spelling, or try a shorter phrase."** Added on Kain's yes at S375, from Nielsen Norman's no-results guidelines and Baymard's finding that readers ignore spelling advice but click a corrected word.
6. Hairline.
7. **Browse by subject**: block heading "Browse by subject" (Como 24/600) with its supporting line, then the seven category cards, the locked card from the category hub (DSRD 8, as §20 uses it), in a 4/2/1 grid. The seven names come from DSRD 1 §4.
8. Hairline.
9. **The workbook offer**: the site's workbook lead-magnet capture (DSRD 4 §5; the Kit form, DSRD 3 §3.1), one heading, one line, one button.
10. **The ask line**, 24px below: "Can't find it? Ask us and a real person will point you the right way." with "Ask us" linking to /enquiries/. Added on Kain's yes at S375 (Baymard: a human door on the page readers are most likely to leave from). The wording is Chat's and Kain may change it.
11. Rainbow stripe and footer.

No controls bar and no pagination in this state. No humour anywhere on it (Nielsen Norman, guideline 3; DSRD 1 §7.3).

### 38.6 What is settled and what is open

**Settled by this section:** both block orders, the result row (option B) and every value above that is copied from a locked section. **Settled by Kain's eye at S375:** the shape of both states.

**Open, for Code's Safari sitting, not for Chat:** the header search control and the dropdown preview (DSRD 1 §7.2 and §7.4; the theme holds the header, so standing rule 16 puts that render in Safari; the S321 brief commissions it). **Open on a fact from Code:** whether SearchWP on the install supplies a spelling correction and phrase synonyms (`ASK__What_SearchWP_On_The_Install_Can_Actually_Do_S366`); the build does not wait on it, because block 5 has its fallback line.

**Stand-ins in the prototypes, named so nobody reads them as decisions:** the snippet text in every row (the real one is the page's excerpt), the workbook offer's words (DSRD 4 §5 owns them), the category card drawn as a plain tile (the locked card replaces it at build), and Mulish standing in for Como on titles (Como was not available in Chat's environment at S375).

**Corrected S378:** the "locked card from the category hub" named in block 7 of 38.5 does not exist. The category hub has no category card (its subject navigation is the pill strip, §20.5). The subject card is registered new in §39.5, where the Knowledge Hub front page needs it, and block 7 here takes that card once Kain has approved it.

**Answered at S178 (Kain, Code's S178 kh-search side session, 21 October 2026; written by Chat, S440).** Section 38.7 answers two of the open items above: it records the fact from Code that the build site's search already corrects spelling (the SearchWP question; phrase synonyms are not mentioned there and stay open), and the words the workbook offer uses on the no-results page (the learning path's signed workbook step words, because DSRD 4 section 5's form words are not written); it also changes the results row of block 7 to two across and adds the band's kinds bar, but it does not touch the header search control and its dropdown preview, which stay open for Code's Safari sitting.

### 38.7 What Kain chose for the top of the page and the filter bar, in Code's S178 side session (Kain, Code's S178 kh-search side session, 21 October 2026; written by Chat, S440)

This adds to the S375 composition and changes none of it except where Kain says so below. Kain chose from four rendered options in Safari (theme previews/kh-search-s178: 1 The Family Band, 2 The Plate, 3 Kinds in the Band, 4 The Answer Panel), each drawn in three states from real build site searches: "anxiety" (80 results), "procrastination" (9) and "enneagram" (none).

**Choice 1: Kinds in the Band (option 3).** Kain: "Yes, Claude, I'm definitely drawn towards kind three. Kinds in the band, I'm definitely drawn towards that." It is the light family band as on the signed lists, with no trail (section 38.4 block 2). In the band, in this order: the "Knowledge Hub" eyebrow; the title "Search the Knowledge Hub" at the one title size; the field pre-filled with the search, with its Search button (block 3); the count line (block 4); then the four-kinds bar the lists use (icons, joined), showing All and each kind that has results, each with its count, and the sort (Most Relevant, Newest) at its right end (block 5). The dark Categories bar with its "All Categories" label follows. The results start 48 below it, with no hairline, because the dark bar is the divider. With no results, the band keeps its title and field in the same place, and the not-found line and the hint follow the field (38.5 blocks 4 and 5).

**Choice 2: the results in two columns, Two Across (round 2, option 1 of four).** Kain asked for it ("maybe two columns ... a little bit neater"), then chose from four rendered ways (Two Across, Picture on Top, Larger Picture, Lead and Pairs): "Yes, Claude, definitely. Let's take the two across. As my pick." This changes the S375 option B on his own word: the same result card (picture left, kind label, title, snippet) now sits two to a row across the full page width, 24 apart, each pair the same height. A grid that would end with a gap ends with the Know Your Psychology logo card, his standing rule for every Knowledge Hub wall. On a phone it returns to one column, 16 apart, with no logo card. Preview commit 93b869ee.

**Choice 3: the search word directory, the Index Below, which becomes an A to Z tab on a phone (round 3).** Kain asked for an A to Z: "I know when I kind of look at a search block like that, I don't know what to type into it. Whereas if I'm browsing an A to Z, I would simply click on the topic that I'm drawn to." He ruled its source: "a word must have been mentioned so many times across all of the articles, in order for it to warrant place on the directory ... a search word directory." He then chose from four rendered placements (Letters in the Band, Index Below, An A to Z Tab, Opens From the Box): "Number two, the index below. The index below kind of makes really good sense, on both desktop and tablet. And I think that could probably switch into an A to Z tab for mobile." The rule, as built: a word earns a place when it is a noun naming a theme and it appears on at least five different published pages (pages, not mentions). The machine lets 786 words through, and a person reads them and keeps the theme words (244 at S178, from Acceptance to Worry, including procrastination, confidence, self-esteem and temperament). Each word shows its number of results and runs that search. On a desktop and a tablet the whole directory sits below the results, under a hairline, headed "A to Z", in four columns (three on a tablet), each letter's words under it. On a phone the index leaves the foot of the page and becomes an "A to Z" tab in the kinds bar, which swaps the results for the directory. With no results, the directory follows the no-results blocks.

**Choice 4, directed by Kain in the same message (no options; his words are the spec).** The pictures in the result cards are slightly wider, and book note cards show the book larger, on the same background the Book Notes pages give a book: "We need consistency throughout this entire site."

**Choice 5: Code's ten improvements, all made at once on Kain's ask** ("look at the page objectively ... ten areas that we have to improve"). The A to Z runs across the full width with a row of letters to jump to; each word's count is the pages that really use it; the index columns start level; the band, the workbook box and the ask line run to the results' full width; the searched word is bold in each title; on a phone, titles take three lines and the kinds become one row the reader swipes; and with no results, the A to Z words sharing the search's first letters appear under the hint. Preview commit d4dbd847.

**The concept is signed (Kain, S178).** "conceptually, this page is fine, all right? But what we now need to do is just build it into the actual website." Code builds it into the theme next, and the page's sign-off follows on the built page, by the process Code defines for it (filed beside the ruling).

**An earlier open item, now answered.** Kain wanted an A to Z way into the search on this page, beneath what it offers, so that a reader who does not know what to type can click a theme instead ("procrastination ... confidence, self-knowledge, self-esteem ... the kind of word we would essentially have a stance on"). Code had proposed the 56 Achology Stances in the Newsroom Vault as its source. Choice 3 above answers it, with the source Kain ruled. The front page research session carries the same idea as a corner link, "See every topic and theme, A to Z" (section 39.10).

**Three facts found in the build.**
1. The build site search already corrects spelling. This is the fact that section 38.6 left open (whether SearchWP on the install supplies a spelling correction); the hint line of section 38.5 block 5 and its fallback are unchanged.
2. The search returns only articles, book notes and quote articles today. Section 38.4 block 5 names more kinds (Workbooks, Help, Courses and Pages); the build does not return them yet.
3. The workbook offer on the no-results page uses the learning path's signed workbook step words, because DSRD 4 section 5's form words are not written.

---

### 38.8 The ten touches, nine taken (Kain, Code's S178 kh-search side session, 22 October 2026; shipped 0.707.436; written by Chat, S441)

Shown to Kain on the real page (theme previews/kh-search-touches-s178, built as 0.707.435), each touch before and after at three widths. Card arrival was left out of the ten on purpose, because it is the shared Rise in turn (DSRD 8 section 41), which plays on this page's results too. Code recommended nine of the ten and left out touch 8, the search words turning orange under the pointer, because with touch 7 two orange things would light on one result at once. Kain, asked "Shall I build in all ten except 8?": "yes, please do Claude".

The nine, all on the page's own parts (the field, the count, the result's insides and the A to Z), none on a shared part:
1. The number of results counts up as the page opens.
2. The reader's search words get a soft highlighter stroke, one result after another.
3. The search box glows softly orange when the reader clicks into it.
4. When the reader types new words, the Search button glows ready.
5. When the reader presses Search, the magnifier sweeps while the next page loads.
6. A result's picture moves a little closer under the pointer.
7. An orange line appears under a result's title under the pointer.
9. A book turns to face the reader under the pointer.
10. When the reader jumps to a letter in the A to Z, its orange line draws in.

Built as theme 0.707.436 and checked in WebKit at 1280, 834 and 390: every touch plays, no console error, no sideways scroll. Under reduced motion nothing moves and the count simply shows; the pointer touches play only where there is a pointer. Code's file: RULING__Search_Results_Page_Ten_Touches_S178, in the channel Archive.

**Rise in turn plays on this page's results (Kain, Code's S179 theme sitting, 22 October 2026; shipped 0.707.439; written by Chat, S441).** The cards arrive one after another as they scroll into view, by the shared card's rule. The rule and its record live in DSRD 8 section 41; this line only says the wall carries it.

**Two of the nine changed later the same sitting (Kain, Code's S178 kh-search side session, 22 October 2026; written by Chat, S442).** Touch 2 is replaced: the search words are coloured Achology orange, shown at once, with no highlighter drawn behind them (section 38.9, why it matched). Touch 7 is taken off: "I hate that, Claude. I really don't like that at all. I don't like the underline." Eight touches stand: 1, 3, 4, 5, 6, 9, 10, and 2 as the orange word.

### 38.9 Walking the built page to sign-off (Kain, Code's S178 kh-search side session, 22 October 2026; signed at theme 0.707.481; written by Chat, S442)

Each pick below was made on the real page in Code's player at three widths, from four rendered options against Before. Where a pick changes 38.4, 38.5 or 38.7, this section wins.

1. **Why it matched: The Words Around It.** The line under each title was the start of the summary, which showed the search word under 4 of 10 results for "anxiety" and 0 of 9 for "procrastination". Code recommended The Sentence; Kain chose The Words Around It: a short run of words either side of the search word, with an ellipsis at each end. Where a page never uses the word, the summary shows as before. This replaces the snippet rule of 38.4 block 7.
2. **The search word in orange.** The matched words in a result's title and line are the theme's text orange, which reads clearly on white, shown at once, nothing drawn behind them. Kain: "I would rather just see the word coloured [Achology] orange." This replaces 38.4 block 7's weight 600 and touch 2 of 38.8.
3. **Words and reading time at the foot.** Every result, the related piece included, ends with the card rule's line, "N Words · M Minute Read", from the same count its own page prints (DSRD 8 section 6.0). Kain: "yes please do Claude".
4. **The Best Match tag.** The first result on page one of a search sorted by relevance carries a small orange badge reading "Best Match", its words centred, beside the kind label, with a soft thin orange edge. Kain: "the badge is already doing the majority of the work", so the edge is subtle; "capitalize the M in match".
5. **No Know Your Psychology logo on the search page, ever.** Kain: "I don't ever want that included visibly as an option." The logo card that ended an odd row of results and the one in the no-results subject grid both go. This replaces 38.7 choice 2's logo card and is the one exception to section 20.0h rule 6.
6. **Even numbers.** A search with an odd number of results ends its last page with one more piece, the closest related one from the same subject as the last result, rather than hiding a real result; the count line still gives the true number. Kain: "It actually makes sense to add one related result from the same subject rather than remove." No workbooks offer in the no-results page's eighth subject space: "For the simple reason that this is a search page."
7. **The clear cross and the count line.** The browser's own clear button is replaced by a thin grey cross that appears only when the box holds words and turns Achology orange under the pointer. The count line reads "80 results for "anxiety"", the searched words in the same orange as the results. Kain: "One and one."
8. **The A to Z is Whole Letters.** No letter carries over into the next column; every column starts on a letter; four columns on a computer, three on a tablet, two on a phone; the letters split where the columns end most level, worked out again by the page whenever the word list grows. Without the page's script it falls back to the columns as built. Kain: "I think five is nice." The space between a word and its number is one step of the spacing scale, 8. Shipped 0.707.445.
9. **Page numbers: Short Run, always centred, Round Disc.** Family wide; the home is DSRD 7 section 17.1 (and 21.9 D3 here). The search page's left alignment goes.
10. **The no-results block is Popular Searches.** Heading "No results for "{search}"", then "Check the spelling, or try one of these popular searches.", then the eight most used words of the search word directory (the A to Z's own list, kept by a person), each with its page count, each running its own search. Kain: "let's go with option one. Let's lock this in." This replaces the not-found line and the hint line of 38.5 blocks 4 and 5. There is no hairline between the Browse by Subject heading and its list; the header there takes the family's unruled form.
11. **The no-results subjects are a Warm Numbers list, Counts Close.** The seven subject cards left a gap once the logo and the workbooks offer were ruled out, so they became a Subject List (one subject a row). Kain asked for it to be less "white and bland", chose Warm Numbers ("And now design this really well"), then Counts Close for the rows: warm cream rows; a large pale orange number for each subject (42, 28 on a phone, after the font scan); a hairline after the number; the name with its line beneath, the line held to 52 characters; the counts a set 48 after it, left aligned; an orange arrow disc on the far right. A phone keeps its stacked rows. It is the search page's own list, so the shared subject card is untouched. This replaces 38.5 block 7.
12. **SearchWP, five settings changed (Kain's yes, "yes, please do").** The record is in DSRD 3 section 9.8. The topic tags and subjects are searched; the weights rebalanced so the article's own words count; only the custom fields that carry reader words are searched; search statistics on; synonyms added. This partly answers 38.6's open question on synonyms.
13. **The font and spacing scan.** Every text on the page sits on the nine type steps; the one fault, the Warm Number at 48, was fixed at 0.707.481. One shared fault is named for the family and not changed here: the topic pill drops to 13 on a phone (a Backlog: Code line).

**Signed off.** Kain, after all five stages of his page approval process (DSRD 6 section 0.1): "Yeah, I'm totally happy to sign off the search results page now. Thank you, Claude. That's brilliant." The page as signed is theme 0.707.481 with the SearchWP settings above. The gate and the page's records (its DSRD 6 record, the approved prototype, the build sheet and the A to Z fill note) follow from Code under the process named in the Search Results Page folder.

### 38.10 The records, the gate exceptions and what waits (Code's S178 kh-search side session, 22 October 2026; final theme 0.707.484; written by Chat, S442)

**The records are filed** in the Search Results Page design folder: the DSRD 6 record, the approved prototype (the page saved whole in its three states, opening without WordPress), the build sheet with every value as built, and the note on how the A to Z is filled. The gate's own-page faults found at 0.707.481 were fixed at 0.707.484 with no visible change (the Best Match badge and the A to Z counts raised to AA contrast, the clear cross drawn from the icon registry, result pictures with srcset, the dividers on the blocks' own edges); kh-search.css passes the stylesheet gate with no dead rules.

**Six gate exceptions, approved by Kain** ("Yeah, that's fine. Happy to follow your guidance here, Claude.", after Code gave the standard practice that a site's own search results stay out of search engines' index): the address (/?s= by design); the Rank Math score, keyword density and meta description (the page is noindex, follow, with no description, keywords or score); orphan (it is reached by searching); acronyms (the results' own words); the 10-word no-results line (block-heading, his own pick); and the workbook offer's tile drawing (icon-registry). They are in page_gate's exceptions for the route /?s=, and the gate now reads an address's query, so the pattern can never touch the homepage.

**What still fails, none of it this page's to fix:** the gate looks up a record by path, and /?s= has the root path (the record is kept by hand until the gate can match a query route); the readiness board does not list this page; the gate can measure a card row mid-arrival under Rise in turn; two article picture files carry a version number in their names (factory); quote face pictures carry no srcset, and the topic pill drops to 13 on a phone (family, Backlog: Code); and Chat's reader halves of the record (chapters 1, 6, 7 and 8) are not run.

**Answered from the S375 brief:** the no-results hint is Popular Searches (38.9 item 10), the "Did you mean" form shown and found nearly idle because partial matching already finds everyday misspellings (eight tried, all found). Exact names tested: two book titles and Viktor Frankl return their own pages first; a course name returns nothing, because the engine covers the four Knowledge Hub kinds only. SearchWP's settings are in DSRD 3 §9.8; statistics log every search; the Metrics extension waits for launch (DSRD 1 §7.5).

**Open:** the scope, which is Chat's to rule: DSRD 1 §7.1 asks for one index over the whole site, and the page Kain designed and signed is "Search the Knowledge Hub" over four kinds; the DiMAP synonym (its expansion is not in DSRD 1) and the problem-phrase synonyms ("can't stop worrying"), both waiting on Chat's list; the SiteGround dynamic cache exclusion for /?s=, not yet checked; and the 404 page's search box, a separate theme job.

---


**The scope is settled (Kain, S448, 27 October 2026; written by Chat, S448).** One search for the whole site, with a Knowledge Hub shortcut: the header search's results page is headed "Search Achology" and shows Help answers as their own kind in the band; the Knowledge Hub front page's box opens on the same page filtered to the Knowledge Hub's kinds, says so, and offers one click to widen. The heading and band were signed as "Search the Knowledge Hub" over four kinds at 0.707.481; this replaces the heading's words and adds one kind, and nothing else on the signed page changes. The reasons are in DSRD 1 section 7.1.
## 39. Knowledge Hub Front Page Layout (COMPOSITION AGREED, Kain S378; LOOK RULED, Kain S390)

One page at `/learn/` (DSRD 1 §2.4; PRD Pr1.8). Its contents were listed in DSRD 2 §1.2; it had no layout here until S378. **This section holds the composition only** (page-composition, rule 11): the job, the reader, the changes and the block order, agreed by Kain in words at S378. How each block looks is ruled by his eye on a render, and recorded here when it is.

### 39.1 The job

Get someone who arrives at /learn/ to pick one way into the library and go to it. **Subordinate job:** take a free workbook.

### 39.2 The reader's arrival state

**Assumption, labelled:** arrives from the header's Learn link or the mega menu, or from the "Learn" crumb on any Knowledge Hub page. Knows Achology is a school; does not yet know what the library holds or how it is organised. A smaller share arrives from a search engine on the Knowledge Hub's name. No evidence yet; the first real evidence is the page's own analytics after launch (DSRD 3 §6.4, Rank Math Analytics).

### 39.3 The changes, in the reader's voice

1. "I know where I am."
2. "This is Achology's free library, and I know roughly what is in it."
3. "I know who writes it, so I can trust it." (the gap the completeness check found, S378)
4. "I can find what I already have in mind."
5. "I can pick my subject."
6. "I can follow a goal or a problem I have, across subjects."
7. "It is alive, and I can start reading something now."
8. "I can get something free to practise with."

The completeness check for a routing page (page-composition, rule 6) was run: where am I (1), what is here (2), is it for me (5, 6), why trust it (3), where next (4 to 8). Both tests run: every block below carries a change, and every change has a block.

### 39.4 Page structure (top to bottom; also the phone order)

1. Sticky header (DSRD 8 §18).
2. **Breadcrumb**, Home > Learn, the §20.3 component. Change 1. *DSRD 2 §1.2 listed it last; every other page puts it first, so it moves to the top here (S378). DSRD 2 §1.2 is corrected to match.*
3. **The top block**: H1, one line on what the library is, the four counts across the whole Hub (articles, book notes, quotes, workbooks, each linking to its cross-category listing, as the §20.4 counts do), one line naming who writes it, and the site search field (the §38 field, DSRD 7 §5.5, per DSRD 1 §7.4). Changes 2, 3 and 4. Words owed: the H1, the line, the trust line.
4. **Subjects**: section header (DSRD 8 §23) and seven subject cards, one per DSRD 1 §4 category, each linking to /learn/{category}/. Change 5. **New component, §39.5.**
5. **Topics**: section header and a strip of topic pills (the §20.8 pill), each linking to /learn/tags/{slug}/, with a link to the all topics index (§35). Change 6. Which topics it carries is owed (DSRD 2 §1.2 says "curated outcome and problem tags"; no list is written).
6. **Latest articles**, **latest book notes**, **latest quotes**: three sections, each a section header with its View all link (to the cross-category listing) and one row of the standard card (DSRD 8 §6.1, §6.2, §6.3), newest first, auto-filled, no curation. Change 7.
7. **The free workbook offer**: the same workbook capture block §38.5 block 9 uses (DSRD 4 §5; the Kit form, DSRD 3 §3.1), so the site has one. Change 8. *DSRD 2 §1.2 called it a banner; one shared block replaces a second design.*
8. Rainbow stripe and footer (DSRD 8 §19).

### 39.5 New component: the subject card

Registered S378. Seven of them on this page; the same card replaces the plain tile in §38's no-results state. Carries, per DSRD 2 §1.2: the subject's name (DSRD 1 §4), one short line on the subject, and its content counts. **The short line (Kain, S378): the first sentence of each subject's own hero intro (§20.9), word for word.** Kain wrote the intros himself at Chat session 27; no new copy is written for the card. The card's line reads from the same source as the hub hero, so the two can never drift. Look not decided; ruled by Kain on a render, then filed to the component library with its prototype and build sheet.

### 39.6 What is settled and what is open

**The words (Kain, S378, approved as drafted by Chat):**
- **H1:** The Achology Knowledge Hub
- **Top line:** Free articles, book notes, quotes and workbooks on psychology and how people live, from Achology, an online school of applied psychology. Pick a subject, follow a topic, or search for what you have in mind.
- **Trust line:** Every piece is sourced, and edited and approved by a named person at Achology. Read how we write. ("Read how we write" links to /policies/how-we-write/, DSRD 1 §2.6.)
- **Topic strip, 12, in this order:** Manage Stress & Anxiety, Overcome Self-Doubt, Break Negative Thinking, Overcome Feeling Stuck, Navigate Life Changes, Build Self-Discipline, Build Confidence, Improve Relationships, Find Purpose & Direction, Grow Self-Awareness, Help Others Grow, Achieve Your Goals. Chat's pick, unevidenced: the problems a first-time visitor most often brings plus the broadest goals. **Kept by Kain at S378, with a review:** an AnswerSocrates check was tried and cannot rank topics against each other (each term is scaled to its own peak), so the strip is reviewed after launch against the site's own search log (DSRD 1 §7.5) and Rank Math Analytics (DSRD 3 §6.4), and reordered from what readers actually type and click.
- **Section headings:** Browse by Subject, Explore by Topic, Latest Articles, New Book Notes, Latest Quotes. **Supporting lines (DSRD 8 §23.4; Kain, S378):** Browse by Subject: "Seven subjects, each with its own articles, book notes, quotes and workbooks." Explore by Topic: "Follow one goal or problem across every subject.", with a "See all 36 topics" link to /learn/tags/. The three latest rows reuse the approved cross-category listing intros (DSRD 2 §4.3) for articles, book notes and quotes, word for word.

**Settled (Kain, S378, in words):** the job, the changes and the block order above. **LOOK RULED, Kain S390 ("yes"), on the whole page rendered at 1280, 834 and 390 in Chat's side panel, reusing the locked header, footer, breadcrumb, section header, pill and the three card types, with the subject card new.** The approved file and its build sheet are in the page's design folder. The subject card is registered in the build sheet and goes to DSRD 8 on Code's build. Counts, quotations and the workbook offer's words in the render were stand-ins and were named as such. **Open, for Kain's eye on a render:** nothing further on the look. **Open, words:** none. **Open, one fact:** how many articles, book notes and quotes exist at launch, which decides whether each latest row shows three or six cards; read from the launch content set before the render.

---

### 39.7 and 39.8 (numbers not used)

These two numbers were skipped when sections 39.9 to 39.15 were written, and those later numbers are named in other documents, so they are kept as they are rather than renumbered (Chat, S448). Nothing is missing here.

### 39.9 The front page direction as Kain chose it, rounds 1 to 6 (S177, 20 October 2026; written home by Chat at the S436 close, 21 October 2026)

Kain's choices change block 6 of the S378 composition and the S390 look: the light family band, not the dark top; the three latest rows go, replaced by one mixed masonry wall of articles, book notes and quote articles; a kinds row above the wall leading to the four main list pages; and, through rounds 2 to 6, The Living Wall of black and white faces of real people the Knowledge Hub covers, Torchlight's depth, Face of the Moment with names appearing in the search bar on hover, and The Logo Introduces simplified, with the Know Your Psychology logo transparent and prominent on the right and no caption. Kain will hand Code new banner text; until it arrives section 39.6's words stay. Code's ruling file follows whole; Code is still adding rounds to it in the channel, so the live file in TO Chat is the later word until Code's S177 closes.

#### RULING: the Knowledge Hub front page direction (Kain, S177, theme)

**For Chat: record these choices in DSRD 9 section 39 and the front page build sheet. They change the S378 composition (block 6) and the S390 look.**

Kain chose from four rendered directions (previews/kh-front-s177: The Family Band, The Reading Room, The Picture Wall, The Seven Doors). His choices, part by part, in his words where given:

1. **Between two.** "I actually really do like the family band ... But I also like the picture wall ... something in between the family band and the picture wall."
2. **The banner.** "a cleaner banner that follows the same color theme we've used throughout the rest of the knowledge hub. Otherwise, we're kind of breaking our own style rules here." (So: the light family band, not the dark top.)
3. **The three latest rows go.** "rather than showing latest articles, new book notes, latest quotes ... we just literally have one of our masonry grids ... the masonry grid is just kind of a mixture." (One mixed wall of articles, book notes and quote articles, the same wall the lists and subject pages use.)
4. **A kinds row above the wall.** "a secondary section that's like different options, like one tab that ... leads through to the main articles page, the main book notes page, the main quote articles page, and workbooks page. So I think it'd be great if that sat above the masonry grid."
5. **Why.** "at the moment, the page just seems very, very empty, very unstructured, and not a particularly great user experience."

Next: four new rendered options built on these choices, one creative; Kain picks; that pick is added here.

OWED BACK: Chat folds choices 2 to 4 into DSRD 9 section 39 (block 6 becomes the kinds row and one mixed wall) and the build sheet.

##### Round 2 (Kain, S177): between option 1 and option 4, as a spectrum of six

Kain saw four options on his round 1 choices (1 Band and Mosaic, 2 Subjects in the Band, 3 Numbers and Cards, 4 The Living Wall). His words: "I think I'm sitting somewhere in between number one band and mosaic and number four the living wall. Except the living wall if that was just to be authors I think that would be actually really quite nice ... it needs to not just be the images that I've created for articles. It needs to be the faces of people, that people visiting the Knowledge Hub would be likely to recognize. Such as Sigmund Freud, Abraham Maslow, Albert Ellis, myself, and a few others. You might just alternate every time someone clicks ... start with like band and mosaic, keep that as number one, have the living wall as number six, except change the images in living wall with faces of people ... images that we have of people actual people from within the Knowledge Hub, and then spectrum that four different variations in between one and six."

So: six options. 1 = Band and Mosaic unchanged. 6 = The Living Wall with the banner's pictures replaced by the faces of real people the Knowledge Hub covers, a different set on each visit. 2 to 5 step between them. His pick from the six is added here.

##### Round 3 (Kain, S177): THE LIVING WALL is the direction

From the six (1 Band and Mosaic to 6 The Living Wall of faces), Kain chose 6: "I absolutely love the living wall. The creative version ... this is definitely the direction we want to go in ... absolutely stunning ... genuinely beautiful to look at ... magnificent." The background of faces stays ("with this kind of background, love it").
Open, in his words: "it's a wee bit harder to read the knowledge hub. Like the impact of the word the knowledge hub with the icon underneath that is just lost a little bit. Because the images are kind of pulling through"; "how we can make the entire hero slightly more balanced"; "there's also an opportunity to build in the know your psychology logo in this. Unquestionably, somewhere, but I'm not sure where."
Next: six variations of The Living Wall answering those three; his pick is added here.

##### Round 4 (Kain, S177): TORCHLIGHT's depth; six variations of it

From the six Living Wall variations, Kain chose the depth of 6, Torchlight: "The depth of the torchlight option feels right to me ... Some of the others just feel way too deep ... the knowledge hub is ... a gateway into all the knowledge throughout the website."
Kept, his words: "the way that you've presented the heading, the text, the search bar, I love it."
Rule, his words: "The Know Your Psychology logo, you've got to lose the white background ... the logos inside of the file system ... are just SVG and PNG versions, and they're all transparent backgrounds ... you've got to go back to the original logo." (The white-plate logo card belongs to the masonry walls only.)
The torch itself: "I'm not convinced on the actual torchlight itself, because when you scroll over the dark words, you can't actually see ... as a concept, I think it's brilliant ... it might just need to dim down and become more subtle when it's hovering over the text."
Next: six variations of Torchlight; his pick is added here.

##### Round 5 (Kain, S177): FACE OF THE MOMENT, black and white, logo centred on the right

From six Torchlight variations Kain chose 4, Face of the Moment: "yes, I do really like the face of the moment."
Changes, his words: "the Know Your Psychology logo we've got to centralize that or position that where the logo anchor is ... just make the Know Your Psychology logo centralized on the right-hand side of the hero banner ... it feels like everything's crammed across the left-hand side"; "still use the face of the moment, spotlight option, but just have them hover over black and white faces ... Not color ones. So maybe just make them all black and white."
Next: a few options in this direction; his pick is added here.

##### Round 6 (Kain, S177): THE LOGO INTRODUCES, simplified

From four Face of the Moment options Kain chose 4, The Logo Introduces: "definitely like the logo introduces". Changes, his words:
- "what I don't like is the name, and the dots underneath the actual logo" (no caption under the logo).
- The names move into the search: "you could have like search the knowledge hub, but when someone hovers over the face, you could have names popping up in the knowledge hub search bar. So it's like someone's actually typing ... then someone obviously clicks into the search bar, they can type whatever they want."
- Balance: "right align it to the edge of the container, maybe make it a little bit larger. And centralize it. With this left-hand block"; "The Know Your Psychology I would say needs to take a more prominent position, not just kind of dropped on the page."
- The left block: "you've got knowledge hub, then the achology knowledge hub, and that doesn't make any sense" (the small "Knowledge Hub" label above the title goes).
- "Simplify, more impactful, less noise."
- Words: Kain will hand Code new text for the banner ("I'm going to give you the text to improve what's written in this hero banner"). Until it arrives the approved DSRD 9 section 39.6 words stay.
Next: four options; his pick is added here.

##### Round 7 (Kain, S177): QUIET WALL; the trust line leaves the banner; balance the spacing

From four simplified options Kain chose 4, Quiet Wall: "they actually like the quiet wall creative". Two instructions, his words:
- "lose the disclaimer text underneath that search bar. That does not need to be in the hero of the Achology Knowledge Hub ... please remove it right now." (The trust line, DSRD 9 section 39.6, leaves the banner. Chat: section 39.3 change 3 and section 39.4 item 3 need correcting; whether the line lives elsewhere on the page is Chat's to propose to Kain.)
- "what we now need to do is really address the spacing issues on this page. Because the spacing is imbalanced."

##### Kain's banner words (S177), word for word, replacing DSRD 9 section 39.6's top line

H1 (unchanged): The Achology Knowledge Hub
Line under it: There's always more to discover about being human. Explore psychological insights, practical wisdom, and fresh perspectives on yourself, others, and life.

OWED BACK: Chat writes these words into DSRD 9 section 39.6 (top line replaced; trust line out of the banner, above) and folds rounds 1 to 7 into section 39 and the front page build sheet.

##### Round 8 (Kain, S177): spacing balanced perfectly; the title on two lines

Kain: "you're use of spacing on this page is not right ... measure this page and tell me what's imbalanced ... I want it balanced perfectly. And I also want the Knowledge Hub spread over 2 lines, because this hero banner deserves to be deeper. Even if this means you place ... some sort of light bulb or something like that, directly after the Achology Knowledge Hub ... show me 4 options."
Measured before (desktop): menu to trail 24, trail to title 64, search to banner foot 64, menu to logo 147, logo to banner foot 104. Built to one measure: 48 (computer and tablet), 32 (phone) for menu to trail, trail to title, search to banner foot, and down the phone stack; the logo equally far from the menu and the Categories bar. Four title endings drawn: none, light bulb, Achology mark, glowing bulb. His pick is added here.

##### Round 9 (Kain, S177): START FROM SCRATCH

Kain rejected round 8 (Code had enlarged the title against the one-size rule and the spacing still read badly): "Start from scratch, Claude ... This is looking absolutely rubbish ... Get another agent to have a look at this design." A fresh design lead wrote a critique, one optical spacing system and four whole directions (side-session notes: DESIGN__KH_Front_Page_From_Scratch_S177). Code built all four: The Faculty Wall, The Lectern, The Horizon (creative), The Sitter. Title back at 33 on two lines; Kain's banner words only. His pick is added here. Rounds 1 to 8 above are superseded by whatever he picks from these.

##### Round 9 pick (Kain, S177): THE LECTERN

"I'd be inclined to go with number two, the lectern ... the rest just feel clunky." Faults, his words: "the Know Your Psychology logo's ... huge. It overpowers the actual name of the Knowledge Hub, which doesn't make any sense." Asked for: "excellent graphic design effort ... four different options on how you can improve this from a spacing, graphic design, and visual perspective ... you can do more with a background of this option as well."

### 39.10 The front page from round 7 to the build on the build site (S177 to S179) (Kain, Code's S177 to S179 theme sittings, 20 and 21 October 2026; written by Chat, S440)

Written home from Code's ruling file RULING__Knowledge_Hub_Front_Page_Direction_S177 and his two ship notes, SHIP__Knowledge_Hub_Front_Page_0.707.421_S178 and SHIP__Knowledge_Hub_Front_Page_0.707.423_S179.

**What this holds and what it does not repeat.** Section 39.9 already holds rounds 1 to 6 and, after them, round 7, Kain's banner words, round 8, round 9 and the round 9 pick (The Lectern). This section carries on from there, in the order of Code's file, which is the order of the rounds: round 11 to the build on the build site at 0.707.424. Code's file has no round 10 and no round 18; none is recorded here. Code's file runs the S179 rounds 19 to 31 before the S178 rounds 32 to 34 because the front page design session stood down at S178 and the theme session carried the page on, so the labels are not in numerical order. Where this section and section 39.3, 39.4 or 39.6 differ, this section is the later ruling and wins, and those sections are left as they stand as the record.

**What the earlier sections now say, in one place.**
- The S378 trust line leaves the banner (round 7, in 39.9). Section 39.3 change 3 ("I know who writes it, so I can trust it") and section 39.4 item 3 therefore no longer describe the banner. Whether the line lives elsewhere on the page was left for Chat to propose to Kain; no file read for this section records that it has been proposed.
- Ruled by Kain in Code's theme session S180, 25 October 2026 (written by Chat, S445): the trust line is off the front page for good, anywhere on it, not only out of the banner. Shown four places lower on the page for it, he said: "I said I wanted it out. Leave it out ... You don't have to ask me if I want it out." His S177 round 7 ruling removed the line from the page as a whole. Nothing was built and nothing on the build site changes. The four option photographs stay in the theme's previews/kh-trust-s180 as the record and are not used. Section 39.3 change 3, the trust line in section 39.4 item 3 and the Trust line in section 39.6 are superseded, and the line is never proposed for this page again. When Kain takes something out, it is out of the page, not moved.
- The banner's words are Kain's own, in the form he last gave them (the "logo spacing is right" entry below). The H1 is "The Achology Knowledge Hub", and the line under it replaces 39.6's top line.
- Block 6 (the three latest rows) is replaced by one mixed wall (39.9 choice 3). The built page, as its ship note lists it, holds the banner and the dark bar, the Mega Panel with Alphabet, the wall and the learning path, so blocks 4 and 5 of 39.4 (the seven subject cards and the topic pills) are not in it, and neither are the subject drawer and the four kind cards of rounds 20 to 30 below. It was built from round 33's pick, the Mega Panel with Alphabet.

#### The banner, from round 11

**Round 11 pick: The Library, with three changes (Kain, S177).** "what I actually really like here option number four ... the library option ... it's simple, it's centralized ... it's good it's clean, it's very, very simple." Three changes, in his words:
1. The Know Your Psychology logo "just feels like it's kind of been dropped in there ... could we somehow build that into the search bar? See how you've got the button at the moment. Could you build Know Your Psychology as a logo into that search bar, so that when it gets hovered over, it presents itself as a button ... maybe you can come up with some options."
2. The background: "while the books are okay, I'm wondering if you might be able to build that kind of background mosaic of faces ... prominent figures such as Freud, Abraham Maslow, faces that people would just typically recognize and associate with psychology."
3. The search prompts: "not just names, but more kind of ... short questions or interesting ideas. Abraham Maslow's hierarchy of needs, Sigmund Freud's psychoanalysis, where can I study psychology online? ... to prompt the visitor to actually engage and use the search. All we need to then make sure is that the mechanism in the background actually serves the searcher."

Code's note for Chat: the prompts are published words. Code uses Kain's three examples and real Knowledge Hub titles (no drafted copy). The final prompt list is Chat's to write with Kain, each prompt proven to return results.

**Round 12 pick: Faces Answer the Search (Kain, S177).** "Yes, Claude, let's go with number four. Faces answer the search. That's brilliant." Two changes:
1. The prompts lead straight to content: "the questions that are being asked in there reflect maybe a part of an article that's already been written somewhere on the site. So that essentially if someone types in what we're prompting them to type in, it takes them right to an article or right to a page."
2. The Know Your Psychology logo stays in the search ("I think that's totally okay"), but not as a raised button: "make it flip round ... with like a search and an arrow or something like that. Please be more creative than what I'm suggesting here ... We don't want a button inside the search bar. We want it to be a real feature."

**Round 13 pick: The Logo Answers (Kain, S177).** "Yeah, go with the logo answers. Claude, that's actually pretty impressive." One change: "expanding the size of the Know Your Psychology logo then, so that it essentially matches the same size as the search button ... equal padding above and beneath and to the right ... the Know Your Psychology to be the same height and depth as the search button, even if that means it's a little bit longer."

**The hero agreed; the page is not signed off (Kain, S177).** "the hero is excellent. Really, really, really nice." One last touch, done: a little more room around the Know Your Psychology logo in the search ("allow a little bit more white space around ... just a tiny little bit"). The page is not signed off: "we will not sign this page off until we've agreed on all other components within the page ... from the browse by subject to then explore by topic to then the actual masonry grid, right the way down. We need this to be a gateway into the entire knowledge hub." The footer and the bottom learning path block are fine. His next question: "we have the main bar, all categories, which are essentially the subjects ... and then we have browse by category, which is the same options ... we're offering the viewer the same thing twice."

**The logo spacing is right; a new banner line; the title as a lockup (Kain, S177).** "that space around the logo is much better, Claude. Totally happy with that." The new line under the title, word for word, which replaces the earlier S177 line: "There's always more to learn about being human. Explore psychological insights, practical wisdom, and fresh perspectives on yourself, others, and life in general." On the title: "turn that into the equivalent of a logo, not necessarily with the achology bubble behind it, but maybe more of a light bulb ... subtly sitting behind it. It just makes it more of a visual something." Four options were drawn.

**Round 14 pick: Bulb in the O (Kain, S177).** "Yes, Claude, that is absolutely phenomenal." Then, his words: "there should be a little bit either more spacing above the Achology Knowledge Hub title or a little bit less space beneath the search bar ... It doesn't seem perfectly centralized ... measure your spacing between the Achology Knowledge Hub and the sentence that comes next, the subtitle. I think it's just a little bit too close ... come back to me once you are clear that the spacing ... is as per our design standards and absolutely immaculate."

**The trail knocks the centred banner out of balance (Kain, S177).** "because we've centralized the text, we're not left aligning. I think there's a conflict here between how you've used spacing within this hero banner and the breadcrumbs ... you've assigned an entire line to that, whereas on this one page, I don't think you need to do that ... having a slightly larger hero banner is great. So I like the space that you have above ... the breadcrumbs line seems to be knocking this out." Code built it with the trail on the centred axis as the group's first, quietest line.

**The trail is never moved; the diagnosis agreed and fixed (Kain, S177).** Kain: "I didn't ask you to move the breadcrumbs ... The breadcrumbs is consistent across the entire site ... Put that back." It was put back. The diagnosis, agreed ("That's the issue that we had"): the spacing above the title was counted from the trail line, so the centred words sat 107 below the band's top edge against 64 above its foot. The fix: the trail stays where it is and no longer counts, and the words are centred on the band itself, depth kept.

**The banner is "absolutely perfect"; two finishing touches done (Kain, S177).** "That's much better. That's absolutely perfect ... I love the design, the layout. This is clean ... really inviting ... phenomenal." Done on his word: more room around the Know Your Psychology logo in the search (8 above and below, 10 to the right edge), and the cream clearing behind the words now fades in softly instead of a hard edge.

#### The two middle blocks, from Browse by Subject to the close of S177

**Browse by Subject, and a consolidation pass (Kain, S177).** The banner's Categories bar and Browse by Subject offer "all categories all over again"; "we're going to need to eventually do some sort of consolidation pass ... multiple different components ... that look different on different pages ... might be worthwhile doing this consolidation pass now as part of this page's design." Code's inventory: every list shares one skeleton; the signed Articles, Workbooks and subject-plus-kind lists also show the seven subjects twice (the banner panel "Browse by Subject" above the same Categories bar); topics appear three ways (doors on lists and subject pages, doors and tiles on All Tags, pills on the front page); the four kinds appear two ways; section heads appear two ways. The agreed approach: the Categories bar stays the one way to jump between subjects; a subject block must tell a newcomer what each subject holds; designed once, it could later replace the duplicate subject panel on the three lists, only on Kain's word, page by page. Kain: "yes, draw the 4 options".

**Round 15 pick: One Subject at a Time (Kain, S177).** "Yes, Claude, like option 3, one subject at a time. Really like that ... very neat." Next, his words: "now just need to look at the actual design of this ... the best design efforts ... Four different directions or four different ways of presenting this. Immaculate spacing, I want this to look like a real journey that we're kind of offering to people. This page is about presenting the extent of what the Knowledge Hub is to any website visitor who lands on it ... the most user-friendly page. User experience here must be of paramount priority."

**Round 16 pick: The Three Steps, concept only (Kain, S177).** "Quite inclined to go with the three steps option ... conceptually, yeah, this is the direction we want to go in. But visually, this looks terrible." He asked for "four different ways of laying this out that's going to make the best use of space". The section heading above it ("Browse by Subject" with its icon tile and line) "looks terrible ... That just can't be there"; "make this look like a creative work of art." Widening it, Kain: "we really need to give some thought to how the sections in this page are going to get broken up. Each section needs to be a kind of a gateway into different aspects of the Knowledge Hub. So this whole page is essentially a door. But it's a door that must present all of the doors within the house ... we just need something more innovative than headings and icons." Next: four whole-page ideas, each with its own section system and its own take on The Three Steps.

**Round 17 pick: The Three Tiers, with one list of subjects (Kain, S177).** "definitely think go with the three tiers." His challenge: "We have a dark bar right underneath the hero banner. It says all categories. Psychology, helping people ... And then directly underneath that, you've gone and built another bar saying browse by subject ... exactly the same thing happening twice ... Your use of font, size, and spacing, isn't good." Agreed ("Yeah, just do it that way"): the block's own strip of seven pictures and its "Browse by Subject" label go; on this page the dark Categories bar does the choosing (a subject picked in the bar opens directly below, with its line, counts and three newest; the bar looks as everywhere else); the subject's name in the block links to its page; and the block is rebuilt on the family's type sizes and measured.

**The close of S177: a fresh session for the two middle blocks (Kain).** "this is not your best design work ... shut the session down ... start up a new one ... leaving the header, the header's fine now, and leaving even right down to the masonry grid. That's perfect ... But the two blocks are literally the categories and explore by topic ... propose the best design you could possibly come up with, but in a new session with a fresh set of eyes." Signed at that point: the banner, the dark Categories bar, the wall and everything below. Open: the subject block (the Three Tiers concept, the dark bar chooses, one list of subjects) and Explore by Topic. The closing fault, in his words: "Have a look at the size of the font and the subtitle of the main banner, and look at the size of the font you've used underneath ... the category name. It's ridiculous. It's completely unbalanced." (The block's line was 21 against the banner's 18.)

#### The subject block, rounds 19 to 31 (Kain, S179)

**The Open Tab; the bar and the subject are one section.** Round 19 set one type scale and showed four ways (The Rail, The Stage, The Index, The Doorway). Kain: "too much white ... not succinct ... I really don't like how you have these titles centralized ... The rail was probably the closest ... But the bar, all categories bar, and the rail, just look like two disconnected components ... I think we need one strip or one section that is just all categories." Round 20 showed the bar and the subject as one section (The Slate Room, The Open Tab, The Window, The Ledger). Kain chose 2: "Yes, Claude, the open tab. The open tab is definitely the right direction ... we can definitely tidy that up." The chosen name opens a cream drawer joined to the dark bar, with a pointer under the name, and the subject's name, line, counts and newest three inside. Round 19's one type scale stands. Next, his words: "look at four different ways of presenting this. And present it as if you want to deliver something exceptionally visually impressive."

**The Shelf.** Round 21 showed four showpiece treatments of The Open Tab (The Spread, The Gallery, The Shelf, The Cover Story). Kain chose 3: "let's go with a shelf Claude ... this is the direction now we need to pay attention to detail. Talk components ... Attention to detail to all the components. Within the shelf option." The drawer under the dark bar held the subject's name, line and counts beside one shelf: the newest article as a framed print, the newest book note as a standing book, the newest quote article as a card, with their labels and titles beneath.

**Oak; the subject block is chosen.** Round 22 finished every component of The Shelf in four finishes (Oak, Gallery White, Library Brass, Evening Lamp). Kain: "Go with Oak." The subject block was The Open Tab drawer under the dark bar, holding The Shelf in Oak (oak shelf with grained front edge, walnut frame with mat and glass, standing book with its spine, leaning quote card with its orange tab, labels centred beneath, objects set down in turn when a subject is chosen). Preview: theme previews/kh-front-s177, opt1.html (commit 153c4ca1).

**The subject block's composition is agreed.** Kain: "it is not design excellence ... We do not move on until we are both agreed ... One block, one title, one paragraph, one segment at a time." Code loaded the design skills, read the build sheet and section 39, studied references, measured the block and recomposed it as one grid (round 23, commit 22e17200): the subject's name and the tops of the framed print, the book and the quote card on one line; the three objects one height on the oak shelf (the tallest one's, at least 200 on a computer); the counts ending level with the shelf; the three labels sharing one line under it; and the shelf inside the page's edges. Kain: "Yes, the composition is right. Move on to the subject's name and line."

**Spine for the name and line; the bar and the drawer must evidently be one.** Round 24 showed four treatments of the subject's name and line (Quiet, Spine, Shelf Label, Emblem), each with balanced line breaks and a tablet reading width. Kain chose Spine, an orange rule binding the subject's name and its line: "I like the spine option ... there needs to be greater synchronicity between the tab that all categories bar and this tab. The two need to evidently be one. And we're not quite there yet ... the spine is definitely the direction we want to go in. But it's not quite right just yet."

**The whole front page assembled (Code's call, on Kain's order to drive it).** Round 25 drew four joins of the dark bar and the drawer (Folder Tab, Matching Line, The Thread, Folder Tab with Crown). A relay from the kh-gate-cleanup session carried Kain's principle: assemble the front door from signed blocks, invent nothing new (its seven subject tiles were dropped, because the S177 rule stands and the bar is the only chooser). Kain then told Code to stop asking and drive. Code's calls, for Kain to sign or overturn on the whole page: the join is the Folder Tab with Crown; the drawer keeps the composed Oak shelf with Spine; Explore by Topic is no longer a front page design but the signed topics band taken whole from the lists ("Explore the Achology Knowledge Hub by Topic", four families); and the order below the drawer is the signed lists' order: the kinds row and the wall, the topics band, the learning path, the footer. The whole page's spacing was checked at 1280, 834 and 390 (48 at every boundary, 32 on a phone, the learning path gap matched to the lists). Preview commit 523ef013.

**The tab goes, the arrow returns; the drawn shelf goes.** Kain on the assembled page: "the tab going into the all categories bar ... looks absolutely terrible ... The previous option ... with a little arrow pointing into the page was much better"; "the shelf is just meh ... The quote looks terrible. The book doesn't even look like an actual book ... we've gone from maximum effort to minimum." Done (round 27): the small dark arrow under the chosen name is back; the Spine stays; the drawer holds the subject's name and line, its counts level with the line's foot, and its three newest as the signed wall cards with their own designed images (the article's banner, the book cover on its band, the designed quote card), on the wall's three columns, with one picture shape, one label line and one card height. The wall below never repeats a drawer piece.

**The opening block made instructional, four kinds.** Kain on round 27: "a lot cleaner ... really, really good ... make this opening block more instructional ... someone landing on this page for the first time ever, is not going to necessarily know that we have four unique different types of content ... these three cards need to kind of be matched ... there will also ultimately be workbooks." Code proposed and Kain said yes: four matched cards, one per kind (Articles, Book Notes, Quote Articles, Workbooks). Each held the newest of that kind in the chosen subject as its own designed picture; the kind's name and its count in this subject, linking to that subject's list of the kind; the kind's own line, word for word from its signed list page; and the newest title on one shared foot line. For Workbooks (none published) the card was the signed All Tags tile panel with the Workbooks icon, the workbook list's line, and the learning path's own link "Explore All Workbooks". The separate counts row went. Built as round 28. Kain: "Yes, the four-card block is right." (S179, on round 28, commit 63fe4be5.) The Articles card's line was the Articles list's own ("All of Achology's reads are centralised on this one hub page ..."), which describes that list page, not the kind, so a line defining an Article was owed, in Kain's words or Chat's.

**Four simple buttons and the topic quilt.** Kain then reversed the four-card block: "it's not quite right yet ... we need this block to actually educate the website visitor that there is four ways that they can study and learn psychology just through the Achology Knowledge Hub ... they all look so completely different ... all the doors look the same, but also uniquely different"; and "the topic quilt ... and also, the four buttons beside it ... four simple buttons ... one standardized design that applies to all seven categories ... propose some ways". Round 29 showed four options: the drawer opens on the All Tags page's own four kind buttons, each linking to the chosen subject's list of that kind (1 Beside, 2 Row, 3 With Example, 4 Tabs), with the All Tags topic quilt replacing the topics band.

**The mechanism: the bar picks the subject, the strip picks the kind, the wall answers both.** Kain, in place of round 29's options: "All we need ... is the black strip with the category titles ... we just simply use masonry grid ... all categories ... pulls through a masonry grid of all different types of content from all categories ... as they tab their way through ... the motivation tab ... explains that there are four different channels ... articles, book notes, quotes, workbooks ... more of like a menu item ... how the masonry grid kind of flips around ... we're losing the subtitle just above the masonry grid." Built as round 30: the dark bar's All Categories label and the seven subjects are the subject choice (the small arrow under the choice); the strip under the bar shows, for a subject, its name and line with the Spine, and for every choice the subject walls' own signed filter buttons (All, Articles, Book Notes, Quote Articles, Workbooks) with that choice's counts; the one masonry wall below flips in place, laid out by the signed wall script, 24 pieces at a time in each subject's own order. When a choice has nothing (Workbooks today), the workbook list's own line and "Explore All Workbooks" stand in for the wall. The kinds row above the wall was gone, and the topic quilt and the learning path followed. All 40 subject and kind states were tested at 1280, 834 and 390.

**Define the problem; research; four concepts.** Kain on round 30: "There's no instruction here whatsoever ... We need an infrastructure ... You haven't defined the problem." Code defined it with Kain: a newcomer meets a library of 806 pieces arranged three ways at once (7 subjects, 4 kinds, 36 topics), and the page shows the controls but never the system. Four tests: the arrangement is understood in five seconds; book notes on mental wellness take two clicks; there is one designed object at the banner's quality; and one standard serves every subject, kind and phone. With the front page research session (its page: theme previews kh-front-research-s178, commit 0674166d; Chat's note NOTE__Knowledge_Hub_Front_Page_Research_S178) the model was agreed: say the library's shape once; name the ways in (Greater Good, Psyche); open a subject as one labelled row per kind, empty kinds left out (Psyche); always say where the visitor is (Public Domain Review); every door shows it is full. Seventeen of the 28 subject and kind pairs are empty or thin. Kain: "I really like the hero banner ... we need to think about everything that comes underneath it ... let's get the concept first." Round 31 showed four concept mock-ups under the signed banner: 1 The Directory, 2 Rooms (the research session's recommendation), 3 Three Doors (creative), 4 Shelves. The words were the site's own, and the line naming the system was owed by Kain or Chat.

#### The Mega Panel and the wall, rounds 32 to 34 (Kain, S178)

**The research, then ten angles, then ten more between the A to Z and the Mega Panel.** Research came first (theme previews, kh-front-research-s178: index.html and FINDINGS.md; Chat's note NOTE__Knowledge_Hub_Front_Page_Research_S178). Then Kain asked for ten angles, in his words: "ease of navigation. And premium user experience ... easy ... transparent ... I don't think people need to see numbers, people need simple instructions ... this door needs to be a door, It needs to show people how to navigate their way through this knowledge hub ... I like aspects of the directory. However, it's just columns ... all different depths ... it needs to be contained. The whole thing needs to be within a unit ... synchronicity, order, structure, standards, minimum use of white space, really using the page well." Round 32 (angles.html, a1 to a10) showed The Console, Three Ways In, The Sentence, The Lobby Board, Four Corners, The Route Map, The A to Z, The Bento, The Mega Panel and The Depth Ladder. Kain on round 32: "I am absolutely torn between 7 the A to Z and 9. Which is the mega panel ... we only have 4 types of article ... I would love to see an additional 10 options ranging between the A to Z which is option 7 and 9 the mega panel ... presents all of the topics within the Knowledge Hub as kind of just a navigatable menu. Navigation, map, those are the words that spring into mind." His idea for the search page, passed to the search session (section 38.7): an A to Z page of every theme the library writes about (beyond the 36 topics, for example productivity and temperament), with the front page block carrying "an option in the bottom corner to view all topics and themes". Round 33 (angles2.html, b1 to b10, from nearest the A to Z to nearest the Mega Panel) showed Colour Coded A to Z, The Letter Rail, Doors and Index, The Contents Page, The Switchboard, Index Cards, The Atlas, Two Level Menu, Alphabetical Mega Panel (a level grid: four columns of eight rows each, kinds on top, reading styles along the foot, courses closing it) and Mega Panel with Alphabet. The instruction words were stand-ins. Code stood the front page design session down at S178; the theme session carried the page, design and build, on Kain's decision.

**Round 33 pick: 10, The Mega Panel with Alphabet (Kain, S178).** "I'm really drawing towards number 10, the mega panel with Alphabet ... I think there's probably a little bit of work to be done in it. To make it kind of really visually spectacular. But I think this is our option." On the wall beneath it, his words: "Underneath that, I think we have the opportunity to really present this the masonry. The masonry grid. I think we just need to think through a really balanced and ruled way of doing this. So that no two articles touch, no two book notes touch, things like that. We've managed this in some of the other pages." Round 34 (S178, preview front.html in kh-front-research-s178) built the Mega Panel with Alphabet on the page's type scale: a letter in the alphabet lights the topics that begin with it, and the kinds show their icon and name only (the cut-off kind lines removed). The wall beneath held articles, book notes and quote articles in equal shares and was laid so that no two cards of one kind touch (zero touching at 1440, 1280, tablet and phone; one or two pairs remained at 1024 to 1100). It waited on Kain's eye.

**The wall follows the subject pages' signed rules; never reinvent them (Kain, S178).** Kain on round 34's wall: "what you seem to be doing here is trying to recreate a set of rules that we've already created ... the category pages have got this masonry grid right, genuinely really right ... We need to start capturing these rules ... I cannot afford to waste or lose an hour and a half explaining to you to do something that I've already explained to you to do." Done: round 34's invented rules (equal thirds, and a new layout script) are removed. The front page wall follows section 20.0c, "The grid", items 1 to 9, across the whole Hub: 48 cards; book notes (the kind the Hub holds fewer of) at least one in every row of four, spread evenly in the fixed rotation; at most one quote a row; no author more than two quotes, the authors taking turns; laid out by the theme's own `kh-subject.js`, unchanged. Measured beside the Psychology page on the build site, it has the same make-up (31 articles, 13 book notes and 4 quotes against 33, 11 and 4) and the same quote authors in turn. Code asked that section 39 say its wall is the section 20.0c wall, so that no session rebuilds it from scratch again; this section says so at its end. Two facts for Kain, not changed: the signed front page wall is three columns on a computer and the subject pages four (rule 7 of 20.0c); and on the signed walls articles do touch articles (the Hub holds more than twice as many articles as book notes), so "no two articles touch" would need a new ruling on rule 1 of 20.0c.

#### Finishing the page, and the build (Kain, S178 and S179)

**Finish the front page: spacing and type, dead code, then bells and whistles (Kain, S178).** "we need this home page to essentially be a gateway into all other pages ... evaluate spacing ... visually spectacular ... inspect spacing to ensure that the full page meets our spacing and text standards. Font standards. And then do a secondary run to clear out all dead code ... And then look at bells and whistles ... what I mean is making things pop and sparkle and shine and just go above and beyond what placing images in text on a screen does ... making every component of the page we're looking at visually and interactively spectacular." Pass 1 was done: 48 at every block boundary on computer and tablet and 32 on a phone; the panel heading 24 on a phone (it was 21); the tablet heading no longer leaves one word alone; the phone kinds two by two and the course strip stacked; every other size outside the scale belongs to the signed learning path. Pass 2 was done: the page's own stylesheet holds only the rules it uses (about a tenth of the round sheets), proved identical element by element at 1280, 834 and 390, at rest and with a letter pressed. Pass 3 offered ten touches for Kain to choose from (player: kh-front-research-s178/touches.html): 1 the panel unfolds; 2 topic rows answer the pointer; 3 the alphabet previews as you point; 4 the kinds show three real pictures; 5 the hint points the way; 6 the wall arrives card by card; 7 wall cards lift and glow; 8 the course strip catches the light; 9 Back to the map; 10 every door answers a press.

**Build it on the real site (Kain, S178; shipped 0.707.421).** Kain: "Why don't you just build this page in the actual website? So we can from here just make live edits ... We're so close to the direction now ... It's really, really good." Code built and deployed it as 0.707.421. The theme files: `learn-home.php` rewritten; new `kh-front-setup.php`, `kh-front.css` and `kh-front.js`; one require in `functions.php`; and `achology_kh_subject_posts` and `achology_kh_subject_quotes` in `knowledge-hub-parts.php` now accept no subject, for the whole Hub, with the subject pages unchanged. What the page holds, top to bottom:
1. The banner and the dark bar exactly as signed at S177.
2. The Mega Panel with Alphabet (round 33's pick 10, round 34): four columns of eight rows; the alphabet lights its topics; topics with fewer than ten pieces are not shown as doors (DSRD 1 section 5.1's floor).
3. The wall: the subject pages' wall by section 20.0c across the whole Hub (48 cards: 31 articles, 13 book notes, 4 quotes, authors in turn), laid by `kh-subject.js` unchanged, and saved and cleared with the subject walls.
4. The learning path as on the all-subjects lists (Psychology's course).

Checked on the build site at 1280, 834 and 390: gaps of 48, 48 and 48 (32 on a phone), 27 doors, 17 letters, no broken picture, no sideways scroll and no script error. Built in a worktree, merged fast-forward, deployed and pushed; local, server and zip agree. Owed at that ship: the page's Rank Math title and description (Chat, with Kain), since it still showed the site's default title; the ten bells-and-whistles touches, chosen by Kain on this page next; the stylesheet's short preview class names (`z`, `z9`, `zf`) to be renamed in the tidy; and the policies, help and people stylesheets the page loads but does not use.

**Standards first, then one touch at a time (Kain, S178).** Kain on the built page (0.707.421): "rather than taking all 10, we could just do one at a time. So you propose what you're about to do, and then we do it ... first do a full evaluation of your use of spacing ... I'm just seeing spacing imbalance right down the page ... It's like a lot of information, knowledge, words just dumped on the page. The infrastructure's neat, the design is good ... there's evidently no integration of hairlines ... This is the minimum standard for every page ... there's no heading above the articles. The masonry grid." Code's scan, measured against the Psychology page, found no hairline at any block boundary (DSRD 7 section 4.3 requires one, 48 above and below, 32 on a phone); the panel's heading was not the standard section header and the wall had none (DSRD 8 section 23 and 23.4: icon box, title, supporting line); and the panel used about nine text treatments, six coloured capital labels and two oranges, every word at weight 600.

**The standards pass goes in; the headings' words wait for his look (Kain, S179; shipped 0.707.424).** Code proposed the standard section header on the panel ("Find Your Way Around the Achology Knowledge Hub" / "Choose a kind of reading, or follow a topic. Every topic runs across all seven subjects.") and on the wall ("The Newest in the Achology Knowledge Hub" / "Articles, book notes and quote articles, newest first, from every subject."), with a hairline at both block boundaries (panel and wall, wall and learning path; 48 above and below, 32 on a phone). Kain: "why don't you just put your proposals in, and then once they're in, what I would rather do is judge the view the look and feel of the page first, and then we can get down to me proposing edited titles and subtitles." So the proposed words go in as placeholders; the look is judged first; the final titles and supporting lines are Kain's own, written after. Built and deployed as 0.707.424. The ship note was filed under 0.707.423, the version first planned, and shipped as 0.707.424 because the search page session holds 0.707.423 uncommitted on the main folder. What changed (`learn-home.php`, `kh-front-setup.php`, `kh-front.css`, `style.css`):
1. The standard section header (DSRD 8 section 23 and 23.4: orange icon box spanning the title and its supporting line, Achology in orange) opens the panel and the wall. The panel's own heading strip is gone, and its "Or pick a subject in the bar above" hint moved into the new header (under the title on a tablet and a phone).
2. A hairline at both block boundaries, panel and wall, and wall and learning path (DSRD 7 section 4.3), with unruled headers so there is no second line.
3. `kh-front.css` passes the CSS gate: values already on the scale became their tokens (nothing moves), and every other flagged value is noted as built at 0.707.421, for the type stage and the tidy.

Measured on the build site at 0.707.424: 48 at every boundary on computer and tablet and 32 on a phone; headers 32 above their block; icon boxes 54.4 square (36 on a phone); no broken picture and no sideways scroll. Local, server and zip agree. Kain on the real page: "Yes, they do. But ... you tell me if they are right." Code checked the headers against DSRD 7 section 4.3 and DSRD 8 section 23 on the page and found them right; one item not in the standard, the rounded "Or pick a subject in the bar above" button in the header's end slot, goes to the type stage. Kain: "Yes, please do" to stage 2, the panel's text styles.

**The panel's text styles, option 1, One grey label (Kain, S179).** Code measured fourteen text treatments in the panel (six capital labels in six colours, three oranges, every word at weight 600) and showed four options on the real page (theme previews/kh-front-type-s179): 1 One grey label, 2 No labels, 3 Colour kept quieter, 4 The index. He recommended 1. Kain: "yes". Built: every small capital label in one soft grey; topic names at regular weight so the column headings lead; every link on white in the one link orange at 14; the A to Z letters at 500; and the header hint a plain orange link (the standard header's end slot). The column colours stay in each column's top stripe and its icon discs.

**Shipped (Code, S179; written by Chat, S440).** The option 1 text styles shipped on the build site as theme 0.707.431 (SHIP__Knowledge_Hub_Front_Page_Panel_Type_0.707.431_S179): every small capital label in one soft grey, topic names at regular weight, every link on white in the one link orange at 14, the A to Z letters at 500, the header hint as a plain orange link in the standard header's end slot. Text only, no row, column or gap moved; measured at 0.707.431 with gaps unchanged at 48 and no sideways scroll.

**Touch 2, Spotlight, shipped 0.707.432 (Kain, Code's S179 sitting; written by Chat, S440).** Kain picked version 4 of four shown on the real page (theme previews/kh-front-touch2-s179): "That spotlight is lovely. Very, very good work ... let's build spotlight into the real page." On a pointer, a panel row lights with a soft wash of its column colour, its icon fills with the colour and grows a touch, its name turns orange, an arrow glides in, and the rest of that column dims to about 55 per cent; pointer devices only, instant under reduced motion, never while a letter in the A to Z is lit, nothing moving at rest. Checked on the build site at 0.707.432; css_gate passed.

**Touch 6, Rise in turn, and the ruling that a card touch belongs to the shared card (Kain, Code's S179 sitting; written by Chat, S440).** Kain picked Rise in turn for the wall and ruled that a touch applied to a card is baked into the shared card and plays on every Knowledge Hub wall, not on this page alone: "we potentially componentify each individual card and how this works. So if we apply rise and turn, then the rise and turn gets applied to all cards across all pages that carry cards. Within the knowledge hub." At 0.707.434 Rise in turn is built into the shared wall script (kh-subject.js section 5) and plays on any wall whose list carries data-arrive; only the front page carries it until the sweep brief Kain signs takes it to every wall. The rule's home is DSRD 8 section 41, the Knowledge Hub rulebook entry.

**The top band drift, shipped 0.707.437 (Kain, ruled in the page family session and passed on to Code's S179 theme sitting, 22 October 2026; written by Chat, S441).** The banner's Library mosaic now drifts behind the banner at 0.3 of the scroll, the same slow drift Kain ruled for the workbook page's band shelf (section 37.8, touch 8), shown to him before and after at theme previews/kh-front-drift-s179. The wall's cards arrive by Rise in turn, now on every Knowledge Hub wall (DSRD 8 section 41, shipped 0.707.439).

**Where the page stands (written S440).**
- The page is built on the build site at theme 0.707.424.
- Its wall is the section 20.0c wall, "The grid", items 1 to 9, across the whole Hub, laid by the theme's own `kh-subject.js`. No session rebuilds it or invents rules for it; a change to the wall is a change to section 20.0c.
- The two section headers' words (the panel's and the wall's) are placeholders until Kain writes his own, after he has judged the look and feel of the page.
- The page is not yet signed off. Kain's position from S177 stands: "we will not sign this page off until we've agreed on all other components within the page". The files read record no sign-off since, and the ten bells-and-whistles touches, taken one at a time, are still to come.
- The page's search title and description (Kain's "yes" to Code's draft, Code's S179 theme sitting, 22 October 2026; shipped 0.707.491; written by Chat, S442): title "Knowledge Hub: Psychology Articles and Book Notes | Achology", description "Free psychology articles, book notes, quote articles and workbooks across seven subjects, to help you understand yourself, other people and life." Set through Rank Math filters, since the route has no post. Still owed by Chat: a line defining an Article.
- **The wall at 4, 3 and 2 columns, shipped 0.707.490 (Code's S179 theme sitting, 22 October 2026; written by Chat, S442).** The front page took the one wall's columns (section 20.0h rule 1) ahead of the sweep, its own 3, 2, 1 overrides removed; measured 48 cards, every column level. The topic pages still run 3, 2, 1 until the one-wall sweep.
- Recorded as Chat's from round 11 and not closed in any file read for this section: the final list of the search prompts, each proven to return results.
- **The front page changes under the one wall (Kain, Code's S179 theme sitting, 22 October 2026; written by Chat, S442).** Its wall moves to 4, 3 and 2 columns and gains the Know Your Psychology logo card (section 20.0h), through the one wall sweep brief.
- **The front page tidy, shipped 0.707.482 (Kain: "yeah, I'd like you to do the front page tidy up", Code's S179 theme sitting, 22 October 2026; written by Chat, S442).** Code removed every front page style rule that matched nothing, renamed the panel's working names into one family (kfm), and removed the old front page's subject cards and category pill strip and their rules; the .kh-pill and .kh-search rules stay because other pages use them. Measured before and after at 1280, 834 and 390: no element outside the wall moved or changed. Not done: the page still loads the policies, help and people stylesheets through the site-wide chain, which is a Backlog: Code line, not a front page change.
- **The final checks, shipped 0.707.493 to 0.707.497 (Kain, Code's S179 theme sitting, 22 October 2026; written by Chat, S445).** Kain said yes to fixing the real faults and recording his six design exceptions (DSRD 7 section 4.3, Exception 14). page_gate on /learn/ went from 36 fails at 0.707.491 to 5 at 0.707.497, none of them the page's own. Fixed: the wall's last cards sat only 24 above the hairline after the move to 4, 3 and 2, and now sit 48 (32 on a phone); the map panel's own bottom edge, read as a second line, is removed; the banner's 33 faces have width, height, smaller copies and early loading for the first row; and the search button logo has its 320 copy. Nothing else moved. Left, with owners: the wall header's supporting line is 11 words until Kain writes his own heading words; the title reads 70 on the build site only, because its name is "Achology TEST Site" (59 live); 182 old workbook redirect rows point at /learn/ with an unfinished chain (factory, on Backlog: Code); and the orphan crawl missed 913 pages, though the page is linked from the header on every page. The DSRD 6 record is filed in the Knowledge Hub Homepage design folder. The one wall changes named two bullets above landed at 0.707.498 (section 20.0h).

### 39.11 The ten touches: Kain's seven picks (Kain, Code's S180 front page sitting, 26 October 2026; written by Chat, S446)

Asked "Shall I build touches 1, 2, 5, 7, 8, 9 and 10 into the page?" with all ten playing on the real page, Kain answered: "Yes. Build touches 1, 2, 5, 7, 8, 9 and 10 into the front page." Built in kh-front.css and kh-front.js only (commit eb50a272), shipped at theme 0.707.529.

1. **The Bulb Lights Up.** The bulb in the o of Knowledge glows as the page opens, and brighter while someone is in the search.
2. **Torchlight on the Faces.** Under a pointer, the faces near it come up out of the fade and warm a little.
5. **The Icons Draw Themselves.** Each section heading's round icon draws its lines as it comes into view.
7. **The Colour Stripes Fill In.** The panel's four colour stripes run across from the left, one after another.
8. **The Alphabet Ripples.** The A to Z letters rise in a wave as the strip comes into view; a letter lifts under the pointer.
9. **The Lines Draw Outward.** Each hairline draws out from the middle as it comes into view.
10. **A Shine Across the Foot.** A soft light crosses the panel's dark foot as it comes into view, and its link's arrow nudges on.

Not taken: 3 The Banner Arrives, 4 The Search Lights Up, 6 The Columns Rise. All seven stand still for a reader who asks for less motion, and nothing is hidden if the script does not run. At rest the page is the page of 0.707.527 at 1280, 834 and 390.

**Fixed in the same sitting (0.707.527):** the wall's cards end 48 above the line to the learning path (32 on a phone), as Kain saw the page before the one wall; the A to Z strip, its letter gap and the see-all rows put on DSRD 7 section 4's scale; Faces Answer the Search (round 12, signed) restored after the S178 prune lost its one style.

**Reach (DSRD 8 section 41):** touches 9 and 5 would fit every Knowledge Hub page that uses the standard section header and hairlines. They are built on the front page's own classes only; a sweep to the shared parts is proposed separately and is not ruled.

**The gate's reading of the wall's last boundary (Chat's call, S446).** page_gate reads the wall to the learning path as 24 above the line (8 on a phone) because the wall's box carries its last row's gap and the pull-back is a negative margin; the cards themselves end 48 above it (32 on a phone), measured in WebKit. This is the instrument's error, not a design exception: the gate is changed to measure to the wall's last card, and no exception is recorded.

**Still not signed off.** The prototype and build sheet are written into the design folder when Kain signs the page off.

**39.12 The learning block is Pick Where You Are, in Kain's words (Kain, Code's S180 front page sitting, 26 October 2026; live at 0.707.545; written by Chat, S446).** Kain: "I don't like the CTA, take your learning further. Especially in this homepage, because they haven't even necessarily started learning yet." Of four designs on the real page he chose the first: "I'm drawn towards 1. Pick where you are ... don't ask chat for this. I'm going to do this." The four cards and their words are the component Pick Where You Are Cards, DSRD 8 section 42. The block's heading and line are Code's, seen and kept by Kain: "Where Would You Like to Begin?" and "Read for free, practise with a free workbook, or study a full course. Start wherever suits you, and go further whenever you're ready." This overtakes Chat's RULING__Front_Page_Learning_Block_Words_Final_S446 for the cards; its diploma fact is kept. The block is the front page's own; every other Hub page keeps the shared learning path. The banner, the panel and the cards are logged components (DSRD 8 section 42).

**39.13 The front page is signed off (Kain, Code's S180 front page sitting, 26 October 2026, at theme 0.707.547).** "Yes, I'm really happy with the look of it, Claude, to be honest. Really happy with it. I think it just looks fantastic." The page as he signed it is the last section of BUILD_SHEET__Knowledge_Hub_Front_Page_S390.md and the prototype achology-knowledge-hub-front-page-proof-v1.html in the Knowledge Hub Homepage folder, which win over this section. His one point, that the wall's cards arrive slowly, is the shared wall's Rise in turn (a card held until well up the screen, then a 0.6 second fade); the fix changes every Hub wall and is the main theme session's to build and show him. Still his to write: the panel's and the wall's section header words.

**39.14 The review block becomes a signpost to the reviews page, in a dark band (Kain, Code's S183 theme main session, 26 October 2026; written by Chat, S446).** Kain: the old block's text "doesn't look good", and "it needs to connect through to the reviews page making it an arrow or a direction, kind of like a signpost". Of four presentations he chose the Dark Band: "I actually think the dark band is our smartest option. Let's go with dark band." The copy he approved: the label WHAT OUR STUDENTS SAY; five stars; Daniel Carter's five-star review of 7 August 2024, word for word, "If you apply yourself properly to this course it is going to change your life. It is incredibly in depth and I am going to pursue these topics further at Achology."; Daniel C.; Verified student, Diploma Course in Modern Applied Psychology (DiMAP); the site's figures, 4.66 average rating from 4,516 verified reviews, read from achology_figures(); Read All Student Reviews, the whole block one link to /reviews/. Kain then asked to improve the whole bottom section, from the learning block through the dark band; its final form is added here when he picks. Built behind preview switches at 0.707.562 to 0.707.565; the old block stays live until his pick ships.

**39.15 The bottom section is the Staircase on Soft Dawn (Kain, Code's S183 and S184 theme main sessions, 26 October 2026; on the build site at 0.707.585; written by Chat, S447).** Of four bolder versions built on the climb his cards already draw he chose the third: "I choose three staircase. That's looking really, really good." Of four skies behind it, after asking for the sky to cover the whole block at every width and for the review band's square corner to be rounded, he chose the second: "Yes, Soft Dawn." **The Staircase:** at four across, the four Pick Where You Are cards rise 72, 48, 24 and 0 from left to right; the Dark Band of 39.14 stands 48 below them, its top edge sloping with the stair, carrying the approved review, the figures with "out of 5" added, and Read All Student Reviews, the whole band one link to /reviews/. Below four across the cards stack and the band stands under them. The old Kylei R. block is gone. **Soft Dawn:** a dawn sky running the full width of the browser window at every width, from just under the line above the section to the coloured line below it, rising out of the white page and fading back into it; a soft sun with faint rays behind the diploma card (behind the fourth card on a phone), which catches its light; the review band's four corners all rounded. Declined, so nothing is shown twice: Breathing Room, One Journey, Inset Caption, The Summit, Panorama, Summit Log, Night at the Summit; Sunrise, Paper Mountains, Trail Map, Night Climb; Edge to Edge, Golden Floor, Rising Sun. The prototype in the Pick Where You Are Cards design folder and its build sheet were re-exported at 0.707.585 and win over this line.

**The sky is the Straight Merge (Kain, Code's S184 theme main session, 26 October 2026; on the build site at 0.707.589; written by Chat, S447).** Kain: "the background orange is now competing with the text underneath the 'Where would you like to begin?' title." Of four quieter skies he asked for a merge of two, "can you somehow merge clear header and paler dawn?", and of four merges chose the first: "I'm going to say yes to the straight merge." The header and its line stand on plain white; the dawn rises from the cards down over 120 and settles back into white before the coloured line; the sky, the sun's glow and the rays at about half their Soft Dawn strength. Declined: Clear Header, Paler Dawn, Lower Sun, Morning Haze; Gentle Rise, Paler Still, Warm Summit. Overtaken by Step 3 below.

**The review band is The Gauge (Kain, Code's S184 theme main session, 26 October 2026; on the build site at 0.707.596; written by Chat, S447).** Kain found the band unbalanced, "so much in it" on the left and "so little" on the right, and ruled that the five stars must go because they contradict the true rating of 4.66 out of 5, that the figures show 4.66, that Average Rating takes capitals and that the course name links to the course page; he said yes to the band no longer being one whole link, since a link cannot sit inside a link. Of four arrangements he chose the fourth: "Option 4 please Claude". The review side keeps WHAT OUR STUDENTS SAY, Daniel C.'s words and his name, the five stars gone, and under his name "Verified student, Diploma Course in Modern Applied Psychology (DiMAP)", the course name a link to the course page. The figures side is a wider, lighter page (the band split three fifths and two fifths): a half dial sweeping to 4.66 of 5 with 4.66 and OUT OF 5 inside it, five drawn stars beneath it each filled by its own share, then Average Rating, the review count, and Read All Student Reviews as the link to /reviews/. Held empty until the band is in view, the dial and stars fill to 4.66 once; with reduced motion or without the script they simply show 4.66. The band no longer lifts on hover. This overtakes 39.15's "the whole band one link to /reviews/". Declined: Rating Seal, Star Meter, More Proof, Two Pages; Stars Inside, Stars Beneath, Stars Around.

**The sky is Step 3, and the page is signed off again (Kain, Code's S184 theme main session, 26 October 2026; on the build site at 0.707.605; written by Chat, S447).** Asked for a sharper sky, Code named five faults through a designer's eye and proposed a pale, nearly flat dawn; Kain: "build 8 on a spectrum from subtle to less subtle please", then "Step 3 please", and in the same message, "Lets lock this full page in now shall we!" The sky runs the full window width from just under the line above the section to the coloured line below it; the header on white; a pale dawn below it; one thin horizon line, orange at 0.18, at the foot of the card pictures; one pale sun, a clean-edged half circle 210 in radius, risen on the line behind the diploma card; no rays and no glow on the diploma card, so the dial leads. This overtakes the Straight Merge above. At sign-off the page gate read 35 passed and 11 failed, the same eleven as at the S180 sign-off, and axe found no WCAG 2.2 AA violation, after two faults of the new band were fixed at 0.707.605 (the drawn stars hidden from screen readers; Read All Student Reviews a step lighter, #F8B27A, for AA contrast). One gate line, the review's padding-top 120 on a computer (48 on the scale plus the Staircase's 72 step, so the words clear the band's sloping top), is the signed Staircase itself and is written in the page's DSRD6 record; Kain's "As it looks, i love it - please dont make any more changes" is read as his yes (Chat, S447), and it is DSRD 7 section 4.3, Exception 17. The prototype in the Knowledge Hub Homepage folder and the Pick Where You Are Cards prototype were re-exported at 0.707.605 and win over this line.

**The review band's finish is Soft Rings (Kain, Code's S184 theme main session, 27 October 2026; on the build site at 0.707.608; written by Chat, S447).** Kain approved the band in concept and asked for finishing touches: the stars to shine through when they reach 4.66, the half circle to pulse very slightly, capitals on Verified Reviews, Read All Student Reviews in line with the course line, and a very subtle background on the right-hand page. Of four he chose the first: "Yes, Soft Rings." The count reads "from 4,516 Verified Reviews" (his copy, 0.707.607). On a computer and a tablet Read All Student Reviews sits on the line of the Verified student caption, with the dial, the stars, Average Rating and the count centred in the space above. Once the stars fill to 4.66 they shine gold (#FFC857 with a soft gold glow) one after another, 0.18s apart, and settle back to orange; the dial then pulses very gently (a soft orange glow coming and going over 3.2s); faint white rings, 28 apart, spread from the dial across the right-hand page. With reduced motion nothing moves. Declined: Warm Glow, Fine Grain, Starfield.

**The sky is gone: the section stands on plain white (Kain, Code's S190 theme side session, 27 October 2026; on the build site at 0.707.653; written by Chat, S449).** The sun was first pinned to the diploma card at 0.707.652, so it no longer slid off at narrow windows. In Safari Kain still saw it cut off, with the horizon line running through the cards: "You've cut off the sun completely ... It just looks a mess." Offered the sun and line removed with the wash kept, he said: "No, remove the whole sky background, plain white." The Pick Where You Are block on the Knowledge Hub front page, the seven subject pages and the 32 list pages has no dawn wash, no horizon line and no sun. The Staircase cards and The Gauge review band are unchanged. This overtakes Step 3 and Soft Dawn above. The re-export of the Pick Where You Are Cards prototype and build sheet, and of the Knowledge Hub Homepage prototype, without the sky is owed by the theme main session.

**Pick Where You Are closes every Knowledge Hub subject and list page (Kain, Code's S189 Safari afternoon, 27 October 2026; on the build site at 0.707.640; written by Chat, S449).** Kain wanted the signed block exactly as signed: "I didn't need to see the blocks ... I just wanted this exactly as I signed it." It now closes the seven subject pages and every list page, as well as the front page.

**The rings ripple, Gentle Ripple (Kain, Code's S184 theme main session, 27 October 2026; on the build site at 0.707.612; written by Chat, S447).** Kain: "it'd be great if these ripples could just somehow be rippling ... even just subtly". Of four, gentlest first, he chose the second: "Yes, Gentle Ripple." The rings (white at 0.04, 28 apart, centred on the dial) drift outward continuously, one ring's width every 9 seconds; with reduced motion they stay still. Declined: Slow Drift, Steady Ripple, One Wave. Earlier in the same sitting Kain said of the page as it stood: "As it looks, i love it - please dont make any more changes". The ripple is the one change he then asked for himself, and the front page is finished.

**The learning block on a tablet takes Wide Rows (Kain, Code's S194 and S203 theme sittings, 1 November 2026; on the build site at 0.707.680; written by Chat, S452).** Kain saw the block, "Where Would You Like to Begin?" (39.12), break between 768 and 1199 in his own screenshots. Of four rendered options shown at 950 wide (Shorter Pictures, Stepped Pairs, Code's recommendation, Sideways Strip and Wide Rows) he chose the fourth: "i would like 4 Wide rows please". Between 768 and 1199.98 wide the cards stand one to a row, each with the whole 145/100 picture 290 wide beside the words, in `kh-front.css`. This sets the tablet behaviour of the Staircase (39.15): the computer's four across with the climb, and the phone's rows, are unchanged. Read on the build site at 950 wide: four cards 886 wide, each picture 290 wide; measured at 780, 950 and 1150, and unchanged at 1268 and 390. The Knowledge Hub Homepage prototype was re-exported at 0.707.685 with this ruling in its header.

## 40. Quote Page Layout (TEMPLATE APPROVED BY KAIN, "100% approved", Code's S146; recorded by Chat S401)

**S149 and S150: the note at the head of section 22 governs where it touches this section (the rail, the date line, the type link, one hero, the Download row, and from S150 the hero's speech bubble, the one side panel and the subtitle).**

The quote page is built on the content page standard the article and book note share (§22, §32, the one block standard at §22). Until S401 its rulings lived only in DSRD 8 and the quote page's design folder; this section is its page-level home. Recorded from RULING__The_Quote_Page_Sitting_S146 and RULING__The_Quote_Page_Design_Principles_For_Every_Hub_Page_S146 (channel Archive). Kain approved the template whole at S146; the Kain's-eye half of chapters 10 and 11 is written in its DSRD 6 record, and the machine halves and chapters 1 to 9 stay open, so the page reads "built, gate open".

1. **The hero picture** is a square on the 256 cover column, from just above the label to the date line, inside the band's padding, so its right edge is the side panel's right edge. Three Achology bubbles sit behind it (large 180 behind its top right, medium 96 by its lower left, small 44 and faint beside its top left), desktop only, 1024 and up (theme 0.707.68 to 0.707.70). Below 1024 it stacks at 16 by 9 with no bubbles. **The pictures are blurry on purpose; never flag their softness as a fault.** **Superseded S150 (0.707.121): the three loose bubbles are gone, and from 1200 wide the picture is cut to a speech bubble 216 wide with a thin orange line in the same shape behind it; see the note at the head of section 22, item 10.**
2. **Download, Share and Copy** are separated by a 1px upright mid-grey line, 16 tall, centred in the 24 gap (0.707.66). Where the browser cannot share, the line falls only between the two buttons left.
3. **No Related Further Reading at any width** (§22.8, 0.707.82): Explore More Quote Articles does that job. The side panel travels the whole page and rests 48 above the hairline closing Explore More, and that hairline runs on across the right column, drawn by the panel, never by widening the hairline (the course cards widened at 0.707.79 when the hairline itself was widened, and were put right at 0.707.81).
4. **The reading progress line, the reading column's width and the body text size** follow the site standard at §32, items 5 and 6.
5. **The course picture in the writing carries the three bubbles in miniature (Kain, Code's S147, theme 0.707.97 and 0.707.98; recorded by Chat S403 from RULING__The_Book_Note_Is_Finished_And_The_Quote_Course_Picture_S147).** Kain: "it might be good for us to assign a very, very similar treatment to the image which appears halfway down the quote article." The course cover in the writing (a subject picture that keeps its own shape) takes the book note author photo's treatment, refined at 0.707.98 to tab 3 of four: the picture 224 wide with its top the figure's top, the figure 256 wide, the bubbles in the 32 strip at its right (96, 48 turned at the picture's foot, 22 between), the caption the picture's width; the medium bubble hangs from the caption so it meets the foot of a picture of any shape. Quote pages only, from 768 up; on a phone the picture keeps its plain, centred look. Measured live at 1440, 768 and 390: picture top 0 from the figure top, caption 16 below, no sideways scroll. The values live in the Author Photo component's build sheet (prototype v2); this item records the ruling.
6. **The course block's words** are the S147 words at §22.10 ("Ready to Take Your Learning Further?"), with "this article" kept on the quote page by Kain's choice.
7. **The section numbers (Kain, Code's S149, theme 0.707.109; recorded by Chat S405).** The same orange labels as the book note (§32, item 16), above each heading and in the contents. The contents' first entry, The Quote, is the quote card and has no heading, so the headings read from 02, matching their entries; Explore More carries its number above its heading. Verified live by Code on Trust Is The Key Ingredient: four headings numbered 02 to 05, five contents entries, all orange.
8. **The side panel and the subtitle (Kain, Code's S150, theme 0.707.127 to 0.707.132; recorded by Chat S408).** The panel carries the quote's source cover (the book's for 75 book quotes, the course's for 201 course quotes), at the foot of the screen once the hero has gone, with no decoration behind it, the book note panel's cover exactly (256 by 357, the book's own shadow). Book quotes keep "View the Book on Amazon"; course quotes take "View this Course on Achology". The author's picture and Know Your Psychology leave the panel. The subtitle takes two lines, balanced. The record is at the head of section 22, items 13 and 14.

9. **The in-text picture needs a section of three paragraphs or more (Kain, Code's S156 sitting, theme 0.707.156; recorded by Chat S418 from RULING__In_Text_Picture_Needs_Three_Paragraphs_S156).** Kain, on the first Lane B quote page read in Safari: "the problem is there's only two paragraphs in that section, which means it creates massive white space on the page". The picture still sits at the top of the second paragraph (item 5; section 22 item 12; the S116 rule), but only in a section of three paragraphs or more. The section the page names is tried first, then up to two after it; the first with three paragraphs or more takes the picture. Where none has three, the named section keeps it, so no page loses its picture. One function serves the quote page, the article and the book note (`achology_book_author_portrait()` in `knowledge-hub-parts.php`), so the rule binds all three. Measured by Code: 276 quote pages already have three paragraphs in the first section and are unchanged; the 17 Lane B drafts have two, and each takes the picture in its second section.

The general design rules this sitting produced, which bind every page, are recorded in DSRD 7 (S401). The side panel's rules are at §22.8.

### 40.1 The hero from S162 and S163

The quote page takes the Soft Light hero and its page changes in §22.15 and §22.15a, and the Ring contents panel and the close of §22.15b (S164 and S165), (S163: the Drawn Bubble contents, the panel down to the two paths, the two paths foot) whole. **Its hero is the article's:** the faded portrait, with no quote, slip or card in the band; the quote appears once, in the card under the band. The listen bar is off this page (Kain, K10, S422; built 0.707.234). The side panel runs down to the hairline above the two paths (S163, §22.15a item 4), restoring Kain's S146 ruling; the foot is the two paths. Below 1200 the Amazon or course button sits in the side panel's strip under the contents. Where anything above in §40 says otherwise, §22.15 wins.

## 41. Help Answer Page Layout (THE HALO BAND AND NINE TOUCHES RULED, Kain, Code's S180 sitting, 26 October 2026; SIGNED OFF at theme 0.707.540 the same day; written by Chat, S446)

**Overtaken 21 November 2026: the page takes The Help Centre Frame (Kain, S544; written by Chat, Session 480). See the last paragraphs of this section.** The Halo band, the facts inside it and the Two Ends foot described below are gone from Help answers.

**Where every value lives.** The approved prototype `PROTOTYPE__Help_Answer_Page_S180.html` and `BUILD_SHEET__help-answer-page.md`, in the FAQ Article Page folder of the Help design prototypes, cut from the build site under Code's Harness Rule 14. The prototype wins over this section. The category picture's rule is DSRD 1 section 8.2b.

**Kain's words:** "F2 Halo. Can we go with that, please? And then, yeah, I think all of the touches are absolutely great." Later the same sitting: "Yes, put the facts inside the band and take Listen off." Live on the build site at theme 0.707.532.

**The top of the page, in order.** The trail; then the Halo band: a slim slate band with the title in white and the date, word count and reading time under it, ended by the category picture (216 round, white keyline; 96 on a phone), which is bigger than the band and stops the slate at its centre, with faint white rings across the slate. The band bleeds 32 left so the title sits on the answer's edge; the picture's outer edge is the answer's right edge; the band's floor is 152, so a one-line title takes the two-line band. On a phone the band runs edge to edge with the picture half above its top edge. Then the answer; then the vote strip, which carries the enquiry line; then the related questions.

**The nine touches,** each standing still for a reader who asks for less motion: Reading Line; Picture Arrives; Answer Unfolds; Living Links; Orange List Dots; Thumbs Answer Back; Questions You Feel; Questions Arrive; Enquiry Line. The tenth, Listen Glow, retired with the Listen control.

**The enquiry line's words (Kain, in the S180 sitting, live since 0.707.534):** "Have a Question We Haven't Covered? Make an Enquiry", linking to /enquiries/. They replace the words Chat confirmed earlier the same day.

**The vote is Bare Thumbs (Kain, S180, live at 0.707.537):** "Yes, build option 2, Bare Thumbs." The thumbs stand alone in soft grey, no outline, 20 across in a 44 round hit area, warming to orange under the pointer; the chosen one sits on an orange tint. "Yes" and "No" stay in the markup for a screen reader, hidden from the eye. The pill shape approved 2026-07-29 is retired. Declined: Quiet Circles, Joined Pair, Warm Tiles.

**Signed off (Kain, S180, theme 0.707.540):** "The design is absolutely fine. The page design is signed off." The sign-off covers the Halo band with the facts inside it and Listen off, the touches, the Two Ends foot with his enquiry words, Bare Thumbs, and the review's fixes (list bullets back, list text 18, the band 48 under the crumbs). Prototype and build sheet at 0.707.540 in the design folder.

**Gone from the page:** the reading bar, its hairline and the Listen control (Kain's S422 ruling, help half closed at 0.707.532); the category picture inside the answer.

**Declined, so nothing is shown to Kain twice:** picture places Beside, Before and Above the Title; bands Warm Band, Picture Leads, Slate Band, Picture Fills the End, Picture Ends the Band, Designed Whole; the five bands with the slate running past the picture; Medallion, Sunrise, Slate Ring and Two Layers; the facts on their own line under the band. Three whole-page directions (Editorial, Charcoal Masthead, Warm Paper) were drafted and never shown.

**The one gate line this design makes, recorded as an exception at the sign-off (0.707.540):** breadcrumb-below reads 72 from the crumbs to the title (48, then the band's 24 inside it), against the site-wide 48 (Kain, S080), because the title sits inside the band he chose. The earlier 112 and the band's 56 above are gone at 0.707.540. The hairline line at the band's foot is the gate not yet knowing a filled band is its own boundary, as it already knows for a bordered card: an instrument fix for the factory session, not an exception.

**Open, not ruled:** whether the word count earns its place among the band's facts (asked in a brief Kain pasted in the sitting; unchanged).

**Three touches now come from site components (Kain, Code's S181 founder pages sitting, 26 and 27 October 2026; written by Chat, S447).** Each is one component under COMPONENT_REGISTRY.md's shared features, with its dated line in DSRD 8. Touch 1, Reading Line: the Help answer joins the site's one reading line, the Knowledge Hub line ("Yes, the Knowledge Hub line for the whole site."; 0.707.590), so its own 4px line at the top edge is gone and the thin 1px line at the header's foot takes its place. Touch 4, Living Links: the link hover wash is now drawn by base.css for every reading page ("Yes, the link hover wash on every page."; 0.707.613); on the Help answer it looks the same. Touch 5, Orange List Dots: retired; the list dot is grey on every reading page ("No, grey list dots for the whole site."; 0.707.609). The category picture in the band also sits whole on a white disc, by the shared rule of section 43 (0.707.603).

**The Help answer page takes The Help Centre Frame (Kain, Code's S544 sitting, through the main session, 21 November 2026; built at theme 0.708.337, the rail's indent mended at 0.708.339; written by Chat, Session 480, from RULING__Help_Answer_Page_The_Help_Centre_Frame_S544, DONE__Help_Centre_Frame_Built_S544 and SESSION_REPORT__S544). Where this paragraph and the rest of the section differ, this paragraph wins.** Shown four researched whole-page directions drawn on the real answer What is Achology? (the round: previews/help-answer-redesign in the theme, round.js and build.py), Kain chose and signed the Help Centre Frame. **His words:** "I actually really like the Help Center frame. I think it's neat, it's clean, it's tidy, and it's simple ... my choice is number 1, the Help Center frame." And of the topic picture: "would it be possible to build the section image ... in the top right-hand column above the on this page section." Shown the built page: **"Yes, signed."**
- **Left:** all fifteen Help topics in the Help landing's order, the current topic open on a window of eight of its questions and "All N questions". The questions run in the category page's own order (the editor Order field, newest as the tiebreak), so Previous and Next Question agree with that page.
- **Centre:** the breadcrumb, the title, the updated date and reading time, The Short Answer panel (from the answer's excerpt; no panel where there is none), the answer without its picture, the site's helpful strip, then Previous Question and Next Question. The topic overline over the title was removed (the topic was named three times above the answer) and the title's capitals stand level with the rail label and the picture.
- **Right:** the topic's section picture (the existing per-topic Help picture, lifted from the answer's own content so Rank Math still sees it, floating on white: "so it's just floating on the page"), then On This Page (from the answer's H2s, hidden under two), then Still Need Help? with the plain Make an Enquiry line. The side columns' two arrow links are plain links ("All N questions", "Have a question we haven't covered? Make an Enquiry"), because the arrow disc would not lay true in a 216 column.
- **Below 1024** the right column folds away and On This Page moves into the answer. **On a phone** it is one column, with a Browse Help Topics control that opens the rail.
- **The seven labels stand as placed (Chat, Session 480, ANSWER__Gate_Lines_And_Open_Rulings_S480 section 6):** The Short Answer, On This Page, Help Topics, Still Need Help?, Browse Help Topics, Previous Question and Next Question.
- **The reading column is a named exception (Kain, S544: "just make a proposal, please, based on best practices"; Code's proposal, his to overturn).** On Help answers in this frame it is 584 wide at 1200 and up, about 70 characters a line, against the 800 rule in section 32 item 6 and the S147 memory rule. The reason: 65 to 75 characters is the comfortable reading measure, and 800 would mean dropping one of the two side columns he chose. Every other page keeps 800. Measured at 1280: rail 64 by 256, centre 368 by 584, right 1000 by 216.
- **Gone from Help answers:** the $7 trial panel, the Other Questions block, the old Halo band and the old Related list (it stays in each answer's own content). **Kept, Chat's calls (S480, section 6 item 2):** the nine support topics keep their closing routes card (Contact Our Support Team and Ask an Achologist Anything; Kain, S091, "a person, not an offer") under the frame, and the UKRLP and ICO credit line stays under the frame on the answers that carry it.
- **Gate.** The page type's own gate lines (gutters 24, 24 and 16, the frame's trail above the rail with no Home step, and the hairline spacing of the Browse Help Topics pill on a phone) are ruled in ANSWER__Gate_Lines_And_Open_Rulings_S480 section 6 as the signed frame's own values. Schema is unchanged (FAQPage, BreadcrumbList); the speakable selectors name the new title and body classes.

## 42. Help Landing Page Layout (PLAIN TOP AND NINE TOUCHES RULED, then SIGNED OFF, Kain, Code's S181 sitting, 26 October 2026; written by Chat, S446)

**Where every value lives.** `BUILD_SHEET__help-landing-page.md` in the Help Landing Page folder of the Help design prototypes, with the page's DSRD 6 record beside it. The built template is archive-faq_article.php with the landing rules in help.css and help-landing.js. The build sheet wins over this section.

**Kain's words:** "1. Plain top please." Then, on ten touches: "all of them please, apart from five, light." Then: "Yes, I sign off the Help Centre page as it is." Signed on the real page in his Safari at theme 0.707.558, with the nine touches from commit e8612ca8.

**The page, in order.** The title block (overline, title, lead) on the page's one text line, not centred (DSRD 7 section 4.4a), with no band. The two groups of topic cards under 24 section headings, the word Achology in orange; on a phone each card puts its mark beside its name, every word kept. Popular Articles in the shared questions card (the FAQs block), as on the Help answer, Courses and Enquiries pages. The close in Kain's enquiry words from the signed Help answer, "Have a Question We Haven't Covered?" with a Make an Enquiry button to the Enquiries page, replacing the Contact Support email button. A hairline at every block boundary, 48 above and 48 below, 32 and 32 on a phone; the page ends 48 above the footer (DSRD 7 section 4.3).

**The nine touches,** each standing still for a reader who asks for less motion: Cards Rise in Turn; The Marks Draw Themselves; Warm Lift; The Mark Fills; The Count Points On; The Lines Draw Across; The Questions Arrive; The Title Settles; The Bubbles Drift. Not taken: the Spotlight.

**Declined, so nothing is shown to Kain twice:** Halo Band, Wide Band, Halo Band and Doors.

**Metadata (Chat confirms Code's wording, S446):** SEO title "Achology Help Centre: Straight Answers to Common Questions"; description as on the page, "Straight answers to the questions we're asked most: courses, membership, pricing, certificates, and support, all in the Achology Help Centre."; focus keyword "Achology help centre". The theme ships CollectionPage and BreadcrumbList schema.

## 43. Help Category Page Layout (TEN THEN SHOW ALL, Kain, Code's S181 sitting, 26 October 2026; SIGNED OFF at theme 0.707.603 the same day; written by Chat, S446)

**Where every value lives.** `BUILD_SHEET__help-category-page.md` and `PROTOTYPE__Help_Category_Page_S181.html` in the FAQ Category Page folder of the Help design prototypes. The built template is taxonomy-faq_category.php with help-category.js and help.css under .help-page--category. The prototype wins over this section.

**Kain's words:** on the structure, "I'd like to go for three, because that allows us to standardize how we present FAQs, right throughout the entire website"; on four whole pages built that way, "Option 2 please."

**The page, in order.** The trail; the Halo band of the signed Help answer (title, description, count, the category's picture); All Articles in This Category, every question with its answer line, ten showing and the rest behind "Show All {n} Questions"; Kain's enquiry line from the signed answer page; the other categories of the same kind under the Help landing's heading for that kind; the close by type as ruled at S091 (support: the answer page's closing card; pre-purchase: the trial panel). Where a question has no written excerpt, its line is the answer's own first sentence that is not a question.

**The two labels (Chat confirms, S446, as Kain picked the page with them):** "Show All {n} Questions" and "All Articles in This Category".

**DSRD 6 chapter 6, item 4** ("nothing behind a click or a collapse") is read against Kain's pick: every question stays in the delivered text, and rows 11 onward wait behind Show All by his choice. Recorded in the page's DSRD 6 record as an exception made by his pick.

**Later the same day: the review round, Two Ends (Kain, Code's S181 Help category sitting, 26 October 2026; live at 0.707.572; written by Chat, S447).** Asked whether every part of the live page was right, Code found the band floating off its places, the side bubbles half cut by the screen edge, the foot in three loose parts and long category names pushing their counts across. The first three were brought to the signed Help answer page; the foot and the list went to Kain as four options. "Option 1, Two Ends, please": the foot is the Two Ends foot of the Help answer page (section 41), and each other category's count sits under its name. The tablet trail reading is DSRD 7 section 4.3, Exception 16.

**The final pass, Both and a Ripple (Kain, the same sitting: "4 please"; live at 0.707.577).** Both section headings sit evenly above their first words; the description carries curly apostrophes; each answer line is held to two lines (three on a phone); the rows take the Help answer page's Questions Arrive and Questions You Feel touches; the other categories take the Help landing's warming mark; and one soft orange ripple runs out from the category picture when the page opens, standing still for a reader who asks for less motion. The values are in the build sheet, which wins over these lines.

**Then the band, More Air and Round End (Kain: "option 1, More Air, Round End"; on the build site at 0.707.586),** under the line standard for titles and descriptions, written home in DSRD 7 (beside the measure rule) and DSRD 8 (beside the fold rule).

**The ending is the Closing Card (Kain, Code's S181 Help category sitting, 26 October 2026: "Option 1, the Closing Card, please"; on the build site at 0.707.589; written by Chat, S447).** The other categories become the first part of the answer page's two-part closing card; on the nine support categories its second part is the support routes; on the six pre-purchase categories the trial panel follows. The build sheet carries the values. Found by Code for the answer page's owner and not touched: on a phone the answer page's closing card heading "Still Have Some Unanswered Questions?" ends on "Questions?" alone, against the line standard; the category page ties it.

**The band picture is shown whole, White Disc Behind (Kain, the same sitting: "Option 1, White Disc Behind"; on the build site at 0.707.603; written by Chat, S447).** The band first took the Help answer banner's shape (0.707.598); the crop then cut the picture's own label and orange strokes, so the picture now sits whole on a white disc, uncut, on the 15 category pages and on the Help answers, by one shared rule.

**Signed off, with two exceptions (Kain, the same sitting, at theme 0.707.603; written by Chat, S447).** "Yes, I sign off the Help category pages, with both exceptions." Both are written into the page's DSRD6_RECORD.md as approved by Kain: (1) on a tablet the trail reads 80, because the picture rises into that space, as on the answer page (DSRD 7 section 4.3, Exception 16); (2) the gate reads his enquiry line as the heading's supporting line.

**The band picture is Bigger, Further Out (Kain, Code's S184 theme main session, 27 October 2026: "Yes, Bigger, Further Out."; on the build site at 0.707.615; written by Chat, S447).** Kain: the picture at the end of the banner "seems really small", and it would be better "a little bit bigger, but also pushing it outside of the generic container." Of four, shown on three categories, he chose the second, told that it breaks his S146 rule that a picture never breaches its container. On a computer (1024 and wider) the picture is 300 across (from 216) and its outer edge passes the 800 column by 80 into the page, never closer than 32 to the window's edge; the band's square end stays on the picture's centre, so the halo and the ripple still spread from it, and a deeper band still grows the picture to 12 more than its depth. On a tablet and a phone nothing changes. The Help answer banner is untouched. It is the one named exception to that rule, in DSRD 7 section 14.0 rule 1. Declined: A Size Up, Biggest, Half Out.

## 44. School Page Layout (BLOCK ORDER AND THE KNOWLEDGE TREE RULED, Kain in Code's S512 and S519 sittings, 12 November 2026; written by Chat, Session 468)

**The block order (Kain, "Yes, move it", school pick 21, after Code read the nine blocks against the block map).** Banner; What This School Teaches; the five courses; the story; the knowledge tree; six free teachings; practise; what students say; enrol. The tree stood eighth, between What Students Say and the price, sending readers to 117 free pieces at the point of enrolling; it now follows the story. The grounds alternate: white story, sand tree, dark free teachings. The block map with each block's change is BLOCK_MAP__School_Page.md in the school page's preview folder.

**The knowledge tree (Kain's pick 20, "Yes, build it", on four whole options; built at 0.708.063).** The tree on the left; beside it the search and the topics, numbered, in two columns of five, the last rule of each column level with the tree's ground, the same number on each crown. Nothing under the tree: a leaf pointed at says its title on the leaf and lights it in the list. Under the block, the chosen topic's titles as a contents page: ten in two columns, one line each, in the order the leaves stand, never split by kind; its heading names the topic and its count and says the key once; one button shows the rest. On a phone the titles open straight under the chosen topic, six of them. One upright runs through the search glyph, every topic number, the heading's number and every leaf mark. Below 1280 the topics take one list (DSRD 7 section 4.2). Six long NLP titles end in three dots, as Kain saw and chose. Its words are SCHOOL_WORDS_SIGNED_S465.json, key knowledge_tree; its title and line are Kain's own (DSRD 7 section 3.3). Kain, signing it off in Safari: "Yes, Claude, it actually really is."

**Where the worry about time and the certificate lives (Chat's call, Session 468; Kain may overturn).** "I no longer worry about what I may do with it, the time, or the certificate" has no block on the school page since the questions people ask before enrolling came off it (DSRD 2 section 2.5 item 27). It lives on the course pages the school links to, whose questions answer it course by course. Nothing is built for it on the school page.

**Kain's picks of 15 and 16 November 2026, on Code's S521 sitting (written by Chat, Session 470).**

1. **Six Free Teachings, The Week on a Line (school picks 23 and 24).** Of four directions: "I'm looking at option number one, the week on a line. I actually really like this. It's simple, but I believe you can polish it". Of the polished line: "Yes, build it". On the built page at 0.708.079: "Yes, it's right"; and after the privacy line moved beside the tick box at 0.708.083: "Yes, it's right". One component, two fillings: a school page shows its six signed teachings, a course page its own lessons 1 to 6. No picture and no name of Kain in the block ("I don't want this page to be about me"). The Day 1 question line stays off (Chat's call, Session 470: he signed the block without it). Its band spacing is recorded in DSRD 7 section 4.3.
2. **The story, one chapter at a time, with The Read On Card (school pick 25).** "Yes, it is Claude. Yeah, that's actually really neat." The story opens on its first chapter; a stop on the banner or the card at a chapter's foot opens the next. The card reads "Next: Chapter Two of Five", the next chapter's name and years, "In This Chapter", then that chapter's moment titles; the last chapter has no card. The fifth chapter is named What You Can Learn in This School, with Today. It takes two lines on the banner's fifth stop at 1440 and on the card at 390, and stays so (Chat's call, Session 470: both lines are full, nothing is cut and no type shrinks).
3. **The story's line endings, signed on the built page** (DONE__School_Story_Line_Endings_Signed_S521, Archive): the last lines are laid by measure, never held as a block, the rule the site's last-line sweep then carried to every page at theme 0.708.099.

**The knowledge tree on a tablet (school pick 29, Kain in Code's S528 sitting, 16 November 2026; written by Chat, Session 470).** Of his own earlier tablet arrangement, the tree beside one long list: "such a poor use of space". Shown four versions on the School of NLP, he said: "Yes, version 1". From 768 to 1279 wide the tree takes the computer's arrangement: the tree on the left, a third of the width; the ten topics beside it in two columns of five, their names one step smaller (16, DSRD 7 section 3.2); the counts in one column at the rule's end; the chosen topic's titles under the whole block in two columns, one line each, ten shown. This replaces "below 1280 the topics take one list" in the knowledge tree paragraph above for tablets; the phone (under 768) and the computer (from 1280) are unchanged. Built at theme 0.708.123 (DONE__School_Page_Knowledge_Tree_Tablet_Layout_S528, Archive).

**The week draws itself along the line (school pick 30, Kain in Code's S528 sitting, 16 November 2026; written by Chat, Session 471).** On the Six Free Teachings block, beside picks 23 and 24. Shown four ways the week could arrive, he said: "Yes, version 1". As the block comes into view and its two figures count up, each day arrives in turn, Day 1 to Day 6: its ring lands, its words rise, and the line draws on to the next ring, once per visit. Under reduced motion, or with no script, the week stands whole. The finished state is the block as signed. It runs on all seven school pages and all 28 course pages. Built at theme 0.708.124 (DONE__School_Page_Six_Free_Teachings_The_Week_Draws_Itself_S528, Archive).

**A pressed row folds open (school pick 31, Kain in Code's S528 sitting, 16 November 2026; written by Chat, Session 471).** In the Practise What You Learn block, on school pages only. Shown four ways a pressed row could open, he said: "Yes, version 1". The row's line folds open in under half a second and shut a little quicker, its words coming up as it opens, and the plus turns over to a minus. A shut line stays out of reach of the keyboard and a screen reader. Under reduced motion nothing moves. The block at rest is unchanged (picks 6 and 14). Built at theme 0.708.125 (DONE__School_Page_Practise_Rows_Open_Smoothly_S528, Archive).

**The film stands flush with the top of What This School Teaches (Kain in Code's S528 sitting, 16 November 2026; written by Chat, Session 471).** "Claude, this is the second time I've had to pull you up with this video, not sitting flush with the top of the 'What This School Teaches' block." On a computer the heading, its line and the text are the left column, and the film's top is the heading's top, as on a course page; on a tablet and a phone the film stands under the text. DSRD 7's full container rule is corrected to match. Built at theme 0.708.126 (DONE__School_Page_Film_Flush_With_The_Top_S528, Archive).

**The Courses in This School is The Dark Stage (school pick 32, Kain in Code's S528 sitting, 16 November 2026; written by Chat, Session 471).** "this block here is letting down the entire page." Of four directions: "I like the dark stage option actually", with "you're using full width of columns when it comes to placing text" and "We have essentially an entire suite of buttons designed for the website and links, and you don't seem to be using it." The chosen course stands on the brand dark, its picture melting into the panel, its name at 28 (24 on a phone), its line at 18 in white at 0.9, its three figures one row with hairlines between; Explore This Course is the site's main button (DSRD 7 section 5.1); a two row supporting line fills its row (DSRD 7's full container rule, now site-wide). Built at theme 0.708.127 to 0.708.130 (DONE__School_Page_Courses_Block_The_Dark_Stage_S528, Archive). Owed by Code: the whole page's controls brought into the button family and its spacing measured against DSRD 7 sections 4 and 5.1.

**On the school pages the buy bar steps aside over the story's closing panel (school pick, Kain in Code's S542 sitting, 20 November 2026; built at theme 0.708.306; written by Chat, Session 480, from RULING__School_Pages_Buy_Bar_Steps_Aside_Over_The_Story_Panel_S542).** Kain's S482 rule had the bar step aside over the old story; the new story had no such rule, so the bar sat under the closing panel and two buy buttons showed at once. Shown four options in the Change Viewer (previews/school-page-s482/round-bbar.js): 1, the bar steps aside while the story's closing panel is on screen; 2, while the chapters are read; 3, for the whole story; 4, the bar stays and its button goes quiet. He answered **"Yes, option 1."** school-page.js section 9 marks the page while `#school-story .sps-foot` is on screen, and school-page.css slides the bar away then, on the seven schools only (not the Access All Areas Pass). It is the course page's own move over its price block (course-page.css ch1). Checked at 1280 and 390 on all seven: the bar is away over the panel and back once the panel has passed. It is a behaviour, not a look; the ruling lives in the two files' comments, which quote Kain, and here.

**What students say is the one reviews block (Kain, Code's S542 sitting, 20 and 21 November 2026; built at 0.708.348 to 0.708.350; written by Chat, Session 480).** On the school pages the block shows two rows with the third behind the control, its look Membership's, with the two link cards Read All Student Reviews and View All Member Testimonials in place of the two plain text links ("Yes, do that"; "Yes, Claude, I'm totally happy to go with that"). The block is written whole in DSRD 8 section 44.


## 45. Homepage and Academy Page Block Maps (STRUCTURE RULED, Kain in Code's S522 Schools page sitting, 16 November 2026; written by Chat in a side session of that sitting)

**Structure only.** The look of neither page is ruled, nothing is built, and no block is designed with real copy until its words are signed. This section is the home of both block maps. Code's working copy, with the same tables, is BLOCK_MAP__Academy_Page_And_Homepage.md in the Schools page proposal folder of the theme's previews folder.

**45.1 Kain's rulings, in his words.**

1. **There is no separate Schools page. There is one Academy page.** "rather than having a schools page within the website, we literally just have an academy page, because trying to explain what all the schools are doesn't make any sense when we can just link to them. Anyone who's interested will click through ... we'd actually just have an academy page that introduces all aspects of the academy, from what the academy is, why it exists, what it believes. We can link to the beliefs through this page as well. The 7 different schools and the courses, and then the learning experience within the community."
2. **The Homepage and the Academy page are structured together, so they never do the same job.** "we need this page to be clearly distinguished and apart from the homepage ... we don't want two pages essentially doing the same thing."
3. **Neither page repeats what a built page already says.** "nobody in the world who isn't a Udemy student knows who I am ... I don't want this to be a major thing ... we've got a founder's letter, don't we? And we've also got an about page ... I want you to look at this entire website, right, and tell me what needs to be on the homepage and what needs to be on the academy page." And: "Guesswork's not going to cut it now."
4. **The structure of both pages,** as Code put it to him after reading every built template block by block: "Yes, that's right".

**45.2 The dividing line.**

- The Homepage is about all of Achology. It says what Achology is in one glance and gives a door into each wing. It never explains.
- The Academy page is about the training alone. It says the one thing no built page says: what a school is, how the seven differ and fit together, and where to start.
- The About page keeps who, why and the story. Pricing keeps cost. Certification and Accreditation keep what is earned. Neither new page restates them; each gives a short taste and links.

**45.3 The Homepage, at `/`.** Its job: get a stranger to understand what Achology is and choose a wing.

| # | Block | The change it carries (the reader's words) | Component |
|---|---|---|---|
| 1 | What Achology Is | "I now know what this place is." | New. One bold sentence, two buttons. |
| 2 | The Figures | "I now believe many people learn here." | Existing: `achology_figure_bar()`. |
| 3 | Three Wings | "I now know the three things I can do here, and which is mine." | New. Train in the Academy (to the Academy page), read free in the Knowledge Hub, learn together in the community. |
| 4 | Around the World | "I now believe this is real and worldwide." | Existing: `achology_global_impact()`. |
| 5 | In Members' Own Words | "I now trust it, because people like me say so." | Existing: `achology_member_stories()`. |
| 6 | Ten Different Ways to Experience Achology | "I now know every door, if the three wings were not mine." | Existing: `achology_site_gateway()`. |
| 7 | Stay in Touch | "I am not ready, but I do not want to lose this." | The general mailing list sign-up. Not yet a component. |

Not on the Homepage, and why: a seven schools row (the header menu and the footer carry the seven schools on every page); a founders block (About, the founders' letter and Our People own it); the $7 first month as its own block (the footer invitation carries it on this page); the "Where Would You Like to Begin?" block (it is already on About, Pricing and every Knowledge Hub page); the mountain (it lives on the Academy page only). This overtakes DSRD 4 section 10.1's nine blocks and DSRD 2 section 2.1; DSRD 4 section 10.0 says what became of each.

**45.4 The Academy page, at `/academy/`.** Its job: get someone who wants to train to choose a school or a first course.

| # | Block | The change it carries (the reader's words) | Component |
|---|---|---|---|
| 1 | What the Academy Is | "I now know what the Academy is and what it teaches." | New. One plain definition, 28 courses, seven schools. |
| 2 | Seven Schools, Seven Questions (a working name; it was Seven Schools, One Mountain until later the same day, section 45.8) | "I now know what a school is, how the seven differ and how they fit together." | New. The centrepiece. Each school stands under its own name with about four questions beneath it, drawn first from Kain's signed lesson questions, each tied to the course that answers it (section 45.9, which overtakes 45.8's one question for each school). The questions themselves are not yet signed. |
| 3 | Where to Start | "I now know my first step." | New. The Diploma as the course that belongs to all seven schools, and a link to the Courses page's chooser. |
| 4 | How Learning Works Here | "I now know what studying here is like." | New. Watch, practise with a workbook, practise with people, earn the certificate. Four short steps, each linking to the page that explains it. |
| 5 | What It Is Taught From | "I now know what this place believes before I buy." | New. The beliefs in a few lines, links to What Achology Believes and the Manifesto. |
| 6 | Three Ways to Study | "I now know I can take one course, one school or everything." | New, headline level only. Links to Pricing. |
| 7 | Questions | "I no longer worry about the things I had not asked." | Existing: `achology_faq_block()` with chosen Help answers. |

Not on the Academy page, and why: Why It Exists (the About page's first question and the founders' letter); Who Teaches You (Our People); What You Earn (the Certification and Accreditation pages; block 4 links to them); a reviews wall (the Reviews and Testimonials pages; the school and course pages carry their own); prices (Pricing). This overtakes DSRD 2 section 2.2's five blocks and section 2.4's Schools page.

**45.5 The order, tested against what students say and what people ask (Chat, 16 November 2026; the test Code's block map named as owed).** Two sources were read. The 4,517 student reviews in the theme's review file were counted by what each one speaks of, by a script of plain word matches, so the figures are rough guides and no more: the teacher and the teaching, about 13 in 100; how clear and easy to follow the course is, 11; using it in real life, 10; a change in how they see things, 7; the workbooks and written resources, 7; helping other people, 6; the certificate or a career, 6; being new to the subject, 5; understanding themselves, 5; price and value, 4; what to take next, 2; the community, 2. The Help section's own questions were read by category: the Getting Started questions are where to start, which course to take first, being overwhelmed by the options, whether there is an order, and whether a beginner can begin. **The order stands.** Where to Start stands third, straight after the schools, because choosing is what a newcomer asks about most. How Learning Works Here stands before the beliefs, because students speak of clear teaching and real use far more often than of a point of view. Three Ways to Study stands sixth, because price is among the things students speak of least. Two things the evidence shows that the order does not carry, both recorded and neither changing a block: the teacher is what students name most, and the Academy page leaves Who Teaches You to Our People on Kain's own ruling above, so block 4's first step carries one link to the people who teach (Chat's call; Kain may overturn); and the reviews cannot test the Homepage's third wing, because almost all of them were written by students who studied on Udemy, where there was no community to speak of.

**45.6 The words.** Chat's, under the Site Copy check sheet and the Content Standard's Part 18. They live in each page's design folder: 000__COPY__Academy_Page_Words_S522 in the Academy Landing Page folder and 000__COPY__Homepage_Words_S522 in the Homepage folder. Each file says at its head whether Kain has signed it.

**45.7 Open, with owners.**

1. **What Achology Believes is not built.** Its signed words are APPROVED__What_Achology_Believes_Page_Copy_S386 in the Launch Content Planning folder (Kain, 28 September 2026; corrected S425); the theme has no template for it, and its brief has waited on a theme session since Session 390. The Academy page's block 5 and the Certification page's button both link to it. Code's, behind the Academy page.
2. **The addresses.** /academy/schools/ is retired and redirects to /academy/ (DSRD 1 sections 2.3, 11.3 and 13.1; Chat's call from ruling 1, which Kain may overturn).
3. **Unbuilt pages these two link to:** /membership/ and /access-all-areas/. A link to a page not yet built is a page to come, not a broken link.
4. **The Homepage's Stay in Touch block** has no component and no words yet. Its form is one of DSRD 4 section 5.1's and its words are written with that form.

**45.8 The mountain is dropped from block 2, and Seven Questions is being explored in its place (Kain, later in Code's S522 sitting, 16 November 2026; written by Chat the same day).** Of the mountain, Kain said: "it's not transparent enough ... I think the mountains, that was where I was there and thinking, you know, a while back, but I think we need to simplify this ... I'm not even saying use mountains." Code put four concepts to him in words and recommended Seven Questions: each school is presented as the one human question it answers, in the visitor's own words; the visitor spots their question and it opens to the school behind it; the Diploma is the course that asks all seven. His answer: "Yeah, I'm open to exploring this, Claude. It would certainly make sense." **That is a direction to explore and not a signature.** What follows from it: block 2's working name is Seven Schools, Seven Questions; no mountain words are written for it, and Code's mountain map is no longer its first drawing; block 3 follows from it, with the Diploma as the course that asks all seven; and block 7 is not headed Questions beside a block of seven questions (its heading is Chat's to choose). The seven questions are the idea itself, so they go to Kain for his yes before the other blocks' words. They are found in the customer's own language and never invented: Chat's proposal, with the students' words behind each one, is QUESTIONS__Seven_Schools_Seven_Questions_S522 in the Academy Landing Page folder. Nothing else in sections 45.1 to 45.7 changes, and the Homepage is untouched.

**45.9 One question for each school is turned down; each school takes several (Kain, later again in Code's S522 sitting, 16 November 2026; written by Chat the same day).** Shown Chat's seven questions, Kain said: "why do I think the way I do, and can I change it? That's a good question. But how am I getting in my own way? That question doesn't even make sense. Like, no one would. I don't think anyone would ever actually ask that ... rather than kind of pin everything onto one question, I think what we need to find, I think we need to find a range of questions for each school ... We need these questions to be pretty much the same length ... people have more than just one question, don't they? And the schools answer way more than just one question ... these questions, they need to be specific. They need to be descriptive, and questions that actually make sense." Of the mindfulness question he said it has nothing to do with mindfulness, "Not the way in which we teach it." Code then proposed, and he answered "yes": each school shows its own name plainly with four questions beneath it (three or five where a school reads better so, never forced), drawn first from the 354 lesson questions he has already signed on the course pages, with the reviews, Help and search demand as support. Every question passes three tests: a real person would say it out loud; the school teaches the answer, as Achology teaches it; and it names something specific. The questions are of similar length, and each is tied to the course that answers it, so that it can link there. "Why do I think the way I do, and can I change it?" is kept, on his praise. **What this overtakes:** section 45.8's one question for each school, the first four about yourself and the last three about other people, and the Diploma as "the course that asks all seven". Chat's proposal under the new shape, 29 questions with the course behind each, is the file QUESTIONS__Seven_Schools_Seven_Questions_S522 in the Academy Landing Page folder, which replaces the first proposal under the same name. Kain reads it before anything else moves; the other blocks' words stay unasked until then.

**45.10 The questions are the visitor's, not the teacher's: five rules (Kain, later again in Code's S522 sitting, 16 November 2026; written by Chat the same day).** Shown the 29 lesson questions, Kain did not sign them: "I can see now that what you've done is you have essentially pulled together a list. You've got 4 questions for each. But I can also see that you haven't given any thought whatsoever into framing these questions as questions that the website visitor might actually resonate with ... You have not drafted these questions in consideration of questions that the actual website visitor might actually be asking right now." And: "I don't want you to guess here. There must be a marketing rule or a marketing principle here somewhere ... about drafting questions as though they are written from the perspective of the student or of the learner or of the customer ... what's the actual principle here that you need to build these questions off?" A lesson question is what a teacher asks; it is not what a visitor arrives with. Code named the principle to him with its sources, and he answered: "Yes, rebuild them". **The principle:** enter the conversation already going on in the reader's mind (Robert Collier, The Robert Collier Letter Book, 1931); write to the reader's stage of awareness (Eugene Schwartz, Breakthrough Advertising, 1966), and a new visitor to the Academy page knows their problem and does not yet know the product; take the words from real customers and never from the writer (voice of customer research, Joanna Wiebe, Copyhackers); and speak in words the user already knows, never the organisation's terms (Nielsen Norman Group, usability heuristic 2). It is DSRD 2 section 0.4's own drafting layer, copy found in the customer's language and never invented. **The five rules, for every question in block 2:** (1) it names a problem or a wish, never a topic; (2) it is in the first person, I, my, me; (3) it uses no word the visitor has to learn from Achology; (4) it can be traced to real people saying or searching it, with the proof kept beside it; (5) the course sits beneath it as the answer, never inside the question. **Still standing from section 45.9:** each school under its own name, about four questions each, similar length, each tied to the course that answers it, and each truly taught by that school as Achology teaches it. "Why do I think the way I do, and can I change it?" stays. The signed lesson questions now serve only to prove which course answers a question. Chat's rebuilt proposal keeps its file name, QUESTIONS__Seven_Schools_Seven_Questions_S522, and carries each question's proof.

**45.11 The kind is right and the wording was too loose: a question a visitor could bite (Kain, later again in Code's S522 sitting, 16 November 2026; written by Chat the same day).** Shown 28 first person questions taken almost word for word from searches, Kain said: "do you really think these questions just need to be like 5, 6, 7 words long? Do you think they can be like a, I don't know, maybe all similar in length, but in a way that are kind of descriptive? Just although they're concise questions, they ask a lot ... some of them just feel like loose ... I just want these questions to be, concise yet clean, descriptive, not vague. Just I want them to be something that a website visitor could bite." Code's reading, put to him: holding a question word for word to a search made it thin, because people type to a search engine in shorthand, and that is not how the thought sounds in a person's head; what gives a question bite is a specific moment the visitor recognises from their own life, with a tension inside it, what I want against what keeps happening. Code showed him four pairs as illustrations, among them "How can I build resilience?" beside "Why do small setbacks knock me off course for days?". His answer: "yes, that is the bite i mean - thank you claude". **The rules as they now read, overtaking section 45.10's five:** (1) a specific moment with a tension in it, never a topic and never a bare wish; (2) first person; (3) no word the visitor has to learn from Achology; (4) the struggle it names is proved by real people, in searches, reviews or Help, kept beside it, and the wording no longer has to be the search itself; (5) the course beneath it as the answer, never inside the question, and the course must truly work on that moment, as Achology teaches it; (6) ten to thirteen words, all close in length. Code's four illustrations are not signed copy. Still standing: each school under its own name, about four questions each, and "Why do I think the way I do, and can I change it?".

**45.12 The plan page is agreed, and block 2 shows the seven schools plainly, with no questions (Kain, Code's S524 restart sitting, 16 November 2026; written by Chat, Session 470).** Code put one page to him in Safari, plan.html in the Schools page proposal folder of the theme's previews folder. Asked "Is this plan right for both pages?", he said: "Yes, that's right". His instruction for the page the same day: "Show the seven schools plainly, name, one line and a door, with no questions." **What his yes covers:** the seven blocks of each page in the order of sections 45.3 and 45.4, each with its job, whether it reuses a built piece and where it links, as the plan page shows them; the Academy page's block 2 as the seven schools, each with its name, one line on what it studies and a door to its own page; and the built pieces reused as they stand (on the Homepage, The Figures, Around the World, In Members' Own Words and Ten Different Ways to Experience Achology; on the Academy page, the questions block under the heading Practical Answers Before You Begin). Every other block is new. **This overtakes sections 45.8 to 45.11:** no questions stand in block 2, so their question rules no longer govern it; they are kept as the record. **Not covered by his yes:** the look of any block (each new block is designed next, one at a time) and the words. The seven school lines on the plan page are Chat's unsigned drafts in 000__COPY__Academy_Page_Words_S522; block 2 needs a heading, a supporting line and one line for each school, written by Chat and signed by Kain before the block is drawn with real copy.


**45.13 Four rulings on the whole Academy page preview (Kain, Code's S527 sitting, 16 November 2026; written by Chat, Session 470, from Code's four RULING files of S527).** Kain looked at the whole page as one preview in Safari (academy-page-s527 in the theme's previews folder) and ruled four things.

1. **The name.** "The Achology Academy of Modern Applied Psychology. That's kind of what it is." It is the page's title in the banner and is written home in DSRD 5 section 2. Chat's call, which Kain may overturn: the full name stands as the page title and in the page's search title; the breadcrumb, the header and the footer keep the one word Academy, as a menu word; the short form without "Modern" is never used.
2. **An introduction block under the banner.** "some sort of information block ... 2 paragraphs of equal length text that we can build at the top of this page". It stands straight under the banner and the section bar, headed Why Does Achology Exist?, with his signed About page words. This overturns section 45.4's choice to leave Why It Exists off this page.
3. **The section bar.** "use that component that we've already built into the course pages and the school pages on this page." The course page's own component, reused and not redrawn. Its labels are Chat's to write.
4. **The beliefs block becomes the page's foundation.** "we're really emphasizing here the foundational assumptions and beliefs that we base all of the content on within all the courses, within all the schools." Asked whether to rebuild it as a wall of doors to the Seven Beliefs articles, placed under the seven schools, he said "yes, please do".

**The order now:** the banner; the section bar; Why Does Achology Exist?; The Seven Schools; What Every Course Is Taught From; Where to Start; How Learning Works Here; Three Ways to Study; Practical Answers Before You Begin. This overtakes section 45.4's order where they differ.

**Also asked, not yet picked:** a banner wall of the field's faces, portraits faint at rest and in colour under the mouse; four shapes are in front of him in the Change Viewer (round-hero.js in the same folder). Nothing on the page is signed yet: every word on the preview is Chat's unsigned draft or his own About page words.

*No em or en dashes in this addition; checked before writing.*

**45.14 The banner, the opening block and the words, signed (Kain, later in Code's S527 sitting, 16 November 2026; written by Chat, Session 470, from Code's three later RULING files of S527).**

1. **The banner is The Whole Banner.** Of four shapes in the Change Viewer: "This looks brilliant. I actually think I really like option 4, the whole banner." 96 portraits across the banner's full width, strong at the right and a whisper under the words. With it: the best known stand at the left ("Plato in there, Aristotle, obviously, definitely Sigmund Freud, Maslow"); each portrait is drawn in on the head, shoulders and chest; the name under the mouse is one small line, first initial and surname ("we can only have one line of text per name"). Of the changed banner: "that's a beautiful, beautiful looking banner." His own portrait stands third row down, fourth from the right, at his ask ("place a picture of me, Kain Ramsay, somewhere in that"). Nothing more is said of it here.
2. **The banner line and the opening block** are his own phrases, placed by Code at his ask. Of them: "that is fantastic. What you've just done is absolutely fantastic." The block is headed Why Does the Achology Academy of Modern Applied Psychology Exist? and replaces the About page words of 45.13 item 2.
3. **Its movement.** Asked for "bells and whistles" on the top two blocks, he was shown four: the tilted speech bubble faint behind the right paragraph and past the frame's edge, in this block only; the opening block's words rising in one after another the first time it is reached; the wall arriving column by column; one face at a time coming up in colour every few seconds, never under the title's words. All four stand still under reduced motion.
4. **The words, signed by Chat on Kain's instruction** ("read them, confirm, approve, ensure they pass the news desk standards", 16 November 2026). Each is measured on the page at 1440 and 390 with no last line under four words, scanned clean of banned words, and judged by a second reader. "For the first time" is taken out as a claim no one can prove; the paragraph says instead that Achology takes no side in the argument. "Should never have been held captive by academia" is taken out under the Content Standard, Part 18 rule 1, which names others fairly and never by a fault; the line now says the ideas belong to everyone, not only to those inside a university. The words are in Chat's answer to Code, ANSWER__Academy_Page_Words_Signed_S470, in the channel Archive once Code has placed them.
5. **Chat's calls, which Kain may overturn.** Living people leave the portrait wall, because a sales banner can read as their endorsement; Code fills the places from portraits of people no longer living, and his own portrait stays. The wall carries one small Portrait credits link that opens each portrait's credit as its author page shows it. The beliefs block keeps the seven beliefs only: no doors for parts 1 and 9, and no topic stances on this page. On a phone the reading text never goes under 16, as on the course page.

*No em or en dashes in this addition; checked before writing.*

**45.15 The seven schools block becomes one gateway, the Journey Line (Kain, later again in Code's S527 sitting, 16 November 2026; written by Chat, Session 471, from Code's three last RULING files of S527).**

1. **One gateway, not seven strips.** "rather than having seven strips ... a mechanism ... they're kind of cards that contain an image, the school name, and a description of the school and why the school exists ... Very, very simple, but then allows people to kind of click through the seven different schools ... it's kind of like the gateway, giving a taster of all schools". This replaces the seven rows of 45.12. Each school's description is the first paragraph of that school page's own signed What This School Teaches block, word for word.
2. **The heading and line introduce the schools.** "we need to warm up the visitor and take them on a learning journey. So we need to explain what the schools are, why they exist, and how they're different from traditional psychological schools, within the heading and the subheading". His angle: the schools of psychology have debated for a century, Achology takes no part in it, and each school offers one perspective on understanding and influencing the human experience. These replace the heading and line Chat signed earlier the same day. "For the first time" stays out, as in 45.14 item 4.
3. **Four directions for every block worked like this.** Of a single design placed on the page: "When we're iterating like this, you give me 4 options to choose from, then I choose the direction ... this is our minimum standard ... you never work in a block like this unless you're giving me 4 directions to choose from." It restates the standing rule of S121, S154, S183 and S478.
4. **The pick is the Journey Line.** Of four (The Seven Doors, The Journey Line, The Deck, The Circle of Seven): "2, Journey Line". Seven numbered stops on one line, each with its school's full name; under it one wide panel holds the chosen school's picture in a field of its own colour, "School 1 of 7, 5 Courses", its name, its signed line, its description and the door Explore the School; two arrows step through in order. On a tablet and a phone the seven numbers stand in a row on the line, over the panel, the picture at its top. Preview commit d6891dca. The other three designs' rules leave the stylesheet once Kain calls the block finished.
5. **Signed:** see 45.16 item 4.

*No em or en dashes in this addition; checked before writing.*

**45.16 The schools block finished and passed, and the beliefs block picked (Kain, later still in Code's S527 sitting, 16 November 2026; written by Chat, Session 471, from Code's five last RULING and ASK files of S527).**

1. **The schools block is the Open Stage.** Asked for every component of the Journey Line to be made "more visually impressive, more visually spectacular", he was shown four finishes (The Lit Line, The Colour Stage, The Open Stage, The Seven Windows) and said: "let's go with option three ... I really like that. That's just very, very neat." No card; the picture stands on its oval, the words behind one rule of the school's colour. His standard for it: "pay attention to detail on every component. And by that, I mean every component."
2. **His six corrections.** The picture goes back to its oval ("The oval looked really cool"). Nothing stands behind it: of the neurons drawn there, "an absolute mess", and of the watercolour tried next, "That's rubbish". The line under each name is that school page's own banner subtitle, on at most two lines ("at least 2 full lines ... maybe kind of shorten it a little bit"). "School 1 of 7" moves into the card, on the line of Explore the School at the card's other side. "Next School" is gone ("everyone can see what the next school is going to be based on the road numbers"). The numbered circle's hover shadow stays clear of the text. And: "next time, just wait. If I share a picture, ask me what I want to change." He passed the block down: "Yes, move down" (preview commit 5082e6c1).
3. **One name shortened on the line, by his leave.** "I'd be happy for you to lose the word applied, if that would allow us to somehow get the name of the school on 3 lines." On the line's stop only, the school reads The School of Mindfulness, Insight and Wisdom (MIW), because its full name ran to four lines and stood 1 from its neighbour. The full DSRD 5 name stands in the panel's heading and is what a screen reader hears. Chat's ruling: a named exception to DSRD 5's never-shortened rule, on this one stop label only.
4. **The words, signed by Chat, Session 471.** The gateway's heading: Seven Schools, Working Together and Not Against Each Other. Its line, cut to the 25 words the supporting line allows: "For a century, psychology's schools have argued. Achology's seven bring their strongest ideas together, each a different way of understanding people and helping them change." The four school subtitles Code cut to two lines are signed as cut (ANSWER__Academy_Schools_And_Beliefs_Words_Signed_S471 in the channel). **Overtaken (Kain and Chat, Session 472, 16 November 2026):** all seven subtitles are rewritten as schools and signed at 33 to 35 words and 202 to 221 characters each, and each card takes its school's line as it stands (DSRD 2 section 2.5 item 31). The two-line limit above is overtaken for the card by that signature; if a signed line cannot sit on the card as designed, Code tells Chat and the card's measure is put to Kain on a rendered round, and no signed word is cut to fit.
5. **The beliefs block is the Staircase.** Of four (The Seven Lines, The Staircase, The Spine, The Keystone): "Let's go in the direction of staircase. I do genuinely like that." Of its look: "it's designed well, but ... it's just empty ... I want the design now to be really strengthened."
6. **Its doors open in a new tab.** "these beliefs, they need to open in a new tab ... because this is essentially a purchase page. So we can't be linking out to an information page. We need to have the product page remain open in their tab." Each link says so to a screen reader. The link is on each belief's own name, never on a label such as Read This Belief (Content Standard Part 16).
7. **Its words, and the rule for its seven sentences.** "the text within this block, it's again it's empty text ... I'd like the complete text solution". Of the sentences: "draft a full sentence of explanation for every single one of them ... very, very similar in length, plus or minus five characters", and then: "these beliefs, we're not speaking to the person. These are statements of fact, kind of like presuppositions ... They are beliefs." So each is a statement of fact about people, never addressed to the reader, all seven within five characters of each other, and each faithful to its belief in the signed What Achology Believes copy. The heading, its line and the closing words speak to the visitor, from his own article, The Seven Beliefs Achology Is Built On. The signed words are in the ANSWER file named in item 4; they replace the heading and line of 45.14.

*No em or en dashes in this addition; checked before writing.*'

**45.17 The beliefs block in Kain's own words, and the lower blocks reused (Kain, Code's S527 and S530 sittings, 16 and 17 November 2026; written by Chat, Session 471).**

1. **The block is the Side Stair.** After rounds of four (the Staircase, the stones, the soft, the path and the right side): "totally happy to go with option two, the side stair", with The Panel Beside at its right. One orange line of treads and risers, each belief a step further in, its number, its name (the link, new tab) and its sentence beside it; the line ends in a floor; the panel stays in view beside the first five beliefs. Kain agreed nine improvements and six more ("I want to say yes to all six ... but ... adhering to our ... font size, font weight rules, and also our spacing rules").
2. **His title, placed by Code at his direct word:** The Seven Beliefs Every Achology Course Is Built On ("7 beliefs, 1 chain means nothing"). It replaces Seven Beliefs, One Chain.
3. **His supporting line, word for word:** "No matter which subject interests you most, every Achology course is grounded in the same seven foundational beliefs. We'd rather you read them now than come across them unexpectedly halfway through your first course." His copy, placed as given, past the 25 word band.
4. **His seven names and sentences, pasted by him, replace Chat's seven, exactly as he typed them, every capital and full stop** (sentence 6 as he rewrote it). Kain, 17 November 2026: "I gave you 7 titles. Use them, Claude ... Use the text I gave you." Elsewhere (the What Achology Believes page, the nine Seven Beliefs articles, the vault) the signed names stand until Kain says the new ones hold everywhere.
5. **The panel's words, plain at his word:** "you've written some sort of poetry here that most human beings will not be able to understand." Its line: Each belief builds on the one before it. Under it: That is why they come in this order. Take one away and the ones after it stop making sense. We'd rather you read all seven now and decide Achology isn't for you than start a course without knowing what it is built on.
6. **The lower blocks are the site's own** (S530): "Do not reinvent the wheel". Where to Start is the signed learning block, Where Would You Like to Begin? (S183, S184); How Learning Works is the course page's How the Course Works and About the Certificate (picks 209 to 212), headed How Every Course Works and About the Certificate; the ways to study are the four cards that open the Pricing page, headed Four Ways to Study; the questions are unchanged.

*No em or en dashes in this addition; checked before writing.*

## 46. Access All Areas Pass Page Layout (BLOCK MAP AND WORDS SIGNED, Kain, 18 November 2026: "Yes, they're right" and "Yes, sign them"; written home by Chat at Chat's seat the same day)

One page, one instance, at `/access-all-areas/` (WordPress post 45036). Composed by Code with the `page-composition` skill and shown to Kain in Safari as 000__BLOCKS__Access_All_Areas_Page.html; his picks are PICKS.md, and the page's words are 000__COPY__Access_All_Areas_Page.md, all in the Access All Areas Page folder under Homepage + Commercial Design Prototypes. This section replaces DSRD 2 section 2.21's four blocks, whose four changes are all carried below (what the pass is, block 1; everything included, blocks 3 and 5; the cost against its parts, block 8; the purchase, blocks 1 and 8). The pass's positioning record, which the page reads from, is DSRD 4 section 1.7.1. Prices, plans and the checkout address are read from DSRD 4 sections 1.1 and 1.3 at build, never from here.

### 46.1 The job

**This page exists to get a visitor who is serious about Achology to buy the Access All Areas Pass.**

### 46.2 The reader's arrival state

| # | What is true on arrival | Basis |
|---|---|---|
| A1 | They already know Achology and are weighing its biggest step | **Assumption.** They arrive from the Pricing page, a course page's price block, the Academy page and the menu. The old pass page's searches were almost all for Achology by name (DSRD 4 section 1.7.1, component 4). Confirmed after launch from analytics |
| A2 | They want to know what they would own, and whether it is worth it | Evidenced: the pass's Help answers (posts 245, 225, 229, 341) are the questions people ask about it |
| A3 | Many read on a phone | **Assumption.** Confirmed after launch |

### 46.3 Page structure (top to bottom; this is also the phone order)

| # | Block | The change it carries, in the reader's voice | Built from |
|---|---|---|---|
| 1 | The Banner | "I know what this is: every Achology course and a year of membership, in one pass." | The signed banner (.pw-hero), the Access All Areas Pass picture (Pricing Page folder), two buttons: Get the Access All Areas Pass (to block 8) and See Every Course Inside (to block 3) |
| 2 | The Facts Strip | "I can see how big it is at a glance." | The Events page's strip, four facts: All 28 Courses, Seven Schools, 12 Months of Membership, Lifetime Access |
| 3 | Everything Inside | "I can see every course I would own, school by school." | The seven school artwork cards with their courses, as on the Pricing page |
| 4 | The Route to Master Achologist | "This is the fastest way to the highest title." | The five levels as the Accreditation page shows them (DSRD 4 section 9.1), each with a line on the courses the pass already includes |
| 5 | A Year Inside the Community | "I know what the 12 months of membership give me, every day." | The site's one heartbeat block (achology_heartbeat_block()), this page's words |
| 6 | Who It's For | "This is meant for someone like me." | **New block.** Four people from the positioning record, each a thought in their own words with one paragraph; its look comes as four whole options when it is designed |
| 7 | What Students Say | "I trust the teaching." | The course pages' Voices Wall, its figures from the figure register (DSRD 5) |
| 8 | The Price | "It's worth it, and I can pay in a way that suits me." | The course page's signed price card on Light Sand: $5,249 struck, $2,995, Pay In Full or three, six or twelve monthly payments, Due Today, Get the Access All Areas Pass, the 14-day guarantee |
| 9 | Questions | "Nothing is left worrying me." | achology_faq_block() on the S464 Light Sand standard, eight signed Help answers, each with a summary passed for this page |
| 10 | The Site Footer | The page ends on the pass, with no second offer. | The footer without the $7 band, as on the course pages |

### 46.4 The two closing tests

**Every block carries a named change:** yes, all ten. **Every change has a block:** yes. The pass's button repeats in the banner and on the price card, the same action each time, and no other exit is offered.

### 46.5 The rules the words keep

- **Only what is included** (Kain, 17 November 2026, DSRD 4 section 13). Block 6 names who the pass suits, never who it does not.
- **The saving is said one way only:** the pass costs less than its 28 courses and 12 months of membership bought separately (DSRD 4 section 1.2 fact 3).
- **"The fastest route to Master Achologist"** carries its evidence beside it: the pass includes every course all five levels ask for. Block 4's closing line says each level also asks for checked practice in the community, so no reader takes the pass for a level.
- **Every set of lines that shares a space runs the same rows** at the built width, measured with the site's font (the vault note on short lines that share one space). Code re-measures on the built page.

### 46.6 What is settled and what is open

**Settled:** the ten blocks and their order (Kain, 18 November 2026: "Yes, they're right"); the words, signed the same day (Kain: "Yes, sign them", on READING_PAGE__Access_All_Areas_Page_Words.html), held in 000__COPY__Access_All_Areas_Page.md. **Open:** block 6's look (four options); then the preview, block by block, measured against DSRD 7, and the theme build.

*No em or en dashes in this addition; checked before writing.*

### 46.7 Overtaken the same day: the pass page takes the school page's shape (Kain, 18 November 2026; written home by Chat, Session 478)

The ten-block map above is a source only. Shown the preview, Kain ruled it out and the school page's template in: "we just need to use the approved school page structure, except for the Achology Access All Areas Pass ... we can just use the same template and reframe the school template for the Access All Areas Pass product." "Claude, we don't need to reinvent the wheel here." (PICKS.md, Pick 3.)

**The blocks as built, top to bottom (the school page's, section 44, reframed):**
1. The Banner (the school banner).
2. What the Access All Areas Pass Teaches, With Who It Is For (the school's first block).
3. All 28 Courses Included Within the Pass (the school's courses block, each opening its panel on the right).
4. The Story of Modern Applied Psychology (the school's story, five chapters).
5. The six free tutorials from the Academy (the school's tutorials band).
6. The Achology Knowledge Tree, across every published workbook.
7. Practise What You Learn.
8. What Students Say About Studying at Achology.
9. The Access All Areas Pass and Payment Options, with the buy bar along the foot of the window.

**The words** are signed in the school shape (Kain, 18 November 2026: "Yes, sign them", on READING_PAGE__Access_All_Areas_Page_School_Shape.html) and held in 000__COPY__Access_All_Areas_Page.md; every line of the ten-block words that fits a school field is reused word for word. **The colours:** the page shares the school template and keeps the brand's orange (DSRD 7 section 2). **The page is signed and its record closed** (Kain, 20 November 2026, at 0.708.266: "This page is stunning ... Yep, I'm 100% happy to sign this off"; DSRD6_RECORD.md in the Access All Areas Page folder reads CLOSED).

*No em or en dashes in this addition; checked before writing.*

## 47. Membership Page Layout (BLOCK LIST SIGNED, then rebuilt block by block, Kain in Code's S537 sitting, 19 and 20 November 2026; written home by Chat, Session 478)

One page, at the membership address DSRD 1 holds. Composed by Code with the `page-composition` skill and research (RESEARCH__Membership_Page_S537.md), shown to Kain as BLOCKS__Membership_Page_S537.html; the words are WORDS__Membership_Page_S537.json; all three sit in the Membership Sales Page folder. The preview is built in the theme's previews/membership-page folder (build.py and memb.css).

### 47.1 The job

**Get a curious visitor to start their first month for $7.** The one action, "Start for $7", repeats in the banner, in the joining block and in the footer's $7 band. Left out on purpose: countdown timers, invented figures, and any list of what is not included (DSRD 4 section 13).

### 47.2 Page structure (top to bottom; this is also the phone order)

| # | Block | What it is, and Kain's ruling |
|---|---|---|
| 1 | The Banner | The school page's banner, reframed for membership ("Yes, switch", 19 November 2026: "membership's essentially a product page"). Kain's own Canva picture of members together (membership-banner.png, built as hero-memb at the school sizes), on the school banners' faint Academy building ("Yes, it's right", 0.708.259). |
| 2 | The First Block | The school page's What This School Teaches, With Who This School Is For, reframed for membership ("Yes, switch"). |
| 3 | Everything Achology Membership Includes | The Membership Bento ("Yes, build 1"): the seven features of DSRD 4 section 13 and the annual extra as tiles of different sizes. The cards take Words on the Pictures ("I like option number three, words on pictures") and The Watermark Wash ("The watermark wash please"): live sessions and networking are whole photographs with white words on a dark fall; the six small cards a warm fall with their icon large and faint; the annual card keeps its orange edge. Every title on one line and three full lines of text at 1270. Words signed: `includes_fitted` ("Yes, sign them"). |
| 4 | The Heartbeat | The Academy page's #academy-events band, cut whole, with its three facts and Join a Free Event This Week ("I want this block in the page. Do it now, please"; "Yes, it's right"). |
| 5 | A Week Inside the Achology Community | The Events page's weekly timetable, cut whole and run by events.js ("Yes, add it"). |
| 6 | From Your First Session to Master Achologist | The Full Ladder ("Yes, build it"): the six level badges rising in a row, four cards of one shape beneath, each naming the level it reaches. His rule for the cards: "2 full lines of heading ... 5 or 6 full lines of subheading. But just choose one or the other. You might as well use max": two heading lines over six text lines. Words signed: `takes_you_v2` ("Yes, sign them"). |
| 7 | Growth, Connection and a Business Built Here | The Quote Wall ("3 The quote wall please claude"): on the dark band, each quote on a pane in white under a large orange mark, headed by a phrase in the member's own words; quotes cut only by leaving words out, every gap an ellipsis, to eight full lines at 1270. Each member's level badge pinned to the photo's corner, the level on the overline row, the profile link a small icon beside the name. Words `members_v2`: not yet signed. |
| 8 | Choose How You Join | Monthly and annual side by side, terms beside each button, from the Pricing page's signed membership block. Being redesigned with Kain in Code's sitting (20 November 2026). |
| 9 | Practical Answers Before You Join | achology_faq_block() on the S464 Light Sand standard. Being redesigned with Kain in Code's sitting (20 November 2026). |
| 10 | The Site Footer | With its $7 band. |

### 47.3 The rules the blocks keep

- **Reuse before redesign.** Blocks 1, 2, 4 and 5 are other pages' signed blocks, cut whole; Kain: "It would make sense to not waste it or try and reinvent the wheel."
- **Cards that share a space run the same lines,** measured at 1270 with the site's font, and Kain's rule is to use the most room the card gives.
- **Only what is included** (DSRD 4 section 13), and every fact from its home.

### 47.4 What is settled and what is open

**Settled:** blocks 1 to 6 and their words (the page words signed 19 November 2026, "Yes, sign them", with `includes_fitted` and `takes_you_v2` signed since). **Open, with Code and Kain now:** block 7's words, blocks 8 and 9, then the page's record and the theme build.

*No em or en dashes in this addition; checked before writing.*

### 47.5 What was built after the block list, S543 to S553, 20 to 23 November 2026 (Code's theme sessions; written home by Chat, Session 480, from the ship briefs of those sessions)

This records what was built and what Kain signed. 47.2's order stands, and 47.4's open list is overtaken: the members block, the joining block and the questions block are built as below. The ten improvements Kain asked for in his whole-page review of 22 November are mapped, with their reach, in previews/membership-page/audit-s551/reach.html in the theme.

1. **The banner (0.708.307 to 0.708.323, Kain's "Yes, ship it"; subtitle "Yes, it's right").** The title reads Achology Membership and Subscription Plans. The price line and the figures line under it are gone. Behind the picture sits a quiet wall of 170 grey faces, the same count as the Academy banner and none repeated (28 real members from Canva, 142 AI faces), on computer widths only, with no movement and no names; it runs up under the breadcrumb row and is a little fainter. The subtitle, the button (Join for $7. Cancel Anytime.), the first block's heading (What Achology Membership Can Give You) and its line are Kain's own words, placed as given. The lone-word script no longer evens this subtitle; the school banners keep it. At 0.708.324 the what-is-Achology film in the first block has its own cover, the Zoom call of nine people faded right back with a line globe in front and the play button on top (Kain's brief; "Yes, it's right"), and What You Get in the questions block carries three answers, adding posts 350 (live events) and 342 (mentoring). The words are in WORDS__Membership_Page_S537.json.
2. **The Includes card's session length (0.708.353).** Asked in the main session, Kain answered in his own words, **"Groups Last Between 60-90 Mins."** The Unlimited Live Sessions card reads: "Join as many live sessions on Zoom as you like, Monday to Friday. Groups last between 60 and 90 minutes, each a discussion, a tutorial, a skills workshop or coaching practice, where you take part and try ideas." It is 38 words, and the page gate's entry for the card reads 38.
3. **Choose How You Join, Lifted on Dark (0.708.369 and 0.708.370, Kain's picks from round-join2.js option 3, round-gift.js option 1 and round-fire.js option 3, "Yes, build 3").** The block sits on the brand dark band with the plans as white cards lifting off it. The Annual card is crowned by an orange Gift Banner carrying the offer. The Pass card's neuron fires above the Monthly plan, a pathway runs from it into the gift banner, and each spark lands there and lights the card's ring; the orange haze behind the card is gone. Every line is Chat's signed plain words, placed word for word (ANSWER__Membership_Join_Block_Plain_Words_S551, and the 24-word lead of ANSWER__Membership_Join_Lead_25_Words_S551); the old gift lines are out of the card. The join prices stand at 42, as Kain chose them on the rendered round. On a phone: annual first, then monthly, then the list, with the neuron small in the corner and no path.
4. **The checkout foot (0.708.381, corrected at 0.708.383).** Each plan card closes on the signed checkout foot that every course and school buy card already carries: the lock, Secure Checkout, the Stripe badge and the five card marks, drawn unchanged from the Pass page's own stored data and seated inside the card's frame so every signed rule applies. Kain's rule behind it: "Why on earth are you designing brand new components when we already have components and standards already designed and set?" A component that exists is reused as it is, never redesigned. The Pricing page's Access All Areas Pass card and both membership plans take the same foot (0.708.395), and the foot's rules now have one home, checkout-foot.css (58 rules moved verbatim from course-page.css, proved identical on a course page, a school page, the Pass page, the Academy, Membership and the gift page at 1440, 1024 and 375). On Pricing the Pass card now stands about 90 taller than the school card beside it, left as designed because the grid aligns its cards to the top.
5. **From Your First Session to Master Achologist, The Progress Track (0.708.373; Kain: "The progress track is perfect.").** Of four rendered options (round-climb.js) he chose The Progress Track for the six member badges, then asked for no haze behind the nodes, a thinner line and bubbles graded in size and colour from left to right. The badges grow from 76 to 132 and start in grey. Beneath them sit six Achology bubbles, growing from 16 to 26 and shading from grey to orange, on a 2px line that stops short of each one. When the block scrolls into view the line fills, each bubble pulses as it is reached and its badge comes into colour, once. A step card lights its badge on hover and a badge its card. Without the script, or for a visitor who asks for less motion, the row simply stands lit. At 375 the badges stand one size (Master a step larger) and the track steps aside. No words changed.
6. **Band rhythm (0.708.392, improvement 7: "Every Block Changes Colour From the One Before").** The members block now stands on Light Sand, so the page's bands run white, sand, dark, sand, white, sand, dark, sand and no two neighbours share a colour. Its own top hairline is gone, since the change of ground marks the boundary, as on the school pages, and its figures strip turns white so it still reads as a panel. Every band keeps its 64 above and below. Scoped to /membership/ only.
7. **The section bar (0.708.394, improvement 1: "A Slim Guide That Follows You Down the Page").** The course pages' own section bar (course-page.css .snav and course-page.js, reused unchanged, as Kain ruled at S551) sits under the banner, sticks under the site header, marks the block in view, and a click glides to that block's heading, 24 under the bar. On a phone it scrolls sideways with the course bar's soft edges. Eight labels: Overview, Includes, Live Events, Your Week, Your Path, Reviews, Pricing, FAQs. Four are the course bar's own labels for the same jobs; the other four are the names in Kain's improvement map.
8. **The members block** (What Our Members Say About Achology Membership) is the one reviews block (DSRD 8 section 44), one row of three and no control.
9. **The questions block's hover arrow (0.708.393, improvement 10, part).** In the site's one questions block each question now ends on the site's text link arrow, which slides in as the question turns orange on a hover or a keyboard focus, keeping its place at rest so no line moves; under reduced motion it fades and does not slide. The questions were already 16 semibold in the heading face and the answers 14 regular in soft grey.
10. **Gate.** After these builds the page gate read 44 passed and 1 failed, the failure being rank-math (post 45034 never scored), which waits on Kain's one click.

*No em or en dashes in this addition; checked before writing.*

---

## 48. Six Day Free Lessons Page Layout (SIGNED on its rendered mock-up, Kain, 23 November 2026: "Yes, sign it"; written home by Chat, Session 481)

**What the page is for.** The private page a reader opens from their six free lessons emails, after signing up on a course page (six lessons) or a school page (six teachings). It hands over each day's video and gets out of the way, and lets the reader enrol at any point. One template, two fillings: the course filling at `{course page}/free-lessons/`, the school filling at `/academy/{school}/free-teachings/`. Kain's ruling of 18 November 2026 stands: "a page that says, yeah, here's your six ... Each day, over the next 6 days, one video unlocks ... it just needs to be really simple."

**The signed mock-up is the spec.** Folder: Six Day Free Lessons Page 23 November 2026, in the Project Delivery System folder. `page.html` (the page, read with the theme's own stylesheets; `?kind=course|school&day=1..6`), `Six Day Free Lessons Mockup (one file).html` (the copy Kain signed, every part inlined), and the two signed price blocks it carries. Its `<style id="new-parts">` block is everything new; every other part is a signed block's own.

**The blocks, top to bottom.**
1. **The course hero** (the course page's signed hero, section 24's block 1): the breadcrumb ending "Your Six Free Lessons" (school: "Your Six Free Teachings"); the title "Your Six Free Lessons from {course name}" (school: "Your Six Free Teachings from the {school name}"); in the proof line's place, six progress dots (filled for each open day) with "{n} of 6 open" and "{Lesson|Teaching} {n+1} opens {weekday}" (that last part dropped on day 6; on a phone it takes its own line and the separator dot goes); the line "A new lesson opens each day for six days, and every lesson you have opened stays here for you to watch again." (school: "A new teaching opens each day for six days, with its workbook, and every teaching you have opened stays here for you to watch again."); the primary button "Watch {Lesson|Teaching} {n} Now" to the player; the two promises "Nothing to Pay" and "Every {Lesson|Teaching} Stays Open"; the course or school picture on the right. On a phone the picture is not drawn, so the lesson comes first.
2. **The player band** (white): the overline "{Lesson|Teaching} {n} of 6", the lesson's name as the block heading (Como 24/600), the lesson's question as the Lead with Bar (school: "From the {school name}"), then the video full width of the 1104 column at 16:9, then a row: the lesson's summary on the left (school: one line on the workbook and the button "Open Your Workbook"), and on the right, behind a hairline, "Up Next" with the next lesson's number, name and weekday ("All Six Are Open" on day 6). On a phone the row stacks, "Up Next" under a hairline above it. The video plays only on our site (the Vimeo player, as the course page's).
3. **The six day track** (the course page's signed Week on a Line, dark band): overline "Your Six Free {Lessons|Teachings}", heading "Watch Each {Lesson|Teaching} as It Opens", line "Press any open day to watch it. A locked day shows the day it opens, and we email you as soon as it does." Three states: **playing** (the filled orange circle, name in white, "Playing now"); **open** (the ringed number, name underlined, its minutes; pressing it loads that lesson in the player and scrolls to it); **locked** (dimmed to half, a padlock in the circle, "Opens on {weekday}" in fire light). On a phone the label sits under the name. The foot line: "Then You Decide" with "Watch all six at your own pace, and then decide whether the {course|school} is right for you." No sign-up form here.
4. **What Students Say** (the signed reviews block, as on the course or school page).
5. **The signed pricing block** (BRIEF__Build_The_Signed_Pricing_Block_On_All_Four_Pages_S480): the course card for a course, the school card for a school. Its opening line on this page only: "You can enrol at any point, without waiting for all six {lessons|teachings}, and pay once or monthly with no interest." Its top padding is 0 here, so the gap from the reviews band is 64. The enrol button is never locked.
6. **The site footer** without the free lessons invitation (the reader has already signed up): the map and the Roundup.

**Text.** No line of one, two or three words at 1280 or 375: headings, the track's names and the Lead with Bar lines balance; paragraphs wrap pretty. Words checked against the banned and watched lists; no dash.

**Left out on purpose (Chat's calls, Kain may overturn):** What You Will Learn, to keep the page simple; the footer's free lessons invitation.

**How a day unlocks** stays as BRIEF__Six_Day_Free_Lessons_Page_Preview_18Nov sets it: a reader token made at sign-up, day 1 at sign-up and day n at (n-1) x 24 hours, the token remembered in the browser, no token showing day 1 open with the sign-up form in the track's place, and the old `/free-lessons/{n}/` addresses landing on that day.

*No em or en dashes in this addition; checked before writing.*
