CODE DISPOSITION, S541: WAITS ON Kain's go-ahead in the S541 sitting, after the Academy phone walk closes; this session takes it next.
NEEDS: Code to rebuild the site-wide footer exactly as Kain signed it on the rendered mock-up, wire its Achology Roundup sign-up to Kit, and send one DONE with the proof.

# BRIEF: the footer, rebuilt from the signed mock-up

From Chat, 20 November 2026. For a theme session.

Model: Claude Opus 5.5. Effort: high.

## Why

Almost every page is now designed, so the footer becomes the map of the whole site and the one place on every page to join the Achology Roundup. Kain signed it on the rendered mock-up: "Yes, build it" (20 November 2026, after four rounds in Chat). It replaces DSRD 8 section 19's option A.

## The spec

**The signed mock-up is the spec:** `MOCKUP__Footer_Design_System_20Nov.html` in the Header + Footer folder (Component Design Prototypes). It was built from the theme's own fonts.css, base.css, buttons.css, footer.css and buttons.js, and from the fo2 footer form rules in course-page.css, so its classes are the theme's. The only new CSS is the block scoped `.fx` near the top of its style element; carry that into footer.css without the `.fx` scope. Build it exactly, then compare the built footer with the mock-up at 1280 and 390 before Chat looks.

**From top to bottom:**

1. **The invitation, four variations (Kain, 20 November 2026: "Yes, add both").**
   - **Most pages:** the $7 band (`footer-invite`, `btn btn-primary footer-invite__btn is-on-dark`), as built.
   - **Course pages:** the six free lessons band (fo2, pick 296), as built.
   - **School pages and the Access All Areas Pass page:** the six free teachings band (fo2, S482), as built. Chat read the pass page's footer on the build site the same day: it already carries it, "Try Six Free Teachings Before You Decide", so nothing changes there.
   - **Workbook pages, new:** the fo2 band offering the six free lessons of the course the workbook comes from, through the course free lessons route (form 6, course-kit.php) with that course's fields, exactly as the course page's own footer form sends them. Words: the over-line "Experience the Course", the heading "Try the First Six Lessons Before You Decide" (both the course band's signed words), and the line "We'll send you the first six lessons of {course name}, the course this workbook comes from, one each day for six days." with the course's DSRD 5 name linked to its page; the button "Send Me the First Six Lessons" and the tick box "Send me the six lessons and Achology's emails." (both signed on the course band). The workbook's course is the one its page already names under Where This Workbook Comes From. Where a workbook has no course, its footer keeps the $7 band. The line is Chat's wording inside Kain's frame, overturnable.

   Only the spacing changes on every variation: `.footer-main` top padding `--sp-2xl`, the invite's padding-bottom and margin-bottom `--sp-xl`.
2. **The map, five columns in this order (Kain's words):** About Us, Courses, Community, Learn for Free, Schools. Schools is last and widest. At 1024 and up: `repeat(4, minmax(0,1fr)) minmax(0,1.5fr)`, gap `--sp-xl`. From 768: four columns, Schools full width beneath. Under 768: two columns, Schools full width last. Each column heading (`footer-col__head`, an h2) is itself a link to its section, with no arrow: the theme's button script turns an arrow into a disc. Links keep `footer-col__links` and the family's fire line; each school keeps its own colour line (`footer-school`, `--fire-line:var(--school-{key}-primary)`). Under 768 each link has at least 24 pixels of tap height.

| Column | Heading opens | Links, in order |
|---|---|---|
| About Us | /about/ | Founders' Letter /about/founders-letter/; What Achology Believes /about/what-achology-believes/; Our People /about/instructors/; The Manifesto /about/manifesto/; Code of Ethics /about/code-of-ethics/ |
| Courses | /courses/ | The Academy /academy/; Access All Areas Pass /access-all-areas/; Pricing Options /pricing/; Certification /certification/; Accreditation /accreditation/ |
| Community | /membership/ | Live Events /events/; Free Live Events /free-events/; Member Testimonials /testimonials/; Student Reviews /reviews/; Code of Conduct /about/code-of-character-and-conduct/ |
| Learn for Free | /learn/ | Articles /learn/articles/; Book Notes /learn/book-notes/; Quote Articles /learn/quotes/; Workbooks /learn/workbooks/; All Topics /learn/tags/ |
| Schools | /academy/schools/ | Neuro-Linguistic Programming; Cognitive Behavioural Psychology; Life Coaching and Skilled Helping; Counselling and Hypnotherapy; Mindfulness, Insight and Wisdom; Mental Health and Emotional IQ; Personal Growth and Development (the footer-only names Kain ruled at S134, each to its school page) |

3. **The Achology Roundup, on every page (revised on Kain's "yes please", 20 November 2026, after "There's nothing here that says it's a newsletter").** The signed fo2 parts (b4 fields with their name and envelope icons, `b4-btn pf2__btn`, the round `pf2__tick`) inside `footer-invite fo fo--2 footer-roundup`, with a top hairline and padding `--sp-xl`. Words, left: the over-line "Our Occasional Newsletter"; the title "The Achology Roundup" at `--text-24`; one line at `--text-14`, "New courses, events and opportunities, sent only when there's something worth telling you." Right, at 1024 and up: name, email and the button on one line (`grid-template-columns: minmax(0,1fr) minmax(0,1fr) auto`, gap `--sp-sm`, the button `grid-column: auto`), the form 640 wide, the tick box beneath; the block centred on its row. Below 1024 the fo2 form stacks as signed. Fields "Your first name" and "Your email address"; button "Join the Roundup"; tick box "Send me the Roundup and Achology's emails." No privacy line under it (Kain, pick 296). It sends to the Kit route already built from BRIEF__Achology_Roundup_Kit_Route_20Nov (roundup-kit.php, theme 0.708.267, tag 26223648, sequence 2979796; DONE__Achology_Roundup_Kit_Route in TO Chat). The footer is now that route's visible form; its hidden test form may go.
4. **One bottom row.** Left: the copyright "© 2026 Achology Transactions Ltd", linked to /help/privacy-and-legal/achology-s-registered-company-details/ (that signed Help answer holds the company names, numbers and registered office, which keeps the site within the UK disclosure rule); then Help Centre /help/, Enquiries /enquiries/, Privacy, Terms, Cookies, the Complianz Cookie Settings button (its id and classes unchanged), All Policies /policies/. Gap `--sp-xs` by `--sp-lg`, and none of the "·" separators. Right: the logo at 28 pixels and the four social icon buttons at 32. On one row at 1024 and up; stacked below that, each link 24 pixels tall to tap.

**Out of the footer:** Student Sign In (Kain: it lives in the header), Free Coaching, Disclaimers, Trust, How We Write, Refunds and Accessibility as separate links (they sit behind All Policies), the long company paragraph, and "All rights reserved."

## Checks Code runs before the DONE

1. Every footer link answers 200 on the build site, and every heading opens its section.
2. A screenshot of the built footer beside the mock-up at 1280 and 390.
3. css_gate and the page gate on five pages, each showing its own invitation: one ordinary page, one course page, one school page, the Access All Areas Pass page and one workbook page.
4. One real free lessons sign-up through a workbook page's footer, read back from Kit with that course's fields and tags.
5. One real Roundup sign-up through the footer, as manager+roundup-test@achology.com, first name "Roundup Test", read back from Kit with its tag and sequence 2979796.

## What Chat checks afterwards

The footer on the build site at 1280 and 375 for short lines and tap sizes, every link, and the welcome email arriving for the test sign-up.

Done when: the new footer is on every page of the build site, matches the signed mock-up at 1280 and 390, every link opens, and a Roundup sign-up from it is in Kit with its tag and sequence and the welcome email sent.

OWED BACK: one DONE in TO Chat with the theme version, the two screenshots, the link check and the Kit read-back.

*No em or en dashes in this file; checked before writing.*
