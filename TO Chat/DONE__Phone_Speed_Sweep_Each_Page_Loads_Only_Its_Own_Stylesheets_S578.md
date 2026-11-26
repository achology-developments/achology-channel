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

## Tools and care

`tools/speed_page_check.js` (S577) and `tools/speed_pack.py` carry the method; the pack tool reads the live site one page at a time with a two second pause and stops after four refusals (the standing rule on crawling achology.com). A pack is served only while every source sheet is unchanged; after a stylesheet edit run `speed_sweep.py min`, `speed_pack.py`, prove, then `speed_pack.py --enable-all`.

OWED BACK: nothing to Chat.

*No em or en dashes in this file; checked before writing.*
