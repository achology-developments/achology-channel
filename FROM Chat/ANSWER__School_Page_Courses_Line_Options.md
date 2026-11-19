> CODE DISPOSITION, S532: WAITS ON the school page theme session showing Kain the four courses-block lines; it belongs to that session, not the Access All Areas Pass session.
> CODE DISPOSITION, S530: DONE in 0.708.230 (commit 33d32877). Kain saw the four lines and then wrote his own title and line, "Yes, place them"; none of the four was used. See SHIP__School_Page_Courses_Block_Light_Card_S530 in TO Chat.

For Code, the school page theme session (S530 side session). What this needs: show the four lines to Kain on the real page in the Change Viewer, then place the one he picks, the same on all seven schools.

Done when the line Kain picks stands word for word under The Courses Included Within This School heading on all seven schools, and its rows at 1440, 1024, 834 and 390 match the table below.

From Chat, 18 November 2026. Answers your words job for the courses block's supporting line.

# The courses block line: four options, one for all seven schools

**Used:** DSRD 7 section 3.3 (the five supporting line rules, Lead with Bar, the full container width), the Content Standard's word lists as the gate reads them, and the vault note A Set Of Short Lines That Share One Space Is Judged By Its Rows At The Built Width, Not By Its Word Count.

## The four lines

| | The line | What it does |
|---|---|---|
| **1 (recommended)** | The courses run in order, so if you’re new you’ll know where to begin. | Tells the reader the list is a path, and that the top of it is where a newcomer starts. |
| 2 | Each course stands on its own, so you can start with the one you need. | Tells the reader there is no set path: any course can come first. |
| 3 | Open a course to see what it teaches, how long it runs and how it’s rated. | Tells the reader how to use the block: each course opens to show its line, its hours and its rating. |
| 4 | One enrolment gives you every course below, so none costs you extra. | Tells the reader what the enrolment buys: every course in the list, with no extra charge per course. |

**I recommend line 1.** It says the one thing the list can't show by itself: that the order is deliberate, and where a newcomer begins. It holds true on all seven schools, because each one opens with its newcomer's course. It also avoids repeating the title, which already says every course is included, as line 4 partly does.

Lines 1 and 2 contradict each other on purpose, so Kain can choose between a path and free choice. Line 3 is the one imperative. DSRD 7 rule 4 allows it here, because this block's job is to have the reader open a course.

## Why they are short: measured on the built block

I measured the four lines on your mirror's NLP school page, inside the block's own `p.lead-bar` (Mulish 500, 18 on 27.9), after the site font had loaded.

| Width | Text width | Rows | Last row full |
|---|---|---|---|
| 1440 and 1280 | 1106 | 1 | 52 to 56% |
| 1024 | 930 | 1 | 62 to 66% |
| 834 | 772 | 1 | 75 to 81% |
| 390 | 352 | 2 | 65 to 84%, five to eight words in the last row |

- The 834 width sets the length. A line of about 86 characters fills 92% of one row there, and in Safari it can tip into a second row with one or two words in it.
- A two-row line is not possible across every width either. At 1440 it would need more than 25 words, which breaks rule 2, or its second row would be nearly empty.
- So all four are one row on a computer and on a tablet, and two even rows on a phone. They run 68 to 74 characters and 12 to 16 words, inside rule 2's 12 to 25.
- For comparison, the NLP line as built today is 92 characters. It is one row at 1440, but at 834 it runs to 99% and can tip.

## The gates

- **Word lists:** checked against `content_gate_standards.json`: banned always, flagged in context, machine tells (always and flagged), watched words, the stance never words, the banned rules 7 and 8, and the banned link labels. The steady family was checked by hand. No hits on any of the four.
- **Dashes:** none.
- **Rule of three:** line 3 lists three things. These are the three things a course actually shows when it opens, not a rhetorical triplet, so I kept it. The gate flags this pattern but never fails it.
- **Not run:** voice_measure and content_gate measure a whole piece (sentence spread, paragraph bands). They have no reading for one site line, and content_gate has no site copy type.
- **Body guard:** no working note in any line.
- **Facts:** every fact in a line is on the built block: the order (newcomer's course first, the Diploma Course in Modern Applied Psychology (DiMAP) last, checked in all seven data files), the hours and the rating on each course, and one school enrolment covering every course.

## For the build

- Place the picked line word for word on all seven, in the courses block's `p.lead-bar`, in each school's data file and in SCHOOL_WORDS_SIGNED_S465.json, so a rebuild keeps it.
- Keep the curly apostrophes.
- Re-measure on the built page at 1440, 1024, 834 and 390, and report any line that runs a different number of rows from the table above.

## Your tree DONE

Nothing is owed from me. Your SHIP note says Kain wrote his own help line, "Choose a specific topic of interest to explore the resources available on it.", so the clash with his title is gone. My line with "above" is withdrawn.

*No em or en dashes in this file; checked before writing.*
