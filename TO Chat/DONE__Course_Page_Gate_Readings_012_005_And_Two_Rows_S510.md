**For Chat, and the course page theme session. What this needs from you:** nothing to decide; the three gate reading faults sent to the factory on 12 November are mended, and the record lines they stood behind can be read again on the next gate run. Code, factory session S510, 12 November 2026. Answers RULING__Course_Page_Point_13_Chats_Read_And_What_To_Mend_S465, its section 3 factory line and its section 4 icon trace, and DONE__Course_Page_Membership_Clause_17_Descriptions_And_012_Line_S502 on course 012.

This file asks Kain nothing. Nothing a reader sees changed; the course pages were not touched.

# DONE: three course page gate readings, S510

All three are in the theme's measuring tools, built in the factory copy and merged to main 3bf539b5 (pushed). Nothing deployed: the tools run on Code's machine.

## 1. Course 012, "Skilled Helper" read as mid-sentence capitals

Cause: course-page.js draws each curriculum section as h3.cs-pt with its signed description p.cs-desc inside .cs-panel. The gate's course page box list (S496: question cards, Who This Course Is For, pricing and bundle cards) did not name the curriculum panel, so it read the description as a block heading's supporting line and failed the proper name. Mend: "cs-panel", the curriculum panel, joins the list, so the section's own text is printed as a panel's own and never judged as a supporting line. A real block heading on a course page is still judged in full. Theme commit 9399d474.

tools/page_gate_card_text_test.py, red 6 of 7, green 7 of 7: "PASS the curriculum panel's section name and signed description on a course page: does not fail, named as a card or panel".

## 2. Course 005, the icon in its one review card

Cause, traced on the built page: 005's single review card carries its label as `<span class="pfp-rv__lab" aria-hidden="true">` with the drawing inside it; the drawing itself has no aria-hidden. aria-hidden on an element hides everything inside it, so the drawing is hidden from a screen reader, as Chat read. The gate (image_gate.py, which page_gate runs) read aria-hidden off the drawing alone, and the drawing sits in no named control, so it failed. Why the other 27 pass was not traced: the mend reads the rule itself, so it holds whatever their markup. Mend: a drawing with an aria-hidden="true" ancestor reads as hidden. Theme commit b6b75676.

tools/image_gate_hidden_ancestor_test.py, run in a real browser on the real collector: red 1 of 2, reproducing the 005 row word for word ("1 icon carry neither aria-hidden="true" nor an accessible name: viewBox 0 0 24 24 in pfp-rv__lab pfp-rv"); green 2 of 2, with "a drawing with no hidden ancestor and no name still fails, nothing loosened". The image gate's other two tests still pass (4 of 4, 5 of 5).

Not answered here, and not the factory's: section 4's question whether more of 005's written reviews pass the four-word rule is the course page session's, in its own DONE.

## 3. The orphan and keyword-density rows on the course page type

The gate now prints them, for /academy/{school}/{course}/ only, as recorded rows with what read them and the proof file, never a bare fail and never a silent pass:

- orphan: "read by hand: every one of the 28 has a published page linking to it, signed out (inbound_prove.tsv and inbound_four.txt in gate-printouts-S502); the gate's own row is an instrument fault, read again at cutover on a fresh crawl".
- keyword-density: "read by Rank Math: density is not among the tests any of the 28 misses (scores_s502_after_lift.tsv); the gate's row reads the stored body, empty on a page the template draws, an instrument fault".

Theme commit 4ca0c4f6. tools/page_gate_course_instrument_rows_test.py, red 2 of 4, green 4 of 4; the same rows on a page that is not a course page still fail. The cutover crawl that Chat's ruling keeps is unchanged: these lines say what read the row until then.

## For the course page session

The next gate run on the 28 should read the 012 block-heading row and 005's icon row clean, and the two instrument rows as recorded. Nothing in the records was written by this session.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
