DISPOSITION (Chat, S464, 11 November 2026): answered in FROM Chat RULING__Postbag_Rulings_For_The_Theme_Sessions_S464 section 1; DSRD 7 3.3 written. Archived.

**For Chat. What this needs from you:** write Kain's ruling into DSRD 7 section 3.3 (the Lead with Bar), and rule on its reach to the course pages (section 3). Code, theme session S479 (Certification Page Final Touches), 11 November 2026.

# RULING: the supporting line's orange bar hangs outside the text container

## 1. Kain's words, 11 November 2026, in this sitting

Shown the Certification page for his own read, he sent a picture of How Someone Can Check Your Certificate and its supporting line and said: "Can you see what the problem is with a subheading, Claude? We have one simple rule, don't we? That all text, lines up against the container, which means that the little orange hairline sits actually outside of the actual text container. Can you see this? I'm not sure why this is broken."

The fault: the bar stood on the container's edge and the line's words stood 18 in from it (the 2 bar and its 16 inset), so the words did not line up with the heading above or the content below. It was built that way from the course page's Lead with Bar (course PICKS.md 221), and the comment in certification.css describes DSRD 7 3.3 as "a 2 orange edge on its left, 16 in".

## 2. What is built

Theme 0.707.944 (commit dd739631, pushed, deployed). The page to open: https://achologytest.com/certification/#check

The line is pulled left by the bar and its inset, so the words stand on the container's edge and the bar stands in the gutter: the rule DSRD 7 4.4 gives a panel (it bleeds so its words sit on the column edge). 16 between bar and words from 768 up; on a phone, where the gutter is 20, 8 between them, which leaves 10 from the bar to the screen's edge. It reaches every supporting line on Certification (six sections and the stance block) and the close's line, and, because the rule is one declaration in certification.css for both pathway pages, the Accreditation sections that carry the Lead with Bar and its close. No word changed.

Measured on the build site in WebKit at 1268, 834 and 390, all seven lines on Certification: the first word's left edge equals the heading's (154 and 154; 32 and 32; 20 and 20); the bar stands at 136, 14 and 10; nothing sideways.

Status in The Harness's words: changed, verified 3 of 3 widths on Certification; Accreditation not measured by me (it is the other theme session's page; that session is told). The deploy tool's first proof did not close on this ship: one file on the server, the course page stylesheet, did not match the folder, because the course page session was changing it at that moment; it is that session's file, its own ship (0.707.945) follows, and that session is told to verify.

## 2a. Kain's own read of the whole Certification page, the same sitting

After the bar was mended and shown, asked whether the rest of the page is right: "Yes, it's right" (11 November 2026). Recorded in his words in the page's DSRD 6 record; the chapter lines that rest on his eye (10 and 11) are yours to mark from it. Folded back the same session: PROTOTYPE__Certification_Page_S479_APPROVED.html in the Certification Page design folder, the whole page as the server rendered it (all eight sections). The S364 prototype is superseded by it; whether that file stays as the signed spec's own artefact is yours to say. The block-only export made an hour earlier is removed, since the whole page now holds it.

## 3. What Code needs from you

1. **DSRD 7 3.3** gains the sentence: the Lead with Bar's bar hangs outside the text container; the line's words stand on the container's edge. Kain's words above are its ground.
2. **The course pages carry the same line eight times** (the What You Will Learn line, the certificate, curriculum, reviews, pricing, free lessons, questions and close lines; course-page.css), each with the bar on the container's edge and the words 18 in. Kain's rule is "all text lines up against the container", so they are the same fault. Kain froze the course page's design on 10 November ("no more redesigns"). Is this a fault mended under the rule, or a change that waits? It is the course page session's file; that session is told.
3. On Accreditation, one more line of the same kind lives in accreditation.css (the level panels' New at This Level note): the Accreditation session's, and it is told.

OWED BACK: the DSRD 7 line and your ruling on section 3 item 2, to FROM Chat.

DOCUMENT TYPE: RULING

*No em or en dashes in this file; checked before writing.*
