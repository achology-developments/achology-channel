> CODE DISPOSITION, S471: WAITS ON one real final build on a Mac where Google Drive is mounted, to prove lock D live; locks A, B and C and lock D against a temporary drive are DONE and proved (43 of 43 cases), in DONE__Four_Locks_For_New_Course_Workbooks_S471.

**For Code (factory). What this needs from you:** add four locks to the vault gate, and one step to the workbook build tool, so no Claude can write a new course's workbooks outside the standard, then report in TO Chat. Chat, Session 460, 10 November 2026, on Kain's "Yes, brief Code".

## Why

Kain: "these workbooks must all be written to the exact standards that we've already defined, and you can't just be going off doing your own thing again." The 86 signed workbooks are the floor. The road for a new course is written in `RUNBOOK__New_Course_Workbooks_S460.md` (04. The Achology Newsroom, 99 Working Papers, workbook_standard_s458). Read it whole first; its section 2 is the twelve steps and its section 5 names the four gaps below. Eight of the twelve steps are already locked by `vault_gate.py`, `content_gate.py` and `build_workbook.py`. Four are not.

## The four locks

**A. Only approved lectures.** The workbook titles file (`<batch>_TITLES.json`) gains an approved lecture list, recorded with Kain's words like the titles. `build --kind workbook` refuses any record whose source lecture is not on that list. Done when: a test builds a batch with one record off the list and the build refuses it, naming the record; the same batch with the list passes.

**B. A proper way to start a new workbook's record.** Today `build` sets aside any page with no record, and the hook refuses any save into Content Records for a page no true batch covers, so a new course cannot start inside the gate at all. Add `vault_gate.py new-record --batch <batch> --lesson <NNN-MMM>`: it writes one blank record in the signed exemplar's shape (005-020 The NLP Anchoring Technique: every section heading and every Page fields row, values empty except source_course, source_lecture and course_page_url read from DSRD 5 and DSRD 1, and cover_image the next number on the rotation list, its row added in the same step). It refuses a lesson that is not on the approved list (lock A), a lesson that already has a record, and any session that has not logged its Newsroom read. Done when: tests show each of the three refusals and one good record that the content gate reads as a workbook and fails only on its empty fields.

**C. One sample before the rest.** The titles file names one sample record. Until that record is signed, the hook refuses a save into the batch's staged folder for any other record of the batch, and `sign` refuses any other record of the batch. Done when: a test stages a second record before the sample is signed and is refused; after the sample is signed, the second is accepted.

**D. Filing into Drive.** After a final build (no flag, or `--strict`) that passes, `build_workbook.py` copies the PDF to the shared drive Achology Library, folder Achology Course Workbooks, the course's folder (named as the course's CSV in the lesson master), named `NNN-MMM <Lesson Name> WORKBOOK.pdf`, the lesson name read from the lesson master with a colon written as " -", and replaces a file of that name. The Drive is mounted on this Mac by Google Drive for desktop under the manager@achology.com account; find the folder by its name, never a written path (standing rule 24). If the folder cannot be found, the build still succeeds and prints that the filing was skipped. Done when: one final build files its PDF there, and a rebuild replaces it rather than adding a second copy. The 86 already filed there at S460 match this naming.

## Constraints

- Standard library only in `vault_gate.py`, as now.
- No existing lock is loosened. `vault_gate_acceptance.py` and `content_gate_acceptance.py` pass as before, plus the new tests, each written red first, then green.
- Nothing in Content Records is changed by this job except by the tests' own throwaway records, removed after.
- Report in TO Chat: the four locks, the tests, and one line on anything in the run book that turned out wrong when you built them.

*No em or en dashes in this file; checked before writing.*
