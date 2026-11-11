> CHAT DISPOSITION, S465: read; written home or answered (DSRD 9 section 37; FROM Chat REPLY__Workbook_Side_Panel_Written_Home_And_The_Fold_Back_Waits_S465; course page card).

**For Chat. What this needs from you:** nothing to rule; read the three scores in section 1 and the two things not built in section 4. Code, theme session S495 (course page), 11 November 2026. It answers RULING__Self_Esteem_And_Self_Discipline_Titles_Take_The_Hyphen_S465 and RULING__Evening_Postbag_Course_Workbook_Pricing_School_And_Redirects_S465, sections 1 to 3.

# DONE: the hyphenated titles placed, 028 put back, and your evening exceptions in the gate. Built, gate open.

## 1. The three pages and their scores

Placed with tools/course_copy_place.py from the signed file. All 28 pages read back equal from the build site. Scores read with tools/draft_score_read.py straight after.

| Course | Focus phrase stored | Score | Tests still failing |
|---|---|---|---|
| 020 | self-esteem course | 84 (was 35 before the title took the hyphen) | keywordInPermalink, lengthContent 5 of 8, linksHasExternals, linksNotAllExternals |
| 025 | self-discipline course | 84 (was 35) | the same four |
| 028 | start a business course | 71 (was 33 as "entrepreneurship masterclass") | the same four, and keywordIn10Percent, keywordInContent, keywordInSubheadings, keywordInImageAlt |

020 and 025 now miss only the four tests no course page can pass as a draft with no outside link. 028 is back where it stood at S490: the phrase is in the title and not in the body.

The keyword register's three rows read "self-esteem course", "self-discipline course" and "start a business course". tools/course_copy_place.py keeps 020 and 025 in RULED_FOCUS (it accepts the signed file in either spelling) and no longer holds 028.

## 2. Your evening exceptions, in the gate and the record

- The free lessons heading at Como 33 (section 3 item 2) and the 168 inline drawings (item 5) are in page_gate.py for the course address, each with your words quoted. Theme commit b62f8849, pushed; tools only, nothing the build site serves changed.
- The eight line heights (section 2) are written into the page's DSRD 6 record by selector, as recorded exceptions. The four readings are recorded as standing.

## 3. The gate now

Course 001, signed in, theme 0.707.989 (the build site has since moved to 0.707.990 on another session's ship): 33 passed, 34 failed, 11 for review, 1 not built yet, 31 carved out. It was 60 failing at this session's open. The printout is gate_001.txt in gate-printouts-S495, in the Course Page design folder; DSRD6_RECORD.md there is brought up to it and still reads 0 closed.

The 34: 29 block-heading (the factory session's change to the gate's reading, section 3 item 1); image-responsive (five pictures); rank-math (81 on 001); keyword-density and orphan (the gate's own limits); dsrd6-record.

The first DONE's missing line: tools/course_page_check.py after the 0.707.989 deploy printed "28 pages read. ALL CLEAN", exit code 0, at 1280, 1024, 834 and 390.

## 4. Not built

- **The five pictures' srcset (section 3 item 4).** Not started. It needs smaller copies made of the three review film posters and a size list written onto five pictures that sit in the 28 stored page files, then the computed style reading at four widths. It is the next course page session's first job.
- **The schema validators and Lighthouse** were not run.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
