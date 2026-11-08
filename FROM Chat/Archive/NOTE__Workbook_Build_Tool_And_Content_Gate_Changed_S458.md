> CODE DISPOSITION, S462: DONE. Read in full; it asks for no work and owes nothing back. The hold on the workbook document build and the workbook page import stays in force under BRIEF__Workbook_Build_Tool_Fill_The_Pages_S458 until Chat sends the word.

**For Code (factory session). What this needs from you:** read it before you next run the workbook build tool or the content gate on a workbook; nothing to build. Chat, Session 458, 8 November 2026.

# NOTE: the workbook build tool and the content gate changed in Session 458

**Why.** Kain found that 21 of the 33 Mindset Mastery workbooks reported on the course ("the course calls this") instead of teaching the subject, and that the workbook layout wasted space. He signed one Workbook Standard for copy, design and spacing (99 Working Papers/reading/session_458_workbook_standard_and_plan.html in The Achology Newsroom folder) and asked that it be enforced by the tools, not trusted. All 86 workbook records are now being rewritten to it in Chat's programme (99 Working Papers/workbook_standard_s458/RUNBOOK__Workbook_Programme_S459.md).

**What changed in 02. The Machine.**
1. content_gate.py, workbook type: new FAILs held on every workbook whatever its date: course or lecture talk outside the fixed Before you begin line; paragraphs over 80 words; sentences over 40 words; no complete ## Scorecard (written_by, checked_by a different worker, read_by_chat, twelve reading rules each PASS with evidence); no ## Pull quotes (one per Learn page, at most 25 words, word for word). The Before you begin check reads the new first line ("This workbook is drawn from a lesson in Achology's course ...") and fails the retired lecture line. Learn page 1 is now 6 to 12 paragraphs. The page title check follows the pack (the longest tail within 60 characters). content_gate_acceptance.py was updated with them; it fails only the four tests that already failed before S458 (help answer voice line, finding 13, two real-signature tests).
2. workbook_build_tool/build_workbook.py is the new design (Mulish body, clean covers, reading column with margin notes, school colour, notes boxes only at section ends, and the rest in the standard). It runs the content gate first and REFUSES any record the gate fails; --review lets only the signature fail. The previous tool is kept beside it as build_workbook__before_S458_design.py.bak. It needs ~/.achology/venv/bin/python, which now has Pillow, pypdf and Playwright with Chromium.

**What it means for you.** Every one of the 86 workbook records now fails the gate until it is rewritten, so the tool will refuse to build them, by design. The hold on the workbook document build in BRIEF__Build the 33 Mindset Mastery workbooks stays: build nothing from Built Workbooks or the records until Chat sends the word that a batch is signed and built. The workbook page import waits the same way.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
