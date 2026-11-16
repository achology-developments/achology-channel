> CHAT DISPOSITION, S470: DONE. Written home in the course page signed spec, section 10 item 2.

**For Chat. What this needs:** read only; nothing to write home unless DSRD 8 or 9 records the curriculum's open and close behaviour, in which case the lines below replace "one closed above shuts at once". Code, S518, 14 November 2026.

# DONE: the course curriculum opens and closes smoothly, all 28 course pages, theme 0.708.075

Kain, on his walk: "when I ... click on one of the plus or minus symbols, it jolts the whole page ... What I want is a far smoother user experience where when people kind of click the plus or the minus button, it just opens and closes. It's really smooth. It's not clunky. And also the page doesn't jolt around." Then: "just fix it and then reload the page".

**What was wrong, measured in WebKit.** (1) Opening a lesson below an open one snapped the open one shut in one frame and jumped the page 264 to match. (2) A lesson's question line appeared in one frame, the row growing 58 to 88 at once, before the paragraph slid.

**What changed.** course-page.js: the lesson above slides shut at the same pace as the new one opens, and the page follows it frame by frame, so the clicked button stays still; with reduced motion it settles in one step as before. The question line is wrapped in one span. course-page.css: the question line slides open and shut with the paragraph on the same .35s, the running time fades in, and reduced motion turns both off.

**Proof, 1440 and 390, four clicks each (open below an open one, close, open, open below again):** the clicked button moves at most 1 pixel; the lesson grows and shrinks over about 20 frames, at most 30 to 42 pixels a frame; the page's scroll moves at most 40 pixels a frame where it jumped 264. Commit e3e0bf75; local, server and zip agree at 0.708.075.

*No em or en dashes in this file; checked before writing.*
