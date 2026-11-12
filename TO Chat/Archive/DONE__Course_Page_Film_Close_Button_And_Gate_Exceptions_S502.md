> CHAT DISPOSITION, S465 side session, point 13 (12 November 2026): DONE: read, nothing owed by Chat; the About page's close button went to Kain through the main session, as section 3 says.

**For Chat. What this needs from you:** nothing for the two jobs; one finding in section 3 is a separate fix on the About page and any shared video lightbox, sent to the main session as a yes or no. Code, theme session S502 (course page), 11 November 2026.

DOCUMENT TYPE: report of finished work. Not a page spec.

# DONE: the film box close button, and the three block-heading exceptions in the gate

## 1. The film box close button (0.708.017, theme commit e7c10854)

Kain's word through the main session, to "Shall I give the film's close button the site's standard look?": "So I'm definitely going to say yes to that". Your call too (RULING__Course_Page_Scores_Free_Lessons_And_Kains_Answers_S465, 1.6): reusing a signed control needs no four options.

- The registered control exists: the Shared Video Lightbox's close button (Component Registry row "Shared video lightbox"; components.css). It was reused, not redrawn: the same class, the site's X icon, the same corner, 8 in from the top and right, 40 across.
- The button family (buttons.css, Ring to Fire, pick 9) then gives it the ring look and the orange focus mark, as it does every icon button. It also sets position relative, which drops the button out of its corner. One course-page.css line keeps the registered corner. Nothing else was added.
- The round: previews/course-film-close-s502, one switch, proved by tools/viewer_proof.py (5 measured, 0 failed). The mirror was left running on port 8305 for anyone who wants to see it.
- On the build site, signed out, with the cookie banner up: on a phone the button sits 338 from the top, well clear of the banner, and a tap closes the film on courses 001 and 018. The point 9 check on 001 then passes every film row by mouse, touch and keyboard.

## 2. The three block-heading exceptions (theme commit d9046650)

Your night ruling, section 1.4. page_gate.py was clean when this session took it.

- The three rows are named exceptions for the course page type and print your ruling: What You Will Learn's 11-word line, and the pricing heading's 39-word, three-sentence line.
- Each is matched on the heading and the count, so a line that changes length fails again.
- Test: tools/page_gate_course_heading_exceptions_test.py, six cases, red first (3 of 6 before the change), 6 of 6 after. The older card-text test still passes 6 of 6.
- The gate on course 001: 34 passed, 4 failed, 8 for review, 1 not built yet, 34 carved out (it read 7 failed). The four left: the record itself, orphan (the instrument limit, with the hand read beside it), rank-math (81) and keyword-density (the instrument limit).

## 3. Found in passing, not touched

On /about/ the shared lightbox's own close button is pushed out of its corner by the same button family rule: it shows half cut off at the film's top left. Any page using the shared video lightbox will show the same. Mending it changes what a reader sees on another page, so it goes to Kain through the main session as one yes or no. The mend is one rule in components.css.

## 4. What is next in this session

Your late ruling's sections 1.2, 1.5 and 2.3: the feed to Rank Math and the 28 scores read again, "1 lesson", and the second course restart.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
