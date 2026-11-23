> Disposition, Chat S480, 23 Nov 2026: record; archived. No board card moved.

NEEDS FROM CHAT: nothing to act on; read for the record. The ruling to write home is RULING__Course_Intro_Video_Card_S544 beside this file.

# SHIP: the course introduction video card on all 28 course pages, theme 0.708.346

**For:** Chat. **From:** Code, branch 3 of the S544 theme sitting.

## What changed

- All 28 course pages: the teaching picture now plays the course's own introduction film (its lesson 1 Vimeo id from ANSWER__Course_Intro_Videos_Links_And_Card_Words_S544), with Kain's card foot under it: "View This Course's Introduction Video" and the running time (3:11 to 19:48). The 2:15 promotional film is gone from the course pages; the school pages keep it.
- tools/course_page_data.py step 8 now writes the card from tools/course_intro_films.json (the 28 ids and times, copied from your answer), so every later run of the generator keeps it. Nothing else in the tool changed.
- The 28 stored data files took one line each, the card, by the same markup step 8 writes (proved identical on course 001 against a full generator run). The reviews block is not in them: that is the reviews session's.
- course-page.css: the card's rules. course-page.js: the foot plays the film, and the window is named for it.

## Why

Kain's design and "Yes, all 28" (RULING__Course_Intro_Video_Card_S544). Kain then signed the built card on the build site: "Yes, it's signed".

## Proof

Measured on the build site at 1280 and 390 on six courses: 001 (5:50), 016 (19:48, the longest), 011 (3:11, the shortest), 002 (11:09), 008 (19:39), 027 (7:41). Every card has its own id and time; the foot is on one row at the card's edges with 16 padding; the card stands level with the block heading at 1280; 16 down to the facts; nothing sideways; Como loaded. On 016 a press on the foot opens 579929159 in the window named Course introduction video, focus goes to Close and returns to the picture. css_gate on course-page.css: PASS.

## Owed from Chat

Nothing for this ship. The films still play each course's old lesson 1 cut until your video sessions replace each one on Vimeo under the same id, as your answer says.

## Links

- https://achologytest.com/academy/neuro-linguistic-programming/diploma-modern-applied-psychology/
- https://achologytest.com/academy/mindfulness/mindfulness-mental-health/
- https://achologytest.com/academy/life-coaching/skilled-helper/

*No em or en dashes in this file; checked before writing.*
