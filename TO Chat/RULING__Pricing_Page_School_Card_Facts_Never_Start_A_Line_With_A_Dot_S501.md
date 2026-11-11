**For Chat. What this needs:** write Kain's pick home in DSRD 9 section 36.9, beside the pricing page's other picks. Code, theme session, 11 November 2026 (session id 975f955d), the pricing page's third sitting. This file is also the ship brief for the change.

DOCUMENT TYPE: ruling. Not a page spec.

# RULING: on a phone no line of a school card's facts starts with a dot

## 1. His words

Shown as one switch in the Change Viewer (previews/pricing-s489/round-facts.js, proved by tools/viewer_proof.py, 5 measured, 0 failed). Kain, 11 November 2026: "Yes, build it".

## 2. What changed, and why

On a phone the three facts under a school name (courses, hours, lectures) broke after the second, so the second line of all seven school cards began with a dot. Each fact now carries its dot in a fixed slot at its left, 19 wide, the 8, the dot and the 8 it had; the slot that starts a line falls outside the line's left edge and is clipped. A fact in the middle of a line reads as before; one that starts a line stands on the line's edge.

Styles only, in pricing.css, under the phone tier. The Access All Areas Pass card is left out: its facts line already has its own mechanism, where a dot can never begin a line. Computers are untouched. No word or figure changes.

## 3. Read on the build site at 0.708.023

Commit 7837c028, written as 0.708.022. At 390, on all seven school cards, the third fact stands at 69 from the left, the line's edge, where it stood at 80 behind its dot; the first line moves by 1 at most; every card the height it was (394 or 418; the Pass 416); no sideways scroll. At 1268 every fact and card as before. The sitting's four earlier picks read in place in the same run.

## 4. How it reached the build site, for the record

This session deployed 0.708.022. A moment later another theme session's deploy from an older clean copy put 0.708.021 back on the server, without this change. The theme folder was clean at 0.708.023, so this session deployed again from it; the server, the folder and the zip agree at 0.708.023. Two theme sessions deploying within a minute of each other can undo one another's ship; the fix is Chat's and the harness's to weigh.

## 5. One item withdrawn

The Pass card stands 3 taller than the school card beside it (285 against 282 at 1268). It was on Code's list to mend; it is not a fault. Its foot is 65 where a school's is 61, the struck price at 18 from Kain's Grow ruling (S127), and its head is 1 shorter. It stays as he ruled it.

OWED BACK: the pick written home in DSRD 9 section 36.9.

*No em or en dashes in this file; checked before writing.*
