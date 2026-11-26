For Chat: what this needs: (1) DSRD 3 section 5 and DSRD 10 section 9 to be brought into line with what shipped (the two rows named below); (2) a yes or no on adding Event data to the Events page (not on the agreed list, so not built). Nothing else is asked.

Done when: Chat has updated the two DSRD rows and answered the Event question in FROM Chat.

# SHIP: rich results, item 2 of the agreed string (0.708.510)

Code, S579 theme session (Opus), 26 November 2026.

## What Google's Rich Results Test said before

- A course page (CBT Practitioner): 3 valid items: Breadcrumbs, Course, Review snippets. No change needed.
- The courses directory (/courses/): 28 invalid course items. Each item was a Course with only a name, a provider and an Offer; Google's course markup needs a description and a course instance too.
- A workbook page: 1 invalid course item, the same cause (its isBasedOn was a Course with only a name and an address).

## What shipped (0.708.510)

- **The courses directory** lists each course by the address of its own page, Google's summary page form for a course list. Google now reads the page with no invalid items (Breadcrumbs valid). Each course page keeps its full Course, Offer and rating. **DSRD 3 section 5** (and the S362 spec section 5) still describe the old item shape: please change the row to "ItemList of the 28 course page addresses (summary page form); the full Course lives on each course page".
- **The seven school pages** add an ItemList of their own courses' addresses, named as the page's main entity. **DSRD 10 section 9** says school pages carry "WebPage + BreadcrumbList": please add "+ ItemList of the school's course addresses". The pass page carries none (it lists no school's courses).
- **Each course page's Course** now has an @id (its address plus #course), and **every workbook** points at it by that @id instead of naming a half-filled Course. My own reader confirms no workbook page now carries a Course item; Google's test hit its daily limit before it could re-read the workbook.

## Audited and already right

Book notes (Review of a Book, with its author and Rating), articles (Article with author), quote pages (Quotation), Help answers (FAQPage with Question and Answer, and a speakable part), breadcrumbs on every page kind read.

## Left, and where it belongs

- **Person and Organization links (sameAs), Kain's job title, the organisation logo on the course provider:** these are facts, so they belong to item 3 (AI citation readiness: one consistent fact set), whose words and links are Chat's. Not touched.
- **Events:** the Events page carries no Event data. The 22 records hold day, UK time, length, access and kind, enough for Google's online event markup (next date worked out from the weekday, online attendance, the page as the place). Event is not on item 2's list, so it was not built. Yes or no?

*No em or en dashes in this file; checked before writing.*
