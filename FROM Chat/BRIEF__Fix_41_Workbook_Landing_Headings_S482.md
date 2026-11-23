What this needs from Code (theme session or the factory): apply the heading fixes in heading_fixes.json to 41 workbook landing pages, in each page's record and on the build site, then rerun the gates.

Done when every old string in the file reads as its new string on the build site and in the record, the content gate and the page score are rerun on all 41, and one DONE lists any page that failed to match or fell under 86.

# BRIEF: 41 workbook landing headings that read wrongly (Chat, Session 482, 23 November 2026)

Governing pieces, named so nothing is searched for: The Achology Content Standard Part 17.6 and DSRD 2 section 1.7 (the heading is "What Is [the idea]?" and "What [the idea] Is Used For", with "People use [the idea] to:"); the workbook-landing-page skill; the Shared Road every kind of page travels, and the workbook card in 17 Packs of The Newsroom Vault. This brief adds no rule. It makes the idea name agree with Is or Are on 41 pages where it did not.

## The fault
Chat read ten drawn pages (the human read DSRD 6 section 0 owes) and found the first heading breaks when the idea's name is plural or is not a thing: "What Is the Five Levels of Human Experience Model?", "What Is Carl Rogers' Nineteen Propositions?", "What Is Who Am I Really?". The "Is Used For" heading breaks the same way. Chat read all 212 headings; the 41 in the file are the ones that read wrongly. The other 171 stand. Kain saw the before and after on one rendered page (Workbook Headings Before And After.html, in the folder) and said "Yes, rewrite them".

## What to do
The folder `FROM Chat/Workbook Heading Fix 23 November 2026` holds `heading_fixes.json` and the rendered before and after page. For each of the 41 entries in `headings`:
1. In the record's landing page body (the record is in the workbook folder of the Newsroom's content records, named by its number and the slug) and in the live post, replace `old_h1` with `new_h1`, `old_h2` with `new_h2` and `old_people_use` with `new_people_use`, exact strings.
2. Where the entry has `old_find` and `new_find`, replace that phrase inside the sentence "And if you find ... useful, the course is there whenever you want to explore the ideas around it." and nowhere else.
3. Two sentence mends, in `sentences`: carl-rogers-nineteen-propositions (drops "a theory put forward by Carl Rogers", so the opening paragraph names him three times, not four) and the-core-counselling-skills (the last line was missing its noun).
4. If any old string does not match exactly on a page, do not guess. Leave that page and list its slug in the DONE.

## After
Rerun the content gate for the workbook type and the Rank Math score on all 41. A page whose focus keyword was in the changed heading, or one that drops under 86, goes back to Chat in the DONE with its slug, the old and new score, and the line that moved. Do not mend it yourself.

The headings of the other 171 pages and every other word on all 212 stay as they are.

OWED BACK: one DONE to TO Chat with the 41 results.

DOCUMENT TYPE: brief.

*No em or en dashes in this file; checked before writing.*
