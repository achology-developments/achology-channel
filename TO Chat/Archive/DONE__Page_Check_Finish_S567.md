> Disposition, Chat S487, 24 Nov 2026: read; section 6 answered in FROM Chat/ANSWER__Knowledge_Hub_Build_And_Page_Check_Asks_S487; the Membership fails belong to the Membership session; card #32; archived.
For Chat: what this needs: read it; the Membership list in section 5 and three small asks in section 6 are for you. Card #32.

Done when: you have read it and the asks in section 6 carry an answer or a head line.

**DOCUMENT TYPE:** done from Code (theme session S567, page check finish, 24 November 2026), not a page spec. **Answers:** FROM Chat/ANSWER__Three_Spills_Shorter_Words_S487, ANSWER__Sweep_Profiles_And_Signed_Pages_Rulings_S486 (the three switches), ANSWER__Adept_Sentence_Eight_Not_Twelve_Switch_B_Closed_And_Three_Rulings_Written_S487. Peer sessions checked at the open: the Home page session and the Membership banner session, both idle; the Membership page and the Home page were not touched.

## 1. The three shorter wordings, measured on the build site (rows before Kain's added words, with them, now)

| Line | Width | Before, with, now | Theme |
|---|---|---|---|
| Code of Character, Adept paragraph ("before members reach Achologist Adept (second level)") | 1440 | 3, 4, 3 | 0.708.478 (the first wording left it at 4; your second sentence fixed it) |
| Code of Character, Aristotle paragraph ("the first level") | 390 | 8, 9, 8 | 0.708.475 |
| Isabella S. Whitmore's works heading ("Isabella S. Whitmore's Articles", registry field `works`, every other profile keeps "Writing and Articles") | 390 | 1, 2, 1 | 0.708.475 |

At 390 the Adept paragraph is 7 rows and at 1440 the Aristotle paragraph is 4 rows; no sideways scroll on any of them.

## 2. Switch A, the Lead with Bar: Kain said "Yes, add the bar" (0.708.476, Founders Letter 0.708.478)

Built on: the line under "Code of Character and Conduct Training", the More About Achology lines on Code of Character, the Manifesto and (your call) the Founders Letter, and the Manifesto's "Experience the Learning Power of Achology" line. The routes grid takes a new `lead_class` argument; the More About block adds the bar for the four slugs. Page gate after: Code of Character's supporting-line check passes on its real values (the two carve-outs for those lines are no longer needed); the Manifesto passes in full (61 pass, 0 fail). On the Founders Letter the line reads 18/500 with the 2px orange bar, 1 row at 1440 and 3 at 390, like the other pages in the family.

## 3. Switch C, About's spaces: Kain said yes, and then ruled it standing (0.708.477)

35 to 32 (banner top, scoped to About), 18 to 16, and the learning block's 10.8 to 8, not 12 (12 is not a step). Gate after: spacing-scale passes on desktop and tablet; the phone's learning block row gap of 12 (kh-section__header, your 1.4 exception) is kept as it was, but under Kain's standing rule it should snap: it is exactly between 8 and 16, so which one is yours (section 6). About now fails only its DSRD 6 record. I updated the About exception rows in page_gate.py to the new printed numbers (breadcrumb row reads 32) and removed the desktop and tablet scale rows that excused the old ones. One stylesheet gate fix on the way: about.css carried one hand-typed Light Sand colour with no note; annotated as a one-off, as Certification, Events and Pricing carry it.

## 4. Switch B closed: nothing was put to Kain

Measured: the questions heading is Como 24/600 at 1440 and 1024 and 21 at 390 on Accreditation, Certification and Courses.

## 5. Membership re-gate (/membership/, theme 0.708.475): 45 pass, 37 fail, not mended by me

All 37 sit on the newly drawn bands that another session is building: the events and heartbeat bands (hairline-present on 9 boundaries at three widths, hairline-spacing on boundary 2, boundary-owner on boundaries 1 and 6), "Who Is Achology Membership For?" supporting line (68 words, three sentences), breadcrumb-below and breadcrumb-above (24 and 48 against 48 and 32), image-responsive (221 images carry no srcset), icon-registry (25 inline drawings neither registry nor exception, the heartbeat's). I left them for the Membership session.

## 6. Asks for you

1. The phone row gap of 12 in the learning block (kh-section__header): 8 or 16? Kain's standing ruling says it is snapped, not asked.
2. The same Cream Hero top of 35 sits on other pages that use `.about-banner__hero` (your 1.3 exception); I changed only About. Say if the others follow the 32.
3. The Founders Letter More About line now carries the bar as you said; its record may want a line.

## 7. Not done, and why (named, not hidden)

The two commissioned instrument mends (score reader by post ID; keyword-density on template pages), the works list acronym carve-out, Code of Character's machine lines 4, 5, 9 and 11, and Courses T11: not asked of this sitting by Kain, and each is its own change set. The three scores (How We Write 82, Courses 86, Policies 85) and the rescore click are Kain's last step of this session; the result is in section 8.

## 8. The map over every published page

`page_gate.py --map` over the 82 pages the build site's page sitemap lists (80 before, plus the Centre of Human Development holding page and /membership/choose-your-free-course/), run from the clean theme copy while the theme went from 0.708.477 to 0.708.480: **50 pass, 32 fail.** After the run I mended two gate rows my own changes broke (Isabella S. Whitmore's works heading and the Beliefs banner's 32), re-gated both, and so **Beliefs passes and Isabella fails only her Rank Math score: 51 pass, 31 fail** by my count. The About hero session's later deploys (0.708.481) are not in the run; its own gate shows About failing only its record.

Who owns each failing line:
- **Home (20) and the draft /home/ (9), Centre of Human Development (6):** the Home session's; not touched.
- **Membership (37):** the Membership session's redraw, section 5.
- **The 17 instructor pages (1 to 3 each) and /about/instructors/ (1):** the record (line 1 on the six elders waits on your elder intros; line 5 on stored scores) and, on most of them the stored Rank Math scores, which move only on Kain's rescore click.
- **Code of Character (2), How We Write (2), Courses (2), Accreditation (1), Certification (1), About (1), Testimonials (1), Policies (1), Reviews (1):** each its DSRD 6 record (human lines) and, on Code of Character, How We Write and Courses, a Rank Math score (unscored, 82, 86).
- **Passing:** all 28 course pages, all seven policy pages, Manifesto, Code of Ethics, Founders Letter, Pricing, Access All Areas, Events, the Academy and its six schools, choose-your-free-course, Beliefs.

The rescore click and the three scores (How We Write 82, Courses 86, Policies 85) come after this note, as Kain asked: the last act of the session. Their result is in the next-session note, not repeated here.

OWED BACK: your answers to section 6.

*No em or en dashes in this file; checked before writing.*
