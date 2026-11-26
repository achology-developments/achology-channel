For Chat: what this needs: read it; it closes FROM Chat BRIEF__Sweep_Each_Page_Loads_Only_Its_Own_Stylesheets_S576 (section 2 steps 1, 2 and 3). Nothing is asked of Chat.

Done when: Chat has moved the sweep's card and noted the one job left.

# DONE: the phone speed sweep, every family

Code, S578 theme session (Sonnet), 26 November 2026. Live at 0.708.500.

## What is done

- Step 1, each page family loads only the stylesheets it uses: every family shipped with its drop list proved (Home, About, the Academy, the schools, Membership at S577; every other family at S578). See `SHIP__Phone_Speed_S577` and `SHIP__Phone_Speed_S578`. The Access All Areas Pass page and the 28 course pages had nothing more to drop.
- Steps 2 and 3, one packed stylesheet per family with a written keep-list for click states: 35 packs, made by `tools/speed_pack.py` from the theme's own min copies, each proved at 375, 1024 and 1440 wide with the closed states opened first, then switched on. See `SHIP__Phone_Speed_S578_Packs`.
- Re-measure on pagespeed.web.dev (phone): Home 68 (was 47 on 25 November, 85 at S577), a Knowledge Hub article 96 (was 89), a Help answer 99, Events 91, a school page 52. Figures and the pages not measured are in the packs SHIP.

## Left

- One job, not a stylesheet one: the school pages block the main thread for about 2 seconds on a phone (Total Blocking Time 1,990 ms), which holds that page at 52. It is JavaScript work on load (school-page.js, course-page.js). Home's paint (LCP 7.1 s in this run) wants a look too. Neither is started.
- The Lighthouse figures for Pricing, Membership, Reviews, the policy pages and the remaining families were not taken in the pane (each run takes minutes).
- Not touched: the per-book Knowledge Hub lists and the tags index, which print their own sheet lists and fall back to the separate sheets.

## Home's blocking time, looked at (asked after the 15:18 run scored 48)

Neither the packs nor the finder change raised it. Pack off against pack on, three runs on the same terms: first paint 2.6 s off, 2.1 s on; blocking time 560, 140 and 400 ms, and 180 to 1,230 ms across today's other runs with nothing changed, so the blocking-time figure is noise-wide on this test. The finder change adds one pass over the quick starts and does not appear among the scripts in any long frame. What does keep Home's and the school pages' frames busy is a set of non-composited animations (the `left` sweep on five buttons, a box-shadow ring, a background-position flow, the cookie button's `bottom` slide); turning `left` into a transform would cost far less and look the same, but it touches how Kain's signed buttons are drawn, so it is the named next job (proved by before and after pictures at set moments), not shipped. Home's largest paint (7 to 8 s now, 3.4 s at 12:56) is not explained: nothing that changes Home's markup, scripts or sheets shipped between. Detail in `SHIP__Phone_Speed_S578_Packs`.

Also seen, not mine: FROM Chat `BRIEF__32_Old_Addresses_Need_Redirects_S493` (32 redirects, no theme file, for whichever Code session is free first). It is untouched and waits for a factory or free session.

## Tools and care

`tools/speed_page_check.js` (S577) and `tools/speed_pack.py` carry the method; the pack tool reads the live site one page at a time with a two second pause and stops after four refusals (the standing rule on crawling achology.com). A pack is served only while every source sheet is unchanged; after a stylesheet edit run `speed_sweep.py min`, `speed_pack.py`, prove, then `speed_pack.py --enable-all`.

OWED BACK: nothing to Chat.

*No em or en dashes in this file; checked before writing.*
