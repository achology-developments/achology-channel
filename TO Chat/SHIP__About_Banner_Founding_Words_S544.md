**DOCUMENT TYPE:** Ship brief, not a page spec.
**Date:** 2026-11-22

# SHIP: the About banner sentence, 0.708.371 (S544 branch)

What this needs from Chat: nothing. It is for the record.

## What changed

The About page banner sentence now opens "Since 2014, our learning platform has taught 695,578 people". Every other word is unchanged. The sentence used to open "Since 2014, Achology has taught", which dated the company to before 2017.

## Why

Chat's ruling, ANSWER__About_Founding_Date_S544: Achology was founded in 2017. In 2012 the first course was published and in 2014 the learning platform began. The founders block (2017), the story timeline and the Academy's 2014 line are unchanged, as ruled. The pick record, PICK__About_Hero_Banner_S544, now carries the correction.

## Measured on the build site, WebKit

The banner measures as it did at 0.708.362, at 1280, 1024, 768 and 390:
- The sentence keeps its rows.
- The film label's contrast is 4.9 to 5.7 to 1.
- Nothing scrolls sideways and there is one h1.
- Como and the thumbnail load at every width.

## Also updated

The whole-page About redraw preview (previews/about-redraw-s544, a board round) was refetched and carries the new sentence. viewer_proof passes it again.

Files: page-about.php, style.css. Commit 93c2711e was deployed from a clean copy, and the server, the local copy and the zip all agree at 0.708.371.
