> Chat S494, 26 Nov 2026: noted on Page Speed. Archived.
For Chat: what this needs: read it; four ships for item 1 of the agreed string (pass Core Web Vitals on phones). Nothing is asked of Chat.

Done when: Chat has noted the four ships and what is left of item 1.

# SHIP: phone speed, the scripts (0.708.506 to 0.708.509)

Code, S579 theme session (Opus), 26 November 2026. Measured with Lighthouse 12 run on Code's own Mac (phone, simulated slow network and 4x slower processor), three runs per page, each with a fresh address so no run reads the page cache.

## What shipped

- **0.708.506, the last-lines script (no-lone-words.js).** Same lay, half the work: blocks are found without comparing every block with every other; a text is written only where its words change (the second lay on Home rewrote every text three times); every block is read before any wrap is set. On a slowed phone, Home's script time went from 1.9 s to 0.96 s.
- **Outside the theme, same day:** SiteGround's lazy picture script (lazysizes) switched off in SiteGround Speed Optimizer (`siteground_optimizer_lazyload_images` 0). No page used it (no picture carried its markup); every picture already uses the browser's own lazy loading. It was the school page's largest script cost (about 2 s on the slowed phone).
- **0.708.507, banner picture preload (speed-setup.php).** School and course pages name their top band's picture in the head, so it no longer waits for the stylesheet.
- **0.708.508, font preload (speed-setup.php).** Every page names its four fonts (Mulish Latin, Como Medium, SemiBold, Bold) in the head. First paint went from 2.0 s to 1.4 s on every page measured.
- **0.708.509, the price block (pricing-block.js).** Its lines are read all together, then tied, where each line made the page lay itself out again. Its script time on the school page went from 0.85 s to 0.34 s.

## How each was proved

No ship changes anything a visitor sees. For the two scripts, a test loads the page in Chrome at 375, 1024 and 1440 wide with the new script swapped in, waits for the fonts and the late lays, and records every line break the lay puts in, every wrap it sets, and the finished markup and set heights of every price block; the old and new records must match exactly. Last lines: nine pages (Home, About, Reviews, Testimonials, a school, a course, Events, Membership, the Founder's Letter), 24 of 24 page widths the same, and the same again on the live site after the deploy. Price block: school, course, Membership, Pricing, Certification, 15 of 15 the same. Both tests were shown to fail with the script emptied (24 and 15 differences).

## Phone scores, before and after (three runs each)

| Page | Before (today) | After |
|---|---|---|
| Home | 84 to 85, first paint 2.0 s, blocking 450 to 490 ms | 92 to 93, first paint 1.4 s, largest paint 2.3 s, blocking 220 to 260 ms |
| School (Cognitive Behavioural Psychology) | 67 to 77, blocking 710 to 740 ms | 79 to 81, first paint 1.4 s, largest paint 3.3 s, blocking 410 to 440 ms |
| Course (CBT Practitioner) | not run before | 88, largest paint 3.5 s, blocking 120 ms |

Layout shift on all three: 0.012 in the lab (passes; under 0.1).

## Left of item 1

- The school page's largest paint (3.3 s; passing is 2.5 s) is now held by the page's own size: the browser's work on the 320 KB page itself is about 3.7 s on the slowed phone, more than all its scripts together. The remaining script cost is spread thin (course-page.js, school-page.js, buttons.js, no single hot spot over 0.1 s in the profile).
- The non-composited animations (button sweep `left`, the ring's box-shadow, the footer's flowing background, the cookie button's slide) still to move to transform; it changes how Kain's signed buttons are drawn, so it goes to him as Before and After first.
- Field layout shift on Home (0.12 in Google's visitor data) cannot be read again until the 28-day visitor data refreshes; the font preload removes the likeliest cause (words redrawn when the fonts arrive).

*No em or en dashes in this file; checked before writing.*
