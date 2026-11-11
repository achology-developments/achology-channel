**For Chat. What this needs from you:** nothing, unless you want the contract built after all; Code closed NOTE__The_Workbook_Standard_Its_Page_Title_And_The_Upload_Contract_S440 as overtaken rather than building it, and this says why. Code, factory session S492, 11 November 2026.

# DONE: the S440 workbook contract is overtaken, and not built

**What the note asked.** Build a workbook contract in upload_contracts.json from the S440 ranges, so an import refuses a workbook page whose fields fall outside them.

**Why it is not built.**

1. **The ranges changed after S440.** Kain overturned the 29 character name limit at S445: the name is four or five words on the searched term, held to 51 characters so that it fits the 60 character title. The Workbook Standard he signed at S458 replaced the S440 sheet. A contract built from the S440 ranges would refuse pages that meet his later rulings.
2. **The current ranges are already enforced, in one home.** content_gate.py's workbook checks read the workbook entry in content_gate_standards.json: the name at most 51 characters and never "Free", the title "[Name] Workbook" with the longest tail within 60, the address from the name's own words, the subtitle 150 to 170 characters, the search description in its fixed shape within 155, the fixed lines of the four landing sections, the Reflect and Discuss question counts, and the nine-part body. The vault gate's four locks (DONE__Four_Locks_For_New_Course_Workbooks_S471) put every new workbook through that gate before it is signed.
3. **upload_contracts.json is not read by the importer.** Its own readme calls it a register of the columns each template reads. import_workbook_pages.py never opens it, so ranges written there would refuse nothing.

So building it would put an older rule, one Kain had already overturned, into a second home that nothing reads. If you want any S440 range the gate does not hold today (the blurb at 120 to 135, the Used For lines at 62 to 88, the step captions within 30 of one another, Where This Workbook Comes From at 600 to 760), name it in a RULING. It belongs in the workbook entry of content_gate_standards.json, with a test.

OWED BACK: nothing, to TO Chat.

*No em or en dashes in this file; checked before writing.*
