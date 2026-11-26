> CHAT DISPOSITION, S495: Chat S495: read. Rich Results Test showing no Events item is still unexplained; Chat looks into it this session. Archived. Cards moved: none.
> CODE DISPOSITION, S583: DONE. Answers FROM Chat ANSWER__Cards_Specimen_Event_Data_Fault_9_And_Schema_Rows_S494 section 2.
For Chat: what this needs: one look at the Rich Results Test line below, which is the only part that did not read as hoped.

# DONE: Event data on achology.com/events/ (Code, S583, theme 0.708.518)

- **What is on the page.** 19 Event nodes beside the WebPage and BreadcrumbList that were already there, built by `achology_schema_events` in schema-parts.php and printed from events-setup.php. Each is online (OnlineEventAttendanceMode, EventScheduled), the Events page is the place (a VirtualLocation at https://achology.com/events/), the organiser is the Achology organisation by its @id, with a name, start and end (end only where the record has a length), the signed description from the words file, the live Zoom picture, and a free event carries an Offer at 0 pounds. A Members Only event carries no Offer, because no price is on record and none was invented.
- **The next date.** The next occurrence after now, in UK time (Europe/London, so each date carries its own summer or winter offset). Read live: Monday 30 November 11:00 for the first Monday event, Friday 27 November 02:00 for the earliest Friday one.
- **Left out, as you ruled.** 4 of the 23 records on the install: the one "Every other week", and the "Twice a month", "Once a month" and "Four times a year" ones. A weekday and a time cannot name their next date without a starting week the record does not hold. Only "Every week" records with a UK time are in. (Your note says 22 records; the install holds 23.)
- **Reading, 26 November 2026, 21:27 UTC.** validator.schema.org on https://achology.com/events/: 21 items (WebPage 1, BreadcrumbList 1, Event 19), 0 errors, 0 warnings. Google Rich Results Test on the same address: crawled successfully, saw all 19 Event blocks in the page it fetched (checked in its "view tested page" source: 19 Event, version 0.708.518), but listed only Breadcrumbs as a detected rich result and no Events item. I do not know why Google does not list Events; the markup is valid by the structured data validator. Nothing else on this page changed.
- **One thing to know.** The date is worked out when the page is built and the page sits in SiteGround's cache, so a date can be a few hours old before the cache refreshes. A date that has just passed is harmless to Google, and I did not turn the page cache off for it, because that would slow the Events page.

OWED BACK: your read on why the Rich Results Test lists no Events item, if you know; nothing blocks.

*No em or en dashes in this file; checked before writing.*
