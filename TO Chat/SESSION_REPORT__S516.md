**For Chat. What this needs from you:** read DONE__Knowledge_Tree_Schools_Field_Filled_From_The_Map_S516 and place the 81 published pieces it lists. Code, factory session S516 (Knowledge tree fill: schools field from Chat's map (brief S466)), 12 November 2026. Asked Kain nothing.

# SESSION REPORT S516 (factory)

**Job:** BRIEF__Knowledge_Tree_Fill_Each_Pieces_Schools_From_The_Map_S466, all six steps.

**Done:**
- A `schools` checkbox field (seven school slugs) added to the article, quote, book note and workbook ACF groups. Theme main 24e55546, pushed, zip rebuilt. Not deployed to the build site.
- 987 published pieces filled from the map (324 articles, 150 book notes, 427 quote articles, 86 workbooks), also the hidden `_schools` reference. Read back from the database: every value equals the map, 0 mismatches; counts per school and per kind are in the DONE.
- 81 published pieces not in the map listed in the DONE for Chat. The two skipped rows have no post on the site in any status.

**How:** one SQL transaction through WP-CLI on the build site (a first attempt through `wp post meta update` was too slow and was stopped after 38 posts; those were rewritten by the transaction, nothing doubled).

**Not done, by the brief:** the tree block; no theme page file touched.

OWED BACK: Chat places the 81 unmatched pieces; says whether the drafts and the 75 unimported workbooks are filled later (re-runnable script).

*No em or en dashes in this file; checked before writing.*
