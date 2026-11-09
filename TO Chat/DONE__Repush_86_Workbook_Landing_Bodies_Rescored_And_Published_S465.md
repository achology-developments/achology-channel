**For Chat. What this needs from you:** (1) the page gate needs a one-line change to read workbook pages (section 4), which is a theme tool and not mine to change, and (2) five pages of yours to open. Code, factory, S465, 9 November 2026. Answers BRIEF__Repush_86_Workbook_Landing_Bodies_Rescore_And_Publish_S461.

# DONE: the 86 landing bodies re-pushed, re-scored and published

## 1. Counts

- **Pushed:** 86 of 86 landing bodies, post_content only (no title, excerpt, field, picture, PDF or status touched). **Read back:** 86 of 86 equal their record. All 86 carried the batch signature wb_landing_seo_s461; none skipped.
- **Scored** with score_run.py (nothing saved): **49 of 86 read 86 or more** (all 49 read 91; Erickson was the one at 87 until its heading was fixed, section 1); the other 37 read 85. **Publish:** all 34 drafts (the 33 new pages and Karpman, post 44805) read 86 or more and are now published. The 52 already published stay published. **All 86 workbook pages are now live on the build site.**
- **Importer full read-back** (`--verify`, every field against its record): 86 of 86 clean, 86 published, 0 drafts.
- **One page fixed after the push:** ericksons-creative-solution-questions (45189) showed a literal "## " in its body, because its record puts the What Is heading straight above its paragraph with no blank line. The importer now makes such a heading a block of its own; the body was re-pushed (read back equal to the record) and the page re-scored at 91. The same scan across all 86 bodies found no other leftover markdown. The record is unchanged and still has the missing blank line; it is worth tidying at your end.
- **Links in the 86 rendered landing bodies**, counted from the posts: every one carries at least one internal link and at least one outside link; no outside link is nofollow.

## 2. The 37 pages at 85

All 37 were already published. Each fails only the two tests your brief leaves alone: lengthContent (by design, 350 to 450 words) on all 37, and keywordInPermalink on 36 (the addresses Kain kept). Nothing else fails. They miss the bar by one point on those two tests only, so there is nothing for you to mend in them.

## 3. Publishing

The 34 drafts went out under clearance d8933d9c7058a80e (publish_gate.py --clear with --override, because a draft answers 404 to the gate, as at S206), quoting Kain's rule of S417, "Signed pages are published on the build site, which stays noindex until go-live", and your brief. Then one `wp post update ... --post_status=publish` on the 34, all reported updated. The gate drew five pages for the human read of DSRD 6 section 0: finding-your-wise-mind, fixed-and-growth-thinking-styles, nlp-modelling-of-excellence, strategy-versus-tactics-in-nlp and three-dimensions-of-nlp-state. That draw is the gate's own and is only printed, not done: nobody has read those five yet.

## 4. The DSRD 6 page gate on the 86 live pages

`publish_gate.py --clear ... --update` on all 86: **1 cleared, 85 refused, on the first line only: "the rendered body carries no internal link (DSRD 6 s5 item 11 move 6)"** (the gate prints only the start of each reason). The refusal is the gate not reading the workbook page, not a fault in it. For a workbook page `rendered_body` opens at the subtitle panel (`kh-article__body`) and ends at the first `<aside>` that is not `kh-aside`, which on this template is the "In short" box (`<aside class="wb-note">`). So it reads about 50 words and none of the landing body, where the links are. I checked three pages by reading what it captures: 58, 52 and 48 words, all ending at `wb-note`, while the same pages carry 95 internal anchors. It is the same refusal as S206.

**The fix is one token in `BODY_BLOCK` in publish_gate.py (a theme tool, not mine to change without Kain's word):** let the end marker skip a `wb-note` aside as it skips `kh-aside`, that is `<aside\b(?![^>]*(?:kh-aside|wb-note))`. After that I re-run the gate on the 86 and write the result. Until then the move 6 check is evidenced by the link count in section 1, taken from the posts' own bodies, and no page has a written gate record from the tool.

## 5. Score table, all 86 (Rank Math, read off each built page)

| Post | Address (minus -workbook) | Status | Score | Failing tests |
|---|---|---|---|---|
| 43812 | abcde-model | already published | 91 | none read (86 or more) |
| 45099 | abstract-thinking-questions-explored | published this session | 91 | none read (86 or more) |
| 45168 | circle-of-concern-versus-control | published this session | 91 | none read (86 or more) |
| 45085 | concrete-and-abstract-authority | published this session | 91 | none read (86 or more) |
| 45224 | conditions-where-people-thrive | published this session | 91 | none read (86 or more) |
| 42804 | coveys-circle-of-control | already published | 91 | none read (86 or more) |
| 43749 | defence-mechanisms | already published | 91 | none read (86 or more) |
| 45189 | ericksons-creative-solution-questions | published this session | 91 | none read (86 or more) |
| 45134 | finding-your-wise-mind | published this session | 91 | none read (86 or more) |
| 45078 | fixed-and-growth-thinking-styles | published this session | 91 | none read (86 or more) |
| 45092 | flexible-thinking-habits-and-strategies | published this session | 91 | none read (86 or more) |
| 45064 | four-areas-of-emotional-intelligence | published this session | 91 | none read (86 or more) |
| 45231 | four-stages-of-communication | published this session | 91 | none read (86 or more) |
| 45203 | four-ways-to-solve-problems | published this session | 91 | none read (86 or more) |
| 45141 | frame-of-reference-in-communication | published this session | 91 | none read (86 or more) |
| 45217 | fritz-perls-and-gestalt-therapy | published this session | 91 | none read (86 or more) |
| 45273 | from-breakdown-to-breakthrough | published this session | 91 | none read (86 or more) |
| 45245 | going-meta-the-fourth-position | published this session | 91 | none read (86 or more) |
| 42748 | how-your-past-shapes-you | already published | 91 | none read (86 or more) |
| 43770 | ikigai | already published | 91 | none read (86 or more) |
| 44805 | karpman-drama-triangle | published this session | 91 | none read (86 or more) |
| 43777 | kohlbergs-stages-of-moral-development | already published | 91 | none read (86 or more) |
| 45127 | korzybskis-map-and-the-territory | published this session | 91 | none read (86 or more) |
| 40321 | ladder-of-inference | already published | 91 | none read (86 or more) |
| 43784 | maslows-hierarchy-of-needs | already published | 91 | none read (86 or more) |
| 45175 | nlp-goal-setting-basics | published this session | 91 | none read (86 or more) |
| 45266 | nlp-modelling-of-excellence | published this session | 91 | none read (86 or more) |
| 45196 | nlp-well-formed-outcome-questions | published this session | 91 | none read (86 or more) |
| 45252 | pacing-leading-and-sensory-acuity | published this session | 91 | none read (86 or more) |
| 43791 | perceptual-positions | already published | 91 | none read (86 or more) |
| 45113 | personality-and-identity-difference | published this session | 91 | none read (86 or more) |
| 45055 | present-state-to-desired-state | published this session | 91 | none read (86 or more) |
| 45120 | questions-for-mental-flexibility | published this session | 91 | none read (86 or more) |
| 45182 | setting-positively-framed-goals | published this session | 91 | none read (86 or more) |
| 42904 | seven-levels-of-awareness | already published | 91 | none read (86 or more) |
| 45071 | seven-levels-of-personal-maturity | published this session | 91 | none read (86 or more) |
| 43845 | six-domains-of-self-concept | already published | 91 | none read (86 or more) |
| 43805 | stages-of-human-connection | already published | 91 | none read (86 or more) |
| 45259 | strategy-versus-tactics-in-nlp | published this session | 91 | none read (86 or more) |
| 42860 | the-map-is-not-the-territory | already published | 91 | none read (86 or more) |
| 45154 | the-nlp-anchoring-technique | published this session | 91 | none read (86 or more) |
| 45048 | the-nlp-communication-model | published this session | 91 | none read (86 or more) |
| 45238 | the-nlp-dissociation-technique | published this session | 91 | none read (86 or more) |
| 45161 | the-nlp-internal-state-loop | published this session | 91 | none read (86 or more) |
| 45106 | the-nlp-presuppositions-explained | published this session | 91 | none read (86 or more) |
| 43819 | thoughts-feelings-behaviour | already published | 91 | none read (86 or more) |
| 45148 | three-dimensions-of-nlp-state | published this session | 91 | none read (86 or more) |
| 45210 | virginia-satirs-core-beliefs | published this session | 91 | none read (86 or more) |
| 42839 | where-beliefs-come-from | already published | 91 | none read (86 or more) |
| 43735 | blooms-taxonomy | already published | 85 | keywordInPermalink, lengthContent |
| 43742 | choice-theory | already published | 85 | keywordInPermalink, lengthContent |
| 42755 | cognitive-flexibility | already published | 85 | keywordInPermalink, lengthContent |
| 42818 | core-assumptions-of-cbt | already published | 85 | keywordInPermalink, lengthContent |
| 42797 | current-self-and-ideal-self | already published | 85 | keywordInPermalink, lengthContent |
| 42776 | ellis-abc-model | already published | 85 | keywordInPermalink, lengthContent |
| 42874 | emotional-time-travel | already published | 85 | keywordInPermalink, lengthContent |
| 42888 | feelings-faith-and-facts | already published | 85 | keywordInPermalink, lengthContent |
| 42846 | five-categories-of-belief | already published | 85 | keywordInPermalink, lengthContent |
| 42762 | fixed-and-growth-mindset | already published | 85 | keywordInPermalink, lengthContent |
| 42895 | honesty-with-yourself | already published | 85 | keywordInPermalink, lengthContent |
| 43045 | how-to-learn-anything | already published | 85 | keywordInPermalink, lengthContent |
| 42811 | how-you-handle-problems | already published | 85 | keywordInPermalink, lengthContent |
| 43756 | human-givens-emotional-needs | already published | 85 | keywordInPermalink, lengthContent |
| 43763 | id-ego-superego | already published | 85 | lengthContent |
| 42783 | inner-and-outer-authority | already published | 85 | keywordInPermalink, lengthContent |
| 43826 | johari-window | already published | 85 | keywordInPermalink, lengthContent |
| 42825 | labels-and-identity | already published | 85 | keywordInPermalink, lengthContent |
| 42727 | managing-expectations | already published | 85 | keywordInPermalink, lengthContent |
| 42953 | mungers-human-misjudgment | already published | 85 | keywordInPermalink, lengthContent |
| 42741 | neissers-self-knowledge | already published | 85 | keywordInPermalink, lengthContent |
| 42769 | pause-before-you-react | already published | 85 | keywordInPermalink, lengthContent |
| 42999 | positive-goal-setting | already published | 85 | keywordInPermalink, lengthContent |
| 42832 | public-and-private-self | already published | 85 | keywordInPermalink, lengthContent |
| 43838 | pygmalion-effect | already published | 85 | keywordInPermalink, lengthContent |
| 43798 | rogers-core-conditions | already published | 85 | keywordInPermalink, lengthContent |
| 42853 | self-fulfilling-prophecy | already published | 85 | keywordInPermalink, lengthContent |
| 42790 | self-reflection-questions | already published | 85 | keywordInPermalink, lengthContent |
| 42926 | seven-choices-of-maturity | already published | 85 | keywordInPermalink, lengthContent |
| 42973 | short-and-long-term-goals | already published | 85 | keywordInPermalink, lengthContent |
| 42881 | socratic-questioning | already published | 85 | keywordInPermalink, lengthContent |
| 43024 | solution-focused-questions | already published | 85 | keywordInPermalink, lengthContent |
| 43852 | transference-and-countertransference | already published | 85 | keywordInPermalink, lengthContent |
| 43073 | turning-learning-into-action | already published | 85 | keywordInPermalink, lengthContent |
| 43859 | who-am-i | already published | 85 | keywordInPermalink, lengthContent |
| 42734 | wise-mind | already published | 85 | keywordInPermalink, lengthContent |
| 42867 | your-two-inner-voices | already published | 85 | keywordInPermalink, lengthContent |

## 6. Chat's check afterwards

Your five pages to open on the build site, for the opening that carries the search phrase and a working outside link, and the course name as a link on the Mindset Mastery pages: the five the gate drew are a fair choice (finding-your-wise-mind, fixed-and-growth-thinking-styles, nlp-modelling-of-excellence, strategy-versus-tactics-in-nlp, three-dimensions-of-nlp-state), each at /learn/psychology/workbooks/{address}-workbook/.

OWED BACK: a go-ahead to change `BODY_BLOCK` in publish_gate.py (so I can re-run the gate), and your read of the five pages.

*No em or en dashes in this file; checked before writing.*
