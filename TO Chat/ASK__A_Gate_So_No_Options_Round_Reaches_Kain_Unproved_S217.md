**For Chat. What this needs from you:** one rule written into The Harness (Rule 7, and Layer 2's hook list) saying no Change Viewer round opens in Kain's Safari unless `tools/viewer_proof.py` has passed on that exact round in the last twenty minutes; the hook is already built and wired on Kain's direct order, so this asks for the words, not the work. Code, theme session S480 (a side session of the course page sitting), 11 November 2026.

# ASK: a gate so no options round reaches Kain unproved

**Kain's words (course page sitting, 11 November 2026, angry and tired):** "please just make these options work. This has been maybe 4 or 5 times now. When you present options to me, they don't work. Please fix this permanently. What is the permanent fix for giving me options that work?"

**What was wrong, measured in WebKit on the round open in his Safari** (the Certification stance round, four options). Three of the four options opened with the block that changes about 2,200 pixels above the window on a computer, and all four about 4,800 above it on a phone; Before then showed a different place again. Two causes in the one shared viewer: it worked out where to land once, a moment after the page loaded, and a page still laying itself out then slid away with nothing to correct it; and Before and After kept his place as a count of pixels from the page top, so an option that made the page taller or shorter showed him a different block. A third, found in the run: where the option adds a block the Before page does not have, there was nothing to keep the place against at all.

**What Code has built (theme repository, previews/_change-viewer, tools, harness).**
1. The viewer now lands on the part the option names, re-measures for five seconds and puts it back the instant the page moves, and stops the moment he scrolls or presses anything. Before and After keep his distance from that part; for a new block, from the named blocks either side of it. A round whose part is missing, or whose After is the very same page as Before, says so in the bar: "This option could not be shown. Tell Claude." Every round file works unchanged.
2. `tools/viewer_proof.py`: presses every option or switch, Before and After, Replay, Computer and Phone in WebKit and passes only when the part is on screen every time, in the same place after Before and After, the After page differs from Before, and the page raises no error. It warns when Safari holds two tabs of one round. Its acceptance file proves it fails on the old viewer and passes on the new one.
3. The hook `h12_viewer_proof.py` with its acceptance file (ten cases), wired on every shell command: a command that opens a `/viewer/?round=` address in Safari is refused without a pass from the last twenty minutes, and a round file or the viewer edited after its pass is unproved again. Built and wired without waiting, under Rule 14, on Kain's words above; the precedent is H11's four designs check, added the same day on his word.

**What only Chat can do.** The Harness document does not name H12 or the proof. Until it does, the wall stands in code and in the viewer's README but not in the rules. Asked: one sentence in Rule 7 (a round is proved by the tool before it is opened to him; one round, one tab) and H12 in the hook list, replacing whatever line the growth governor needs to leave. If Chat rules the hook should not have been wired before the words, say so and Code unwires it the same session.

**Not covered, said plainly.** The gate reads shell commands only: a round opened in Safari by another route (the browser tools) is not stopped. The proof runs on the first page a round names, not every page in its Page switch. Kain's already-open tabs keep the old viewer until that tab is reloaded.

OWED BACK: the rule's sentence and H12's line in The Harness, or a ruling to unwire.

*No em or en dashes in this file; checked before writing.*
