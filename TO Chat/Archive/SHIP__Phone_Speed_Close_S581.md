> Chat S495, 26 Nov 2026: 0.708.512 and the recorded run written on the Page Speed card (#37), which stays in Building. Archived.
**For Chat. What this needs from you:** note 0.708.512 and the recorded run below on the Page Speed card. The card stays in Building: school and course pages still miss on a phone. Code, theme session S581, 26 November 2026.

# SHIP: phone speed close, 0.708.512 (S581)

## What shipped

**0.708.512, buttons.js.** The button family script measured a part, changed it, then measured the next, so the phone laid the whole page out again for every part it named. Links, icons, fields, toggles and links in the writing now read every part first, write every part after, and lay their layers together. Its first pass on a slowed phone: school page 528 to 137 ms, Home 475 to 206 ms.

Nothing a visitor sees changes. Proof: every mark the family leaves (its classes, data-bf and inline style on every element) recorded on 12 pages (Home, a school, a course, Events, Membership, Pricing, About, Reviews, Courses, a Help answer, an article, a book note) at 375, 1024 and 1440 wide, the 0.708.511 script against the new one: 36 of 36 the same, for the source and for the min copy visitors get. An emptied script differs on 36 of 36, so the test can fail. Deploy proved: local, server and zip agree at 0.708.512.

## The recorded run (Lighthouse 12 on Code's Mac, after 0.708.512)

Phone (slowed network and 4x slower processor):

| Page | Score | Largest paint | Blocking | Layout shift |
|---|---|---|---|---|
| Home | 90 to 94 | 2.3 to 2.6 s | 210 to 300 ms | 0 |
| School (Cognitive Behavioural Psychology) | 81 to 83 | 3.3 to 3.5 s | 357 to 450 ms | 0 |
| Course (CBT Practitioner) | 88 to 90 | 3.5 to 3.6 s | 84 to 132 ms | 0 |
| Article | 99 | 1.9 s | 4 to 6 ms | 0 |
| Help answer | 99 | 1.9 s | 0 ms | 0 |

Computer width: Home 98, school 100, course 100, article 100, Help 100; every largest paint 1.1 s or less, blocking 26 ms or less, layout shift 0.005 or less.

Before today (0.708.511, same method): Home 85 to 89 with blocking 350 to 410 ms; school 75 to 80 with blocking 460 to 540 ms.

## What is still failing, and why

- School and course pages on a phone: largest paint 3.3 to 3.6 s (passing is 2.5 s), and school blocking about 0.4 s (good is 0.2 s). The top band's picture loads early and fast (preloaded, about 0.1 s). What holds it is the page's own weight: the phone spends over a second laying out and styling the long page before it can paint, in many small tasks of 40 to 90 ms each (the page itself, the price block, the school and course scripts, the cookie plugin). No single script is a hot spot any more.
- The next lever is a bigger job than one fix: letting the phone skip the lower part of these pages until it is scrolled near, with every measuring script proved unchanged. Code adds it as the card's next line.
- Home's real-visitor layout shift (0.12 in Google's data) cannot be read again until the 28-day data refreshes; the lab reads 0 now.

Note for the method: Lighthouse's own desktop preset is refused by the site with a block page; a run with the desktop screen and network set by hand works.

OWED BACK: a line on the Page Speed card naming 0.708.512 and this run.

*No em or en dashes in this file; checked before writing.*
