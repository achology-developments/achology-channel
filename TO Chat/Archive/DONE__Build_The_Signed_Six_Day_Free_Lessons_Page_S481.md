> Disposition, Chat S482, 23 Nov 2026: read; the four open lines ruled in FROM Chat/ANSWER__Six_Day_Page_Four_Open_Lines_S482 (reviews block to the mock-up's shorter cut, balanced wrapping for short lines); Kain is shown the page; archived. Board: #23 comment, stays in Ready until Code's rerun.
NEEDS FROM CHAT: read the six day pages at the addresses below against the signed mock-up (pictures in the main session's notes folder), rule the two open lines (the reviews block and the mock-up's own short lines), then point Kain at it. Code, Branch 1 of S562, 23 November 2026, theme 0.708.437.

# DONE: the signed Six Day Free Lessons page, every course and school (answers BRIEF__Build_The_Signed_Six_Day_Free_Lessons_Page_S481)

Built to the signed mock-up (`Six Day Free Lessons Page 23 November 2026`, page.html), DSRD 9 section 48, the 18 November unlock logic and the signed pricing block. One template, `six-day-lessons.php`; `six-day.css` is the mock-up's `new-parts` rule for rule; `six-day.js` loads an open day into the player. Commits dc0ce5a8, 6db5bdbe, 39281bf0 on main; deployed from a clean copy, server, zip and version proved.

## Addresses (build site)

- Course: `/academy/{school}/{course}/free-lessons/`, all 28 answer 200 with every block (hero, player, track or free block, reviews, pricing block), noindex, no footer invitation.
- School: `/academy/{school}/free-teachings/`, all 7 answer 200 the same way.
- Course 001: /academy/neuro-linguistic-programming/diploma-modern-applied-psychology/free-lessons/
- School of NLP: /academy/neuro-linguistic-programming/free-teachings/
- Old addresses: `.../free-lessons/{n}/` and `.../free-teachings/{n}/` answer 302 to `?day=n`, which lands on that day with the track showing days 1 to n (four read, course and school).
- Test readers for looking at any day (made for the comparison, kept for your read): course 001 day 1 `?r=ugf2iybfw2nu6y9cn7nl6kfg`, day 3 `?r=au0swwjkmbexj4v381ieyuv1`, day 6 `?r=vq15u0u1cez9hly5ewldenb8`; NLP day 1 `?r=v6znmzbl3uubn4zfg9toddi5`, day 3 `?r=bs7fffnxxmbovn1ruujgzfdu`, day 6 `?r=ifsukxhlj5k2hyvprstvsafp`.

## Against the mock-up (1280 and 375, day 1, 3 and 6, course 001 and NLP: 12 views, headless)

| Block | Order | Size | Words | Score |
|---|---|---|---|---|
| 1 Hero | same | identical, all 12 views (e.g. 1104 x 423 at 1280, 335 x 508 at 375) | same; the weekday is the clock's (the mock-up assumes a Monday sign-up) | 10 |
| 2 Player band | same | identical, all 12 (film 1104 x 621 / 335 x 188) | same, plus the film button's spoken name "Play: {lesson}" (not seen) | 10 |
| 3 Six day track | same | identical, all 12 (592 at 1280, 1056 at 375) | same, weekdays by the clock | 10 |
| 4 What Students Say | same | **taller**: 1263 against 647 at 1280 (course), 1416 (school) | **see open line 1** | 7 |
| 5 Pricing block | same | 9 px shorter at 1280, 14 taller at 375 (course); 9 / 33 shorter (school) | the line is section 48's word for word; the card marks are the signed block's Visa, Mastercard, Amex, Discover where the mock-up's frame shows Stripe and Apple Pay | 8 (Branch 2's component, reused unchanged) |
| 6 Footer | same | site footer, Roundup kept, invitation gone | same | 10 |

No sideways scroll at either width in any view. The short lines are exactly the mock-up's at both widths (see open line 2).

## Open lines for Chat

1. **The reviews block.** The mock-up shows a shortened copy (heading, one row, Show More). Section 48 says "the signed reviews block, as on the course or school page", and the brief says signed blocks are reused, never redrawn, so the page carries the stored block whole: its figures strip, two rows and the two link cards. Say if Kain's page should carry the mock-up's shorter cut instead. The school's heading and lead take section 48's words ("What Students Say About This School").
2. **Short last lines that the mock-up itself has.** At 1280 the track's names wrap to 3 lines with 2 or 3 words last ("Introducing the Diploma in Modern Applied Psychology"), and the hero title's last line holds 3 words; at 375 the title ends on 2. The built page wraps exactly as the signed mock-up does, so meeting "no line of one, two or three words" would mean changing the signed layout. Code left it as signed.
3. **Which summary.** A course lesson's question and summary come from data/lectures (the description's first paragraph, and the first sentence of its second). Lessons 1, 2, 3 and 6 of course 001 match the mock-up word for word. Lesson 4 shows one sentence where the mock-up shows two, and lesson 5's mock-up summary is a hand-trimmed sentence. Neither is typed into the template.
4. **No token, no day asked.** The mock-up does not draw it. The page shows day 1 in the player and, in the track's place, the course's or school's own signed free block with its form, as the course or school page prints it. A sign-up there sends the reader straight to their own page.

## How the reader token is stored

- Made at sign-up (course-kit.php `achology_free_lessons_request`): 24 lower case letters and digits, in wp_options as `achology_sd_r_{token}` => kind, key (course number or school code), sign-up time, not autoloaded; deleted again if Kit refuses the sign-up.
- Sent to Kit as `free_lessons_link` or `free_teachings_link`: `{page}?r={token}&day=`. It ends on an empty day on purpose: the live course emails link their picture as `{{ subscriber.free_lessons_link }}{n}/`, which now opens the reader's own page on lesson n; a reader from before the token holds the plain address and still goes by the old `/n/` redirect. A school reader's `teaching_N_film` (the field each school email's picture opens) is now `{page}?r={token}&day=N`. **No Kit email was edited**; the pass's films are unchanged.
- Kept in the browser: cookie `ach_sd_{kind}_{key}`, one year, HttpOnly, SameSite Lax.
- Day n opens (n - 1) x 24 hours after sign-up. `?preview_day=n` shows any day to admins only. `?day=n` opens days 1 to n for anyone: the main session's call (S562), since the lessons are free, so the daily opening sets a pace and is not a lock, and every old email link must keep working.

## Test sign-ups, read back in Kit (through the site's own connected Kit account)

| Reader | Kit id | Read back |
|---|---|---|
| manager+sixday-course@achology.com, course 001 | 4403196821 | `free_lessons_link` = the reader's page with token; lesson fields filled; tags 25695128 and 25695129 |
| manager+sixday-nlp@achology.com, School of NLP | 4403196858 | `free_teachings_link` and all six `teaching_N_film` = the reader's page with token and day; tags 25962820 and 25962821 |

Both links open the right lesson on the reader's own page. Kit's search lagged behind the API for some minutes, so read them by id if a search shows nothing.

## Checks

- The enrol buttons open the right checkouts (course, school bundle, Access All Areas Pass on the course; the school on the school), never locked.
- Retired: the S560 banner round (previews/six-day-lessons-s560 marked superseded).

OWED BACK: nothing further from Code unless Chat rules the open lines.

DOCUMENT TYPE: done.

*No em or en dashes in this file; checked before writing.*
