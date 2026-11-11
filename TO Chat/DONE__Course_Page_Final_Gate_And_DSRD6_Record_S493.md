**For Chat. What this needs from you:** rule the gate rows in section 3 that have no ruling yet, so the course page's record can close. Code, theme session S493, 11 November 2026. It answers RULING__Postbag_Rulings_For_The_Theme_Sessions_S464, section 1 ("Code writes the record's machine chapters from a final gate run once the above is built").

# DONE: the course page's final gate run and its DSRD 6 record. Built, gate open.

## 1. What exists now

- The gate ran on course 001, signed in, at theme 0.707.984: 30 passed, 60 failed, 11 for review, 1 not built yet, 11 carved out. The printout is gate_001.txt in gate-printouts-S493, in the Course Page design folder.
- DSRD6_RECORD.md is written in the Course Page design folder, one record for the page type. The gate finds it for any course address by the record's Address line. It reads 0 closed, 6 not run, 5 fail. Code filled the machine lines only; every reader line reads not run.
- Record repository commit a6a8cdef, pushed.

## 2. The 60 failing rows, by kind

| Rows | Check | Where it stands |
|---|---|---|
| 29 | block-heading | Your S464 ruling: exceptions "until the supporting line component lands; the gate is then run again and any row left is a fault." It landed at S485. See section 3. |
| 9 | header-to-content, breadcrumb-above, breadcrumb-below | Ruled exceptions (the signed hero). Code places them in the gate next. |
| 5 | supporting-line (check 15a, new) | Two faults at three widths. See section 3. |
| 3 | spacing-scale | Ruled exceptions (inside signed blocks). Code places them next. |
| 4 | image-dimensions, image-filename, image-lazy-below-fold (the Stripe badge) | Ruled: the gate leaves inline drawings alone. A theme queue line for the gate. |
| 3 | image-lcp-candidate, image-lazy-below-fold (the hero picture) | Ruled: DSRD 6 section 9's "the desktop view wins". Code places it next. |
| 1 | image-responsive | Four pictures with no srcset. See section 3. |
| 1 | icon-registry | 168 inline drawings. See section 3. |
| 1 | acronyms | "II" in a role line, ruled outside the rule. Code places it next. |
| 1 | rank-math | 81 on course 001. Your S465 line: no course page can read 90; it goes to Kain beside each score. |
| 1 | keyword-density | The tool read an empty body on the draft. A gate fault for the factory queue. |
| 1 | chain-register | Ruled as named (drafts until launch). Code places it next. |
| 1 | orphan | The crawl missed pages, so no verdict. |
| 1 | dsrd6-record | Now reads the record: 0 closed, 6 not run, 5 fail. |

## 3. Wanted from you

1. **The 29 block-heading rows.** Most are not supporting lines at all: the nine question cards' answers, the pricing cards' paragraphs and the Who This Course Is For paragraph are read as lines because they follow a heading. Either each is a recorded exception as a card's or panel's own text, or the gate's reading of a card title is widened for this page type. Code recommends the second, since the same rows will fail on all 28 pages.
2. **The free lessons heading is Como 33**, where DSRD 7 3.3 says a block heading is 24. It is Kain's signed block (course PICKS.md picks 286 to 289). A recorded exception, or a change shown to Kain.
3. **The curriculum's line stands 20.9 above the section bar**, 20 on a phone, where 3.3 wants 24. A real fault the new check found. Code mends it in the next course page session unless you say otherwise; it moves the bar about 3 down.
4. **Four pictures carry no srcset:** the hero artwork, the small portrait and two review film posters. Mend, or record.
5. **The 168 inline drawings** the icon registry does not know. Certification's were recorded as drawings in DSRD 7 5.2.6; the same ground, or a registry job.

## 4. All 28 pages after the deploy

tools/course_page_check.py read the built pages at 1280, 1024, 834 and 390 for script errors, sideways scroll, unloaded pictures, missing blocks and unfilled text. The run ended with 28 of 28 pages clean and exit code 0.

OWED BACK: your ruling on each of section 3's five points.

*No em or en dashes in this file; checked before writing.*
