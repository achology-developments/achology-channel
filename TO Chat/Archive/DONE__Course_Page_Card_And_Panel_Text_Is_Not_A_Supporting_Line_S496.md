> CHAT DISPOSITION, S465 night postbag (11 November 2026): DONE. The three rows are Kain's own words and are recorded exceptions; written into the course page signed spec, section 3i, and answered in RULING__Night_Postbag_For_The_Theme_Sessions_S465.md in FROM Chat, section 1.4.

**For Chat. What this needs from you:** a ruling on the three block heading rows that are left, in section 3. Code, factory session S496, 11 November 2026. Answers RULING__Evening_Postbag_Course_Workbook_Pricing_School_And_Redirects_S465, section 3 item 1.

# DONE: on a course page, a card's or panel's own text is no longer read as a supporting line

## 1. What was built

page_gate.py's block heading check now knows the course page type's own cards and panels. On an address shaped /academy/{school}/{course}/, a heading inside one of these boxes is that box's own title, and the text under it is the box's own:

- a question card (the nine answers),
- the Who This Course Is For panel,
- a pricing card,
- a bundle card.

They are printed as one INFO row that names each, never dropped silently. A block heading on a course page, an h2 with its line, is still judged in full. The reading reaches the course page type only: the same question card on any other page still fails.

## 2. Proof

- tools/page_gate_card_text_test.py, six cases, written first: red 2 of 6 before the change, 6 of 6 after. Three cases prove the cards and the panel no longer fail; three prove a real block heading still fails and that another page type is untouched.
- The gate run on course 001 on the build site, before and after: 29 block heading fails before, 3 after, with 13 headings named as a card's or panel's own.
- Verified on 1 of 28 pages. The other 27 share the template and the same boxes, and were not run this session.
- The gate's older carve-out test still passes 6 of 6. Theme commit d5285271, pushed. No theme file was touched and nothing was deployed.

## 3. The three rows left, for your ruling

These are real block headings with real supporting lines, so the gate is right to fail them:

1. **"What You Will Learn":** its line is 11 words, one short of 12. "Here's an overview of what you'll learn in this training course."
2. **"Enrol in This Course and Payment Options":** its line is 39 words, where 25 is the most.
3. **The same line** is three sentences, where two is the most.

Each is either a recorded exception inside a block Kain signed, or a change of signed words. Both are yours.

OWED BACK: your ruling on the three rows; the course page session then writes them into the page's record.

*No em or en dashes in this file; checked before writing.*
