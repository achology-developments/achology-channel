REPORT: Events booking and ticketing options for Achology and the Centre for Human Development
Researched 23 November 2026. Research only: nothing in the theme, project or channel was changed.

## The short answer

Do nothing to the Achology launch. Today's Events page (the Event post type plus the Kit form 5 sign-up, with live member events in Circle) already does what Achology needs, and a booking plugin would add weight without adding anything a visitor needs.

For the Centre for Human Development, use **Events Manager** (the free plugin on wordpress.org). It is the best fit for "a bigger events page, and not building from scratch" because the free version already gives unlimited events, unlimited free bookings, recurring events, time zones, attendee lists, confirmation emails, calendar buttons and capacity limits, and it is built to be edited by the site owners. If the Centre later needs paid tickets, waitlists or custom booking fields, the paid add-on is about $89 to $129 a year for one site.

## What Achology needs, from the spec (sections 6, 7 and 11)

- A free event sign-up that goes to Kit, with a tag per event and a sequence per event. Kit form 5 does this today.
- 22 event kinds plus about 19 weekly entries, edited by Kain and Karen in WordPress. Times stored in UK time and shown in the visitor's time zone. Already built.
- Members-only events are not booked on the site at all. They run in Circle, which members pay for.
- Achology therefore has no booking problem to solve. The gap is only at the Centre, which will have a larger events page and may sell tickets.

## Comparison table

Figures come from each plugin's wordpress.org listing and the vendors' own pricing pages on 23 November 2026, unless marked. "Pro" means a paid add-on.

| Option | Licence and maintenance | Free tier gives | Needs paid for | Cost | Fit in a custom theme | Could serve the Centre too |
|---|---|---|---|---|---|---|
| **Events Manager** (WP plugin) | GPL, version 7.6 released 19 Nov 2026, 60,000 installs, rated 4.2 out of 5 | Unlimited events and bookings, free RSVP, recurring series, timeslots, multi-day, capacity limits, time zones per event, attendee lists with CSV export, approvals, confirmation emails, Google, Outlook and Apple calendar buttons and iCal feed, virtual locations, REST API, CSV import, hybrid events, migration from The Events Calendar | Payments (PayPal, Stripe, Square), PDF tickets with QR check-in, custom booking form fields, waitlists (the listing marks these Pro) | Free. Pro $129 a year, one site (sale price $89 until 1 Dec); Pro Plus $169 a year | Strong. Templates can be overridden in the theme, block editor blocks, shortcodes, template tags | Yes, one plugin on both sites |
| **The Events Calendar** with **Event Tickets** (WP plugins) | GPL, 6.18.4.1 and 5.31.1.1, both updated in the last week, 600,000 and 90,000 installs | Calendar views, iCal export, free tickets and RSVPs, Stripe and PayPal ticket sales through Tickets Commerce | Recurring events (Calendar Pro), waitlists, custom registration fields, WooCommerce, QR check-in, Zoom (Plus and add-ons) | Free core. A competitor's page says free Stripe sales carry a 2 percent fee, which The Events Calendar's own pages do not confirm. Plus and Pro are paid | Good, but it brings its own event post type and heavy templates, which would clash with Achology's existing Event post type | Yes, but recurring events cost money, and weekly events are the whole point |
| **Modern Events Calendar Lite** (WP plugin) | GPL, on GitHub, vendor Webnus | Calendar, single, multi-day and recurring events (vendor says so; a third party says recurring is Pro) | Booking and ticketing (the vendor's own upgrade pitch is "advanced booking system, selling tickets") | Pro is paid, no lifetime licence | Heavy styling | No: bookings are the paid part |
| **Eventin** (WP plugin) | 4.1.31, updated 22 Nov 2026, 10,000 installs, rated 4.7 | Free or paid events, RSVP, recurring events, Zoom and Google Meet links sent after registration, QR check-in, confirmation emails (all as listed on its page) | Not checked in detail | Free core | Own post types and styling; not verified in a custom theme | Possible, less proven than Events Manager |
| **EventPrime** (WP plugin) | 4.4.0.0, updated 18 Nov 2026, 7,000 installs | Calendar, bookings, recurring, free and paid events with PayPal and Stripe | Not checked in detail | Free core | Own post types; not verified | Possible, smaller community |
| **Sugar Calendar Lite** (WP plugin) | 3.18.0, updated 19 Nov 2026, 10,000 installs | Calendar, registrations, Stripe ticket sales | Recurring events, venues, RSVPs (the listing says Pro) | Free core | Light by design | Weak: recurring and RSVPs are paid |
| **GatherPress** (WP plugin) | 0.36.2, updated 7 Nov 2026, only about 100 installs | Events, RSVPs without an account, guests, emailing attendees, online events, block editor | Not paid; it is simply small | Free | Block based | Small and young, so a risk |
| **Hi.Events** (open source app, not WordPress) | AGPL-3.0 with extra terms, v2.2.0 released 7 Nov 2026, 4,200 GitHub stars, 164 open issues | Self-hosted: ticketing, check-in, widgets and API, but a visible "Powered by Hi.Events" link and published code changes | Removing the branding link and keeping changes private (from 249 euros a year) | Self-host free. Cloud: about 0.75 percent plus 40 cents a paid ticket plus Stripe (secondary sources, not confirmed on its own page) | Separate app, embedded by widget, so it does not sit inside the theme | Possible for paid tickets, but it needs hosting SiteGround cannot give (it is a Docker app) |
| **pretix** (open source app, not WordPress) | AGPL, active (last push 23 Nov 2026), 2,579 stars, 181 open issues | Hosted: first 500 free tickets a year free; self-hosted community edition free | Hosted paid tickets: 2.5 percent, capped at 15 euros a ticket (older page gives a 2,500 free ticket allowance, so conflicting) | Hosted fees as left, or run your own server | A WordPress widget plugin embeds the shop, but its page warns it is not tested with the last three WordPress releases | Strong for proper ticketing, but a second system to run |

Others I looked at in passing and did not rate: WP Event Manager (a directory style plugin, 80 percent rated, mostly sold through paid add-ons), and Luma, which is off WordPress and so does not fit "owners edit events in WordPress".

## Recommendation

**Events Manager (free) for the Centre for Human Development. Leave Achology as built.**

Reasons:
1. It is the only free option whose free tier covers what the Centre's weekly, bookable events need: recurring series, capacity limits, time zones, confirmation emails, calendar buttons, virtual links, unlimited bookings. The Events Calendar charges for recurring events; Sugar Calendar charges for recurring and RSVPs; Modern Events Calendar Lite sells booking as the upgrade.
2. It is a WordPress plugin, so Kain and Karen edit events in WordPress, as the house rules require. Hi.Events and pretix would be a second system with its own login.
3. It is maintained: 7.6 shipped four days ago, and it has an official import from The Events Calendar, so there is no lock in either way.
4. It stays out of the way: no per-ticket fee in the plugin itself, and the Pro add-on is optional.

Achology is left alone because the Event post type and the Kit sign-up already exist, are signed, and have no gap. Adding Events Manager there would duplicate the 23 records.

**Cost:** 0 pounds for the free version. Paid only when the Centre wants paid tickets or waitlists: Pro at $129 a year for one site ($89 during the sale to 1 December 2026), plus Stripe's own card fees.

**Code's time (my estimate, not from any vendor):** the Centre events page, about 2 to 3 days to template the list, week view and event pages to the Centre's design, plus about half a day to connect bookings to a mailing tool (Kit, or whatever the Centre uses) by a small function on the plugin's booking hooks. For Achology there is no work at launch, and none after unless Kain chooses to move it.

**What it keeps:** the Achology Events page, the 23 Event records, Kit form 5, Circle for members-only events, and the Kit tags and sequences. **What it replaces:** nothing on Achology. At the Centre it replaces the idea of a custom-built events calendar and booking form.

## If Kain later wants Achology on the same tool

Events Manager can hold the weekly entries as recurring events and send each free sign-up to Kit through a hook. That would be a real build (about 2 to 3 days to move the 23 records and restyle) for no visitor gain, so I would not do it before there is a reason such as paid public events.

## When the answer would change

- If the Centre mainly sells paid tickets to large events with scanning at the door, pretix hosted (2.5 percent, capped) or Hi.Events Cloud (cheaper per ticket) are better than paying for plugin Pro plus Stripe, but they live off the site.
- If recurring is not needed at the Centre, Event Tickets (free) is a safe second choice.

## What could not be verified

- Events Manager's own free versus Pro comparison table lost its tick marks in the text I could read. I could not confirm from its pages which tier holds waitlists, webhooks, Zoom links and the number of recurring events allowed. The wordpress.org listing marks waitlists, payments, PDF tickets and custom form fields as Pro, and recurring events as free. A short test on a staging install would settle all of these in an hour.
- Whether Events Manager can post to Kit without Pro. It has booking hooks for code, but I did not test it, and I found no ready made Kit connector for any of these plugins. Zapier, Make or the WP Webhooks plugin could bridge, with free tiers.
- The 2 percent Stripe fee on free Event Tickets comes from a competitor's page only.
- Hi.Events Cloud fees come from third party sites, not from its own pricing page. The pretix free ticket allowance differs between two of its own pages.
- Eventin, EventPrime and GatherPress were judged from their listings only; none was installed or checked in a custom theme.
- Whether Events Manager's templates fit the Achology Event post type has not been tested, and I did not test any plugin on the build site.
- Code's time estimates are mine.
- Modern Events Calendar Lite's listing could not be read from the plugin API, so I used its GitHub page and third party reviews.

## Sources

- https://wordpress.org/plugins/events-manager/
- https://wp-events-plugin.com/pricing/
- https://wp-events-plugin.com/features/
- https://wordpress.org/plugins/events-manager-zoom/
- https://wordpress.org/plugins/the-events-calendar/
- https://wordpress.org/plugins/event-tickets/
- https://github.com/webnuswp/modern-events-calendar-lite
- https://wordpress.org/plugins/wp-event-solution/
- https://wordpress.org/plugins/eventprime-event-calendar-management/
- https://wordpress.org/plugins/sugar-calendar-lite/
- https://wordpress.org/plugins/gatherpress/
- https://hi.events/licensing
- https://github.com/HiEventsDev/Hi.Events
- https://pretix.eu/about/en/pricing/
- https://github.com/pretix/pretix
- https://wordpress.org/plugins/pretix-widget/
- https://theeventscalendar.com/product/wordpress-event-tickets-plus/
