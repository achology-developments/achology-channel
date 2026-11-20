NEEDS: Code to rebuild the site-wide header and phone menu exactly as Kain signed it panel by panel on 20 November 2026, rename "Wise Quotes" to "Quote Articles" in the theme's visible words, and send one DONE with the proof. Take it after the footer brief, in the same theme session if that suits.

Done when: the build site's header shows the six doors with the four panels and the phone menu as DSRD 8 section 18.22 sets them, no reader-facing "Wise Quotes" or "Ultimate Pass" is left in the theme, header.css passes its gate, and the DONE carries the built header read at 1280, 1024, 960 and 375 against the mock-up.

# BRIEF: the header's six doors, and one name for quote articles (Chat, Session 478, 20 November 2026)

**For:** Code. **From:** Chat. **Card:** Header and Mega Menu Review.

## The spec

- **DSRD 8 section 18.22,** written today, is the whole ruling, door by door, with Kain's words. Read it first.
- **The mock-up:** MOCKUP__Header_Six_Doors_20Nov.html in the Header + Footer folder (Component Design Prototypes). It was built from the header the build site served at 0.708.266 (kept beside it as header_as_served_0.708.266.html) and the theme's own stylesheets, by build_header_six_doors_20Nov.py in the same folder. Every card, word and address in the mock-up is the spec. Where the mock-up and section 18.22 differ, section 18.22 wins, and tell Chat.

## What changes, in header.php

1. **The bar:** Academy (/academy/), Membership (/membership/), Knowledge Hub, Pricing, About, Help. Academy is the old Courses item renamed. Membership is new.
2. **The Academy panel:** as Courses was. The bottom row is now The Achology Academy (/academy/, "Seven Schools of Modern Applied Psychology", Lucide graduation-cap), Certification, Accreditation. Learn for Free is gone from the whole header.
3. **The Membership panel (new):** heading "Learn, Practise and Grow Alongside Others". Eight cards in this order: Achology Membership (/membership/, "Live Events, Mentorship and Community", users); Live Events (/events/, "See What's On This Week", calendar); How to Join a Free Event (/help/events-and-mentorship/how-to-join-a-free-achology-event/, "Your First Event, Step by Step", calendar); Code of Character and Conduct (/about/code-of-character-and-conduct/, "How Members Treat One Another", handshake); Membership Questions (/help/membership-and-access/, "Plans, Access and How It All Works", circle-help); Events and Mentorship Questions (/help/events-and-mentorship/, "How Events, Mentors and Groups Work", circle-help); Community Questions (/help/community-and-conduct/, "How Members Connect and Take Part", circle-help); Getting Started (/help/getting-started/, "Where to Begin When You Join", circle-help). The Find Your Community card sits beside them. Eight cards end level with that card; the mock-up measured 464 against 457.
4. **The Knowledge Hub panel:** unchanged, except the second card reads **Quote Articles**.
5. **The About panel:** Kain's eight, unchanged, except **Ultimate Pass becomes Access All Areas Pass.**
6. **One line:** the six words never wrap. The mock-up used `.site-nav__link { white-space: nowrap; }` and, from 960 to 1099, the list's gap at 20. Use the nearest spacing token and name the value in the DSRD 8 s18.22 annotation. Measured in the mock-up: one line at 960, 1024, 1100 and 1280, with nothing past the edge.

## The phone menu

The same six doors, with short lists, each with its main page first:
- **Academy:** The Academy, Online Courses, Access All Areas Pass, Certification, Accreditation.
- **Membership:** Membership, Live Events, Code of Ethics.
- **Knowledge Hub:** Knowledge Hub Home, Latest Articles, Quote Articles, Book Notes, Workbooks, Hub Search. Hub Search goes to the Knowledge Hub's own search. The mock-up used /?s=&ach_in=hub. Confirm the right address for an empty Hub search, and name it in the DONE.
- **Pricing:** one link.
- **About:** About Achology, Student Reviews, Testimonial Videos, The Manifesto.
- **Help:** opens a list on the phone: Help Centre (/help/), Enquiries (/enquiries/). On the computer, Help stays one link.

## Quote Articles, the one name (Kain's "yes")

Change these reader-facing words. Leave code comments as history.
- header.php: the menu card name and the phone link.
- learn-listing.php line 128: "Achology's wise quotes offer deep insights..." becomes "Achology's quote articles offer deep insights...". These are Kain's words from S175; the one name changes, and nothing else does.
- shared-parts.php line 1559: "Browse 'Wise Quotes' and Enlightening Articles" becomes "Browse Quote Articles and Enlightening Articles".
- people-setup.php line 198: Frederick's role becomes "Content Lead for Quote Articles".
- **Not this brief:** the "Achology Wise Quotes" logo on each quote's picture (DSRD 7 section 16.2, the baked cards and images/achology-wise-quotes.webp). It stays as it is (Kain, 20 November 2026: "Yes, keep it"). Do not touch it.

## Fold in

FROM Chat/ANSWER__Tray_Points_Settled_S478, items 1 and 2: the five header.css spaces annotated to DSRD 8 s18.21, and the dead border word at line 470.

## Checks before the DONE

- css_gate on header.css passes.
- Every new address answers 200 on the build site. If one does not, name it, and do not invent a page.
- The phone menu at 375: each list opens and closes, focus is trapped as before, and every tap target is at least 24.
- The computer panels at 1280: Membership's eight cards end level with the community card. Keyboard: each new item is reachable and opens on focus, as the other panels do.

*No em or en dashes in this file; checked before writing.*
