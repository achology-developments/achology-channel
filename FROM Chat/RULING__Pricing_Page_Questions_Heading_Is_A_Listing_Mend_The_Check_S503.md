**For Code: the pricing page theme session (S503). What this needs:** mend the supporting line check's reading as section 2 says, prove it with the six cases of section 3, run the gate on /pricing/, mark chapter 2 with the words of section 4, and cut the approved prototype. Chat, 12 November 2026, written in a side session of Chat's seat that your S503 sitting opened under Kain's ruling of 12 November 2026 (The Shared Rules, section 6).

DOCUMENT TYPE: ruling. Not a page spec.

This file asks Kain nothing. Nothing in it is his to see: no page changes.

Answers RULING__Pricing_Page_Questions_Side_By_Side_And_Even_Band_Spacing_S503 (sections 1 to 4) and RULING__Pricing_Page_Kains_Word_On_The_Whole_Page_S503.

Done when: the check is mended and its test passes, the gate on /pricing/ prints no failing supporting-line row, chapter 2 of the page's record carries section 4's line, and the approved prototype is cut at the version then served.

Read from the vault first: none fit; the governing text is DSRD 7 section 3.3.

Model: no writer or checker is needed; the theme session makes one small change to its own tool.

## 1. The ruling

**It is a mend to the check's reading, your choice (b). No exception is recorded for this block or this page, and nothing is added to page_gate.py for it.**

The words of DSRD 7 section 3.3 that govern:

- Rule 1: "A heading stands alone only where the line would merely restate it, or where the block is a listing of items that describe themselves (the policies index, the instructor sections and the help hub headings are the existing legitimate cases)."
- The boundary paragraph: "The test is the structure around the heading, never a list of pages".
- Of every exception in the section: "The gate reports it as a named exception, never a silent pass."

The reasons.

1. The questions block is a listing of six answers that describe themselves. They are the Help section's own rows, the case rule 1 names. The heading has no supporting line and needs none. Nothing on the page is wrong, so there is nothing to except.
2. The check already agrees with this at two widths out of three. At tablet and phone width the rows stand under the heading, the check meets the list, and it counts the heading as one with no line. Only at computer width, where the list stands beside the heading, does it read differently. One block cannot be a listing at two widths and a failing supporting line at the third. The page did not change between the widths; the reading did.
3. An exception would be entered by page. The same misreading will come back on the next block that stands a list beside its heading, on any page. The section's own test is the structure, so the mend is made once, in the check.

## 2. What the check does today, and the mend

I read tools/supporting_line_check.py at theme commit 3b41623d, and the block's markup in pricing-parts.php (the `pricing-questions` section).

What happens at computer width. The heading stands in the left third and `ul.help-q-list` in the right two thirds, level with it. The check passes over everything that stands beside the heading (the test "top is above the heading's foot"). So it passes over the list itself, the first row, its link and the question's title, all of which start level with the heading. It never meets the list as a list. The first thing whose top is under the heading's foot is `span.help-q__excerpt`, the first question's answer line, deep inside the list and inside a link. That is taken as the supporting line: Mulish 16, weight 400, soft grey, no bar, 9.6 under the heading, 16 to the next row. Those are your four rows.

**The mend, in words to build exactly.** In the loop that looks for the line, before the test for a line of words:

1. For each thing after the heading, find its holder: the nearest ancestor that is inside the block, does not hold the heading, and is one of the check's own stop kinds (the tags in `STOP`: a list, a link, a button, a form, a figure, a table and the rest of that set).
2. A thing with a holder is that holder's own content. It is passed over, and the search goes on. It is never the line.
3. The first holder passed over this way is remembered. Where the search ends with no line and no other reason, the reason printed is: "a listing stands beside the heading (" plus the holder's name plus "); nothing under the heading is a line of words". On /pricing/ the name will be `ul.help-q-list`.
4. Nothing else in the check changes. A stop kind met under the heading still ends the search as it does today. A card's content is already passed by the card test and stays so. The heading's row, the tilt rule and the named exceptions are untouched.

The search goes on rather than stopping, on purpose: where a picture or a list stands beside a heading and a real supporting line follows in the heading's own column, that line must still be found and judged. A mend that stopped at the first holder would turn a failing line into a silent pass.

The file was clean in git when I read it (last commit 3b41623d, the workbook page session's). Run `git status` on it before you edit, and if another session holds it changed, wait for its commit; do not edit over it.

## 3. The proof cases, red first

In the check's own test file, beside the S506 cases. Cases 1 and 5 must be seen red before the mend and green after it. The others are guards and must be green both before and after.

1. **A list beside its heading.** The heading in a left column, a list of rows in a right column, level with it, the first row's second line starting under the heading's foot (the /pricing/ shape). Wanted: no line; the heading counted with the reason of section 2 item 3, naming the list. Red today: the row's second line is read as the line and fails type, bar and both spaces.
2. **The same markup stacked.** The heading above the list. Wanted: no line, "the next thing is" the list, as today.
3. **A real line under the heading, a list beside both.** The heading and a `lead-bar` line in the left column, the list in the right. Wanted: the line is found and passes all five checks.
4. **A picture beside the heading, a real line after it in the markup.** Wanted: the line is found and passes, as today.
5. **The check can still fail.** The heading in the left column with a paragraph under it at Mulish 16, weight 400, no bar, and a list beside both. Wanted: that paragraph is the line and fails line-type and line-bar. Run it against a cut that stops at the first holder to see it red; the cut of section 2 is green.
6. **The real page.** /pricing/ at all three widths: "Achology Pricing: Commonly Asked Questions" is counted with no line at each width, and no supporting-line row fails or is carved out for it. The three section lines still pass, and the opening cards' and the learning block's rows still print as their named carve-outs.

**One wider read, so nothing moves unseen.** Run the check before and after the mend on /pricing/, one course page, /certification/ and one workbook page, and compare the two reports row by row. The only rows that may move are the four of section 4. Any other row that moves is reported to Chat by page, heading and figure, and is not given an exception.

## 4. In the pricing page's record

Once the gate is run after the mend and prints no failing line in chapter 2, mark chapter 2, with the version filled in:

"pass, 2026-11-12, [machine, Code S503] page_gate at {version}: no failing line. The questions heading stands without a supporting line: a listing beside its heading is still a listing (DSRD 7 section 3.3, Chat's call of 12 November 2026, RULING__Pricing_Page_Questions_Heading_Is_A_Listing_Mend_The_Check_S503). The check's reading was mended; no exception is recorded for the page. The seven card-name lines and the learning block's line print as carve-outs."

If the gate still prints a failing line in chapter 2 after the mend, chapter 2 stays open and the line comes back to Chat as printed. Then cut the approved prototype at the version served, as your file says.

## 5. What Chat wrote home

- **DSRD 7 section 3.3:** a new paragraph, "A listing that stands beside its heading is still a listing", with the pricing questions block as the worked case, and the words that the fault is mended in the check and no page exception is recorded.
- **DSRD 9 section 36.9:** pick 13 in Kain's words ("Side by Side, yes"), saying that it replaces his S126 choice of the Help article's card for this page only, that the Help pages keep their card, that the registry's row for the shared question row is unchanged, that the three looks he did not pick stay in the round folder, and the 0.708.044 mend. Pick 14 in his words ("yes, I choose even space round the sand bands as you recommend"), with your measured 96, 96 and 64. The questions heading standing without a line. Section 36.7 row 5 notes pick 13.
- **DSRD 9 section 36.9, Kain's word on the whole page:** "Yes, it's right", 12 November 2026, theme 0.708.044, to your question "Does the pricing page look right to you now?", standing beside his S209 "finished"; it says the word does not mark chapter 2, which closes on the gate run.
- **The change register** (the DSRD folder's README): rows 7 and 9.
- **The Build Board:** the pricing page's card carries his word and what closes chapter 2.

Your two files are archived in TO Chat with their disposition lines.

OWED BACK: one DONE when the gate has run: the printout's name, chapter 2's mark, the prototype's version, and any row on another page that moved under the mend.

*No em or en dashes in this file; checked before writing.*
