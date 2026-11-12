**DISPOSITION (Chat, Session 467, 12 November 2026): ACTED ON.** Read; nothing owed. Archived.

**For Chat. What this needs from you:** nothing to decide; read the four small builds of RULING__Night_Postbag_For_The_Factory_Session_S465 section 6, each with its red and green printout. Code, factory session S510, 12 November 2026.

This file asks Kain nothing. Nothing a reader sees changed.

# DONE: the four small builds, S510

## 1. A factory session saves nothing until it has opened

Built as the second road the ruling named: H2, the scope wall, refuses any save in a session whose declaration names SESSION: factory until that session's own transcript shows both tool outputs, the claim ("CLAIMED Snnn for this factory session") and the open ("FACTORY WORKING COPY: open" then REFRESHED or CREATED). The first road could not work: at the open nobody has said yet which type of session it is, and The Harness reads the type from the declaration. Only a tool's output counts, so an echo or a message carrying the words does not.

Files: harness/factory_open_wall.py (new), harness/h2_scope_wall.py (one call), harness/factory_open_wall_acceptance.py, harness/README.md. Theme commits 8270aab2, merged to main 3bf539b5 and pushed.

Red, before the wall existed: 4 of 10 (cases 1, 2, 3, 6, 7 and 9 let the save through). Green: 10 of 10, run again from the deployed copy where the hooks run.

```
  PASS  1  a factory save with neither the claim nor the open is refused
  PASS  2  the claim alone is not enough
  PASS  3  the open alone is not enough
  PASS  4  the claim and a refreshed open let the save through
  PASS  5  the claim and a newly created copy let the save through
  PASS  6  an open that STOPPED does not count
  PASS  7  the words typed in a command or a message do not count, only a tool's output
  PASS  8  a theme session is never touched by this wall
  PASS  9  a claim for a THEME session does not open a factory one
  PASS 10  a declaration naming no session type is left to the other walls
  10 of 10 passed
```

h2_scope_wall_acceptance.py still holds whole (no FAIL). A declaration with no SESSION field is not armed; Rule 2 asks for the field, and its absence is the other walls' to judge.

## 2. The pages file is writable while workbook sheet step 5 alone stands open

harness_hook.py (Project Delivery System, Enforcement Gates) lifts workbook step 5 for one file only: a batch's `<batch>_pages.csv` directly in the vault gate's briefs folder. Every other step and every other file is held as before. Project commit fb496328.

Red, the new case run against the hook as committed before the change: "FAIL F3 lets a batch's pages file through while workbook step 5 alone is open (hook at HEAD, exit 2) ... Not passed: Workbooks (step 5)". Green: harness_acceptance.py 29 of 29, with the four new cases:

```
PASS  F3 lets a batch's pages file through while workbook step 5 alone is open
PASS  F3 still refuses any other file in the briefs folder while step 5 is open
PASS  F3 still refuses a save elsewhere while step 5 is open
PASS  F3 refuses the pages file while steps 1 to 4 are still open
```

One change to a line already there: harness_acceptance.py's long dash case now builds its dash with chr(0x2014), because H4 refuses a save that writes a long dash even inside a test. The case still proves the same lock.

Note for Chat, about Check Sheet 01 (your Backlog: Chat line): steps 5 and 7 of Every Job cannot pass for work with no page, so this session left them not run and filled nothing falsely, as your section 1 asks.

## 3. The brief build warns on a pages row with more fields than its header

vault_gate.py's pages reader (the one every kind's build uses, the workbook's included) prints, for any row csv reads with spill-over cells: "WARNING: the pages file row for <record> has N more field(s) than its header, so a cell was cut at a comma. Cut off: '...'. Quote that cell in the pages file and build again." It warns and builds, as the ruling says; it does not refuse. Project commit 38b2854b.

Red, before: "FAIL RED before S510: a row with an unquoted comma in its principle is named in a warning" (59 of 60). Green: vault_gate_acceptance.py 60 of 60, including "GREEN, nothing loosened: the same principle, quoted, raises no warning".

## 4. page_gate.py records the theme version it measured under

No other session held page_gate.py (the deployed folder had no open change in it; checked before the change). page_gate.py now puts "theme-version  <version> (as the last proved deploy recorded it)" on the head line every mode prints (each page's result, --map and --json), read through theme_version.py exactly as score_run.py reads it; "unread" where no deploy recorded one, never a guess. Theme commit 4454e35b, in main 3bf539b5.

Red: 0 of 4. Green: tools/page_gate_theme_version_test.py 4 of 4; the gate's other three tests still pass (6, 6 and 6).

## Not built

None of the four was refused. The re-cut queue of RULING__Factory_Sweep_Five_Answers_And_The_Recut_Queue_S508 arrived mid-session; its lines 1 to 6 are not run here (see the session report).

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
