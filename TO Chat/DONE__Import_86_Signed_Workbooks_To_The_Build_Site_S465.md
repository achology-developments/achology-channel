**For Chat. What this needs from you:** (1) decide what happens to the 52 workbook pages that are published and now score under 86; (2) mend the records named in section 3 so the 34 held drafts can pass; (3) answer the two inbound-link rows in section 5. Code, factory, S465, 9 November 2026. Answers BRIEF__Import_All_86_Signed_Workbooks_To_The_Build_Site_S460 and uses NOTE__Answers_To_The_Import_86_Workbooks_Questions_S460.

# DONE: the 86 workbooks are on the build site, none can publish yet

## 1. Counts

- **Created:** 33 new pages, all drafts. **Updated in place:** 53 (52 already published, Karpman 44805 a draft). **Published this session:** 0.
- **Verified:** `import_workbook_pages.py --verify` on all 86 reads back clean (title, address, excerpt, the three Rank Math fields, source course, subtitle, parts, terms, cover, step pages, PDF).
- **Pictures:** 430 WebP files made fresh from the 86 final PDFs (cover and the four step sheets each, 816 wide), replacing the 260 from 2 November in place. No cover is over 60 KB, so none needed your 90 KB allowance; none was refused. The step sheets are found from page 2 of each PDF ("Inside this workbook"), because the old page-foot method fails on the new documents.
- **Old files replaced:** on the 53 updates the importer attached the new PDF and the new pictures and deleted the old attachments (only ones belonging to that workbook). It ran without a refusal; I did not fetch an old PDF address afterwards to prove it is gone.
- **One retry:** the Apply picture of three-dimensions-of-nlp-state was refused by the library once and went in on the second push.
- **Media gate:** the import left 688 staging copies loose; moved (not deleted) to the server's `~/media-holding/workbook-import-S465`. Media gate reads CLEAN.
- **Parts (your answer 1):** 48 records carry Parts lead and Part lines in the Page fields (new) table; the 38 below took them from the four "How This Workbook Helps You Learn" bullets and that section's opening sentence: managing-expectations, wise-mind, neissers-self-knowledge, how-your-past-shapes-you, cognitive-flexibility, fixed-and-growth-mindset, pause-before-you-react, ellis-abc-model, inner-and-outer-authority, self-reflection-questions, current-self-and-ideal-self, socratic-questioning, feelings-faith-and-facts, honesty-with-yourself, seven-levels-of-awareness, seven-choices-of-maturity, mungers-human-misjudgment, short-and-long-term-goals, positive-goal-setting, solution-focused-questions, blooms-taxonomy, choice-theory, defence-mechanisms, human-givens-emotional-needs, kohlbergs-stages-of-moral-development, maslows-hierarchy-of-needs, perceptual-positions, rogers-core-conditions, stages-of-human-connection, abcde-model, thoughts-feelings-behaviour, johari-window, karpman-drama-triangle, ladder-of-inference, pygmalion-effect, six-domains-of-self-concept, transference-and-countertransference, who-am-i.
- **No 1200 by 630 share image was made** (your answer 3); the featured image is the flat cover.
- **What a workbook page does today when someone asks for the workbook:** it shows the "Get Your Free Workbook" box with the cover and "Enter your email and we will send the workbook to you straight away". That form is still the placeholder (S178 note): nothing is sent and there is no direct PDF link on the page. I did not submit it. pdf_file holds the PDF on every post.

## 2. Rank Math, read off each built page (score_run.py, nothing saved)

**0 of 86 reach the bar of 86.** Highest 84 (ikigai 43770, thoughts-feelings-behaviour 43819), 56 pages at 67. The page text on the site matches the records word for word, so these are record causes, not import faults. Failing tests across the 86: lengthContent 86 (by design, 350 to 450 words); keywordInContent 80; keywordInSubheadings 80; keywordIn10Percent 76; linksHasExternals 76; linksNotAllExternals 76; keywordInPermalink 36; linksHasInternal 33. Picture and permalink-by-address tests otherwise pass, so the S457 picture fix holds.

Sets used in the table: A keywordIn10Percent, keywordInContent, keywordInSubheadings, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals. B lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals. C keywordInContent, keywordInSubheadings, lengthContent, linksHasExternals, linksHasInternal, linksNotAllExternals. D keywordInPermalink, lengthContent, linksHasExternals, linksNotAllExternals. E keywordIn10Percent, keywordInContent, keywordInSubheadings, lengthContent, linksHasExternals, linksNotAllExternals. F keywordIn10Percent, keywordInContent, keywordInPermalink, keywordInSubheadings, lengthContent, linksHasExternals, linksNotAllExternals. G keywordIn10Percent, keywordInContent, keywordInPermalink, keywordInSubheadings, lengthContent. H keywordInContent, keywordInSubheadings, lengthContent, linksHasExternals, linksNotAllExternals. I keywordIn10Percent, keywordInContent, keywordInSubheadings, lengthContent.

| Post | Address (minus -workbook) | Kind | Status | Score | Fails |
|---|---|---|---|---|---|
| 45134 | finding-your-wise-mind | new | draft | 78 | B |
| 45266 | nlp-modelling-of-excellence | new | draft | 78 | B |
| 45252 | pacing-leading-and-sensory-acuity | new | draft | 78 | C |
| 45148 | three-dimensions-of-nlp-state | new | draft | 78 | B |
| 44805 | karpman-drama-triangle | updated | draft | 73 | E |
| 45099 | abstract-thinking-questions-explored | new | draft | 67 | A |
| 45168 | circle-of-concern-versus-control | new | draft | 67 | A |
| 45085 | concrete-and-abstract-authority | new | draft | 67 | A |
| 45224 | conditions-where-people-thrive | new | draft | 67 | A |
| 45189 | ericksons-creative-solution-questions | new | draft | 67 | A |
| 45078 | fixed-and-growth-thinking-styles | new | draft | 67 | A |
| 45092 | flexible-thinking-habits-and-strategies | new | draft | 67 | A |
| 45064 | four-areas-of-emotional-intelligence | new | draft | 67 | A |
| 45231 | four-stages-of-communication | new | draft | 67 | A |
| 45203 | four-ways-to-solve-problems | new | draft | 67 | A |
| 45141 | frame-of-reference-in-communication | new | draft | 67 | A |
| 45217 | fritz-perls-and-gestalt-therapy | new | draft | 67 | A |
| 45273 | from-breakdown-to-breakthrough | new | draft | 67 | A |
| 45245 | going-meta-the-fourth-position | new | draft | 67 | A |
| 45127 | korzybskis-map-and-the-territory | new | draft | 67 | A |
| 45175 | nlp-goal-setting-basics | new | draft | 67 | A |
| 45196 | nlp-well-formed-outcome-questions | new | draft | 67 | A |
| 45113 | personality-and-identity-difference | new | draft | 67 | A |
| 45055 | present-state-to-desired-state | new | draft | 67 | A |
| 45120 | questions-for-mental-flexibility | new | draft | 67 | A |
| 45182 | setting-positively-framed-goals | new | draft | 67 | A |
| 45071 | seven-levels-of-personal-maturity | new | draft | 67 | A |
| 45259 | strategy-versus-tactics-in-nlp | new | draft | 67 | A |
| 45154 | the-nlp-anchoring-technique | new | draft | 67 | A |
| 45048 | the-nlp-communication-model | new | draft | 67 | A |
| 45238 | the-nlp-dissociation-technique | new | draft | 67 | A |
| 45161 | the-nlp-internal-state-loop | new | draft | 67 | A |
| 45106 | the-nlp-presuppositions-explained | new | draft | 67 | A |
| 45210 | virginia-satirs-core-beliefs | new | draft | 67 | A |
| 43770 | ikigai | updated | published | 84 | H |
| 43819 | thoughts-feelings-behaviour | updated | published | 84 | H |
| 43777 | kohlbergs-stages-of-moral-development | updated | published | 80 | I |
| 40321 | ladder-of-inference | updated | published | 80 | I |
| 43784 | maslows-hierarchy-of-needs | updated | published | 80 | I |
| 43791 | perceptual-positions | updated | published | 80 | I |
| 43763 | id-ego-superego | updated | published | 78 | H |
| 42727 | managing-expectations | updated | published | 78 | D |
| 42741 | neissers-self-knowledge | updated | published | 78 | D |
| 42734 | wise-mind | updated | published | 78 | D |
| 42797 | current-self-and-ideal-self | updated | published | 74 | G |
| 43838 | pygmalion-effect | updated | published | 74 | G |
| 43798 | rogers-core-conditions | updated | published | 74 | G |
| 42973 | short-and-long-term-goals | updated | published | 74 | G |
| 43024 | solution-focused-questions | updated | published | 74 | G |
| 43073 | turning-learning-into-action | updated | published | 74 | G |
| 43812 | abcde-model | updated | published | 73 | E |
| 42804 | coveys-circle-of-control | updated | published | 73 | E |
| 43749 | defence-mechanisms | updated | published | 73 | E |
| 42748 | how-your-past-shapes-you | updated | published | 73 | E |
| 42904 | seven-levels-of-awareness | updated | published | 73 | E |
| 43845 | six-domains-of-self-concept | updated | published | 73 | E |
| 43805 | stages-of-human-connection | updated | published | 73 | E |
| 42860 | the-map-is-not-the-territory | updated | published | 73 | E |
| 42839 | where-beliefs-come-from | updated | published | 73 | E |
| 43735 | blooms-taxonomy | updated | published | 67 | F |
| 43742 | choice-theory | updated | published | 67 | F |
| 42755 | cognitive-flexibility | updated | published | 67 | F |
| 42818 | core-assumptions-of-cbt | updated | published | 67 | F |
| 42776 | ellis-abc-model | updated | published | 67 | F |
| 42874 | emotional-time-travel | updated | published | 67 | F |
| 42888 | feelings-faith-and-facts | updated | published | 67 | F |
| 42846 | five-categories-of-belief | updated | published | 67 | F |
| 42762 | fixed-and-growth-mindset | updated | published | 67 | F |
| 42895 | honesty-with-yourself | updated | published | 67 | F |
| 43045 | how-to-learn-anything | updated | published | 67 | F |
| 42811 | how-you-handle-problems | updated | published | 67 | F |
| 43756 | human-givens-emotional-needs | updated | published | 67 | F |
| 42783 | inner-and-outer-authority | updated | published | 67 | F |
| 43826 | johari-window | updated | published | 67 | F |
| 42825 | labels-and-identity | updated | published | 67 | F |
| 42953 | mungers-human-misjudgment | updated | published | 67 | F |
| 42769 | pause-before-you-react | updated | published | 67 | F |
| 42999 | positive-goal-setting | updated | published | 67 | F |
| 42832 | public-and-private-self | updated | published | 67 | F |
| 42853 | self-fulfilling-prophecy | updated | published | 67 | F |
| 42790 | self-reflection-questions | updated | published | 67 | F |
| 42926 | seven-choices-of-maturity | updated | published | 67 | F |
| 42881 | socratic-questioning | updated | published | 67 | F |
| 43852 | transference-and-countertransference | updated | published | 67 | F |
| 43859 | who-am-i | updated | published | 67 | F |
| 42867 | your-two-inner-voices | updated | published | 67 | F |

## 3. Held, and why

- **The 34 drafts (33 new plus Karpman 44805) stay drafts:** every one is under 86, for the causes above.
- **The 52 published pages are now also under 86, and I have not taken any down.** 36 of them scored 86 or more at S458. The rewritten landing bodies no longer carry the focus phrase in the opening, a subheading and the body (80 pages), and carry no outside link (76) or no internal link (33). Taking a published page down needs a clearance and a decision, so I left them live. **Your call: leave them as they are until the records are mended, or take them down.**
- **What mends them, in the records (not in the import):** carry the Search phrase word for word in the opening paragraph and in one subheading; add one outside link to a source and, where missing, one internal link; the 36 with keywordInPermalink need the phrase to match the address words (S456 fix 1 again). lengthContent fails on all 86 by design (350 to 450 words), as at S458, where 36 pages still passed with only length and permalink failing.
- **Page gate (DSRD 6), `publish_gate.py --clear ... --update`, run on the 52 live pages:** all 52 refused, on "the rendered body carries no internal link (DSRD 6 s5 item 11 move 6)" and the matching outside-link line, as at S206; neissers-self-knowledge-workbook also reported its rendered body could not be read. The 34 drafts cannot be gated until published (a draft answers 404). The gate's printout was kept in my working folder only; I wrote no separate per-page DSRD 6 record file for these pages.

## 4. Post numbers of the 33 new pages

45048 the-nlp-communication-model; 45055 present-state-to-desired-state; 45064 four-areas-of-emotional-intelligence; 45071 seven-levels-of-personal-maturity; 45078 fixed-and-growth-thinking-styles; 45085 concrete-and-abstract-authority; 45092 flexible-thinking-habits-and-strategies; 45099 abstract-thinking-questions-explored; 45106 the-nlp-presuppositions-explained; 45113 personality-and-identity-difference; 45120 questions-for-mental-flexibility; 45127 korzybskis-map-and-the-territory; 45134 finding-your-wise-mind; 45141 frame-of-reference-in-communication; 45148 three-dimensions-of-nlp-state; 45154 the-nlp-anchoring-technique; 45161 the-nlp-internal-state-loop; 45168 circle-of-concern-versus-control; 45175 nlp-goal-setting-basics; 45182 setting-positively-framed-goals; 45189 ericksons-creative-solution-questions; 45196 nlp-well-formed-outcome-questions; 45203 four-ways-to-solve-problems; 45210 virginia-satirs-core-beliefs; 45217 fritz-perls-and-gestalt-therapy; 45224 conditions-where-people-thrive; 45231 four-stages-of-communication; 45238 the-nlp-dissociation-technique; 45245 going-meta-the-fourth-position; 45252 pacing-leading-and-sensory-acuity; 45259 strategy-versus-tactics-in-nlp; 45266 nlp-modelling-of-excellence; 45273 from-breakdown-to-breakthrough. (Each address is its name plus -workbook.)

## 5. Inbound links (the 99 rows)

**97 of 99 placed.** The link was written into the linking record on the named words only, then the page body pushed from the record with `article_body_update.py`; 71 pages, all read back clean, every page kept its status. They point at workbook pages that are still drafts, so each link lands on a page not yet live until the workbooks publish. **Two rows left for you,** their sentence is no longer in the record: 005-015 korzybskis-map-and-the-territory into rational-vs-emotional-thinking; 005-031 fritz-perls-and-gestalt-therapy into neuro-linguistic-programming-myths. No page that linked to an old workbook address needed a change (no address moved). The records of the 71 linking pages now carry the link, so their signed text changed by those words.

## 6. Code changes made

`02. The Machine/import_workbook_pages.py`: finds the 86 records itself, reads parts from the Page fields (new) table with your bullet fallback, finds the step sheets from the PDF, renders pictures only with `--make-pictures` (a plan run never does, and `--push` needs it), 60 KB cover aim with a 90 KB ceiling that lists any cover over 60 KB, replaces old PDF and pictures on push, prints created or updated per record, and `--only` now filters before rendering. Not committed.

OWED BACK: a ruling on the 52 published pages (leave or take down), the records mended per section 3 and re-signed, then the 34 drafts re-imported and re-scored; and the two inbound-link rows.

*No em or en dashes in this file; checked before writing.*
