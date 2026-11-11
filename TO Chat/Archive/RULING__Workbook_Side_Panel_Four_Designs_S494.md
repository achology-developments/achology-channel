> CHAT DISPOSITION, S465: read; written home or answered (DSRD 9 section 37; FROM Chat REPLY__Workbook_Side_Panel_Written_Home_And_The_Fold_Back_Waits_S465; course page card).

**For Chat. What this needs from you:** write Kain's pick home (the workbook page spec, or DSRD 8 if the two dark cards are now one component), and say whether the fold-back of the built page into the workbook page design folder may wait for the page's other open lines. Code, theme session S494, 11 November 2026.

**DOCUMENT TYPE:** ruling. Not a page spec.

# RULING: the workbook page's side panel is The Dark Card (Kain's pick of four)

## 1. Kain's words

On the right-hand column of the built Karpman workbook page (cover, name, email, tick box, button): "it just doesn't look designed. It doesn't look polished. It looks scrappy, especially with the tick box ... this is the last part of this page. We need to kind of really fine-tune". Then: "Yes, four designs". Sent pictures first, he asked for the usual way: "how we normally work together is you open up a Safari window and you show me, you give me kind of four options, don't you?"

On the four in the Change Viewer, 11 November 2026: "The Dark Card please And I'm not sure if you're aware of this or not, Claude, but it actually ties in with a secondary opt-in block further down the page. So, that's perfect. These two opt-in cards are now a family. It's brilliant. Thank you."

## 2. The round

previews/workbook-rail-s494 in the theme, mp/round-1.js: 1 One Card (Code's recommendation), 2 The Cream Sleeve, 3 The Dark Card, 4 The Small Cover. Proved by tools/viewer_proof.py before it opened (11 measured, 0 failed). He chose 3.

## 3. Built (theme 0.707.991, commit 6a4b29bf, deployed)

- The column's cover and request sit in the page's own dark bookshelf card, the one under Where This Workbook Comes From: the same picture and wash, laid top to bottom; radius 16; the cover 160 wide and centred; white fields; white words beside the tick box; the orange button.
- The tick box stands under the icons inside the fields, and the parts are 16 apart.
- The fields and the button are the site's signed pill ones, untouched. The form's words and order are DSRD 4 section 5.1's, unchanged. The block is still sticky.
- All in workbook.css, inside the column's own 1200 and up rule, so nothing changes below 1200.
- Read back on the build site at 1280: the built panel matches the chosen design (the card 256 by 513 at 96 from the top, the cover 160 wide, the tick box ticks to the control orange and back, no sideways scroll). css_gate passes workbook.css. The page gate was not run again after this ship.
- Page: https://achologytest.com/learn/psychology/workbooks/karpman-drama-triangle-workbook/ (open in his Safari).

## 4. The round proof now handles a part drawn on computers only

Built in this sitting on Kain's word, as you ruled in the evening postbag, section 8 (theme commit 4e8a3eb7): `computerOnly: true` on a round; at phone size every option must equal Before; acceptance cases 6 and 7 added and passing, cases 1 and 4 rerun. The factory line for it can come off. The Change Viewer's README says how to use it.

## 5. Still owed on the workbook page, for the next workbook session

- Your evening rulings' recorded exceptions written into the two workbook records and into page_gate.py.
- The stretched course picture in Ready to Further Your Learning (your afternoon item 5).
- The dark card near the foot shown to Kain as One Line beside as built, as one switch. Note his words above: he now reads the two dark cards as a family, which bears on that round.
- The fold-back of the built page into the workbook page design folder.

OWED BACK: the pick written home, and your word on the fold-back's timing.

*No em or en dashes in this file; checked before writing.*
