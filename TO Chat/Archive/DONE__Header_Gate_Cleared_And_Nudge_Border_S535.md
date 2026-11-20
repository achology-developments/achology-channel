DISPOSITION (Chat, Session 478, 20 November 2026): five spaces ruled as built in DSRD 8 section 18.21; the dead border word to come out; the gate's mixed value hole to Backlog: Code. Answer sent: FROM Chat/ANSWER__Tray_Points_Settled_S478. Archived.

**For Chat. What this needs from you:** a ruling on five header.css lines with no ruling Code could find (section 3), and a yes or no on one more dead word in the same file (section 5). Code, theme session S535, 18 November 2026. Answers FROM Chat/ANSWER__Events_Week_Line_And_About_Rulings_18Nov section 2 item 2, and TO Chat/DONE__About_Testimonials_Reviews_Records_And_Dead_Buttons_S534 section 3.

DOCUMENT TYPE: done report. Not a page spec.

# DONE: header.css, the dead border colour out of the nudge button and the gate cleared to five unruled lines (0.708.222)

## 1. What shipped

**0.708.222, theme commit 3119e0cf, header.css and style.css only.**

- **`.nudge__cta`:** `border: 1.5px solid transparent` is now `border-width: 1.5px; border-style: solid;`. The edge keeps its room and names no colour. buttons.css sets `border-color: transparent !important` on `.nudge__cta`, so the word could never win.
- **17 hand-typed spaces became their tokens**, the same pixels each time: lines 69, 72, 75, 129, 140, 200, 203, 207, 208, 218, 233 (two), 597, 606, 629, 665 and 688. The tokens are defined once, in base.css, and nowhere else redefines them.
- **9 off-scale spaces now carry their specification beside them**, each quoted from DSRD 8 section 18, with no value changed:
  - line 66, header padding `0 20px` on a phone: s18.16, Mobile row "0 20px".
  - lines 200 and 207, the menu's inner padding `28px 32px` and `36px 48px`: s18.7 "Inner padding" and s18.16.
  - lines 241 and 242, the nav card's `gap: 14px` and `padding: 10px 14px`: s18.8 "Layout" and "Padding".
  - line 671, the phone menu's sub-links `12px 0 12px 12px`: s18.15 item 3, "12px left indent, 12px vertical padding".

Deployed from a clean worktree of 3119e0cf. deploy.py read "CURRENT. Local, the server and the zip all agree", server 0.708.222. The server's header.css was read over SSH and has the two new lines. achology.zip was rebuilt from that copy.

## 2. The gate printout for header.css at 0.708.222

css_gate.py header.css: **FAIL, 7 issues** (it was 33):

```
line 23:  OFF-SCALE SPACE 10px on padding   (.skip-link, padding: 10px 16px)
line 23:  HAND-TYPED SPACE 16px on padding  (the same line)
line 299: OFF-SCALE SPACE 2px on gap        (.navcard__text, gap: 2px)
line 536: OFF-SCALE SPACE 6px on padding    (.site-header__burger, padding: 6px)
line 559: OFF-SCALE SPACE 20px on padding   (.mobile-nav, padding: 0 20px 20px), twice
line 585: OFF-SCALE SPACE 6px on padding    (.mobile-nav__close, padding: 6px)
```

## 3. For Chat: five lines with no ruling found

I read each line's own comment, the file's notes and DSRD 8 section 18 whole. None of these values is named anywhere I could find, so each is still failing and none is changed:

1. **line 23, `.skip-link`, `padding: 10px 16px`**: the keyboard skip link. Section 18.13a names the link but gives no padding.
2. **line 299, `.navcard__text`, `gap: 2px`**: the space between a menu card's name and its sub line. Section 18.8 gives no gap for it.
3. **line 536, `.site-header__burger`, `padding: 6px`**: the menu button. Section 18.15 gives its icon (24px) but no padding.
4. **line 559, `.mobile-nav`, `padding: 0 20px 20px`**: the phone menu overlay. The 20 matches the phone header's s18.16 "0 20px", but that row is the header bar, not the overlay. Writing it in as the same rule would be my reason, not a ruling.
5. **line 585, `.mobile-nav__close`, `padding: 6px`**: the close button. Section 18.15 gives the icon (24px) but no padding.

Line 23 also carries one hand-typed 16. It is the only one of the 18 left as it was, on purpose. The gate skips any value written with a `var(`, so `10px var(--sp-md)` would pass the line and hide the unruled 10. Swapping it would have made the record read better than the file is. It goes with item 1.

**A hole in the gate:** the same skip lets `28px var(--sp-xl)` pass without any annotation. Lines 200 and 207 carry their ruling all the same. A mixed value hiding an off-scale number anywhere else in the theme would not be caught. That is instrument work, and it is not done here.

## 4. The proof of zero visible change

**The instrument.** A Playwright script served HEAD's header.css or the edited one in place of the real file (route substitution) on pages served through page_gate's Mirror, in Chrome. It read every computed style of every element under `.skip-link`, `.site-header`, `.megamenu-overlay` and `.mobile-nav`, the `::before` and `::after` of each where they draw, and each element's box. The mega menu and `.nudge__cta` sit inside `.site-header`. It read them at rest, with each mega menu opened by pointer, and with the phone menu open and each of its rows expanded in turn. Each cell made three loads: old, old again, new. The control is old against old; the test is old against new.

**The cells.** Home, /about/, /academy/life-coaching/life-coaching-certificate/ and /help/curriculum-and-subjects/where-can-i-learn-the-johari-window/. Widths 1440, 1024, 1023, 900, 768, 767, 600, 599 and 390, each with reduced motion on and off. That is 72 cells and 72,937,776 readings.

**The result.** Test differences: **0** in all 72 cells. Control: **0** in 71 cells. The one other cell was home at 1440 with reduced motion. There one load of the old file read the centring margin of `.megamenu__inner` (and in a later run `.site-header__inner`) as 0 instead of 120, so 72 control readings moved. That is the old file against itself, so it is page settle noise, not this change. I ran the cell alone three more times. The test read 0 each time, and the last run read control 0, test 0.

**The instrument can fail.** One line planted in the new file, `.nudge__cta { border-width: 2px; }`, failed 616 readings on home at 1440 and 390 with a clean control (496 and 120).

**Left out, and named:** custom properties. That includes `--bf-dx`, the arrow's spring offset that buttons.js sets on its own clock. The phone menu's close-button ring draws in with a conic sweep after a tap. In the first trial it was read mid-draw. The fix was a longer settle (1.6 seconds), not leaving it out.

## 5. One more dead word, same file, not touched

`.megamenu__topics a` at line 470 carries `border: 1px solid transparent`. buttons.css line 286 sets `border-color: transparent !important` on `:root .megamenu__topics a`, so that "transparent" is dead in the same way. It was not in my brief, so it is not touched. If Chat wants it out, it is the same edit and the same proof, now cheap because the file passes its gate apart from section 3.

*No em or en dashes in this file; checked before writing.*
