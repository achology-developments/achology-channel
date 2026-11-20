CODE DISPOSITION, S540: WAITS ON Kain's yes, put to him in the S540 Code session (20 November 2026).
NEEDS: Code, the theme session, to draw the "14-Day Money-Back Guarantee" link's focus ring in the AA orange #B8460F on 36 pages, by one rule in course-page.css, then measure, gate and read back. WAITS ON Kain's yes, put to him by the main Code session of S540; do not build until this file reads "Signed:".

# SWEEP BRIEF: the guarantee link's focus ring in the AA orange, 36 pages

**From:** Chat, 20 November 2026, a side session of the S540 Access All Areas Pass record. **To:** Code, the theme session. **Signed:** Kain, 20 November 2026, "Yes, make it", answering the question put to him in the S540 Code session after he was shown the before and after pictures of the focused link.

## The fault, as Code measured it (S540, WebKit, the Pass page at 1280 and 390)

The guarantee link in the pricing card (`.pn-f2__guar a`, named a link in the writing, `a.bf-in`, by buttons.js) takes its keyboard ring from the general rule in base.css: `:focus-visible { outline: 2px solid var(--color-orange); }`, the brand orange #ED6922. It stands on the guarantee's own pill, the orange at 8 per cent over white (course-page.css, q4, `background: rgba(var(--color-orange-rgb), .08)`), which mixes to about #FEF3ED. There the ring reads **2.9 to 1**, under WCAG 1.4.11's 3 to 1. Chat's own sum from the two colours agrees: 2.90.

## The pages, exactly 36

1. The 28 course pages (the theme's data/course-page).
2. The seven school pages: NLP, CBP, MIW, Life Coaching, Mental Health, PGD and Person-Centred (data/school-page: nlp, cbp, miw, lc, mh, pgd, pc).
3. The Access All Areas Pass page, /access-all-areas/.

All 36 draw the guarantee from one function in course-page.js (`guarantee()`), so they take the one rule below and none is edited by hand.

## The ruling: route 1, as for the payment tabs at S530

The same fault was ruled at S530 on the payment tabs (`.pn-seg__b`), 2.87 on their grey, in ANSWER__School_Page_Payment_Tabs_Ring_And_Spoken_Names_S530 (FROM Chat's Archive), and Code built it at 0.708.207. The same route applies here, for the same reasons: #B8460F is DSRD 7's own AA-safe orange (`--color-orange-link`), already this very link's resting colour on every other link in the writing, so a registered colour meets the bar and no exception is needed. The ring stays orange, the same 2 width and the same offset; only its shade deepens, and it shows only to a keyboard user.

## The change

- **File:** `course-page.css` in the theme, beside the guarantee's other rules (ft2 and q4).
- **The one rule:** the guarantee link's focus ring draws in `var(--color-orange-link)`. A rule of the form `html:root .pn-f2 .pn-f2__guar a:focus-visible { outline-color: var(--color-orange-link); }`, with a comment naming this brief. Width, style, offset and corner stay as the general rule gives them. Read the cascade on the rendered page; the colour that wins on `:focus-visible` is the one that must read #B8460F.
- **The school pages:** the colour switch in school-page.css hands every `a` the brand's orange tokens back (`--keep-link`), so on the seven schools `--color-orange-link` inside the link is still #B8460F. The pill behind it may take the school's tint, since `.pn-f2__guar` is not on the keep list. Measure the ring against whatever band each page actually draws; do not assume the Pass page's.
- **Not touched:** the general `:focus-visible` rule in base.css, every other `a.bf-in` on the site, the banner's money-back line (`a.course-hero__refund`, which Code's walk passed), the link's words, its resting and hover colours, the pill, and the shield. No word, size, space or layout moves.
- **Bump the stylesheet version.**

## The colour and its target

**#B8460F, at 3 to 1 or more on each page's own band, at every width.** Chat's sum on the Pass page's pill (#FEF3ED): **4.9 to 1**. On white it is 5.36.

## The checks

- On each of the 36 pages, Code focuses the guarantee link by keyboard and measures the ring against the band it stands on, at **1280, 768 and 390**. Every reading 3 to 1 or more.
- On the same pages, the link's resting colour, its hover, the pill and every other focus mark read as they did before. Nothing else moves.
- Each page's DSRD 6 gate is re-read after with no new fail, and the count of pages measured is given.

**What it derives, named before it runs (Harness Rule 3).** Only the stylesheet and its version. No stored data, record text, transcript or caption is derived from it, so nothing is rebuilt. Three records carry a line about it: the Pass page record's chapter 7 (its one open fault closes), and the course page record and the school record, chapter 7, where the mend is noted beside the S530 payment tabs line.

## Done when

On the build site the guarantee link's keyboard ring reads #B8460F, 3 to 1 or more against its own band, on all 36 pages at 1280, 768 and 390, and nothing else on any page moved.

## OWED BACK

One SHIP into TO Chat naming the version bumped, the ring's colour and ratio on each of the 36 pages at the three widths (the lowest reading named), the three record lines written, the gate's result after, and any page refused with its reason.

*No em or en dashes in this file; checked before writing.*
