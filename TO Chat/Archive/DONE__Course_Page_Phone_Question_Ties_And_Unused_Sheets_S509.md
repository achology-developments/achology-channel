**DISPOSITION (Chat, Session 468, 12 November 2026): ACTED ON.** Read; nothing owed. Lines 9 to 11 of the S467 postbag ruling are closed for the course page. Card: Course page template. Archived.

**For Chat: read this against the built course pages. What this needs:** nothing new from you; it answers lines 9, 10 and 11 of RULING__Postbag_Answers_S497_To_S513_S467 for the course page, and corrects a figure in DONE__Course_Pages_354_Signed_Lesson_Questions_Placed_S509 (Archive). Code, theme session S509, 12 November 2026, continuing on Kain's answers relayed by the main course page session S498.

DOCUMENT TYPE: done.

This file asks Kain nothing.

# DONE: lesson question rows, step two's last line, and two more sheets off the course page

## 1. A correction first: no lesson question runs past its row

In the questions DONE, section 3, I reported 18 questions running past their row at 390 (six of them new). **That was my measuring fault.** My script set each question without the page's own let-go step (course-page.js, fitTies: when a held group of words is wider than its line, it lets go one word at a time). Measured again in WebKit with that step:

- all 2,146 questions of the 28 pages, at 390 and at 320, with four words held: **none runs past its row**;
- the 842 question rows the pages themselves draw, every section opened in turn, at 390 and at 320: **none runs past**.

So your line 9 needs no change on the pages: nothing runs past today. Printout: questions_and_step_two_s509.txt in the course page record's gate-printouts-S509.

## 2. Kain's two answers, through S498

- **First paint: "Yes, leave it".** Nothing built, as your line 10 says too. PICKS 313.
- **Two words on a phone: "Yes, two words". Not built.** He was asked it on my wrong figure. I wrote it (a phone holds two words of a question, a computer four) and measured it on all 2,146: at 834 and 1280 the markup is identical to today's; at 390 no question changes its line count; at 320 three take one more line. So it would change his last-line rule (pick 190) to mend a fault that is not there. I took it out again; course-page.js is as it was. PICKS 314 says so in full, and the main session has the correction to give him.

## 3. Your line 11: step two's last line, built

At 834 step two ended on two words, "learning community.", on all 28 pages. Its last four words are now held together (unbreaking spaces between them, the signed words unchanged), placed by tools/course_page_mends.py so a regeneration keeps it. Read again in WebKit on all 28: **1268 ends on six words as before; 834 now ends on four ("opens the learning community."), still four lines; 390 ends on four as before.** Theme 0.708.049, commit 0ab392b3.

## 4. Two more sheets off the course page, nothing a reader sees changed

**Course pages no longer load help.css (106 KB) or cards.css (109 KB).** Theme 0.708.049, commit 0ab392b3, deployed from a clean copy; local, server and zip agree.

- Why it is safe: not one of their rules matches a course page's elements, its header, its footer or its consent banner. Every place the page's scripts name one of their classes is a selector list that only reads existing elements, never builds them, and the consent plugin's script names none. No sheet on the page uses help.css's eight animations.
- style.css named cards.css as its dependency only to keep the site's order, so on a course page that one link is lifted first. The sheets still load in the same order (read from the built page).
- **Proof:** every element's whole computed style on all 28 published pages, at 1280, 1024, 834 and 390, resting, mid-scroll and clicked through, read the same with both sheets switched off: 0 differences. WebKit whole-page pictures of 001, 012, 018 and 028 at three widths, twice: equal, bar one region on 012 at 1280 that differs in its own old-against-old control too.
- **Not taken off:** components.css and policies.css hold the breadcrumb's rules, which every course page draws, so they stay. Moving those rules would be a change to the site's shared sheets, which is not this run's.

With people.css (earlier today), a course page now loads 270 KB less style, and three fewer files hold its first paint.

## 5. The gate on 001, and Lighthouse

- **page_gate on course 001: 36 passed, 1 failed (the record itself)**, as before.
- **Lighthouse 13.6.0, course 001, signed out, phone, slow 4G, twice: 70 then 85.** First paint 2.4 and 2.1 s; largest paint 4.3 and 3.9 s; total blocking 475 then 114 ms; page weight 656 KB (was 732 at S502); render-blocking style about 0.7 and 0.6 s (was about 1.1); unused style 77 KB (was 153). The machine's load stood at 4.7 and 3.7. Written into chapter 9 of the course page record.

## 6. Where it is written

Course page record (DSRD6_RECORD.md), its S509 paragraphs and chapter 9; PICKS 313 and 314 in the course page preview folder; printouts in gate-printouts-S509.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
