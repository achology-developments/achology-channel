**For Chat. What this needs:** read the three pages' task lists below, rule on the questions in each page's list D and on the four points in section 2, and decide which visible items go to Kain and in what order. Code, theme session S505, 12 November 2026. It answers BRIEF__Audit_Of_The_About_Testimonials_And_Reviews_Pages_Look_And_Code.

DOCUMENT TYPE: report. Not a page spec. It asks Kain nothing.

# REPORT: audit of the About, Testimonials and Reviews pages, look and code

## 1. How it was done

Three readers, one a page, each on Opus 5.5 at xhigh as the brief names, read the built page at 1440, 768 and 390 wide, its served HTML, its stylesheets and its template, against DSRD 6, 7 and 8 and the page's signed spec and record. The main session (Fable 5.2, which cannot switch its own model) checked each tidy-up against the files before shipping it, shipped only what the brief's section 5 allows, and proved each by pictures.

Every item below carries its evidence. The pictures, measurements, saved HTML and measuring scripts are in this session's working folder, one folder a page (about, testimonials, reviews) and one for the shipping proof (proof). That folder is temporary: say if any of it should be kept in the pages' design folders and Code will copy it there.

Counts: About 18 visible, 10 behind the scenes, 6 tidy-ups, 12 questions. Testimonials 15, 18, 7 and 12. Reviews 17, 11, 9 and 18.

## 2. What shipped, what waits, and four points to rule

### 2.1 Shipped (nothing a visitor can see changed)

| Page | Item in its list C | File | Version | Proof |
|---|---|---|---|---|
| Testimonials | C1 dead `tm-panel` rule out | testimonials.css | 0.708.030 | pictures match |
| Testimonials | C2 dead `about-grid` outdent out | testimonials.css | 0.708.030 | pictures match |
| Testimonials | C3 copy of the shared ruled-block rule out | testimonials.css | 0.708.030 | pictures match |
| Testimonials | C4 stale comment (the class list), in part | testimonials.css | 0.708.030 | a comment |
| Testimonials | C5 fallback nothing sets out | testimonials.js | 0.708.030 | pictures match |
| Reviews | C1 selector half that matched nothing out | reviews.js | 0.708.035 | pictures match |
| Reviews | C2 stale batch size in a comment | reviews.js | 0.708.035 | a comment |
| Reviews | C3 the chart's two override rules folded in | reviews.css | 0.708.035 | pictures match |
| Reviews | C4, C5, C6, C7 (the middle one of its three), C8 stale comments | reviews.css | 0.708.035 | comments |

Theme commits 2bd90a7f and 7aa6a9aa (Testimonials) and db1a9745 (Reviews). css_gate.py passes both stylesheets; both scripts parse; deploy.py printed "CURRENT. Local, the server and the zip all agree" at 0.708.030 and at 0.708.035.

**The picture proof, and how it had to be taken.** A plain before and after pair could not match on these pages even with no change between them: the map block's markers pulse for ever (Reviews A11), and the cards' background pictures arrive at slightly different moments. So each page was photographed with motion stilled, at 1440, 768 and 390, twice in the same browser on the same build site: once with the files as they stood before the change swapped in, once with the new files, the swap counted so a picture cannot be taken for a "before" it is not. Testimonials: identical on every pixel at all three widths (1440 by 6436, 768 by 8303, 390 by 13154). Reviews: identical on every pixel at 768 and 390 (768 by 12234, 390 by 20823); at 1440 the first old-files picture differed from the new by 7,308 pixels in eight scattered spots, a second old-files picture then matched the new on every pixel, and differed from the first old-files picture in the same eight spots, so the difference was in that one capture and not in the files.

**One thing to know.** The school page session's deploy at 0.708.033 carried reviews.css and reviews.js to the build site a few minutes before this session committed them, because all sessions share one theme folder. The edits were finished and had passed css_gate.py by then, and the pictures above prove them, so nothing wrong was ever shown. It is the same fault the two-sessions brief exists to stop.

### 2.2 Waits: every template comment fix (three pages)

The harness refuses any edit to a page template unless the SPEC field names a signed spec that sits in the channel and carries its PAGE GATE line at its foot ("H2 PAGE GATE INTAKE: blocked. The SPEC field names 1 document and none of them is in the channel"). The three specs live in the pages' design folders, and the Reviews spec carries no PAGE GATE line at all. That wall was put there on purpose, so Code did not work round it. These wait on Chat's word on how a comment-only template edit is cleared:

- About C1 to C6 (page-about.php and about-setup.php: stale comments, and thirteen dead inline colours).
- Testimonials C6 and C7 (page-testimonials.php: one stale comment, one indent).
- Reviews C9 (page-reviews.php: four comments written before the page was built).

Also held back by choice: the rest of Testimonials C4 (the lightbox comment's claim about DSRD 7 section 5.3's 14px row, which should be corrected in the DSRD first, see Testimonials D7) and Reviews C7's first and third comments (left as they stand; they describe history and are not wrong enough to touch without Chat's reading).

### 2.3 Four points for Chat

1. **The template wall (2.2).** Name the route for comment-only edits to the three templates, or leave them.
2. **The version line.** The brief says change nothing in a shared file. A ship needs the version line in style.css moved, which is shared. Code moved it, twice, as every session does, and names it here.
3. **The last-line rule.** The brief asks for no last line of one, two or three words. DSRD 7 section 4.1 and no-lone-words.js forbid only the single word. All three readers measured under both readings and ask which governs (About D4, Testimonials D6, Reviews D16).
4. **The tools.** shot.py's whole-page picture repeats the top of the page once the picture passes 16,384 device pixels, so on these long pages its 768 and 390 pictures are wrong at the foot at scale 2 (scale 1 is sound). page_gate.py misreads three things on these pages (Testimonials B15, About D10). Both are factory work; say if they go on Backlog: Code.

## 3. Faults shared across the pages, to be fixed once

Each names the pages it touches. The detail and evidence sit in the page lists.

1. **The video dialog's close button is knocked into the top left corner** by the button family (buttons.js names it an icon button; buttons.css then wins). About A4, Testimonials A2. Pages: About and Testimonials, and any page drawing the shared video dialog. The fix sits in buttons.js, which loads on every page.
2. **The site header stays bright above an open dialog** (header 1000, dialogs 300). About A4, Testimonials A4. Pages: About, Testimonials, any page with the default member-story dialog.
3. **Single words alone on a last line.** Testimonials and Reviews are not switched on in no-lone-words.js at all; About is, but the script misses six of its blocks and the word after the orange Achology. About A3, Testimonials A5, Reviews A5. Pages: all three. An entry in that script acts only on the page it names.
4. **The supporting lines are not the Lead with Bar component.** About A18, Testimonials A12, Reviews A9. Pages: all three. Waits on the signed sweep brief DSRD 7 section 3.3 names; it is most of each page's gate failures.
5. **The member story posters** print older wording than the captions and the play button sits on the words; the captions are hidden on About and shown on Testimonials. About A1, Testimonials A8 and A9. Pages: About, Testimonials.
6. **The global impact block:** its markers pulse for ever with no pause (DSRD 6 section 7.1 names them), its words sit 16 inside the page's text line, and its lead is not on the shared component. Reviews A10, A11, Testimonials B18. Pages: Reviews, Testimonials.
7. **Stylesheets loaded and not used.** cards.css and people.css apply nothing on any of the three; ConvertKit's files load with no form; about.css, help.css, policies.css and components.css are 3 to 14 per cent used. About B1 and B9, Testimonials B8, Reviews B8. Pages: every page on the site (functions.php). help.css is also printed twice wherever the FAQs block is drawn (Reviews B4).
8. **The hero differs between the three.** About's lead is 21, the others 18; Testimonials serves a 409 KB PNG lazily where About and Reviews serve WebP copies eagerly. Testimonials B1, Reviews D10. Pages: all three.
9. **The Ten Ways gateway:** its flagship picture is under-resolved on sharp screens and its line lacks a hyphen in "28 course". About B6 and D3, Testimonials B18, Reviews B8. Pages: all three, and every page that draws the gateway.
10. **Nothing steps down on a phone.** DSRD 7's S189 phone rule steps text one size below 768; the H1 stays 33 on all three. Testimonials D8, Reviews D8. Pages: all three. A question, not yet a fault.
11. **Links in body text** are drawn in the action orange where DSRD 7 section 5.5 says the AA orange. Reviews A16 and D17. Pages: every page with a link in body text.
12. **The share picture's description** is one word ("About", "testimonials"). About B10, Testimonials B17. Pages: About, Testimonials. A Rank Math field; the words are Chat's.
13. **The records are behind the pages.** Each DSRD6_RECORD.md carries fails that no longer reproduce and lines not run; the Reviews spec and several DSRD rows describe an earlier page. About D1, Testimonials B15 and B16, Reviews B10, D11 and D12. Pages: all three. A fresh gate run that purges the cache is owed on each before any record line is written; the readers ran the gate without a purge, so their runs are not for the record.
14. **The cookie banner** holds the keyboard on a first visit and covers controls. Testimonials A15, Reviews A17. Pages: every page (Complianz).

## 4. The three pages

In each page's lists, "shipped" and "waits" are settled by section 2 above: only the rows in table 2.1 shipped; every other item waits.

---

## About page audit: https://achologytest.com/about/

Read only. Nothing in the theme or the project was changed. Measured on 11 November 2026 on the build site, theme 0.708.024 at the start and 0.708.028 at the end. Other sessions shipped course page work meanwhile; git shows no commit to any file this page loads in that time.

**Folder:** `/private/tmp/claude-501/-Users-kainramsay-Documents-CLAUDE---Anthropic-Ai/03c15077-a23a-4ce8-b05f-acb45926942f/scratchpad/about/`

- `about-1440.png`, `about-768.png`, `about-390.png`: full-page pictures at scale 2. The consent banner was declined and every reveal played; each was taken at rest from the top, in 4,000 pixel pieces stitched together (D10 says why shot.py's single capture could not be used). The pinned Story shows its at-rest state, so its own frames are in `states/`.
- `states/`: viewport pictures of every moving part at 1440 by 900, 1440 by 1080, 768 by 1024 and 390 by 844. They cover the Story part way through, the era jumps, the question selector, hovers, the video dialog, the phone bar and back to top.
- `details/`: close-ups of the member strip, the 2025/26 row, the phone Story card and phone Story rows.
- `about-served.html` is the HTML as served. `data/` holds every measurement as JSON (`measure-*.json`, `interact.json`, `kbwalk-1440.json`, `weight.json`, `compare.json`). `tools/` holds the scripts that took them.
- Instruments run:
  - page_gate.py `--no-purge`: 61 passed, 57 failed, 33 carved out.
  - css_gate.py on about.css: PASS.
  - axe, run inside page_gate: zero WCAG 2.2 AA violations.
  - My own Playwright scripts in the installed Chrome.

### Where the page is right

- **Spacing:** hairlines and their 48/48 (32/32 on a phone) pass at every boundary page_gate reads, at three widths. Gutters are 48/32/20 and header to content 48/48/32.
- **Layout and type:** the 960 column holds; the H1 is 33/700; every H2 is 24/600/1.25 (DSRD 7 3.1 H2 Section). There is no sideways scroll at 390 or 768, and on a computer every unboxed block starts on one text line at 240.
- **Images:** all 17 are WebP or SVG with alt, srcset and sizes. The hero picture is the largest-picture candidate with fetchpriority high, and everything below the fold loads lazily.
- **Structured data:** both JSON-LD blocks parse and match the visible breadcrumb.
- **Questions:** the selector is a true accordion (h3, button, aria-expanded, aria-controls) and works by mouse and by Enter.
- **Video dialog:** it traps focus, closes on Escape, returns focus to the card and releases the scroll lock.
- **Movement:** the hero action lands the Story heading 52px under the header on a computer, and the era buttons move the Story to the right era.
- **Copy checks:** all 62 links resolve, and there are no em or en dashes.

### Known and not re-raised (recorded exceptions or Kain's rulings)

- DSRD 7 4.3 Exception 1 (the Story's upper boundary, 48 above and 32 below) and Exception 2 (the hero line on the text column).
- The 960 column (DSRD 9 29.1).
- The learning block's own spaces, auto gaps and drawings (Exceptions 18 and 21). page_gate still prints kfp-sign__sub at 10.8 and 2.1 and the phone section header at 12; Exception 18 covers them.
- The selector's collapsed answers (DSRD 6 chapter 6, S295).
- The AI acronym in Kain's 2023 words, and the 6 above the band labels (record chapter 11).
- The Related Questions gate reading, taken before the questions animate in.
- The opening paragraph at 21 on About only.
- The member questions kept for screen readers on About only (but see A1).
- The Story lede stepping aside on laptops under 960 tall (spec 5a row 2).

---

### A. What a visitor sees

**A1. Member video posters: the play button covers the printed question on all five cards, and the printed words are not the words screen readers hear.**
- **Where:** "Five Aspects of the Achology Experience", the five posters (`achology_member_story_cards()`, shared-parts.php lines 1636 to 1640; the badge is in components.css).
- **Evidence:**
  - `details/1440-member-strip.png`: the 44px play disc sits on the printed words, for example "studying", "that's", "collaborative" and "community". The same happens at 768 (`slices2/t-03.png`) and at 390.
  - The posters print the old questions, for example "How have you personally benefitted from studying Achology training courses?" and "What are the 5 things you value most about the Achology community?". The hidden caption, the alt and the button name carry Kain's S103 words ("How have you benefitted from studying Achology courses?", "What are the five things..."). Four of the five differ.
  - Kain's S209 ruling hid the caption "because the poster already carries the same words" (spec 5a); it does not. With the caption hidden, the only visible question on About is an image of text (WCAG 1.4.5).
  - The two large posters are soft on a Retina screen. They show 472px wide at 1440, `sizes` claims 432px, and the largest file is 640px wide where 944 is needed.
- **Fix:** re-export the five posters from their masters with Kain's S103 words, the words clear of the centre (or the badge moved to a corner). Add 960 and 1280 wide versions and a true `sizes`. Until then, show the caption again on About.
- **Size:** medium. **Kain's eye:** yes. **Shared:** shared-parts.php and components.css, reaching About and Testimonials.

**A2. Phone Story: the dark card shows 2026 at the top of a list that starts in 2012, and its chart runs through the era dates.**
- **Where:** The Achology Story at 390 (and any phone), where the block lies flat.
- **Evidence:**
  - `states/390-after-hero-action.png`: the bar under the menu reads "2012 Achology Origins" while the card below it reads "2026 / Community Development / 695,578", on one screen.
  - `details/390-stage-card.png`: the growth line and its "100,000" label cross "2024 to 2026".
  - Cause: in flat mode story-scroll.js line 269 paints the final year once, and the stage name and dates are absolutely placed over the chart (about.css lines 80, 92, 144).
- **Fix:** in flat mode, paint the card from the row being read (the phone bar already finds it, story-scroll.js lines 81 to 82), or paint 2012. Under 768, put the chart below the year, era and dates in normal flow.
- **Size:** medium. **Kain's eye:** yes.
- **Shared:**
  - story-scroll.js: About, plus the seven school pages, where it loads but finds nothing.
  - about.css: About, Testimonials, Founders' Letter, Reviews, Pricing, Code of Ethics, Code of Character and Conduct, /courses/ and the seven school pages.

**A3. Lone words and short last lines at tablet and phone widths.**
- **Evidence** (`data/measure-*.json`, lineBreaks, read after no-lone-words.js has run):
  - **390:**
    - The H2 reads "Five Aspects of the Achology / Experience", with one word alone. no-lone-words.js lines 26 to 28 cannot tie a last word that follows the orange Achology word, because the space sits at the start of the last piece of text, not the end of the one before.
    - The H2 reads "...and Who / It's For" (22 per cent).
    - Story paragraphs end on one word: "set." (2020), "practice." (2022), "encountered." (2024), "for." (2025/26).
    - "a new 28- / course curriculum" breaks at its hyphen (2023).
  - **768:**
    - Story paragraphs end "name." (2014), "order." (2015), "standard." (2019) and "had set." (2020, 12 per cent).
    - Headlines fold at 19 to 20 per cent: "...Published / on Udemy" and "...Founded with / 12 Courses".
    - The open answer ends "understanding needs." (24 per cent).
    - The founders block ends "named Skye." (27 per cent, also at 390).
    - The flagship card ends "this year." (18 per cent).
    - Related Questions excerpts end "own terms." (11 per cent) and "the standards." (15 per cent).
  - **1440:** clean, apart from two Related Questions titles at 39 and 46 per cent.
- **Cause:** Kain's S209 trim of the Story was measured on a computer only. no-lone-words.js line 15 does not list `.m-desc`, `.pfq-panel p`, `.founders__text p`, `.help-q__excerpt`, `.gateway__desc` or `.tw-lede`.
- **Fix:**
  - Mend the orange-word case in no-lone-words.js: when the last piece of text starts with a space, make that space a no-break space.
  - Add the six selectors.
  - Add `text-wrap: balance` on `.m-title` and the block H2s, and `text-wrap: pretty` on the paragraphs. DSRD 7 3.2 already uses it on the Question List.
- **Size:** medium. **Kain's eye:** yes. **Shared:** no-lone-words.js (the founder pages and About) and about.css.

**A4. The video dialog's close button sits top left, 8px cut off, and the header stays bright above the dimmed page.**
- **Where:** the member video dialog, at every width.
- **Evidence:**
  - Pictures: `states/1440-dialog-open.png` and `states/390-dialog-open.png`.
  - Read with the dialog open: the close button is `position: relative` at x = -8, inside a panel with `overflow: hidden`, transparent with a white mark.
  - components.css line 723 places it absolute, top 8, right 8, on a white disc. buttons.js gives it `.bf-icon`, and buttons.css line 294 (`:root .bf-icon { position: relative }`) wins over it.
  - The header is `z-index: 1000` and the dialog 300, so the header sits undimmed above the backdrop. It is inert, so it looks live and does nothing.
- **Fix:** keep the two dialog close buttons absolute (one rule in the button family for close buttons inside dialogs), and raise the dialogs above the header.
- **Size:** small. **Kain's eye:** yes. **Shared:** components.css and buttons.css, site wide; reaches About and any page that renders `.shared-video-lightbox`.

**A5. The timeline's count chips: orange numbers at 3.16 to 1, and on a phone a squashed icon.**
- **Where:** the four chips (2017, 2021, 2022, 2025/26).
- **Evidence:**
  - Computed `color: #ED6922` on white at 18px, 700 (16px on a phone): 3.16 to 1 against the 4.5 bar. 18px bold is under the 18.66px large-text line, and DSRD 7 section 1 says brand orange "fails AA below large-text size".
  - The colour is inline, page-about.php lines 340, 379, 388 and 430.
  - At 390 the round people mark is squeezed into an oval and the label wraps to two lines (`states/390-after-era-4.png`).
- **Fix:** set the number in `--color-orange-link` (#B8460F, 5.35 to 1), and add `flex-shrink: 0` on `.tw-track .m-stat__icon` (about.css line 585).
- **Size:** small. **Kain's eye:** yes (a colour). **Files:** page-about.php (page only) for the colour; about.css (shared, as in A2) for the icon.

**A6. Phone: the "Community Development" era heading breaks onto two lines.**
- **Evidence:** `slices2/m-03.png` (390): the pill reads "COMMUNITY / DEVELOPMENT" and its dates "2024 to / 2026". The other four era headings fit on one line.
- **Fix:** let the dates drop under the pill on a phone (`flex-wrap: wrap` on `.fam-group__head`, `white-space: nowrap` on `.m-dates`).
- **Size:** small. **Kain's eye:** yes. **Shared:** about.css.

**A7. Phone: an era button lands its era heading under the phone bar.**
- **Evidence:**
  - `states/390-after-era-4.png`, read by script: after "The Evolution Years", the era heading's top is at 80 while the bar covers 72 to 117.
  - The hero action lands the Story heading at 113, touching the bar (`states/390-after-hero-action.png`).
- **Fix:** under 768, set `scroll-margin-top` on `.fam-group` and `#about-story` to the header plus the bar plus 16.
- **Size:** small. **Kain's eye:** yes. **Shared:** about.css.

**A8. On a computer the question selector can be emptied.**
- **Evidence:** `states/1440-pfq-all-closed.png`. Clicking the open question closes it, the right column goes blank and the block shrinks to a list of five (about.js lines 160 to 166, "Clicking the open question closes it").
- **Fix:** from 1024 up, clicking the open question keeps it open. Below 1024, keep the accordion as it is.
- **Size:** small. **Kain's eye:** yes. **Shared:** about.js (About and Pricing, whose questions block is the same `.pfq`).

**A9. Keyboard: Tab skips six of the Story's seven links, including its closing "start right here".**
- **Evidence:** `data/kbwalk-1440.json`. Stop 16 is "Kain Ramsay" (2012); stop 17 is the first member video card.
- **Skipped links:** Prof. Gerard Egan, the DiMAP link, accreditation, the Society, free events and "start right here" (to /membership/).
- **Cause:** story-scroll.js lines 254 to 266 give any link outside the window `tabindex="-1"`, and nothing brings a focused row into the window. A keyboard reader can reach them only by scrolling with the arrow keys first.
- **Fix:** keep every link in the Story tabbable. When one takes focus, scroll the page by the row's distance from the reading line; the Story moves one to one with the page, so the distance is known.
- **Size:** medium. **Kain's eye:** no (behaviour), but it reopens the spec section 8 item 6 choice (D5). **Shared:** story-scroll.js.

**A10. The 2020 headline is the one sentence-case headline among thirteen.**
- **Evidence:** "COVID-19 pandemic accelerated the acceptance of online learning worldwide" (page-about.php line 365, `states/1440-story-2.png`). `git log -S` shows it unchanged since v0.36.0; every other headline is Kain's S209 title-case wording.
- **Fix:** Kain's or Chat's words in title case (copy, D3).
- **Size:** small. **Kain's eye:** yes. **File:** page-about.php (page only).

**A11. "2025 / 26" crowds its count chip from 768 up.**
- **Evidence:** `details/1440-row-2025-26.png`. The year is about 97px wide in a 96px column and the chip reaches 17px to the left, leaving about 5px between them; the other years leave 40 or more.
- **Fix:** let that chip start where the year's column ends, or widen the year column to 104 on this row only.
- **Size:** small. **Kain's eye:** yes. **Shared:** about.css.

**A12. The phone bar's year is orange on dark at 3.3 to 1.**
- **Evidence:** `.tw-phonebar b` is 18px, weight 900, #ED6922 on #354149. DSRD 7 section 1 measures that pair at 3.32 to 1, under 4.5 for text below 18.66px. The light orange #F5A05C is the registered small orange on this dark (5.0 to 1).
- **Fix:** `.tw-phonebar b { color: #F5A05C }` (about.css line 659).
- **Size:** small. **Kain's eye:** yes. **Shared:** about.css.

**A13. The learning block's "OUT OF 5" measures 4.2 to 1.**
- **Evidence:** `.kfp-sign__of` is 14px, 600, #F5A05C on the rating panel at rgb(65, 76, 84): 4.2 to 1 (`data/measure-1440.json`, contrast), at all three widths.
- **Fix:** a lighter warm orange for this one label. The band already uses #F8B27A for Read All Student Reviews (DSRD 9 39.15).
- **Size:** small. **Kain's eye:** yes. **Shared:** kh-front.css, reaching About, Pricing, /learn/, the subject pages and the list pages.

**A14. The Story's foot (known; recorded once, not designed here).**
- **What you see:** the Story ends on Kain's closing line, then the Story's own closing hairline (the `.tw-wrap` bottom border, about.css line 434). The four-number band sits 48 below that line, and the "Five Aspects" heading 48 below the band, with no line between them.
- **Evidence:** `states/1440-story-after.png`; measured at 4507, 4555 and 4741 at 1440.
- **Effect:** the band reads as the top of the member stories, not the end of the Story. The redesign is already planned elsewhere.

**A15. On a 1440 by 900 laptop the pinned Story leaves about 100px of empty white under its window.**
- **Evidence:** `states/1440-story-2.png`. The frame is 705px tall from a top of 92, so it ends at 797 of 900. The laptop rule sizes the window at `100vh - 520px` (about.css line 650), tuned for windows about 640 tall.
- **Fix:** on screens 900 tall and over, let the window take the spare height (for example `calc(100vh - 420px)`), shown to Kain before and after.
- **Size:** small. **Kain's eye:** yes. **Shared:** about.css.

**A16. The Story's counter reads 11,512 against 2012 at rest.**
- **Evidence:** `interact.json`, "1440_rest" and "1440_after_hero_action": the count reads 11,512 with the odometer on 2012. The data's 2012 point is 5,000, and DSRD 9 23.3 says "At rest: 5,000". The reading line, 96px into the window, already sits past the first row when the Story starts.
- **Fix:** hold the first row's value until the reading line passes its title.
- **Size:** small. **Kain's eye:** yes. **Shared:** story-scroll.js.

**A17. Below 1024 the questions block sits 16px in from the page's text line.**
- **Evidence:** at 768 the heading and intro start at 32, the answers at 48 and the marks just inside them. At 390 the figures are 20 against 36 (`data/measure-768.json`, `measure-390.json`, edges). On a computer a negative 16px margin brings them back to the line. DSRD 7 4.4a says every block's words begin on one vertical line.
- **Fix:** below 1024, `.pfq-q { margin-left: -16px }` and the panel's side padding to 0, as on a computer.
- **Size:** small. **Kain's eye:** yes. **Shared:** about.css (About and Pricing).

**A18. The block supporting lines are not yet the Lead with Bar component (known, waits on the sweep).**
- page_gate fails six supporting lines at three widths: What It Is, Thinking, Story, Five Aspects, Ten Ways and Related Questions. They are 16 or 14px with no orange bar.
- DSRD 7 3.3 says every page moves onto the component "only under the signed sweep brief". Recorded here because these account for most of the 57 gate fails.

---

### B. Behind the scenes

**B1. The closing learning block brings 87 KB of stylesheet for about 1 KB of rules.**
- **Evidence** (`data/weight.json`, Chrome's record of which rules apply, after scrolling, opening every question and hovering):
  - knowledge-hub.css is 291,470 bytes (86,918 compressed); about 1,348 bytes of its rules are used on About.
  - kh-front.css is 44,562 bytes; about 9,745 are used.
  - kh-front.js is 8,588 bytes; about 91 per cent never runs.
  - All three are loaded by kh-front-setup.php lines 48 to 52.
- **Fix:** give the learning block its own small stylesheet (its kfp rules and the few knowledge-hub.css rules it relies on), loaded by its own renderer. Prove no change in computed style on About, Pricing and /learn/ at three widths.
- **Size:** large. **Kain's eye:** no. **Shared:** kh-front-setup.php, kh-front.css and knowledge-hub.css (About, Pricing, the Knowledge Hub pages). Waits.

**B2. The two figures are typed into the template, against the spec.**
- **Evidence:** spec section 6 item 2 wants "the two counts read from their homes, not typed".
  - page-about.php types 695,578 at lines 104, 269, 430 (twice), 440 and 703, and as 695.578 in the Story data at line 239.
  - It types 216 at lines 104 and 703.
  - The register is `achology_figures()` (shared-parts.php lines 635 and 636).
- **Fix:** print the register's values in those places; the served text stays identical.
- **Size:** small. **Kain's eye:** no. **File:** page-about.php (page only). Not in C because those lines hold Kain's sentences; the main session should agree first.

**B3. The modified date is three months stale, and three dates disagree.**
- **Evidence:**
  - The JSON-LD `dateModified` reads 2026-08-04 (page-about.php line 40).
  - `og:updated_time` reads 2026-09-02.
  - Kain's new opening, Story lead, headlines and close shipped on 2 November (commits b16913ee, and 4413f229 to 8611fe35).
  - DSRD 6 chapter 6 item 2: the date "changes only when the content genuinely changes".
- **Fix:** set `ACH_ABOUT_MODIFIED` to 2026-11-02.
- **Size:** small. **Kain's eye:** no. **File:** page-about.php (page only). It changes the served data, so it is not in C.

**B4. About carries its own copy of the member video dialog.**
- **Evidence:**
  - page-about.php lines 666 to 672 and about.js lines 222 to 246 do what `achology_shared_video_lightbox()` and shared-parts.js already do. About passes `'lightbox' => false` (line 461).
  - DSRD 3 2.6: "A page-local copy of a shared block is a defect." DSRD 8 12.2 also says neither page "carries a private copy".
  - The copies differ. About's iframe is titled "Achology member story"; the shared one is titled "Achology member story video" and hides Vimeo's title, byline and portrait.
- **Fix:** drop About's dialog and handler and use the shared one; compare the two open dialogs in pictures.
- **Size:** medium. **Kain's eye:** only if the pictures differ. **Shared:** page-about.php, about.js and shared-parts.php.

**B5. The hero action and back to top leave keyboard focus behind.**
- **Evidence:**
  - about.js lines 78 to 81 stop the browser's own jump and scroll by script instead, so focus stays on the button at the top while the view is at the Story. The next Tab goes back up to the first question.
  - Back to top (lines 92 to 94) scrolls up and then hides itself (line 90), so focus falls to the page body.
- **Fix:** after the scroll, focus the Story heading (`tabindex="-1"`). After back to top, focus the H1 or the skip target.
- **Size:** small. **Kain's eye:** no. **Shared:** about.js; the code only acts on About's markup.

**B6. Pictures sized wrongly for the screen.**
- **Evidence:**
  - (a) The posters, as in A1: `sizes` says 432px, they show at 472px from 1024 up, and the largest file is 640 wide.
  - (b) On a phone the 900px hero file (93,804 bytes) loads at fetchpriority high to draw a backdrop at 12 per cent opacity. `sizes` "(max-width: 599px) 100vw" picks the 900 wide file at scale 2 and 3.
  - (c) The flagship tile's background, course-001.webp (704 by 370, 66,386 bytes), is drawn at about 292 by 310, so at scale 2 it is enlarged about 1.2 times.
- **Fix:**
  - (a) As A1.
  - (b) `sizes` "(max-width: 599px) calc(100vw - 40px)", and drop fetchpriority on phones (or serve the 640).
  - (c) An image-set with a larger version.
- **Size:** small. **Kain's eye:** no. **Files:** shared-parts.php (a), page-about.php (b, page only), components.css (c, site wide).

**B7. Rules in about.css that never apply on About.**
- **Proof that the Story classes are About's alone:** `m-stat`, `m-year`, `m-title`, `cons-*`, `fam-*`, `odo-*` and `tw-track` appear in page-about.php only. The school page moved to its own `sps` block at S497; school-page.js line 15 names `fa-row` only in a dead section.
- **Overridden on every About element by later `.tw-track`, `.tw-frame` and `.cons-stage` rules:**
  - `.m-stat` and `.m-stat span` (lines 29 to 30), `.m-year` (26), `.m-title` (27), `.fa-row.read .m-title` at 700 (106).
  - `.policy-body .m-desc` at 14 and grey (28).
  - The `.cons-count__num` gradient and its #F5A05C one-off (126 to 129).
  - `.cons-terminus__bar` at 14 by 3 and its UNRESOLVED 2px note (116 to 122), and `.cons-terminus p` (123).
  - `.fam-odo`, `.odo-col` and `.odo-strip span` at 104, and the under-1024 rule at 56 (57 to 69).
- **Repeated:**
  - `.fam-groups` is identical to `.fam-groups--full` (54, 73).
  - `.tw-wrap` (434, 454), `.cons-terminus` (115, 133, 565, 614) and `.cons-groups` (132, 136) are each split over several rules.
  - `.cons-groups .m-dates` repeats `.m-dates`.
- **Fixed numbers where a design-system value exists:** `.st-lm` names `'Como'` (97); `.tw-track` padding is `24px` (501); `.founders` gap is `64px` (691); `.tw-frame { top: 92px }` appears twice (449, 662).
- **`!important`:** on `.tw-track .m-year` (508) it exists only to beat the dead inline colours (C5).
- **Fix:** delete and merge, proved by a computed-style comparison of About at three widths.
- **Size:** medium. **Kain's eye:** no. **Shared:** about.css (every page listed in A2). Waits.

**B8. Comments that now say the wrong thing (shared files).**
- **about.css:**
  - The file header lists sections 1 to 7; the body runs to 16, with no section 5.
  - It says the blocks are used by page-about.php only, while nine page types load it.
  - Lines 263 to 273 and 318 describe a question-mark icon and a "solid orange disc with a white mark". The button family now draws plus and minus rings (`states/1440-hero.png`).
  - Lines 276 to 278 say the weights went to 600 and 700, against lines 253 to 258 and the measured 500 and 600.
  - Lines 616, 621 and 654 name about.js for work story-scroll.js now does.
- **about.js lines 1 to 9:** "Three independent scripts" heads a list of four, still lists the timeline (now in story-scroll.js), and says "Loaded only on /about/" (Pricing loads it too, functions.php line 987).
- **functions.php:** the 6j comment (lines 947 to 956) sits above 6k's code; 6j's code is at 985 to 989.
- **story-scroll.js line 4:** "The About page and the seven school pages run from this one file". DSRD 8 12.1 says it has been About's alone since S497.
- **Fix:** correct the comments. They are invisible, but the files are shared, so they are not in C.
- **Size:** small. **Kain's eye:** no. **Shared:** about.css, about.js, functions.php and story-scroll.js.

**B9. What the page weighs** (`data/weight.json`, 1440).
- The HTML is 155,021 bytes (27,520 compressed).
- Eighteen stylesheets come to about 1.05 MB once unpacked (about 299 KB compressed). Chrome counts about 163 KB of rule text as used; the rest is unused rules and comments.
- Two site-wide sheets have no rule used on About at all: cards.css (110,831 bytes) and people.css (55,796).
- help.css is about 6 per cent used, policies.css about 6 and components.css about 14.
- ConvertKit's frontend.css and frontend.min.js load though there is no form on the page.
- Scripts come to about 135 KB unpacked, 46 KB of it Complianz.
- Fonts: four files, about 93 KB.
- None of this is About's alone to fix: see D8.

**B10. Smaller code points.**
- The era buttons mark the era being read with a class only (`is-on`, story-scroll.js line 288). Adding `aria-current="true"` would tell a screen reader. Small, story-scroll.js.
- `og:image:alt` is "About". A description of the share picture would be better (a Rank Math field, set over WP-CLI). Small.
- `<div id="bottom">` wraps the learning block (page-about.php line 632). It is fine, but Pricing and the Knowledge Hub pages use the same id for the same block, so the shared anchor name is worth recording in the component's notes. No change.

---

### C. Invisible tidy-ups safe to ship now

These touch only page-about.php and about-setup.php, and both serve About alone:
- page-about.php is WordPress's template for the page with slug `about`, and no file includes it; a search of every theme php and js file finds it named only in comments.
- about-setup.php's functions are called only from page-about.php line 750 (`achology_about_videos`). Its filter acts only on the `group_about_videos` field group, and `achology_iso8601_duration` is called only inside the file.

Every change below is a PHP comment, which is never sent to the browser, except C5, whose proof is given with it.

**C1. page-about.php, the file's opening comment, lines 10 to 17** (from "The page is static by design." to "see functions.php."). Replace with:
```
 * The page is static by design. Every word, figure and route is baked into
 * the theme rather than the editor, because the layout is bespoke throughout:
 * a pinned timeline window, a question selector, a member-story grid and the
 * Knowledge Hub's learning block as its close. None of it survives being
 * retyped in Gutenberg. Editing the page means editing this file.
 *
 * Assets (functions.php section 6f and step 10, and kh-front-setup.php):
 * about.css after policies.css, whose frame this page borrows; story-scroll.js
 * then about.js; and, for the closing learning block, knowledge-hub.css,
 * kh-front.css and kh-front.js. about.css and about.js also load on other
 * pages that reuse this page's blocks.
```
Why: the old text promises a "ten-direction close" and says the two files load "for this page only". Both stopped being true: the page has closed on the learning block since S209, about.css loads on nine page types, and about.js also loads on Pricing.

**C2. page-about.php lines 32 to 38** (the comment opening "The page's two honest dates"). Replace with:
```
/*
 * The page's two honest dates, in one place because the JSON-LD reads them
 * (datePublished and dateModified). The page shows no "Page updated" line:
 * Kain removed it at S238 (see the note at the foot of this template).
 * Published is the day the page first shipped (v0.36.0, 22 July 2026).
 * Modified moves only when the page genuinely changes, which is the whole
 * point of the signal.
 */
```
Why: the old comment says a visible "Page updated" line reads these dates; lines 634 to 649 of the same file record that the line was removed.

**C3. page-about.php lines 699 to 700** (the comment opening "The same two dates the visible"). Replace with:
```
	/* The two dates defined at the top of this file. The page shows no visible
	   date (Kain, S238); these are the machine-read half of DSRD 6 section 6. */
```
Why: it repeats the same stale "visible line" claim.

**C4. page-about.php lines 243 to 267** (the comment opening "S103: Kain's rewrite of this lead", in the PHP block before the `tw-lede` paragraph). Replace the comment's contents with:
```
					 * Kain's own Story lead, placed word for word at S209 (2 November
					 * 2026; spec section 3). It is 21 words, inside DSRD 7 section 3.3's
					 * 12 to 25, so the S103 recorded exception, written for the
					 * 29-word line this one replaced, no longer applies. The 695,578
					 * is the locked figure.
```
Why: the comment describes a 29-word line and an exception the spec says "no longer applies". The line below it is Kain's 21-word S209 line.

**C5. page-about.php, the thirteen year lines: remove the inline colour.**
- **Lines:**
  - 297 and 306 (`style="color:#354149"`)
  - 321, 330 and 339 (`#4d6672`)
  - 354 and 363 (`#6b7680`)
  - 378, 387 and 396 (`#c05a1a`)
  - 411, 420 and 429 (`#ED6922`)
- **Change:** each `<div class="m-year" style="color:...">` becomes `<div class="m-year">`; the text is unchanged.
- **Why invisible:**
  - about.css lines 507 to 508 set `.tw-track .m-year { ... color: var(--color-dark) !important; }`, outside any media query. An `!important` rule in a stylesheet beats a normal inline colour.
  - All thirteen years sit inside `.tw-track` (page-about.php lines 288 to 437).
  - about.css loads on About at every width (functions.php lines 848 to 850).
  - No script reads a year's style; story-scroll.js reads only its text (lines 85 and 117).
- **Measured:** every `.m-year` computes rgb(53, 65, 73) at 1440, 768 and 390. Prove it after the change with the same computed-colour read and a picture comparison at three widths.
- **Record:** the design records that still describe era-coloured years are listed in D1.

**C6. about-setup.php lines 11 to 14** (from "Nothing here renders anything." to "the AboutPage block above it."). Replace with:
```
 * Nothing here renders anything. The five posters on the page come from
 * achology_member_story_cards() in shared-parts.php; what these values
 * produce is the VideoObject schema (DSRD 10 §9), emitted at the foot of
 * page-about.php with the same custom-JSON-LD pattern as the AboutPage block
 * above it. Until the group is filled in, it produces nothing.
```
Why: the posters have not been "baked in the template" since the member stories moved to a shared function.

---

### D. Questions for the main session

**D1. Records that no longer match the built page. Who corrects which?**
- **Spec section 3** records an earlier wording of both the opening paragraph and the What It Is intro line. The template carries Kain's later words (commits b16913ee, 4a652c0b and 0679b6b8, theme 0.707.756 and 0.707.757).
- **DSRD 7 3.3** still carries two recorded exceptions for lines no longer on the page: the S103 29-word Story lead and the S349 41-word What It Is line.
- **DSRD 7 3.1** gives the odometer 104px on a computer. As built it is 56, 42 on laptops under 960 tall, and 33 under 1024.
- **DSRD 7 1.2** says the year text takes the era colour; the built years are dark (S209), see C5.
- **DSRD 8 12.1** says the blocks are "used by page-about.php only" and the selector is "all closed on load" (the first question opens). It also says the member stories carry no private copy of the dialog, which B4 contradicts.
- **DSRD 9 23** still has the old lede, "At rest: 5,000" and "Origins", years "at 24", the counts as "pills, 14 on an orange wash" (built as outlined chips at 18 and 700), the old window heights, and "enqueued only on /about/".
- **DSRD6_RECORD.md:**
  - Chapter 1 fails on "history books" and "ecosystem", and chapter 2 on a 44-word line. None of these is on the page now; a search of the served HTML finds none of them.
  - Chapters 3, 4, 5 and 9 read "not run".
  - page_gate reads the record as "4 closed, 4 not run, 3 fail".

**D2. The title says "Since 2017"; the page says "Since 2014".** The Rank Math title, and the share titles, read "About Achology: Applied Psychology Education Since 2017". Kain's opening paragraph says "Since 2014", and the description says "a decade". This sits beside the open founders "in 2017" point in spec 5a. Chat's and Kain's.

**D3. Copy points for Chat.**
- The fifth question heading is two sentences and reads "by who" (Chat noted "whom" at S295).
- The 2020 headline is in sentence case (A10).
- The shared gateway's "the Achology 28 course curriculum" lacks its hyphen (About, Testimonials and Reviews).
- The 2019 milestone links "Diploma Course in Modern Applied Psychology (DiMAP)" to /courses/, although the DiMAP course page is now published.
- The posters say "5 things" where Kain wrote "five" (A1).

**D4. Which line rule governs About?** The brief's rule (no last line of one, two or three words) is stricter than DSRD 7 4.1's written standard. That standard says titles have no lone word and fold near two thirds, never under 40 per cent; descriptions have no lone word and no last line under 40 per cent. DSRD 7 says it is built only on the Help category band. A3 lists every case under both readings.

**D5. Does spec section 8 item 6 still stand?** It chose `tabindex="-1"` for Story links outside the window. That leaves six links and the Story's call to action out of the keyboard path (A9). Reopening it changes the behaviour of a signed mechanic.

**D6. Kain's S209 ruling to hide the member questions on About** rested on the posters carrying the same words, and they do not (A1). Re-export the posters, or show the captions again?

**D7. The hero's scroll-down button shows its arrow at a diagonal.** The button family turns every arrow 45 degrees at rest (buttons.css line 102). So the down arrow (DSRD 7 5.2, "Hero story button arrow") rests pointing down and right, and points straight down only on hover. Is that intended for this button?

**D8. Site-wide weight.** cards.css and people.css load on every page and use nothing here; ConvertKit's files load on pages with no form. Whose job is it, and is per-template loading wanted?

**D9. Text on the dark at white 65 per cent.** The Story card's dates and counter caption, and the band's labels, sit between the three strengths written into DSRD 7 3.2 at S464 (0.9, 0.72, 0.56). They pass AA (about 4.7 to 1 at the card's lightest corner, 5.4 on #354149). Move them to 0.72, or record the 0.65?

**D10. Problems with the measuring tools.**
- **(a)** shot.py's full-page capture at scale 2 repeats the top of the page once the picture passes 16,384 device pixels. All three About pictures it took were wrong at the foot; the 1440 one from about 8,200 css pixels down. Taking pieces and stitching them, as here, avoids it.
- **(b)** In a capture taken beyond the visible window, the 768 hero artwork vanished: its arrival animation (help.css line 1740) restarts and is caught at opacity 0. I held it at full opacity for the capture only.
- **(c)** page_gate's image-dimensions FAIL on three posters does not reproduce. The served files are 640 by 360 (1.778) against attributes of 460 by 258 (1.783), inside its 0.02 tolerance. The "704x370 file" it names is the size of course-001.webp, so the check appears to pair the wrong image; I have not verified beyond that.
- **(d)** keyword-density reports "the body is empty" on a page built from a template.

**D11. Structured data.**
- No VideoObject is emitted, because the ACF group is still empty (as at S139). The five Vimeo IDs already live in `achology_member_story_cards()`. Read the schema from there (one source), or wait for the group?
- The AboutPage `about` entry is a stub (name and address only), because nothing outputs the Organization on this page.
- Chat's BRIEF__Search_Data_On_Every_Built_Page_Type covers built page types; is About in it?

**D12. Are the Story's laptop window (A15) and its at-rest counter (A16) worth Kain's time now,** given the Story's foot is already being redesigned in another session? Both are in the same files and could go with that work.

---

## Audit: the Member Testimonials page, /testimonials/

Read only; nothing in the theme or the project was changed. Measured on the build site on 11 November 2026 against theme 0.708.023 to 0.708.025; other sessions deployed while this ran. Read this session: the signed spec, DSRD6_RECORD.md, DSRD 7 sections 1, 1.1, 3 to 3.3a, 4 to 4.5 and 5.3, the Component Registry, and the stylesheet and template comments on every block named below.

### Files beside this one (all in the testimonials output folder)

- **Full pages:** `full-1440.png` (2x), `full-768.png` (1x), `full-390.png` (1x), with the cookie banner hidden in the headless copy.
  - 768 and 390 are taken at 1x because Chrome repeats tiles in any capture taller than 16,384 device pixels.
  - shot.py's own 768 and 390 pictures had that fault (the lower third of the phone picture repeated the top), so they were deleted.
  - `testimonials-1440.png` is shot.py's first-visit view, with the cookie banner over the question buttons.
- **Slices:** `slice-1440-00` to `-07`, `slice-768-00` to `-04`, `slice-390-00` to `-05`.
- **Dialog pictures:** `lightbox-1440.png`, `lightbox-1280x720.png`, `lightbox-390x800.png`, `lightbox-768x1024.png`, `story-lightbox-1440.png`, `about-dialog-1280x720.png`.
- **Question button states:** `shuffle-mid-1440.png`, `tab5-1440.png`, `tabs-hover-1440.png`, `tabs-focus-1440.png`, `tabs-keyboard-focus-1440.png`.
- **Measurements:** `measure-1440/768/390.json`, `interact-1440.json`, `interact2.json`, `compare.json` (the same blocks on /about/ and /reviews/), `vimeo-check.json`, `weight.json`, `c-proof.json`, `served.html`, `served-headers.txt`. The scripts that produced them are the `.py` files in the folder.
- **page_gate:** run once with --no-purge, so it must not be used for the record.

### Where the page is right

- **No sideways scroll** at 1440, 768 or 390.
- **Spacing at block boundaries.** Every boundary reads 48 above and 48 below the hairline at 1440 and 768, and 32 and 32 at 390. Header to breadcrumb is 48, breadcrumb to title 48, title to lead 24. The hero line stopping at the text column is DSRD 7 section 4.3 Exception 2.
- **One text line.** Every block's words start at 240 at 1440 (32 at 768, 20 at 390). The card grid, global impact panel and enquiries panel bleed 32 either side on Kain's S142 960 column (components.css line 1146).
- **Type.** The H1 is Como 33/700/1.2. Every block heading is 24/600/1.25. The lead is the Lead Paragraph row, 18/500/1.55.
- **Accessibility scan.** No text on a flat ground falls below its contrast bar. axe 4.10.2 reports zero WCAG 2.2 AA violations.
- **Question buttons.**
  - Each press sets aria-pressed on that button alone.
  - It re-orders the nine cards and swaps quote, picture, alt text, srcset and the play button's name.
  - The first render matches the data's first question exactly (0 mismatches).
- **Keyboard.**
  - Tab goes breadcrumb, then the five buttons, then the nine cards, each with a visible 2px orange ring.
  - Enter opens the dialog with focus on its close button.
  - Tab stays inside the dialog, Escape closes it, and focus returns to the opening card.
  - While it is open, the page behind is inert and aria-hidden and scrolling is locked.
- **Structured data.** Both JSON-LD blocks parse. The WebPage description matches the meta description, and the BreadcrumbList matches the visible trail.
- **Alt text and links.** All 27 pictures carry alt text, and all 53 links resolve.

---

### A. What a visitor sees

#### A1. The five question buttons sit inside one huge pill-shaped outline, and the rows have lost their own lines
- **Where:** Block 4.
  - At 1440 a wide oval runs through the rows below the chosen one.
  - At 390 it becomes a tall oval cutting across every row.
  - Each row has lost its hairline and white box; only the chosen row shows its fire frame.
- **Evidence:**
  - Pictures: `slice-1440-00.png`, `slice-1440-01.png`, `tabs-keyboard-focus-1440.png`, `slice-390-00.png`, `slice-768-00.png`.
  - Measured at 1440: `.tm-filter` is 960 x 342 with border-radius 999px, and every `.tm-tab` border is transparent.
- **Cause:**
  - buttons.js line 164 adds the parent of any `.tm-tab` to the family's tab rows.
  - buttons.css lines 216 to 223 then give that row `border-radius: var(--radius-pill) !important` and an inset hairline ring.
  - buttons.css lines 225 to 235 strip each tab's border and background.
  - That treatment was made for a one-line horizontal tab bar. testimonials.css line 59 says the family was meant to reach these buttons, but not as a pill track.
- **Fix:** Keep the family's chosen-row fire frame, focus ring and hover. Drop the track ring and pill radius on a vertical row, either with a stacked-row modifier or a selector naming `.tm-filter`. Give each row back the hairline testimonials.css line 49 describes. Which of two looks is Kain's to pick (D10).
- **Size:** Small to medium.
- **Kain's eye:** Yes.
- **File:** Shared. buttons.css and buttons.js load on every page; a selector naming `.tm-filter` reaches this page alone.

#### A2. The video dialog's close button is knocked into the top-left corner, half cut off, and pushes the video down
- **Where:** The answer dialog and the story dialog.
  - The close button should be a white disc at the top right over the video.
  - It sits at the panel's top-left corner as a thin ring, cut in half by the panel edge.
  - The video drops 40px, leaving a white strip above it.
- **Evidence:**
  - Pictures: `lightbox-1440.png`, `lightbox-390x800.png`, `lightbox-768x1024.png`, `story-lightbox-1440.png`.
  - Measured at 1440 x 900: panel left 260 against close left 248, close position `relative`, video top 40px below panel top.
- **Cause:**
  - On opening, buttons.js `icons()` (lines 246 to 255) names the close an icon button (`bf-icon`).
  - buttons.css lines 293 to 303 (`:root .bf-icon`, loaded last) set `position: relative`, `background: none !important` and a dark colour.
  - These override testimonials.css line 99 (absolute, top 12, right 12, white disc).
- **Same on /about/:** At 1280 x 720 its close left is 102 against panel left 110, position relative, transparent fill (`about-dialog.json`, `about-dialog-1280x720.png`).
- **Fix:** Add `.tm-lb__close, .about-video-lightbox__close, .shared-video-lightbox__close` to the skip list in `icons()` so each dialog's close keeps its signed disc. Restoring the position alone is not enough: the family's dark cross with no fill would vanish on the black video.
- **Size:** Small.
- **Kain's eye:** Yes.
- **File:** Shared (buttons.js, every page). The fix changes only these three dialogs.

#### A3. Forty of the forty-five filmed answers refuse to play on the build site
- **Where:** Every answer card except five.
  - Vimeo shows "Sorry. Because of its privacy settings, this video cannot be played here."
  - The five that play (1033843642, 929543499, 1033838777, 1033842856, 1033845034) are exactly the five member story videos.
- **Evidence:** `lightbox-1440.png` and `vimeo-check.json`. Each player was loaded once with the build page as referrer, in headless Chrome, not Safari.
- **Known context:**
  - The record's S296 note says permission is set for achology.com and will work at cutover, which leaves chapter 11 unable to close on the build site.
  - Spec section 4b says the fourteen other videos were given achologytest.com at S090.
- **Fix:** Add achologytest.com to the forty videos' embed lists with tools/vimeo_embed_whitelist.py, then re-run vimeo_check.py. This writes to the Vimeo account, so it needs Kain's authority (D1).
- **Size:** Small.
- **Kain's eye:** Yes.
- **File:** No theme file.

#### A4. The site header stays bright on top of the open dialog and covers its top edge
- **Where:** The open dialog.
  - At 1440 x 900 the panel's top 21px is under the header.
  - At 1280 x 720 the top 40px is under it, where the close button would sit.
- **Evidence:**
  - Pictures: `lightbox-1440.png`, `lightbox-1280x720.png`.
  - header.css line 37 is `z-index: 1000`; testimonials.css line 68 is `.tm-lb { z-index: 300 }`.
  - components.css line 697 gives About's dialog 300 as well (`about-dialog-1280x720.png`).
  - The workbook and certification viewers use 1000 and do not have this fault.
- **Fix:** Raise the dialog layer above 1000, in testimonials.css line 68 and components.css line 697 together.
- **Size:** Small.
- **Kain's eye:** Yes.
- **File:** testimonials.css is page-only. components.css is shared: /about/ and any page drawing member stories with the default dialog.

#### A5. Single words alone on the last line: the page is left out of No Lone Words
- **Counts:**
  - One-word last lines: 3 at 1440, 17 at 768, 17 at 390.
  - Two- or three-word last lines: 23 at 1440, 14 at 768, 28 at 390.
- **Examples:**
  - At 1440: "offers" (gateway line), "courses?" (second related question), "personally." (enquiries body).
  - At 768: the H1 ends "Words", and four of the five story captions end on one word.
  - At 390: "Questions" (Nine Achologists heading), "courses?" and "community?" in two buttons, and four related answers.
  - The full list per width comes from running `lines.py`.
- **Evidence:** measure-*.json lastLines, measured after the page's scripts ran. compare.json shows no-break spaces present on /about/ and absent here.
- **Cause:** no-lone-words.js line 15 reads `main.policy-page--about:not(.policy-page--testimonials)`.
- **Fix:**
  - Add a PAGES entry for `main.policy-page--testimonials` with About's lines plus `.tm-heading, .tm-intro, .tm-tab__q, .gi-intro__title, .gi-intro__lead, .gi__heading, .gi__lead, .lite-quote`.
  - testimonials.js line 40 rewrites `.lite-quote` on each question change, so the quotes need the tie re-applied there.
  - The feature removes one-word lines only, not two- or three-word ones (D6).
- **Size:** Small.
- **Kain's eye:** Yes.
- **File:** no-lone-words.js loads everywhere but acts only on the pages it lists, so the new entry reaches this page alone.

#### A6. Two of this page's block headings sit 8px above their line, not 16
- **Where:** "Nine Achologists. Five Questions" and "Five Aspects of the Achology Learning Experience". The other headings on this page, and About's same Five Aspects block, measure 16.
- **Evidence:**
  - compare.json headingGaps: here 8, 16, 8, 16, 0, 16; on About 16 throughout.
  - DSRD 7 section 4.3's table gives "reading text under a section heading | 16", and section 3.3 gives 16 under the block heading.
  - testimonials.css lines 40 and 111 use `margin: 0 0 var(--sp-sm)`.
- **Fix:** Use `var(--sp-md)` on both lines.
- **Size:** Small.
- **Kain's eye:** Yes.
- **File:** testimonials.css, page-only.

#### A7. The Five Aspects lead is grey here and dark on About
- **Where:** "Watch testimonials from our past and present students..." renders #5E6B75 here and #354149 on About.
- **Evidence:** testimonials.css line 112 `color: var(--color-soft-grey)`. DSRD 7 section 1.1: "if a person reads it as sentences, it is #354149".
- **Fix:** Use `var(--color-dark)`, or fold it into the supporting line sweep (A12).
- **Size:** Small.
- **Kain's eye:** Yes.
- **File:** testimonials.css, page-only.

#### A8. Each story card shows its question twice, in two wordings, and the play badge sits on the words
- **Where:** Block 6.
  - Each poster's baked-in question ("How have you personally benefitted from studying Achology training courses?") is repeated by a visible caption in other words ("How have you benefitted from studying Achology courses?").
  - The translucent play badge sits in the middle of the baked text.
- **Evidence:** `slice-1440-03.png`, `slice-390-02.png`, `slice-768-02.png`. compare.json shows captions visible here and hidden on About.
- **Known:** about.css lines 161 to 168 hide these captions on About (Kain, S209). The comment there says "Testimonials ... is untouched until Kain rules on the reach." The badge over the words is the same on About.
- **Fix:** Wait for Kain's ruling (D3). If yes, remove `:not(.policy-page--testimonials)` from about.css line 166.
- **Size:** Small.
- **Kain's eye:** Yes.
- **File:** about.css is shared, but this selector reaches only About and Testimonials.

#### A9. The same questions are worded differently in two places, and apostrophes are mixed
- **Where:**
  - Button 02 says "benefited"; its story caption says "benefitted".
  - Button 05 says "the 5 things"; its caption says "the five things".
  - The button labels and card quotes use straight apostrophes (who's, you've, You'll); the captions, related questions and lead use curly ones.
- **Evidence:** served.html; page-testimonials.php line 155 and the tm-data block; shared-parts.php lines 1636 to 1640.
- **Fix:** A copy call (D4).
- **Size:** Small.
- **Kain's eye:** Yes.
- **File:** page-testimonials.php is page-only. shared-parts.php is shared (the captions also appear, hidden, on About).

#### A10. The dialog's text is cramped and uneven
- **Where:**
  - The italic question sits directly on the answer with no space between.
  - In a story card, the empty name and country lines leave about 18px above the question.
- **Evidence:** `lightbox-1440.png`, `story-lightbox-1440.png`. interact-1440.json shows question and answer margins of 0 and 0. `.tm-lb__q` and `.tm-lb__a` (written by testimonials.js lines 108 and 114) have no rule in any stylesheet.
- **Fix:** Add `.tm-lb__q { margin-bottom: var(--sp-sm); }` and hide the empty name and country lines. Show it to Kain together with A2.
- **Size:** Small.
- **Kain's eye:** Yes.
- **File:** testimonials.css and testimonials.js, page-only.

#### A11. The global impact block no longer links to /reviews/
- **Where:** Block 5.
  - The spec says its lead links to /reviews/, and the template comment says the phrase "all our reviews" carries the link.
  - The lead now has no link, and nothing in the page body links to /reviews/. Only the footer's "Student Reviews" does.
- **Evidence:**
  - interact-1440.json giLink is empty.
  - global-impact.php lines 138 to 153: "It carries no "our reviews" ... Testimonials shows the sentence without its link to /reviews/; named to Kain the same turn."
- **Status:** Known to Kain at S141 but never settled. Both template comments (page-testimonials.php lines 172 to 188) still describe the link.
- **Fix:** Kain's words (D2).
- **Size:** Small.
- **Kain's eye:** Yes.
- **File:** global-impact.php is shared by /reviews/ and /testimonials/; the link is drawn only on this page.

#### A12. None of the six supporting lines uses the Lead with Bar style, and they come in five styles
- **Where:** 16 dark (twice), 16 soft grey, 14 soft grey, 18 on 1.75, and 16 white. DSRD 7 section 3.3 sets 18/500/1.55 dark with a hung orange bar.
- **Evidence:** page_gate's supporting-line check fails at all three widths.
- **Status:** Known. DSRD 7 says other pages move onto it "only under the signed sweep brief".
- **Size:** Medium.
- **Kain's eye:** Yes.

#### A13. The S390 copy rulings are not on the page yet
- **Where:**
  - The lead has no DSRD 2 section 2.24 Member sentence.
  - "Achologists" in the H2 is not explained where it first appears.
  - "UK" is not spelled out where it first appears.
- **Evidence:** The record's "RULING RECORDED, Chat S390", items 1 to 3.
- **Status:** Known.
- **Size:** Small.
- **Kain's eye:** Yes.
- **File:** page-testimonials.php, page-only.

#### A14. All nine members are labelled "Senior Achologist"; Our People calls three of them Master Achologists
- **Where:** The dialog line and every portrait's alt text. Our People names Alec Wells, Andrew Nelson and Dr Jonathan Frost as Master Achologists. The name mismatch is already on the record; the level mismatch is new.
- **Evidence:** testimonials.js lines 32 and 101; shared-parts.php line 1727; people-setup.php lines 285, 296 and 340.
- **Fix:** Kain's ruling (D5), then a per-member `rank`, which achology_member_voices already supports.
- **Size:** Small.
- **Kain's eye:** Yes.
- **File:** testimonials.js and page-testimonials.php are page-only. shared-parts.php is shared.

#### A15. On a first visit the cookie banner covers the question buttons at 1440
- **Evidence:** `testimonials-1440.png`.
- **File:** Complianz, site-wide; not this page's fault.

---

### B. Behind the scenes

**B1. The hero picture is a 409 KB PNG, lazy-loaded, with no smaller copies.**
- **Where:** page-testimonials.php line 116. The file is 780 x 780, drawn at 320 on desktop and as a 12% backdrop on a phone.
- **Evidence:**
  - It is 28% of the 1,475,571 bytes the page fetches at 1440 and 41% of the 994,981 at 390.
  - page_gate's image-format, image-responsive and image-lcp-candidate checks fail at all three widths.
  - About and Reviews serve 320 and 640 WebP copies eagerly, About with fetchpriority high.
- **Fix:** Make 320 and 640 WebP copies, draw them through achology_derivative_attrs, drop `lazy` and add `fetchpriority="high"`.
- **Kain's eye:** No, if the render proof matches.
- **Status:** Waits on the FROM Chat pictures brief, item 1, so it is not done twice.

**B2. No VideoObject is emitted.**
- **Where:** page-testimonials.php lines 37 to 44 still say the rule is unwritten; spec section 7 ruling 3 (S390) wrote it.
- **Status:** Briefed (FROM Chat, structured data brief, line 10). The comment correction alone is C6.

**B3. The 45 transcripts are data, not page text.**
- **Where:** tm-data holds 24,508 bytes and 2,160 words, and nine data-transcript attributes hold another 2,751 bytes.
- **Status:** Known; record section 6, spec criterion 5.

**B4. The first question's nine quotes and transcripts are typed in two places.**
- **Where:** shared-parts.php lines 1751 to 1835, and the tm-data block on page-testimonials.php line 350. They agree today, but nothing keeps them so. Both sit in templates rather than in fields the owners can edit.
- **Status:** Waits on the field-group build (B2).

**B5. The script puts the master JPG back on the page and drops the theme version from picture addresses.**
- **Where:** testimonials.js line 9 (`asset()` adds no `?v=`) and line 32 (src set to the `.jpg`).
- **Evidence:** `stacey-q4-avatar-220.webp` was fetched twice, with and without `?v=`.
- **Fix:** Carry the version on `#tm-data` and use the `-220.webp` as src.
- **Status:** Waits; it changes requests. Page-only file.

**B6. Most members' five portraits are the same file five times, and the 45 posters are never shown.**
- **Evidence:**
  - Jon's q1, q2 and q5 portraits have the same checksum; Brian's q1 and q2 differ.
  - 131 picture requests at 1440 after pressing all five questions.
  - The poster branch (testimonials.js lines 129 to 136) runs only for a card with no Vimeo id, and none lacks one.
- **Status:** Waits.

**B7. A story card leaves the previous member's name on the dialog.**
- **Where:** testimonials.js line 119. After opening Brian Boyle's answer then a story card, a screen reader announces "Brian Boyle, member testimonial video".
- **Fix:** Always set the label.
- **Status:** Waits; behaviour change. Page-only file.

**B8. Shared stylesheets the page loads and barely uses.**
- **Evidence (coverage after pressing every question):**
  - cards.css 0% (28 KB on the wire), people.css 0% (18 KB), help.css 3% (32 KB), about.css 3% (21 KB), policies.css 4%, components.css 10% (38 KB).
  - ConvertKit's CSS and JS load with no Kit form on the page.
  - WordPress's button-block CSS and Complianz's cookieblocker CSS are 0% used.
  - 18 stylesheets, 219 KB on the wire in all.
- **Status:** A site-wide decision in functions.php lines 699 to 719. Waits.

**B9. Dead link code.**
- **Where:** page-testimonials.php lines 183 to 193 pass a `link_url`. global-impact.php lines 142 to 153 replace a phrase that no longer exists. The output is the same with or without it.
- **Status:** Waits on D2.

**B10. Hand-typed dialog values.**
- **Where:** testimonials.css line 99 (12px offsets), line 96 (a 2px margin) and line 70 (an rgba backdrop).
- **Status:** css_gate passes the file. Waits for the dialog fixes in A2 and A10.

**B11. Both `allow` and `allowfullscreen` are set on the player.**
- **Where:** testimonials.js line 127 and shared-parts.js line 43. Chrome logs a warning.
- **Status:** Untested in older Safari. Waits.

**B12. Escape cannot close the dialog while the Vimeo player has focus.**
- **Detail:** A cross-origin frame swallows the key, so modal.js never sees it.
- **Status:** Unverified by test; inherent to the player.

**B13. Member cards do not announce that they open a dialog.**
- **Where:** shared-parts.php line 1701 lacks `aria-haspopup="dialog"`; the story cards beside them have it (line 1105).
- **Status:** Shared with /accreditation/ and /cards/. Waits.

**B14. A dead selector in the button family.**
- **Where:** buttons.js line 20 lists `.tm-tabs`, which nothing renders.
- **Status:** Shared file. Waits.

**B15. The readiness record is out of date, and three page_gate failures are page_gate's own misreadings.**
- **The record:** Section 7 still reads fail on an axe contrast finding, but axe now reports zero. A run that clears the cache first is owed before any record line is written.
- **The gate's misreadings:**
  - "hairline-present boundary 4 ... no hairline". The 1px line is there at y 2905.5, 48 either side, and visible in `slice-1440-03.png`.
  - "gap-heading-line is 0". Measured 8.
  - "keyword-density: body is empty". The page's words are in the template by design.
- **Header pictures:** page_gate also fails `nlp.webp` (96 x 96 attributes on an 81 x 64 file) and `mental-health.webp` (29.2 KB in a 20 KB slot). These are site-header pictures, not this page's.

**B16. Two stale rows in DSRD 7.**
- **Detail:** Section 3.1's "Featured Testimonial Quote" describes an element deleted at S054. Section 5.3 still records the dialog at 14px; it is built and measured at 16px.

**B17. The share picture's description is "testimonials".**
- **Detail:** This is the Rank Math `og:image:alt`. The words are Chat's to write; Code sets the field.

**B18. Shared component drift seen here.**
- **Global impact:** label padding 6px is off the scale, and white text is used at six strengths where DSRD 7 now names three. Reaches /reviews/ too.
- **Card quote:** `.lite-quote` is 16 italic on 1.55 (components.css line 1256), and no DSRD 7 row names it.
- **Gateway flagship picture:** `course-001.webp` is 704 x 370, drawn 291 x 308, so it is under-resolved on a 2x screen.
- **Duplicate id:** `cmplz-manage-consent` (Complianz, every page).

---

### C. Invisible tidy-ups safe to ship now

**Page-only proof:**
- testimonials.css is enqueued only by `is_page( 'testimonials' )` (functions.php lines 933 to 935).
- testimonials.js is enqueued only by the same test (lines 1057 to 1059).
- page-testimonials.php is the template for that slug alone.
- A grep of every php, js, css and py file in the theme (previews excluded) finds no other loader.

**Computed-style proof for C1 to C3:**
- `c_proof.py` removed the rules from the stylesheet in a headless copy of the page only, through the browser's own style tools; nothing on the server changed.
- It compared every element's full computed style and box at 1440, 1100, 1040, 1039, 1024, 768, 767 and 390, after a control pass with no edit.
- **Result:** 1,062 elements. The control pass showed 0 differences, and so did the edit, at all eight widths (identical hashes; c-proof.json).

**C1. Delete the dead `tm-panel` rule.**
- **Where:** testimonials.css line 60, `.tm-panel[hidden] { display: none; }`.
- **Why invisible:** No element has class `tm-panel` in served.html, page-testimonials.php or testimonials.js.

**C2. Delete the dead `about-grid` rule.**
- **Where:** testimonials.css line 110, the `@media (min-width: 1040px) { .about-grid {...} }` line.
- **Why invisible:** Only achology_routes_grid() draws `.about-grid`; this page calls achology_site_gateway() (line 226), and served.html has no `about-grid`.

**C3. Delete the copy of the shared rule.**
- **Where:** testimonials.css line 119, and the second selector in the phone query on lines 120 to 123.
- **Replacement:**
  ```
  @media (max-width: 767px) {
    .tm-about-proof { margin-top: var(--sp-xl); padding-top: var(--sp-xl); }
  }
  ```
- **Why invisible:** components.css lines 1159 to 1169 declare the same selector with the same values at both tiers. No stylesheet loaded in between overrides it, checked by grepping every `policy-body--ruled` rule in the theme.

**C4. Correct the stale comments in testimonials.css.**
- **Lines 19 to 21:** Remove "`tm-panel`" so the list reads "`tm-filter` and `tm-tab` (the question navigator)".
- **Lines 71 to 84:** Replace from "THE LIGHTBOX IS THE LIVE PART OF THIS FILE" through "...the panel lift is close to" with:
  ```
  /* THE LIGHTBOX. The panel takes --radius-panel (16px), the stage-panel tier
     of DSRD 7 section 5.3; the 14px recorded there at S223 is no longer what
     is built (measured 16px, 11 November 2026). The other three values below
     are genuine one-offs with no token behind them: the panel lift is close to
  ```
  Then keep lines 85 to 89 unchanged.
- **Why invisible:** CSS comments render nothing.

**C5. Drop a fallback nothing sets.**
- **Where:** testimonials.js line 8.
- **Replacement:** `var URI = (dataEl.getAttribute('data-uri') || '').replace(/\/$/, '');`
- **Why invisible:** The template always prints `data-uri` (line 350, present in served.html), and nothing in the theme defines `TM_URI`.

**C6. Correct the stale schema comment.**
- **Where:** page-testimonials.php lines 37 to 44, from "WHAT IS DELIBERATELY NOT EMITTED" through "...the real page the row was waiting for."
- **Replacement:**
  ```
   * NOT YET EMITTED: VideoObject. The row this comment once waited for is
   * written: the signed spec, section 7 ruling 3 (Chat, S390), sets one
   * VideoObject per filmed answer from an editable field group, the About
   * page's method. It is briefed as Backlog: Code line 10 and is not built.
  ```
- **Why invisible:** A PHP comment is never sent to the browser.

**C7. Fix one indentation slip.**
- **Where:** page-testimonials.php line 214, `'lightbox' => false,`, which has one tab too many.
- **Why invisible:** Whitespace inside a PHP array changes nothing that runs or is sent.

---

### D. Questions for the main session

1. **Vimeo (A3).** May the forty answers have achologytest.com added to their embed lists with tools/vimeo_embed_whitelist.py? The tool's header records Kain's authority for the fourteen only.
2. **The link to /reviews/ (A11).** Should a linked phrase return to Kain's S141 sentence? If not, the spec row, the template comments and the dead argument should be corrected.
3. **Story captions (A8).** Does Kain's S209 ruling to hide the captions on About reach this page?
4. **Wording (A9).** "Benefited" or "benefitted", "5" or "five", and curly apostrophes throughout: is this Chat's call or Kain's?
5. **Levels and a name (A14).** Are all nine "Senior Achologist", or are three "Master Achologist" as on Our People? And is "Stacy Anderson" right, given every one of her files is named `stacey-...`?
6. **Last-line standard.** The brief counts last lines of one, two or three words; No Lone Words and DSRD 7 section 4.1 forbid only a single word. Which standard governs this page?
7. **DSRD 7 rows (B16).** Should Chat retire the "Featured Testimonial Quote" row and correct the dialog radius from 14px to 16px?
8. **Phone type sizes.** Nothing on this page gets smaller below 768: the H1 is 33 at 390, as on About and Reviews. DSRD 7 section 4.1 gives 28 below 639, and the S189 phone rule steps every size down one below 768, with no exception for this family. Is this family an exception, or does it owe the step?
9. **Related Questions type.** These rows (and About's) set the question at 16 and the answer at 14. DSRD 7's Question List row sets 18 and 16 for "every list of questions with a one-line answer". Does that reach `help-popular`?
10. **The question navigator's look (A1).** Should the fire frame sit on rows that keep their own hairlines, or stand alone with no lines? Either needs Kain's eye on the page.
11. **The close of the page.** About now closes on the learning block (Kain, S209); this page still closes on the enquiries panel, as its spec signs. Is the difference intended?
12. **The footer name.** The footer links to this page as "Testimonial Videos"; the breadcrumb, title and spec say "Member Testimonials". Is that intended?

---

## Audit: the Student Reviews page, /reviews/

Built page: https://achologytest.com/reviews/ on the build site. Measured 11 November 2026 at theme 0.708.024 (the served HTML's `?ver=`). A later run read 0.708.025 after another session shipped; no reviews file changed between the two. Nothing in the theme or the project was changed.

**Read first:**
- SPEC__Reviews_Page_S053.md, DSRD6_RECORD.md and GATE__DSRD6_Reviews_Page_S053.md
- DSRD 6 sections 2 to 12; DSRD 7 sections 1, 3, 4, 5.3 and 5.5; DSRD 8 section 14; DSRD 9 section 29
- every line of page-reviews.php, reviews.css, reviews.js and reviews-setup.php
- the parts of functions.php, shared-parts.php, global-impact.css, buttons.css and buttons.js, help.css, components.css and no-lone-words.js this page touches

**How it was measured:**
- full-page pictures with shot.py
- page_gate.py with --no-purge, and css_gate.py on reviews.css
- my own Playwright scripts (installed Chrome) reading computed styles, boxes, last lines, contrast, images and network at 1440, 768 and 390
- every control exercised by mouse and keyboard, plus one load with scripting off
- four single read-only requests to the site's REST routes
- about a dozen page loads in all

**Files.** All are in `/private/tmp/claude-501/-Users-kainramsay-Documents-CLAUDE---Anthropic-Ai/03c15077-a23a-4ce8-b05f-acb45926942f/scratchpad/reviews/`, and paths below are relative to it.
- Full-page pictures: `reviews-1440.png`, `reviews-768.png`, `reviews-390.png` (2x).
- Viewable slices at 1x: `seg/w1440-00.png` to `seg/w390-08.png`.
- States: `states/` (dropdowns open, filtered view, empty view, translation, no scripting, focus rings, the hero at 390 on About, Testimonials and Reviews).
- Data: `served.html`, `page_gate_output.txt`, `measure_1440_768_390.json`, `interact.json`, `compare.json`, `final.json`, `probe.json`.
- Scripts: `measure.py`, `measure.js`, `interact.py`, `compare.py`, `final.py`, `probe.py`, `texts.py`.

**Where the page is right, measured:**
- **Spacing and type.**
  - Hairlines measure 48 above and 48 below at desktop and tablet, and 32 and 32 on a phone, at every boundary.
  - Header to content is 48, 48 and 32.
  - There is one h1, at Como 33/700. Gutters are 48, 32 and 20.
- **Overflow.** Nothing runs past the screen edge at any width; the only element outside is the off-screen skip link.
- **Accessibility.** axe 4.10.2 reads zero WCAG 2.2 AA violations. Every text colour clears AA; the lowest is 4.55:1, white on the action-orange buttons.
- **The review wall.** The masonry has zero overlaps and every gap is 24. None of the first 31 cards moves when "Show more reviews" adds 32 more.
- **Landing.** "Read the Reviews" lands the archive heading 8px under the sticky header. A search, a course or a chart row lands on the archive, not the page top.
- **Dropdowns.** They work by mouse, arrow keys, Home, End, Enter, Escape, Tab and typed letters, and close on an outside click.
- **Translation.** It opens and closes, and the wall re-lays without overlap.
- **No scripting.** The page still works: native selects, a plain two-across grid and real "Show more" links.
- **Order.** The default order is striped exactly as the spec says; the first twelve read 5, 5, 4, 5, 4.5, 5, 5, 5, 3, 3.5, 5, 4.
- **Structured data.** Both JSON-LD blocks parse, and the breadcrumb matches the visible trail word for word.
- **Typing.** The served review texts already carry the DSRD 9 section 29.6 decision 4 typing pass. All 32 start with a capital; 31 end on a full stop or other mark, and the last ends on an emoji.

**Known and recorded, not re-raised:**
- "FREE" and the Ten Ways gateway line (named exceptions, S145).
- The "A Global Learning Movement" wording (DSRD 7 section 3.3 exception).
- The 960 column (DSRD 9 section 29.1).
- Links to the six unbuilt school pages.
- The speed line, carried as a site-wide exception (S141).
- No Review or AggregateRating schema, by design.
- 4.66 against the archive's own 4.62 (the reason is written in page-reviews.php).
- The standout reviews were removed; the Theme filter and card titles wait on the tagging pass.
- The screen-reader read, run once before launch (S484).

The S141 independent walk of the page listed fourteen items. Six are now fixed:
- a search lands on the archive
- Show more exists
- the country panel has no overflow at 390 (375 was not measured)
- the hero copy
- the header search
- the videos moved to /testimonials/

Six are still open, now with measurements: A1, A6, A7, A12, A13 and A15.

---

### A. What a visitor sees

Ordered most visible first. "Page-only" means a file proved to serve /reviews/ alone (proof in C). "Shared" names every page the file reaches.

**A1. On tablet and phone, reviewer names are cut to a few letters on almost every card.**
- **Where:** the card's name, date and stars row: `.rv-card__name` (reviews.css 896 to 905), on one row with Verified, the date and the stars (862 to 888).
- **Evidence:**
  - Names cut with an ellipsis: 0 of 31 cards at 1440, **28 of 32 at 768 and 27 of 32 at 390** (`measure_1440_768_390.json`, cards.truncatedNames).
  - At 768: "Deni…", "Suza…", "Rone…", "Ade…" (`seg/w768-01.png`). At 390: "Denise…", "Yusuf …", "Suzan…" (`seg/w390-01.png`). Even "Thomas" and "Zach O." are cut.
  - Kain's S053 one-row ruling and the S141 960 column were judged on a card about 468 wide. The card is 340 wide at 768 and 350 at 390.
  - This is the S141 walk's hindrance 6, fixed only at desktop.
- **Fix:** where the row cannot fit (cards under about 440 wide), let it break: the name alone on the first line, with Verified, the date and the stars beneath. That is the S258 two-line arrangement DSRD 8 section 14.2 records. Another option is the stars on their own line. Render two or three options at 768 and 390 for Kain.
- **Size:** medium. **Kain's eye:** yes. **File:** reviews.css, page-only.

**A2. On tablet and phone, every course name in the card footer is cut after one line.**
- **Where:** `.rv-card__course-line`, the two-line limit that counts "This review is from a student of" and the course name together (reviews.css 1062 to 1071).
- **Evidence:**
  - Text is cut on **0 cards at 1440, 32 of 32 at 768 and 32 of 32 at 390**: "Diploma Course in Modern Applied…", "Counselling Skills Practitioner Course…" (`seg/w768-01.png`, `seg/w390-01.png`).
  - The prefix was lengthened at S053 against a two-line budget of 590px on the 428px card. On a 340px card the prefix fills the first line by itself.
- **Fix:** give Kain options, since he ruled the footer never runs to three lines:
  - the prefix on its own line, with the name limited to two lines beneath it, on narrow cards
  - the 52px artwork dropped on narrow cards, which returns 64px
  - a shorter prefix on narrow cards, in his words
- **Size:** small to medium. **Kain's eye:** yes. **File:** reviews.css, page-only.

**A3. On a phone, the Course list runs off the left edge of the screen.**
- **Where:** `.ach-select__panel` (reviews.css 486 to 517) and the flip in reviews.js `open()` (190 to 194).
- **Evidence:**
  - At 390 the list is 380 wide on a 318-wide box. It flips to align right and starts at **x = -26**.
  - Every course loses its first letters: "ll courses", "iploma Course", "Beginner's Guide" (`states/course-dropdown-open-390.png`; `interact.json` m_course_open).
  - A visitor cannot scroll left to reach the cut text.
- **Fix:** cap the list at the screen width with `max-width: min(380px, calc(100vw - 2 * var(--sp-lg)))`. In `open()`, flip right only if the flipped list fits; otherwise keep it left and let the width cap do the work.
- **Size:** small. **Kain's eye:** yes. **Files:** reviews.css and reviews.js, page-only.

**A4. The ratings chart shows whole-archive counts whatever the search or course, so a row can promise reviews that are not there.**
- **Where:** `achology_review_rating_chart()` in reviews-setup.php 552 to 604. The counts are queried by rating only (559 to 575), while each row's link keeps the current search and course (583 to 590).
- **Evidence:**
  - With the course set to "Mindset Mastery", the page reads "Showing 3 of 3 reviews" while the chart still reads 2,897 / 541 / 621 / 223 / 234 (`states/course-filter-1440.png`).
  - Clicking "3 stars, 234 reviews" then shows "No reviews match that search yet" (`interact.json` chart_3stars_with_course).
  - A search for "coach" (327 results) shows the same whole-archive chart.
- **Fix:** one of two, Kain's choice.
  - (a) Count within the current course and search. Keep caching the unfiltered and per-course counts as now, and count a keyword view live within the S103 limits.
  - (b) Keep whole-archive counts, but make each chart row start a fresh view (drop course and search from its link), and say so in the chart's title.
- **Size:** medium. **Kain's eye:** yes; this changes how a block he signed at S141 behaves.
- **File:** reviews-setup.php. Its display code serves /reviews/ alone, but the file loads on every request, so treat it as shared for shipping.

**A5. Lines end on one word, and this page is not switched on for the lone-word fix About uses.**
- **Where:** no-lone-words.js lists only the founder pages and About (lines 12 to 16). `main.policy-page--reviews` is not in it.
- **Evidence (after scripts run, `measure_1440_768_390.json` lone):**
  - **One word alone on the last line:**
    - the gateway line "offers" at **all three widths** (About, carrying the same locked gateway, shows "Achology offers"; `compare.json`)
    - the h1 "Reviews" at 390
    - "Movement" (map block heading) at 390
    - "Experience" (FAQs heading) at 390
    - "Globe" (map block line) at 768
  - **Two or three words alone:**
    - "Reviews Archive" and "Across 216 Countries" at 390
    - "Experience Achology" (gateway title) at all widths
    - "for you." (hero lead) at 390
    - "experience with Achology." (archive lead) at 768 and 390
    - "countries, total." at 390
    - the FAQ answers' last lines at 768 and 390
  - **Review texts, reported once:** 16 of 31 or 32 end on a line of one to three words at every width. They are students' own words and are left alone.
- **Fix:** add one entry to PAGES in no-lone-words.js:
  `{ page: 'main.policy-page--reviews', lines: '.policy-title, .policy-lead, .gi-intro__title, .gi-intro__lead, .gi__heading, .gi__lead, .gi__honest, .rv-archive__title, .rv-archive__lead, .gateway__lead, .gateway__name, .gateway__desc, .help-close__heading' }`
  - That clears every one-word case.
  - The two- and three-word cases need DSRD 7 section 4.1's line standard (fold at about two thirds), which no page in this family carries yet (D16).
- **Size:** small. **Kain's eye:** yes. **File:** no-lone-words.js, shared. It loads on every page, but an entry acts only on the page it names, so only /reviews/ would change.

**A6. A chosen course is cut mid-letter in its box, with no ellipsis.**
- **Where:** `.ach-select__value` is `display: flex` (reviews.css 428 to 435), and an ellipsis cannot draw on a flex box.
- **Evidence:**
  - "Mindset Mastery: The Ulti" at 1440 (`states/course-filter-1440.png`).
  - The box is 228 wide at 1440 and about 146 at 768, so most course names are cut.
  - The S141 walk's cosmetic item 10 ("All rati…" at 1024) is the same control.
- **Fix:** draw text values into an inner span with `overflow: hidden; text-overflow: ellipsis; white-space: nowrap` (reviews.js `paint()`, 89 to 95), keeping flex for the star rows.
- **Size:** small. **Kain's eye:** yes. **Files:** reviews.css and reviews.js, page-only.

**A7. Anonymous reviews show the name "Verified S.", next to the word Verified.**
- **Where:** `achology_review_display_name()` (reviews-setup.php 226 to 268) shortens every two-word name to first name plus initial. That includes the stand-in DSRD 2 section 2.24 itself prescribes, "Verified Student".
- **Evidence:**
  - The tenth card reads "Verified S. Verified February 2026" (names list from `texts.py`).
  - The export holds **84 rows** with "Verified Student" (`grep -c -i "verified student" data/reviews.csv.php`).
  - This is the S141 walk's cosmetic item 12; its cause is now found.
- **Fix:** return "Verified Student" unchanged when the name is that stand-in (or already "Verified S."). Then correct the stored `reviewer_name` on the 84 posts, by a re-run of the loader's reset or a one-off update over WP-CLI.
- **Size:** small. **Kain's eye:** yes, though it only restores the documented wording. **File:** reviews-setup.php (shared for shipping, as A4).

**A8. A search of fewer than three letters, or more than sixty characters, is thrown away without a word.**
- **Where:** `achology_review_filters()` blanks any search under 3 or over 60 characters (reviews-setup.php 350 to 358). The search box (page-reviews.php 391) has no `minlength` or `maxlength`.
- **Evidence:**
  - `?rv_q=ok` shows "Showing 31 of 4,516 reviews", the box comes back empty, and there is no Clear link. A 61-character search does the same (`interact.json` short_q, long_q).
  - The visitor's word simply vanishes. "AI", "UK" and "OK" are real searches.
- **Fix:** add `minlength="3" maxlength="60"` to the box so the browser explains before sending. When a too-short word does arrive, keep it in the box with one line saying searches need three letters (Kain's words).
- **Size:** small. **Kain's eye:** yes (a new line of copy). **Files:** page-reviews.php (page-only) and reviews-setup.php.

**A9. The archive heading is one size larger than the page's other block headings, and its lead line is grey where the map block's is dark.**
- **Where:** `.rv-archive__title` is Como 28/600 and `.rv-archive__lead` is soft grey 16/400 (reviews.css 88 to 103).
- **Evidence:**
  - The map block's heading, the gateway heading and the FAQs heading are all Como 24/600. The archive heading is 28 at every width (`measure_1440_768_390.json` type).
  - DSRD 7 section 3.1: "H2 Section | 24px | 600 | 1.25", and "it is the one heading size".
  - The page gate fails it (heading 28, wants 24), and fails all three lines under the block headings against DSRD 7 section 3.3's "Lead with Bar" (`page_gate_output.txt` lines 70 to 122).
  - The stylesheet records "28 and a soft-grey lead since S141, as on the archive render Kain approved". So this is a look Kain ruled at S141 meeting a later standard. DSRD 7 section 3.3 says every page moves onto the shared heading component under the signed sweep brief.
- **Fix:** carry it in the block heading sweep: the archive heading to 24, and the archive and map lead lines onto the shared `lead-bar` component.
- **Size:** medium (rides the sweep). **Kain's eye:** yes. **Files:** reviews.css (page-only) and global-impact.css (shared: /reviews/, /testimonials/).

**A10. Near the top of the archive, the words start on three different lines.**
- **Where:** the search panel `.rv-bar` (reviews.css 147 to 158, 265 to 269) and the map panel `.gi` (global-impact.css).
- **Evidence at 1440 (`interact.json` fields):**
  - The heading, lead, count and cards start at x 240.
  - The search box and Course box edges start at 232; their labels and the hint start at 248.
  - The map panel's words start at 256.
  - DSRD 7 section 4.4 says a panel bleeds 32 "with matching 32px inner padding, so content inside the panel returns to exactly" the column. `.rv-bar` pads 24, putting its content 8 outside the column; `.gi` pads 48, putting it 16 inside.
  - DSRD 7 section 4.4a (one text line per page) is site-wide, and its sweep "runs only on a signed brief naming its pages". The S141 comment says the bar's spacing was chosen from four variants.
- **Fix:** in the section 4.4a sweep, set the bar's padding to `var(--sp-xl)`, which puts the labels' words at 256 with the map's, or set the map to 32. Decide on the rendered page.
- **Size:** small to medium. **Kain's eye:** yes. **Files:** reviews.css (page-only) and global-impact.css (shared: /reviews/, /testimonials/).

**A11. The map block's markers pulse for ever, with no way to stop them.**
- **Where:** `.gi__pulse::before`, `animation: gi-pulse 2.2s ease-out infinite`, on five markers (global-impact.css 584 to 589). The computer's reduced-motion setting stills them (594 to 596).
- **Evidence:**
  - `document.getAnimations()` lists five gi-pulse animations that never stop (`final.json` animations).
  - DSRD 6 section 7.1 names "the Global Impact pulses" under WCAG 2.2.2: they must stop within five seconds or offer a pause. Its words: a finding here goes to Kain "rendered, with options".
- **Fix:** options for Kain: pulse three times and then rest; pulse only for a few seconds while the map is in view; or add a small pause control.
- **Size:** small. **Kain's eye:** yes. **File:** global-impact.css, shared: /reviews/, /testimonials/.

**A12. The translation button says "Show original" while the original never hides.**
- **Where:** reviews.js 627 to 628 (`OPEN = 'Show original'`).
- **Evidence:** opened on a Spanish review, the original stays and the translation appears beneath it, while the button reads "Show original" (`states/translate-open-1440.png`). This is the S141 walk's cosmetic item 11, still open.
- **Fix:** a label that says what the next click does, for example "Hide translation" (Kain's words).
- **Size:** small. **Kain's eye:** yes. **File:** reviews.js, page-only.

**A13. The empty result is one grey line, worded for a search even when there was none, with no full stop.**
- **Where:** page-reviews.php 452 to 458.
- **Evidence:**
  - "No reviews match that search yet" appears under a course plus "3 stars" view with no search at all (`interact.json` chart_3stars_with_course, `states/empty-state-1440.png`).
  - Nothing else fills the space; "Clear filters" sits up in the bar.
  - No search word is highlighted in results either (`interact.json` search_coach: mark 0).
  - This is the S141 walk's cosmetic item 14, still open.
- **Fix:** Kain's words for a sentence that fits searches and filters alike, ending in a full stop, with "Clear filters" repeated beside it.
- **Size:** small. **Kain's eye:** yes. **File:** page-reviews.php, page-only.

**A14. The search fields are 44 tall where the site's field standard now says 46.**
- **Where:** `.rv-bar__input, .rv-bar__select` and `.rv-bar__go` at 44px (reviews.css 321 to 332, 358 to 363), and `.ach-select__trigger` at 44px (416).
- **Evidence:**
  - Measured 44 at 1440 (`interact.json` fields).
  - DSRD 7 section 5.5: "Height | 46px, level with the main button beside it (Kain, S208 pick 16; was 44px)", and "Submit | the §5.1 main button at the field height, 46px".
  - The bar's labels are Mulish 14/600 dark (Kain's S141 C3), while section 5.5 still lists Como 12/600 uppercase soft grey (D6).
- **Fix:** move the fields, the dropdown boxes and the Search button to 46 once D6 is answered.
- **Size:** small. **Kain's eye:** yes. **File:** reviews.css, page-only.

**A15. The browser tab title and the band disagree: "Verified Ratings" and "Verified Reviews".**
- **Where:** the Rank Math title "Achology Student Reviews: 4,516 Verified Ratings" (`page_gate_output.txt` line 55), against the band's "4,516 Verified Reviews".
- **Evidence:** as above. This is the S141 walk's cosmetic item 13, still open.
- **Fix:** change one word in the title, over WP-CLI, in Chat's or Kain's wording.
- **Size:** small. **Kain's eye:** yes (it is a word). **File:** none (a Rank Math field).

**A16. The links in the registration line use the action orange at 12px.**
- **Where:** `a.bf-in` and links in body text take `--color-orange-action` #C85015 (buttons.css 168 to 177). On this page that is the two numbers in the UK Register of Learning Providers (UKRLP) line under the FAQs card.
- **Evidence:**
  - Measured #C85015 on white, 12px, 4.55:1 (`measure_1440_768_390.json` lowContrast). It passes AA on white by only 0.05.
  - DSRD 7 section 1: the action orange is "for controls on a white ground and never for text".
  - DSRD 7 section 5.5's closing paragraph: a link in body text "rests in the AA orange #B8460F".
- **Fix:** one token in buttons.css, if the documents are right (D17).
- **Size:** small. **Kain's eye:** yes. **File:** buttons.css, shared: every page with a link in body text.

**A17. Site-wide, seen on this page (for the record; not this page's to fix).**
- On a first visit the keyboard is held inside the cookie banner: 60 presses of Tab cycled its three buttons and never reached the page (`interact.json` tab_stops).
- On a phone the cookie banner covers the Course list (`states/course-dropdown-open-390.png`).
- The footer's last row reads "How We Write  Cookie settings" with no dot between the two (`seg/w1440-05.png`).
- Files: Complianz and footer.php; every page.

---

### B. Behind the scenes

Ordered by effect on visitors and on the site, highest first.

**B1. Every review is listed publicly at /wp-json/wp/v2/review.**
- **Where:** `register_post_type( 'review', ... 'show_in_rest' => true ... 'public' => false ... )`, reviews-setup.php 88 to 95.
- **Evidence:**
  - A request with no login returns 200 with `X-WP-Total: 4516`, and each review's shortened name, course number and date, for example "Kylei R., course 001" (`probe.json`).
  - The review text is not exposed (its field group has `show_in_rest: 0` and the type has no editor).
  - `public => false` does not hide it.
  - The listing sits outside the S103 limits on the page's own search: it can be paged 100 at a time, with no cache.
- **Fix:** close the route to visitors. Either set `'show_in_rest' => false`, which makes the edit screen fall back to the classic editor (check that in the admin first), or add a `rest_endpoints` filter that drops `/wp/v2/review` for anyone who cannot edit posts. See D13.
- **Size:** small. **Kain's eye:** no. **File:** reviews-setup.php (loaded on every request).

**B2. With scripting off, the later batch pages state the wrong count; their canonical address is unverified.**
- **Where:** page-reviews.php 335 to 338 and 452 to 458.
- **Evidence:**
  - With scripting off, `?rv_p=2` shows "Showing 64 of 4,516 reviews" over 32 cards (cards 33 to 64) (`interact.json` nojs).
  - Filtered addresses carry empty parameters (`?rv_q=coach&rv_c=&rv_r=`), so one view has many spellings.
  - The canonical address on `?rv_p=N` cannot be read on the hidden build site; Rank Math withholds it there. If at launch it points every batch at /reviews/, search engines discount batches 2 onwards. That works against DSRD 6 section 6's "whole archive reachable without scripting".
- **Fix:**
  - When `rv_p > 1`, print "Showing reviews 33 to 64 of 4,516" (Kain's words).
  - Drop empty parameters, by switching empty fields off before sending or by a server redirect.
  - Add the canonical on batch pages to the launch check list.
- **Size:** small. **Kain's eye:** only for the count wording. **File:** page-reviews.php, page-only.

**B3. The page's WebPage schema has no description, though the description now exists.**
- **Where:** page-reviews.php 67 to 90. The comment says the description and dates are left out because "this page's metadata is not written yet ... Both land together."
- **Evidence:**
  - The Rank Math description is now written (144 characters; `page_gate_output.txt` line 56).
  - The served WebPage entry carries name, url, isPartOf and about only (`final.json` jsonld).
  - Both blocks parse. There is no Review or AggregateRating entry, as designed.
- **Fix:** read the Rank Math description into `description`, as page-about.php does, and add `dateModified`.
- **Size:** small. **Kain's eye:** no. **File:** page-reviews.php, page-only.

**B4. help.css is printed twice on this page.**
- **Where:**
  - `achology_enqueue_component_style()` (shared-parts.php 71 to 82) checks only its own handle, `achology-component-help`.
  - help.css is already loaded on every page as `achology-help` (functions.php 715).
  - `achology_faq_block()` calls it (shared-parts.php 1237).
- **Evidence:**
  - There are two `<link>` tags for the same help.css: one in the head, one before the footer (`served.html`).
  - The browser fetches it once (same address), but reads and applies its 295 rules twice, the second time after reviews.css and buttons.css.
  - Removing the second copy in the browser changed **0 of 2,568 elements** on 26 measured style properties (`final.json` help_double), so the fix is safe here.
- **Fix:** return early when `wp_style_is( 'achology-' . $slug, 'enqueued' )` or `'done'`.
- **Size:** small. **Kain's eye:** no.
- **File:** shared-parts.php, shared by every page with the FAQs block: /reviews/, the courses directory (template-courses.php), /certification/, /accreditation/, /enquiries/ (enquiries.php), the Help archive (archive-faq_article.php), and the other shared-parts.php callers.

**B5. The HTML and each batch of reviews are heavy with repeated drawings.**
- **Where:**
  - `achology_review_stars()` (reviews-setup.php 634 to 651) prints the full star drawing five or six times per card.
  - The Rating options carry five star rows in `data-ach-stars` (page-reviews.php 427).
  - Each card also prints its quote mark and arrow drawings.
- **Evidence:**
  - The served HTML is 303,258 bytes for 32 cards. It holds 303 inline drawings totalling 135,121 bytes; one star drawing is about 590 bytes.
  - The five `data-ach-stars` attributes are 19,968 bytes (`final.json`).
  - Each "Show more" returns 190,080 bytes for 32 cards, with no cache header (`probe.json`).
  - Compressed transfer size was not measured.
- **Fix:**
  - Put one hidden SVG `<symbol>` per glyph in the page, and use `<use href="#…">` in each card (the load-more batches reuse the page's symbols). Or draw the star as a CSS mask.
  - Add a short cache header to the load-more route, for example 15 minutes, matching the existing server cache.
- **Size:** medium. **Kain's eye:** no (a picture comparison proves it). **File:** reviews-setup.php (its display code serves /reviews/ alone).

**B6. The small course pictures fetch a file four times too big on high-density screens.**
- **Where:** the card footer image, `achology_derivative_attrs( ..., 704, array( 104, 360, 540 ), '80px' )` (reviews-setup.php 857).
- **Evidence:**
  - At 1440 on a standard screen, each card loads `course-NNN-104.webp` (about 4.3 KB).
  - At 390 on a 2x screen, each loads `course-NNN-360.webp` (22 to 26 KB) for a picture drawn 80px wide (`final.json` net_390x2).
  - The page's pictures total 502,002 bytes at 390 on 2x, against 280,224 at 1440 on 1x.
  - The gate also fails `image-dimensions` on all 32: the attributes say 52 by 42, while the file's shape is about 1.9 to 1.
- **Fix:**
  - Add a 208-wide copy to the list (2x of the 104 drawing).
  - Set the width and height attributes to the file's own shape; CSS keeps the 52 by 42 box.
  - This sits inside the open BRIEF__Pictures_Sized_For_Every_Screen_Across_The_Theme job.
- **Size:** small. **Kain's eye:** no. **File:** reviews-setup.php, plus new image files.

**B7. The map loads late although it is in the first screen on desktop and tablet.**
- **Where:** `world-dots.svg` (113,014 bytes decoded) in global-impact.php.
- **Evidence:** the page gate fails `image-lcp-candidate` at desktop and tablet (the map loads lazily, with no high-priority flag) and on mobile (the hero art has no high-priority flag) (`page_gate_output.txt` lines 168 to 174).
- **Fix:** load the map immediately (`loading="eager"`) on these two pages, where the block sits under the hero; mark the hero art `fetchpriority="high"`.
- **Size:** small. **Kain's eye:** no. **Files:** global-impact.php (shared: /reviews/, /testimonials/) and page-reviews.php.

**B8. Most of the stylesheet weight on this page does nothing here.**
- **Evidence (`final.json` usage, net_1440).** There are 18 stylesheet links, 788,190 bytes decoded. Rules whose selector matches anything on the page at rest:

  | Stylesheet | Rules used | Note |
  |---|---|---|
  | cards.css | 0 of 275 | |
  | people.css | 0 of 124 | |
  | ConvertKit frontend.css | 0 of 72 | plus its 7,333-byte script, with no Kit form on the page |
  | about.css | 21 of 263 | loaded for the hero button and portrait header |
  | help.css | 55 of 295 | loaded twice (B4) |
  | policies.css | 26 of 207 | |
  | components.css | 59 of 278 | |
  | reviews.css | 99 of 114 | see below |

  - The other 15 rules in reviews.css are for states this audit exercised (open list, chosen value, Clear filters, translation, chosen chart row), plus the dormant `.rv-card__title`. So no dead rule is proved in reviews.css.
  - The gateway's flagship art pulls the 704-wide original `course-001.webp` (66,386 bytes) into a box about 290 wide (components.css 1125).
  - Method: each selector was tested on the page at rest, so a rule used only in a state can be counted unused.
- **Fix:** these are the numbers for the site-wide speed fix that the record's section 9 exception carries. For this page, the hero rules about.css lends could move to components.css, so /reviews/ can drop about.css.
- **Size:** large (site-wide). **Kain's eye:** no. **File:** functions.php (every page).

**B9. The fields' rounded pill shape and focus frame arrive only with JavaScript.**
- **Where:** base.css sets `--radius-input: 10px` (line 286). buttons.js adds `.bf-field` at runtime (218 to 234), which draws the pill and the orange focus frame.
- **Evidence:** with scripting off, the bar's fields have 10px corners (`states/nojs-archive-1440.png`). DSRD 7 section 5.3 says inputs are "pill, 999px".
- **Fix:** set `--radius-input` to the pill in base.css, so the no-script look matches; buttons.js keeps the frame.
- **Size:** small. **Kain's eye:** no (nothing changes with scripting on). **File:** base.css, every page.

**B10. The page's readiness record and the gate disagree with the page's real state.**
- **Evidence:**
  - The page gate today: 58 passed, 38 failed, 5 for review, 1 not built, 19 carved out (`page_gate_output.txt`).
  - The record's table still shows section 1, 2 and 7 machine fails from 30 September and 1 October, and section 11 "not run". Yet its own closing lines say section 7 reads zero (true today) and that Kain's eye is the section 11 verification.
  - New since the record: section 1 now also finds "FAQs" (the FAQs heading) and "CPD" (an FAQ answer) used before being spelled out. Neither is covered by a recorded exception.
  - The gate's `spacing-scale` fails count six locked card values from DSRD 8 section 14 (20, 10, 3, the 10/24 footer padding, 12) and the hero buttons' annotated 26.
  - `keyword-density` and `orphan` are limits of the gate itself: the editor body is empty by design, and the crawl missed 913 pages.
- **Fix:** a fresh sweep of the record by Code, never a hand edit. "FAQs" and "CPD" go to Chat for a spelling-out or an exception (D7, D18).
- **Size:** small. **Kain's eye:** no. **File:** DSRD6_RECORD.md (written by the gate tool).

**B11. Comments in shared files that now say the wrong thing.**
- functions.php 173 to 178 says the /testimonials/ page and the social proof components query the review type. Only page-reviews.php and the loader call any review function (grep across the theme).
- functions.php 182 to 185 says the loader "never publishes: every row lands as a draft"; reviews-import.php line 10 says "EVERYTHING LANDS PUBLISHED".
- reviews-setup.php 9 to 17 says the type serves course proof on all 28 course pages and /testimonials/. The course pages take their reviews from their own data; course-parts.php has no review query.
  - So the brief's guess that reviews-setup.php serves the course and pricing pages is not borne out. Its display code serves /reviews/ and its load-more route alone.
  - The file still loads on every request, for the content type, the load-more route and the import screen.
- **Fix:** correct the comments when those files are next open.
- **Size:** small. **Kain's eye:** no. **Files:** functions.php (every page) and reviews-setup.php. Waits, because both are shared.

---

### C. Invisible tidy-ups safe to ship now

**Proof that the three files are this page's alone:**
- WordPress picks page-reviews.php for the slug "reviews", and nothing includes it: grep for `page-reviews` across the theme's php, js and py finds only comments.
- reviews.css and reviews.js are loaded only under `is_page( 'reviews' )` (functions.php 942 to 945). No other file loads them; grep for `reviews.css`, `reviews.js` and `achology-reviews` finds only comments elsewhere.
- Every class and id reviews.css styles (`rv-*`, `ach-select*`, `reviews-header*`, `policy-page--reviews`) is printed only by page-reviews.php, by reviews-setup.php's card code (called only by page-reviews.php and its load-more route), and by reviews.js.
- buttons.js names `.ach-select__trigger` and `.ach-select__native` as fields to frame; no edit below touches them.
- components.css 1145 styles `.policy-page--reviews`; no edit below touches it.
- None of the three files was in the working tree's changes at session start.

**Shipping note.** Every item is a comment, a merge that leaves the styling result identical, or a selector that finds the same single element.
- Ship them with the theme's version bump.
- Run css_gate.py on reviews.css (it passes today).
- Prove with a before-and-after comparison of computed styles at 1440, 768 and 390; zero differences are expected.

**C1. reviews.js line 695: a selector half of which matches nothing.**
- Old: `	var grid = document.querySelector( '[data-reviews-grid], .rv-grid' );`
- New: `	var grid = document.querySelector( '[data-rv-grid]' );`
- **Why invisible:** the page prints exactly one grid, `<div class="rv-grid" data-rv-grid>` (page-reviews.php 469). `data-reviews-grid` exists nowhere in the theme. Both forms return the same element, and line 346 already uses `[data-rv-grid]`.

**C2. reviews.js lines 620 to 622: the batch size in a comment.**
- Old:
  ` * Delegated from the document, because the load-more button adds cards in` /
  ` * batches of 50 and a listener bound per card would miss every batch after the` /
  ` * first.`
- New:
  ` * Delegated from the document, because the load-more button adds cards in` /
  ` * batches of 32 (ACHOLOGY_REVIEW_PER_PAGE in reviews-setup.php) and a listener` /
  ` * bound per card would miss every batch after the first.`
- **Why invisible:** it is a comment.

**C3. reviews.css: fold the two S145 overrides into the rules they override.**
- Lines 186 to 191, old: `.rv-dist {` / `  grid-area: dist;` / `  display: flex;` / `  flex-direction: column;` / `  gap: 6px; /* one-off, Kain S141: the chart's row rhythm as approved */` / `}`
- New: the same rule, with its fifth line as `  gap: 0; /* S145: the rows meet; each row is 24 tall, see below */`
- Lines 202 to 212 (`.rv-dist__row { ... text-decoration: none; }`): add one line before the closing brace: `  min-height: 24px; /* S145, WCAG 2.2 2.5.8 */`
- Lines 220 to 226, delete: `.rv-dist__row {` / `  min-height: 24px;` / `}` / (blank) / `.rv-dist {` / `  gap: 0;` / `}`
- Keep the S145 comment at 214 to 219; it still describes the values.
- **Why invisible:**
  - The selectors, specificity and file are the same. The later declarations win today, and the earlier rule now carries the same values.
  - No other rule anywhere sets `gap` on `.rv-dist` or `min-height` on `.rv-dist__row`. Grep across the theme's CSS finds `.rv-dist` rules only at reviews.css 181 to 238 and 1345 to 1353, which set padding, colour, outline and transforms.

**C4. reviews.css lines 1356 and 1357: a comment with no rule under it.**
- Delete: `/* The UKRLP line under it, as on the courses page (courses-directory.css,` / `   Kain S138): 24 under the card, centred, the shield in brand orange. */` and the blank line after it.
- **Why invisible:** it is a comment. The UKRLP line is styled by help.css (`.cd-credit`), not here.

**C5. reviews.css lines 14 to 16: the file's state line.**
- Old:
  `   STATE: hero, the global impact component, and the archive (S053). Still to` /
  `   come: the standout reviews, which sit between the two, and the where-next` /
  `   panel. Nothing here should be read as a decision about those.`
- New:
  `   STATE: complete. Kain removed the standout reviews from this page (S053),` /
  `   and the where-next panel became the Ten Ways gateway and the questions` /
  `   block (S053, S142); DSRD 9 section 29.4 holds the order.`
- **Why invisible:** it sits inside the opening comment.

**C6. reviews.css lines 109 to 111: draft markers that no longer exist.**
- Old:
  `   The draft lines carry data-rv-draft in the markup instead. That attribute is` /
  `   a marker for us, not a style: it is how the page can be swept for copy nobody` /
  `   has approved yet, and it comes off each line as Kain settles it. */`
- New:
  `   The draft lines carried data-rv-draft until Kain supplied every line (S053,` /
  `   S141); no marker remains on the page. */`
- **Why invisible:** it is a comment. `data-rv-draft` appears in no printed markup; grep finds it only in a page-reviews.php comment.

**C7. reviews.css: three comments that still say three across.**
- Lines 640 to 642, old:
  `   PLAN section 7: "three across at desktop, two at tablet, one at phone, 24px` /
  `   gap". The gap is --sp-lg, which IS 24px, so the value is named rather than` /
  `   typed.`
- New:
  `   PLAN section 7 said "three across at desktop, two at tablet, one at phone,` /
  `   24px gap"; Kain ruled two across at S053 (below). The gap is --sp-lg, which` /
  `   IS 24px, so the value is named rather than typed.`
- Lines 666 and 667, old:
  `   scripting, or before the script runs, the cards render as the ordinary` /
  `   three-across grid below and the page is never broken, only less pretty. */`
- New:
  `   scripting, or before the script runs, the cards render as the ordinary` /
  `   two-across grid below (one column under 600px) and the page is never` /
  `   broken, only less pretty. */`
- Lines 685 and 686, old:
  `   is placed in it. The column WIDTH is still worked out from the same three` /
  `   columns and the same 24px gap, read off this stylesheet at run time, so the`
- New: the same two lines, with `three` replaced by `two`.
- **Why invisible:** they are comments.

**C8. reviews.css lines 877 to 880 and 886: a comment that contradicts its own rule.**
- Old (877 to 880):
  `   Centred rather than baseline-aligned, and that stays deliberate now the stars` /
  `   sit outside this group: the star row is five SVGs in an inline-flex box, and` /
  `   a box like that has no text baseline of its own, so browsers fall back to its` /
  `   bottom edge and the stars sit low. Centring is the alignment that holds.`
- New:
  `   Baseline-aligned, as DSRD 8 section 14.2 item 4 records (Kain, S053): the` /
  `   name, Verified and the date are three pieces of text, and only the baseline` /
  `   puts their letters on one line. The stars sit outside this group and take` /
  `   their own measured drop at .rv-stars.`
- Line 886, old: `  gap: 10px; /* one-off: name to country, as built on the page Kain approved; annotated S140, no value changed */`
- Line 886, new: `  gap: 10px; /* one-off: name, Verified and date, as built on the page Kain approved; annotated S140, no value changed */`
- **Why invisible:** they are comments. The rule beneath already reads `align-items: baseline`, and the value stays 10px with its "one-off" note intact for css_gate.

**C9. page-reviews.php: four comments written before the page was built.** Indentation as in the file.
- Lines 7 and 8, old:
  ` * As of this commit that page does not exist yet, so this template is reachable` /
  ` * only through the preview until he makes it.`
- New: ` * The page exists and is published on the build site.`
- Lines 18 to 20, old:
  ` * STATE: frame and hero only. Blocks 4 through 7 of the plan (the global impact` /
  ` * component, the standout reviews, the archive, and the where-next panel) are` /
  ` * not built. Do not read the absence of a block here as a decision about it.`
- New:
  ` * STATE: complete. The order is DSRD 9 section 29.4's: hero, global impact,` /
  ` * archive, the Ten Ways gateway and the questions block. Kain removed the` /
  ` * standout reviews at S053.`
- Lines 219 to 223 (four tabs, then ` * `), old:
  `The archive block does not exist yet, so #reviews-archive is` /
  `not on the page and this button does nothing when clicked.` /
  `reviews.js guards on the target existing, so it stays inert` /
  `rather than erroring, and starts working the moment the` /
  `archive block lands. ArrowDown is registered at DSRD 7 §5.2.`
- New:
  `The archive is below, at #reviews-archive; reviews.js scrolls` /
  `to it and still guards on the target existing. ArrowDown is` /
  `registered at DSRD 7 §5.2.`
- Lines 272 to 279 (three tabs, then ` * `), old: the paragraph beginning `COPY STILL OWED. The plan leaves the narrative to be settled with` and ending `plan's own wording.`
- New:
  `THE COPY is Kain's (S053, S141) and lives with the block in` /
  `global-impact.php, where the figures and the framing line are` /
  `recorded.`
- **Why invisible:** PHP comments never reach the browser.

---

### D. Questions for the main session

**D1.** Narrow cards (A1, A2): which arrangement for the name row and the course footer when a card is under about 440px wide? Kain's S053 rulings were made on a card 428 to 468px wide.

**D2.** The ratings chart (A4): should its counts follow the current course and search, or should a chart row start a fresh view?

**D3.** The schema maps disagree.
- DSRD 3 line 248 reads "Reviews, Testimonials, ... | WebPage | Rank Math auto | None needed".
- DSRD 10 line 306 reads "Reviews, Testimonials | WebPage + BreadcrumbList | Theme JSON-LD", and is still marked not built.
- The page follows DSRD 10: the theme writes the schema, and Rank Math emits none here.
- DSRD 6 section 4 says "DSRD 3 holds the full map".
- Which one governs, and who corrects the other?

**D4.** page-reviews.php 58 to 65 gives three reasons for emitting no Review schema for each review. Reason 3 was that the 28 course pages did not exist.
- The gate's link check now resolves all 76 links it checked; its only planned 404s are six school pages. So the course pages exist.
- The template's own note says that once they do, the honest position is a Review entry for each review, with the course as `itemReviewed`, and still no AggregateRating.
- Does the page now take them? No search rich result is available either way.

**D5.** The course artwork's corner radius.
- DSRD 8 section 14.4 says 8px.
- DSRD 7 section 5.3 (Kain, S113) says every picture takes `--radius-card`.
- The build has drawn 12px since theme 0.388.0 (commit 40498ac2, "the eleven stray corners move onto the four standard sizes"), and reviews.css 1048 to 1051 still says 8.
- Confirm that 12 stands, so DSRD 8 section 14.4 and that comment can be corrected.

**D6.** DSRD 7 section 5.5 lists the field label as "Como 12px/600 uppercase 0.08em, soft grey", and fields at 46px. The bar carries Kain's S141 plain labels (Mulish 14/600, brand dark) and 44px fields. Does section 5.5 take the S141 labels, and does the bar move to 46 (A14)?

**D7.** The page gate's spacing check fails six locked card values from DSRD 8 section 14, and the hero buttons' annotated 26 (B10). Record them as named exceptions, or teach the gate the locked card's values?

**D8.** DSRD 7 section 3.0's phone rule (S189) says text steps down one size below 768.
- On /reviews/ at 390, the h1 stays 33, the archive heading 28 and the card text 16; only the FAQs block steps down.
- css_gate.py passes reviews.css.
- Is the rule meant only for sizes a page declares for phones, or should this page step down?

**D9.** reviews.css 1229 to 1231 marks the translation control's look "NOT RULED BY KAIN YET ... Every value below is Code's proposal for that sitting". Was it ruled? And what are Kain's words for the button's label when the translation is open (A12)?

**D10.** About's hero lead line is 21px from 768 up (DSRD 7 section 3.2, the Lead Paragraph row, About only). Reviews and Testimonials share the same hero layout at 18px (`compare.json`). Is that intended?

**D11.** SPEC__Reviews_Page_S053.md is stale on many points, where the page has since moved on by Kain's rulings:
- the map block's heading and lead copy
- the figure labels, and 4,517 against 4,516
- batch 50 against 32
- field type 15px, and the labels
- block 8 as the enquiries panel
- its approved HTML predates S141 and S142

DSRD 9 section 29.4 carries the S141 and S142 changes. Should the spec be refreshed, or DSRD 9 section 29.4 marked as the current record?

**D12.** DSRD 8 section 14.5 still says "50 per batch"; DSRD 9 section 29.4 and the code say 32.

**D13.** /wp-json/wp/v2/review (B1): close it to visitors, or accept it because every name on it is already on the page?

**D14.** At launch, should the batch pages (`?rv_p=N`) carry their own canonical address (B2)?

**D15.** If wanted, Kain's words for three lines: the three-letter search message (A8), the empty-result line (A13), and a batch page's count (B2).

**D16.** Which line rule governs this page?
- The brief's rule: no last line of one, two or three words.
- DSRD 7 section 4.1's line standard: titles never end on one word alone; descriptions never end on one word, and their last line is never under 40 per cent of the longest.
- no-lone-words.js only prevents the single word.

**D17.** DSRD 7 section 5.5 says links in body text rest in #B8460F. buttons.css 169 draws them, and `a.bf-in`, in the action orange #C85015, which DSRD 7 section 1 keeps for filled controls. Which is right (A16; site-wide)?

**D18.** The FAQs block brought "FAQs" and "CPD" onto the page before either is spelled out (B10). Spell them out where they first appear, or record exceptions?

---

OWED BACK: Chat's rulings on the four points in section 2.3 and on each page's list D, and the order in which the visible items go to Kain.

*No em or en dashes in this file; checked before writing.*

> CHAT DISPOSITION, S466: answered by RULING__About_Testimonials_Reviews_Audit_Answered_S466 in FROM Chat.
