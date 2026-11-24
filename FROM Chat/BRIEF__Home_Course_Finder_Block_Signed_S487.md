For Code: what this needs: build the Home page's course finder (Find the Right Course or Learning Path for You), exactly as its signed mock-up, in the Gateway's place in Kain's S567 Home order (hero, Who Is Achology?, Voices, then the finder, then free events, the films, the Knowledge Hub belt, questions, close), from the theme's own data, and compare the build against the mock-up at 1440, 1024 and 375 before Kain looks. Answer with a DONE.

Done when: the block stands in the Gateway's place with no measured difference from the mock-up at 1440, 1024 and 375; every choice, quick start and payment tab behaves as in the mock-up; all 39 products open their own pages; and your DONE answers the five questions at the foot.

**DOCUMENT TYPE:** brief from Chat (Session 487, 24 November 2026). **Card:** #98 (Homepage: Sign And Build The Front Page). **Kain's word:** "Yes, sign it", on the whole block in his side panel, after shaping it over the sitting. His words, item by item, are in DSRD 9 section 45.28. **This replaces the Academy grid** Kain briefed you on in S567 ("Gateway Into the Academy", DSRD 9 45.27): the grid was drawn and turned down; the finder stands in the Gateway's place. The mock-up shows it straight under the road block only because it was drawn on the S486 preview; your order of S567 is the one to follow.

**Read first.** DSRD 9 section 45.28 (what is signed). DSRD 4 sections 1.1 to 1.4 and 2 (prices, plans, the three routes). DSRD 5 sections 1 to 4 (courses, bundles, hours, students, stars). pricing-block.php and pricing-block.css (the payment tabs, .pb-seg, and the stored #pr-data plans the finder reads). DSRD 7 sections 3.0 and 4 (type and the spacing scale). DSRD 8 section 7 (the course card's figures, for comparison only).

**The spec is the mock-up.** Folder "Home Course Finder Block 24 November 2026" in FROM Chat:
- home-finder-signed.html: your Home preview with the road, this block, the proof block and the Knowledge Hub block in place. The signed view is section #home-finder-5 (classes cf cf5 cfE); the page opens on it.
- finder-block.css: the block's rules. The signed block uses the shared .cf and .cfb rules, .cfE, and everything in the second half (Session 487's three asks, the spacing, Chat's last five). The .cf1 to .cf4, .cfA to .cfD and .ag rules are earlier rounds: ignore them.
- finder-block.js: the engine (choices, matching, nearest fit, sorting, the list, the tabs, quick starts, hairlines). Everything is in one IIFE; the option 2 and 4 parts are unused.
- finder-data.js: the 39 products with every field the block reads (built by finder_data.py from courses-setup.php, DSRD 4, DSRD 5 and the plans below). Do not ship this file typed: see item 2.
- plans-from-pr-data.json: the 36 products' payment plans, read from the course pages' stored #pr-data, the same figures the Pricing page reads.
- Home Course Finder Plan 24 November 2026.html: the plan in words Kain checked (subjects per course, depth, length bands, routes).
- data.py, plan.py, finder_data.py, build3.py, build4.py, build6.py: how the mock-up was made.

**What to build.**
1. **Heading and line, Kain's own words, word for word:** "Find the Right Course or Learning Path for You" and "Select as many options as you like to find relevant courses, schools and learning plans, each with a direct link to explore further." Both balanced when they wrap. The site's last-lines script set the line to plain wrap at 1024 (one long row, then four words); the mock-up forces text-wrap-style: balance. Make the script give the same two near-equal rows, as DSRD 7's last-lines rule 3 asks, rather than an !important.
2. **One home for the data.** The finder's products are drawn from the theme's own homes at build: courses-setup.php (names, slugs, hours, stars, students), the stored #pr-data plans (every monthly figure, never worked out: DSRD 4 section 1.1), DSRD 4's membership prices, and the Session 487 facets (subjects per course, routes, depth, the Diploma in both Practitioner and Master Level). Put the facets in one data file in the theme, owner-editable if you can (the build stance, section 9 of the Project Instructions); the mock-up's finder-data.js is the reference for every value.
3. **The bar:** one white bar in six equal parts, Subject, What You Want, Depth, Time, Price, School, each showing its name and current choice; its text on the page's text line, its rounded ends 32 outside (16 on a phone); two columns of three on a phone; labels never wrap at tablet width. Each part opens its choices beneath the bar; one open at a time; a click outside closes it. Choices: Subject, What You Want, Depth and School take several; Time and Price take one; Price also takes "Up to $__ a Month".
4. **The list:** the count line ("All 39 courses, schools and plans" before any choice; "5 fit your choices" and a Clear all link after); the Pay In Full and Pay Monthly tabs at its right, in the Pricing page's own .pb-seg look; six results, Show all for the rest; nothing chosen opens on the Diploma, the pass, monthly membership, then the courses most taken; if nothing fits every choice, the nearest are shown and the dropped choice is named.
5. **Each result, the formula** (Kain: "There needs to be a formula"): line 1 what it is (depth and Course; School Bundle and its number of courses; Membership; the pass's fire badge "Full Academy Curriculum"); line 2 the name; line 3 always stars | students | hours of on-demand teaching | membership included, leaving out only what does not apply, short hairlines between, and no hairline at a line's start or end. Courses 3 Months Membership; bundles, the pass and the Diploma with membership 12 Months Membership. The pass is named "The Achology Access All Areas Pass" on this block. A 3px line of the school's colour beside each result, just outside the text line; the pass and membership in Achology's orange.
6. **Prices:** Pay In Full: the price, then the Pricing page's row line ("Or Five Monthly Payments of $59.80"). Pay Monthly: "From $59.80 a Month", then "Pay over 3 or 5 months". Monthly membership "$7 First Month", "Then $34.50 a month" in both views; annual "$345 a Year", "Paid once".
7. **Quick starts,** a quiet line of text links under the bar: Not sure where to start? Try New to all of this | I want to help others | Looking after my mental health | Short courses | Under $100. On a phone, one line that slides sideways and fades at its edge.
8. **Spacing, on the scale:** 8 between each of the three lines, the name at 1.3, 24 above and below each result, 4 between the price's two lines.
9. **Keyboard and screen readers:** every choice a button with aria-pressed; the tabs as tabs; the list's count in a polite live region; focus outlines in the action orange; reduced motion respected. Run axe on the built block.
10. **Two figures to bring into line:** the pass's students. The finder shows 695,578 (DSRD 5's locked unique count); the stored #pr-data pn.all reads 872,284, which counts each course's students apart. Report which pages print 872,284 and change none without Chat's word. And confirm 600+ hours is the pass's figure everywhere.

**The five questions for your DONE.**
1. Where did you put the finder's data, and can Kain or Karen edit a course's subjects without touching code?
2. Did the last-lines script balance the line at 1024, and how?
3. What does axe report on the block?
4. Which pages print 872,284 for the pass, and which 695,578?
5. Any measured difference from the mock-up, at any width, and why.

**Not in this brief:** a version of the finder on the Courses page and the Pricing page (Kain wants one later; it is on Chat's backlog and will come as its own brief).

*No em or en dashes in this file; checked before writing.*
