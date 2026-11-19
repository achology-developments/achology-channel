**Needs from Chat: nothing to build. One record line: the Academy page's signed Learning Journey block changed shape after the page was signed.**

# SHIP: the Academy page's Your Learning Journey block is Slim Rows, on 0.708.239 (S538, 19 November 2026)

**What changed.** On /academy/, the block Your Learning Journey with the Achology Academy (the S530 Lit Path) is more compact on a computer. Each step's picture narrows to 160, and its link now stands beside its price, on one line. The review's rating is set across: the dial on the left, and the stars, label and count on the right. The words, the path and every movement are unchanged.

**Why.** Kain: "The depth of the block is actually just kind of overwhelming. It's just kind of ridiculously deep ... We just need to make this more compact." He saw four compact options in the Change Viewer (previews/academy-page-s527/round-journey.js) and said: "Slim Rows makes sense".

**Type and gaps, on his second instruction.** Kain: "check your use of fonts, font size, font weight, and spacing ... this is not in alignment with our in-house standards." Measured in the block before the pass:
- the review quote was Como 24/500, as large as the block heading;
- the 4.66 figure was 42/600, louder than the heading and outside the weight rule;
- the small capital labels were at 0.1em;
- "out of 5" was 14;
- the review link was 14, beside step links at 16;
- the price was in the reading face.

Now every style is a DSRD 7 row. The quote is the Pull Quote (Mulish 18 italic). The figure is Como 21/700, the labels 14/600 at 0.08em, "out of 5" the 12 Overline, the links one size at 16 and the price Course Card Price Como 18/700. On a phone each of these steps down one size.

The gaps are as signed at S530. There is 24 between the steps and between the columns, 24 inside each card, 8 from label to title and 16 from title to price, and 32 inside the review panel. The rows are written beside the rules in academy.css. Kain, on the corrected round: "Yes, build it".

**Depth.** At 1440 the block went from 1,249 to 1,044. At 1024 it went from 1,482 to 1,285. On a phone the layout is unchanged, apart from the type stepping down.

**For your record.** The Academy page was signed whole at S533 (post 33498). This block now differs from the signed preview's Lit Path at computer width. The Lit Path note in academy.css stands, and the new Slim Rows note sits under it. The page's DSRD6_RECORD.md may want this block re-run on the next gate pass.

**In passing.** At session open the deploy check found three school film pictures (images/schools/film-pass*.webp) that differed between the server and local. They came from the Access All Areas Pass session's commits, not mine. I deployed from a clean worktree of HEAD (a522ae2f), which includes that session's committed pictures.

**Then, on 0.708.240 (commit d91044ec), the review panel.** On the built block Kain said: "the top bit is crammed, what our students say, then the quote is just totally crammed, and then the bottom block is ... just beyond spacious ... a complete waste of space." The rating's half had been taking every spare pixel of the 731 panel (427 for 179 of content). From four options in the Change Viewer (round-panel) he chose The Quote Leads: "Yes, build 2". The rating now keeps its own height as a footer, with 32 inside. The quote takes the rest of the panel, centred, with 116 above and below, 24 under its label and 32 above the name. The block stays 1,044. Measured on the build site at 1440. Another session shipped its own 0.708.240 and then 0.708.241 on top of this commit, and the build site serves 0.708.241 with this change in it.

Theme commit a522ae2f. Deployed and proved: local, server and zip agree on 0.708.239. On the build site at 1440, 1024 and 375, every type style was measured against the register, with no sideways scroll.
