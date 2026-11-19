**Needs from Chat: nothing. For your record and the school page's chapter 10.**

# SHIP: the school banners carry Kain's school building behind them, on 0.708.233 (S530 side session, 19 November 2026)

**What changed.** Each of the seven school banners used to carry a course picture, faded behind its floating picture. That was the film poster's course art, borrowed. It is now Kain's own school building, one picture for all seven. The picture is All Seven Schools In Banner Background Image, in the School Images (all variants) folder of the School Page images. Kain's words: "The school banner just needs to be the same as the course banner. It's just different images." The floating picture is unchanged: set 3, the school picture without the logo, in the course picture's place.

**How it is built.** The builder (tools/school_page_data.py) sets every banner's --course-art to images/schools/school-banner-wide.webp. That file is his picture set whole on a clear canvas of the course card's shape. school-page.css then follows his picks from round-sban:

- **Strength.** "Softer", 0.2. The course banner uses 0.3.
- **Centred top to bottom in the whole band, breadcrumb strip included.** His words: "central between the top and the bottom of the banner". Measured at 1270: 42 above the roof, 43 below the steps.
- **Moved 48 to the right.** His words: "move the whole thing to the right just a little bit". This was pick 2 of four, and he said "Yes, build option 2".

The layer narrows from the left, so nothing scrolls sideways. That was measured at 1024, 1270 and 1440 on NLP, Person Centred and Personal Growth. Below 1024 the banner keeps the course banner's own rules, at 0.2. Nothing else in the seven data files changed; this was checked field by field.

**Signed.** Kain, on the built NLP page in Safari, 19 November 2026: "Yes, it's right".

**Then 0.708.234 (commit 9137daff): each school's own picture on its film.** Kain made eight film pictures: the seven schools and the Access All Areas Pass. They are in School Film Pictures, inside the School Images folder, all 1408 by 740, the course card's shape. Each school's film now shows its own picture instead of a borrowed course picture. The builder writes it as film-{code}.webp at 704, 540 and 360, using the course film's own sizes. The picture sits on the film exactly as a course picture sits on a course film, with the play button in the middle. Measured on all seven at 1270, and on NLP at 390: every picture loads at the 540 copy. film-pass.webp is made and is waiting for the Access All Areas Pass page, which belongs to that page's own session. This supersedes the school cards on the film (round-scard), which no page uses.

**Then 0.708.235 and 0.708.236: Kain's second film designs.** He redrew all eight and re-uploaded the folder; the whole bulb now sits inside each picture. The film copies were remade under the same names. Each picture's address now carries a fingerprint of its contents (?v=), because the theme's pictures are kept by browsers for a year. Removed from the theme because no page uses them, though git keeps them: the school cards, and the wide bulb and icon copies from this session's rounds. The old designs in his School Film Pictures folder were replaced by the new ones.

**Still open on the school page, all Kain's:**
- His courses line is three sentences, which DSRD 7 section 3.3 never allows. A two-sentence version in his words was put to him.
- His sign-off on the new film pictures.
- The behind-the-scenes clean-up of the school page code waits behind the banner.

*No em or en dashes in this file; checked before writing.*
