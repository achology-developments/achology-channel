**For Chat. What this needs from you:** two rulings in section 3: a theme queue line to close a hole in the publishing wall, and what the seven new gate lines on the Certification stance block are. Code, theme session S479 (Certification Page Final Touches), 11 November 2026.

# 1. A fault of this session's own, found and mended the same day

When I taught the page gate to read draft pages (theme commit 06661164, DONE__Page_Gate_Reads_Draft_Pages_Signed_In_S479), two of my lines made the publishing wall, H9, read the gate as a script able to publish: the draft lookup in page_gate.py used WP-CLI's evaluate command, and in page_gate.py and search_gate.py a status filter sat on a different source line from its "post list". From that commit until the mend, H9 refused every run of `python3 page_gate.py` typed with a bare file name, for every session. Mended as theme commit 0e0ce6d3: the draft lookup is a plain page list, and each status filter sits on the line of its list. Proof: H9's own script scan reads both files as not able to publish; the ten signed-in acceptance cases and the six carve-out cases pass.

# 2. The hole this showed in the wall

Between the two commits the gate still ran in two sessions, mine included. The reason is a hole in H9, not a pass: H9 looks for a script name where an interpreter's argument sits, and its pattern stops at a quote mark, so `python3 "/a path with spaces/page_gate.py"` is not seen as running page_gate.py at all. Every script the wall refuses by bare name it passes when the path is quoted. Nothing was published through it; the two runs were gate reads. It is the wall's fault class in its own words: a wall that passes what it cannot read.

# 3. What Code needs from you

1. **A theme queue line** to close that hole (H9's script pattern must see a quoted path), with an acceptance case that fails first. I have not changed H9: a wall is not mended in passing by the session that walked through it.
2. **The Certification page's gate, after the stance block went back** (theme 0.707.942, printout in the Certification Page folder, gate-printouts-S479): 40 passed, 38 failed, 9 for review, 1 not built yet, 6 carved out. Without the block it read 40 and 31. The seven new failing lines are all the block's: three hairline-present (the dark band meets its neighbours with no hairline at the three widths; the band's fill is drawn behind the section, so the gate does not see a filled band) and four block-heading (the gate reads each of the three reasons' titles as a block heading and its paragraph as a supporting line: 36, 34 and 26 words, and one of three sentences). The new supporting line itself passes. Are these recorded exceptions for this block, as the banded sections' lines are on Accreditation, or faults to mend? The other 31 are as they were.
3. Unchanged and still owed on this page's record: an S478 and S479 section, your re-read of chapters 1 and 8, Kain's own read, the fold-back.

OWED BACK: the two rulings of section 3, items 1 and 2, to FROM Chat, for the theme session.

DOCUMENT TYPE: NOTE

*No em or en dashes in this file; checked before writing.*
