**For Chat. What this needs from you:** write Kain's pick home (DSRD 8, the Browse More decisions, and DSRD 9 section 37), since on workbook pages it changes how his S179 "whole page titles" are shown. Code, theme session S500, 11 November 2026.

**DOCUMENT TYPE:** ruling. Not a page spec.

# RULING: on workbook pages, Browse More shows each title's ending as a small note

## 1. Kain's words

From the audit he asked for at S494, the item "Browse More's six titles all end Workbook: Free Worksheet". At S500, when it came up: "Yes, next item". On four ways of showing the titles in the Change Viewer, told that the whole titles were his own S179 choice: "4 Ending as a note please".

## 2. The round

previews/workbook-more-titles-s500 in the theme, mp/round-1.js: 1 Name Only (Code's recommendation), 2 Shortest, 3 Quiet Ending, 4 Ending as a Note. Proved by tools/viewer_proof.py before it opened (11 measured, 0 failed). He chose 4, not the recommendation.

## 3. Built (theme 0.708.024, commit 189e68fd, deployed)

- single-workbook.php cuts each sibling's page title at its last colon. The name is the link's words in the list's own lettering; the ending ("Free Worksheet") is a small quiet note at the right, before the arrow: the writing's face at 14, soft grey. Under the name on a phone.
- **No word is written or changed.** Both parts are the title's own words. A screen reader still hears the whole title, colon included. A title with no colon prints whole. One title has two colons ("Going Meta: The Fourth Position Workbook: Free Worksheet") and is cut at the second.
- Workbook pages only. Articles, book notes and quote pages print their whole titles as before.
- Read back on the build site in WebKit on three workbooks at 1440, 1200, 1100, 834 and 390: every name on one line with at least 16 to its note from 834 up; on a phone the note sits under the name and each row is 75 tall where it was 54. No sideways scroll. css_gate passes workbook.css.
- Page: https://achologytest.com/learn/psychology/workbooks/karpman-drama-triangle-workbook/

## 4. One thing you should know

Where a workbook's title ends differently (Karpman's search title ends "Free Worksheet and Exercise"), its note reads whatever its own page title's ending is. The list prints the post's title, not its search title, so today all six notes read "Free Worksheet".

OWED BACK: the pick written home.

*No em or en dashes in this file; checked before writing.*
