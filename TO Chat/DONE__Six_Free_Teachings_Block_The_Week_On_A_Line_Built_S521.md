Needs from Chat: write Kain's two picks on the Six Free Teachings block home, note three things this build leaves open for you, and move the board cards.

# DONE: the Six Free Teachings block is built as The Week on a Line (Code, theme session S521, 15 November 2026)

Answers RULING__The_Six_Signed_Free_Teachings_And_Their_Lectures_S521. On the build site at theme 0.708.079 (commits 4384ea58 and c4fc4f0f).

## Kain's rulings, in his words (The Harness, Rule 14)

1. On the block as it stood: "I'm probably around about 17% happy with it ... I don't like looking at me ... I don't want this page to be about me."
2. Of four whole directions in the Change Viewer (round-six.js; The Week on a Line, Paper Pages, The Six Days, Your Inbox): "I'm looking at option number one, the week on a line. I actually really like this. It's simple, but I believe you can polish it ... we need to see synchronicity, we need to see structure, we want to see this thing polished." School PICKS.md, pick 23.
3. Of the polished line (round-line.js, option 1 of four): "Yes, build it". School PICKS.md, pick 24.

4. On the built school page in Safari at 0.708.079, asked "Is the built block right on the school page in your Safari?": "Yes, it's right".

## What is built

- One component, two fillings, as your ruling's section 3 puts it. All 28 course pages show their own lessons 1 to 6. The School of NLP shows its six signed titles, each with the length of the lesson your section 1 names: 27, 16, 29, 25, 33 and 12 minutes, and the figure above them reads 142 minutes, their sum.
- No picture and no name of Kain in the block: the six stills, Day 1's name plate and the row of tiles are out of the markup. The labels read "Day 1" to "Day 6"; "With Its Workbook" is gone from them on both page kinds.
- The look: one grid of six equal columns 24 apart; each day one column (a 48 ring with its number, Day 1 filled orange, the Overline label, the name as the H4 Card Title at 16, the length as Body Small, the six lengths on one line); the line 8 clear of each ring; the form under it, each control two columns, its panel bleeding 16; the two figures on the fourth column; Then You Decide as the closing line. On a tablet and a phone the line runs down the left.
- Where: tools/free_block.py (called by course_page_data.py and school_page_data.py, so a page built again keeps it), course-page.css (one rule set at its end), data/course-page and data/school-page.
- Read on the build site at 1440: the school page and the Diploma course page. Phone and tablet were read in the preview round, on the same rules, and not yet on the built pages.

## A fault of mine, mended

0.708.078 left half the old block after the new one on the school page (a stray fragment under the block). Mended at 0.708.079 within minutes. The tool now proves on every file that nothing outside the block moves and that a second run changes nothing; all 29 files were checked against the commit before the build.

## Left open, for you

1. The block's title on the school page still reads "Six Free Teachings, Each With Its Workbook", which your ruling calls a stand-in. Its words are yours.
2. The Day 1 question line ("What can you expect from ...") is no longer shown. Say if it should return.
3. A band exception for DSRD 7: the block's own 48 between its bands stands (pick 306); the form's panel bleeds 16 on a computer; the minutes figure on a school page is the sum of the six lengths.

## Not done

- The DSRD 6 gate was not run again on the course pages or the school page after this change: built, gate open.
- The CBP and mental health school pages do not exist in the theme's data yet (only the NLP school's), so their six are in the tool and not on a page. The four schools with no signed six are not built at all.
- The school form is not wired to any Kit sequence, as your ruling says.
- The rules that drew the old pictures are still in course-page.css, unused, for the dead code sweep.

OWED BACK: the picks written home; your word on the three open lines.

*No em or en dashes in this file; checked before writing.*
