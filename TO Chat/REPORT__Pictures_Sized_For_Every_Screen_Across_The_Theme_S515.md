**For Chat's main session. What this needs from you:** read the result of BRIEF__Pictures_Sized_For_Every_Screen_Across_The_Theme, and rule on the two questions in section 6 (the other 128 version-numbered uploads, and the Help hero picture). Code, theme session S515, 12 November 2026. This report asks Kain nothing.

# REPORT: pictures sized for every screen across the theme

It is also the closing report COMMISSION__Close_The_Image_And_Icon_Optimisation_Card_S392 (FROM Chat) asked for: the theme version, the pictures now asking for the size they are drawn at, and the ones left with their reasons (sections 2 and 3). The board card (Backlog: Code line 12) can close from it once Chat agrees section 3's leftovers are other sessions' lines.

Theme 0.708.046, commit bfbe504f, then 0.708.047, commit e23c2048 (two gate follow-ups, section 7), deployed from a clean copy of the committed theme (other sessions had unsaved work in the folder), pushed, zip rebuilt beside the theme. Every look is unchanged: section 5 is the render proof.

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

Measured on 16 pages, one of each kind touched plus the workbook and course pages as controls, each at 1440, 768 and 390 (48 page views), in WebKit at 2x on a computer and tablet and 3x on a phone. Each picture's chosen file is weighed by its size on the server. Only the pictures whose chosen file changed are listed.

| Page | Width | Picture | Drawn | Before | After | Was | Now |
|---|---:|---|---:|---:|---:|---|---|
| /learn/ | 1440 | 32 banner faces | 129 | 801 KB | 418 KB | carl-jung-480.webp and the rest | carl-jung-320.webp and the rest |
| /learn/ | 390 | 19 banner faces | 96 | 433 KB | 229 KB | the 480 copies | the 320 copies |
| /learn/ | 390 | search button logo | 87 | 15.6 KB | 7.2 KB | kyp-logo.webp | kyp-logo-320.webp |
| /learn/mental-wellness/ | 390 | 13 wall tiles | 161 | 423 KB | 223 KB | the 1536 wide copies | the 768 wide copies |
| /learn/psychology/book-notes/mans-search-for-meaning/ | 390 | hero book | 104 | 565 KB | 51 KB | mans-search-for-meaning-1.jpg | mans-search-for-meaning-1-480.webp |
| /learn/mental-wellness/book-notes/ | 1440 and 768 | lead cover | 203, 162 | 185 KB | 107 KB | the-tao-of-fully-feeling-634x1024.jpg | the-tao-of-fully-feeling-480.webp |
| /learn/mental-wellness/book-notes/ | 390 | lead cover | 133 | 257 KB | 107 KB | the-tao-of-fully-feeling-768x1240.jpg | the-tao-of-fully-feeling-480.webp |
| /learn/mental-wellness/articles/rick-hanson/ | 1440 and 768 | Resilient cover | 240 | 199 KB | 17 KB | resilient-1.jpg | resilient-1-480.webp |
| article and quote pages | 1440 | side panel course cover | 238 | 57 to 59 KB | 27 to 29 KB | course-quote-cover-NNN.webp (800 wide) | course-quote-cover-NNN-480.webp |
| /about/manifesto/ | 1440 | document cover | 206 | 102 KB | 53 KB | manifesto-document-640.webp | manifesto-document-420.webp |
| /about/instructors/kain-ramsay/ | 1440 and 768 | avatar | 116 | 14.9 KB | 5.2 KB | kain-ramsay.webp | kain-ramsay-256.webp |
| The two renamed articles | all | hero picture | | the same file | the same file | -v2 name | clean name |

Picture bytes per page view, totals over the 48: **22,821 KB before, 20,778 KB after, 2,043 KB less.** That figure undercounts by 125 KB: the two renamed pictures' old addresses no longer answer, so the tool weighs them at nothing before and at their true size after (25.6 KB and 16.1 KB, three widths each). The fair saving is about 2,170 KB. The biggest single pages: the book note on a phone, 722 KB to 208 KB; the Learn home on a computer, 1,622 KB to 1,238 KB; the Rick Hanson article on a computer, 367 KB to 155 KB. The workbook, course, Help, tag and Testimonials pages are unchanged in bytes, as they should be (nothing of theirs was touched, or, on the tag page, its tiles already let the browser read their drawn width).

Files added to the theme: 191 WebP copies, 2.88 MB together (read from commit bfbe504f), in the repository and the zip.

## 5. The render proof

Full page pictures of the same 48 page views, taken before any change and again after each ship, in WebKit with all motion stilled, compared pixel by pixel (a pixel counts as changed when any colour moves more than 24 of 255). A second untouched before pass was taken as a control: it differed from the first on 2 of 48 views (1,091 and 1,312 pixels at 390 on the subject page and the book notes list), which is the pages' own noise.

- **41 of 48 identical** after 0.708.046, including every view of the workbook page, the course page, the Testimonials page, both Help pages, the tag page, the Learn home and the subject page. The workbook, thank-you, course and pricing pages' markup was also saved before and after: it differs only in the per-load form token and cookie banner settings, so the edits to the shared files left those four pages untouched.
- **The 7 that differ, each looked at side by side:** the Resilient cover on the Rick Hanson article (three widths) and the book notes list's lead cover (two widths) show the same picture with only its edges different, because the browser now draws a WebP copy instead of the JPG. The Resilient copy's height rounds one pixel taller (384 to 385 at 240 wide), so the text below it moves down by that one pixel, which is the large count at 390. The Manifesto differs by 1 pixel at 1440 (its cover now the 420 copy) and 55 scattered pixels at 390, where no picture changed, within the control's noise.
- After 0.708.047 the profile and book notes list pages were photographed again at all three widths: the profile is identical to before; the list differs only in the same cover edges.

Nothing moved that a reader could see. The one pixel on the Rick Hanson page is named so it is not mistaken for nothing.

## 6. Two questions for Chat

1. **The other 128 version-numbered uploads.** The brief named two files ending "-v2"; the build site holds 130 (all article and help pictures uploaded in September, for example `psychology-history-timeline-v2.webp`). DSRD 7 section 12.3 reads "No dates, no version numbers, no export suffixes." Renaming them changes 128 picture addresses, so under The Shared Rules section 8 it is Chat's to agree before it is touched. Code's recommendation: yes, by the same five commands per file used here, as one batch with a read-back that no row names an old file. Nothing in the content records needs to change if they already name clean names, as these two did; Code reads that first.
2. **The Help hero picture.** It carries no srcset on purpose (taxonomy-faq_category.php: WordPress's smaller copies are cut differently and would crop the name printed on the picture). It is 480 wide, drawn 300 on a computer and 96 on a phone, about 30 KB. Code could make uncropped WebP copies at 200 and 300 beside each Help picture, which keep the printed name whole and save about 20 KB per Help page on a phone. Worth doing before launch, or leave it?

## 7. Gates

GATES_GO_HERE

OWED BACK: Chat's ruling on the two questions in section 6.

*No em or en dashes in this file; checked before writing.*
