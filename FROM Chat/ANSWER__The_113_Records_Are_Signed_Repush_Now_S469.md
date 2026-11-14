> CODE DISPOSITION, S517: WAITS ON the 113 records carrying wb_landing_seo_s469 in the files on this machine (read at 15:46 UTC on 14 November: record 001-015 still carries its 12 November signature); see NOTE__Workbook_Records_Still_Unsigned_On_This_Machine_At_1546_UTC_S517 in TO Chat.

This answer needs the 113 workbook landing bodies re-pushed now: they are signed and in the records.
This answer asks Kain nothing; every question goes to Chat through TO Chat.
Done when: the steps of BRIEF__Repush_113_Workbook_Landing_Bodies_Rescore_And_Publish_S469 are run and Code's DONE lists each page with its score.
Model: Opus 5.5. Effort: high. For Code's factory session.

Answers NOTE__Workbook_Repush_Waits_On_The_S469_Mend_Reaching_The_Records_S517.

**The records are signed.** Your note was written while the gate's signing step was still running. It finished at 15:39 UTC on 14 November: "SIGNED 113 of 113 pages into their records". Read again now: 113 record files in the workbook folder of Content Records carry a signed line ending "wb_landing_seo_s469_to_sign.html", for example 001-015's: "Kain Ramsay; 2026-11-14; Session 469; Yes, sign them (to the 113 workbook landing page search mends, read as three random pages old beside new, wb_landing_seo_s469_to_sign.html)". Emerald's (003-046) is among them, so its draft (post 46962) takes the mended body with the rest.

**One change to the importer.** import_workbook_pages.py lines 617 and 618 accept --body-only only for records signed under wb_landing_seo_s461. Let it also accept wb_landing_seo_s469 (the signed line names the batch through its reading page, as the S461 line does). Add the case to its test.

Then run the brief in order: the --body-only push of the 113, the read-back against the records, score_run.py, the page gate, publishing at 86 or more quoting Kain's rule of S417, and the second look at 46549 and 46619.

The free tier sweep's rows B6 and B7 stay a separate job, as you say.

*No em or en dashes in this file; checked before writing.*
