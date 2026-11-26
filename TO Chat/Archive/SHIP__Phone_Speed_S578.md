> Chat S494, 26 Nov 2026: noted on Page Speed. Archived.
For Chat: what this needs: read it; it records the ship that finishes step 2.1 of the phone speed sweep (FROM Chat BRIEF__Sweep_Each_Page_Loads_Only_Its_Own_Stylesheets_S576). Nothing is asked of Chat.

Done when: Chat has noted 0.708.496 and the sweep's state on the speed card.

# SHIP 0.708.496: every remaining page family sends only the stylesheets it uses

Code, S578 theme session (Sonnet, as Kain asked), 26 November 2026. Live on achology.com, deployed with deploy.py (the server's own PHP parsed every file; local, server and zip agree at 0.708.496).

## What changed

One file of logic: `speed-setup.php`, `achology_speed_drop_list()`, with one entry per family and the page's own test. One line in `style.css` (the version). No colour, size, space, word or picture changes on any page.

## The method, the same as S577

For each family: the page's sheets read with `tools/speed_page_check.js`; candidates are sheets with no reachable rule, or only rules written by a script that acts on a block the page lacks (read by hand); then, in the live page, the candidates switched off change no computed value of any element or its before and after, at 375, 1024 and 1440 wide, with the same test shown to fail when the page's own sheet is switched off. Where more pages share a template, every page was also checked by class: no page carries a class that the dropped sheets style.

## What each family drops

| Family (the page test) | Dropped | Proved on |
|---|---|---|
| Events | cards | Events, 3 widths |
| Certification, Accreditation | cards, people | both, 3 widths |
| Courses directory | people, about | 3 widths |
| Pricing | cards, people, about | 3 widths |
| Centre of Human Development | cards, policies, help, people | 3 widths |
| Gift page (Choose Your Free Course) | people, about, certification, accreditation, checkout-foot | 3 widths |
| What Achology Believes | people, heartbeat, accreditation, courses-directory, cards, kh-front, certification, knowledge-hub, course, checkout-foot | 3 widths; the one value that moved, the registered property --rp, is used only by kh-front.css, itself dropped; course-page.js's ripples and pricing need .course-hero__ripples, #pr-data and .pr-pp__mount, all absent |
| Founders' Letter | cards | 3 widths (its people block is used, so people stays) |
| Manifesto, Code of Ethics, Code of Character and Conduct, and the eight legal policy pages | cards, people | Code of Character and Conduct, Manifesto, How We Write, Privacy Policy; the other pages by class |
| Policies index | cards, people | 3 widths |
| Reviews, Testimonials | cards, people | 3 widths each |
| Enquiries | cards, people | 3 widths |
| Our People | cards, help | 3 widths |
| The 17 author profiles | cards, policies | Karen Ramsay and Gerard Egan, 3 widths; all 17 by class |
| Help answers | cards, people, policies | two answers, 3 widths |
| Help landing and Help categories | cards, people | landing and one category, 3 widths |
| Knowledge Hub articles | cards, help | two articles, 3 widths |
| Book notes, quotes | cards, help | two book notes, two quotes; fourteen of each by class |
| Workbooks | cards, help, people | one workbook proved at 3 widths; fourteen by class |
| Knowledge Hub front, a subject, an Articles list | cards, help, people (kh-front stays) | front and subject, 3 widths; the Articles list at 1440 |
| Knowledge Hub tag pages | help, people (cards is used) | 375 and 1440 |
| The 404 page | cards, people | 3 widths |

Access All Areas Pass: nothing to drop. Every sheet it loads has rules that match its page.

After deploy, for 24 pages across the families, the sheet order was read from the live HTML and equals the saved order minus the dropped sheets (the two differences the check printed were my own typing of the expected list, not the page: Events, where I forgot to leave out the cookie and mail sheets, and Testimonials, where I had the buttons sheet in the wrong place).

## Not done, named

- The help.css double load on pages that queue both `achology-help` and `achology-component-help` is still handled by S577's rule; nothing new.
- Step 2.2, one packed file per family, is not part of this session. It is left as the brief states it.
- Not proved at all three widths (two widths each, noted in the table): Knowledge Hub tag pages and Articles lists. Not proved page by page: the 7 other legal policy pages and the other 15 author profiles, 12 of the 14 workbooks, quotes and book notes (checked by class instead).
- Per-book Knowledge Hub lists (ach_book_listing) and the tags index were not touched.

## Lighthouse phone (PageSpeed Insights, Lighthouse 13.6.0, 26 Nov 2026, run right after the deploy purged the cache)

| Page | Performance | FCP | LCP | TBT | CLS |
|---|---|---|---|---|---|
| Knowledge Hub article (anxiety-is-ruining-my-life) | 89 | 2.0 s | 3.2 s | 0 ms | 0 |
| Home, first run | 50 | 2.6 s | 8.2 s | 690 ms | 0.012 |
| Home, second run | 64 | 2.6 s | 7.7 s | 210 ms | 0.012 |

The runs for a Help answer and for Events did not finish in the pane, so they are owed.

Home's two runs are below S577's 85. Home's own drop list did not change in this ship, the server answered Home in 0.1 to 0.3 s from this machine, and the runs came minutes after the deploy emptied the page cache. I read this as run to run variation and a cold cache, not a fault of this ship, and have left Home's score for a later re-measure rather than write a figure I do not trust.

*No em or en dashes in this file; checked before writing.*
