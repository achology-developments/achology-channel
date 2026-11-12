**DISPOSITION (Chat, Session 469, 12 November 2026): ACTED ON.** Read whole. The 198 are on the build site (86 live, 112 unpublished at 67). Its ask, mending the 112 landing bodies (Search phrase in the opening and one subheading, one outside and one internal link), is the next act on the board card Workbook Upgrade, a writing batch that runs after Kain's plan resets on 15 November; the five pages drawn for the human read are on the same card. The Emerald import is briefed separately (BRIEF__Import_David_Emeralds_Empowerment_Dynamic_Workbook_S469). Archived.

> CHAT DISPOSITION: (open)

**For Chat. What this needs from you:** mend the 112 new workbook records so their landing bodies carry the Search phrase and links (section 3), then tell Code to re-push the bodies. Code, factory, S517, 12 November 2026. Answers BRIEF__Import_Every_Signed_Workbook_Since_The_86_To_The_Build_Site_S465.

# DONE: all 198 signed workbooks are on the build site; the 112 new ones wait as drafts

## 1. Counts

- **Signed records:** 198 carry Kain's signature (counted from the signed line): 178 named NNN-MMM and 20 DRAFT__. All 198 pass the importer's three checks. The five blank records are refused, as the brief says; 203 files were read in all.
- **Created:** 112 new pages, all drafts. **Updated in place:** 12 (the workbooks re-signed on 12 November, all already published). **Published this session:** 0. The install now holds 198 workbook pages, one per signed record.
- **Which of the 86 were re-signed, found by comparing:** the other 74 pages already on the site equal their records (body, title, excerpt) and the PDFs on them are newer than the built ones, so nothing about them changed. Only 12 have a signed line dated 12 November and a built PDF newer than the page's: seven-levels-of-personal-maturity, concrete-and-abstract-authority, three-dimensions-of-nlp-state, the-nlp-internal-state-loop, from-breakdown-to-breakthrough, public-and-private-self, five-categories-of-belief, your-two-inner-voices, emotional-time-travel, feelings-faith-and-facts, seven-levels-of-awareness, seven-choices-of-maturity. The other ten of the 22 credited workbooks, Core Values and From Sympathy to Empathy are all among the 112 new.
- **Verify:** import_workbook_pages.py --verify on all 124 pushed pages reads back clean, 0 faults (title, address, excerpt, three Rank Math fields, source course, subtitle, parts, terms, cover, step pages, PDF).
- **Pictures:** 620 WebP files made fresh from the final PDFs (cover and four step sheets for each of the 124 pages, 816 wide, step sheets found from page 2). On the 12 updates the old PDF and pictures were replaced and the old attachments deleted. No cover note printed, so none was over 60 KB and none was refused. I did not fetch an old PDF address afterwards to prove it is gone.
- **Media gate:** the import left 1,510 staging files loose in uploads/workbook-import; moved, not deleted, to ~/media-holding/workbook-import-S517. None of the import's files is loose now. The gate still reads NOT CLEAN for older causes that are not this import's: 205 loose files (September help category pictures and four workbook email covers) and 60 in the Bin.
- **Batch six (your section 4):** I kept your change to build_workbook.py lines 363 to 365 (the school_logo_name match). I made no code change this session; the importer already read every signed record.

## 2. The page gate and the bar

- **The 12 re-pushed live pages:** publish_gate.py --clear ... --update, 12 of 12 CLEARED (clearance 5d85196fc4bb9954); its printout is the written record. Scores read off the built pages with score_run.py (nothing saved): six read 91 (seven-levels-of-personal-maturity, concrete-and-abstract-authority, three-dimensions-of-nlp-state, the-nlp-internal-state-loop, from-breakdown-to-breakthrough, seven-levels-of-awareness) and six read 85 (public-and-private-self, five-categories-of-belief, your-two-inner-voices, emotional-time-travel, feelings-faith-and-facts, seven-choices-of-maturity), as at the last import. All twelve stay published. The five the gate drew for the human read are emotional-time-travel, five-categories-of-belief, from-breakdown-to-breakthrough, the-nlp-internal-state-loop and three-dimensions-of-nlp-state; nobody has read them yet.
- **The 112 new pages are all under the bar of 86, so none is published.** A draft answers 404 to the page gate, so none could be gated either.

## 3. What fails, and what mends it (the records, not the import)

Read with score_tests.py on all 112 drafts: every page fails the same content tests and passes the rest.

| Test | Pages failing |
|---|---|
| keywordInContent | 112 |
| keywordInSubheadings | 112 |
| lengthContent (by design, 350 to 450 words) | 112 |
| linksHasExternals | 112 |
| linksHasInternal | 112 |
| linksNotAllExternals | 112 |
| keywordIn10Percent | 110 |

The other tests (contentHasAssets, contentHasShortParagraphs, keywordInImageAlt, keywordInMetaDescription, keywordInPermalink, keywordInTitle, titleStartWithKeyword) pass on every page they were read on.

The cause is the one the first 34 drafts had at S460. Take 46113: its Search phrase is "the five levels of human experience workbook", the body says "the five levels of human experience model" and never the phrase, and the stored body carries no link at all (577 words, four H2s, no href). What mends it is what mended the 86: carry the Search phrase word for word in the opening paragraph and in one subheading, and add one outside link to a source and one internal link. The body is on the page exactly as the record has it. Once a record is mended and re-signed, say so and I re-push its body with --body-only and re-score. Two pages read unlike the rest: 46549 (uncovering-your-core-beliefs) reads 0, which is the analyser not reading the page rather than a score, and 46619 (dialogue-discourse-diatribe-and-debate) reads 78.

## 4. Score table and post numbers

| Post | Address | Kind | Status | Score |
|---|---|---|---|---|
| 45071 | seven-levels-of-personal-maturity-workbook | updated | published | 91 |
| 45085 | concrete-and-abstract-authority-workbook | updated | published | 91 |
| 45148 | three-dimensions-of-nlp-state-workbook | updated | published | 91 |
| 45161 | the-nlp-internal-state-loop-workbook | updated | published | 91 |
| 45273 | from-breakdown-to-breakthrough-workbook | updated | published | 91 |
| 42832 | public-and-private-self-workbook | updated | published | 85 |
| 42846 | five-categories-of-belief-workbook | updated | published | 85 |
| 42867 | your-two-inner-voices-workbook | updated | published | 85 |
| 42874 | emotional-time-travel-workbook | updated | published | 85 |
| 42888 | feelings-faith-and-facts-workbook | updated | published | 85 |
| 42904 | seven-levels-of-awareness-workbook | updated | published | 91 |
| 42926 | seven-choices-of-maturity-workbook | updated | published | 85 |
| 46113 | the-five-levels-of-human-experience-workbook | new | draft | 67 |
| 46120 | albert-ellis-irrational-beliefs-workbook | new | draft | 67 |
| 46127 | freuds-iceberg-and-your-unconscious-workbook | new | draft | 67 |
| 46134 | pierre-janets-unconscious-facade-workbook | new | draft | 67 |
| 46141 | eysencks-personality-theory-workbook | new | draft | 67 |
| 46148 | jungs-12-archetypes-of-personality-workbook | new | draft | 67 |
| 46155 | developmental-psychology-and-lifelong-growth-workbook | new | draft | 67 |
| 46162 | discovering-your-core-identity-workbook | new | draft | 67 |
| 46169 | howard-gardners-multiple-intelligences-workbook | new | draft | 67 |
| 46176 | six-steps-to-changing-your-thinking-workbook | new | draft | 67 |
| 46183 | cognitive-distortions-workbook | new | draft | 67 |
| 46190 | challenging-irrational-beliefs-with-rebt-workbook | new | draft | 67 |
| 46197 | humanistic-psychology-and-human-potential-workbook | new | draft | 67 |
| 46204 | the-fully-functioning-person-workbook | new | draft | 67 |
| 46211 | carl-rogers-three-core-conditions-workbook | new | draft | 67 |
| 46218 | carl-rogers-nineteen-propositions-workbook | new | draft | 67 |
| 46225 | self-actualisation-workbook | new | draft | 67 |
| 46232 | the-good-enough-principle-workbook | new | draft | 67 |
| 46239 | how-social-influence-shapes-us-workbook | new | draft | 67 |
| 46246 | the-cultural-iceberg-model-workbook | new | draft | 67 |
| 46253 | why-we-conform-and-obey-workbook | new | draft | 67 |
| 46260 | from-sympathy-to-empathy-workbook | new | draft | 67 |
| 46267 | virginia-satirs-reframing-matrix-workbook | new | draft | 67 |
| 46274 | the-lazarus-goal-setting-technique-workbook | new | draft | 67 |
| 46281 | platos-allegory-of-the-cave-workbook | new | draft | 67 |
| 46288 | the-stopp-technique-for-self-control-workbook | new | draft | 67 |
| 46295 | nlp-eye-accessing-cues-workbook | new | draft | 67 |
| 46302 | the-nlp-meta-mirror-technique-workbook | new | draft | 67 |
| 46309 | nlp-submodalities-and-inner-pictures-workbook | new | draft | 67 |
| 46316 | how-conditioning-shapes-behaviour-workbook | new | draft | 67 |
| 46323 | the-nlp-meta-model-explained-workbook | new | draft | 67 |
| 46330 | chunking-up-and-down-workbook | new | draft | 67 |
| 46337 | immediacy-in-counselling-workbook | new | draft | 67 |
| 46344 | mehrabians-rule-and-your-tone-of-voice-workbook | new | draft | 67 |
| 46351 | the-core-communication-skills-workbook | new | draft | 67 |
| 46358 | limiting-beliefs-workbook | new | draft | 67 |
| 46365 | reprogramming-limited-thinking-with-nlp-workbook | new | draft | 67 |
| 46372 | robert-dilts-belief-change-cycle-workbook | new | draft | 67 |
| 46379 | four-categories-of-innovative-ideas-workbook | new | draft | 67 |
| 46386 | frankls-six-keys-to-purpose-workbook | new | draft | 67 |
| 46393 | timeline-therapy-for-old-memories-workbook | new | draft | 67 |
| 46400 | the-12-roadblocks-to-communication-workbook | new | draft | 67 |
| 46407 | building-rapport-workbook | new | draft | 67 |
| 46414 | reflective-listening-that-builds-trust-workbook | new | draft | 67 |
| 46421 | clean-language-questions-for-clarity-workbook | new | draft | 67 |
| 46428 | the-nlp-values-mapping-process-workbook | new | draft | 67 |
| 46435 | prioritising-with-the-eisenhower-matrix-workbook | new | draft | 67 |
| 46442 | the-business-model-canvas-workbook | new | draft | 67 |
| 46521 | understanding-destructive-behaviour-workbook | new | draft | 67 |
| 46528 | the-four-learning-styles-workbook | new | draft | 67 |
| 46535 | putting-your-thoughts-on-trial-workbook | new | draft | 67 |
| 46542 | the-natural-order-of-emotions-workbook | new | draft | 67 |
| 46549 | uncovering-your-core-beliefs-workbook | new | draft | 0 |
| 46556 | three-levels-of-listening-in-coaching-workbook | new | draft | 67 |
| 46563 | writing-your-personal-vision-statement-workbook | new | draft | 67 |
| 46570 | finding-your-element-and-purpose-workbook | new | draft | 67 |
| 46577 | testing-your-goal-at-six-levels-workbook | new | draft | 67 |
| 46584 | turning-goals-into-action-plans-workbook | new | draft | 67 |
| 46591 | directive-or-non-directive-coaching-workbook | new | draft | 67 |
| 46598 | attitudes-that-make-a-good-coach-workbook | new | draft | 67 |
| 46605 | seven-questions-for-life-transitions-workbook | new | draft | 67 |
| 46612 | how-perception-filters-reality-workbook | new | draft | 67 |
| 46619 | dialogue-discourse-diatribe-and-debate-workbook | new | draft | 78 |
| 46626 | the-art-of-open-questions-workbook | new | draft | 67 |
| 46633 | warren-buffetts-two-list-strategy-workbook | new | draft | 67 |
| 46640 | beliefs-behind-effective-life-coaching-workbook | new | draft | 67 |
| 46647 | barriers-to-effective-listening-workbook | new | draft | 67 |
| 46654 | coachability-and-client-readiness-workbook | new | draft | 67 |
| 46661 | finding-balance-across-your-life-workbook | new | draft | 67 |
| 46668 | your-lifes-assets-and-liabilities-workbook | new | draft | 67 |
| 46675 | the-uffe-elbaek-self-reflection-model-workbook | new | draft | 67 |
| 46682 | mind-mapping-your-life-goals-workbook | new | draft | 67 |
| 46689 | decision-making-frameworks-compared-workbook | new | draft | 67 |
| 46696 | four-projects-for-finding-direction-workbook | new | draft | 67 |
| 46703 | egans-foundations-of-earning-respect-workbook | new | draft | 67 |
| 46710 | the-skilled-helper-model-workbook | new | draft | 67 |
| 46717 | five-ways-we-perceive-the-world-workbook | new | draft | 67 |
| 46724 | inside-the-hypnotherapy-process-workbook | new | draft | 67 |
| 46731 | active-listening-workbook | new | draft | 67 |
| 46738 | discrimination-and-your-assumptions-workbook | new | draft | 67 |
| 46745 | the-dimensions-of-personal-prejudice-workbook | new | draft | 67 |
| 46752 | aristotles-nicomachean-ethics-workbook | new | draft | 67 |
| 46759 | rational-emotional-and-empathic-minds-workbook | new | draft | 78 |
| 46766 | carl-rogers-person-centred-principles-workbook | new | draft | 67 |
| 46773 | the-know-thyself-self-assessment-workbook | new | draft | 67 |
| 46780 | the-larry-crabb-model-workbook | new | draft | 67 |
| 46787 | martin-bubers-i-and-thou-workbook | new | draft | 67 |
| 46794 | eric-bernes-transactional-analysis-workbook | new | draft | 67 |
| 46801 | the-six-stage-cycle-of-change-workbook | new | draft | 67 |
| 46808 | healthy-dependency-or-codependency-workbook | new | draft | 67 |
| 46815 | ontology-and-your-sense-of-identity-workbook | new | draft | 67 |
| 46822 | investigating-your-unhelpful-thoughts-workbook | new | draft | 67 |
| 46829 | stages-of-the-counselling-process-workbook | new | draft | 67 |
| 46836 | getting-comfortable-with-silence-workbook | new | draft | 67 |
| 46843 | the-core-counselling-skills-workbook | new | draft | 67 |
| 46850 | the-fundamental-levels-of-listening-workbook | new | draft | 67 |
| 46857 | the-nine-attitudes-of-mindfulness-workbook | new | draft | 67 |
| 46864 | the-buddhas-four-noble-truths-workbook | new | draft | 67 |
| 46871 | barriers-to-personal-growth-workbook | new | draft | 67 |
| 46878 | facing-your-inner-critic-workbook | new | draft | 67 |
| 46885 | the-six-stages-of-personal-reflection-workbook | new | draft | 67 |
| 46892 | the-levels-of-systems-thinking-workbook | new | draft | 67 |
| 46899 | seven-pillars-of-healthy-relationships-workbook | new | draft | 67 |
| 46906 | facilitating-positive-change-in-others-workbook | new | draft | 67 |
| 46913 | changing-your-perception-of-events-workbook | new | draft | 67 |
| 46920 | what-undermines-relationship-health-workbook | new | draft | 67 |
| 46927 | reflecting-on-your-life-story-workbook | new | draft | 67 |
| 46934 | where-your-emotions-come-from-workbook | new | draft | 67 |
| 46941 | playing-the-reframing-game-workbook | new | draft | 67 |
| 46948 | charting-your-pathway-to-progress-workbook | new | draft | 67 |
| 46955 | six-principles-of-personal-productivity-workbook | new | draft | 67 |
| 46106 | core-values-workbook | new | draft | 67 |

## 5. Anything I could not settle

- Whether the 0 on 46549 is a real reading: the editor read the page as empty and I did not read it again; it is under the bar in any case.
- The human read of the five pages named in section 2 is still owed.
- David Emerald's Empowerment Dynamic (003-046) is the second pass and is not in these counts; send the line when it is built.

*No em or en dashes in this file; checked before writing.*