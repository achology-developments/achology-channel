**For Chat. What this needs from you:** write Kain's pick home (DSRD 9 section 37, beside the two dark cards), and rule on one keyboard order point below a computer's width (section 4). Code, theme session S500, 11 November 2026.

**DOCUMENT TYPE:** ruling. Not a page spec.

# RULING: the workbook page's lower dark card is One Line

## 1. Kain's words

At the S500 open: "the lower dark card shown beside the side panel as a pair". When it came up: "Yes, show me". On two switches in the Change Viewer, One Line switched on as Code's recommendation: "Yes, One Line".

## 2. The round

previews/workbook-foot-s500 in the theme, mp/round-1.js, two switches, one or the other: the tick box under the fields' icons (the smallest change), and One Line. Proved by tools/viewer_proof.py before it opened (7 measured, 0 failed). The two dark cards are never on screen together: the side panel leaves before the lower card arrives, and Kain was told so.

## 3. Built (theme 0.708.018 to 0.708.020, commits 93975ea8, ee7dcf27, c2d79114 and b6ea27e2, deployed)

- From 1200 wide the lower dark card's name, email and button are one white bar, the tick box on a quiet line under the bar's first icon, as the hero. The fields, the button and the tick box are the signed ones. No word changes.
- The template now writes the button before the tick box in this card, as in the hero, so a keyboard meets them in the order the eye does at computer width. The side panel keeps the tick box, then the button.
- **Below 1200 the card looks exactly as it did.** The round said "computer and tablet", and that was wrong: read back on the build site, the card is 680 wide below 1200 and the cover takes 172 of it, so a bar left the email field 26 wide at 834, 1024 and 1100. I deployed that for a few minutes, found it in the read-back, and moved One Line to start at 1200, where the card is 984. Kain was told.
- Read back in WebKit at 1440 and 1200 (the bar 742 wide, the email field 328, the tick box on the same edge as the first icon), and at 1100, 834 and 390 (the card as built, the tick box above the button). The tick box ticks and unticks at all five. No sideways scroll. css_gate passes workbook.css.
- Page: https://achologytest.com/learn/psychology/workbooks/karpman-drama-triangle-workbook/

## 4. One point for you

Below 1200 the eye still meets the tick box, then the button, as built, but the markup now has the button first, so a keyboard there reaches the button before the tick box. It is the price of one markup serving both arrangements. The other way round would put the same mismatch at computer width, where One Line is. Say if you want it the other way, or the card rearranged below 1200 so the button stands first.

OWED BACK: the pick written home, and your word on section 4.

*No em or en dashes in this file; checked before writing.*
