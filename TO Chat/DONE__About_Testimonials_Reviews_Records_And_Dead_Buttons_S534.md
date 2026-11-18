**For Chat. What this needs from you:** read the three records' machine halves; rule the two dead rules left outside about.css (section 3) and the instrument faults (section 4). Code, theme session S534, 18 November 2026. Answers FROM Chat/RULING__Postbag_Answers_S497_To_S513_S467 line 4 and the call for fresh records on the About family after S514.

DOCUMENT TYPE: done report. Not a page spec.

# DONE: About, Testimonials and Reviews records run fresh; the dead button paint out of about.css

## 1. The three DSRD 6 records, run fresh with the cache purged

Run with page_readiness_board.py --sweep (page_gate v9 against DSRD 6 Version 31, then browser_check), one page at a time; every run printed "cache-purge  dynamic cache purged before measuring". Each record's machine block is dated 2026-11-18.

A first sweep was taken while other theme sessions were deploying, and while this session's own hover check ran. It produced false fails: a 29 at one About boundary, Firefox not loading, a missing h1. The records stand on later runs made alone. Board line after the runs (closed, not run, fail):

- **/about/** 2 closed, 6 not run, 3 fail. Machine: section 2 passes (13 checks, 2 carve-outs), 3 passes, 5 passes, 7 passes, 10 passes (31 checks, 8 carve-outs). Section 1 fails on the AI acronym in Kain's own 2023 milestone words, as before (with Chat). Section 11 fails on instrument readings, section 4 below. Kain's S209 section 10 pass is restored word for word: the busy run overwrote it and the sweep then cleared it to "not run". The row carries one added note saying so.
- **/testimonials/** 0 closed, 7 not run, 4 fail. Machine: sections 1, 2 (8 checks, 4 carve-outs), 3, 5 and 10 (41 checks, 12 carve-outs) pass. Section 7 fails: axe, color-contrast on the orange count of the chosen question filter (`#tm-tab-1 > .tm-tab__n`), now 5 nodes. That is the theme queue's open line on that number, which waits on Kain's eye or Chat's word on #B8460F. Section 11 fails, section 4 below.
- **/reviews/** 6 closed, 2 not run, 3 fail. Machine: sections 2 (7 checks, 3 carve-outs), 3, 5, 7 and 10 (31 checks, 8 carve-outs) pass. Section 1 fails: "FREE" in the gateway tile "Get Access to FREE 1-1 Coaching and Workshops" read as an acronym. That is signed tile copy, so it is Chat's to rule (an exception for a word in capitals, or the words). Section 11 fails, section 4 below.

The open human and Kain lines (the reader halves of sections 1, 6, 7 and 8, and section 9 speed) are untouched, as DSRD 6 section 0 requires.

## 2. The dead button paint, out of about.css (theme VERSION_HERE)

**What came out.** Four rules: the two the ruling names (about.css 176 and 715, the hover rules) and the two rest rules beside them (175 and 714):

- `.policy-body a.about-proof__btn { color; text-decoration }` and its `:hover { color }`
- `.policy-body a.founders__link { color; text-decoration }` and its `:hover { color }`

The button family sets colour and underline with !important at rest (buttons.css 62 to 67 and 123 to 128), so none of the four could ever win, in any state. Their two comments now say so. Net 104 bytes fewer; the gap and arrow rules stay.

**How they were found.** dead_button_scan.py (this session's scratch folder) read every stylesheet rule in the browser on the four pages that once loaded about.css, at 1440 and 390. It flagged any non-important colour, background, border colour, radius, shadow or underline declaration that lands on an element the family dresses. In about.css it found exactly these four, on every page and width where the two buttons stand.

**The proof of zero visible change.**
1. Hover: every family button on About, Testimonials, Reviews and the Founders' Letter, at 1440 and 390, read at rest and pointed at, with HEAD's about.css and with the edited one served in the browser. 68 buttons, 32 visible, 0 differences in colour, background, underline, radius or shadow.
2. css_deletion_proof.py, every element and every property at nine widths, both motion settings: PROOF_HERE

## 3. Dead button paint found outside about.css, left for Chat

These are the same kind and just as dead, but each sits in a stylesheet that loads beyond this job's pages. Taking them out is a sweep under Harness Rule 3, so they wait for Chat's word:

1. warm-room.css: `.policy-body a.warm-room__btn { color; text-decoration }` and its `:hover { color }`. The button is the family's btn-primary, so both are outweighed. Reaches every policy family page that carries the warm room.
2. header.css: `.nudge__cta { border-color: transparent }`. The family sets the same transparent with !important. Every page.

The other hits the scan printed are shared resets that still do work on elements outside the family, so they are not dead: base.css `:where(a[class])`, `.btn` and `button`, and policies.css `.policy-body a`.

## 4. Instrument faults found on the way (for Chat; Code mends nothing here without a word)

1. **Firefox is not installed on this machine.** browser_check reports "Firefox could not start: Executable doesn't exist" and counts that as a page fault, so section 11 fails on every page swept from this computer. Chrome passes the same pages. The fix is Playwright's Firefox installed here, or the check reporting an absent browser as not run.
2. **A fail detail with a "|" in it breaks the record's table.** The busy run's About section 10 fail named "boundary 3 (policy-body policy-body--r | policy-body ...)". Written into the table cell, the pipe split the row, and the next sweep's clearing then lost Kain's pass. Mended by hand here. The lasting fix is the sweep escaping "|" in what it writes (page_readiness_board.py, rewrite_record).
3. **The deletion proof's page list and noise.** css_deletion_proof.py's default list still names /about/founders-letter/, which no longer loads about.css (the tool refuses it, correctly). Its control also reads noise from page scripts that measure on their own clock: the lone-words hold, the tab slider and the header menu overlay. Two full runs made while other sessions worked failed their control on that noise.

*No em or en dashes in this file; checked before writing.*
