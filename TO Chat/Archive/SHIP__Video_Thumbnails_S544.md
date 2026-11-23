> Disposition, Chat S480, 23 Nov 2026: record; archived. No board card moved.

NEEDS FROM CHAT: nothing to act on; read for the record.

# SHIP: Kain's video thumbnails on the introduction films, theme 0.708.355 and 0.708.356

**For:** Chat. **From:** Code, branch 3 of the S544 theme sitting.

## What changed

- **All 28 course pages (0.708.356):** the picture in each course's video card is now Kain's thumbnail for that course, images/video-thumbs/course-NNN-intro at 960 and 1920 (srcset 960w and 1920w, width 960 height 540, alt unchanged). The card foot, the play button and the film are as signed. tools/course_page_data.py step 8 writes the same picture, so every later run keeps it; the 28 stored files took one line each, after the reviews session's push.
- **The Access All Areas Pass page (0.708.355):** its film picture is Kain's pass-intro thumbnail, the same way. tools/pass_page_data.py writes it; the stored parts.json took the same one line.
- **The seven school pages (0.708.354):** placed by the school session in its own files; measured here.
- The 76 files (38 designs at two sizes) were committed and deployed by the main session (cd912bb8, 0.708.353).

## Why

Kain designed the 38 thumbnails in Canva: "all of the designs are finished ... They're all good to go" (through the main session, S544).

## Proof

Measured on the build site at 1280 and 390 on course 001, the Pass page and the School of NLP: each picture is drawn 440 by 248 at 1280 and 350 by 197 at 390, 16 by 9 like its box (no stretching), the 960 file covering the 2x need (880 and 700), the play button exactly centred, nothing sideways, the course card foot on one row as signed. Courses 011, 016 and 027 each serve their own thumbnail. The first-block pictures keep their loading as before (the school and Pass films high priority, none lazy).

## Not done yet, with what it waits on

- **about-intro:** the About page has no introduction or promotional film, only the five member stories, which keep their real faces. The main session gave it to the session redesigning the About banner with the About Achology film, which builds the thumbnail in.

## Added at 0.708.357: the Membership page

Its session archived, the main session gave it to Code. The film picture is Kain's membership-intro thumbnail at 960 and 1920, written by the builder (previews/membership-page/build.py first(), which tools/membership_page_data.py reads) and swapped into the stored data/membership-page/main.json, one line. page_gate.py's image-lazy exception for the page now names membership-intro-960.webp. Measured at 1280 and 390: 440 by 248 and 350 by 197, 16 by 9, play centred, nothing sideways, no broken picture on the page. images/membership-film-cover.webp and its @2x are now named by nothing in the theme; left on disk for Chat or the next tidy to retire.

## Links

- https://achologytest.com/academy/neuro-linguistic-programming/diploma-modern-applied-psychology/
- https://achologytest.com/academy/neuro-linguistic-programming/
- https://achologytest.com/access-all-areas/
- https://achologytest.com/membership/

*No em or en dashes in this file; checked before writing.*
