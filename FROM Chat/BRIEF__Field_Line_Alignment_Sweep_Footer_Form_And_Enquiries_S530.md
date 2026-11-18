What this needs: Code moves the lines under the fields on two more templates to Kain's new standard (DSRD 7 section 5.5): a line under a field starts at the field's icon, or at its text where it has none.

This brief asks Kain nothing. Code sends every question to the school page theme session (the main session), never to Kain.

Done when: on the 28 course pages' footer invitation form and on /enquiries/, every line under a field starts at the field's icon or text inset and ends the same distance in from the right, measured on the built page at 1280, 834 and 390, with the numbers in one DONE in TO Chat.

Model: Opus 5.5. Effort: medium.

From Chat, a branch session of the S530 school page sitting, 18 November 2026. It answers ASK__School_Page_Field_Line_Alignment_Standard_And_Sweep_S530.

## The standard (DSRD 7 section 5.5, written today)

Kain, 18 November 2026, on the built school page: "I would like this standard to be implemented site-wide". The rule as written: a line of text directly under a field (a tick line, a hint, a note, an error) starts where the field's leading icon starts and ends the same distance in from the field's right edge. With no icon, it starts at the field's own text inset (padding plus frame: 21 on a standard field) and ends the same distance in from the right. Under two fields side by side, it takes the left field's inset on the left and the right field's on the right. It is never flush with the field's edge and never centred. The start is read off the rendered field at every width, never typed as a guess.

Kain set the standard and asked for it everywhere, so these mends go straight to the build. Nothing goes to him as a round.

## The two places

1. **The course pages' footer invitation form, all 28** (course-page.css, `.fo2__form .pf2--pair .pf2__small`). The tick line is centred under the two fields: at 1280 the tick stands at 809 against the name field's person icon at 728. Start it at the name field's icon, as the free form's tick line already does (0.708.209), and end it the same distance in from the email field's right edge. Where the two fields stack on a phone, it takes the one field's insets.
2. **/enquiries/** (enquiries.php). These fields have no icon, so each line starts at the field's text inset:
   - the note under the message box ("Please do not include passwords, bank details..."), which today starts flush with the box's edge (120 against 120). The tall box's own padding sets its inset; read it off the box.
   - every field's error line (`.enq-err`), shown on a mistake. Trigger each error to read it.

The ASK's check of one page per template, 25 templates, found nothing else under a field. The menu's search has its link grid under it, which is not a line of text and stays as it is.

## How it is proved

- Before and after, each line's left and right edges against the icon or first character, at 1280, 834 and 390, in WebKit, with each state shown (an error line shown, the tick line on the course footer).
- Nothing else on either form moves: no field, gap, size or colour changes (the button family changes looks, never layout, DSRD 7 section 5.1).
- css_gate passes the files changed, with the version bumped.

OWED BACK: one DONE in TO Chat with the readings, the theme version, and any third place found while measuring.

DOCUMENT TYPE: brief.

*No em or en dashes in this file; checked before writing.*
