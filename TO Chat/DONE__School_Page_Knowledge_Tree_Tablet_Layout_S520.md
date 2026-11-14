**For Chat. DONE, Code, school page theme session, S520, 14 November 2026, theme 0.708.073 on the build site.** The knowledge tree's tablet layout (768 to 1279 wide) is changed on Kain's pick.

**What happened.** Kain saw the block in a Safari window about 1000 wide, where it takes the single list built at 0.708.065 (the tree above, ten topics in one column, half the screen empty), and asked to adjust the tablet layout "so that ... there's like two columns". Code showed four looks in the Change Viewer (round-ktab.js, proved by tools/viewer_proof.py): 1 the tree on top with the topics in two columns (Code's recommendation), 2 the same with one column of titles, 3 a smaller tree, 4 the tree beside the single list, staying in view. He chose 4: "Option 4 please".

**Built.** From 768 to 1279 the tree stands on the left, 300 wide, held in view (sticky, 120 below the top), while the single list of topics and the chosen topic's titles under it are read on the right. Under 768 (phone) and from 1280 (the tree beside two topic columns) nothing changes. Read on the build site in WebKit at 768, 834, 1000, 1279, 1280 and 390: no topic name wraps (the list is 372 wide at 768), nothing runs sideways, the tree stays in view as the list scrolls, 1280 and 390 are as before.

**For Chat to write home.** A second band exception for this block, beside the 1280 one you wrote into DSRD 7 section 4.2: from 768 to 1279 the block lays the tree (300 wide, held in view) beside its single list. The 300 and the 120 are one-offs annotated in school-page.css. The pick is school PICKS pick 22.

*No em or en dashes in this file; checked before writing.*
