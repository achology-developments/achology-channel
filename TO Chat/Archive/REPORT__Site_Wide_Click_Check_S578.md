> Chat S494, 26 Nov 2026: all faults fixed (S577, S580) or left as signed (fault 9, ruled). Archived.
> CODE DISPOSITION, S577: all five faults fixed and proved live at 0.708.504 and 0.708.505 on Kain's "Yes, fix all five" (TO Chat SHIP__Click_Check_Fixes_S577).
# REPORT: Site-Wide Click Check of the Live achology.com (S578)

Plain words. Run on the live site, 26 November 2026, theme 0.708.503, in the built-in browser, at laptop width (1440) and phone width (375). Nothing was changed, nothing was submitted, and no personal details or card numbers were entered. Kain's yes is needed before any fix.

**Session number.** The brief called this S579; the harness numbered the session S578, so the files use S578.

## The short answer

No broken, stuck or error-throwing control turned up. Every toggle, tab, accordion, filter and menu I tried opened, closed and undid correctly, the console held no real errors on any page, no page scrolled sideways on a phone, and nothing was behind a dead button. I found **five small faults**, all to do with the cookie banner, menu wording and the film, none of which stops a visitor doing anything. They are listed first. Then the full list of what was tested.

## Faults found

1. **The cookie banner's "See Preferences" panel shows only "Functional (Always active)".** Statistics, Preferences and Marketing are hidden by the stylesheet (display none). What I did: opened the banner on the homepage at phone width (a fresh visitor, no cookies), pressed See Preferences. What happened: one row, Functional, and nothing a visitor can switch on or off; "Save preferences" can then only mean "reject". What should happen: either a Statistics row (Google Analytics and Clarity are statistics) the visitor can switch on, or the Preferences button removed so the banner does not offer a choice it does not hold. Whether the bare panel is intended is Kain's call.
2. **Escape does not close the reopened cookie banner.** What I did: after Reject All, pressed the footer "Cookie Settings" link, then Escape. What happened: the banner stayed. It is marked as a modal dialog, so Escape is expected to close it; the small close button does work. Low.
3. **The cookie banner's close button is named "close-dialog" for screen readers** (a code label, not words). Low.
4. **The phone menu button keeps the words "Open menu" while the menu is open.** What I did: opened the menu on the homepage at 375. What happened: the button's spoken label stayed "Open menu"; only its expanded state changed. What should happen: "Close menu" while open. Low.
5. **The Vimeo film on the homepage loads Vimeo after a Reject All.** What I did: rejected all cookies, then pressed Play on the "Achology film". What happened: the Vimeo player loaded and started. The visitor did press Play, so it may be acceptable, but it is a third party loading with statistics and marketing rejected. This is for Kain to rule on, not a click fault.

Not faults, checked and cleared (so nobody chases them): several "does not turn off when pressed again" results were the one-of-several pattern (sort chips, course tabs, staircase rows), which is correct; "Pay Monthly" looked dead to my script only because the finder redraws its buttons; the pricing "View the courses" rows close on the second press but take about half a second, so a fast check read them as stuck; one 404 in the console belonged to the deliberate 404-page test; the search icon does not close the search on a second press, but "Close search" and Escape do.

## What I tested, page by page

Method for every page: each toggle, tab, accordion and chip switched on and again off, one at a time; console and failed-file check after each page; sideways scroll check; keyboard on the header, search, phone menu and cookie banner.

**Every page (header, footer, cookie banner, newsletter).**
- Search button: opens, puts the cursor in the box, Escape closes and returns focus to the button, "Close search" closes it. OK.
- Phone menu at 375: opens, closes by button, by Escape (focus returns to the button), the page behind stops scrolling while open. The five menu groups open one at a time and shut again. OK apart from fault 4.
- Cookie banner at 375, fresh visitor: shows Accept All, Reject All, See Preferences. Reject All set the cookies to deny, no Google or Clarity request, no analytics cookie. The footer "Cookie Settings" link reopens it; the close button closes it. Accept All was not pressed so no test visit lands in Kain's analytics. Faults 1 to 3.
- Newsletter form in the footer (Kit, "Join the Roundup"): empty and bad-email cases show their message ("Enter your first name", "Enter your email address in the form name@example.com") and put the cursor on the right field. The hidden extra field is out of reach of the keyboard. Nothing was sent. OK.

**Homepage (laptop and phone).** The course finder: the quick-start buttons switch on and off, filter chips switch on and off, Clear all empties everything, the monthly price box takes a number and empties again, the count wording reads right. OK at both widths. The film Play button starts the film in place (fault 5).

**Academy page and the NLP school page.** History chapters and school rows switch to the one picked; the first row stays lit when pressed again, which is the pattern. OK.

**A course page (NLP Practitioner).** Section rows and the "Pay In Full / Pay Monthly" tabs work. OK.

**Courses page.** Sort chips (most popular, highest rated, most in-depth) switch one at a time. OK.

**Pricing page.** Course-group tabs, pay-in-3 and pay-in-5 tabs, "View All 28 Courses" and the eight "View the courses included" rows open and close. OK, laptop and phone.

**Membership page and Choose Your Free Course page.** Week, Month and List views, Monthly and Annual price tabs. OK.

**Events page.** Month and List views, the price tabs. OK.

**Access All Areas page.** The 28 course rows and the ten benefit rows each show their own panel and switch to the next; the three pay tabs; "Show More Reviews". OK.

**About page and What Achology Believes.** Chapter tabs, question rows, belief rows, "Show More Reviews". OK.

**Instructors list and an instructor page; Testimonials; Reviews; Accreditation; Certification; Centre of Human Development; Privacy Policy.** Nothing beyond the header to break, no console or file errors. OK.

**Knowledge Hub landing and the Psychology subject page.** The filter row All, Articles, Book Notes, Quotes works one at a time. OK.

**Search results page** (for "anxiety"). Results load, the filter boxes and the newsletter box are present. OK.

**An article, a workbook, a book note and a quote page.** Load with no error; only the header controls to test. OK.

**Help Centre landing page and the 404 page.** Load, search box present, no error. OK.

## What was not tested

- Not all 80 pages: one page of each kind, plus the pages where a theme script runs.
- The gift page, the Enquiries form, and the help category and help article pages did not get their own pass. They load scripts that behaved on the other pages, but nobody pressed their own buttons.
- Accept All in the cookie banner, and any real form sending, by instruction.
- Row-by-row keyboard use of the pricing and academy rows (header, menu, search and banner only).
- Scripts that only act while scrolling (the section bar, the reading line).

## Method note for the next check

A press-and-press-again script gives false alarms on pages that redraw their own buttons (the finder) and on anything that closes with a short slide (pricing rows). Real mouse clicks and a half-second wait removed every false alarm here.

OWED BACK: Kain's yes on the faults above; or a ruling on fault 1 and fault 5.

## S579: the leftover pages (gift, Enquiries, a Help category, a Help answer)

Checked 26 November 2026 by a helper session of Code's S579, at phone and laptop width, mouse and keyboard, changing nothing (no form sent, no cookie choice made). There is no page named gift; the free course page (/membership/choose-your-free-course/) was taken as it. No console errors from any of the four pages.

Faults found, fixes only after Kain's yes:

6. **Free course page, the course cards:** pressing a card's picture, its tick circle included, does nothing; the picture sits over the hidden choice. Pressing the title or the lower card works. Both widths.
7. **Free course page and Enquiries form:** leaving an empty or wrongly typed name or email field shows no message, so a visitor learns only when they press Send. Both widths. (Send was not pressed, so what Send itself says was not seen.)
8. **Help category page (Membership, Access, and Plans):** the browser tab reads "Membership, Access, and Plans Archives | Achology"; the word Archives is WordPress's default. Both widths.
9. **Help category page, minor:** after Show All 23 Questions the button goes and the list cannot be folded again.
10. **Help answer page, phone width:** Escape does not close the open Browse Help Topics panel; only its button does.

Working as it should: the free course page's choice line and menu; the Enquiries topic chips, their Quick Answers and the extra field for each topic; Show All moving focus to the first new question; every link on the four pages (200); the Help answer's On This Page links, Yes and No, and Next Question. One record: the helper pressed Yes or No on the answer "choose free course annual achology membership" at both widths, which counts as a visitor vote where analytics consent exists.

Not settled: whether the keyboard focus ring shows on the Help answer's Yes and No buttons (only a scripted check was made; a real Tab pass settles it).
