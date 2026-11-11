**WAITS ON (Chat, Session 464, 11 November 2026):** Kain's yes to the one page check sheet; DSRD 7 now settles four of its section 4 voids (line height, text on dark, focus mark, card edge).

# REPORT: The One Page Check Sheet, and Every Void in It (S476)

**Needs from Chat, in one sentence:** on Kain's yes to this check sheet, correct the stale sentences in section 3 whose figure a later ruling of his already settles, and read section 4's proposed new rules before Code writes any of them home.

**For:** Chat. **From:** Code, factory session S476, 10 November 2026. **Ordered by:** Kain, in the course page sitting (S472): "devote one brand new session to defining all of the site-wide standards and the checks that must be in place in order for every single page to be approved", and, asked whether to send it to Chat: "No, Claude, I would like you to do this yourself. I would like you to identify every single void in this check sheet. And propose how to fill it."

**State:** proposed, not built. No gate, hook, standard or page was changed. Nothing was deployed. Kain has been shown the sheet as one page and asked one yes or no.

**How it was made.** Read this session: DSRD 7 whole (407 checkable rules found), DSRD 3 and DSRD 10 whole, DSRD 6 whole with its record template, the every-page rules of DSRD 9 (some page sections searched, not read in full), and the code of page_gate.py, css_gate.py, image_gate.py, media_gate.py, component_gate.py, search_gate.py, publish_gate.py, deploy.py, health_check.py, the harness hooks and the check tools in tools. Six helper readers on a cheaper model made the inventories; Code judged them and re-read the passages this report quotes (DSRD 7 section 3.3, DSRD 6 chapters 7, 9 and 10, the page gate's list of checks). The six inventories, with section and line numbers for every row, are in the side session notes folder of the course page group, named INVENTORY_ and then DSRD7, DSRD3_DSRD10, DSRD6, DSRD9, CHECKS_page_gate_css_gate and CHECKS_other_gates_and_hooks. No gate was run and the build site was not touched.

## 1. The count

The sheet has 98 checks. **28 are checked today** by a machine that can fail the page or by a named person. **36 are partly checked**: in the stylesheet but not on the built page, at one width of three, by hand only, or with a hole. **21 are written in a standard and checked by nothing.** **13 have no written rule at all.**

So a page can pass every check that exists and still break a written standard, which is exactly what happened on the course page.

## 2. The check sheet

One row per check. "Who" is who should check it. "Today" is what exists now.

### Type and Headings

| What is checked | The rule and its figure | Where the rule lives | Who | State | Today |
|---|---|---|---|---|---|
| Only our two typefaces appear: Como for headings, Mulish for everything read. | Como and Mulish, plus Caveat only where registered | DSRD 7 section 3 | Machine | **Written, not checked** | Nothing reads the typeface the browser actually used. |
| Every text size is one of the nine agreed sizes. | 12, 14, 16, 18, 21, 24, 28, 33, 42 | DSRD 7 section 3.0 | Machine | **Partly checked** | css_gate check E reads the stylesheets only. Nothing reads the built page, inline styles or the previews folder. |
| Every piece of text uses one registered style whole: its size, weight and line spacing together. | The Como and Mulish style tables | DSRD 7 sections 3.1 and 3.2; DSRD 6 chapter 10 | Machine | **Written, not checked** | DSRD 6 chapter 10 says the machine lists every value the page uses. That listing was never built. |
| One page title, in the page title style. | One h1, Como 33, weight 700, line spacing 1.2 | DSRD 7 section 3.1 | Machine | **Partly checked** | page_gate h1: size and weight, at computer width only. Not the typeface, the line spacing or the phone size, and the phone figure is written two ways. |
| Every block heading is in the block heading style. | Como 24, weight 600, line spacing 1.25 | DSRD 7 sections 3.1 and 3.3 | Machine | **Written, not checked** | No check. DSRD 9 still says 22 in three places. |
| Every block heading has one supporting line under it. | One line per block heading, named carve-outs only | DSRD 7 section 3.3 rule 1 | Machine | **Partly checked** | page_gate block-heading sees a line only when it is a plain paragraph directly after the heading. Any other markup is never found and never fails. |
| The supporting line is the right length and case. | 12 to 25 words, one or two sentences, sentence case | DSRD 7 section 3.3 rules 2, 3 and 5 | Machine | **Checked** | page_gate block-heading. Kain's own recorded wordings are named exceptions. |
| The supporting line is in the supporting line style. | Mulish 18, weight 500, line spacing 1.55, brand dark #354149 | DSRD 7 section 3.3, Lead with Bar | Machine | **Written, not checked** | THE PROVEN VOID. Nothing checks it. |
| The supporting line carries its orange bar. | 2px orange edge on the left, 16 between the edge and the words | DSRD 7 section 3.3, Lead with Bar | Machine | **Written, not checked** | THE PROVEN VOID. Nothing checks it. |
| Heading levels run in order, with none skipped. | No written rule. Proposed: h1, then h2, then h3, never a jump | Nowhere yet | Machine | **No rule yet** | tools/heading_levels.py exists and is run only by hand. |
| Every heading is in title case. | Kain's ruling of 3 November 2026, held only in Code's memory | Not in DSRD 7 | Machine and person | **No rule yet** | The ruling never reached the standard. A machine can flag likely misses; a person settles them. |
| The word Achology is orange in every heading, white on a dark band. | Action orange in headings; white on dark | DSRD 7 section 1 | Machine | **Written, not checked** | No check. |
| Only the four agreed weights are used. | 400, 500, 600, 700 | DSRD 7 section 3 | Machine | **Partly checked** | css_gate check I, stylesheets only, seven named exceptions. |
| No long dashes anywhere a visitor reads. | None | The Shared Rules section 1 | Machine | **Checked** | page_gate dashes, and hook H4 on every edit. |

### Body Copy

| What is checked | The rule and its figure | Where the rule lives | Who | State | Today |
|---|---|---|---|---|---|
| Reading text is the body style. | Mulish 18, weight 400, line spacing 1.75 | DSRD 7 section 3.2 | Machine | **Written, not checked** | tools/reading_text_sweep.py by hand only. DSRD 9 still says 17 in two places. |
| The reading column is the one agreed width. | 800 | DSRD 7 section 4.1 | Machine | **Partly checked** | page_gate content-width passes 800 and the retired 880 alike, at computer width only. 880 is still written in DSRD 7 and in ten places in DSRD 9. |
| Each kind of text is in its own colour. | Read text #354149; scanned text #5E6B75; mid grey #8A9199 never for anything read; small orange text #B8460F | DSRD 7 section 1.1 | Machine | **Written, not checked** | css_gate check B only confirms a colour is a named one, never that it is the right one for the job. |
| Every block's words begin on the one text line down the page. | One vertical line per page; only panels use the container edge | DSRD 7 section 4.4a | Machine | **Written, not checked** | No check. |
| Links inside writing look like links. | Words #B8460F, 1px underline at 25 per cent, solid on hover in 0.2 seconds | DSRD 7 section 5.1, pick 12 | Machine | **Written, not checked** | No check on the built page. |
| A link that leaves the site opens a new tab and says so. | New tab, the outbound arrow, hidden words for screen readers | DSRD 7 section 1.0 | Machine | **Written, not checked** | No check. |
| The words pass the writing standard. | The Achology Content Standard check sheet | DSRD 6 chapter 1 | Person (Chat) | **Checked** | Chat reads; the machine checks acronyms and dashes. |
| Text never gets cut off or overlaps when a visitor enlarges it. | No written rule. Proposed: nothing clipped at wider letter, word and line spacing (WCAG 1.4.12) | Nowhere yet | Machine | **No rule yet** | No check. |

### Spacing

| What is checked | The rule and its figure | Where the rule lives | Who | State | Today |
|---|---|---|---|---|---|
| Every space is a step on the spacing scale. | 0, 4, 8, 16, 24, 32, 48, 64 | DSRD 7 section 4 | Machine | **Partly checked** | page_gate spacing-scale and css_gate check G. A declaration that mixes a token with a typed number passes whole, and DSRD 9 still writes off-scale gaps of 6, 10, 12, 18 and 20. |
| The space under a block heading is 16. | 16 | DSRD 7 section 3.3 | Machine | **Written, not checked** | THE PROVEN VOID. tools/course_page_check.py prints the figure for course pages and cannot fail. |
| The space under a supporting line is 24. | 24 | DSRD 7 section 3.3 | Machine | **Written, not checked** | THE PROVEN VOID. DSRD 9 gives 16, 20 and 32 for the same space on different pages. |
| The space between the header and the first content is right. | 48, and 32 on a phone | DSRD 7 section 4.3 | Machine | **Checked** | page_gate header-to-content, all three widths. |
| The space between blocks is right. | A hairline with 48 above and 48 below; 32 and 32 on a phone | DSRD 7 section 4.3 | Machine | **Checked** | page_gate hairline-spacing, all three widths, with named exceptions. |
| The space between the last block and the footer is right. | Written two ways: 48, and 64 | DSRD 7 sections 4.3 and 17.1; DSRD 9 | Machine | **Written, not checked** | Two figures, no check. |
| The page's side margins are right. | 20 on a phone, 32 on a tablet, 48 on a computer | DSRD 7 section 4.1 | Machine | **Checked** | page_gate gutters, all three widths. |
| The page's outer width is right. | 1200 | DSRD 7 section 4.1 | Machine | **Partly checked** | page_gate content-width, computer width only. |
| The breadcrumb sits in the right place. | Its gap above, 48 below, on the text line | DSRD 7 section 4.3 | Machine | **Partly checked** | page_gate breadcrumb rows check it. DSRD 9 gives five different figures for the gap below. |
| Each space between two blocks belongs to one owner, never two adding up. | One owner per boundary | DSRD 7 section 4.3 | Machine | **Partly checked** | page_gate boundary-owner, computer width only. |
| The spaces inside a block are the agreed ones. | No written rule for which step goes where: paragraph to paragraph, card padding, grid gaps, picture to caption | Nowhere yet | Machine | **No rule yet** | Only the scale is checked, never the right step in the right place. This is the general form of the fault Kain saw. |
| The page never scrolls sideways at any width. | No sideways scroll from 320 wide upwards | DSRD 6 chapter 7 (by hand) | Machine | **Partly checked** | A person checks at 400 per cent zoom. Only the course page tool measures it. |

### Hairlines and Colours

| What is checked | The rule and its figure | Where the rule lives | Who | State | Today |
|---|---|---|---|---|---|
| A hairline sits where blocks meet, and never at the very top or bottom. | One hairline per boundary | DSRD 7 section 4.3 | Machine | **Checked** | page_gate hairline-present and hairline-edges. |
| Every hairline is the hairline: 1px, in the hairline colour. | 1px, #EEEDED | DSRD 7 section 4.3 | Machine | **Partly checked** | The gate accepts any line up to 2px in any colour. The colour is named in the code and never used. |
| Only the brand's named colours are used. | The palette tokens | DSRD 7 sections 1 and 2 | Machine | **Partly checked** | css_gate check B catches typed hex codes in stylesheets only; colours written other ways slip through. |
| All text is readable against its background. | 4.5 to 1 for text, 3 to 1 for large text | DSRD 6 chapter 7 (WCAG 2.2 AA) | Machine and person | **Partly checked** | The scan runs at phone width only and only on the page at rest. |
| Text is still readable when hovered, focused or pressed. | The same ratios in every state | DSRD 6 chapter 7 | Person (Chat) | **Partly checked** | By hand only. Three unreadable hovers were found this way after clean scans. |
| Field edges, icons and focus rings stand out from their background. | No written figure. Proposed: 3 to 1 (WCAG 1.4.11) | Nowhere yet | Machine | **No rule yet** | No check. |
| Section backgrounds follow the Light Sand system. | The Light Sand rules | DSRD 7 section 3.3a | Machine | **Written, not checked** | No check. |
| Corners are one of the four agreed roundings. | 12, 999, 999, 16 | DSRD 7 section 5.3 | Machine | **Partly checked** | css_gate check D, stylesheets only; it wrongly passes 120 and 160. DSRD 7 itself uses 10 in three places. |
| Shadows are the named shadows. | The shadow tokens | DSRD 7 section 5.4 | Machine | **Checked** | css_gate check C. |
| A school's colour appears only where it belongs and stays readable. | The school colour reach and its contrast clause | DSRD 7 sections 2.1 and 2.2 | Machine | **Partly checked** | tools/school_colour_contrast.py, by hand only. |

### Buttons and Links

| What is checked | The rule and its figure | Where the rule lives | Who | State | Today |
|---|---|---|---|---|---|
| Every button is one of the registered buttons. | A pill, 46 tall, Como 14 weight 600, 24 side padding | DSRD 7 section 5.1 | Machine | **Written, not checked** | No check on the built page. Section 5.1 still describes the retired gradient button beside the Clean one. |
| A button changes clearly when hovered, focused and pressed. | The registered states | DSRD 7 section 5.1 | Person (Chat) | **Partly checked** | By hand only. |
| Two buttons side by side are a main one and a quiet one, never two the same. | The pairing rule | DSRD 7 section 5.1 | Person | **Written, not checked** | Nobody is named to check it. |
| Everything a finger presses is big enough. | At least 24 by 24; proposed 44 for main buttons and menus on a phone | DSRD 6 chapter 7.1 (WCAG 2.5.8) | Machine | **Partly checked** | By hand, once, before launch, on one page of each type. |
| Every link goes somewhere real. | Every internal link answers | DSRD 6 chapter 11 | Machine | **Checked** | page_gate links-resolve. A link to a page not yet built is recorded, not failed. |
| Every link says in its words where it goes. | The link label standard | DSRD 1 section 6.4 | Person (Chat) | **Checked** | Chat reads. |
| Tabs, pills and menus are the registered ones. | The registered family | DSRD 7 section 5.1 | Machine | **Written, not checked** | No check. |
| Icons come from the icon list, at their agreed sizes. | The icon registry and its sizes | DSRD 7 section 5.2 | Machine | **Partly checked** | image_gate checks the icon is on the list, never its size. |

### Images

| What is checked | The rule and its figure | Where the rule lives | Who | State | Today |
|---|---|---|---|---|---|
| Every picture is in the right file type. | WebP for pictures, SVG for line art | DSRD 7 section 12.3 | Machine | **Checked** | image_gate. |
| No picture is heavier than its allowance. | Hero 200KB, card 80, book cover 60, portrait 60, share image 120, icon square 20, background 40 | DSRD 7 section 12.3 | Machine | **Checked** | image_gate. |
| Every picture is sharp on a sharp screen. | A normal and a double size of the space it fills | DSRD 7 section 12.3 | Machine | **Partly checked** | image_gate checks the two sizes are offered. Nothing compares the picture's real size with the size it is drawn at, so a soft picture passes. |
| No picture is far bigger than it needs to be. | No written figure. Proposed: never more than two and a half times the size it is drawn at | DSRD 6 chapter 9 says only 'right dimensions' | Machine | **No rule yet** | No check. |
| Pictures hold their place while loading, so nothing jumps. | Width and height set on every picture | DSRD 7 section 12.3 | Machine | **Checked** | image_gate. |
| Every picture has its description. | Every picture described; decoration left empty | DSRD 7 section 12.3 | Machine | **Checked** | image_gate. |
| Each description says what the picture shows. | Never 'image of', never a file name | DSRD 7 section 12.3 | Person (Chat) | **Checked** | Chat reads. |
| The main picture loads first and the rest wait their turn. | Lead picture first; pictures further down load as they near | DSRD 7 section 12.3 | Machine | **Checked** | image_gate, with one named exception. |
| Every picture on the page really loads. | No broken picture | DSRD 6 chapter 11 | Machine | **Partly checked** | The gate never scrolls the page, so pictures further down are never asked for and never checked. |
| No picture breaks out of its box. | Inside its band and padding | DSRD 7 section 14.0 rule 1 | Machine | **Written, not checked** | No check. |
| Picture file names are tidy. | Lower case, hyphens, descriptive | DSRD 7 section 12.3 | Machine | **Checked** | image_gate. |

### Forms

| What is checked | The rule and its figure | Where the rule lives | Who | State | Today |
|---|---|---|---|---|---|
| Every field is the registered field. | 46 tall, 20 side padding, the registered edge | DSRD 7 section 5.5 | Machine | **Written, not checked** | No check. |
| Every field says what it is for. | A label on every field | DSRD 6 chapter 7 | Machine | **Checked** | The accessibility scan. |
| Whatever has the keyboard's attention shows a clear ring. | The fire frame on fields; no written figure for links and buttons | DSRD 7 section 5.5 | Machine and person | **Partly checked** | By hand only, and half the rule is unwritten. |
| A mistake is explained in words, beside the field. | Errors in words | DSRD 6 chapter 7 | Person (Chat) | **Checked** | Chat checks. |
| The form really sends, and the visitor is told so. | Proved on the built page | DSRD 6 chapter 11 | Person (Code) | **Partly checked** | Checked when remembered; the course page sign-up says thanks and sends nothing today. |

### Movement

| What is checked | The rule and its figure | Where the rule lives | Who | State | Today |
|---|---|---|---|---|---|
| Anything that moves does so at an agreed speed. | No written rule. Proposed: three named speeds and one easing, taken from the signed pages | Nowhere: DSRD 7 has no movement section | Machine | **No rule yet** | No rule and no check. |
| With a visitor's reduce movement setting on, everything is still. | All movement respects the setting | DSRD 7 section 5.1; DSRD 6 chapter 7.1 | Machine | **Partly checked** | The gate switches the setting on to steady its measuring and never tests it. |
| Anything that moves by itself for more than five seconds can be paused. | Five seconds (WCAG 2.2.2) | DSRD 6 chapter 7.1 | Person | **Partly checked** | Once, before launch, by hand. |
| Nothing shifts about while the page loads. | Layout shift 0.05 or less | DSRD 3 section 4.3 | Machine | **Partly checked** | A person watches one load. No machine reading in the gate. |

### Accessibility

| What is checked | The rule and its figure | Where the rule lives | Who | State | Today |
|---|---|---|---|---|---|
| The automatic accessibility scan finds nothing. | No failures against WCAG 2.2 AA | DSRD 6 chapters 7 and 7.1 | Machine | **Partly checked** | The gate scans at phone width only; the standard says computer and phone. |
| The whole page works by keyboard alone, in a sensible order. | Everything reachable and usable; the focused item never hidden | DSRD 6 chapter 7 | Person (Chat) | **Partly checked** | By hand. A machine can walk the tab order and catch a hidden or ringless stop. |
| The page holds together when enlarged. | 200 per cent, and 400 per cent into one column | DSRD 6 chapter 7 | Person (Chat) | **Partly checked** | By hand. The 400 per cent case is the same as a 320 wide screen, which a machine can measure. |
| The page tells a screen reader what it is. | No written rule for page language, skip link or landmarks | Nowhere in DSRD 3 | Machine | **No rule yet** | The scan catches some of it by accident. |
| A screen reader can follow the page from top to bottom. | Read aloud on a Mac and an iPhone | DSRD 6 chapter 7.1 | Person | **Partly checked** | Once, before launch. |

### Speed

| What is checked | The rule and its figure | Where the rule lives | Who | State | Today |
|---|---|---|---|---|---|
| The page is fast on a phone. | Server answer 0.8s, first paint 1.5s, main content 2.0s, response 150ms, shift 0.05 | DSRD 3 section 4.3 | Machine | **Partly checked** | Run by hand on one page of each type. Every page carries the same recorded miss, waiting on one site-wide fix. |
| The page is not heavy. | No written figure for total weight, number of files, or the size of styles and scripts | Nowhere in DSRD 3 | Machine | **No rule yet** | No rule and no check. |
| Fonts load without a flash or a jump. | Half written: Como only. Nothing for Mulish, preloading or how many files | DSRD 3 section 13 | Machine | **No rule yet** | No check. |
| The page carries no styles or scripts it does not use. | No written rule | Nowhere yet | Machine | **No rule yet** | Dead code is found by hand, page by page. |
| Nothing the page asks for fails to arrive. | No failed file | DSRD 6 chapter 11 | Machine | **Checked** | page_gate assets-load. |
| The page throws no errors in the browser. | No written rule. Proposed: none | Nowhere yet | Machine | **No rule yet** | No check. |

### Search and Data

| What is checked | The rule and its figure | Where the rule lives | Who | State | Today |
|---|---|---|---|---|---|
| The search title and description are present and the right length. | Written two ways: 60 and 155 at most, and 70 to 165 | DSRD 6 chapter 3 | Machine | **Partly checked** | page_gate uses 60 and 155; health_check uses 70 to 165. |
| The page names its one true address. | A canonical address, and the right one | DSRD 6 chapter 5 | Machine | **Partly checked** | The gate checks that one exists, never that it is correct. |
| The address, indexing, breadcrumb trail, old address and inbound links are right. | Exact, against DSRD 1 | DSRD 6 chapter 5 | Machine | **Checked** | search_gate, five rows. |
| The Rank Math score meets its bar. | 81 to 90 by page type | DSRD 6 chapter 5 | Machine | **Checked** | search_gate, from Code's own score table. |
| The key phrase is used the right amount. | 1.0 to 1.5 per cent | DSRD 6 chapter 5 | Machine | **Checked** | search_gate. |
| The page is in the sitemap. | Listed | DSRD 6 chapter 5 | Machine | **Checked** | page_gate sitemap. |
| The page's hidden data for search engines is the right kind and valid. | Written two ways: the tables in DSRD 3 and DSRD 10 disagree for eight page types | DSRD 3 section 5.3; DSRD 10 section 9 | Machine | **Written, not checked** | DSRD 6 chapter 4 has no machine check at all. |
| AI assistants can read and quote the page. | The five checks | DSRD 6 chapter 6 | Person (Chat) | **Checked** | Chat reads. |
| Nothing on the page loads insecurely. | None | DSRD 6 chapter 11 | Machine | **Checked** | page_gate mixed-content. |

### The Page Frame

| What is checked | The rule and its figure | Where the rule lives | Who | State | Today |
|---|---|---|---|---|---|
| The page carries the right blocks in the right order. | The page's signed design and its layout spec | DSRD 6 chapter 2; DSRD 9 | Person (Chat) | **Checked** | Chat reads. tools/course_page_compare.py can prove a built page equal to its signed design, for the course page only, by hand. |
| Shared parts are the registered component, never a look-alike. | The Component Registry | The Harness Rule 11 | Machine | **Partly checked** | component_gate measures one specimen page per component and no other page; nine components have nothing to measure against. |
| The page looks right in Safari, where Kain judges it. | Safari, Chrome and Firefox at computer, tablet and phone widths | DSRD 6 chapter 11 | Machine and person | **Partly checked** | Every machine measurement is taken in Chrome's engine. Safari is checked by eye. |
| The page is easy to use. | The thirty second checks and the full walk | DSRD 6 chapter 8 | Person (Chat, then Kain) | **Checked** | Chat walks; Kain's look is the second pair of eyes. |
| The page has its written record, with nothing failing and nothing skipped. | A DSRD 6 record with no fail and no not run | DSRD 6 section 0; The Harness Rule 6 | Machine | **Partly checked** | Enforced for two kinds of template file only. Course, Certification and Accreditation pages, and every draft, arm nothing. |
| The check can read the page at all. | Every page, published or draft | Nowhere yet | Machine | **No rule yet** | The gate cannot sign in. Pointed at a draft it grades the 'not found' page instead and prints a mixed result. |

## 3. Voids of the first kind: one thing, two figures

A check cannot be built against a rule that is written two ways. These are the places found. "Settled by" names the later ruling where there is one; "Not settled" goes to Kain on a rendered page, one at a time.

| The thing | One place says | Another says | Settled by |
|---|---|---|---|
| Space under a block heading and under its supporting line | DSRD 7 section 3.3: 16 and 24 | DSRD 9: 2 or 8 under the heading; 16, 20 or 32 under the line (sections 20.2, 20.7, 22.16a, 37.7) | DSRD 7 section 3.3, Kain, 8 November 2026 |
| Reading column width | DSRD 7 section 4.1: 800 | 880 still in DSRD 7 sections 3.2, 4.4 and the measure rule, and in ten sections of DSRD 9; page_gate accepts both | 800 (Kain, S111, S357) |
| The inset panel | DSRD 7 section 4.4: 944, built as 880 plus 32 each side | On an 800 column the same sum gives 864 | Not settled: Kain's eye |
| Body text size | DSRD 7 section 3.2: 18 | DSRD 9 sections 22.6 and 32.4: 17 | 18 (Kain: fixed, S147) |
| Text size on a phone | DSRD 7 section 3.0: every size steps down one below 768 | DSRD 7 section 4.1: the scale is fixed and only the page title changes; the title's own step is written as below 639 and below 768 | Not settled |
| Page title size by width | DSRD 9 section 34.13: 33 at every width | DSRD 9 sections 20.14 and 21.9: 28 on a tablet, 26 on a phone; section 22.15: 28 on a phone | Not settled |
| Block heading size | DSRD 7: Como 24 | DSRD 9 sections 20.7, 22.8, 22.10: Como 22 (not one of the nine sizes) | 24 |
| Supporting line colour | DSRD 7 section 3.3: brand dark #354149 | DSRD 9: mid grey #8A9199 in three sections, soft grey #5E6B75 in three others | #354149 (8 November 2026) |
| Last block to footer | DSRD 7 section 4.3 and DSRD 9 section 42: 48 | DSRD 7 section 17.1 and DSRD 9 sections 20.2, 21.9, 38.5: 64 | Not settled |
| Breadcrumb to title | DSRD 9 sections 26, 20.0f, 34.13: 48 | 12, 20, 72 and 80 elsewhere in DSRD 9 | Not settled |
| Spacing tokens on a phone | DSRD 7 section 4: the two largest steps shrink below 768 | DSRD 7 section 4.3: the 48 step never shrinks | Section 4.3 (later) |
| Hairline spacing 'nothing else, at any width' | DSRD 7 section 4.3: 48 and 48 | Its own exceptions 20, 22 and 23 give other figures, and one removes the hairlines | The rule, with the exceptions named as exceptions |
| Rounded corners | DSRD 7 section 5.3: four tiers, 12, 999, 999, 16, 'and nothing else' | 10 used in sections 5.2.4 and 5.5; 14 on the testimonials lightbox | Not settled: name 10 or collapse it |
| Button sizes | DSRD 7 section 5.1 calls 46, 40 and 36 superseded | The same section then uses them for the family and for fields | The family (2 November 2026) |
| The main button | Pick 17, Clean: flat | The gradient, rim and glow still described beside it | Clean |
| Hover and ink colours | DSRD 7 section 1: hover #D85A1B, light orange #F5A05C, two text colours only | Section 5.1: ember hovers, light orange #FFC08F, a third ink #2D3940 | Section 5.1 (later) |
| Menu link line | Pick 13: 1px | Pick 19: 1.5px; section 14.0 rule 4 says list links change by colour only | Not settled |
| Pagination | DSRD 7 section 17.1: a 40 by 40 pill with a 10 rounding | The same section: a 36 tall round pill | Not settled |
| Search title and description length | page_gate: at most 60 and 155 | health_check: 70 to 165 | Not settled |
| Hidden data per page type | DSRD 3 section 5.3 | DSRD 10 section 9 differs for eight page types; the two also disagree on who emits it | DSRD 10 (DSRD 3 defers to it) |
| Heading case | Kain, 3 November 2026: every heading in title case | Not written in DSRD 7 at all | Write it home |

DSRD 9 is the main source: many of its page sections were written before the site-wide rulings and still carry their own figures. The fill is not to edit every page section; it is one sentence at the head of DSRD 9 saying that DSRD 7 governs every site-wide quantity and a page section may differ only by a named exception, and then the stale figures are removed as each page is next touched.

## 4. Voids of the second kind: no rule at all

Things a professional build is held to that our standards do not state. Each is proposed in our own terms and tokens; no outside code is proposed. None is written home without Kain's yes, and each new figure that changes how a page looks is shown to him rendered first. The outside figures are from Code's own knowledge of the published standards, not fetched this session; each is re-read at its source before its rule is written home.

| The thing | What the outside standard says | Our proposed rule | Where it would be written |
|---|---|---|---|
| Contrast in every state | WCAG 2.2, 1.4.3 and 1.4.11 | Text 4.5 to 1; large text (24px, or 18.66px bold) 3 to 1; field edges, icons and focus rings 3 to 1 against what they sit on; the same in hover, focus and pressed states. | DSRD 7 section 1.1 as a rule, beside its measured pairs |
| Focus ring on everything | WCAG 2.2, 2.4.7 and 2.4.11; 2.4.13 as our own bar | Every interactive part shows a ring at least 2px thick with 3 to 1 contrast, never hidden under the header. Links and buttons take the fire frame the fields already have. | DSRD 7 section 5.5, widened from fields to all parts |
| Target size | WCAG 2.2, 2.5.8; Apple and Google platform guidance of 44 and 48 | Nothing pressed is under 24 by 24. Main buttons and menu items on a phone are at least 44 tall. Our 46 buttons already meet it; the small icon links are the risk. | DSRD 7 section 5.1 |
| Heading order and page landmarks | WCAG 2.2, 1.3.1, 2.4.1, 3.1.1 | One h1; levels never skipped; the page states its language; a skip link is the first stop; header, main and footer are marked as such. | DSRD 3, a new every-page markup section |
| Text spacing and reflow | WCAG 2.2, 1.4.10 and 1.4.12 | No sideways scroll at 320 wide; nothing clipped when line spacing is 1.5, paragraph spacing 2 times, letter spacing 0.12 and word spacing 0.16 of the text size. | DSRD 6 chapter 7, as machine rows |
| Picture sharpness | Common practice for sharp screens: a double-size file, no benefit beyond it | The file a sharp screen receives is at least 2 times the drawn width and no more than 2.5 times. DSRD 7 section 12.3 already asks for the two sizes; this adds the measured proof. | DSRD 7 section 12.3 |
| Speed on real pages | Google's Core Web Vitals: main content 2.5s, response 200ms, shift 0.1, at three visits in four | Keep DSRD 3's tighter targets. Add how they are read: phone profile, three runs, the middle kept; and the real-visitor reading after launch as already written. | DSRD 3 section 4.4 |
| Page weight | Performance budgets, as used by public design systems and Lighthouse | Written limits for total weight, styles, scripts, font files and requests per kind of page, set from our own lightest signed pages. | DSRD 3 section 4, a new allowance table |
| Fonts | Common practice: modern file type, text shown at once, only the first fonts preloaded | Every font is WOFF2 and shows text immediately; at most two files are preloaded; a stated limit on files per page; the stand-in font sized so the swap does not shift the page. | DSRD 3 section 13 |
| Movement | Public design systems (Material, Carbon) keep interface movement between about 100 and 500 thousandths of a second with named easings; WCAG 2.2.2 and 2.3.3 | Three named speeds and one easing, taken from our signed pages; all of it still under the reduce movement setting. | DSRD 7, a new movement section |
| Which space goes where | Spacing practice in public design systems: the scale, plus a short table of where each step is used | A short table in our own steps: heading to supporting line 16, line to content 24 (both already ruled), then paragraph to paragraph, card padding, grid gaps and picture to caption, each read from the signed pages and put to Kain where the pages disagree. | DSRD 7 section 4 |
| No errors in the browser | Common release practice | A page throws no script errors and asks for nothing from a site that is not on our list. | DSRD 3 |

## 5. Voids of the third kind: a check that cannot bite

1. The page gate cannot read a draft. Pointed at one, it grades the 'not found' page and prints a result that mixes two pages.
2. The page gate runs only when a person types it, or at publishing. No hook runs it after a page is built or changed.
3. The completion hook (H5) knows a page was worked on only from two kinds of file name. Course, Certification and Accreditation pages, data-file pages and drafts arm nothing.
4. H5 blocks only when a closing sentence uses a completion word and names the page. Without that sentence a missing record is a notice. A second stop passes every block.
5. The edit hook (H4) forgets a failing gate as soon as a later edit passes, and counts a gate it could not run as a pass. It never runs the page gate, though its own notes say it does.
6. Forty-one of the page gate's fifty-six exception entries waive every failure of that check for a whole family of pages, not the one line that was granted.
7. The stylesheet gate's waiver is any comment near the line that contains the word Kain, DSRD, one-off or deliberate. A typed number beside a token passes. Roundings of 120 and 160 pass. The previews folder is not read.
8. The gate never scrolls, so pictures lower on a page are never requested and never checked.
9. The accessibility scan runs at phone width only, at rest only, with reduce movement forced on.
10. Every measurement is taken in Chrome's engine. Kain judges in Safari.
11. Deploying runs no page check, and nothing rechecks other pages after a shared stylesheet changes.
12. The component gate measures one specimen page per component, measures the previous deploy, and skips nine components that have no specimen.
13. A write made through the shell fires none of the file hooks.
14. DSRD 6 chapter 10 says the machine lists every value a page uses. It was never built, so the chapter is filled in by hand or not at all.
15. The record template has no line for the five stages (section 0.1), the pre-launch accessibility run (7.1) or the page type table (12).
16. Thirty-six places where a check's notes claim more than its code does (seventeen in page_gate and css_gate, nineteen in the others).

## 6. The fills, in the order Code recommends

The first is the proven one. The second and fourth make every later check worth having, because a check that cannot read the page or can be skipped protects nothing.

**1. The line under each block heading.** Its style, its orange bar and its two spaces (16 above it, 24 below it), measured on the built page, on every kind of page. This is the one you caught.

How: Build one rendered-page check, `supporting-line`, into page_gate.py. For every block heading it finds the line that follows by position on the page (not by markup, so a line that is not a plain paragraph is still found), then reads the computed style and the boxes: typeface Mulish, size 18, weight 500, line spacing 1.55 (27.9px), colour #354149 or the band's light colour on a dark band; a left edge 2px wide in the orange token with 16 of padding; the gap from the heading's bottom edge to the line's top edge 16; the gap from the line's bottom edge to the next visible box 24. Tolerance 1px. At 1440, 900 and 390. The heading itself is read for Como 24, weight 600. The policy pages' carve-out and Kain's recorded wordings stay named exceptions. Start from tools/course_page_check.py --gaps, which already measures these three gaps and only lacks expected values and a way to fail. Acceptance file first, red before the fix: one fixture page with a correct block and one with each fault.

**2. Let the check sign in.** So a draft is checked exactly like a published page. Today the 28 course pages cannot be checked at all.

How: Give page_gate.py a `--signed-in` switch that borrows the short-lived session tools/score_run.py already mints (the route tools/course_page_compare.py proves works: cookies added, every write blocked, the admin bar stripped). The gate must read the page's status first and refuse to grade a 'not found' page: a check that reads nothing must fail. Never call the revoke step while Kain is working, because it signs him out too.

**3. Every piece of text against the registered styles.** Typeface, size, weight and line spacing together, for every heading and every paragraph, on the built page.

How: Build the listing DSRD 6 chapter 10 already promises: walk every visible text node in the page, collect each distinct set of typeface, size, weight, line spacing and colour with a count and one example, and match each set to a row of DSRD 7 sections 3.1 and 3.2 read from the document itself (tools/dsrd_line_index.py), never from a copy in the code. A set that matches no row fails with its example text. Role checks on top: h1 is the page title row, a block heading is H2 Section, reading text is the body row. Registered components declare their own sets through their build sheets.

**4. Make the check impossible to skip.** No page reaches you without its record, drafts included, and a failing check cannot be cleared by a later edit.

How: Four changes in the harness. H5 arms on any work that changes what a page shows (a template, a data file, a part, a stylesheet a page loads), not only on two kinds of file name, and finds the page from the declaration's SCOPE line. H5 blocks on a missing or open record whenever the page is put to Kain, not only when the word 'done' appears, and a second stop no longer passes. H4 keeps a failing gate on its ledger until that same gate passes, and an unrunnable gate counts as a fail. The 41 exception entries that waive a whole check for a whole page family are each cut down to the named lines they were granted for, or removed.

**5. One figure for each thing the standards state two ways.** About twenty places where two documents, or two parts of one, give different numbers for the same thing.

How: Section 3 of this report lists them. Where a later ruling of Kain's already settles the figure, the stale sentence is simply corrected in its home (Chat's job, no question for Kain). Where no ruling settles it, the figure goes to Kain on a rendered page, one at a time. The gate then reads each figure from the one home.

**6. Buttons, links, fields, corners and hairlines on the built page.** Each one measured against its registered look, not only read in the stylesheet.

How: One rendered-page check, `registered-parts`: every button, text link, tab, pill, icon button and field on the page is matched by its computed height, padding, rounding, typeface and colours to a row of DSRD 7 sections 5.1, 5.3 and 5.5; every hairline is 1px in #EEEDED; every rounding is one of the four tiers. A part that matches no row fails with a picture of it. Also mend css_gate: read mixed declarations value by value, fix the rounding test that passes 120 and 160, and make the waiver a named line in a waivers file instead of any comment containing the word Kain.

**7. Pictures: sharp, and all of them checked.** Each picture's real size compared with the size it is drawn at; the page scrolled so every picture is loaded and checked.

How: Add two rows to image_gate.py. `image-sharp`: at each width and at a device scale of 2, the file the browser chose must be at least 2 times the drawn width (a little grace, 1.9) and no more than 2.5 times; photographs only, never SVG. `image-loaded`: the gate scrolls the page top to bottom before reading, then fails any picture whose natural width is zero. Also read what each srcset offers, not only that one exists.

**8. Accessibility: widen the machine half.** Both widths, the keyboard walk, finger-sized targets, enlarging, the reduce movement setting, and readability when hovered.

How: Run the scan at 1440 and 375 as DSRD 6 chapter 7.1 already says. Add rendered checks a machine can do without judgement: tab through the page and fail any stop with no visible ring or one hidden under the header; fail any target under 24 by 24 that is not a link inside a sentence; fail sideways scroll at 320 wide; apply the wider text spacing of WCAG 1.4.12 and fail clipped text; with reduce movement on, fail any animation still running after one second; hover and focus each interactive part and measure the contrast of its words in that state. The person's walk stays for what needs judgement.

**9. Measure in Safari's engine too.** You judge in Safari; every measurement today is taken in Chrome's engine.

How: Run the geometry rows (spaces, widths, line counts, the supporting line) a second time in WebKit through Playwright, and fail where the two engines differ by more than 1px. The local Playwright cannot start WebKit today (a version mismatch), so the first step is to mend the install.

**10. Speed: a machine reading and weight allowances.** A reading per kind of page taken by the gate, and written limits for how heavy a page may be.

How: Run Lighthouse from the gate on one page of each type, phone profile, three runs, the middle one kept, against DSRD 3 section 4.3. New rule to write: allowances for total page weight, styles, scripts, font files and the number of requests, each set from what the lightest signed pages already achieve rather than invented. Add a no-errors-in-the-browser row. The one site-wide speed fix on the theme queue comes first, or every page fails for the same known reason.

**11. A movement rule, then its check.** How fast things move and how they ease, written once; today there is nothing to check against.

How: Measure every transition and animation on the signed pages, propose three named speeds and one easing that cover them, show Kain the few that would change, and write the table into DSRD 7 as a new section on his yes. The check then reads computed transition and animation durations against the table.

**12. Search data.** The right hidden data for each kind of page, the true address, and one title length.

How: Settle the DSRD 3 and DSRD 10 tables into one. Then a machine check for DSRD 6 chapter 4: parse the page's JSON-LD, confirm the types the table names for this page type are present with their required fields. Make the canonical row compare the value with the page's own address. One pair of title and description limits in both tools.

**13. Recheck after any site-wide style change.** One page of each kind checked again whenever a shared stylesheet changes, so a fix on one page cannot quietly break another.

How: deploy.py runs page_gate on one representative page per type (the list in DSRD 6 chapter 7.1) after any deploy that touches a shared stylesheet, template part or script, and prints which rows changed against the last run.

**14. Correct the checks' own notes.** Thirty-six places where a check's notes claim more than it does.

How: Each note is corrected to say what the code does, or the code is made to do what the note says. Listed in the two check inventories.

Every fill is built the way the harness already asks: an acceptance file that fails before the change and passes after, and a check that prints what it skipped.

## 7. The two standing rules that stop the drift returning

**Rule one. No rule enters a standard without its check entering the gate in the same piece of work.** A ruling that states a figure is written home together with the gate row that measures it, or with one line saying a person checks it and who. A rule with neither is not yet a standard. Test: every row of this check sheet names a check or a person; a new ruling adds a row.

**Rule two. No page is put to Kain without its DSRD 6 record, drafts included.** The record is made by the gate reading the page as it will be seen, signed in where it is a draft, and carries no fail and no not run except a recorded exception. Test: the completion hook refuses a turn that shows Kain a page whose record is missing or open.

Both are proposed to replace, not add to, existing text (The Shared Rules, section 9, the growth governor): rule one replaces the enforcement paragraph of DSRD 7 section 3.3, which named four word checks and left the look unchecked; rule two replaces the narrower file-name test in the harness's Rule 6 enforcement.

## 8. Two open course page items, carried so they are not lost

1. **The course page's subheading spaces still break DSRD 7 section 3.3.** As relayed from the S472 sitting (not re-measured here): the space under the supporting line is 24, 24, 32, 48, 32, about 64, 48 and 32 across the eight blocks, so two of eight meet the standard. Kain has not yet answered whether to set them all to the standard. Not done here.
2. **The Reviews page and the Testimonials page** are the two pages Kain says have not been reviewed, and each needs a review of its own. Not done here.

## 9. What this report does not claim

No gate was run, so every "Today" line rests on reading the code, not on watching it fail. Some page sections of DSRD 9 were searched rather than read whole, so another conflicting figure may sit there. DSRD 8, DSRD 1, DSRD 2, DSRD 4 and DSRD 5 were not read for this job. The helper readers' line numbers were spot-checked, not all verified.

OWED BACK: Chat's read of sections 3 and 4, and the stale sentences corrected in their homes once Kain has said yes to the sheet.
