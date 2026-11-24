# SHIP: the Membership banner on the Home hero's design, 0.708.471 (S567)

**Needs from Chat:** nothing to act on. One alt line is waiting on your words, at the end.

**What changed.** Kain picked option 1, "The Home Hero", from a proved round of four (24 November 2026). His words: "Option one is very, very good". He asked for one change: the line should read over three rows, not five. The /membership/ banner (post 45034) is now one dark band:
- the breadcrumb, then his title, line, $7 button and ticks, all unchanged (the line now runs the full 616 column, three rows at every computer width);
- the members' faces, faint behind the words;
- the film (Vimeo 708764177) easing in from the right.

Pressed, the film plays inside the band. It grows into a rounded card with the faces all round it, and the band deepens to hold it at full column width. Closing it returns the banner. There is no figures strip. The people-learning picture that was the banner's now sits in the opening block, "What Achology Membership Can Give You", in place of the film's button.

**Why.** Kain: the Home banner is "absolutely lovely"; the Membership banner was the one he never liked, for its picture. He did like the faces behind it.

**Measured on the build site** (DSRD 7 3.1 and 4):
- 1440 and 1024: breadcrumb 48 from the top, 24 to the title. Title 33, two rows. 24 to the line, which is 18 on three rows. 32 to the button, 64 under it.
- 375: title 28, line 16, the film below the ticks with 48 above and 48 below it.
- No sideways scroll at any width. Playing and closing were tested at 1440.

**Files.**
- membership.css, section "S567"
- hero-film.js (new; enqueued in membership-setup.php)
- data/membership-page/main.json: only the banner and the opening block's film were swapped, by previews/membership-page/membership_banner_s567.py
- the preview round: previews/school-page-s482/round-mhero.js

Commit b5dbeaae on main. deploy.py proved local, the server and the zip agree.

**Code's calls, for Kain to overturn:**
1. The title stays at the 33 page-title size, not Home's 42, because page_gate holds every h1 to 33.
2. "Achology" in the title is white, because it is orange except on a dark band.
3. The film shows Home's own picture of the same film.
4. The breadcrumb sits inside the band, as on the Courses page.
5. The old banner's rules in membership.css (.school--memb, .memb-faces) are now unused and are left for the stylesheet split.

**Alt text.** The people picture keeps its old alt ("Four young adults talking and taking notes together..."), which still describes it. Write a new line if you want one for its new place.

**Then 0.708.472, the same change set (Kain, after he saw it):**
- **The three figures are out of the page.** Kain: "It doesn't actually need to be there." The opening block's 7 Courses Included, 5 Member Levels and 216 Countries Reached are removed from the stored page, with no gap left: the Who box now stands 24 under the picture, its own margin.
- **The people picture is raised.** Kain: "budge the whole image up a little bit". From 1024 up, its drawing now starts level with the tops of the title's capitals (measured 0.3 off at 1440 and 1024). It is set as a share of the picture's width, so it holds at every computer width.
- The phone is unchanged apart from the figures going.
- Commit 5ca55988; deploy.py proved again.

*No em or en dashes in this file; checked before writing.*
