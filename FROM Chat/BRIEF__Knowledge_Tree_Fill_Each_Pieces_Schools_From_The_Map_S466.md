> CODE DISPOSITION, S513: WAITS ON the factory session's DONE in TO Chat carrying the per-school counts and the unmatched list; read whole by the pricing page theme session S513, which is not a factory session and leaves it untouched.

**For Code, the factory session. What this needs:** add one field naming each Knowledge Hub piece's schools, fill it from Chat's map, and send back the list of published pieces the map does not cover. Chat, Session 466, 12 November 2026. It answers REPORT__What_The_Site_Records_About_Pieces_And_Schools_For_The_Knowledge_Tree_S504.
This session asks Kain nothing: every question goes back to Chat's main session through TO Chat.
Model: Sonnet 5.5. Effort: medium (a data fill with a read-back, no writing).
Done when: every published article, book note, quote article and workbook on the build site that the map names carries its schools in the new field, proved by a count per school read back from the database, and the unmatched list is in TO Chat.

Vault notes for this job: none fit; this is a data field, and no word on any page changes.

DOCUMENT TYPE: brief. Not a page spec.

# BRIEF: fill each piece's schools from the map

## 1. Why

Kain asked for a knowledge tree on each school page: "some way of the website visitor getting access to all articles and questions that we have written, articles or workbooks or quote articles or book notes ... that tie in with the school" (S497). Your report showed that nothing on a piece names a school. Kain said yes to Chat finishing the map for all seven schools (12 November 2026: "yes").

## 2. The map

MAP__Every_Piece_To_Its_Schools_S466.csv, in the School Page folder of Academy + Courses Design Prototypes. 1,075 rows from the content records, one per piece: slug, kind, title, schools (school slugs joined by a bar, as in /academy/<slug>/), placed_by. A piece may sit in more than one school.

How it was made, so you can check a row: each piece's hub (one of the 29 hub guides) gives its schools, and so does any course it names, read against DSRD 5 section 3's school lists. The Diploma, which stands in every school, gives no school on its own. About 130 pieces with no hub or only the Diploma were placed by hand by Chat.

## 3. What to do

1. Add one field to articles, book notes, quote articles and workbooks: `schools`, holding the school slugs. Owner-editable, as the build stance asks.
2. Fill it from the map by slug. Write nothing else on any piece.
3. Read back: the count of published pieces per school and per kind.
4. List every published piece of the four kinds whose slug is not in the map (your report counts 404 published articles; the records hold 336, so about 70 articles will be unmatched), with its slug, title and category. Chat places those by hand.
5. Do not build the knowledge tree block. Its design is put to Kain in the school page session, after this field exists.

OWED BACK: one DONE with the per-school counts and the unmatched list.

*No em or en dashes in this file; checked before writing.*
