**For Chat. What this needs from you:** your rulings on the six things in section 4, which are what is left of the page gate's picture, spacing and wording rows on a course page after today's mends. They sit beside the rulings already asked in DONE__Page_Gate_Reads_Draft_Pages_Signed_In_S479. Code, theme session S481, 11 November 2026, on Kain's order for the hidden faults with the page frozen as built.

# Status in the words The Harness requires

Changed, verified, committed, pushed and deployed: theme 0.707.939 (commit 6990e4ca) on the build site, all 28 course pages. For the course page itself: **built, gate open: the course page's DSRD 6 record** (no record yet; 56 rows still read fail on course 001, almost all waiting on your rulings).

# 1. What changed, and nothing a reader sees moved

Four faults the gate reported on a draft course page, each with one right answer. DSRD 6 section 7: "The scan must come back with zero failures, or each failure fixed or recorded as an exception per section 0." DSRD 7 section 12.3: "Width and height are mandatory on every image element, in real intrinsic pixels."

- **The three course facts under the video.** Each fact's link sat beside its dt and dd inside the group, and a group in a definition list may hold only a dt and a dd (axe definition-list, serious). The link now sits inside the dd. It is positioned against the group as before, so it covers the same box.
- **The five lesson tiles.** On a tablet and a phone they are one row that scrolls sideways, and nothing in it could be reached from the keyboard (axe scrollable-region-focusable, serious). While the row scrolls it now takes a place in the Tab order, with the site's own focus ring; on a computer, where all five show, it takes none. This one is in course-page.js.
- **The tick beside "Then You Decide".** It carried neither a name nor aria-hidden; it is decoration beside its words, so it is hidden from a screen reader.
- **The three review film pictures.** They carried no width or height; each now states its real size, 960 by 540, read from the file's own header by the builder.

The three markup mends are in the page builder (the course page design folder's build.py); the 28 data files were regenerated with tools/course_page_data.py and the signed copy was put back with tools/course_copy_place.py (27 courses read back equal to the signed copy).

# 2. The proof

- **The data.** A script took each of the 28 committed data files, made the three intended changes to it, and asked whether the result is the file now on disk: 28 of 28 equal, 56 links moved, 28 ticks hidden, 84 pictures sized, nothing else different. Its first run failed on all 28 because its own tick pattern was wrong, so it can fail.
- **The rendered pages.** Every element's box (kind, classes, place, size) in the page body and the footer sign-up was read on courses 001, 009 and 023 at 1280, 1024, 834 and 390, signed in as the gate reads a draft, before the deploy and after: 12 of 12 readings the same, same page heights. A control, two readings of the untouched site, was also 12 of 12 the same; an earlier, cruder reading differed on 4 of 12 from scroll state alone, which is why the reader was steadied first.
- **The gate, course 001.** Before: 27 passed, 58 failed; accessibility-scan 2 violations; icon-hidden-or-named 1; image-dimensions 3 with no size and 2 that do not match. After: 29 passed, 56 failed; accessibility-scan "axe 4.10.2: zero WCAG 2.2 AA violations"; icon-hidden-or-named "all 241 icons this theme draws are either hidden from a screen reader or named"; image-dimensions down to the 2 that do not match (section 4, items 1 and 2).
- **The deploy.** deploy.py's three proofs: server identical to local's runtime set, the zip matching the theme, local and server both 0.707.939.
- **Not measured.** WebKit. The readings are Chrome's. Neither mend can differ by engine as far as I can reason it (the link has all four offsets set against the group; the film pictures' box is set by the stylesheet, absolute and 100 per cent), but that is reasoning, not a measurement. The focus ring on the lesson row was read from the computed style, not looked at.

Rendered page, a draft, so signed in: https://achologytest.com/academy/neuro-linguistic-programming/diploma-modern-applied-psychology/

# 3. Two things about how this session ran

- **The two shared notes files were not on this Mac at the open** (course-page-theme-build.md and course-page-model-review.md, which the S477 report says hold the handover). The old main session's notes folder is gone and the scratch area was emptied when the Mac restarted at about 12:19. The fault list was rebuilt from a fresh gate run on course 001, so anything the notes held beyond the gate's rows is lost unless it is in the S477 and S479 files here. Kain's own ask from pick 308, a hint that the outcome cards can be clicked, as four options, is still not started.
- **The check sheet harness ran.** Every Job steps 1 to 4 passed with proofs (DSRD 6 read whole). Built Pages steps 1 to 3 (Penpot frame, new parts, Kain's signature on the frame) cannot pass on a fault fix to a page signed outside Penpot; I recorded each as an exception with its reason and Kain's opening words for this session, rather than a pass. The S479 RULING already asks you about those three steps; overturn mine if you rule otherwise.

# 4. What is left on the gate's picture, spacing and wording rows, for your rulings

I changed nothing for any of these.

1. **The small instructor portrait** (kain-ramsay-128.webp) states 32 by 32 and the file is 128 by 128. DSRD 7 12.3 gives one answer, the real 128. It is mine to mend in the builder once I have checked the stylesheet sets its size everywhere it shows (it does where it shows today). Left out of this change set only to keep it to one regeneration; say if you want it held.
2. **The Stripe badge** is drawn from inline data, so the gate reads it as a picture with no filename, no lazy loading and a size that does not match (four rows). Either the gate should leave inline drawings alone, or the badge becomes a named file. Yours to rule.
3. **The six free lesson stills are .jpg on every course (168 files), and 12 pictures on the page carry no srcset.** A picture production job (new files, an upload, the data). Is it Code's under Kain's hidden faults order, or does it want its own brief?
4. **The video's poster picture** (course-001.webp, 440 by 248) is the largest picture above the fold on a computer and carries no fetchpriority; on a tablet and a phone it is below the fold and not lazy. It cannot be both. This is the shape of DSRD 6 section 9's named exception ("the desktop view wins"), which names the subject page and the Articles lists only. The hero's own picture already carries fetchpriority high. Yours to rule.
5. **Fourteen declared spaces off the scale** (the gate's spacing-scale row at each width): the hero's top padding 51 (35 on a tablet and a phone), 128 and 96 above the outcomes, 20 above a caption, several 12s in the pricing card, a 2 and a 1.7 between rows, and four more. Every one is inside a block Kain signed, and correcting any of them moves something a reader could see, so under DSRD 6 section 0.1 none is mine to change: each wants recording as an exception, or putting to Kain rendered.
6. **Acronyms.** SoMAP is used in the certificate block's fourth step before it is spelled out (words, yours). The gate also names "II" in "Senior Achologist II", which is a role line and outside the rule by section 1.

OWED BACK: your rulings on section 4, to FROM Chat, for the theme session.

DOCUMENT TYPE: DONE

*No em or en dashes in this file; checked before writing.*
