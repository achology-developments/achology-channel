> CHAT DISPOSITION, 10 November 2026 (branch of Chat's main session): written home: DSRD 9 section 20.0i and DSRD 8 section 6.2's family note, read back. Archived.

**For Chat. What this needs from you:** write the workbook card into DSRD 9 section 20.0 (the Knowledge Hub wall's cards) and DSRD 8 section 6.2's family note, as below. Code (theme session), S466, 9 November 2026.

# RULING: the workbook card on the Knowledge Hub walls (Kain, S466, Option 3 Comb Bound)

Kain, 9 November 2026: "in the category pages. It's the workbooks card ... I think what we might be better off doing with the workbook cards is just creating them to essentially match book note cards". Shown four whole options in the Change Viewer (round-wc.js, previews/workbook-card-s466), he answered: "Option 3, Comb Bound". Built and on the build site at 0.707.864 (SHIP__Workbook_Card_Comb_Bound_0.707.864_S466).

**The rule.** A workbook on a Knowledge Hub wall is its own card, never the article tile. It is the book note card's shape with one difference, the picture:
- Shelf, label, title and body are the signed book note card's (cream shelf #F7F4EF with the floor band from 78%, 16 above and below, the floor shadow, label with icon, title, body padding 16).
- The label reads Workbook, with the workbook icon (file-pen).
- The picture is the workbook's featured image, the whole page (the PDF's page 1, US Letter, 816 by 1056, ratio 0.773), never cropped. It faces the reader, 176 high, held by a comb binding down its left edge, on the shelf; corners 2, 4, 4, 2; shadow 0 2px 6px at 28 per cent of the brand dark.
- Under the title it carries the workbook's own one-sentence description (its excerpt) in the book note's grey description line (Kain, S466, "Option 2, Description", chosen beside the article, book note and quote cards). It carries no word count and no reading time: a workbook has neither. Built at 0.707.865.
- A title word too long for a phone card breaks rather than running out of the card (`overflow-wrap:break-word` on the workbook title).

**New values for DSRD 9 section 20.0 (all one-offs, annotated in kh-subject.css):** picture height 176; comb ring drawing 18 by 11 repeated down the edge from 6 below the top to 6 above the foot, overhanging the sheet by 6; the 6 optical nudge on the picture so the overhang stays centred on the shelf; corners 2, 4, 4, 2; shadow as above.

**The workbooks lists' lead panel (Kain, S466, "Option 1, Same Stance"), built at 0.707.867.** The "Latest Workbook" panel takes the Latest Book Note panel's stance (kh-subject.css, S174): the same dark ground (#1A242B), soft focus (blur 14, saturation .95, opacity .75) and wash, the same turn (rotateY -16 with perspective 900), corners (2, 5, 5, 2) and lift shadow (0 22px 44px at 50 per cent black), the page 70 per cent of the panel high to a 320 maximum (240 between 1024 and 1100), at 9 per cent from the right; the cover's own picture, blurred, stands where the bookshelf picture does; the workbook card's comb binding, drawn for a dark ground, runs down the page's left edge; no word count; on a phone the page sits on top, 220 high, turned 12, with the wash darkening downwards. New values: the 70 per cent height and 320 and 240 maximums, the light comb drawing.

**The workbooks lists' Editor's Picks (Kain, S466, "Option 4, Titles Only"), built at 0.707.868.** The four picks are their names alone, in full, 16 on 1.4, no picture, spread evenly down the cream panel (the list's own hairlines and padding), the panel keeping the lead panel's 440 height. A workbook's page is not cropped to a strip anywhere in this list. No new value beyond the 16 on 1.4 title size, which is the Card Title step.

**Not changed:** the book note card, the article tile, the quote card, `.card--workbook` in cards.css, and every other place a workbook cover is drawn (listed in the SHIP).

*No em or en dashes in this file; checked before writing.*
