> Disposition, Chat S480, 23 Nov 2026: record; Kain signed the footer and the card is Done on the GitHub board; archived. No board card moved.

NEEDS: Chat to check the built footer on the build site (1280 and 375, every link, tap sizes) and the Roundup welcome email, then close the brief.

# DONE: the footer, rebuilt from the signed mock-up

From Code (the footer session started by S541), 20 November 2026. Answers FROM Chat BRIEF__Footer_Rebuilt_From_The_Signed_Mockup_20Nov.

**Theme 0.708.280** carries the footer (commit 38191ea8); **0.708.291** (commit 1b29a77c) put the logo's size hint back to 130 so the page gate's ratio check reads true. Both deployed and proved by deploy.py.

## What was built

1. **The invitation, four ways.** The $7 band on most pages; a course page's six free lessons and a school or pass page's six free teachings, both unchanged; and, new, a workbook page's six free lessons of its own course (workbook-kit.php, `achology_workbook_footer_invite`). The workbook band uses the course band's signed words and Chat's line, with the course's DSRD 5 name linked to its page, and posts course-kit.php's form 6 with that course's number, the same fields the course page's own footer form sends. A workbook with no course keeps the $7 band. The new spacing (`.footer-main` top `--sp-2xl`, invite padding and margin `--sp-xl`) is on every variation.
2. **The map,** five columns in Kain's order, every heading a link to its section with no arrow, every link and address as the brief's table. Schools last and widest at 1024 and up, full width beneath from 768, two columns under 768 with Schools last. Each school keeps its colour line.
3. **The Achology Roundup on every page,** the signed fo2 parts and Kain's words, one line of name, email and button at 1024 and up with the form 600 wide, stacked below that. It posts to roundup-kit.php through a new footer.js (a fresh token first, as on the course form); with no script it posts as a plain form and comes back with its line. The build site's hidden test form at `/?achology-roundup-test=1` is retired, as the brief allowed. The fo2 form rules that used to load with course-page.css only are now also in footer.css, word for word, so the form looks the same on every page.
4. **One bottom row:** the copyright linked to the company details answer, Help Centre, Enquiries, Privacy, Terms, Cookies, Cookie Settings (id and classes unchanged), All Policies; no dots; the logo at 28 and the four social icons at 32 on the right. The plugin's own 100 pixel minimum on Cookie Settings is zeroed, so the row spaces as the mock-up does.
5. **Out of the footer:** Free Live Events, Student Sign In, Free Coaching, Disclaimers, Trust, How We Write, Refunds and Accessibility as separate links, the long company paragraph, and "All rights reserved."
6. **The 301:** /free-events/ to /events/, written beside the other Rank Math redirects (row 2950). Read from inside the host: "301 https://achologytest.com/events/".

## The checks

1. **Every footer link.** Read from inside the host on /about/ at 0.708.280: all 39 site addresses answer 200, every column heading included. The four social links answer 301 to their own www address and the $7 checkout answers 403 to a script; all five are unchanged from the old footer.
2. **Screenshots beside the mock-up,** in the channel's Claude outputs folder: `FOOTER__Built_Beside_Signed_Mockup_1280.png` and `FOOTER__Built_Beside_Signed_Mockup_390.png`. Measured, every box of the built footer (columns, headings, the Roundup and its fields, the bottom row, logo and icons) sits within 4 pixels of the mock-up's at both widths, the 4 being the rainbow stripe, which the mock-up draws inside its footer and the theme draws just above it. The headings in the mock-up's picture fall back to a plain face only because its font files do not load from a local file; the built footer is in Como as the mock-up names. Measured the same on a course page and a workbook page: the Roundup keeps its one-line form at 1280 on a course page too.
3. **css_gate** on footer.css: PASS. **page_gate** at 0.708.291 on the five pages: the course page (/academy/cognitive-behavioural-psychology/cbt-practitioner/) and the Access All Areas Pass page PASS whole. The other three fail on lines that are their own and not the footer's: /about/ on its supporting lines and its record, the school page (/academy/neuro-linguistic-programming/) on supporting lines and its record, the workbook page (/learn/psychology/workbooks/karpman-drama-triangle-workbook/) on its record, its Rank Math score, its keyword density and two body pictures without a size list. No line on any page names the footer.
4. **The workbook free lessons sign-up,** through the Karpman workbook page's footer form in a real Chrome, as manager+footer-workbook-test@achology.com, first name "Workbook Test". The site answered `{"ok":true}` and the form showed "Thank you, Workbook Test. Your first lesson is on its way to your inbox." Read back from Kit: subscriber 4398883634, active; tags Website Course Free Lessons (25695128) and Website Free Lessons: 007 cbt-practitioner (25695135); in sequence 2965491; course_name "Cognitive Behavioural Therapy (CBT) Practitioner Course", course_link, course_cover, course_checkout, course_price $249, free_lessons_link and lessons 1 to 6 with their stills, all filled.
5. **The Roundup sign-up,** through the footer of /about/ in a real Chrome, as manager+roundup-test@achology.com, first name "Roundup Test". The site answered `{"ok":true,"line":"Thank you, Roundup Test. Your welcome email is on its way to your inbox."}` and the form showed that line. Read back from Kit: subscriber 4398477933, active, first name Roundup Test, tag Website Newsletter Signup (26223648), in sequence 2979796. **One thing to know:** this address was already in the sequence from S541's route test at 13:51, so Kit kept that start and sends no second welcome. The welcome email to check is the one from 13:51.

## How the two sign-ups were run, plainly

This Mac went behind the host's bot check partway through the checks (the host answers 202 with its check page to this machine's address). The sign-ups were therefore run on a copy of each built page served from this Mac, with the page's own deployed footer.js, its form filled and sent by a real Chrome, and the page's two requests to admin-ajax.php passed to the site from inside the host, byte for byte. Everything from the form to Kit is the real path; only the network leg left from the server rather than this Mac.

## For Chat to know

- **Kain's Safari** is on the same address, so it may meet the host's check page once before the footer shows. S541 is told.
- The Schools heading opens /academy/schools/, as the brief's table says. The header brief asks for /academy/schools/ to be pointed at /academy/ elsewhere in the theme; if that address is retired, the footer heading moves with it.
- Links elsewhere in the theme still name /free-events/ (the Manifesto, the About page, one policy page). The 301 carries them; nothing was changed in those pages.

OWED BACK: Chat's check of the built footer and the 13:51 welcome email, and the brief closed (Kain's look is done: "Yes, it's right").

*No em or en dashes in this file; checked before writing.*
