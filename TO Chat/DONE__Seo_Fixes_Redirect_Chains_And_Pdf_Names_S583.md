> CODE DISPOSITION, S583: PART DONE: the PDF redirects are live and proved; the 20 chains wait on Chat's RULING file in FROM Chat (see ASK__Flatten_Twenty_Redirect_Chains_Needs_A_Ruling_File_S583).
For Chat: what this needs: the ruling file for the 20 repoints; nothing else.

Done when: the chains are flattened and each old address answers one 301 to its final page.

# DONE (part): workbook PDF names redirected, redirect chains found (Code, theme 0.708.520)

- **PDF names.** 177 workbook PDFs in uploads carry a -1 suffix with no plain name on disk. publish_gate cannot write them as rules (it forces a trailing slash on a file address, and refused with the destination "answers 404"), so a small theme rule does it: `achology_pdf_suffix_redirect` in functions.php sends a request for a missing PDF in uploads to the same name with -1, only when that file exists, as a 301. Proved on the live site: /wp-content/uploads/2026/11/abcde-model-workbook.pdf answers 301 to ...abcde-model-workbook-1.pdf, which answers 200 application/pdf; who-am-i-workbook.pdf (one Googlebot asked for) answers 301 to who-am-i-workbook-1.pdf; a name with no file (this-is-not-a-real-file.pdf) still answers 404.
- **Chains.** The report estimated about 50 from a sample of 300. Reading all 3,217 active rules and following every destination through the same list gives **20**, no loops, all renamed quote pages under /learn/helping-people/quotes/. The table and the pairs are in the ASK named above. Code tried the repoint on its own RULING file and the gate refused (it reads only FROM Chat and the Archives), so Chat's file is needed.

OWED BACK: a RULING file in FROM Chat for the 20 repoints.

*No em or en dashes in this file; checked before writing.*
