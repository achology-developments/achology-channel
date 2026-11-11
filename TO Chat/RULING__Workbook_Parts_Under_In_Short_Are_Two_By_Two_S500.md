**For Chat. What this needs from you:** write Kain's pick home (the workbook page spec and DSRD 9 section 37). Code, theme session S500, 11 November 2026.

**DOCUMENT TYPE:** ruling. Not a page spec.

# RULING: the parts under the In Short note are Two by Two

## 1. Kain's words

On the built Karpman workbook page, with a picture of the block: "This block just looks, it's just words dumped on a page. It doesn't really seem to be doing much for the page. I'm just wondering if there's a way we could make that a bit more visually impressive." On four designs in the Change Viewer: "Yes, Claude, I do like the 2x2 ... there's the heading ... And then the text, within the cards is the same as well. It's just all very, very samey ... I'm definitely drawn towards the 2x2, but it's still not quite right." Shown Two by Two with four switches, two of them on: "Yes, build it".

## 2. The rounds

previews/workbook-steps-s500 in the theme. Round 1, four designs: 1 Names Stand Alone, 2 Two by Two (Code's recommendation), 3 Cream Cards, 4 One Cream Panel. Round 2, four switches on Two by Two: the opening line with the bar and quieter sentences (both recommended and on), orange names, bigger names (both off). Each round proved by tools/viewer_proof.py before it opened (11 measured, 0 failed). He chose Two by Two with the two switches that were on. PICKS.md holds both rounds.

## 3. Built (theme 0.708.007 and 0.708.009, commits fb1ad75b and 713559f1, deployed)

- The opening sentence of the block is the site's Lead with Bar, switched on in single-workbook.php by its class, never copied (DSRD 7 section 3.3).
- The parts stand in two columns, each under a thin line that starts with a short orange piece. Each name stands on its own line in the heading face at 21. Each sentence is the page's quieter text, 16 at line height 1.6 in soft grey, as the step sentences under How This Workbook Helps You Learn. A lone last part runs the full width. One column on a phone.
- The parts carry no numbers: the block prints each record's `workbook_parts`, an idea's parts, four or five of them, and they are not always steps.
- No word changes. The block is in workbook.css; nothing else on the page moved.
- Read back on the build site in WebKit: Karpman at 1440 (the block 413 tall, the bar outside the column, 24 from the lead line to the parts), Ikigai at 834 (two columns, five parts, the fifth full width), Circle of Concern at 390 (one column). No sideways scroll at any of the three. css_gate passes workbook.css.
- Page: https://achologytest.com/learn/psychology/workbooks/karpman-drama-triangle-workbook/

## 4. One thing you should know

Karpman's block still prints the four steps, one of the 38 records you ruled are rewritten to the idea's own parts. The design holds either way; it was judged on Ikigai's five long parts as well.

OWED BACK: the pick written home.

*No em or en dashes in this file; checked before writing.*
