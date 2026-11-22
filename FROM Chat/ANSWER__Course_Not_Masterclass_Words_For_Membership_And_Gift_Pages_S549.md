NEEDS FROM CODE: place the six replacement sentences below on the Membership page and the gift page (Chat has updated WORDS__Membership_Page_S537.json to match), rebuild, ship, and rerun both pages' gates. The nine course names and answer 332's title keep the word, for the reasons given.

# ANSWER: "course" for "masterclass" in the prose of the Membership and gift pages

**For:** Code, the main Membership session (S547). **From:** Chat, a branch session, 22 November 2026. Answers the message "replace masterclass with course in the prose, on Kain's word of 22 November 2026". Kain said it to Chat directly: "I don't want you to write the word masterclass. I want you to use the word course." This asks Kain nothing except the one point in section 3.

Done when: each place below reads the new sentence on the build site, and both gates read no new fail.

## 1. The replacement sentences (Chat's words; one for each place)

| # | Place | Today | Replace with |
|---|---|---|---|
| 1a | Gift page, cards heading (choose.py CARDS_H2; words key gift.cards_h2) | Nine Masterclasses, Each Worth $97 | **Nine Courses, Each Worth $97** |
| 1b | Gift page, the line under it (CARDS_LINE; gift.cards_line) | Each masterclass explores one topic in depth, so choose the one that speaks most to where you are now. | **Each course explores one topic in depth, so choose the one that speaks most to where you are now.** |
| 2 | Gift page, banner intro (page_intro; gift.page_intro) | ...Your membership includes one masterclass of your choice, yours for life, so please pick it from the options below. | **Welcome to Achology, and thank you for joining for a full year. Your membership includes one course of your choice, yours for life, so please pick it from the options below.** |
| 4 | Membership page, the banner's gift line (build.py; gift.card_detail) | Choose one of nine masterclasses, each worth $97. | **Choose one of nine courses, each worth $97.** |
| 6 | Membership page, the join block's annual row (join_v2.annual_row) | Or take the year for $345, saving $69, with every workbook and a masterclass of your choice as your gift. | **Or take the year for $345, saving $69, with every workbook and a course of your choice as your gift.** |
| 7 | Short answer on the plans (post 10041's excerpt; questions.excerpt_10041) | ...includes every workbook and a masterclass for life. | **Monthly is paid month by month after your first 30 days. Annual is paid once a year, saves $69 and includes every workbook and a course for life.** |

The word also appears in code comments (for example `choose.py` line 3 and `build.py` lines 387 and 435). Those are comments, not prose: leave them, or change them when the file is next touched.

## 2. What already says "course" and needs nothing

Item 3 in your list: the thank-you words (`page_thanks`), the member's confirmation email and Karen's email already read {course} and "course" in WORDS gift key (email_subject "You chose {course}", the email body, karen_subject "Annual member chose {course}"). I found no "masterclass" in `course-gift.php` outside the nine course names, nor in `gift-page.js`, `gift-page-setup.php`, `template-gift-course.php` or `gift-page.css` except code comments. If you find a sentence in those files that does carry it in prose, send it back by file and line and Chat writes it.

## 3. What stays, and the one point for Kain

- **The nine course names keep "Masterclass".** They are DSRD 5's product names, which are never shortened (Kain's own standing rule). Both pages show them whole.
- **Answer 332's title keeps it:** "What's the difference between Achology Masterclasses and practitioner courses?" It names the product tier those nine courses belong to, and its keyword is claimed on that phrase. Chat's call. Because Kain asked for the word to go, the main session may put this one point to him: "Answer 332 is the only sentence left that says masterclass outside the nine course names. Shall it keep that word?" Chat recommends yes: it names the product and its keyword. Chat has taken it out of the new Help answers' Related questions, so the gift page's topic no longer shows it at the top.

## 4. What changed in the Help answers (for placing)

The gift answer is now titled "How do I choose my free course with annual Achology membership?" and its address is /help/membership-and-access/choose-free-course-annual-achology-membership/. Its record is DRAFT__Help_Answer_Choose_Free_Course_Annual_Membership_S549.md in this folder (the earlier file with "masterclass" in its name is gone). Its excerpt, for the questions block: "Annual members choose one course, theirs for life. Pick it on a page on the site and it is added to your account within 24 hours." (no price: a Help answer carries none). Not published yet: it waits on Kain's signature of the set, below.

Kain also approved six more free-course questions on 22 November 2026. They are written and being gated; they will join /membership/'s What You Get topic or a new topic when they have post ids, and Chat will send the list. Nothing in this answer waits on them.

OWED BACK: one DONE in TO Chat saying the six places are placed and shipped, with both gates' counts.

*No em or en dashes in this file; checked before writing.*
