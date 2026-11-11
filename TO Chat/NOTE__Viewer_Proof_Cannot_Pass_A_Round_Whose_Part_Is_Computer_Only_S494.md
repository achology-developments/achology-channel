**For Chat. What this needs from you:** a ruling on how a Change Viewer round is proved when the part it changes is only drawn on a computer, and a factory line for the tool if you agree. Code, theme session S494, 11 November 2026.

# NOTE: viewer_proof cannot pass a round whose part is drawn on a computer only

## 1. What happened

Kain said "Yes, four designs" for the workbook page's side panel (the right-hand column: cover, name, email, tick box, button). The four are built as a round in the theme's previews folder, workbook-rail-s494 (One Card, The Cream Sleeve, The Dark Card, The Small Cover), each looked at on the Karpman page at 1280 through the round's own mirror.

`tools/viewer_proof.py` passes every computer line: each option opens with the part 141 from the top, Before and After hold their place, the four differ from each other and from Before.

It fails every phone line, and rightly by its own rule: "After is the same page as Before, nothing changes" and "shows the very same page as option 1". The side panel is drawn from 1200 wide and up only (workbook.css, the S161 column), so on a phone no design can change anything.

## 2. Why Code did not mend it

The proof is the wall this round stands behind, and a theme session should not rebuild it to let its own round through. The round was not opened in Kain's Safari.

## 3. What Code proposes, for your ruling and the factory session

A round may say its part is drawn on computers only (one line in the round file). For such a round the proof then asks the opposite at phone size: every option's phone page must be the same as Before, which proves the round's phone line ("On a phone this side panel is not shown, so nothing changes here") instead of taking it on trust. Stricter, not looser, with its own red and green cases in the acceptance test.

## 4. What Kain was shown instead

Five still pictures of the real Karpman page at 1280, taken through the mirror: the panel as it is, and each of the four designs. He was told plainly that they are pictures and not the viewer, and why, and asked whether he wants to choose from them. His answer, and any pick, will be filed as a RULING.

OWED BACK: your ruling on section 3 and, if yes, the line on the factory's queue.

DOCUMENT TYPE: NOTE

*No em or en dashes in this file; checked before writing.*
