**DISPOSITION (Chat, Session 467, 12 November 2026): ANSWER WRITTEN HOME.** The plan's queue lines and briefs are a Backlog: Chat line, triggered by Kain settling the knowledge tree's finishing round. Archived.

**For Chat. What this needs:** read this plan, correct anything the record contradicts, and turn it into the school page's queue lines and briefs, so the next school page session opens on step 1 without asking Kain anything. Code, theme session S497 (the school page story block), 11 November 2026.

DOCUMENT TYPE: note. Not a page spec.

# NOTE: everything between here and the seven school pages being publish ready

## 0. Why this file exists

Kain, at the end of the S497 sitting: "could I just ask you to please just define a plan for everything that stands in the way of us, between where we are right now and these school pages being published ready, because that's the kind of the plan we need to take into a new session."

## 1. Where the school pages stand tonight (read this session unless marked)

- One school page is built: the NLP school, theme 0.708.023. Its parts are data/school-page/nlp.json, written by tools/school_page_data.py from the preview page previews/school-page-s482/school.html.
- The other six schools have no stored parts, so they do not take the school page template yet (functions.php: a school takes it only once its stored parts exist).
- On the NLP page only the story of the field uses your signed words (S465), with the signed card on Kain's own course. Every other block still shows stand-in words; the tool marks the page `stand_in_words: true`.
- The story block is designed with Kain and built (your DSRD 2 section 2.5 items 16 to 20). The seven signed cards are in the data file.
- Built on his picks at S491: the courses above the story as Choose a Course, Six Free Teachings after the story, Practise What You Learn opening on a press.
- No DSRD 6 record exists for the school page and the page gate has not been run on it. Built, gate open.
- Kain has ruled the seven school pages stay drafts (your item 21), so links to them from the published course pages are pages to come.

## 2. The plan, in the order Code recommends

**Step 1. Place the signed words on the NLP page (BRIEF__Place_The_Signed_School_Page_Words_S465).** Teach tools/school_page_data.py to write every slot from SCHOOL_WORDS_SIGNED_S465.json: banner, teach_line, teach_p1 to p4, who, courses_line, practise_line, cards, practise_close, students_line, faq_line, the nine faqs, enrol_line, enrol_promise, free_line, free_six. Keep `courses`, `free_after_story`, `stills` and `story`. Prove it by a read-back of the built page against the data file, slot for slot. Report every line that ends on one, two or three words at 1268, 834 and 390; you mend the words.

**Step 2. Build the other six schools from data, not from the preview.** The tool reads the NLP preview page for the banner picture, the course cards, the students block, the price card and the buy bar. For six more schools each of those needs a real source: the school's row in DSRD 5 and DSRD 4 for names, figures and price; data/courses.json for each course's name, address, picture, rating, students and hours; the school's own colour token; the school's banner picture. This is the largest piece of building left. Code needs from you: confirmation of each source, and each school's course list in order.

**Step 3. Facts and words still owed, to gather while steps 1 and 2 run.**
1. The six free teachings for the four schools that have none (life coaching, person-centred, mindfulness, personal growth). Until they are signed their free block stays off, as your brief rules.
2. Each school's search title, description and focus phrase for Rank Math, as you gave them for the course pages.
3. The short last lines reported in DONE__The_Seven_Signed_Story_Cards_Placed_S497, if you mend them.

**Step 4. The tidy no reader sees.** Take the school page's load of story-scroll.js and the two dead sections of school-page.js out, proved by a before and after reading (your night postbag, 4.2 item 3).

**Step 5. The block Kain has not yet seen: who teaches this school.** It was item 7 of the S491 review and has never been shown. It is his to open. If he wants it, it comes to him as whole designs first, then polish, as the story did; its words are yours.

**Step 6. One design walk of the whole page with Kain, at computer and phone.** Block by block, one decision at a time, on the NLP page with its real words, then one other school to see a second colour and a second set of courses. Anything he changes is shown as a switch before it is built.

**Step 7. Metadata and structured data, all seven.** Rank Math title, description and focus phrase set over WP-CLI by Code; the page's structured data checked in the validators; scores read from the built pages by Code only.

**Step 8. The gate and the record.** Run page_gate.py on the school page type; write the one DSRD 6 record for the type (found by its Address pattern line); enter the exceptions you rule in page_gate.py with each ruling quoted; mend the real faults. The speed line takes the site-wide exception and the screen reader read is run once for the whole site before launch, as Kain has ruled for other pages.

**Step 9. The fold-back.** The approved school page exported into the School Page design folder as its prototype, its build sheet written, and the Component Registry rows for the story block (prefix sps) and Choose a Course filled.

**Step 10. Your reader lines, then Kain's walk and signature.** The record closed with no line reading fail or not run.

**Step 11. Publishing, only on Kain's word.** His ruling today is that the seven stay drafts. When he lifts it: a clearance from publish_gate.py, the redirects from the old school addresses written and proved, the links from the 28 course pages to their schools read as working, and the Build Board card moved.

## 3. What is not in this plan and may belong beside it

- The schools landing page at /academy/ (a design folder exists; no page is built). Course pages and school pages link to it.
- Whether the About page takes the new story design (on the Decisions for Kain list; Code will not raise it).

## 4. What Code has not verified

Step 2's list of what the tool reads from the preview is from reading the tool's `build`, `courses` and `story` functions this session; the students block, the price card and the footer invite were not read line by line. The state of each school's banner picture and colour token was not checked. Step 11's redirect and link counts were not read.

OWED BACK: your corrections, the queue lines and briefs for steps 1, 2, 4, 7 and 8, and the words in step 3.

*No em or en dashes in this file; checked before writing.*
