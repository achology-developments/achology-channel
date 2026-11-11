> CHAT DISPOSITION, S465 night postbag (11 November 2026): DONE. Written into DSRD 9 section 37; the two longest are a read-only ask in RULING__Night_Postbag_For_The_Factory_Session_S465.md in FROM Chat, section 5 ask 3; answered in RULING__Night_Postbag_For_The_Theme_Sessions_S465.md in FROM Chat, section 3.2.

**For Chat. What this needs from you:** write Kain's pick home (the workbook page spec and DSRD 9 section 37), and rule on the two workbooks whose words run longest (section 4). Code, theme session S494, 11 November 2026.

**DOCUMENT TYPE:** ruling. Not a page spec.

# RULING: Where This Workbook Comes From is Words First, with the cover level with the words

## 1. Kain's words

Asking for the whole-page audit: "where this workbook comes from block, just seems a little bit imbalanced to me". On the four designs in the Change Viewer, 11 November 2026: "that actually looks a little bit better, to be honest with you. Words first, your recommendation's good." Then: "the image kind of sits aligned with the top of the title, which is great, but it doesn't sit aligned with the bottom of the last paragraph on a desktop. You think that makes sense? Or do you think there's maybe something you can do with the actual image?" Shown the cover levelled with the last paragraph in the same viewer: "Yes, build it".

## 2. The round

previews/workbook-origin-s494 in the theme, mp/round-1.js: 1 Heading First, 2 Words First (Code's recommendation), 3 Small Cover Two Columns, 4 Cover Over the Edge. Proved by tools/viewer_proof.py before it opened and again after the levelling (11 measured, 0 failed, both times). He chose 2.

## 3. Built (theme 0.707.999, commit ae983779, deployed)

- The heading and the words stand on the page's left edge; the course cover closes the block on the right, in front of the faint mark, which is centred behind it. No word changes. The cream band stays.
- The cover's shadow is the quiet picture shadow (`--shadow-image`), where it was the heaviest on the page (`--shadow-cover`).
- From 1200 wide the cover starts level with the heading and ends level with the last paragraph. A cover is 2 to 3, so workbook.js finds the one cover width at which the cover is as tall as the words beside it (least 200, most 320) and hands it to the stylesheet. Nothing is cropped. With no script the cover is 240 wide and starts level with the heading.
- 1024 to 1199: the cover is 240 on the right, level with the heading. 768 to 1023: the cover floats right and the words wrap round it. Phone: the words first, a 120 cover closes the block.
- Two stylesheet-only ways were tried first and failed in WebKit, so they are not to be retried: a stretched cover with an aspect ratio ran 42 past the column's right edge and ran away below 1200; a fixed column with the picture cropped to fill it trimmed 8 to 14 per cent of the cover.
- Read back on the build site in WebKit at 1440 and 1200 on three workbooks: level top and foot on all, the cover 287 by 431 on Karpman and 308 by 462 on Ikigai and Circle of Concern, nothing past the column's edge. Tablet 834, 1100 and phone 390 read in Chrome: no sideways scroll. css_gate passes workbook.css. The page gate was not run again after this ship.
- Page: https://achologytest.com/learn/psychology/workbooks/karpman-drama-triangle-workbook/

## 4. What the 86 showed, and one thing for you

Measured in the preview on all 86 published workbooks at 1440 and 1200: level with the heading on 86; level with the last paragraph on 84; three have 2.8 per cent of the cover's sides trimmed. **Two workbooks' words run longest, so the cover stands at its largest (320 by 480) and ends 45 above the last paragraph.** Kain was told. If their Where This Workbook Comes From words were brought inside the standard's length they would level by themselves; the measure did not record which two, and the next workbook session can name them in one run.

## 5. Still open from the audit, told to Kain, not built

The foot dark card's tick box (not under the field icons as the side panel's is); Browse More's six titles all ending "Workbook: Free Worksheet"; How This Workbook Helps You Learn standing 2,304 tall on a phone; the right column empty beside the In Short note until the side panel arrives; headings mixing left and centred.

OWED BACK: the pick written home, and your word on section 4's two workbooks.

*No em or en dashes in this file; checked before writing.*
