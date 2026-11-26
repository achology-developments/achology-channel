> Chat S494, 26 Nov 2026: noted on Page Speed; fault 9 left as signed (FROM Chat ANSWER S494). Archived.
Needs: Chat to note the ship on the Page Speed card and on the click check report; one ruling owed (fault 9, below).
Done when: Chat has noted both and answered fault 9 or left it as signed.

# SHIP 0.708.511: the moving parts drawn the cheap way, and four click faults fixed (S580, 26 November 2026)

**Kain's yes.** Shown to him as one Before and After switch in the Change Viewer (previews/motion-s580, viewer proof passed); his words: "Yes, ship it".

## What changed and why

Phone speed, item 1's last part. Four animations made the browser repaint every frame, which kept a phone busy:
- The main buttons' shine (bf-sweep) moved its `left`; it now moves by transform. Measured the same to a hundredth of a pixel at every moment. buttons.css, and its copies in course-page.css and footer.css.
- The Read On card's ring on the school pages grew a box-shadow; it is now a disc of the same orange behind the arrow, grown by transform and faded by opacity, to the same reach (16 beyond the 48 arrow). school-page.css.
- The footer's Coming in 2027 words flow by background-position, which cannot be moved to transform without changing the look; the flow now rests while the words are off screen and runs while they are on it. footer.css and buttons.js.
- Complianz's cookie settings tab (computers only) slid by its bottom edge; it now slides by transform, same place and same half second. footer.css.

Pictures taken paused at set moments, at 1440 and 390, Before and After: the same every time.

Click check faults (REPORT__Site_Wide_Click_Check_S578, the S579 section):
- 6. Free course page: a press on a card's picture now picks the course (the card is its own layer, so the picture no longer sits over the hidden choice). gift-page.css.
- 7. Free course page and Enquiries: an email typed wrongly is said as soon as the reader leaves the field and cleared the moment it is right; an empty field stays quiet until Send (Code's call, so nobody is told off for passing through). gift-page.js, enquiries.js.
- 8. Help topic pages: the browser tab and shared title read "{topic}: Help | Achology", no longer "{topic} Archives | Achology". faq-setup.php.
- 10. Help answer at phone width: Escape closes Browse Help Topics and hands the keyboard back to its button. help-article.js.

**Not changed, fault 9:** after Show All on a Help topic page the list stays open. That is "Ten Then Show All" as Kain signed it; folding back would add a new button and words. Chat may rule otherwise.

## Proof

min/ rebuilt; the 35 packs rebuilt and each proved by derivation against its proved copy (only this session's rules differ; previews/motion-s580/pack_diff.py). Deploy proved local, server and zip agree at 0.708.511. Live check on achology.com (previews/motion-s580/live_check.js): all nine checks pass, no script errors on any page checked.

No folders added or moved.

*No em or en dashes in this file; checked before writing.*
