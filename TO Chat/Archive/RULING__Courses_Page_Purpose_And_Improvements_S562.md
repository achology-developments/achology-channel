> Disposition, Chat S482, 23 Nov 2026: item 3 answered in FROM Chat/ANSWER__Courses_Page_Three_Extra_FAQ_Answers_S482 (Help 400, 330 and 225); the rest is Kain's ruling, recorded as written; archived. Board: no card moved.
# RULING: The Courses Page's Purpose and Its Three Improvements (S562)

Kain, 23 November 2026, in the Courses page review side session (branch courses-review/s562, cut from origin/main at a70dae1c). Each item below was agreed by Kain in that sitting; his words are quoted.

## 1. The page's purpose

**The Courses page is where someone who does not yet know which course they want tells us what they want to change in their life, and is shown the few courses that fit them best.**

Kain: "Yes, that's it." And earlier in the sitting: "I love the mechanism. I really love the mechanism."

What follows for the Home page: the goal chooser lives on the Courses page alone. The Home page does not rebuild it; it points into it (item 2 below makes that possible).

## 2. The improvements, in order

Kain on the list as a whole: "Yes, that's the list."

**1. Simplify the page.** Kain: "we got carried away with the bells and whistles a little bit ... I don't want to redesign it ... I just want to simplify." On the one proposal put to him: "Yes, simplify it." Every extra from the S180 finish comes off, and the page goes back to its plain section 1 to 6 state in courses-directory.css:
- no orange light following the pointer over the goal tiles (Warm Torchlight);
- the plain brand dark band: no film grain, no orange glow at its foot (Rich Texture); the photograph stays;
- the top arrives still: no counting numbers, no tiles rippling in, no line drawing out with its glint;
- choosing is calm: no squeeze and spring, the soft tick appears without drawing itself, the floating button appears without bouncing or nudging;
- the course cards still rise in as the list changes (kept), but with no blur into focus, no shine across Best match, no pulsing ring.

And three small faults fixed in the same pass:
- the sort words (Most popular, Highest rated, Most in-depth) sit inside the button family's tab frame with room either side (16 each side; 8 on a phone), where today "Most popular" runs into its frame. Kain: "That button block seems to have been contradicted when we upgraded our button system."
- the small instruction line under the goal tiles goes; the line beside the title already asks the same thing.
- the space under the registration line to the footer is the questions band's own 64 (48 and 32 on smaller screens), where the line's own 32 margin doubled it to 96. Kain: "a little bit too much spacing at the bottom of the page." Note for the build: the 32 is the shared .cd-credit margin inside .q-band, so other pages ending on the questions band may carry the same 96; worth one look before the fix is placed in help.css or kept to this page.

Seen by Kain in the Change Viewer as previews/courses-review-s562/round-1.js (viewer_proof.py PASS, 19 measured, 0 failed, 23 November 2026), all switches on.

**2. The Home page links straight into the chooser with a goal already ticked.** For example /courses/?goal=build-lasting-inner-resilience opens the page with that tile ticked and its courses shown. Nothing on the Courses page looks different. Cost: small, about fifteen lines in courses-directory.js: read the goal words from the address (one or several, comma separated, each the tile's own words in lower case with hyphens), tick the matching tiles before the first draw, and leave the page as it is when a word matches nothing.

**3. Three questions in each FAQ column, on the Courses page only.** Kain: "I think we could probably expand the FAQs about our online psychology courses to at least 3 courses per column" and, asked whether this page only or every page: "Yes, this page only." This is a recorded exception to the 20 November rule of two questions per card on every page (WORDS__Question_Block_Last_Four_Three_Columns_20Nov). **Chat chooses** the one extra published Help answer for each of the three cards (Where to Begin, How Courses Run, Paying and Access); today they hold 399 and 402, 329 and 327, 341 and 333.

## 3. Left out on purpose

Showing all 28 courses (Explore More stops at 15, though the overline says 28) was raised and left out to keep the job small.

Nothing is built, committed to main or deployed; every item waits on its build session, with Kain's yes for any deploy.
