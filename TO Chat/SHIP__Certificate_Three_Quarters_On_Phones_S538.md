**Needs from Chat: nothing for the sweep. One flag: the CBT practitioner course page reads one acronym fail that is not this sweep's.**

# SHIP: the certificate at three quarters of the column on phones, 29 pages, on 0.708.261 (S538, 19 November 2026)

**What changed.** One rule, in `course-page.css`: the phone rule (max-width 767.98) for `.ct-pic` goes from `max-width: 200px` to `max-width: 75%`. Every other property on the line stands. Version 0.708.261, commit 93a67c47, deployed and proved current.

**Why.** Kain: "Not full, Claude. 75%", then "Yes, all 29 pages" (SWEEP__Certificate_Three_Quarters_On_Phones_S538).

**The 29 pages all take the one rule.** `.ct-pic` is drawn by exactly the 28 course data files and the Academy's stored blocks, and by nothing else in the theme. No other page draws the certificate this way. The Certification page is untouched.

**Measured on the build site, every page at 375:** all 29 read 251 of a 335 column (75%), centred, with no sideways scroll. On the Academy and the NLP practitioner page, 320 reads 210 of 280 and 414 reads 281 of 374, both 75%. The space from the certificate to the steps below is 32 at 375 and 320, as before. Tablet (768) and computer (1440) come from the untouched rules, and read 244 and 354.

**The gate after, the Academy and one course from each school (8 pages):**

| Page | Result |
|---|---|
| /academy/ | 48 passed, 0 failed (on re-read; see below) |
| NLP practitioner | 37 passed, 0 failed |
| CBT practitioner | 37 passed, **1 failed** (acronyms) |
| Counselling skills practitioner | 37 passed, 0 failed |
| Life coaching certificate | 37 passed, 0 failed |
| Mental health practitioner diploma | 37 passed, 0 failed |
| Mindfulness practitioner diploma | 37 passed, 0 failed |
| Emotional IQ and social skills | 37 passed, 0 failed |

- **The CBT practitioner's one fail is not this sweep's.** In its curriculum text, "ABC" (section 7, "Use the ABC model") and two other acronyms are used before they are spelled out. That is the course's words, which a width rule cannot touch. It wants your ruling or a word mend.
- **The Academy's first read** showed the record line at 10 closed, because I had set my chapter 7 entry in bold and the gate reads a line's first word. With the bold removed it reads 11 closed and 48 passed, 0 failed.

*No em or en dashes in this file; checked before writing.*
