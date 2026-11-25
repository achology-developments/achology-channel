For Chat: what this needs: once Kain has said yes to it in Code's S576 theme session, sign it into FROM Chat unchanged as BRIEF__Sweep_Each_Page_Loads_Only_Its_Own_Stylesheets_S576 so Rule 3's route is met. It asks Chat for no words and no ruling.

Done when: every page family on achology.com loads only the styling it uses, every page looks exactly as it did (proved by picture comparison), and phone Performance on Home is re-measured and written into its record.

# SWEEP BRIEF (draft for Kain's yes): each page loads only what it needs

Code, S576, theme session, Opus, 25 November 2026. Theme 0.708.491 on achology.com.

## 1. Why

Lighthouse on Home, 25 November: phone Performance 47 (first paint 5.3 s, largest paint 11.2 s), computer 67. Its leads: render-blocking styling about 3.7 s, unused styling 458 KiB, unminified styling 315 KiB (REPORT__Day_After_Checks_S575, item 6).

Measured by Code tonight on the live Home page: it loads 33 theme stylesheets holding about 9,800 rules. About 1,500 of those rules touch anything on the page. Nine files touch nothing at all: cards, people, kh-front, checkout-foot, course, gift-banner, warm-room, pricing-block, reading-line. The largest, course-page.css (188 KB), has 155 of its 1,333 rules in use.

The cause is in the theme: home-setup.php and about-setup.php pull in other pages' stylesheets whole so they can borrow a few of their blocks, and functions.php loads policies, help and people on every page of the site.

## 2. What changes, and what does not

Changes: only which styling each page is sent, and how it is packed.
1. A page is sent only the stylesheets it uses: the shared ones (fonts, base, components, buttons, header, footer, style) plus its own, plus any file whose blocks it borrows.
2. Each page family then gets one packed stylesheet, made by a script from the theme's own files: only the rules that page family can use, minified, in one request. The theme's own stylesheets stay the canonical, edited files; the packed ones are generated from them and never edited by hand.
3. Rules that only apply in a state (menu open, an answer opened, hover, focus, the cookie banner, a form's error and thank-you messages, a film playing) are kept by a written keep-list, so nothing that only appears on a click is lost.

Does not change: no colour, size, space, word, block or picture on any page. A page that looks one pixel different at the end is a fault, mended before it ships.

## 3. The pages it covers

Every page family on achology.com: Home; About; Academy; Membership; Certification; Accreditation; the courses directory; the 28 course pages; the 7 school pages; Events; the gift page; the pricing and checkout pages; the Access All Areas Pass page; the founder pages (Code of Ethics, Code of Character and Conduct and their sisters); the centre page; free teachings and the six-day lessons; Help, its subjects and its answers; the policy pages; the people and instructor profile pages; the Knowledge Hub front, subject and tag pages; the articles, book notes, quote pages, workbooks and author pages; the 404 page.

## 4. How each page is proved

For every family, before and after, at 1440 wide and 375 wide (the phone):
1. A full-page picture before and after, compared pixel by pixel by script; any difference is a fault.
2. The click states in section 2.3 opened and compared the same way.
3. The stylesheet count and total styling weight, before and after.
4. Lighthouse phone and computer on Home and on one page of each large family, before and after, written into each page's DSRD 6 record chapter 9.
5. page_gate.py run over the whole site map after; no row may go from pass to fail.

## 5. What is derived from what is being replaced (Rule 3)

- The previews folder: previews are made from the current theme CSS, so the preview maker must read the theme's own files, not the packed ones. Checked.
- The gate tools (css_gate, page_gate, achology_word_check) that read stylesheets or their handles. Checked, and pointed at the canonical files.
- Every place that names a stylesheet handle as a dependency (six-day-lessons.php, free-teachings.php, the setup files). Listed and kept whole.
- Caching: SiteGround's dynamic cache and Memcached purged after each ship; the theme version bumped on each ship.
- The working copy achology.zip rebuilt after each push.

## 6. Order of work

1. Measure every family as it is now (the before set).
2. Step 1 of section 2 (send only what is used), family by family, proved, shipped.
3. Step 2 (one packed file per family), family by family, proved, shipped.
4. Re-measure every page, write the records, one DONE into TO Chat naming this brief.

Each ship is announced with its version and gets its ship brief into the channel. Nothing ships unproved.

*No em or en dashes in this file; checked before writing.*
