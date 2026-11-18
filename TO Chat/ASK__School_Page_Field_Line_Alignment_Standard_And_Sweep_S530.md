For Chat. What this needs: Kain's new site-wide standard written into DSRD 7 section 5.5, and a sweep brief naming the two places left, so Code can mend them.

From Code, the school page theme session (S530 side session), 18 November 2026.

Done when: DSRD 7 section 5.5 carries the rule, and a sweep brief in FROM Chat names the course pages' footer form and /enquiries/.

# ASK: a line under a field starts at the field's icon (Kain's standard)

## Kain's words

18 November 2026, on the built school page. He showed the free form's tick line, where the tick box now stands under the first name box's person icon (0.708.209). He also showed the knowledge tree's "Choose a topic..." line, which stood flush with the search field's edge. He said: "look at how the text in the box is positioned underneath the Enter Your Name tab, right? I would like this standard to be implemented site-wide, all right? ... because there's already a misalignment."

Earlier, on the same form: "move the left line in so that the tick box aligns with the person icon in the your first name block, and whatever that distance is, move the ... privacy policy describes ... in from the right hand side to match".

## The rule, as Code reads it, for DSRD 7 section 5.5

A line of text that stands directly under a field (a tick line, a helper line, a note, an error message) starts where the field's own leading icon starts. It comes in the same distance from the right. Where the field has no icon, it starts where the field's own text starts, at its inner padding plus its frame. It is never flush with the field's outer edge, and never centred under it.

## Where it stands

**Done, on the school pages** (in Code's scope):
- **The free form's tick line**, at 16 in (0.708.209). It is shared, so it is also on the 28 course pages' free block.
- **The knowledge tree's line under its search**, at 21 in (0.708.215).

**Left, other pages** (a sweep). These were found by a check of one page per template, 25 templates:
1. **The course pages' footer invitation form** (28 pages; course-page.css `.fo2__form .pf2--pair .pf2__small`). Its tick line is centred under the two fields: the tick at 809 against the name icon at 728, at 1280. It would start at the icon.
2. **/enquiries/** (enquiries.php):
   - The note under the message box, "Please do not include passwords, bank details...", starts flush with the box's edge (120 against 120).
   - Each field's error line (`.enq-err`, shown on a mistake) stands the same way.
   - These fields have no icon, so each line would start at the field's text inset.

Nothing else on the 25 templates sits under a field. The menu's search has its link grid under it, which is not a line of text.

OWED BACK: the DSRD 7 section 5.5 rule, and a sweep brief for items 1 and 2.

*No em or en dashes in this file; checked before writing.*
