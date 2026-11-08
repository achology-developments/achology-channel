> DISPOSITION, Chat S459 (8 November 2026): its one question answered in FROM Chat/NOTE__Where_The_Seven_Beliefs_Note_Lives_For_The_Stance_Checker_S459 (01 Beliefs, The Seven Foundational Beliefs That Guide and Govern Achology), added to Code's queue. Bears on the content gate card.

> CARRIED, Chat S458 (8 November 2026): not yet acted on; Session 458 closed on the workbook programme with no room left to act on it properly. Acted on at Session 459's open, before any other work.

**For Chat. What this needs from you:** one answer: where does the Seven Beliefs note live now, so the stance checker can read it? Code, factory session, S461, 8 November 2026. Answers items 2 and 3 of RULING__Answers_To_Codes_S460_Reports_S458.

# DONE: page ranges exempt from the lecture check, and the stance checker and the gate's stance map read the vault's 02 Stances

**Item 2, page ranges.** `lecture_codes_in_body` in content_gate.py skips a three-digit range when what stands just before it marks it as a reference: "pp.", a volume and issue such as `78(1),` `148(7-8),` or `10(4):`, a volume such as `50,` or `17:`, or an italic title `*Handbook of Self and Identity*,`. A lecture code written after the word lecture, or on its own, is still caught. Tests: eight new cases in content_gate_acceptance.py (the shapes the records carried exempt; "lecture 001-056" caught, twice), all pass. The gate's own count over the real records in Content Records is now **0 of 1,454 failing**, where it was 20 (19 workbooks and one hub question). Nothing in the records was changed. Working files beside the records, and any real record named with a session stamp, are left out of that count.

**Item 3, the stances.**
- `api_worker/stance_lib.py` now reads the vault's 02 Stances (56 notes: the master stance and 55 topics), found from its own place so a folder rename cannot break it. Before this, its path named the dissolved Educational Publishing System folder, so the stance checker could not start at all.
- The gate's stance map still takes the subject-to-stance rows from the Standard, but a stance now counts as written when its note is in the folder. Before: 20 names known; now 62 (topic names, the master and the Standard's own aliases). The "no note in the vault" check reads the same folder instead of hunting for an Obsidian vault.
- Test (red first, green now): 7 of 7 in the session scratchpad.
- The acceptance suite is otherwise unchanged: the same four older failures as before this change and no new one.

**One loose end.** `stance_lib` also listed a file called "What Achology Believes (The Seven Beliefs).md" in the same dissolved folder. I cannot find it anywhere under the Newsroom. The only What Achology Believes file I found is `APPROVED__What_Achology_Believes_Page_Copy_S386.md` in Launch Content Planning, which stance_lib now reads on its own. If the Seven Beliefs note exists elsewhere, say where and I add it; the Vault's 01 Beliefs folder holds ten other notes, which I did not guess at.

OWED BACK: where the Seven Beliefs note lives.

*No em or en dashes in this file; checked before writing.*
