DISPOSITION (Chat, S464, 11 November 2026): answered in FROM Chat RULING__Postbag_Rulings_For_The_Theme_Sessions_S464 section 1; copy mends and source homes carried as Chat's course page copy batch. Archived.

**For Chat. What this needs from you:** four rulings, in section 5: whether the five tests that fail on all 28 pages are recorded exceptions or copy for you to mend; the nine short line endings in section 3; whether the signed words go home to their two source homes; and how the course page's DSRD 6 record opens, since the gate cannot read a draft. Code, theme session S479, 11 November 2026. Answers BRIEF__Build_The_Signed_Course_Page_Copy_Into_All_28_Pages_S461.

# Status in the words The Harness requires

Changed, read back, deployed, and the scores read. Not "done" in Rule 6's sense: the course page has no DSRD 6 record yet (none in the Course Page folder; the machine gate cannot read a draft page, S472 item 4, still open), so the page is **built, gate open: the course page's DSRD 6 record**. Theme 0.707.935 on the build site (commit 0885e0f8, pushed; the deploy tool's three proofs passed). A page to open, signed in on the build site: the course 002 draft, https://achologytest.com/?page_id=33507&preview=true

# 1. What was placed

- **27 courses (002 to 028):** the hero sentence, the four What You Will Learn paragraphs and the Who This Course Is For paragraph, word for word from the signed copy. Course 001 keeps its signed text, as the brief says. Each was read back from the stored file and equals the signed text.
- **One mechanical change, named:** the signed file writes apostrophes straight; every apostrophe already on a course page is curly, so the page carries them curly (205 apostrophes). Nothing else in a sentence was touched, and no sentence was drafted or reworded.
- **All 28 pages, on the install, over WP-CLI:** the Rank Math search title, description and focus keyword, with the related phrases after the focus keyword in the same field as Rank Math's secondary keywords. Each of the three fields was read back from the install and equals the signed copy. On the built draft of 028 (checked) the browser tab, the sharing title, the sharing description and the Twitter description are the signed title and description, and the H1 stays the course name; on 002 the tab title is the signed one.
- **The register:** the 28 focus phrases are claimed in the keyword register (type page, the page's slug and address, 11 November 2026, S479); none clashed with a phrase already there.
- **Held, as the brief says:** question_mends, unplaced. The pages keep today's lesson questions until the one final question file arrives.
- **Not placed:** questions_people_ask (see section 4).

How it is built, so it can be run again: tools/course_copy_place.py places the words in the theme's course data (data/courses.json for the hero, which the hero, the Course schema description and a Knowledge Hub panel's course line all read; data/course-page for the paragraphs and the Who note), sets the Rank Math fields, and claims the register rows. It is safe to run twice. **It is also the thing to run after any regeneration:** tools/course_page_data.py rebuilds the stored pages from the Course Page Copy folder, and course_rows.py rebuilds the hero from DSRD 2 section 2.6; both homes still hold the old words, so a regeneration brings them back until the signed words are written there (section 5, item 3).

# 2. The 28 Rank Math scores

Read off each built draft page, in the page's own editor, saving nothing. Bar 90, target 95 (DSRD 6 section 5 item 11).

| Course | Score | Focus phrase |
|---|---|---|
| 001 | 71 | online psychology course |
| 002 | 71 | nlp for beginners |
| 003 | 73 | nlp practitioner course |
| 004 | 71 | nlp master practitioner course |
| 005 | 72 | mindset course |
| 006 | 71 | cbt course online |
| 007 | 84 | cbt practitioner course |
| 008 | 80 | cognitive behavioural therapy course |
| 009 | 73 | life coaching course |
| 010 | 71 | life coach training |
| 011 | 71 | egan skilled helper |
| 012 | 71 | helping skills training |
| 013 | 73 | hypnotherapy course |
| 014 | 73 | counselling skills course |
| 015 | 73 | mindfulness practitioner course |
| 016 | 71 | learn mindfulness online |
| 017 | 73 | mindful leadership course |
| 018 | 73 | mental health course |
| 019 | 73 | assertiveness course |
| 020 | 73 | self esteem course |
| 021 | 71 | emotional intelligence course |
| 022 | 71 | life purpose course |
| 023 | 73 | goal setting course |
| 024 | 73 | communication skills course |
| 025 | 73 | self discipline course |
| 026 | 73 | mental resilience course |
| 027 | 72 | marriage course |
| 028 | 71 | start a business course |

**None reaches 90; two reach 80 (007 at 84, 008 at 80).** Nothing on any page was changed to chase a number.

**The same five tests fail on every page, which is why the scores sit within 13 points of each other:**
- the focus phrase is not in the page's opening words (keywordInContent, 0 of 3, all 28);
- the focus phrase is in no subheading (keywordInSubheadings, 0 of 3, 27 of 28; course 027 passes);
- the length test (lengthContent), 5 of 8 on 26 pages and 4 of 8 on 005 and 027, from 1,991 to 2,292 words;
- no link to another site (linksHasExternals, 0 of 4, all 28);
- the links test linksNotAllExternals, 0 of 2, all 28.

**Where each goes (Rank Math skill, Part B step 4):** the first two are copy and keyword, Chat's; the length test is the same shape Kain set aside on Certification at S464; the two link tests both need a link to another site, and a course page carries none, a decision for you and Kain. Code changes none of them without a ruling.

**How a draft's score was read, and why it differs from the usual tool.** The theme's analyser feed (rank-math-feed.php, line 53) returns nothing for a post that is not published, so on a draft the analyser sees an empty page and tools/score_run.py reads a flat 48. I read three of the 28 that way (001, 002, 003) to confirm: all 48, the score of nothing, not a page's score. The reading above is the same analyser fed the page's real words: the draft is fetched signed in, its words are cut out by the theme's own function (achology_rank_math_main_content, over SSH), and they are appended through the same rank_math_content filter the feed uses. tools/draft_score_read.py does it and saves nothing (every write route is refused in the browser). **The control:** on two published pages the feed does work on, Accreditation and Certification, this method with the feed removed reads 88 and 86 with the same failing tests as the standard reading of the same pages (88 and 86). Changing the feed to read drafts for a signed-in admin would be a theme change; I did not make it.

# 3. Paragraphs that end on a line of one, two or three words

Measured in WebKit, the engine nearest Kain's Safari, on every built draft (28 pages, six pieces of text each, three widths), by the position of each word on its line. Computer is 1268, tablet 834, phone 390. Paragraph 1 to 4 are the four description paragraphs in order; the Who paragraph ends on four or more words everywhere.

**Computer (1268):**
- 005, paragraph 1, ends "to grow." (2 words)
- 006, paragraph 1, ends "and behaviour yourself." (3); paragraph 2, ends "in the family." (3)
- 012, paragraph 1, ends "problems or others'." (3)
- 018, paragraph 2, ends "default thinking styles." (3)
- 021, paragraph 1, ends "everyday relationships." (2)

**Tablet (834), not already listed:** 006 paragraph 1 "behaviour yourself." (2); 016 paragraph 1 "imperfections included." (2); 018 paragraph 2 "thinking styles." (2); 021 paragraph 1 "everyday relationships." (2, as at computer).

**Phone (390):** 012 paragraph 3 "integrated throughout." (2); 016 paragraph 1 "and imperfections included." (3); 018 paragraph 2 "default thinking styles." (3); 025 paragraph 3 "flexibility and growth." (3).

**The hero sentence at phone width** (a sentence, not a paragraph, listed because it is the same fault): 001 "they do." (2, 001's own signed sentence); 002 "personal mastery asks." (3); 006 "behaviour for yourself." (3); 014 "different from you." (3); 020 "builds authentic self-esteem." (3); 022 "make serve them." (3); 024 "trust." (1); 026 "mentally strong person." (3). No hero ends on a short line at computer or tablet width.

The page's own script already ties the last two words of a paragraph together, so these are the worst cases the theme can leave; mending them is a copy change, yours.

# 4. Any field the theme could not take

- **None of the fields in the brief needed a theme change.** Hero, four paragraphs, Who paragraph, search title, description, focus keyword and related phrases all went into the theme's course data or the page's own Rank Math fields.
- **questions_people_ask has no place to go.** The Course schema the theme writes carries a name, description, provider, rating, offer and curriculum, and no field for questions; the page's nine buyer questions are its signed FAQ cards. Putting the researched questions into the page's machine-readable lines would be a new theme field (Opus). Tell me if you want it; I have not built it.
- **Related phrases** are held as Rank Math secondary keywords. They affect only Rank Math's own tests for those phrases; the score above is the focus phrase's.

# 5. What Code needs from you

1. Are the five failing tests on every page recorded exceptions (as the length test on Certification), or copy and structure you will mend? Code changes nothing until you say which.
2. The nine paragraphs in section 3 (on seven pages, fourteen cases across the three widths), and any hero sentence you want mended, changed in the copy file, then a Chat RULING and Code runs course_copy_place.py again.
3. Write the signed words to their two source homes (the Course Descriptions copy file in the Course Page Copy folder, and DSRD 2 section 2.6's hero table), so a regeneration cannot bring the old words back.
4. The course page's DSRD 6 record: the gate cannot read a draft. Say which: the pages published, or the gate taught to read signed in (page_gate.py would reuse score_run.py's session). This is still the S472 question.

OWED BACK: the four answers of section 5, to FROM Chat, for the theme session.

DOCUMENT TYPE: DONE

*No em or en dashes in this file; checked before writing.*
