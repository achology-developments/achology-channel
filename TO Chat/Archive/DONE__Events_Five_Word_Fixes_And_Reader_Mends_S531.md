NEEDS FROM CHAT: one ruling, on the week block's line now that it carries Kain's signed second sentence (section 3).

# DONE: the Events page's five signed word fixes, the reader half's mends, and the chapter 1 rulings entered

**For:** Chat. **From:** Code, the Events build side session (S531), 18 November 2026. Answers BRIEF__Events_Page_Five_Signed_Word_Fixes_S475, the reader half in the Events record, and ANSWER__Events_Chapter_One_Copy_Lines_S475. Theme 0.708.179 on the build site.

## 1. The five fixes, read back on /events/ at 1270 and 375

All five were copied from EVENT_TICKET_WORDS_SIGNED_S472.json through tools/events_page_data.py; none was typed in.

1. **Banner, third figure** reads "In Achology Membership, $7 for Your First 30 Days". It sits on one row at 1270, level with the other two. At 375 it takes two rows, and the last row holds 6 words.
2. **The week's line** carries its second sentence. It runs to 2 rows at 1270 (12 words on the last) and 6 rows at 375 (4 words on the last).
3. **The Wiser Woman Project** says "who mentor newer members" on its card line and in its description. The description is 48 words. The ticket's description runs to 5 rows at 1270 (9 on the last) and 9 rows at 375 (5 on the last).
4. **One name for each event.** The kinds cards read "Achologist-Led Community Tutorial" and "Achology Code of Ethics Training". Row 11's Event record (47202) is titled "Code of Character and Conduct Training", and it reads back that way over WP-CLI, in the week and on its ticket. At 375 the longer signed kind name wraps to two rows, so those cards stand 340 tall. Every card in that row is the same height.
5. **The days rule** is built from the Event records, so it stays true when Karen changes an event. Where a kind runs more than once on one day, the days line names the count: "(twice)", "(three times)", or "n times" beyond that.

Nothing runs to a short last line. The two that did at 375 (the third figure and the Wiser ticket) were mended at 0.708.179: the page's entry in no-lone-words.js now covers them, and the ticket evens its description each time it opens.

## 2. The reader half's mends (no visible change)

- **The month's first week** now has a heading, "Week One". It is visually hidden, matching Week Two to Week Four for a screen reader.
- **The closed ticket's empty third-level heading** is hidden until the ticket is filled, so a screen reader no longer announces a blank heading.
- **The breadcrumb's Home link** is now a 24 by 24 target, up from 13 by 13. That is components.css, site-wide. Measured on /events/ and /certification/: only that link's box changed, and nothing on either page moved.
- **The page in the served HTML.** All 13 descriptions, all 13 card lines, and all 8 questions with their answers are in the HTML the server sends, before any script runs.

## 3. The gate, with your rulings entered

Your three chapter 1 rulings are in page_gate.py's table for /events/. Each is matched on its key and its word count, so a changed paragraph fails again:

- **The leads:** the heartbeat lead is 39 words and the kinds lead is 36.
- **The three heartbeat columns:** 30, 34 and 30 words. Column 3 has been 30 since Kain's trim.
- **"Achology's"** in column 1.
- **VALTS** in the title of Help answer 10014.

Two older entries had gone stale, and both are corrected. The facts strip's second boundary no longer carries a state class. The icon line now counts three drawings: the ripples plus the shared heartbeat block's two beats.

Gate on /events/ at 0.708.179: 42 passed, 5 failed, 6 for review, 0 not built yet, 50 carved out (page_gate__events__0.708.179.txt, gate-printouts-S531 in the Events Page folder). The five fails are these:

- **block-heading, the week block's line, two lines, for your ruling.** "A Week Inside the Achology Community": "supporting line is 38 words (want 12 to 25)" and "mid-sentence capitals: Achology's". Both come from Kain's signed second sentence (fix 2). The proposed ground is the same as the leads': a paragraph, not a supporting line; and "Achology's" is the brand's own name. Nothing is entered until you rule.
- **orphan.** The crawl stops on the same 2,219 pages on every run. Each answers 502 through the mirror, while the page itself answers 200 straight from the host. That is a fetch fault of the mirror, not of the pages. Every page's footer links to /events/ (Live Events). Getting this crawl to finish is mirror work, outside this page's build, and is not done.
- **rank-math.** It waits on Kain's one-click rescore.
- **dsrd6-record.** It reads the record, which still holds its chapter 8 blocker (the free sign-up waits on the Kit side and the Zoom links) and its not-run lines (speed, the live page, Kain's eye).

The Events record (DSRD6_RECORD.md, Events Page folder) carries all of the above at 0.708.179.

OWED BACK: your ruling on the week block's line. Code enters it by name and word count, as the others.

*No em or en dashes in this file; checked before writing.*

**Disposition (Chat, 18 November 2026):** read on /events/ at 0.708.184, all five fixes show. Week line ruled in FROM Chat/ANSWER__Events_Week_Line_And_About_Rulings_18Nov. Archived.
