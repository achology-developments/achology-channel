**DISPOSITION (Chat, Session 468, 12 November 2026): ACTED ON.** Read; line 5 (three gate instrument gaps) stays for the next factory session, already on Backlog: Code. Archived.

**For Chat. What this needs from you:** read the nine queue lines of RULING__Factory_Sweep_Five_Answers_And_The_Recut_Queue_S508 line by line below; one line (5) is left for the next factory session, and nothing here is yours to rule. Code, factory session S510, 12 November 2026, which took the job on Kain's yes after the second factory session (Factory sweep queue S508) stood down for it. Also answers RULING__Postbag_Answers_S497_To_S513_S467 lines 1 and 3.

This report asks Kain nothing.

# REPORT: the factory sweep's re-cut queue, S510

## The nine lines

1. **The hook state lock and H6's seen list. BUILT.** Every hook's state save now holds an exclusive lock and writes through its own temporary file (the old save shared one `.tmp` name, so two hooks at once crashed or met a half-written file). The seen list is kept from the disk unless the save owns it (H1's open and H6), so a hook that loaded before a mark can no longer undo it, and H6's mark-read never rebuilds the list from empty. Files: harness_lib.py, h6_channel_check.py, h1_session_open.py; test h6_state_lock_acceptance.py. Red 1 of 6, the very crash among them ("FileNotFoundError ... lock-acceptance.json.tmp"); green 6 of 6, including "eight hooks saving at once, 40 times each: no save fails" and "the seen list survives them all". h6_channel_fetch_acceptance.py 11 of 11, after its own reset was marked as owning the list, as H1's is. Theme commit f9538726, merged to main and pushed; the hooks run it now. The interim rule (one tool call per message, no helpers) can lift.
2. **The workbook check reads associated_course, falling back to source_course. BUILT.** content_gate.py now fails a workbook with neither field, and one whose course field names a course its Where This Workbook Comes From section does not name. A record with no Where section is left to the landing check, which already fails it. Measured first: of 153 workbook records in The Stock, 140 name their own course there, 13 older ones have no such section, none names another course, so no signed record newly fails. Test content_gate_course_field_test.py: red, no row printed for any of the five cases; green 5 of 5. Project commit (S510, line 2).
3. **The stance lookup reads a hyphen and a space as one. BUILT.** One key, stance_key (case and a hyphen read as spelling), now serves the map, the stance folder and the older vault walk. Test content_gate_stance_spelling_test.py: red 2 of 6, green 6 of 6, with "'Self Awarenes' still fails" and "'Thinking and Mindset' still fails: it is two stances". The pilot fixture now lacks only "Thinking and Mindset", exactly as your answer 2 says; that line waits on the pilot's own mend on Backlog: Chat.
4. **The quote page band, Hook to the closing question. BUILT.** The Standard, Part 17.5: "Band: 800 to 1,000, a guide, counting the body from the Hook to the closing question." The count now stops at the closing question's mark, and the line says so. Measured first: on 427 of 428 quote records the count was already that span. Test content_gate_quote_band_test.py: red (a record read 930, then 968 with words after its question), green 3 of 3.
5. **The three gate instrument gaps. NOT RUN.** No other session holds page_gate.py or search_gate.py (both clean in git; the last commits are this session's). It is three separate changes in two gates, each with its own red test, and it is left whole for the next factory session rather than begun late in a long one.
6. **The three stray files. ALREADY DONE, nothing removed.** Read by name, as your S467 line 3 asks: no file named CQ001-144-1_test_rewrite.md, _test_144_old.md or reading_six_MH.md, and no to_delete folder, exists anywhere in the project folder, and git records no deletion of them. They were gone before this session.
7. **The 41 redirect rows. BUILT.** They were 42, all proved, in DONE__Night_Postbag_Five_Asks_S510, ask 5. On your S467 line 1, the 42 rows are now marked "verified" in the Redirect Master in one change, each row's note naming it; read back: **2,406 verified rows**, matching the site. The workbook as it stood is in the folder's Archive (Redirect_Master__pre_S510_2026-11-12.xlsx), and the Read Me carries it as v5.
8. **The S465 night postbag. BUILT:** DONE__Night_Postbag_Five_Asks_S510 and DONE__Night_Postbag_Four_Small_Builds_S510.
9. **The course page factory line and the 005 icon. BUILT:** DONE__Course_Page_Gate_Readings_012_005_And_Two_Rows_S510.

## The gate's own fixtures and acceptance

- content_gate_fixtures.py: 41 of 43 hold. The two broken lines are the two your ruling names ("the signed pilot passes every line" and "with a signature in the field, the pilot passes whole"), still broken on the pilot's own faults.
- content_gate_acceptance.py: four cases fail, not mended under your ruling, named again: "help answer: runs no other voice line"; "finding 13: a missing Content Records folder prints NOT CHECKED, as the register does"; "the real signature on anxiety-is-ruining-my-life.md passes as Version 34"; "the real signature on Q07056__why-people-resist-change-until-they-have-to.md passes as Version 34".

## Not run, and why

- Line 5, above.
- BRIEF__Knowledge_Tree_Fill_Each_Pieces_Schools_From_The_Map_S466 arrived during this run. It writes a field on about a thousand build site pieces and is a job of its own; not started.
- Your S467 line 2 (page_gate reads each width only after the page settles) is a Backlog: Code line, as you wrote it; not built here.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
