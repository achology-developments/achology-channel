DISPOSITION (Chat, Session 478, 20 November 2026): for the record; its flag is the same as the S539 clean-up's. Archived.

**Needs from Chat: nothing for this sweep. One flag: the seven school pages read 24 new line-bar fails from the school colours work, not from this sweep.**

# SHIP: the school story's figures under the heading, nine pages, on 0.708.263 (S538, 20 November 2026)

**What changed.** Commit 8613481b, version 0.708.263, deployed and proved current.
- `school-page.css`: the base `#school-story .sps-figs dt` goes from --text-28 to --text-21, and its phone rule from --text-24 to --text-18. Weight 700 (from the school layout's rule), line height and colour are unchanged. The school layout rule under `main.school-page` sets no size, so the base rule is the one that wins on every page.
- `academy.css`: your ruling on the Academy's phone chapter names, `.sps-ch__name` at --text-18 below 768, on the Academy only.

**Why.** Kain chose "Option 1" in the Change Viewer round (previews/academy-page-s527/round-figures.js, proved 11 of 11), following your ANSWER__School_Story_Figures_Against_The_Heading_S538 and the sweep brief SWEEP__School_Story_Figures_Under_The_Heading_S538.

**Measured on the build site, figures and chapter names, each read from inside the page:**

| Page | 1440 | 768 | 390 |
|---|---|---|---|
| /academy/ | 21/700 | 21/700 | 18/700 (chapter names 18/600) |
| /access-all-areas/ | 21/700 | 21/700 | 18/700 |
| NLP | 21/700 | 21/700 | 18/700 |
| CBP | 21/700 | 21/700 | 18/700 |
| Person-Centred | 21/700 | 21/700 | 18/700 |
| Life Coaching | 21/700 | 21/700 | 18/700 |
| Mental Health | 21/700 | 21/700 | 18/700 |
| MIW | 21/700 | 21/700 | 18/700 |
| PGD | 21/700 | 21/700 | 18/700 |

- On all nine, at every width, nothing in the story stands at or above its heading.
- The labels (`dd`) stay 14, and nothing scrolls sideways.
- On a phone the figures stand two over one, centred, as before. Mental Health at 390 now fits all three on one row, its labels being shorter: one even row, not ragged.
- The Academy at 320 reads the same as at 390.

**The Academy's phone chapter names, on their own line (your call, Kain may overturn):** 21/600 became 18/600 at 390 and 320, under the 21 heading. Nothing else on the page moved.

**The gate after, all nine pages:**
- /academy/: 48 passed, 0 failed.
- /access-all-areas/: 43 passed, 0 failed.
- The seven school pages: 42 or 43 passed, 38 or 39 failed each. None of these fails is the story's figures or chapter names.
  - 24 per page are new since 19 November: "line-bar ... not the orange token" on every supporting line, at three widths. The school pages' bars now wear each school's own colour, from the school colours work shipped since (0.708.260 and after). The gate wants the orange. That is a ruling for you and an instrument row for whoever owns the school colours, not a fault of this sweep.
  - The other 14 are the same as on 19 November (SHIP__Source_Links_New_Tab_Note_Sweep_S538): the headings' and lines' word counts and capitals, the knowledge tree's 32, the film still not lazy, and the record line. They are the school session's.

**For the school clean-up session:** it holds school-page.css in its branch and has merged 8613481b (its merge commit ace843cc), so its deploy keeps 21 and 18.

No page was refused.

*No em or en dashes in this file; checked before writing.*
