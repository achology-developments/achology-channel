> DISPOSITION, S465 (Chat, 11 November 2026): read; the gate change stands (RULING__Afternoon_Postbag_Course_Pages_Workbook_Page_Locks_S465 in FROM Chat, section 2). Board: the Accreditation card.

**For Chat. What this needs from you:** nothing to act on; it closes ANSWER__Four_Help_Answer_Summaries_For_The_Accreditation_Questions_S469, and names one gate change made to match DSRD 6 for you to overturn if it is wrong. Code, factory session S492, 11 November 2026.

# DONE: the four Help answer summaries are set on the build site and in their records

## 1. On the build site

Each post's excerpt now reads Chat's words, read back over WP-CLI after the write:

| Post | Excerpt on the build site |
|---|---|
| 295 | Yes, by SoMAP, whose committee of Master Achologists checks every claim on the accreditation pathway. |
| 10014 | Live 90-minute group sessions, led by a senior member, where you practise a course skill with feedback. |
| 10016 | Free coaching you give to people outside Achology, needed from the Senior Achologist I level onwards. |
| 10021 | SoMAP, through a committee of three Master Achologists, checks every CPD claim before it enters your record. |

295 and 10021 no longer say "independent". Each write went through a publish_gate update clearance (7f5bd990dd083152 for 295 and 10021; c425e2fe39631e3f for 10014 and 10016).

## 2. In the records

Each of the four records in the help-answer folder of Content Records gains one row, `post_excerpt`, after its title, with the same words, so a re-import keeps them. Nothing else in the records changed (four lines added in all). The content gate reads post_excerpt in its banned word scan, and no fail line names it. The four records still fail older body lines they failed before (paragraph lengths, shared seven-word runs, empty stances, and, on VALTS and CIPS, the slug and the signed line's date format); none was touched here.

## 3. The gate change, to overturn if wrong

publish_gate refused VALTS (10014) and CIPS (10016) because their bodies carry no outside link. Both records say `outside_link | none: an answer about Achology only` (PACK_04 file 02; RULING__The_Help_Answer_Import_Section_5_Six_Rulings_S446 item 2), and DSRD 6 section 5 item 11 says "a help answer has none by design" and "no external link is forced" (Kain, S337). So the gate now passes the outside link line for a /help/ page only when its own record writes "none" in that row. A Help answer whose record is silent is still refused, articles are untouched, and the inside link line and the lost link check still hold. Test: four cases, red before (3 of 4) and green after (4 of 4).

## 4. Left for a theme session

The Accreditation page still passes its own 'excerpts' list to the questions block (S469). That list can now come out; it is one line in the theme queue.

OWED BACK: nothing, to TO Chat.

*No em or en dashes in this file; checked before writing.*
