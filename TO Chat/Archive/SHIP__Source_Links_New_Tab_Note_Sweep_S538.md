DISPOSITION (Chat, Session 478, 20 November 2026): for the record; its flag is the same as the S539 clean-up's. Archived.

**Needs from Chat: nothing for the sweep. One flag for the school page session: its pages read 14 fails each, none from this sweep.**

# SHIP: the source links' hidden new-tab note on eight pages, on 0.708.257 (S538, 19 November 2026)

**What changed.** Every new-tab source link in the story on the seven school pages and the Access All Areas Pass page now carries the hidden note `<span class="screen-reader-text"> (opens in a new tab)</span>` inside the link, as on the Academy at 0.708.256. Nothing anyone sees changed: each link keeps its address, its visible words, `target` and `rel`.

**Why.** Your mend 2 (ANSWER__Academy_Page_History_Gate_Rulings_S538). Kain's word on the sweep was "Yes, all of them", and your sweep brief SWEEP__Source_Links_New_Tab_Note_On_Seven_School_Pages_And_The_Pass_Page_S538 carried it.

**How.** I changed one function, `source()` in `tools/school_page_data.py`, in both its link forms. The Pass page draws its story through that same function. `tools/pass_page_data.py` changed only to keep the note when it renames Open Library links. Before the change, rebuilding all eight pages reproduced their stored data exactly. After it, taking the note out of each file gives back the old file exactly. knowledge-tree.json, which the builder rewrites as it runs, was put back each time and is not in this change. The Academy's data came out the same, byte for byte. Commit 6cfe53dd, deployed from a clean copy and proved current.

## The eight pages

| Page | Links given the note | Read back on the build site | Gate after (0.708.257) |
|---|---|---|---|
| Neuro-Linguistic Programming (NLP) | 9 | 9 of 9 | 43 passed, 14 failed |
| Cognitive Behavioural Psychology (CBP) | 8 | 8 of 8 | 43 passed, 14 failed |
| Person-Centred Counselling and Psychology | 9 | 9 of 9 | 43 passed, 14 failed |
| Life Coaching and Professional Helping | 12 | 12 of 12 | 43 passed, 14 failed |
| Mental Health, Wellness and Emotional Resilience | 12 | 12 of 12 | 43 passed, 14 failed |
| Mindfulness, Applied Insight and Wisdom (MIW) | 9 | 9 of 9 | 43 passed, 14 failed |
| Personal Growth and Development (PGD) | 13 | 13 of 13 | 43 passed, 14 failed |
| The Access All Areas Pass | 13 | 13 of 13 | 42 passed, 1 failed (rank-math: never scored, Kain's one click) |

85 links in all. On the personal growth page, all 13 notes measure 1 by 1 and clipped, and nothing scrolls sideways. No page was refused.

**No new fail from the sweep.** On all eight pages, links-resolve passes (66 to 88, all resolve), axe 4.10.2 reads zero WCAG 2.2 AA violations, and acronyms passes.

**The school pages' 14 fails are not this sweep's.** Each page's last printout (gate-printouts-S530) read 1 fail. The 14 are all headings, lines and pictures:
- Who Should Enrol: 64 to 76 words, three sentences;
- the history lede, 38 to 41 words;
- the knowledge tree line, 36 words, with the 32 under it;
- the practise line, 40 to 43 words, and its school-name capitals;
- "Achology's" and "Membership" as capitals;
- the film still not lazy on tablet and phone;
- the record line.
They follow the school session's heading and line changes earlier today (0.708.244 to 0.708.253, "Kain's fine-tuned headings and supporting lines on all seven"), whose matched exceptions no longer meet the new words. That session owns them. The full printout is in my scratch folder, and I can copy it into the School Page folder if you want it there.

*No em or en dashes in this file; checked before writing.*
