NEEDS: Code to set the certificate picture at three quarters of the column on phones, on the 28 course pages and the Academy page (29 pages), by one rule in course-page.css, then gate and read back. Nothing changes on tablet or computer.

# SWEEP BRIEF: the certificate picture at three quarters of the column on phones, 29 pages

**From:** Chat, 19 November 2026. **To:** Code. **Signed:** Kain, in Code's S538 theme session, 19 November 2026. He asked: "on mobile, I'm going to ask if you could make the certificate image probably 100% bigger, or maybe 75% bigger, but apply this everywhere on the website where a certificate image is this size ... It's just very, very small, even mobile." Code showed it at the column's full width and Kain answered: "Not full, Claude. 75%." Code then showed it at three quarters of the column (251 wide on a 375 phone, against 200 now) and asked, "Shall the certificate be three quarters wide on all 29 pages?" Kain answered **"Yes, all 29 pages"**. This is the signed sweep brief Harness Rule 3 needs, the record of his word.

## The pages, exactly 29

1. The 28 course pages, each at /academy/{school}/{course}/.
2. The Academy page, /academy/.

Each draws the How Every Course Works and About the Certificate block (`.d-cert`), whose picture is `.ct-pic`. They all take the one rule below, so none is edited by hand.

**Not in this sweep:** the Certification page. It draws its certificates in pairs and as thumbnails, a different job. Any other page that draws a certificate in another block or at another size is also left alone; if Code finds one that uses `.ct-pic` in the same way, it names it in the SHIP and does not change it without a word from Chat.

## The change

- **File:** `course-page.css` in the theme. The phone rule (max-width 767.98px) that now reads `.ct-pic { ... max-width: 200px; ... }` becomes `max-width: 75%` of the column. Every other property on that line stays: the grid placement, `justify-self: center` and the `margin-bottom`.
- **Tablet and computer stay as they are:** the tablet rule at 280px and the base rule at 360px are not touched.
- **Check the width, not the rule:** on a 375 wide phone the picture should measure about 251px, which is three quarters of the column. Measure it in the browser on at least one course page and on the Academy page, and at 320 and 414 wide too.
- **Bump the stylesheet version** (a CSS change without a version bump is not shipped).
- No wording, no other block and no other breakpoint changes. The sheen and tilt effects, the shadow and the rise animation stay as they are.

**What it derives, named before it runs (Harness Rule 3).** Only the stylesheet and its version. No stored data, record, transcript or caption is derived from it, so nothing is rebuilt.

## Done when

On the build site, at phone width, the certificate picture on all 29 pages measures three quarters of its column (about 251px at 375 wide), still centred, with no overflow and no overlap with the words below it. At tablet and computer widths the picture measures what it did before. The Certification page is unchanged. The DSRD 6 gate is re-read on the Academy page and on a sample of course pages (one from each school at least) with no new fail, and the count of pages measured is given.

## OWED BACK

One SHIP naming the version bumped, the width measured at each phone width on the pages checked, a statement that the 29 pages all take the one rule, the gate's result after, and any page refused with its reason.

*No em or en dashes in this file; checked before writing.*
