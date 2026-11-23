> Disposition, Chat S480, 23 Nov 2026: record; nothing owed; archived. No board card moved.

This needs nothing from Chat except to read it: the buy slip sweep is built and deployed, and the three gate lines left open are not the slip's.

# DONE: the buy slip, Fire Edge, on every product page (Code, slip branch, 22 November 2026)

Answers: SWEEP__Buy_Slip_Fire_Edge_S551 (FROM Chat).

## What was built

Kain's option 1, "Bubble on a Soft Circle", from the round previews/school-page-s482/round-slip.js, with slip.css as it stood at d7a2e0ea. The slip is now one component, achology_buy_slip() in course-parts.php, with its look in course-page.css under "The buy slip". All three routes that print a slip call it:
- the 28 course pages, through achology_course_bar() in template-course.php;
- the seven schools and the Access All Areas Pass, through template-school.php, which reads each page's stored slip and redraws it;
- Membership, through template-membership.php, in the same way.

The parts: the Achology bubble on a soft orange circle, 39 tall; the name over its meta pieces, the dots replaced by hairlines; the rating's star in orange; the price set apart, level with the signed main button and 16 from it; a 3 px fire line along the top; and a soft upward shadow. No word changed. Where the price leaves the button, the button keeps "for $X" for a screen reader. Membership's "Start for $7" keeps its price, as the brief says.

Theme version **0.708.375** (0.708.374 carried the build, 0.708.375 the bubble's sizes list), commits 3d32cf84 and 30478186, pushed. Deployed from a clean copy of the commit. deploy.py proved the server, the local copy and the zip identical.

## The page count

Every page on the build site (85, from wp post list) was fetched fresh and checked for the slip. **37 draw it, exactly the brief's list**: the 7 schools, the 28 courses, /access-all-areas/ and /membership/. No other page draws it. Two pages could not be fetched: /free-events/ (a 301) and /cards/ (a 404). Neither wears a slip template.

## The measures (build site, 0.708.374, the slip's geometry unchanged at .375)

Pages: CBP (school), Mindset Mastery (course), the Access All Areas Pass, Membership.

| Width | Slip height | The circle against the name's ink top | The circle against the meta line's ink bottom | The price against the button's centre | One row |
|---|---|---|---|---|---|
| 1440 | 67 on all four | within 0.4 on all four | within 0.4 on CBP, the Pass and Membership; course 1.8 | 0 on all three with a price apart | yes |
| 1024 | 67 on all four | within 0.4 on all four | within 0.4 on CBP, the Pass and Membership; course 1.8 | 0 | yes; the Pass's long button fits |
| 375 | 65 on all four | the bubble and name step out, as option 1's phone note | the same | 0 | yes, on all four, the Pass's "Get the Access All Areas Pass" included, its right edge at 355 (the 20 gutter) |

The course page's 1.8 is recorded and kept, by the Membership theme session's word ("keep one circle size on every page ... the circle spans the two lines' type, ascender to descender, whatever the words happen to be"). That page's meta line, "4.77★ · 4,523 Students · Lifetime Access to Course", has no hanging letter, only a comma, so its ink ends about 2 higher than on lines with a p.

The fire line (3 px, the fire gradient) and the upward shadow were read on all four pages at every width.

## The page gate (0.708.375)

| Page | Result | Slip lines |
|---|---|---|
| /academy/cognitive-behavioural-psychology/ | PASS, 0 fail | pass |
| /access-all-areas/ | PASS, 0 fail | pass |
| /academy/neuro-linguistic-programming/mindset-mastery-self-discovery/ | 1 fail, not the slip | pass (image-responsive, which failed on the bubble at .374, passes at .375) |
| /membership/ | 2 fails, not the slip | pass |

The three open fails, none of them the slip's, are named so they are not lost:
1. The course page: supporting-line, the phone heading "Questions People Ask Before They Enrol" at Como 21 against 24.
2. Membership: rank-math, post 45034 not yet in the score table.
3. Membership: image-dimensions, achology-bubble-mark-26.webp set at 26x20 against a 25x20 file. That is the member levels block's small bubble, not the slip's (the slip uses the 176 and 352 files).

Not done in this sweep: writing the slip line into each page's DSRD 6 record file. The gate results above are what that line would carry.

## Shown to Kain

The CBP page is open in his Safari, through the Membership theme session.

OWED BACK: nothing.
