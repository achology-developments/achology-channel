**For Chat. What this needs from you:** write Kain's four rulings home (DSRD 9 section 37), and note that the centred-block exceptions you recorded for How This Workbook Helps You Learn now sit on a left-aligned block (section 4). Code, theme session S500, 11 November 2026.

**DOCUMENT TYPE:** ruling. Not a page spec.

# RULING: the workbook page board, four changes built in one go

## 1. Kain's words

On the way of working: "can I ask you now if there's a way we could start working a bit more optimally? Taking one item at a time. Is there any way that we could take all of the items at the same time? ... This is just taking like a long time here." Offered one board, each row already built with Code's recommended fix: "yes".

On the board, in one message:

- Row 1, the steps on a phone: "I'm looking at option number 1, steps on a phone. I'm saying yes to that. However, it seems to me that we're kind of creating a bit more white space in what we need to. It would seem to me that on a phone, that learn should just be in the same line as the actual round number. That would allow us just to drop a little bit of white space. Maybe make the block a little bit neater."
- The course picture and its button, his own ask: "on a phone, that they explore this course call to action. We might as well kind of probably centralize that. With the course image, and you might as well kind of make that larger too."
- The lower dark card, his own ask: "And then get your free workbook. I might as well increase the size of the workbook, and essentially centralize all that as well."
- Row 2, the heading: "In terms of the second heading on the left, yeah, let's just go with that."

## 2. The board

previews/workbook-board-s500 in the theme, board.js, board name workbook-page: 1 Steps on a Phone, 2 Heading on the Left, both Code's recommendations. Proved by tools/viewer_proof.py before it opened (7 measured, 0 failed). A third item, the empty space beside the In Short note, was measured and taken off the board: the side panel waits only while the top form is on screen, and a fix moved it by 50 to 90 of scrolling. Kain was told. PICKS.md holds it.

## 3. Built (theme 0.708.026, commit 919bc2dc, deployed)

- **On a phone, each step of How This Workbook Helps You Learn is one row:** a 96 sheet at the left, the number disc (32) and the name on one line beside it, the sentence under them, read from the left. The block is 1,119 tall on Karpman where it was 2,305.
- **The heading and its line stand on the left edge** at every width, the line as the Lead with Bar by its class in the template, at the reading width. The four steps keep their centred captions on a computer and a tablet.
- **On a phone the course picture is 200 wide and centred, and Explore This Course is centred above it.** The button stays above the picture, as the markup has it.
- **On a phone the lower dark card is centred:** its cover 180 wide, its heading and line centred, the fields and button the full width as before.
- No word changes. The new stylesheet was laid over the built page in WebKit at 1440, 1200, 1100, 834 and 390 on two workbooks before the deploy, and the built page read back the same after it. No sideways scroll. css_gate passes workbook.css.
- Page: https://achologytest.com/learn/psychology/workbooks/karpman-drama-triangle-workbook/

## 4. One thing for you

Your night ruling (3.1) recorded How This Workbook Helps You Learn's spaces as exceptions "inside blocks Kain signed", as a centred block. It is now left-aligned on his word, with 16 declared under the heading and 24 declared above the steps. I have left your entries in page_gate.py as they are, because another session holds uncommitted changes in that file tonight. Say whether they stay or come out; the block's line type and bar entries no longer apply and can come out with them.

## 5. Not yet done

The fixes nobody can see, which I told Kain would go in the same build, are not made yet: the stretched course picture, the shared `kh-fr__live` padding, the pictures with no srcset and the resize-suffix file names. They are next.

OWED BACK: the four rulings written home, and your word on section 4.

*No em or en dashes in this file; checked before writing.*
