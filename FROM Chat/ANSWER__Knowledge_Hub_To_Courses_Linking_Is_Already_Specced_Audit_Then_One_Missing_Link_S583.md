For the theme session: what this needs: an audit of the course block on four Knowledge Hub types against DSRD 1 section 5.7, then the one link the spec asks for and the theme does not print, the course page's home hub link. No decision is left for you; one yes or no goes to Kain (section 6).

Done when: every published article, book note, quote and workbook is read for its course block with the counts and the list of any page with none in your DONE, and each of the 28 course pages carries the one quiet link `Read the Achology guide to {subject}` to its home hub, page gate and link check passed.

# ANSWER: "Knowledge Hub to courses linking" is already specced; the job is an audit plus one missing link (Chat, answering TO Chat/ASK__Knowledge_Hub_To_Courses_Linking_What_Exactly_Is_The_Job_S583)

Each call below is Chat's and Kain may overturn it in a line. The plan note's item 4 line read "every article, workbook, book note, quote links to its right course or school; no orphan pages." That is the whole job, and the specs for it exist, so nothing new is designed.

## The files that hold the spec

- **DSRD 1 section 5.7 (Course Selection, ruled S253):** the matching rule.
- **DSRD 1 section 6.1 (the linking register):** "Every article, quote, and book note page → 'Explore Related Learning Paths' course recommendation", and "Every course page → its home hub", one quiet link reading `Read the Achology guide to {subject}`. Section 6.3 qualifies the course page rule and says this one link is the only exception.
- **DSRD 9 section 32.1:** the block's look and counts (three courses at computer width, two side by side at tablet, two stacked at phone).

## 1. Direction

Both, and both are already ruled. Hub pages to courses is the course recommendation block (section 6.1). Courses to the hub is the one quiet home hub link at the end of each course page (section 6.1, section 6.3). A course page never lists a hub's pages and never links sideways to other courses.

## 2. Hub types

Articles, book notes, quote pages and workbooks. Help answers are not in the spec, so they are left alone (section 6, question). The 29 hub guides are the destination of the course page's link, not a place that carries a course block, because the spec gives them none.

## 3. Template change or content job

A template and data job. Nothing is written into any page body, and no sentence of Chat's is needed. The one exception is a page the audit finds with no course, which is a tag fix in its record: put it on the list in your DONE and the factory fixes the record; never choose a course by hand (section 5.7: "No course is ever chosen by hand for a page").

What the theme already does, read from the theme files (courses-setup.php, single-article.php, single-book_note.php, single-quote.php, single-workbook.php, a worktree dated 23 November, so read the live theme first): `achology_courses_for_content` fills the block on articles, book notes and quotes; the workbook prints its own course card from `source_course` with "Explore This Course". What I could not find in the theme: the text `Read the Achology guide to` anywhere. If the live theme has no such link either, that is the build.

## 4. Where a block sits, and the component

- **The course recommendation block:** it already sits where DSRD 9 section 32.1 puts it on each page type. Do not move or redraw it. It is the signed "Explore Related Learning Paths" component. No four-options round.
- **The workbook card:** stays as built.
- **The home hub link on the course page:** one quiet text link at the end of the course page, after the nine signed blocks, nothing else moving (section 6.3). Use the course page's existing quiet text link style. If the course page holds no signed quiet link style, put four rendered options in the one Change Viewer before building, one marked as the recommendation, as the standing rule asks. The words are fixed: `Read the Achology guide to {subject}`, with the subject as the hub's own title.

## 5. The matching rule

Unchanged: `achology_courses_for_content`, section 5.7 (the page's tags, content attribute tags dropped, the lead tag's mapped courses first, topped up from the next tags, abbreviations resolved through DSRD 5). Do not touch it. For the course page's link, the rule is a lookup: each course has exactly one home hub, from the course to home hub map in the hub plan (DSRD 1 section 3.4 link line 5, DSRD 2's 29 hubs read from the 124 sections of the 28 courses). If the map is not in a file you can find, stop and put the question in your DONE; I will hand it over. Never guess a hub.

## The order of work

1. Read the live theme for the course block and the home hub link. State in one line what is built.
2. Audit: for every published article, book note, quote and workbook, record whether the block shows at least one course and, on the first three, the section 5.7 count. One list in your DONE of any page with none, with its lead tag. Never fix a body.
3. Build the home hub link on the 28 course pages from the map. Run the page gate on one course page and the link check on all 28.
4. DONE to TO Chat with the audit counts, the build and the one list.

## 6. The one question for Kain, for you to put to him

Should Help answers also carry a course card? Chat recommends no: they answer a support question, DSRD 1 does not list them, and a card would pull a reader off the answer. Answerable yes or no.

## Also owed back: the Rich Results Test and Events

I do not know why Google lists no Events item, and I will not guess. The markup is valid on the structured data validator, Google saw all 19, and the Events block is not guaranteed to be shown in the test. Leave it as built and change nothing. The real read is Search Console's Enhancements report for Events after Google next crawls /events/, which I read with Kain's key in about a week; no Code work is owed. The Cards specimen DONE owes nothing back. The loose end, the duplicate page `cards-2` (ID 47678), is Kain's to trash in the admin: I will put it to him.

*No em or en dashes in this file; checked before writing.*
