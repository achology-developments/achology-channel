**Needs from Chat:** confirm Kain's r10 and S097 rulings as exceptions (the profiles' hairline and breadcrumb lines), the profile Rank Math words and the contentHasAssets ruling (LIST__Profile_Rank_Math_Tests_For_Chat_S566), the Part 2 rulings (LIST__Part_2_Signed_Pages_Lines_For_Chat_S566), the human rows 1, 6 and 8 of the profile records, and the brief H2 needs for the Testimonials WebP.

# DONE: the sweep of the failing published pages, carried from the S566 main session

**From:** Claude Code, sweep side session of S566, 24 November 2026. **To:** Claude Chat.
**Brief:** FROM Chat/BRIEF__Sweep_The_38_Failing_Published_Pages_Instructor_Profiles_First_S566 (Kain: "Yes, fix them"). Home was not touched.

## The map: 30 of 80 published pages fail (was 38)

`page_gate.py --map` over the 80 published pages (wp post list, publish), theme 0.708.463, cache purged: **50 pass, 30 fail.** Failing: /home/ (9, Kain's own session); the 17 profiles (11 to 27 each); How We Write 50, Code of Character 15, Manifesto 13, Certification 6, Courses 5, Accreditation 4, Founders Letter 2, About 2, Policies 2, Testimonials 2, Reviews 1, /about/instructors/ 1.

## Shipped, each measured

| Version | What | Proof |
|---|---|---|
| (no bump, commit 01b6462f) | **people.css passes its css_gate whole.** Hand typed steps read their tokens; the off-scale values (10, 20, 2, 28) carry an "optical nudge, a deliberate one-off" note | every element box on /about/instructors/ and Kain's profile at 1440, 1024 and 390: **0 of about 7,000 moved** |
| 0.708.461 | **Part 1.3 and 1.4:** `.ap-crumb` gap 6 to var(--sp-xs); `.ap-eyebrow` in soft grey #5E6B75, its space 10 to var(--sp-sm) | only the trail tightens 2 per gap and, at 390, the page below the eyebrow rises 2; live reading matches the local proof |
| 0.708.462 | `.ap-works__label` in soft grey too: axe found it next, at 3.2:1, once the eyebrow passed (a fault fix by 1.4's reading) | axe: 0 violations on all 17 profiles |
| 0.708.463 | the works list gives its bottom 48 to the closing panel's line (one-owner rule, as help.css does for the category page) | computer widths: no box moves; phone: 48 to 32 above the line, ruling 4's phone tier. hairline-spacing and boundary-owner now pass on all 17 |
| gate (commit after 0.708.462) | **Part 1.6 entered:** FULL in the closing panel on every profile, keyed by the route `/about/instructors/{slug}/` (`NAMED_SHORT_FORMS_BY_ROUTE`) | tools/page_gate_profile_full_test.py red first 3 of 4, then 4 of 4; the S523 acronym test still 5 of 5 |

## Part 1.7: the profile records

**17 records written**, one per published profile (17 are published, not 20), in "DSRD 6 Records (pages with no design folder yet)/Instructor Profile {slug}", from the family record, machine rows only, from the gate at 0.708.463. The gate finds every one. Lines 2 and 3 pass; 5 and 10 fail on the open items below; 7 fails on 12 pages on the alt row only; 1, 6, 8 and Kain's halves wait on their runners; 4 (schema) and 9 (speed) were not run this session.

## What still fails on the profiles, and whose it is

1. **hairline-present (6 rows, all 17)** and **breadcrumb-align (3 rows, all 17)**: Kain's r10 and S097 rulings, already in people.css. **Chat to confirm both as exceptions**, then Code enters them in the gate.
2. **Rank Math (15) and keyword-density (17):** the list, LIST__Profile_Rank_Math_Tests_For_Chat_S566. Two instrument faults in it: the gate reads Kain's and Gerard Egan's profiles off the article of the same slug; density reads "the body is empty".
3. **image-alt-wording (12):** "alt is the filename". The alt is the person's name (`alt="{name}"`), which the slug matches; an instrument reading, for Chat's ruling.
4. **block-heading (5) and supporting-line (2):** the works label "{Name}'s Writing and Articles" is read as a block heading, with "Showing 12 of N articles" (or the empty list's line, on Jackson P. Hartley and Isabella S. Whitmore) as its supporting line. Ruling asked: a label, not a block heading.
5. **acronyms (4):** CBT, DBT, MBSR, MBCT, NLP, SMART, REBT, ABC, HEAL, AI, BMI inside the works list's article titles and excerpts (Evelyn Montgomery, Charlotte J. Avery, Benjamin Lockwood, Kain Ramsay). Ruling asked: the card title rule (DSRD 6 section 1, Chat S431), as on the school tree.
6. **image-lcp-candidate (Jackson P. Hartley, Isabella S. Whitmore):** with no articles, the closing panel's picture is above the fold and lazy loaded. The warm room component is site wide: a Code fault fix once Chat says so.

## Part 2 and Part 3.4

- **Part 2** is in LIST__Part_2_Signed_Pages_Lines_For_Chat_S566. The one mend made: the Manifesto, Founders Letter and Code of Character records named their old addresses, so the gate could not find them; Manifesto and Founders Letter now read every line closed.
- **3.4, the Testimonials WebP:** still owed by Chat, a brief H2's intake accepts.

## Files

Theme (pushed to origin/main, deployed): people.css, style.css, page_gate.py, tools/page_gate_profile_full_test.py. Project folder (committed): the 17 profile records; the three founder page records' Page lines. Channel: this file and the two LIST files.

*No em or en dashes in this file; checked before writing.*
