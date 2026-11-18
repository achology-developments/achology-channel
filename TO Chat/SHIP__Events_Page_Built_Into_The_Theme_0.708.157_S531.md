NEEDS FROM CHAT: a ruling on each Events gate line listed in the page's DSRD6_RECORD.md ("Lines the build view's gate fails"), so the record can read no fail once Kain has created the page.

# SHIP: the Events page built into the theme, 0.708.157 (S531, the Events build side session)

**For:** Chat. **From:** Code, theme session (the Events build side session started by the EVENTS Page Final Audit session), 17 and 18 November 2026. Answers the finish plan's sitting two (previews/events-page-s529/finish-plan.html).

## What shipped

- **The page:** template-events.php ("Events") and events-parts.php draw the signed preview with only Kain's picks. Every word comes from the words file, copied into the theme as data/events/words.json by tools/events_page_data.py, never retyped.
- **The events, editable by Karen:** a post type, Event (WordPress admin, Events), one record per entry: title, Name in Circle, weekday, UK start time, Free or Members Only, kind, description key, length, how often, who hosts, credit, weeks of the month. The 21 signed rows and the month's two untimed entries (Mission Driven Mondays, On Becoming a Person) were written once from the signed rows; the page reads the records.
- **Every time in the visitor's own time zone:** each event moves to its next time on the visitor's clock and to its local day in the week, the month, the list and the tabs; a weekend day gets its own column. Measured with the clock at London, Los Angeles and Sydney. With no script, the footer reads "Times are displayed in UK time." in Kain's line.
- **The questions block** joins certification.css's S464 rules (the preview's copy of them is gone), eight answers in the words file's order, 344 standing in for the free event answer until it is public.
- **The stylesheet** is the preview's own, flattened by tools/events_page_flatten.py: 228 rules of passed-over options gone, 286 that match nothing pruned, every kept rule at its signed weight.
- **Measured against the preview** element by element through the server at 1270, 768 and 375, in the week, the month, the whole list and both tickets: identical but for two mends. The word Achology in the two section headings takes the site's AA accent (axe found brand orange at 3.0 and 2.9 to 1). The list's week one now carries Mission Driven Mondays, as the month always did.
- **Your ANSWER S474 on the ticket:** the share words stand as built; the eleven events with no length on record get no invented length in Add to Calendar (the entry carries its start only).

## What is not done

1. **The page does not exist yet.** Kain creates it and picks the Events template (the main session puts that to him). Then Code sets the signed seo key over WP-CLI, reads it back, scores it, and runs the gate on the page for chapters 3, 4, 5, 9 and 11.
2. **The free sign-up reaches no one yet.** Kit has no free event tag or sequence and no Zoom links (SPEC section 6 and section 9 item 3). The form posts to the site, which answers "That didn't go through. Please try again." until Kit's ids are written into achology_free_event_kit() in events-setup.php. Building Kit's side is yours to brief.
3. **The record's reader lines** (chapters 1, 2, 6, 7 and 8) are yours and Kain's.

## Gates

CSS gate: PASS on events.css and certification.css. The page gate on the build view: 41 passed, 48 failed. Every fail is in the record with its proposed ground; none is a fault Code could find on the page. The printout is in gate-printouts-S531 beside the record.

Theme commits af6d5dff and 55a622e8, deployed as 0.708.157. The school session's 0.708.158 is built on them, so the build site and the zip carry this build.

OWED BACK: a ruling on each listed gate line.

*No em or en dashes in this file; checked before writing.*
