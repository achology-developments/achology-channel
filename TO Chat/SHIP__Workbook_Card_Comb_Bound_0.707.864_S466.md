**For Chat. What this needs from you:** the DSRD 9 section 20.0 values in RULING__Workbook_Card_Comb_Bound_On_The_Knowledge_Hub_Walls_S466; otherwise for the record. Code (theme session), S466, 9 November 2026.

# SHIP: the workbook card on the Knowledge Hub walls, 0.707.864 (S466)

**Why.** Workbooks fell through to the article tile on every wall: the label read "Article", the picture was a wide crop of the top of the cover, and the footer showed the landing page's own word count and reading time ("403 Words, 3 Minute Read"). The cause is one test in `achology_kh_subject_grid_html()` (knowledge-hub-parts.php, about line 4496), which chose book note or else article, with no `.bx-tile--workbook` rule in kh-subject.css. That one function builds the subject, kind list and tag walls and the front page's wall.

**What changed (commit 0d1a82aa, pushed, deployed from a clean copy of HEAD).** Kain asked for workbook cards to match the book note cards and was shown four options in the Change Viewer (Standing Workbook, Fanned Sheets, Comb Bound, Framed Sheet). He picked **Option 3, Comb Bound**, on 9 November 2026.
- knowledge-hub-parts.php: a workbook now has its own `data-kind="workbook"` and `bx-tile--workbook`, the label reads Workbook with the workbook icon, the picture is the featured image whole (WordPress's own 240 and 480 copies), and the footer line is not printed.
- kh-subject.css: the `.bx-tile--workbook` rules, on the signed book note shelf, with the comb binding drawn down the left edge.
- style.css: 0.707.864. The wall's saved copy keys on the version, so every wall rebuilt at once.
- previews/workbook-card-s466/: the four options, the mirror and the round file.

**Checked** on the build site at 1268, 1024, 834 and 390 on the Psychology Workbooks list (23 cards): all 23 labelled Workbook, none with a footer, every picture loaded, each picture and its comb inside its card, nothing sideways, 4, 4, 3 and 2 columns. The All Workbooks list (23) and Motivation Workbooks (1) carry the same cards; the subject wall and front page (34 article and 12 book note tiles, no workbooks) are unchanged. Eight of the 23 titles end on one word, as they did in the article tile: the wall's titles do not use the no-lone-words feature (it covers founder and About pages only), and the wrapping width has not changed. Deploy proofs agree at 0.707.864 (local, server, zip). The CSS gate reports 75 flagged lines in kh-subject.css, the same 75 as before this change, none in the new block.

**Found, not changed.** Other places still draw the new Letter covers as crops: the "Latest Workbook" panel at the top of each workbooks list (the cover's own title text shows through the panel's heading), the Editor's Picks thumbnails beside it, the search results rows, `.card--workbook` in cards.css, and the fanning stack of covers in Browse More. Say which Kain wants next.

**Owed to Kain, one question at a time:** whether the workbook card needs a line at its foot, and if so which words already on the page. Until he answers it has none.

*No em or en dashes in this file; checked before writing.*
