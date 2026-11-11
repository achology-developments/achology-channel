**For Chat. What this needs from you:** rule section 3: whether the course page's speed line takes the site-wide exception the pricing, Certification and Accreditation records carry, or waits for a sound run. Code, theme session S495 (course page), 11 November 2026. Kain, asked whether to run the schema and speed checks: "Yes, run them".

# DONE: the schema check passes on one checker; the speed check ran but its reading is not sound. Built, gate open.

## 1. Schema (chapter 4)

- **The Schema Markup Validator at schema.org,** by its own API, on course 001's two blocks as the built draft prints them: totalNumErrors 0, totalNumWarnings 0. It read a Course and a BreadcrumbList. A draft has no public address, so the two blocks were posted, not the address; nothing else of the page was sent.
- **The fact-match,** labelled against visible on the built page: the name is the same; price 299 USD against "Join this Course for $299"; rating 4.78 from 10,818 against "4.78 (10,818 ratings)"; workload PT51H against "51+ hours of teaching"; the breadcrumb's four steps against the trail shown.
- **Google's Rich Results Test was not run.** It takes a public address, or code pasted into its page by hand; no script can call it. So the chapter still reads not run.

The readings are schema__course_001.json and validator__course_001.json in gate-printouts-S495, in the Course Page design folder.

## 2. Speed (chapter 9)

Lighthouse 13.6.0 on this Mac, phone, simulated slow 4G, course 001, run twice.

| | Run 1 | Run 2 | DSRD 3 section 4.3 |
|---|---|---|---|
| Performance | 66 | 38 | |
| First paint | 2.8 s | 2.9 s | 1.5 s |
| Largest paint | 5.6 s | 6.3 s | 2.0 s |
| Total blocking | 320 ms | 1,780 ms | |
| Layout shift | 0.011 | 0 | |
| Page weight | 814 KB | 814 KB | |
| Accessibility | 100 | 100 | |

**This is not the page's speed.** The page is a draft, so it was read signed in, with WordPress's admin bar in it and no page cache. Three other sessions were running browsers on the machine. The two runs disagree by 28 points. What both agree on: render-blocking style sheets cost about 1.4 s, and 189 KB of style rules are unused. Those are the site-wide causes the pricing page's record names.

The two reports are kept out of the record folder: Lighthouse writes the sign-in cookie into its report.

## 3. Wanted from you

The record's speed line reads fail, with the figures above and the three reasons they are unsound. Either it takes the site-wide speed exception (approved by Kain, S141; blocks only at cutover, S365), as on the three other pages, or it waits for a run on a quiet machine. Code did not choose.

OWED BACK: your ruling on section 3.

*No em or en dashes in this file; checked before writing.*
