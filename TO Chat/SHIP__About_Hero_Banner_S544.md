**DOCUMENT TYPE:** Ship brief, not a page spec.
**Date:** 2026-11-22

# SHIP: the About page banner, 0.708.361 (S544 branch)

What this needs from Chat: one ruling. Does a block this size owe a PAGE GATE line? See the last section.

## What changed

The About page banner is rebuilt as Kain's pick, recorded in PICK__About_Hero_Banner_S544:
- It is the course page hero's warm cream band. The band runs to the window's edges with a hairline foot, and the breadcrumb sits inside it.
- The words are on the left and the Achology film is on the right, both on the page's own 960.
- The heading reads "So, What Is Achology?", with Achology in orange.
- The sentence is Chat's, from ANSWER__About_Banner_Words_S544. The button is still "Read the Achology Story", which scrolls to the story.
- The film is Vimeo 708764177, the same film the school and Membership pages play, on Kain's about-intro thumbnail. There is no cream strip under it. "Watch The Achology Film" and "2:15" sit in white over the top of the picture on a dark fade, with the orange play disc centred.
- The old picture of the building and the old sentence are gone from the About page. The old header rules stay in about.css because Member Testimonials still draws that header.
- about.js: the lightbox frame now takes its title from the button that opened it, so this one reads "The Achology film". The back-to-top button now measures from the new banner.

Files: page-about.php, about.css, about.js, style.css. Commits 1d791800 (0.708.360) and the contrast fix (0.708.361). Both were deployed from a clean copy, and the server, local copy and zip agree.

## Why

Kain, 21 November 2026, asked to "completely redesign the banner ... to follow the standard of the rest of the website", to keep the page's container, to make the paragraph more concise and to build the video in. He picked option 1 of four in the Change Viewer on 22 November and moved the film's words onto the picture.

## Measured on the build site, WebKit

The heading is 33 on a computer and 28 on a phone; the sentence is 18, and 16 on a phone.

| Width | Banner height | Banner to first heading | Text contrast |
|---|---|---|---|
| 1280 | 383 | 48 | 5.7 : 1 |
| 1024 | 375 | 48 | 5.5 : 1 |
| 768 | 710 | 48 | 5.6 : 1 |
| 390 | 595 | 32 | 4.9 : 1 |

- **Layout.** At 1280 the words and film share one centre line inside 160 to 1120. At 768 they stack, with the sentence and film at 560. At 390 they stack at full width. Nothing scrolls sideways at any width, and there is one h1 on the page.
- **Contrast.** Each figure is the film's title and time in white against the lightest pixel behind them.
- **Fonts and image.** Como and the thumbnail load at every width.
- **Click.** A click opens 708764177 in the lightbox, and closing it empties the frame.

Pictures: previews/about-hero-s544/shots/built-1280.png, built-1024.png, built-768.png and built-390.png. The measuring script is previews/about-hero-s544/built.py.

## For Chat

1. The page title in Rank Math is unchanged. Only the visible h1 changed, to "So, What Is Achology?". If Chat wants the page's SEO title or description to echo the new heading, say so and Code sets it over WP-CLI.
2. Code built this from Kain's pick with no PAGE GATE line. The pick record says why: it is one block inside a built page, chosen in the viewer, and Kain's ruling of S160 makes his approval the spec. If Chat rules that a block of this size owes the line, Code corrects the record.
