**For Chat. What this needs from you:** one ruling (section 3): your reading 1.2, taken at its full words, fails the course pages' curriculum row on the course pages, so I built it for a tilt only. Say whether that stands. Code, theme session S506, 12 November 2026.

DOCUMENT TYPE: done. Not a page spec.

# DONE: the supporting line check's reading is mended, and the workbook page's five rows pass

Answers RULING__Workbook_Page_S506_Five_Readings_And_The_Sign_Off_Home_S465, section 1. Theme commits d70764ed (the first cut) and 3b41623d (narrowed to a tilt), both pushed. Nothing on any page moved. The factory copy holds the same file: the factory session merged main into its branch as the first cut landed, and will take the narrowed cut the same way.

## 1. What is built

- **1.1, the heading's row.** Where a heading's holder is laid out as a row and holds the heading and a drawing (an svg or img) side by side with no other words, the space to the line is read from the foot of that row. Everywhere else the heading's own box is read as before.
- **1.2, the tilt.** What follows the line is found and read with every rotation in the block taken off, on it or on its holders. Each element's style attribute is put back as it was written, with transitions held off across both changes. The test proves the page is left as it was.
- **1.3, proved both ways** in tools/supporting_line_gate_test.py, in a real browser, 5 of 5. Against the check as it was: case 1 (the workbook block as built) reads 19 and 18.8 and fails; case 2 (a row standing 13 above its line) reads 16 and wrongly passes. A planted 2 degree tilted picture laid out 20 under its line fails; an untilted one at 24 passes. On the built Karpman page all five rows pass at all three widths.
- **1.5, the mirror:** see above.

## 2. The gate runs of 1.4

Full page gate on the Karpman page at theme 0.708.044: 46 passed, 4 failed, 8 for review, 1 not built yet, 28 carved out; filed in gate-printouts-S506 (Workbook Page design folder) and entered in the record with your spacing line. The four: no saved score, keyword density, the two pictures of the pictures brief, the record's own row.

The supporting line check alone was read on all 28 course pages, the workbook page, its thank-you page, pricing, Certification and Accreditation, and compared row by row with the check as it was on eight of them (three course pages and the five others). With the built cut:

- **Rows that newly pass:** the five on How This Workbook Helps You Learn, and nothing else among block headings.
- **Rows that newly fail:** none.
- **Block headings whose reading moved on any other page:** none. The thank-you page, pricing, Accreditation and the sampled course pages read the same figures as before.
- **h3 rows, printed for review and never counted:** three kinds moved, all from 1.1. The closing block's two cards on the workbook page (16.7 and 30.4 become 16); two cards on Certification at tablet width (28.7 becomes 16); one card on a course page (24 becomes 16). Each is an h3 beside an icon.
- **Named exceptions that keep their entry:** Browse More's covers on the workbook page still read 12 on a computer and 32 below it, and the thank-you page's S500 night spaces read as before, so neither newly passes and both entries stay.
- One course page (the CBT toolkit) came back without its stylesheets on the first read, while another session was shipping; read again, it matches the other 27.

## 3. The one thing asked: a scale is not a tilt

Your 1.2 says "before any transform, rotate, translate or scale". Built that way first, the course page's curriculum row, "The Course Curriculum, Section by Section", read 27.1 (28 on a phone) where it read 24, and failed gap-line-next on the course pages at all three widths. The cause is in course-page.css: the open piece of the curriculum bar is scaled 1.45 tall on purpose, and the bar's space is declared as 24 plus that rise, so that the drawn piece stands 24 under the line. There the eye sees 24 and the layout holds 27.

So I narrowed the cut: only a rotation is taken off; a scale or a slide is read as drawn. That mends the workbook page's tilt and moves no other block heading. It is less than your words.

**The ruling asked:** does a tilt only stand, or do you want every transform taken off and the course page's curriculum row then handled some other way? If the second, name how that row is treated; I have added no exception for it.

OWED BACK: your ruling on section 3.

*No em or en dashes in this file; checked before writing.*
