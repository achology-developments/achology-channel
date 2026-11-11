**For Chat. What this needs:** write Kain's four picks below into DSRD 2 section 2.5 and the school page's layout home, and write the seven schools' words for the block as it now is (one sentence per course is already signed and in use; nothing new is asked for this block). Code, theme session (school page design review), 11 November 2026.

# RULING: the school page's courses stand above the story, as Choose a Course (built, theme 0.707.981)

## 1. Kain's picks, in the Change Viewer, in his words

1. **The courses before the story.** "I do like the courses first. Yeah, definitely buy into that."
2. **The five courses as Choose a Course**, from four shapes shown (a course list, one led with and four beneath, a path of five steps, and a list of names with the chosen course shown whole). "I actually really quite like option number 4, choose a course ... I think we can just kind of tidy it up ... now we can go to really go to town on that." His reason for leaving the cards: "the cards are good, but it just seems very, very clunky on the page ... especially with the missing space."
3. **Six tidy-ups shown as switches; four kept, two refused.** Kept: the price at the row's edge, the school's colour under the picture, the figures as three tiles, the school's one price under the list. Refused: the Start Here mark ("other people who visit the website are going to study NLP before. So we can leave that off") and a line joining the five numbers ("seemed to contradict the line at the side of the selected course"). Start Here is off the block altogether.
4. **Four polishes shown as switches, all kept**: a foot for the price and button, the chosen row lifted, the numbers in soft rings, the rating drawn as stars. "Yes, build it."

5. **Six Free Teachings straight after the story** (added later in the same sitting). Shown as one switch; "Yes, build it." Built: tools/school_page_data.py function `free_after_story`, theme commit 89952e78. The page now runs banner, teaching, courses, story, free teachings, practice, students, questions, price, and closes on the footer's own invitation. Checked on the build site at 1280 and 390: the block stands where the approved preview had it (4,459 and 8,532 down).

Also mended, with no ruling needed: the page's five free lesson stills asked for .jpg files that the course page session replaced with .webp at S490, so they showed empty. The tool now points each at its .webp and stops if one is missing (theme 0.707.982, commit 99cdf8f5).

One thing about this last ship: the course page session held uncommitted theme files and the version line at the time, so pick 5's two files (the school's data file and school-parts.php) were sent to the build site on their own and the cache purged; no version number changed, because no stylesheet or script did. The working copy zip is rebuilt by the next full deploy.

## 2. What was built

- tools/school_page_data.py writes the block from the preview's own course cards and moves it above the story; data/school-page/nlp.json is regenerated; school-page.css and school-page.js carry the look and the behaviour; school-parts.php and the block map state the new order. Theme commit edb47298, deployed, version 0.707.981.
- Every word on the block is read from the page or the course data: each course's sentence is its signed hero sentence (data/courses.json); the line under the list is the price block's own first sentence; its link carries the banner button's words. Code wrote no copy.
- Checked on the build site at 1280 and 390 wide: the built block is the same height as the approved preview at both widths (726 and 1570), nothing runs sideways, and the block order reads teaching, courses, story, practice.

## 3. What is open (so the page is built, gate open, not finished)

- The page's DSRD 6 record does not exist yet and the page gate has not been run on it; the words are still stand-ins.
- The fold-back of this block into a design folder waits on the page being signed, as your S465 ruling held the block map back until then.
- One line of the block's words may now read oddly: the heading's supporting line still says "Start with the beginner's course, or wherever your own questions are", and Kain has taken the Start Here mark off because many visitors have studied NLP before. Chat's call when the school words are written.
- The review's other decisions are still to be shown to him, one at a time: the free teachings moved up, Practise What You Learn shortened, one left edge, the story folded on a phone, and a block on who teaches the school (RULING__School_Page_Review_Invited_And_The_Review_List_S491).

OWED BACK: the four picks written home, and the supporting line settled with the school words.

*No em or en dashes in this file; checked before writing.*
