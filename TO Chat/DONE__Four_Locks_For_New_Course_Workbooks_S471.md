**For Chat. What this needs from you:** one real final build on a Mac where Google Drive is mounted, to prove lock D live (section 2), and a read of the four notes on the run book (section 4). Code, factory, S471, 10 November 2026. Answers BRIEF__Four_Locks_For_New_Course_Workbooks_S460.

# DONE: the four locks for new course workbooks

**Locks A, B and C are built and proved. Lock D is built and proved against a temporary drive, not on the real one.** Test printout: `vault_gate_acceptance.py` prints "43 of 43 cases pass". Each new case was written first and run red, then the code was written and the same cases run green. No existing lock was loosened: the older cases in that file (copy folders, the logged read, the signed-record edit gap, the SoMAP kind) all still pass.

## 1. The locks, where they live

- **A. Only approved lectures.** `vault_gate.py approve-lectures <batch> --lectures 005-020,005-021 --kain-said "..."` records the list in the titles file with Kain's words (it refuses words that are missing, a code that is not NNN-MMM, and a lesson the lesson master does not hold). `build --kind workbook` then refuses any record whose lecture code, the NNN-MMM that starts the record's name, is not on the list, naming the record; it also refuses new workbooks when no list is recorded. A fix batch in which every title is kept names no new lecture and needs no list, so nothing already built is loosened. Cases: refused with one record off the list, builds with the list complete, refused with no list, still builds when every title is kept.
- **B. A way to start a record.** `vault_gate.py new-record --batch <batch> --lesson 005-020 --session <id>` writes one blank record in the shape of the signed exemplar (005-020 The NLP Anchoring Technique): every section heading and every Page fields row, every value empty except `source_course` and `course_page_url` (read from DSRD 5's catalogue and the course table the publish tool links from, which follows DSRD 1), `source_lecture` (the lecture number and its name from the lesson master) and `cover_image` (the next photograph in turn), with its row added to the rotation list in the same step (order 87, photograph 13 on today's list). The `signed` row is there and empty, because only `sign` writes it. It refuses a session that has not logged its Newsroom read, a lesson not on the approved list, a lesson that already has a record, and, as a fourth, a lesson with no approved title in the titles file, because the approved title names the record. A test shows each refusal, and shows one good record that the content gate reads as a workbook and fails on 24 lines, every one a part of the record that is still empty.
- **C. One sample before the rest.** `vault_gate.py name-sample <batch> --record <name>` writes the sample into the titles file. Until that record is signed, the hook refuses any save into the batch's folders (a writer's folder, a staged folder) for any other record of the batch, and `sign` refuses every record but the sample. The gate's own page briefs are never held back. Cases: a second record staged before the sample is signed is refused; the sample may always be staged; after the sample is signed the second is accepted; `sign` names the sample in its refusal.
- **D. Filing into Drive.** After a final build that passes (no flag, or `--strict` or `--accept-locked`; not a draft, review or trial build), `build_workbook.py` copies the PDF to Achology Library, Achology Course Workbooks, the course's folder, as `NNN-MMM Lesson Name WORKBOOK.pdf`, the colon in the lesson name written as " -", replacing a file of that name. The Drive folders are found by their names under the places Google Drive for desktop mounts. Cases: filed under that name; a rebuild replaces it and leaves one file; where Drive cannot be found it prints "filing skipped" and the build still succeeds; a record with no lesson code in its name is skipped, never guessed.

## 2. What I could not prove

Google Drive for desktop is **not mounted on the Mac this was built on** (no Drive folder under the usual mount points), so no real PDF was filed and I could not compare the file names with the 86 filed at S460. The course's folder name is the lesson master sheet's name without `.csv`, matched ignoring case and punctuation; if that folder does not exist the build makes it and says so. Please check the first live build against the folder as it is in Drive.

## 3. Where the files are

`vault_gate/vault_gate.py`, `vault_gate/vault_gate_acceptance.py` and `workbook_build_tool/build_workbook.py` in the Machine. Those folders, and the run book's, are ignored by the project's git, so there is no commit for them; the record repository's autosave carries them. The run book's section 2 table and section 5 now describe the locks.

## 4. Four notes on the run book

1. It says the Drive is mounted on this Mac; it was not on the Mac I built on (section 2).
2. A record's `source_lecture` field holds the lecture number and sometimes two lectures, with no course number, so lock A reads the lecture code from the record's name (`005-020__workbook__...`), which is where the exemplar carries it.
3. The sample has to be named before `build`, because the titles file is one of the things a built brief is checked against; naming it afterwards makes the brief stale and it must be rebuilt.
4. Step 4's "cover number the next on the rotation list" is the build tool's own rule: the order is the row count plus one and the photograph is the last one plus one, 1 to 37 round again; `new-record` uses the same rule so the two cannot disagree.

OWED BACK: nothing now; one real final build on a Mac with Drive mounted, then a line to TO Chat saying where the file landed.

*No em or en dashes in this file; checked before writing.*
