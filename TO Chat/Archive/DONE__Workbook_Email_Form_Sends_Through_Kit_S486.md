**DISPOSITION (Chat, Session 465, 11 November 2026):** Answered in FROM Chat/RULING__Postbag_Rulings_For_The_Theme_Sessions_S465, sections 1 and 2; arrival proved from Kit's records; written home in the workbook page spec and DSRD 4 section 5.1. Board: the workbook page card.

**For Chat. What this needs from you:** read the manager@achology.com inbox for the four test emails listed in section 3 and say whether each arrived and showed the right workbook; that one reading settles the brief's section 5 and its tests 2 and 4, which Code cannot see. Then rule on the five findings in section 5. Code, theme session S486, 11 November 2026 (its theme commits are labelled S484; that number was taken in the channel by another session in the same minute).

# DONE, partly: the workbook email form sends through Kit

Answers BRIEF__Make_The_Workbook_Email_Form_Send_The_Workbook_Through_Kit_S460. Built and on the build site at theme 0.707.964 (commits d7c75773, then two small ones for 963 and 964). Not called finished: the email's arrival is unverified by Code, and the workbook page's DSRD 6 record is not re-marked.

## 1. What was built

- All three boxes on every workbook page (the band, the right-hand column, the dark card) are one working form: "Your first name", "Your email address", a tick box reading "Send me the workbook and Achology's emails.", then the signed button. The name may be blank; the email may not.
- An unticked box stops the form and shows "Please tick the box to get your workbook." under the box. A failure keeps the address in the field and shows "That didn't go through. Please try again."; the failure is written to the server log by workbook, never by address.
- The form posts to the site (workbook-kit.php in the theme), never to Kit's script. It checks a token (a fresh one is fetched before sending, because a cached page can carry an old one), a hidden trap field, and a limit of twenty asks an hour from one network address. With no script the form posts by itself and the server answers the same way.
- The site then tells Kit through the installed Kit plugin's connected account: create or update the subscriber with the first name, write the seven fields, apply `Website Workbook Download` and the category tag, add to sequences 2965204 and 2965261.
- The seven values: `workbook_name` is the title before the colon; `workbook_link` is read from `pdf_file` at that moment; `workbook_cover` is a JPG 300 wide made once from the cover into uploads, folder workbook-email-covers; `workbook_course_cover` is one of 28 new 300 px JPGs in the theme's course covers folder; `workbook_course_tagline` is DSRD 2 section 2.6's line with its first letter lower case, copied word for word into the theme's data folder as course-taglines.json.
- No Kit script loads on a workbook page or its thank-you page, so no Kit cookie is set there, which closes the DSRD 3 section 6.5 question for this form. The Kit plugin's small stylesheet still loads site-wide; it is a stylesheet, not a script.

## 2. How the fields fit (measured in WebKit)

- Computer, 1268: in the band the name field (315) and the email field (its signed 317) share one row, the tick box and the signed button share the next, the privacy line 12 under them as before. The dark card is the same shape at its own width. In the right-hand column the four stand one above the other, 8 apart, the button the column's full width; the whole column block ends at 687 of an 800 tall window.
- Phone, 390: name, email, tick box, button, one above the other, full width, no sideways scroll.
- Field and button heights are the signed 48. The band is 64 taller than before. Tablet width was not measured.
- The tick box is the course page's signed one (form 6) at 20. The accessibility scan in the page gate reads zero WCAG 2.2 AA violations with the form on the page.

## 3. The tests, with times (11 November 2026, UTC)

| # | Workbook | Box | Address | Asked | Landed on its thank-you page |
|---|---|---|---|---|---|
| 1 | Karpman Drama Triangle (Psychology) | band, by direct post | manager@achology.com, name Kain | 15:05:19 | yes |
| 2 | Karpman Drama Triangle | band, in the browser | manager+wbtest1@achology.com, name Karen | 15:16:40 | yes |
| 3 | Circle of Concern Versus Control (Mindset Mastery, Psychology) | right-hand column, in the browser | manager@achology.com, name Kain | 15:19:27 | yes |
| 4 | The Johari Window (Personal Growth) | dark card, in the browser | manager@achology.com, name left blank | 15:19:38 | yes |

- Brief test 1: each box was used once and each of three workbooks once, not all nine pairings.
- Brief test 3, read in Kit: manager@achology.com carries the seven fields, the first name given, `Website Workbook Download`, the Psychology and Personal Growth category tags, and sits in both sequences. The fresh address carries the same for Karpman and was added to the delivery sequence at 15:16:40.
- Brief test 5: an unticked box stopped the form with its line (browser); a bad token and a missing tick are refused by the server; no Kit script on the page.
- The PDF link opens signed out (200, application/pdf). Both JPG covers load (200, image/jpeg).

## 4. The brief's section 5, and tests 2 and 4: NOT PROVED

Code cannot read the inbox. What Kit itself shows, read at 15:22:
- manager@achology.com was already in the delivery sequence from 10 November. Kit records an email sent to it at 15:06:22, one minute after request 1, opened at 15:09:27. Chat may have been testing with the same address at that minute, so this is not attributed with certainty.
- After requests 3 and 4, Kit showed no further send to manager@achology.com within three minutes.
- The fresh address showed no send in its own figures six minutes after asking, while the delivery email's recipient count had risen from 1 to 2.

So whether a second workbook reaches an address already in the sequence is open. Options seen, none built: (a) Chat reads the inbox and the question may close by itself; (b) if repeats do not send, take the address out of the sequence before adding it again, if Kit allows it; (c) send the delivery email from the site itself and keep Kit for the follow-ups; (d) trigger delivery from a Kit automation on the tag instead of a sequence.

## 5. Findings for Chat's ruling

1. Only one of the 86 workbooks carries `associated_course`; all 86 carry `source_course`, the full DSRD 5 name. The form reads `associated_course` first and `source_course` otherwise. The thank-you page reads only `associated_course` (its own rule 2), so it shows no course card for 85 workbooks.
2. Every Mindset Mastery workbook checked sits in Psychology, so the brief's three different categories could not include one; two categories were tested.
3. Two asks from one address inside a minute overwrite the fields before Kit sends, so the first email can show the second workbook (requests 3 and 4 were eleven seconds apart, on purpose once seen). It follows from one set of fields for all workbooks.
4. The test left `manager+wbtest1@achology.com` in Kit, in both sequences, and changed manager@achology.com's first name from "Achology" to "Kain". Both are Chat's to tidy.
5. The page gate on the Karpman page at 0.707.964 reads 39 passed, 14 failed, 8 for review; no failing line names the form. The fails are older lines (the privacy line's 12, picture sizes and names, keyword density, the page never scored, the breadcrumb space). The workbook page's DSRD 6 record was not re-marked this session.

## 6. Kain's connecting steps

None. The Kit plugin on the build site is connected and its token is fresh; every call above went through it.

## 7. Launch day

The seven field values are made by the site at the moment of asking, so they move to achology.com by themselves when the site does. The addresses written inside Kit's own emails (the two logos, the fonts) stay Chat's to change. One line for the launch checklist: after cutover, ask for one workbook and confirm every address in the email reads achology.com.

OWED BACK: Chat's reading of the inbox for the four emails, and rulings on section 4 and section 5 items 1, 3 and 5.

DOCUMENT TYPE: DONE

*No em or en dashes in this file; checked before writing.*
