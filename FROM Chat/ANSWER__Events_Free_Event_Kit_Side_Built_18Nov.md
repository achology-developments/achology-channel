NEEDS FROM CODE (theme, the Events session): the Kit ids below written into achology_free_event_kit() in events-setup.php, shipped with a version bump, then four test sign-ups read back in Kit.

# ANSWER: the Kit side of the free event sign-up is built and published

**For:** Code, the Events theme session. **From:** Chat, 18 November 2026. Answers the free taster sign-up line of the Events page card, and HANDOFF__Free_Event_Zoom_Links_From_Karen_S531.

**Kain's word.** Asked "Are these three free event emails right to send, signed by Karen?" with READING_PAGE__Free_Event_Emails_18Nov open, he answered: "Yes, send them" (18 November 2026). All twelve emails are published in Kit. The words are in EVENT_TICKET_WORDS_SIGNED_S472.json under free_event_emails.

**Kit is built to match the theme, not the other way round.** achology_free_event_send_to_kit() needs no change. It creates the subscriber, tags them with the shared tag and the event's own tag, and adds them to the event's sequence. Only the ids are missing.

## 1. The ids

Write this into achology_free_event_kit(), in place of the empty array:

```php
return array(
	'tag'    => 26107172, // Website Free Events Alerts
	'events' => array(
		'monday-1400-thought-provoking-group-discussion'     => array( 'tag' => 26107173, 'sequence' => 2976571 ),
		'wednesday-1800-live-personal-development-tutorial'  => array( 'tag' => 26107174, 'sequence' => 2976572 ),
		'thursday-0930-thought-provoking-group-discussion'   => array( 'tag' => 26107175, 'sequence' => 2976573 ),
		'friday-1430-applied-psychology-skills-workshop'     => array( 'tag' => 26107176, 'sequence' => 2976574 ),
	),
);
```

The four keys are Chat's reading of achology_event_address() for the four free rows. Before shipping, print achology_event_address() for every free event on the install and check each matches a key here exactly. If one differs, the install's address wins: use it as the key and tell Chat in one line.

Each tag is named "Website Free Event: " followed by its key, as SPEC section 6 says. Update the block comment above the function too, since it still says Kit's side is not built.

## 2. What each sign-up sends

Every sequence sends from manager@achology.com on template 5295433, in Europe/London time. It has three published emails, signed by Karen Ramsay. Repeat is on, so a second sign-up for the same event sends the link again.

| Event | Sequence | Email one, at once | Email two, 2 days later | Email three, 3 days after that |
|---|---|---|---|---|
| Monday 14:00 | 2976571 | 10612615 | 10612616 | 10612618 |
| Wednesday 18:00 | 2976572 | 10612786 | 10612790 | 10612792 |
| Thursday 09:30 | 2976573 | 10612794 | 10612795 | 10612799 |
| Friday 14:30 | 2976574 | 10612801 | 10612803 | 10612806 |

1. **Email one** is sent at once. It carries the event's name, "Every [day] at [time], United Kingdom time", and one button to the event's own Zoom link. The subject is "Your Zoom link for the [event name]".
2. **Email two** is sent two days later, at 11:00 United Kingdom time. It covers the rest of the Achology week and has one button, "See This Week's Events", to /events/.
3. **Email three** is sent three days after email two, at 11:00. It covers Achology Membership and has one button, "Become a Member", to /membership/.

The Zoom links carry meeting passwords. They live in Kit's emails only. Never put one on a page, in the theme, in a log line or in a file in the channel.

**Known behaviour, no change asked.** Someone who signs up for two events gets emails two and three twice, once from each sequence. The spec's consent_text custom field is not sent by the theme, so none was made in Kit.

## 3. The four test sign-ups

Ship the ids, then make one sign-up per event through the ticket's own form on /events/ on the build site. Use the test inbox you used for the workbook form tests, with a different plus address for each event.

1. Monday 14:00, Thought-Provoking Group Discussion.
2. Wednesday 18:00, Live Personal Development Tutorial.
3. Thursday 09:30, Thought-Provoking Group Discussion.
4. Friday 14:30, Applied Psychology Skills Workshop.

For each one, read back:

- the form shows its thank you line, not "That didn't go through", and the debug log has no new [achology free event form] line;
- in Kit, the subscriber exists and carries tag 26107172 and that event's own tag, and nothing else from this set;
- the subscriber is in that event's sequence only;
- email one reached the inbox within a few minutes, with the right event name, day and time, and its button opens that event's own Zoom meeting. Check the meeting number only, and never copy the link into the reply.

Thursday and Monday share an event name, so check closely that the Thursday test got sequence 2976573 and "Every Thursday at 09:30". Leave the four test subscribers in place: emails two and three reaching the inbox two and five days later is the last check.

Done when achology_free_event_kit() carries these ids on the build site, and all four test sign-ups read back as above.

OWED BACK: one line in TO Chat with the version, the four results, and any key that differed from section 1.

*No em or en dashes in this file; checked before writing.*
