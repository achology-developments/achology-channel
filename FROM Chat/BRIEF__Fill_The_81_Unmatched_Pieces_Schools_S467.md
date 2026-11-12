> CODE DISPOSITION, S514: WAITS ON the factory session's DONE in TO Chat with the 81 read back and the new per-school totals; read whole by the About, Testimonials and Reviews theme session S514, which is not a factory session and leaves it untouched.

**For Code, factory session. What this needs from you:** fill the schools field on the 81 published pieces the map did not name, from Chat's placement file. Chat, Session 467, 12 November 2026. This job asks Kain nothing; any question goes to Chat's main session through TO Chat.

Done when the 81 pieces carry the schools field, read back from the database with 0 mismatches against the placement file, and the new per-school totals are reported in a DONE in TO Chat.

Model and effort: Sonnet 5.5, low effort. Size: 81 rows, one run of your existing fill script. Kain's yes to running it: "yes" (Session 467, after reading the seven schools' lists page).

# BRIEF: fill the 81 unmatched pieces' schools

Answers section 3 of DONE__Knowledge_Tree_Schools_Field_Filled_From_The_Map_S516.

1. **The file.** MAP__The_81_Unmatched_Pieces_Placed_S467.csv, in the School Page folder (beside MAP__Every_Piece_To_Its_Schools_S466.csv). Columns: slug, kind, schools, placed_by. Schools are full slugs separated by "|", one to three a piece, exactly as in the first map.
2. **The write.** Run the same re-runnable fill from S516 against this file: the `schools` meta as a sorted array of slugs, and the hidden `_schools` field key reference. Nothing else on any piece changes.
3. **If a slug is not found** among published pieces, skip it, name it in the DONE, and write nothing for it.
4. **Read back** all 81 from the database against the file, and report the new per-school and per-kind table in the shape of S516 section 2.
5. **Later fills.** When the seven drafts and the 75 workbooks named in S516 section 5 are published, the same script fills them from the first map; no new brief is needed for that.

*No em or en dashes in this file; checked before writing.*
