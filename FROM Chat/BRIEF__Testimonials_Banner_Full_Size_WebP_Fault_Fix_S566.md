**Needs from Code:** ship one fault fix on /testimonials/: a full size WebP copy of the banner picture, served beside the two copies it already has, with nothing Kain can see changed. Name this file in the declaration's SPEC field.

Done when the page gate's image line passes on /testimonials/, the picture measures the same at 1440 and 390 before and after, and the record's line 9 is rerun.

# BRIEF: the Testimonials banner picture, a full size WebP copy (fault fix)

**DOCUMENT TYPE:** fault fix brief for one existing page, signed spec kept as it is.
**Date:** 2026-11-24
**From:** Claude Chat, side session of Code's S566 main session. **To:** Claude Code, the S566 sweep session.
**Answers:** TO Chat/DONE__Sweep_The_38_Failing_Published_Pages_S566, item 3.4. It replaces the brief paragraph in FROM Chat/ANSWER__Launch_Check_Three_Questions_And_The_Testimonials_WebP_S485, section 3, which carries the same job.
**Governing spec:** 000__SIGNED_SPEC__Testimonials_Page_S390, in the Video Testimonials Page design folder: block 3, "Header banner image, 780 by 780". **Authority:** Project Instructions section 5, "a fault fix that changes nothing he can see is simply done", and the sweep brief Part 3.4.

## The fault

`page-testimonials.php` serves `images/testimonials/header-banner.png` (780 by 780, about 409 KB) as the banner's own size, with WebP copies at 320 and 640 only (S515). A screen that wants the full 780 gets the PNG.

## The fix, and nothing else

1. Make `images/testimonials/header-banner-780.webp` from `header-banner.png`, the same picture at the same 780 by 780, by the same route the pictures session used for the 320 and 640 copies. Check it by eye against the PNG at full size: no change of colour, edge or crop.
2. In `page-testimonials.php`, line 116, the call `achology_derivative_attrs( 'images/testimonials/header-banner.png', 780, array( 320, 640 ), ... )` takes `array( 320, 640, 780 )`. The `src`, the `sizes` value, the alt, the width and height and `fetchpriority` stay exactly as they are; the PNG stays the fallback.
3. No class, markup, stylesheet or words change. Bump the theme version and purge the cache.

## The proof

- The banner's box measured at 1440 and 390, before and after: the same size and place.
- The network reading at 1440 shows a WebP chosen, not the PNG.
- `page_gate.py` on /testimonials/: the image line passes, nothing else moves.

PAGE GATE: 0 blocks reused / 0 new registered / 0 variants awaiting ruling · data read from 000__SIGNED_SPEC__Testimonials_Page_S390 (block 3) and page-testimonials.php line 116 · class audit 0 gaps (no markup or class change) · contrast n/a, no visible change · anchors 0 unresolved · dashes 0

*No em or en dashes in this file; checked before writing.*
