> CHAT DISPOSITION, S465 night postbag (11 November 2026): DONE. Written into DSRD 7 section 4.3, Exception 26, and DSRD 9 section 37; the family fix is a theme queue line; answered in RULING__Night_Postbag_For_The_Theme_Sessions_S465.md in FROM Chat, section 3.3.

**For Chat. What this needs from you:** a sweep line for the same doubled space on articles and quote pages, and Kain's words written home. Code, theme session S494, 11 November 2026.

**DOCUMENT TYPE:** ruling. Not a page spec.

# RULING: one space above the footer on the workbook page, and the same double on articles and quote pages

## 1. Kain's words

Asking for a whole-page audit of the workbook page, 11 November 2026: "There's quite a lot of spacing. Just above the footer". Shown the audit's list and asked whether to fix the footer space and bring four designs for Where This Workbook Comes From: "Yes, do both".

## 2. What was measured

On the Karpman workbook at 1440: the last two cards ended 128 above the footer, where the page's other gaps run 48 to 96. Two 64s stack: the closing block's own padding-bottom (`.kh-close`, kh-band.css, written at S164 as room for the speech bubble tails, which the block no longer has) and the page's own (`.kh-article`, knowledge-hub.css, 64, 48 below 768).

## 3. Built, on the workbook page only (theme 0.707.994, commit e14a515a, deployed)

`main.kh-workbook .kh-close { padding-bottom: 0; }` in workbook.css. Read back on the build site: 64 between the cards and the footer at 1440, 48 at 390, no sideways scroll. css_gate passes.

## 4. For your sweep

Articles and quote pages are `.kh-article` pages that end on the same closing block, so by the same two rules they carry the same 128. Code did not touch them: The Harness Rule 3 keeps a change set to one page. The one-line family fix is `.kh-article .kh-close { padding-bottom: 0; }` in kh-band.css, after which the workbook's own line comes out. Book notes use `.bn-page` and were not measured.

## 5. Also from the audit, for your knowledge

The seven things Code would improve on the workbook page, as given to Kain: Where This Workbook Comes From (four designs are now in his Change Viewer: previews/workbook-origin-s494, round 1); this footer space; the foot dark card's tick box not yet under the field icons as the side panel's is; Browse More's six titles all ending "Workbook: Free Worksheet"; How This Workbook Helps You Learn standing 2,304 tall on a phone; the right column empty beside the In Short note until the side panel arrives; headings mixing left and centred.

OWED BACK: the sweep line, and his words written home.

*No em or en dashes in this file; checked before writing.*
