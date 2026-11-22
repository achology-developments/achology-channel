NEEDS FROM CHAT: one wording change to DSRD 7's last-lines paragraph (rule 3), named below, so the standard says what the theme now does. Nothing else to act on.

# SHIP: the line lay, paragraphs set whole and titles broken at their phrase, theme 0.708.364 to 0.708.368

**For:** Chat. **From:** Code, branch 3 of the S544 theme sitting.

## What changed

One file, no-lone-words.js, the site's one line lay. Every page it lays takes the change: About, Student Reviews, Events, Membership, the Academy page, the seven school pages, the Access All Areas Pass, and the course pages' How It Works steps.

- **A paragraph is set again whole when its last line ends short (the flow lay).** A paragraph is a block over 140 letters that runs as one text. It keeps the number of lines the browser drew, and its last line holds four words. Whatever room the words leave is shared across every line above, so no one line stands short. It now wraps plainly instead of "pretty", because Safari's pretty itself set a paragraph's last rows near half the column.
- **A two-line title breaks at its phrase.** Where a short text (140 letters or fewer) falls on two lines and one word ends in a comma, colon, semicolon or question mark, the line breaks there. Both lines must still fit, each part must hold two words, and the shorter line must be at least half the longer.
- **The school pages' supporting lines take the flow lay too (0.708.367).** On two rows it does exactly what Kain's S528 fill lay does: the first row as full as it goes, the short row last. On three rows or more, the fill lay had left one row above the last at a third of the column, as in "for / 23% less than if / you bought them individually." on the school pages at 390. The flow lay keeps every row full instead.
- **A short card line of three rows or more is set whole (0.708.367).** The even lay had left "that make up" at a third of a card on a phone, between two full lines.
- **Unchanged:**
  - Titles keep their balanced fold and the even lay; so do two-row card lines and names.
  - A block that holds its own lines, such as a course step's bold title above its sentence, keeps its earlier lay. The flow lay broke inside such a title, "Choose Your Next Learning / Steps" at 0.708.364 and "Complete the Training / Course" at 0.708.367; 0.708.366 and 0.708.368 put that right.

## Why

The main session reported the faults (S544):
- **The Person-Centred school at 1280:** "you experience the / ideas for yourself first, and take away lived experience you / can use".
- **About at 375:** the answer "embody, / and use in your relationships, / your work and everyday life." and the heading "Achology: What It / Is, and Who It's For".

The cause was one rule in one place. The even lay re-set a paragraph's last three lines at the same width, 60 to 70 per cent, under full lines. That is the fault Kain ruled out on the school story's wide cards (S526) and the supporting lines (S528). The fix was made in that same place.

## Proof

Measured on the build site in WebKit at 1280 and 390, the old script against the new on the same pages:
- **The Person-Centred school, 1280:** lines 93 to 96 per cent, last line "relate to other people."
- **About, 375:**
  - The answer is 89, 86, 84 and 74 per cent, then "work and everyday life."
  - The heading reads "Achology: What It Is, / and Who It's For" (60 and 47 per cent).
- **The Events lead, 390:** 73 to 87 per cent on every line, where the fill lay had left "reached one of" at 35.
- **An About timeline card, 390:** "practice." no longer stands alone at 21 per cent; the card ends "accountable professional practice."
- **The full sweep:** see the counts appended below.

## What Chat needs to change

DSRD 7, the last-lines paragraph, rule 3 says "the words of the last three lines are set again over the fewest lines that hold them, as evenly as they go". For a paragraph that is now: "set again whole over the lines it drew, its lines as alike as they go and none short, the last holding four". For a title or other short line, rule 3 stands as written. Rules 1, 2, 4 and 5 are unchanged.

*No em or en dashes in this file; checked before writing.*
