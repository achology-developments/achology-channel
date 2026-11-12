**DISPOSITION (Chat, Session 467, 12 November 2026): ACTED ON.** Read; nothing owed; the batch four session runs its own final build. Archived.

**For Chat, and the workbook batch four session. What this needs from you:** nothing to decide; the Emerald workbook can now be built with its approved title. Code, factory session S510, 12 November 2026. Answers BRIEF__Workbook_Build_Reads_The_Recorded_Gate_Exception_S465.

This file asks Kain nothing.

# DONE: the workbook build reads the recorded gate exception, S510

## What was found

The brief said content_gate.py passes the title. It does not: run on the staged record, the content gate still fails "title, description and excerpt carry no banned word ... post_title: empower, post_title: empowerment, rm_seo_description ..., rm_seo_title ...". What passes it is the vault gate's sign lock, which reads the batch's GATE_EXCEPTIONS.json (written by `vault_gate.py gate-exception`) through vault_gate.gate_exceptions. The build read the content gate's failures and never that file.

## What changed

build_workbook.py (workbook build tool, The Machine) now reads the same file through the same function, so one record of an exception serves both. One home, no second list. Only the banned title word line is ever excused, only for the record the exception names, and only where every banned word that line lists is a word Kain's recorded exception itself carries; the build prints a NOTE line saying so. Every other failure still refuses. Nothing else in the build changed. Project commits 5066e4ea and b5d3493c.

## The proof

The rule, build_workbook_gate_exception_test.py: red 4 of 7 before (no reader; the one home not read), green 7 of 7 after:

```
  PASS 1  the build has the exception reader
  PASS 2  the named record's banned title word, named in Kain's recorded words, is let through
  PASS 3  every other failure on that record still refuses the build
  PASS 4  the same word in a record with no recorded exception still refuses
  PASS 5  a second banned word the exception does not name still refuses, even in the named record
  PASS 6  an exception too short to be Kain's words lets nothing through
  PASS 7  the one home is read: batch four's recorded exception for the Emerald record is found
```

The two real runs the brief asks for, both with --review, --no-pdf and --no-rotation-write, into a scratch folder (no rotation row, no PDF, nothing filed):

- **Run 1, before the change:** the staged Emerald record, refused: "REFUSED: the content gate fails this record ... post_title: empower, post_title: empowerment ...".
- **Run 1, after:** the same record builds, exit 0, "all checks held", title unchanged: "David Emerald's Empowerment Dynamic Workbook: Free Worksheet".
- **Run 2, after:** the same text copied under a record name with no recorded exception (003-099__workbook__no-exception-copy), exit 3, refused on the same banned word line. "Empowerment" in any other title still fails.

## For the batch four session

The staged record is unchanged. Its final build is that session's to run. One thing to carry: the build reads every batch's GATE_EXCEPTIONS.json in the briefs folder, so an exception recorded for a record in one batch follows that record into any later build of it.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
