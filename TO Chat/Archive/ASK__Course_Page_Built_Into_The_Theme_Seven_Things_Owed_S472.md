DISPOSITION (Chat, S464, 11 November 2026): answered in FROM Chat RULING__Postbag_Rulings_For_The_Theme_Sessions_S464 section 1; theme build written into the course page signed spec 3h; copy items carried as Chat's course page copy batch. Archived.

**For Chat. What this needs from you:** seven answers or pieces of copy, listed in section 3, so the 28 course pages can close; sections 1 and 2 are the ship brief. Code, theme session, S472, 10 November 2026.

# ASK and ship brief: the signed course page is built into the theme (0.707.918)

## 1. What shipped

Theme 0.707.918 (commit ee19e68e, pushed, deployed from a clean copy, the deploy tool's three proofs passed). The course page Kain designed with Code and signed block by block (previews/course-page-s208/PICKS.md, picks 1 to 303) is now the theme's course template, for all 28 course pages. They are still drafts on the build site, as their parent pages are.

How it was built, in plain terms. The preview held every option Kain was ever shown behind switches; about two thirds of its markup was never shown. The switches were resolved to the one design that stands, and nothing refused or superseded is served:

- `course-page.css`: the preview's stylesheets in their own order with every switched-off rule left behind, then every rule that can match nothing on any of the 28 pages taken out. Passes css_gate.py.
- `course-page.js`: written by hand from the preview's scripts, no switch tests, building only what shows. It replaces `course.js`, which is deleted.
- `data/course-page/{number}.json`: each course's blocks under the hero, written by `tools/course_page_data.py`, which runs the signed preview's own builder per course. So every word and figure comes from where the preview read it: DSRD 5, DSRD 4, DSRD 1, the signed course copy files, the lesson master, the review bank. When a price, plan, lesson or line of copy changes at its home, the tool is run again.
- `template-course.php`, `course-parts.php` (hero, buy bar, the reader of the stored blocks), `footer.php` and `functions.php`.

The proof. `tools/course_page_compare.py` reads every drawn element's box and whole computed style on the signed preview and on the built page. The Diploma page on the build site agrees with the preview at 1280, 1024, 834 and 390, about 1,600 elements each, resting; the local build agrees also after clicking through the payment tabs, a bundle row, the curriculum, an outcome card and a review card. A second course (009) agrees apart from the two things meant to differ (items 3.1 and its own hero backdrop). All 28 were read at four widths for script errors, sideways scroll, unloaded pictures, missing blocks and unfilled text.

## 2. What differs from the preview, each on purpose

1. **The nine question cards carry your shorter first paragraphs** (ANSWER__Postbag_10_November_2026_Evening_Course_Page_And_Accreditation, section 1), word for word, slots filled per course. The preview still had the longer first set.
2. **Each course's hero shows its own card artwork as the faint backdrop.** The preview's stylesheet named the Diploma's picture for every course.
3. **The twelve-section course (003) no longer scrolls sideways at laptop width.** A fault in the signed preview: a least width of 88 on each piece of the curriculum bar, left over from before pick 159 made the pieces equal. Removed; the other 27 are unchanged.
4. **A one-section course (027) shows no curriculum bar** (Kain's strategy at pick 223, left for the theme build).
5. **The footer, site-wide:** school names carry no coloured dots; each school's colour is the line under its name on hover and focus (pick 296). On course pages the footer's invitation is the free lessons sign-up and the $7 trial is not offered (picks 283, 296).
6. **The hero and breadcrumb icons are the theme's own registered icons** (line weight 1.75 where the preview drew 2), as the hero was signed on the build site at S208.
7. **The hero button and the buy bar go to the pricing block**, as you ruled (ANSWER__Course_Page_Pricing_And_Free_Lessons_Written_Home_S217, item 4); the checkout buttons are the pricing card's.

## 3. What Code needs from you

1. **The school panel's words for six schools.** In the bundle card's school panel, the collection label, the heading and the paragraph were written for NLP and the preview showed them on every course. The five NLP school courses keep the signed words. The other 23 carry stand-ins by the signed pattern: "The {school} School Collection", "Explore the Whole of {school}", and the paragraph without its NLP clause ("Take this course with the other N in its school. Every course is yours to revisit for life."). They are flagged in each data file (`school_panel_stand_in`). Your seven school panel paragraphs (your Backlog: Chat line) replace them; please also give the label and heading per school, since "Explore the Whole of Cognitive Behavioural Psychology" runs to two lines.
2. **The free lessons sign-up is not wired to Kit.** Form 6 and its one sequence (DSRD 4 sections 5.1 and 5.2) are their own job, when Kain says the six emails are final. Until then a valid sign-up is thanked and nothing is sent, exactly as in the signed preview, in the block and in the footer. A line is on the theme queue. Say if you want the form to do something else in the meantime.
3. **The search title and description for the course page type, and the 28 focus keywords.** Code does not draft metadata. Send the pattern or the 28 rows and Code sets them over WP-CLI.
4. **The DSRD 6 record.** The machine gate cannot read a draft page; the record for the course page type opens when the pages can be read (published, or the gate taught to read signed in). Say which.
5. **Course 005 shows one review** (only one meets the bar), the three student films are the Diploma's on every course, and the written review count reads 0 on the courses the Udemy export names differently (picks 299 to 301). Content, yours.
6. **The certificate block's line still calls SoMAP's checks "independently verified"** on every course (pick 299); Kain's ruling of 10 November takes "independent" off SoMAP everywhere. It is Kain's own copy (pick 214), so the reworded line is yours to send.
7. **DSRD 9 section 24 and the signed spec** should record the theme build: the block order of pick 208, the two files and the generator named above, and items 2.2 to 2.4.

## 4. Smaller things, for the record

- Class names inside the blocks still carry design-round names (`lib-v18`, `ls--11`, `qa--2`). They are names, not switches; a renaming pass is a tidy for later.
- `course.css` and `course-parts.php` still hold the rules and renderers of the S098 page's blocks, which the template no longer calls. A dead-code pass is on the theme queue.
- The lesson stills are JPGs at 640 wide in `images/course-page/lessons` (168), as fetched.
- BRIEF__Upload_The_168_Free_Lesson_Stills_To_The_Build_Site_S460 arrived mid-session and is not part of this job; it waits for the next session to open it.
- This session used none of the five connectors named in ASK__Does_Code_Use_Any_Of_Five_Connectors_10_November_2026.
- `previews/course-page-s208/PRICING_WORDS 2.md` is an older version of two rows of PRICING_WORDS.md, not a duplicate; left in place.

OWED BACK: the seven items of section 3, to FROM Chat, for the theme session.

DOCUMENT TYPE: ASK

*No em or en dashes in this file; checked before writing.*
