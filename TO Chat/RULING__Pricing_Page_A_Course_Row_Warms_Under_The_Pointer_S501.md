**For Chat. What this needs:** write Kain's pick home in DSRD 9 section 36.9, beside the pricing page's other picks. Code, theme session, 11 November 2026 (session id 975f955d), the pricing page's third sitting. This file is also the ship brief for theme 0.708.014.

DOCUMENT TYPE: ruling. Not a page spec.

# RULING: a course row on the pricing page warms under the pointer (theme 0.708.014)

## 1. His words

Shown as one switch in the Change Viewer (previews/pricing-s489/round-warm.js, proved by tools/viewer_proof.py, 5 measured, 0 failed). Kain, 11 November 2026: "I'm actually struggling to see what the changes you've made on this ... Oh, I see what you mean, actually. Oh, yeah. Forget that. Much better. Yeah, that's much better. Yep, go for it. Build it. Thank you."

He had to look twice to find it, then chose it as shown. It is left as faint as he saw it.

## 2. What changed, and why

Only a course's name was a link, and nothing tied the name to its price at the far right of the row. The row under the pointer now takes Light Sand, bled one step past the column each side so the words keep the column's edge, and the course name turns to its link orange. The name's link covers the whole row, so anywhere on it opens the course, the price end included, and on a phone too, where nothing shows.

Styles only, in pricing.css; the markup and pricing.js are untouched. No word, figure, size or space changes.

## 3. Read on the build site at 0.708.014

At 1268, with the pointer on the price end of the third row: the row reads rgb(251, 249, 246), Light Sand, with 16 of the same each side; the name reads the link orange; the thing under the pointer is the course's own link; every row 77 tall as before; no sideways scroll. At 390: every row the height it was, the stacked course kinds 128 as built, no sideways scroll. Commit 8e9515ce.

## 4. How it was deployed, for the record

Another theme session held uncommitted course-page.js and functions.php in the shared folder, so this deploy went from a clean copy of the commit, not the folder. The server and the commit agree at 0.708.014. The zip beside the theme folder was not rebuilt by this deploy; the next deploy from the folder rebuilds it.

## 5. Still to be shown

The two ideas for the eight cards, in previews/pricing-s489/PICKS.md, third sitting: a card's course list easing open, and the facts under a school name never starting a line with a dot on a phone. The Pass card standing 3 taller than its neighbour is Code's to mend and prove.

OWED BACK: the pick written home in DSRD 9 section 36.9.

*No em or en dashes in this file; checked before writing.*
