DISPOSITION (Chat, Session 478, 20 November 2026): for the record. Archived.

**Needs from Chat: one request withdrawn. The courses line exception asked in SHIP__School_Page_Banner_School_Building_S530 is no longer needed: Kain replaced that line with a one-sentence line. The rest is for your record and the school page's chapter 10.**

# SHIP: Kain's fine-tuned headings and supporting lines on all seven school pages, on 0.708.251 and 0.708.253 (S530 side session, 19 November 2026)

**What changed.** Kain fine-tuned every block heading and supporting line on the seven school pages, block by block, as he had on the Access All Areas Pass. His words are placed word for word, with each school's own name, number of courses, subject and saving filling the gaps he left. On the NLP page:

- **Block 2:** What You Can Expect to Learn at This School. "Here's a brief look at what you'll learn in this school's five courses." The side panel heading is Who Should Enrol in This School.
- **Block 3:** All Five Courses Included in This School Bundle. "All the courses listed below are included in your enrolment, so you can start with whichever one interests you most."
- **Block 4:** A Short History of Neuro-Linguistic Programming. The line is unchanged.
- **Block 5:** The Neuro-Linguistic Programming Knowledge and Learning Tree. "At Achology, our mission is to make ideas that expand perspectives accessible to everyone who wants to explore them. Each leaf on the tree below links to an article about an idea taught in this school." The heading beside the tree is Choose a Topic, and We'll Fetch You Some Articles.
- **Block 6:** Explore Six Sample Tutorials from This School, with the pass's line, "At Achology, we believe in transparency. That's why you can view up to two hours ...".
- **Block 7:** Weekly Workshops to Practise What You Learn. "In addition to studying the courses included in the School of Neuro-Linguistic Programming (NLP), you can apply your learning in three ways. ..." The three cards' tag, name and headline are as the pass's.
- **Block 8:** What Our Students Say About Studying at Achology, with the pass's line.
- **Block 9:** The School of Neuro-Linguistic Programming (NLP) Flexible Payment Options. "Get all five courses for life, plus 12 months of Achology Membership, for 24% less than if you bought them individually." Each school shows its own saving.
- **Footer invitation:** Experience the Academy; Try Six Free Teachings Before You Decide; "We will send you six free teachings from the Academy, one a day for six days, each with its own workbook."

**Kain's calls in the sitting.** For the tree heading's gap he chose "the subject", then "the subject knowledge and learning tree". On the third card he said "Yes, match the pass", so it reads Practise (UK verb) and Sessions. "This" is in title case in Who Should Enrol in This School and in Explore Six Sample Tutorials from This School. A trailing paragraph in his footer message was deleted on his word, "No, delete it". Code told him that the tree's leaves also open book notes, quotes and workbooks; his line saying "an article" stands as written.

**How.** In tools/school_page_data.py, kain_words and kain_invite set the words over the earlier ones; PRACTISE_TITLE, PRACTISE_LINE and FREE_LINE are his. The tree's title, line, contents title and spoken name are in data/school-page/knowledge-tree.json. The title names [subject], which school-knowledge-tree.php fills from each school's data (subject, the story's own field). On 0.708.253, the footer invitation's button takes only its own width from 1024 up, so the title stands on one row as he asked. The history heading keeps its last two words together. Nothing else in the seven data files changed, checked word by word.

**Measured in WebKit through the mirror.** All seven at 1270, and NLP and Mental Health at 1440, 1024, 768 and 390. Every heading is on one row at 1270 and 1440. The footer title is on one row from 1024 up and on 768. No heading ends on a lone word, and nothing scrolls sideways.

*No em or en dashes in this file; checked before writing.*
