For Chat. What this needs: nothing; it closes BRIEF__Field_Line_Alignment_Sweep_Footer_Form_And_Enquiries_S530.

From Code, the school page theme session (S530 side session), 18 November 2026. Theme 0.708.216, commit 3dedd17e.

# DONE: lines under fields, the sweep

Both places now meet DSRD 7 section 5.5. They were measured in the app's browser through the mirror, before shipping, on the theme as shipped.

## 1. The course pages' footer invitation form (course-page.css)

`.fo2__form .pf2--pair .pf2__small` is no longer centred. It now starts at the name field's icon and ends 16 in from the email field's right edge, the icons' own inset.

| Width | Name icon | Tick | Email field right, row end | Fields |
|---|---|---|---|---|
| 1280 | 728 | 728 | 1192, 1176 (16 in) | side by side |
| 834 | 48 | 48 | 802, 786 (16 in) | stacked |
| 390 | 32 | 32 | 374, 358 (16 in) | stacked |

Before: the tick stood at 809 against the icon at 728, at 1280.

## 2. /enquiries/ (enquiries.css)

These fields have no icon. Their text stands 17 in, read off the rendered fields: padding 16 and the frame 1, the same on every field at every width. The note under the message box and each field's error line now start there and end as far in from the right. The error lines were read with every field set to its error state.

| Width | Line | Field text start, end | Line start, end |
|---|---|---|---|
| 1280 | email error | 481, 775 | 481, 775 |
| 1280 | message note | 137, 775 | 137, 775 |
| 1280 | message error | 137, 775 | 137, 775 |
| 834 | email error | 442, 753 | 442, 753 |
| 834 | message note and error | 81, 753 | 81, 753 |
| 390 | email error | 61, 329 | 61, 329 |
| 390 | message note and error | 61, 329 | 61, 329 |

Before: the note stood flush with the box's edge (120 against 120 at 1280). The topic picker's own error stands under the radio cards, not under a field, so it is left as it is.

## Also

- Nothing else on either form moved: these are padding and alignment on the line alone.
- css_gate passes course-page.css, enquiries.css and school-page.css.
- No third place was found while measuring.
- The school pages' two lines are already in: the free form's tick line (0.708.209) and the knowledge tree's line under its search (0.708.215).

*No em or en dashes in this file; checked before writing.*
