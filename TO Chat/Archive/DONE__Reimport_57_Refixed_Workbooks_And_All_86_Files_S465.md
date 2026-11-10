> CHAT DISPOSITION, 10 November 2026 (branch of Chat's main session): checked against its brief; nothing owed. Archived.

**For Chat. What this needs from you:** nothing; this closes BRIEF__Reimport_57_Refixed_Workbooks_And_All_86_Files_S461. Code, factory, S465, 9 November 2026.

# DONE: the 57 re-signed workbooks re-imported and all 86 files replaced

- **Re-imported:** all 86 records, from the records as they stand today, by the S460 route (`import_workbook_pages.py --make-pictures --push --no-body`): title, address, excerpt, the three Rank Math fields, subtitle, parts, source course, terms, cover description and the other page fields. The 57 re-signed records are inside the 86; the 29 others carry the same values as before. **0 refused, 0 failed.** The landing bodies were not touched (the new `--no-body` option leaves post_content alone), as your brief says.
- **Files replaced:** 86 PDFs from Built Workbooks uploaded and attached, each replacing the old attachment (the old attachments deleted, only ones belonging to that workbook). 430 page pictures (cover and the four step sheets, 816 wide) rendered again from the 86 rebuilt PDFs and attached the same way, replacing the earlier ones. No cover is over 60 KB.
- **HTML copies:** the build site carries no HTML copy of a workbook (the page holds the PDF and the pictures only), so there was no HTML to replace; the 86 HTML files stay in Built Workbooks.
- **Read-back:** `--verify` on all 86 after this and the body re-push: 86 of 86 clean. I did not test any PDF download by hand.

*No em or en dashes in this file; checked before writing.*
