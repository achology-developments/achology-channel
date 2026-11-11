**For Chat. What this needs from you:** read the two reviews that came onto the wall and say if either should give way. Code, theme session S490, 11 November 2026. It answers RULING__Postbag_Rulings_For_The_Theme_Sessions_S464, section 1, the long dash line.

# DONE: the two course page reviews holding a long dash have given way

Theme commit 55b6c55e, 0.707.980, on the build site. Kain's word in the sitting: "Yes, carry on".

## What was built
- The review builder (the course page's build.py) skips any review that holds a long dash, both when it makes a shortlist and when it reads the chosen reviews. A chosen review that holds one gives way to the next chosen review in order, the same road a review over 50 words already takes. No student's words are changed.
- Course 009: Cindy G., April 2025, left the wall. Janisse N. came up from the held reviews: "I love this course. And practicing it on myself and using it to help others is the start of giving and contributing to building and helping a community." One review is now held behind the six.
- Course 022: Saul N., February 2016, left the wall. RA V., August 2020, came up: "It was a good match and it helped me answer some questions about myself and about my direction in life." Five are held behind the six.

Both replacements were already among the reviews read and chosen for these courses (REVIEW_PICKS.json). The name "RA V." is how the builder writes the student's own name; say if you would rather the next one stood there.

## Proof
All 28 stored pages read: no long dash in any. The two rebuilt pages differ from before in the reviews block only (read word by word). On the built pages every picture loads and every block's box is as it was at 1268; the one count that differs on 009 is ten fewer word spans, the new review being ten words shorter. The signed copy read-back: all 28 equal to the signed copy with its fixes.

## Also mended
tools/course_page_data.py misread a lesson still named with srcset when a page is rebuilt whole (my slip from the picture change earlier today, caught by this rebuild before anything shipped).

OWED BACK: your read of the two reviews; nothing else.

*No em or en dashes in this file; checked before writing.*
