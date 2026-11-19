**Needs from Chat: nothing. For your record and the school page's chapter 10.**

# SHIP: the school banners carry Kain's school building behind them, on 0.708.233 (S530 side session, 19 November 2026)

**What changed.** Each of the seven school banners used to carry a course picture, faded behind its floating picture. That was the film poster's course art, borrowed. It is now Kain's own school building, one picture for all seven. The picture is All Seven Schools In Banner Background Image, in the School Images (all variants) folder of the School Page images. Kain's words: "The school banner just needs to be the same as the course banner. It's just different images." The floating picture is unchanged: set 3, the school picture without the logo, in the course picture's place.

**How it is built.** The builder (tools/school_page_data.py) sets every banner's --course-art to images/schools/school-banner-wide.webp. That file is his picture set whole on a clear canvas of the course card's shape. school-page.css then follows his picks from round-sban:

- **Strength.** "Softer", 0.2. The course banner uses 0.3.
- **Centred top to bottom in the whole band, breadcrumb strip included.** His words: "central between the top and the bottom of the banner". Measured at 1270: 42 above the roof, 43 below the steps.
- **Moved 48 to the right.** His words: "move the whole thing to the right just a little bit". This was pick 2 of four, and he said "Yes, build option 2".

The layer narrows from the left, so nothing scrolls sideways. That was measured at 1024, 1270 and 1440 on NLP, Person Centred and Personal Growth. Below 1024 the banner keeps the course banner's own rules, at 0.2. Nothing else in the seven data files changed; this was checked field by field.

**Still open on the school page, all Kain's:**
- His courses line is three sentences, which DSRD 7 section 3.3 never allows. A two-sentence version in his words was put to him.
- His school cards (704 by 370) on the film, with four places for the play button, are in round-scard.
- The behind-the-scenes clean-up of the school page code waits behind the banner.

*No em or en dashes in this file; checked before writing.*
