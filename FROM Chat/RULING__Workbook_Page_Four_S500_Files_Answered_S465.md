**For Code: the workbook page theme session. What this needs:** enter the rulings below in page_gate.py, image_gate.py and the workbook page's DSRD6_RECORD.md (Workbook Page design folder), and build the one small change in section 2. Each section names the TO Chat file it answers. Chat, Session 465, night, 12 November 2026, written in a side session of Chat's seat that Code's workbook page session opened under Kain's ruling RULING__Code_Starts_The_Chat_Session_Itself_When_It_Waits_On_Chat_S498.

DOCUMENT TYPE: ruling. Not a page spec.

This file asks Kain nothing directly. The one point that is his to see is in section 2, as a finished yes or no question for your walk of the Karpman page with him.

No copy is commissioned in this file. No word on any page changes.

Done when: the entries below are in page_gate.py, image_gate.py and the workbook page's record, with a gate run after them filed in the record, and the change in section 2 is built and shown to Kain in the walk.

## 1. DONE__Workbook_Page_Picture_Size_Lists_And_Three_Lines_Left_S500

**1.1 image-filename, the seven names ending "-768x994": change what the gate reads.** These are WordPress's own size copies, which DSRD 7 section 12.3 asks the page to offer. They are not export suffixes. Written home in DSRD 7 section 12.3: the rule is read on the upload's own name.
- **In image_gate.py,** `bad_filename` (or the check that calls it) judges a name ending `-{w}x{h}` by its upload's name when the same picture's srcset also offers a file named without that ending. The stripped name is judged again by the same rule, so a hand-made `photo-1024x768.webp` uploaded as the master still fails. A size ending with no upload beside it in the srcset still fails as "carries an editor resize suffix".
- **Prove it both ways** before calling it built: the Karpman page passes the line, and a planted hand-made name fails it (a green test that cannot fail is worse than none).
- **Mirror it** into the achology-factory copy of image_gate.py in the same job.
- **In page_gate.py:** nothing. This is a change to the reading, not an exception.
- **In the workbook page's record:** chapter for pictures, one line: "image-filename: WordPress's own size copies are read by the upload's name (DSRD 7 section 12.3, Chat S465 night); the line passes on the gate run after the change." Until the change ships, record the line as an instrument limit with this ruling named.

**1.2 spacing-scale, `kh-fr__live` padding 5: nothing moves.** It is already recorded: DSRD 7 section 4.3, Exception 19, "the further reading tag's padding of 5 (kh-band.css, a tag's drawn padding)". Moving it would change the Live tag and the Lessons chip on every reading page, in a block Kain signed at S164.
- **In page_gate.py:** add one entry to COMPONENT_SPACING_EXCEPTIONS, for the component wherever it renders, never by route, matched on the tag's own lines only, so any other off-scale space still fails. The pattern is of the form `^kh-fr__(live|chip) padding-(top|bottom) 5$`; check it against the gate's printed line before you write it. The ruling text: "the closing block's Live tag and Lessons chip, a tag's drawn padding of 5, DSRD 7 section 4.3 Exception 19, recorded for the component wherever it renders (Chat S465 night)".
- **In the workbook page's record:** spacing chapter, one line naming Exception 19 and the carve-out. Articles, book notes and quote pages inherit it with no new line, because the entry is by component.
- Written home: DSRD 7 section 4.3, Exception 19, now names its place at the gate.

**1.3 Section 2's two pictures with no size list.** Noted for BRIEF__Pictures_Sized_For_Every_Screen_Across_The_Theme: the course cover in Where This Workbook Comes From (`course-quote-cover-007.webp`, a theme file with no smaller copies), and the shared top band's phone cover in the Soft Light hero, which is on all four reading pages. Both wait on that job. In the record, the image-responsive line names them as waiting on that brief. Nothing else.

## 2. RULING__Workbook_Lower_Dark_Card_Is_One_Line_S500

**2.1 Kain's pick is written home** in DSRD 9 section 37.8, in his words ("Yes, One Line"), with the 1200 start and the reason for it.

**2.2 The keyboard order below 1200: make the eye match the markup.** Below 1200 the card shows the tick box above the button while the markup has the button first, so a keyboard meets them in the other order. The mend is to drop the `order: -1` rule in workbook.css (the `max-width: 1199px` block for `.wb-capture--body .wb-capture__ok`), so below 1200 the card shows the button, then the tick box under it, as the hero does at every width. Then the eye and the keyboard meet one order at every width, and the two forms on the page match. No word, field or size changes.
- This is a change Kain can see on a card he signed, and the two dark cards are one family, so build it and show it to him as one Before and After in your walk of the page. The question, finished: **"Below a computer's width, the lower card's tick box sits under the button, as it does in the top form. Keep it?"** My recommendation is yes: one order for the eye and the keyboard, and the same as the hero.
- If he says no, put the `order: -1` back, and record the order difference in the record's keyboard chapter for the site's one screen reader read before launch (Kain's ruling at S484).
- **In page_gate.py:** nothing.
- **In the workbook page's record:** keyboard chapter, the order at 1440, 1100, 834 and 390 after the change, read by tabbing through the card.
- Written home: DSRD 9 section 37.8, as my call and his to overturn.

## 3. RULING__Workbook_Page_Board_S500

**3.1 Kain's four rulings are written home** in DSRD 9 section 37.8, each in his words: the steps on a phone as one row with the number and name on one line; the heading and its line on the left at every width; on a phone the course picture 200 and centred with its button; on a phone the lower dark card centred with a 180 cover.

**3.2 The centred-block exceptions for How This Workbook Helps You Learn come out.** That block is now left-aligned on Kain's word, its line the Lead with Bar by its class, and its spaces declared on the scale (16 and 24). An exception left on a block it no longer describes would hide a real fault later. So:
- **In page_gate.py, the workbook route `^/learn/[^/]+/workbooks/[^/]+/$`:** take out every entry for "How This Workbook Helps You Learn", both the centred line pair (`line-type`, `line-bar`) and the night ruling's spaces (`gap-heading-line`, `gap-line-next`), at all three widths. Keep every entry for "Ready to Further Your Learning?" exactly as it is. Update the route's comment to say why the four went.
- **Before you edit,** check the file for another session's uncommitted changes (git status, then git diff on page_gate.py). If there are any, leave them alone and change only your lines.
- **Then run the gate.** If How This Workbook Helps You Learn passes, record it so. If it fails on a line, that is a fault to mend in the build to the scale, not an exception to put back; report the reading in your DONE.
- **In the workbook page's record:** strike the lapsed exceptions, naming this section, and file the gate run.
- Written home: DSRD 9 section 37.8, the exceptions paragraph, now says they lapsed.

**3.3 Section 5's fixes nobody can see** are answered in section 1 above. The "stretched" course picture is closed by your own read at 0.708.029: it was never out of proportion, only given too small a file, and the 704 entry mends that.

## 4. RULING__Workbook_Browse_More_Title_Endings_S500

**4.1 Kain's pick is written home** in DSRD 9 section 22.16a item 4, where the Browse More rules live, and in section 37.8, in his words ("4 Ending as a note please"). DSRD 8 holds no Browse More table, so there is no DSRD 8 home to write; section 37.8's pointer to "DSRD 8, the Browse More decisions, row 9" is corrected to section 22.16a.
- Your section 4 point stands as built: the note reads the post's own title. No title or search title is changed for it.
- **In page_gate.py:** nothing. **In the workbook page's record:** one line in the reading chapter that a screen reader hears each whole title, as you read it at 0.708.024.

## 5. What Chat wrote home tonight

- DSRD 9 section 22.16a item 4: the ending note on workbook pages.
- DSRD 9 section 37.8: One Line, the board's four rulings, the ending note, the keyboard order call, the lapsed exceptions, Exception 19 at the gate, and the size copy reading.
- DSRD 7 section 12.3: WordPress's own size copies are read by the upload's name.
- DSRD 7 section 4.3, Exception 19: its place at the gate, by component.

The four S500 files are archived in the channel Archive.

*No em or en dashes in this file; checked before writing.*
