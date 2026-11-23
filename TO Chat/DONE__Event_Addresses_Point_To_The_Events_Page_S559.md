NEEDS FROM CHAT: read for the record; two untimed records are yours to look at.

# DONE: the event addresses point to the Events page (Code, Branch G, S559, 23 November 2026)

Answers FROM Chat BRIEF__Event_Addresses_Point_To_The_Events_Page_S480. Theme session, Branch G. Theme version on the build site when done: 0.708.402 to 0.708.406 (no theme file changed for this job; the Events page itself is unchanged).

## What was there

The Event post type is not public on the build site (publicly_queryable false, no rewrite), so no event record ever opened as a page here, and none is in any sitemap (Rank Math's index has no event sitemap; read today). Each /events/{record-slug}/ answered 404. The redirects matter for the old site's addresses after the switch and for any shared link.

## The 23 redirects, one 301 each, proved from the server and in a browser

The Events page has no anchor named after a record's slug. Its own anchor for an event is the ticket's address, day, time and title (achology_event_address(), events-setup.php), and the page opens that ticket when the address carries it (events.js, "a shared link opens straight onto its ticket"). So each record's address goes to the page's own anchor, listed as the brief asks (record slug, then anchor):

- mindset-community-discussion-group: monday-1100-mindset-community-discussion-group
- thought-provoking-group-discussion: monday-1400-thought-provoking-group-discussion
- principle-based-discussion-group: monday-1400-principle-based-discussion-group
- live-coaching-practice-and-feedback: monday-1800-live-coaching-practice-and-feedback
- office-hours-with-karen-ramsay: tuesday-1130-office-hours-with-karen-ramsay
- neuro-linguistic-programming-group: tuesday-1300-neuro-linguistic-programming-group
- hands-on-skill-development-session: tuesday-1500-hands-on-skill-development-session
- communication-and-people-skills: tuesday-1900-communication-and-people-skills
- achologist-led-community-tutorial: wednesday-1000-achologist-led-community-tutorial
- achology-code-of-ethics-training: wednesday-1200-achology-code-of-ethics-training
- character-and-conduct-training: wednesday-1500-code-of-character-and-conduct-training
- live-personal-development-tutorial: wednesday-1800-live-personal-development-tutorial
- achologist-led-community-tutorial-2: wednesday-1800-achologist-led-community-tutorial
- principle-based-discussion-group-2: thursday-0930-principle-based-discussion-group
- thought-provoking-group-discussion-2: thursday-0930-thought-provoking-group-discussion
- the-wiser-woman-mentorship-group: thursday-1330-the-wiser-woman-mentorship-group
- achologist-led-community-tutorial-3: thursday-1800-achologist-led-community-tutorial
- informal-coffee-and-conversation: friday-0200-informal-coffee-and-conversation
- informal-coffee-and-conversation-2: friday-1000-informal-coffee-and-conversation
- achologist-led-community-tutorial-4: friday-1430-achologist-led-community-tutorial
- applied-psychology-skills-workshop: friday-1430-applied-psychology-skills-workshop
- mission-driven-mondays-get-clarity-for-the-week-ahead: **week** (the record has no time, so it is not on the page and has no anchor)
- on-becoming-a-person-mentorship-discussion-group: **week** (the same)

Each is a Rank Math row (ids 2952 to 2974), written straight into its table because the gate's redirect writer refuses a "#" in a destination. Proof: each address, asked from the server without following, answers 301 to https://achologytest.com/events/#{anchor}; in a browser, each of the 21 lands on the Events page with its own ticket open (the ticket's name read back matches), and the two untimed ones land on the week. The Event post type, its 23 records, the week, the panels and Kit form 5 are exactly as built.

**For Chat:** the two untimed records (Mission Driven Mondays; On Becoming a Person) carry no day time, so the page does not show them; and the Friday 02:00 Informal Coffee that Branch A flagged is record 47209, informal-coffee-and-conversation.

## Internal links

No published post, post meta or theme file links an /events/{record-slug}/ address.

**The ticket's Kind of Event link (theme 0.708.408, on the main session's yes):** every ticket's link pointed at /events/{kind}/, the planned single pages, which answered 404. The Kinds of Event block has no anchor per kind (its cards are buttons that open a kind's next ticket), so all nine now open the block's own heading, /events/#ev-kinds-h, and the ticket closes as the link is followed. A target change only; nothing moves on the page. The nine pairs (was, now):
- /events/achologist-led-tutorial/: /events/#ev-kinds-h
- /events/code-of-character-conduct-training/: /events/#ev-kinds-h
- /events/coffee-and-conversation/: /events/#ev-kinds-h
- /events/communication-skills-people-skills/: /events/#ev-kinds-h
- /events/live-coaching-practice-observation-and-feedback-session/: /events/#ev-kinds-h
- /events/principle-based-reflective-discussion/: /events/#ev-kinds-h
- /events/skill-development-workshop/: /events/#ev-kinds-h
- /events/the-achology-code-of-ethics-training/: /events/#ev-kinds-h
- /events/the-wiser-woman-project/: /events/#ev-kinds-h

Proof, headless WebKit on the build site: every ticket's data-kindpage reads https://achologytest.com/events/#ev-kinds-h at 1280 and 375 (tickets with no kind carry none, as before); a ticket opened from its address, then its Kind of Event link pressed: the address reads #ev-kinds-h, the ticket is closed, and the Kinds of Event heading stands 80 from the top of the window.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
