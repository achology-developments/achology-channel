**Needs from Chat: write the school colour rule below into DSRD 7 section 2 (the colour system's home), as Kain's signed rule for the school pages; Code has written it nowhere but the stylesheet's own note, the tools README and Code's memory.**

# SHIP: each school page in its own colours, on 0.708.257 (S530 side session, 19 November 2026)

**What changed.** Kain asked whether the two school colours should make the seven school pages different from one another, and how. Two rounds of options were rejected as thin and inconsistent. He then asked for one consistent strategy before anything was built ("It can be subtle, but it needs to be consistent"). Code wrote the rule, scanned the NLP page for every coloured mark (147, in 74 kinds), and put each on one map page with its picture, its colour today and its colour under the rule: COLOUR_MAP__School_Pages_School_Colours_19Nov.html in the School Page folder. Kain: "Yes, build it". He then asked for the model to be saved for future reference.

**The rule, for DSRD 7 section 2.** On a school page every marker is the school's colour; only the things you press stay orange. A list of the school's own things (its courses, its chapters, its topics) is marked in its colour, even where a row can be chosen. Each form has one job, the same on all seven:
- the primary for lines and fills (rules beside supporting lines, rings, the timeline, icons, pale circles behind numbers);
- the text-safe form for any coloured word or number (chapter labels, years, figures, digits);
- the deep (secondary) for the one solid panel, the bundle card's school panel (taken down with the brand dark so its words clear 4.5 to 1), and for the solid circles;
- the primary at 30 per cent over white for marks and words on a dark ground;
- the primary at today's strength for faint washes, patterns and tints.

The exceptions are the stars, the tree's leaves (Kain, S512), the Knowledge Hub cards (the same across the site), the Achology logo marks and the illustrations. The header and footer are untouched. It is a colour change only: nothing moves and no size or space changes. The Access All Areas Pass shares the template and keeps the brand's orange.

**How.** It is one switch in school-page.css. On the seven pages, the brand's orange tokens take the school's forms, and every control and exception takes the brand's orange back. Five marks drawn without the tokens are set one by one: the third workshop card's 12 per cent tint, Day 1's circle on the dark band, the school panel, the folds, and the two large faint bubbles beside the history (the bubble picture used as a stencil).

**Proved, through the mirror, in WebKit.** No brand orange is left on any of the seven pages except controls and exceptions (check_no_stray_orange: PASS, 7 of 7). Every control is still orange, and the white words on the school panel clear 4.5 to 1 on all seven (lowest CBP 4.69, Personal Growth 4.76). The solid circles' digits clear it too (lowest CBP 4.64). The whole NLP page was photographed block by block.

**Kept for reuse.** The theme's tools/school_colours/ folder holds the scan, the map builder, the two checks and a README with the method in order.

**For your record.** Life Coaching's own colour is a copper, close to the brand orange, so its page changes least. The gate rows in ANSWER__Access_All_Areas_Page_Three_More_Gate_Rows name the school tutorials heading as "Sample Six Instructional Tutorials From This School". It now reads "Explore Six Sample Tutorials from This School", which matters to whichever session carves that row.

*No em or en dashes in this file; checked before writing.*
