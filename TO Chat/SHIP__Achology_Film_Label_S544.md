NEEDS FROM CHAT: nothing to act on; read for the record. The three watch lines in ANSWER__Course_Intro_Videos_Links_And_Card_Words_S544 section 3 are retired by Kain's ruling.

# SHIP: the Achology film's name and time over its picture, theme 0.708.363

**For:** Chat. **From:** Code, branch 3 of the S544 theme sitting.

## What changed

- Wherever the Achology film (Vimeo 708764177, 2:15) plays as a page's first film, the words "So, What Is Achology?" sit on the left of its top edge and "2:15" on the right, in white on a soft dark fade that runs down from the top, with no panel. The play button stays centred.
- Four pages carry it: the School of Person-Centred Counselling and Psychology, the School of Personal Growth, the Access All Areas Pass (it plays the same film) and Membership.
- It is the About banner's own label, one component, not two: the same span and classes (about.css .about-banner__label, __label-title, __label-time, built by the About banner session at 0.708.360 to 0.708.362). No new CSS was written; about.css already loads on all four pages. The About banner session was told so and asked to keep those rules unscoped.
- The sources write it, so every later run keeps it: tools/school_page_data.py (ACHOLOGY_FILM_LABEL and achology_film_label, used for the two schools and by tools/pass_page_data.py) and previews/membership-page/build.py. The four stored page files took one line each.
- The watch-line round is retired. No watch-line sentence was ever placed on a page; its preview files left the theme in the About session's commit 543f3342.

## Why

Kain, 22 November 2026, through the main session: "No, Claude, definitely not. Just the text. So, What Is Achology? ... Each word beginning with a capital letter ... That's not an appropriate place to put in a sentence."

## Proof

Measured on the build site at 1280 and 390 on all four pages:
- Box 440 by 248 at 1280 and 350 by 197 at 390.
- Title Como 16/600 at 1280 and 14 at 390, on one row; time Mulish 14 and 12. Both sit 16 in from the edges.
- The play button is exactly centred, and the words end above it.
- Nothing scrolls sideways, and no picture is broken.
- A click on the words still opens the film.

The contrast was read as the About session reads it: the words hidden, the lightest pixel behind each set against white. At 1280, 1024, 768 and 390 the worst is 4.54 to 1, on the Person-Centred school at 390; every reading passes 4.5.

## Page gate at 0.708.363

- Person-Centred school: 44 pass, 0 fail.
- Personal Growth school: 44 pass, 0 fail.
- Access All Areas Pass: 43 pass, 0 fail. Its first run failed on image-lazy-below-fold, because the recorded exception still named the old film-pass picture. That was left over from the thumbnail swap at 0.708.355. page_gate.py now names pass-intro-960.webp, as it already did for Membership's picture.
- Membership: 44 pass, 1 fail. The fail is rank-math (post 45034 never scored), as before this change. It is Kain's one-click rescore, not this work.

## Seen in passing, not this change

The Person-Centred school's first block breaks one paragraph oddly at 1280 ("you experience the / ideas for yourself first, and take away lived experience you / can use"). That is the page's line-lay script, not the film. It was told to the main session.

## Links

- https://achologytest.com/academy/person-centred-counselling/
- https://achologytest.com/academy/personal-growth/
- https://achologytest.com/access-all-areas/
- https://achologytest.com/membership/

*No em or en dashes in this file; checked before writing.*
