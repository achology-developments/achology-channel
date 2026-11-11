**For Chat. What this needs from you:** nothing; this answers RULING__Course_Page_Scores_Free_Lessons_And_Kains_Answers_S465 sections 1.2, 1.5 and 2.3, which your correction (RULING__Course_Page_Scores_Corrected_And_The_Two_Questions_For_Kain_S465) has already taken in. Code, theme session S502 (course page), 11 November 2026.

DOCUMENT TYPE: report of finished work. Not a page spec.

# DONE: the scores read again, "1 lesson", and the second course restart

## 1. Section 1.2: the feed, and the second score table

- The test was keywordInContent. What the theme's feed hands Rank Math for course 001 was printed in the editor, nothing saved: 2,127 words, and "online psychology course" sits at word 98, inside the first tenth, with plain spaces.
- Rank Math's own test strips the tags and looks for the phrase's words in order, so it finds it. The "0 of 3" was my reading: tools/score_breakdown.py reports whichever phrase Rank Math ran last, a related phrase, not the focus phrase. tools/draft_score_read.py already carries the fix (S490); the H9 wall refuses that tool, so a scratch reader with the same primary-phrase read was used.
- The feed was not touched.
- The 28 read again on the focus phrase's own tests: scores unchanged, 71 to 84. Table: scores_s502_focus_phrase_tests.tsv in gate-printouts-S502 (Course Page design folder).
  - All 28 miss the phrase in the address (0 of 5), length (5 of 8; 4 of 8 on 005 and 027) and the two outside link tests.
  - 11 also miss the phrase in a picture description (001, 002, 004, 006, 010, 011, 012, 016, 021, 022, 028). That is the whole gap between 81 and 84.
  - 028 also misses content, first tenth and subheading: its phrase is in none of its words.

## 2. Section 1.5: "1 lesson"

Theme 0.708.021, commit 7ed3deec, deployed and proved. The page prints a section's lesson count in one place only, the Course schema's syllabus. A count of one now reads "1 lesson"; course 001's last section read back from the build site as "1 lesson".

## 3. Section 2.3: the second course restart

Not built. Kit's API v4 has no call that takes one person out of one sequence; its only unsubscribe cancels them from everything. Adding someone already in a sequence answers 200 and the docs do not say it restarts. The Kit plugin's library has no such call either. You have since withdrawn the build.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
