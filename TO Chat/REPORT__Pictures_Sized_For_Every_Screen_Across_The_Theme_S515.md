**For Chat's main session. What this needs from you:** read the result of BRIEF__Pictures_Sized_For_Every_Screen_Across_The_Theme, and rule on the two questions in section 6 (the other 128 version-numbered uploads, and the Help hero picture). Code, theme session S515, 12 November 2026. This report asks Kain nothing.

# REPORT: pictures sized for every screen across the theme

Theme 0.708.046, commit bfbe504f, deployed from a clean copy of the committed theme (other sessions had unsaved work in the folder), pushed, zip rebuilt beside the theme. Every look is unchanged: section 5 is the render proof.

## 1. What was measured first, and how

Thirty-nine pages, one or more of every kind on the build site, were loaded in WebKit at 1440 (twice-sharp screen) and 390 (three-times-sharp phone), scrolled to the foot so every lazy picture loaded. For every picture shown: the file the browser chose, the width it was drawn at, and the width it would need (drawn times screen sharpness). A picture was counted wasteful when its chosen file was more than 1.35 times what it needed, and single-size when it had no srcset.

Most of what the brief names was already done by cloud job 20 and its follow-up (S203), and stayed true when measured: the logos, people photographs, school and course artwork, avatars, testimonial backgrounds, member story posters, the Know Your Psychology marks and every quote face (item 3; section 2). What the measurement found still wrong is section 2's list.

## 2. Each picture, where it appears, and what changed

| # | Picture | Where | Was | Now |
|---|---|---|---|---|
| 1 | The author faces in the Knowledge Hub front page banner (33 faces) | /learn/ | Drawn 96 to 129 wide; the size list asks for 288 to 292 file pixels; only 240 and 480 existed, so every face took the 480 | A 320 copy of every one of the 156 author portraits; the banner offers 240, 320 and 480 |
| 2 | The book note's hero book (the brief's "course cover" family) | every book note | Size list "240px" everywhere; drawn 204, 124, 104; a sharp phone took the full JPG (565 KB for Man's Search for Meaning) | Size list measured per width; a phone takes the 480 WebP |
| 3 | The same hero book on a quote page with no face | quote pages without an author picture | as 2 | as 2 |
| 4 | The course cover in the side panel (item 2's course cover) | every article and quote page | No srcset: its copies are 224 and 448, and the panel asked for 240 and 480 | A 480 copy of the 28 covers; the panel offers 224, 448 and 480 |
| 5 | The book notes list's lead cover | /learn/{subject}/book-notes/ | WordPress's JPG sizes with "240px"; drawn 203, 162, 133; a phone took a 262 KB JPG | Its own 240 and 480 WebP copies first, with the measured sizes |
| 6 | Knowledge Hub wall tiles (article pictures) | the front page, every subject page, tag pages | Size list "calc(100vw - 40px)" below 600, where the wall is two columns; a phone took a 1536 wide copy for a 161 wide tile | Size list measured at nine widths (two columns, half the screen less 34, below 600) |
| 7 | An uploaded book cover in the author portrait block | articles whose book is an upload (Resilient on Rick Hanson's page) | A 203 KB JPG drawn 240, no srcset, though 240 and 480 WebP copies sat beside it since S167 | Offers those copies |
| 8 | The instructor profile avatar | /about/instructors/{person}/ | 400 wide file drawn 116, no srcset, declared 116 by 116 | Its 128 and 256 copies, and its file's own width and height |
| 9 | The document covers (Manifesto, Code of Ethics, Code of Character) | those three pages | Size list "312px" on a computer, drawn 206; "300px" on a phone, drawn 348 | Measured size list and a 420 copy |
| 10 | The Know Your Psychology logo in the front page's search button | /learn/ | Drawn 87, list said 128, a phone took the 640 | List 88px |
| 11 | The two version-numbered picture files (item 4) | The Origin of Cognitive Therapy and Entrepreneurial Mindset articles | the-origin-of-cognitive-therapy-v2.webp, entrepreneurial-mindset-v2.webp | the-origin-of-cognitive-therapy.webp, entrepreneurial-mindset.webp: each file moved, its record pointed at it, its sizes rebuilt, the old copies removed. No database row names either old file now (read back). Both content records already named the clean names, so the build site now agrees with them. The two pictures' own record slugs still read "-v2"; they are not file names and nothing shows them |

Files made: 191 (156 author portraits at 320, 28 course covers at 480, 2 document covers at 420, and the Testimonials header at 320 and 640). All WebP at the tool's quality 80, by tools/make_picture_derivatives.py, whose table now names each.

## 3. Picture changes left for another session (files made, template not touched)

Written as one line on the theme queue.

1. **Workbook page, Where This Workbook Comes From** (`.wb-origin__pic`, single-workbook.php): the course cover has no srcset. Its 224, 448 and 480 copies exist; drawn 287 on a computer and 200 on a phone.
2. **Course page hero artwork** (`.course-hero__art`, course-parts.php): `course-011-square.webp` is 900 wide, drawn 296, 151 KB at 1440. Needs copies of the square artwork set and a size list.
3. **Testimonials page header** (page-testimonials.php): `header-banner.png`, 408 KB, drawn 320 and 350. `header-banner-320.webp` (19 KB) and `-640.webp` (44 KB) exist. The About, Testimonials and Reviews session, live today, was sent the wiring by message.

Not changed because they are drawn by stylesheets other sessions hold, and are decoration (DSRD 7 section 12.3's budget for a decorative background is 40 KB): the Aristotle watermark behind the Manifesto, Ethics and Character pages (69 KB), course 001's artwork behind the About, Testimonials and Reviews gateway tile (66 KB), the bookshelf behind book note and workbook heroes (58 KB), the closing tiles (27 KB), and the full bubble mark on the About family (24 KB, where a 176 copy exists). Each needs its drawn size measured and an image-set line; they belong to a stylesheet sweep, not this brief.

## 4. Bytes before and after

NUMBERS_GO_HERE

## 5. The render proof

RENDER_GOES_HERE

## 6. Two questions for Chat

1. **The other 128 version-numbered uploads.** The brief named two files ending "-v2"; the build site holds 130 (all article and help pictures uploaded in September, for example `psychology-history-timeline-v2.webp`). DSRD 7 section 12.3 reads "No dates, no version numbers, no export suffixes." Renaming them changes 128 picture addresses, so under The Shared Rules section 8 it is Chat's to agree before it is touched. Code's recommendation: yes, by the same five commands per file used here, as one batch with a read-back that no row names an old file. Nothing in the content records needs to change if they already name clean names, as these two did; Code reads that first.
2. **The Help hero picture.** It carries no srcset on purpose (taxonomy-faq_category.php: WordPress's smaller copies are cut differently and would crop the name printed on the picture). It is 480 wide, drawn 300 on a computer and 96 on a phone, about 30 KB. Code could make uncropped WebP copies at 200 and 300 beside each Help picture, which keep the printed name whole and save about 20 KB per Help page on a phone. Worth doing before launch, or leave it?

## 7. Gates

GATES_GO_HERE

OWED BACK: Chat's ruling on the two questions in section 6.

*No em or en dashes in this file; checked before writing.*
