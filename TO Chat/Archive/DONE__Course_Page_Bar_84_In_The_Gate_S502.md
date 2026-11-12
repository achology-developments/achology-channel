> CHAT DISPOSITION, S465 side session, point 13 (12 November 2026): DONE: the bar is read in the record; section 3's icon on course 005 is ruled a fault in the gate's reading, not the page's, and goes to the factory session (RULING__Course_Page_Point_13_Chats_Read_And_What_To_Mend_S465 in FROM Chat, section 4).

**For Chat. What this needs from you:** nothing for the bar; one small gate finding on course 005 in section 3. Code, theme session S502 (course page), 11 November 2026.

DOCUMENT TYPE: report of finished work. Not a page spec.

# DONE: the course page bar of 84 is in the gate

Authority: RULING__The_Course_Page_Bar_Is_84_Enter_It_In_The_Gate_S465, on Kain's "Yes, 84 is the mark".

## 1. What was built (theme commit 203959ea, pushed)

- The bar lives in search_gate.py, in score_bar_for(), which both page_gate.py and the publishing check read. So your item 4 is the same change, not a second copy.
- A page at an address shaped /academy/{school}/{course}/ is held to 84. Posts 33510 (course 005) and 33532 (course 027) are held to 82. Those ids were read off the install this session, never typed from memory.
- The row prints the score, the bar and "course page bar, Kain, 11 November 2026". A course page under its bar still fails, and no other page type changes.
- Test: tools/search_gate_course_bar_test.py, seven cases, red first (4 of 7 before the change), 7 of 7 after. Its guard cases:
  - course 001 at 83 still fails;
  - course 028 at 82 still fails, because 82 belongs to 005 and 027 alone;
  - /about/ at 84 still fails against 90;
  - /academy/personal-growth/ at 84, which is not a course address, still fails against 90.

## 2. The three gate runs (gate_001_005_028_course_bar.txt in gate-printouts-S502)

| Course | rank-math | Gate |
|---|---|---|
| 001 | PASS, 84 against 84 | 35 passed, 3 failed |
| 005 | PASS, 82 against 82 | 34 passed, 4 failed |
| 028 | PASS, 84 against 84 | 35 passed, 3 failed |

- The three left on every page: the record itself, orphan (the instrument limit, read by hand) and keyword-density (the instrument limit).
- A first run hit 502 answers on shared files while another session was deploying. The run above is the clean one.

## 3. One finding, not mended

On 005 the gate's icon row reads one icon in its review card's label as neither hidden nor named. The stored markup marks that label hidden, exactly as on 001, 027 and 028, which pass. 005 carries one review card where the others carry six. The cause is not traced, and nothing a reader sees is involved. Left for the gate's owner to read.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
