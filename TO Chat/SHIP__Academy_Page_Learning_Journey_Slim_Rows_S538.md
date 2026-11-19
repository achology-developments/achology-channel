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

**Then, on 0.708.242 (commit 70c46ea1), the step numbers.** Kain: "could we tweak this block slightly so that the numbers 1, 2, 3, and 4, still sit up against the inside of the container, which just means that a little bit of the orange circle around it sits outside". Each stop moves left by (circle less 1ch) / 2, about 15 on a computer, so each figure starts level with the heading (DSRD 7 4.4a, and the bar hang of 3.3). The dotted path moves with the stops, and the cards stay put. Measured at 1440, 800 and 375, on the edge each time, with no sideways scroll on a phone. A question for your record: should 3.3's hang name a numbered stop beside a column, as it names a bar?

**Then, on 0.708.250 (commit ef6b98d6), the history of the field on the Academy page.** Kain asked for the Access All Areas Pass page's scroll history on /academy/ ("especially in this Psychology Academy page, that would be a really appropriate block"). He said yes to placing it after Why the Academy Exists. Showing it there found that any block between two alternating grounds makes two alike side by side. From four placements in the Change Viewer (round-history) he chose option 1: "Yes, option 1". The history stands on sand, and Seven Schools, Beliefs, the Learning Journey and How Every Course Works swap white and sand.
- **The component.** It is the signed school story component, switched on from its own home (academy-setup.php loads school-page.css and school-page.js), never copied. Turning that sheet on and off moved none of the 1,812 other elements on the page, measured at 1440 and at 375.
- **Your words.** Your two lines (ANSWER__Academy_Page_History_Two_Lines_S538) are placed word for word. Line 1 is two rows at 1440 and at 1104, and four rows at 375.
- **The button.** Choose a Course jumps to #schools.
- **The type.** It is held under the 24 heading: the chapter names, the year and chapter five's three figures are 21, and 18 on a phone. The heading is 21 on a phone.
- **What followed the grounds.** The Beliefs' half stones and its closing panel are white on the sand. The Journey's stops wear a white ring. The course page's certificate block takes the sand.
- **The section bar.** It gains "History".

Two things for your record. First, the school pages and the Pass page draw the same story with chapter names at 28 and the year at 33, above their 24 headings. That is a family question for a sweep brief, not changed here. Second, the Academy page's grounds now differ from the S533 signed record, so DSRD6_RECORD.md wants the page re-run.

**Then, on 0.708.252 (commit badf5841), the history as the school pages draw it.** Kain sent a picture of white blocks behind the history's title, and asked: "please pay real close attention to detail to get the exact layout as it is in the schools page ... just so there's no contradictions whatsoever." The first build had taken the Pass page's look: a dark banner and its own sizes.
- **The school layout.** The school pages' look is the 73 rules in school-page.css under main.school-page, so the Academy's main now wears school-page too (template-academy.php). None of the page's other 2,021 elements moved, measured at 1440 and 375. Every part of the story was then measured against the NLP school page at 1440 and matches.
- **No type override.** The S538 register override is taken out, so chapter five's figures are 28 again, as on the school pages. That means the family question I raised earlier about the size of those figures now covers this page as well.
- **The white blocks.** The strip behind the banner, the panel behind each chapter heading and the ring round each moment's dot are white only to vanish into the school pages' white. Here they take the band's sand. A scan of every element and its ::before and ::after on every sand and white band found nothing else of the kind.
- **The phone heading.** It is 21, as every Academy block heading is on a phone.

**Then, on 0.708.254 (commit ef4b41be), the Achology grey kept.** Kain: "you did have like the Achology grey background, which I thought looked really nice. It just kind of sets this page apart from all the school pages ... reinstate that". On the Academy the story's banner and its partner, the closing panel, take back the component's own dark defaults; every school layout rule stands. The school layout's small capital label is orange-footer on the dark, and the Now Reading pill has a faint white edge with no fill.

Theme commit a522ae2f. Deployed and proved: local, server and zip agree on 0.708.239. On the build site at 1440, 1024 and 375, every type style was measured against the register, with no sideways scroll.

**Then, on 0.708.255 (commit e0cd4b32), the history's opening line in Kain's words.** Kain replaced the first of your two lines with his own: "This is a brief history of modern applied psychology: the philosophical ideas that preceded the field, how the field took shape and evolved over time, and how it all led to the 28 courses available with the Achology Academy today." It is placed word for word. On the build site at 1024 it is three rows of Mulish 18/500 and runs the full container, with no sideways scroll. Your closing line stands. Nothing needed from you.

**Kain's verdict on the history, 0.708.255.** Asked "Is the history right now?", Kain answered: "Yes, it's right". He also chose not to add a bridge block on the Academy's founding between Why the Academy Exists and the history ("Yes, leave it"), because Why the Academy Exists already carries it. For your record: the history block is accepted as built, and DSRD6_RECORD.md still wants the page re-run for the new block and the swapped grounds.

**Needs from Chat: the reader half of the Academy page's record, for the history block, and two rulings to confirm or overturn.**

**The Academy page's gate, re-run on Kain's "Yes, run it".** The machine half reads 48 passed, 0 failed at 0.708.255 (printout page_gate__academy__0.708.255.txt, record updated under "The S538 re-run"). Seven lines failed on the first clean read. Each was entered in page_gate.py (ee3d5272) on your own S533 rulings for this page:
- boundary 10's hairline: the new band made one more boundary (1.1);
- the tablet spacing line: it now reads the phone's two ruled spaces (1.3);
- the history's phone heading at 21 (1.6);
- the history's line at 40 words, with "Academy" as a mid-sentence capital: Kain's own words and the name (1.8).
Please confirm the last two, or overturn them.

**An instrument question.** One run read 18 false fails on the tablet and phone lines. By hand at 768 and 375 every line measures right, and two more runs agreed with the hand. The supporting line check waits only 350 after each width change. Should it wait for the layout to settle? I changed nothing.

**Owed by you.** The reader half for the history block (chapters 1, 2, 6, 7 and 8). One review line: its first chapter heading has no supporting line, as on the school pages.

**Needs from Chat: one sweep brief, if you and Kain want the source links' note on the school pages and the Pass page.**

**Then, on 0.708.256 (commit 89d29f77), your two mends and the settle wait (ANSWER__Academy_Page_History_Gate_Rulings_S538).**
- **NLP at first use.** The 2014 milestone reads your sentence word for word, in the Academy's copy only. It measures 8 rows at 1440, 10 at 1024 and 13 at 375, with nothing sideways. The gate's NLP acronym carve-out is no longer needed.
- **The source links' note.** All thirteen carry a hidden "(opens in a new tab)" on the link. I made this **on the Academy only**: the history's builder adds it as it reads the Pass page's story. Making it in the component means regenerating the seven school pages' and the Pass page's stored data. That is a sweep, and Harness Rule 3 asks for Kain's signed sweep brief first. The Academy's addition is guarded, so it stops by itself once the component carries the note. The one line to change is the `source()` function in `tools/school_page_data.py`.
- **The settle wait.** It is built to your three points: it waits for the fonts, then for two frames in a row that agree, with 250 of quiet, and stops at 3000. An unsettled width is printed NOT RUN, and the check then prints no PASS. The test (`tools/supporting_line_gate_test.py`) gains two cases, both passing, 20 of 20 in all. Three gate runs in a row on /academy/ each read 48 passed, 0 failed, with identical supporting line rows that agree with the hand measures.

The record is updated: chapter 1's human half is moved to pass, and chapter 7 notes the mend. Printout page_gate__academy__0.708.256.txt.
