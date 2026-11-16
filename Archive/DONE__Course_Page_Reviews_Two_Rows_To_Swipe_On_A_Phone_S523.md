> CHAT DISPOSITION, S470: DONE. Recorded in the course page signed spec, section 10 item 7.

DONE: nothing needed from Chat. A ship brief, for Chat's picture of the build.

# Course page reviews on a phone: two rows to swipe (pick 325, 0.708.086)

**What changed.** On every course page, under 768 wide, the What Students Say wall no longer stacks three films and four reviews one under another. The three films stand in one row and all six reviews in a row beneath. Each row is swiped sideways, runs to the screen's edges, and shows the next card at the edge. The wall stands about 520 tall where it stood about 1,900. Every card still turns to its next review on a tap. From 768 up nothing changes.

**Why.** Kain, on his walk of the Diploma page, 16 November 2026. Four ways were shown in the one Change Viewer (round 10 of the course outcome cue preview folder in the theme's previews); he chose the first: "Yes, build 1".

**Where.** The theme's course page stylesheet and script, the reviews wall only. No stored page data was touched: the script gathers the cards into the two rows on a phone and puts them back in their own order from 768 up. Without the script a phone keeps the one column it had. Recorded as pick 325 in the course page picks record.

**Proof.** Measured in WebKit on the build site at 360, 390, 767, 768, 1024 and 1440 on the Diploma and the Mental Health Practitioner Diploma: every card turned twice, the width taken across 768 and back both ways, no word leaves its card, no page wider than its screen, no script error. A first cut of mine put the rows in the wrong state after a width change; found in my own check, mended before the ship.

**Not done.** The course page's DSRD 6 record and Chat's Safari read are untouched by this; the course page is not called finished. Not tried on a real phone by hand; the swipe itself is the browser's own sideways scroll.

*No em or en dashes in this file; checked before writing.*
