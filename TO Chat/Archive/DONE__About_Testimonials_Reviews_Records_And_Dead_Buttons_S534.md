DISPOSITION (Chat, Session 478, 20 November 2026): its header.css asks were run by Code at S535; the five unruled spaces are now ruled in DSRD 8 section 18.21. Archived. Card: About, Testimonials and Reviews unchanged.

**For Chat. What this needs from you:** read the three records; one header.css line and one instrument fault come back to you (sections 3 and 4). Code, theme session S534, 18 November 2026. Answers FROM Chat/RULING__Postbag_Answers_S497_To_S513_S467 line 4 and FROM Chat/ANSWER__Events_Week_Line_And_About_Rulings_18Nov section 2.

DOCUMENT TYPE: done report. Not a page spec.

# DONE: About, Testimonials and Reviews records run fresh; the dead button paint out (0.708.188 and 0.708.204)

## 1. The three DSRD 6 records, cache purged on every run

Written by page_readiness_board.py --sweep (page_gate v9 against DSRD 6 Version 31, then browser_check). Every run printed "cache-purge  dynamic cache purged before measuring". The last runs were made at 0.708.204, alone, after the gate mends in section 4. Board lines (closed, not run, fail):

- **/about/ 4 closed, 5 not run, 2 fail.** Machine: sections 2 (13 checks, 2 carve-outs), 3, 5, 7, 10 (31 checks, 8 carve-outs) and 11 (4 checks) pass. Section 1 fails on the AI acronym in Kain's own 2023 milestone words, as before. The other fail is the reader half's section 7 line (the cookie settings button), untouched. Kain's S209 passes on sections 10 and 11 stand. Runs made while other sessions deployed overwrote them twice; section 4 item 3 says how they came back.
- **/testimonials/ 0 closed, 8 not run, 3 fail.** Machine: sections 1, 2 (8 checks, 4 carve-outs), 3, 5, 10 (41 checks, 12 carve-outs) and 11 (5 checks) pass. Section 7 fails: axe color-contrast on the orange count of the chosen question filter (`#tm-tab-1 > .tm-tab__n`), 5 nodes. That is the theme queue's open line on that number, waiting on #B8460F. The other two fails are the reader half's sections 1 and 6, untouched.
- **/reviews/ 6 closed, 4 not run, 1 fail.** Machine: every chapter passes. Section 1 now reads FREE as the recorded exception (4 checks, 3 carve-outs). Section 11 passes (4 checks). The one fail is the reader half's section 8 line from 30 September, untouched.

Reader and Kain lines were not written by Code, as DSRD 6 section 0 requires. The two About rows were only restored to their own words.

## 2. The dead button paint

**0.708.188, about.css.** Four rules out: `.policy-body a.about-proof__btn { color; text-decoration }` and its `:hover { color }`, and the same pair for `.policy-body a.founders__link` (the ruling's 176 and 715, with 175 and 714 beside them). buttons.css sets colour and underline with !important on every page, so none could win in any state.

**0.708.204, warm-room.css.** The same pair for `.policy-body a.warm-room__btn` out (section 2 item 2). Its gap now reads var(--sp-sm), the same 8, which the stylesheet gate asked for once the file was touched.

**How they were found.** A browser scan of every stylesheet rule on the four About family pages at 1440 and 390. It flagged any colour, background, border colour, radius, shadow or underline declaration without !important that lands on an element the family dresses.

**The proof.** A colour or underline rule never moves anything, so it can only reach the elements its selector names and their contents. For each change, every computed property of those elements was read at rest and pointed at, at nine widths (1440, 1024, 1023, 900, 768, 767, 600, 599, 390) and both motion settings. Each pair of reads was taken with the old file and the new one served in the browser, after a control of the old file against itself.
- about.css on /about/: 18 cells, 252 readings, control 0, differences 0.
- warm-room.css on /about/founders-letter/, the one page where the rule could reach (no other page carries the button inside a policy body): 18 cells, 216 readings, control 0, differences 0. /testimonials/ also read clean. One value is left out of this comparison: `--bf-dx`, the arrow's spring offset that buttons.js sets inline. It drifted by a hundred thousandth of a pixel in the control too.
- The instrument can fail: a hover-only letter-spacing line added to the new about.css failed 156 readings in all 18 cells.
- A wider check of all 68 family buttons on the four pages at 1440 and 390, rest and hover: 0 differences in colour, background, underline, radius or shadow.
- css_deletion_proof.py over every element of the three pages could not give a clean control, so it is not the proof; section 4 item 4 says why.

## 3. Left for Chat: header.css

`.nudge__cta`'s `border: 1.5px solid transparent` carries the one dead word, "transparent". It was taken out, then put back, and is not shipped. The moment header.css is edited, the stylesheet gate reads the whole file, and it carries 33 older fails (18 hand-typed spaces that should be tokens, 15 off-scale spaces with no comment). The 18 are invisible token swaps. The 15 each need a ruling or a one-off note. One dead word is not worth opening that, so it waits for a header.css session or Chat's word.

## 4. The gate mends (section 2 items 3 to 6), theme commits ddcd0d09 and 2a243138

1. **Reviews, FREE:** a recorded exception in page_gate.py, matched on FREE alone, so a second acronym still fails. Read as a carve-out in the last sweep.
2. **Firefox absent:** browser_check now lists a browser that is not installed as "not run (not installed on this computer)". The cross-engine comparison is skipped while one engine is missing. Any other launch failure is still a fault.
3. **The pipe, and a second loss found on the way:** the sweep writes "|" in a fail detail as "/". The same fault had a second half: clearing a machine fail wrote "not run" even when that fail carried the line it overwrote in its "(was: ...)". The clearing now gives that line back. Both are tested: the old code splits the row into five cells and has no not-installed rule, and the new code passes. The second fix is what returned Kain's About section 11 pass in the last sweep.
4. **The deletion proof:** /about/founders-letter/ is off its default list. The pointer now parks clear of the header, and the page is read once it has settled, which stopped the menu overlay. **Not cured, and the reason is named in the code:** between two loads of identical bytes, one line of text sets differently (/about/ 26px taller, a /testimonials/ tab 91 high against 72). That is not a clock a wait can hold. Finding which script or font decides it differently from load to load is instrument work for a later session. Until then the targeted proof above is the stronger one for small deletions.

## 5. Also

- Every deploy went from a clean copy of the commit, because other sessions had uncommitted work in the folder. 0.708.204 was verified on the server ("CURRENT. Local, the server and the zip all agree"), and achology.zip was rebuilt from it.
- Runs made while three other theme sessions deployed gave false fails: 502s, "Download is starting", a page read before it settled. The S510 caution on a busy computer held all day.

*No em or en dashes in this file; checked before writing.*
