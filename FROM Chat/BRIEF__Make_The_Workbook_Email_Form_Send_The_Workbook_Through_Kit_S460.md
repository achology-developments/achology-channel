> CODE DISPOSITION, S468: WAITS ON the Accreditation page sitting ending; read in full by this theme session mid-sitting, and it is the next theme job after it, not started.

**For Code, theme session. What this needs from you:** make the "Get Your Free Workbook" box on all 86 workbook pages a working form that hands the address to Kit, so Kit emails the reader their workbook, then report in TO Chat. Chat, Session 460 branch, 10 November 2026. Every decision below is Kain's or Chat's and is recorded; build without asking unless something here cannot be built as written.

Read first: DSRD 4 section 5.1 (the paragraphs "How the workbook download gate works" and "No tick box", Kain's yes of 10 November 2026) and section 6.4 ("Settled"); DSRD 2 section 1.7 (the email box and the thank-you page); the Shared Road and The Workbook Pack in 17 Packs, and the Words notes, for the one line of copy this adds.

## 1. What is already done in Kit (by Chat, through Kit's connector)

Account: Achology Transactions Ltd, Creator Pro. Nothing else in Kit needs building for this job.

- **Tags:** `Website Workbook Download` (id 25677339), and seven category tags named `Website Workbook Category: <category>` for the seven DSRD 1 section 4 categories (ids 25677340 to 25677346).
- **Custom fields (keys):** `workbook_name`, `workbook_link`, `workbook_course`, `workbook_cover`, `workbook_course_link`, `workbook_course_cover`, `workbook_course_tagline`.
- **Sequence `Website Workbook Delivery` (id 2965204):** one email, sent 0 hours after joining, Kain's words in the Achology email design he approved on a real inbox test. It reads the five fields above. Repeat is on.
- **Sequence `Website Workbook Follow-Ups` (id 2965261):** three emails on days 2, 5 and 9. All three are in and published, in Kain's own words. Repeat is off.
- Two sequences named `Design Test` and `Design Test 2` are Chat's tests; ignore them.

## 2. The form, on every workbook page

1. **All three boxes work** (the band, the right-hand column and the dark card under the writing, `$ach_capture` in single-workbook.php), and each asks, in this order, exactly as Kain chose on the rendered page ("Yes, this form", 10 November 2026): a field "Your first name", a field "Your email address", a tick box reading "Send me the workbook and Achology's emails.", then the existing button. Nothing else (Kain: "no paragraphs, no explainers").
2. **The tick box must be ticked to get the workbook.** It starts unticked. If the button is pressed without it, the form stays put and shows under the box: "Please tick the box to get your workbook." The name may be left blank; the email may not. The fields and box must sit inside the signed design without changing any signed size or spacing; in the band and the column, where space is tight, keep their order and say in your report how they fit at computer and phone width. The privacy line stays as signed in the band and the dark card.
3. **Submitted on the server, never with Kit's script.** Post to the site (a REST route or admin-post), check a nonce, a honeypot and a simple rate limit, and validate the address. Loading no Kit script means no Kit cookies, which closes the DSRD 3 section 6.5 question for this form; say so in your report.
4. **On success, send the reader to** `/learn/workbooks/thank-you/{workbook-slug}/`, the page already built. On failure, keep them on the page with the address still in the field and this line under the button: "That didn't go through. Please try again."; log the failure.

## 3. What the site sends to Kit (API v4)

For the workbook the reader asked for, at the moment they ask:
- Create or update the subscriber by email, with `first_name` set to the name given (left as it is in Kit if blank), and with the fields: `workbook_name` (the workbook's searched name, for example "Karpman Drama Triangle Workbook": the title before the colon, the same name the thank-you page uses), `workbook_link` (the URL of its `pdf_file` attachment, read at that moment, so a re-import can never leave a stale link), `workbook_course` (the full DSRD 5 name from `associated_course`), `workbook_course_link` (that course's page, through `achology_course_url`), `workbook_cover` (the cover image, see section 4), `workbook_course_cover` (the course's own cover from the theme, `images/course-covers/course-quote-cover-NNN`, as a 300 px JPG like the workbook cover) and `workbook_course_tagline` (the course's tagline from the tagline table in DSRD 2, for example "develop the skills and psychological understanding needed to positively influence people's mental health and wellbeing.": first letter lower case, full stop kept, because the email reads "a course for people who'd like to {tagline}").
- Apply the tag `Website Workbook Download` and the tag for the workbook's primary `kh_category`.
- Add the subscriber to sequence 2965204 (delivery) and to sequence 2965261 (follow-ups).

The connection: use the installed Kit plugin's connected account if you can, or a Kit API key kept in wp-config, never in the theme. Kain does whatever connecting is needed himself, in Safari: write him the exact clicks, one action per step, checked against the screen you can see, in your report.

## 4. Pictures and addresses in the email

- **The cover:** Outlook on a computer does not show WebP. Give each workbook an email cover as a JPG, 300 px wide, made from its cover, and send that URL as `workbook_cover`. If a JPG cannot be made without a decision, send the WebP and say so.
- **The build site's address is inside the Kit email** (the two logos and the fonts load from achologytest.com, and so do the covers and PDFs). Add a launch-day line to your launch checklist: every achologytest.com address in Kit's two sequences moves to achology.com. Tell Chat which addresses, and Chat changes the emails.

## 5. One thing to prove, not assume

When an address that has already had one workbook asks for a second, Kit must send the second. Chat found that adding an address already in a sequence returns its record without restarting it. Test it with sequence 2965204, which has repeat on. If the second workbook does not arrive, do not invent a fix: report exactly what happened and the options you see.

## 6. Done, and how it is tested

Done when, on the build site, with a real address Chat can read (manager@achology.com):
1. Each of three workbooks from three different categories (Karpman Drama Triangle, one Mindset Mastery, one other), asked for from each of the three boxes, lands on its own thank-you page.
2. The email arrives within two minutes for each, with the right cover, name, course and link, and the link opens the PDF for someone not signed in to the site.
3. Kit shows the address with the seven fields and the first name, both tags, and in both sequences.
4. A second workbook for the same address arrives (section 5).
5. All three boxes show the name field, the email field and the tick box at computer and phone width, an unticked box stops the form with its line, and the email greets the test by the name given; the page passes its DSRD 6 gate, and no Kit script loads on the page.

Report in one DONE file in TO Chat: what you built, the five test results with times, the section 5 finding, Kain's connecting steps, and the launch-day addresses. Chat then shows Kain the working form.

*No em or en dashes in this file; checked before writing.*
