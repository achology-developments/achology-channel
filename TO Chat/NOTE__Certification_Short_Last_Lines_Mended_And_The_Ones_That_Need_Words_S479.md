**For Chat. What this needs from you:** one ruling, in section 3: how the last short lines on the Certification page are mended, since they sit in the site's shared FAQs block. Code, theme session S479 (Certification Page Final Touches), 11 November 2026.

# 1. What was done

Kain's rule of 10 November 2026, as your S462 ruling records it: "no line of one, two or three words on a rendered page, at computer and phone width". It is in no standard yet and has no check, so I measured the Certification page against it by hand-built measure, in WebKit (Safari's engine), at 1268, 834 and 390: every heading, paragraph, list line and table cell in the page's main, counting a fault where the last line holds one to three words and fills under 60 per cent of its column (a heading that breaks into two even lines is not a fault).

Found: 3 at 1268, 9 at 834, 14 at 390. Among them: the banner's sentence ending "Achievement too." on a phone; five of the six Is and Is Not cells on tablet and phone ("practise.", "with others."); both Which Path paragraphs on a phone ("its lessons."); the check block's "code." and "(DiMAP)" on a phone; the close's sentence ending "Competency and Achievement." on a computer.

Mended as theme 0.707.943 (commit 3c0224ce, pushed, deployed, three proofs passed): those texts are set in even lines at the widths where each fault was measured, and nowhere else, so the line counts Kain agreed on a computer stand (the cells' three lines, Which Path's five). No word changed and no design changed. Measured again on the build site: one fault left at each width, section 3. The even lines do not leave a narrow ragged column: the cells fill 82 to 93 per cent of their room on tablet and phone, the path paragraphs 91 and 96 on a phone.

Status in The Harness's words: changed, verified 3 of 3 widths; the page stays built, gate open.

# 2. One earlier decision changed, named

A phone rule on the Which Path paragraphs had set plain wrapping, with the note "on a phone the evened wrap left a short ragged column". Plain wrapping is what ended both paragraphs on two and three words. It is now the careful wrap; measured in WebKit at 390 the paragraphs fill 91 and 96 per cent and end on seven and six words.

# 3. What Code needs from you

The one fault left at each width is a summary line inside the questions, which is the site's shared FAQs block, not this page's to restyle:
- at 1268, the summary under "Will employers recognise my Achology certificate..." ends "own qualification." (31 per cent of its column);
- at 834 and 390, the summary under "How do I explain Achology qualifications..." ends "to their needs." (34 per cent).

Two roads, yours to choose: (a) you re-cut those two Help summaries by a word or two; or (b) a theme queue line to set every summary in the FAQs block in even lines, site-wide, as a component change (it would mend every page that uses the block, and it changes how every summary breaks). I recommend (b), because the same fault will be on every page that carries the block and words cannot be cut for three widths at once.

Also for your list: the rule wants its line in DSRD 7 and a machine check (your S462 ruling says so). The measure used here is the start of that check: last line of one to three words and under 60 per cent of the widest line, in WebKit.

OWED BACK: your choice of (a) or (b), to FROM Chat, for the theme session.

DOCUMENT TYPE: NOTE

*No em or en dashes in this file; checked before writing.*
