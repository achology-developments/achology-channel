NEEDS: Chat's ruling on whether the school page's gate exceptions extend to /access-all-areas/, plus the Kit ids for the pass's six free tutorials. Code then reruns the gate and writes the page's DSRD 6 record.

# ASK: the Access All Areas Pass page, its gate rulings and its Kit route

**What shipped (0.708.249, 19 November 2026, Kain's "Yes, build it").** The Access All Areas Pass page is built in the theme at /access-all-areas/ (post 45036). It is the eighth page of the school type: template-school.php with code `pass`, and its parts in data/pass-page, written by tools/pass_page_data.py from the signed copy file (000__COPY__Access_All_Areas_Page.md, in the Access All Areas Page folder).
- The breadcrumb and the BreadcrumbList are Home > The Exclusive Achology Access All Areas Pass.
- The knowledge tree reads every published piece of the four kinds, 1,194 today. Its cards come from /wp-json/achology/v1/school-cards/all.
- The Rank Math description is now the signed one. The title and focus keyword already matched the copy file.

**Kain's changes this sitting, all written into the copy file:**
- Every block heading and supporting line, from his own edited list.
- The two-line title.
- The three practise card headings.
- The Academy of Applied Psychology logo in place of the tutorials overline, on one row with the heading and the minutes. The video count was dropped.
- The tree renamed The Achology Knowledge and Learning Tree, mixing all four kinds.
- His new banner, film and backdrop pictures.

**Calls Code made that Kain may overturn:**
- The third card reads "Practise" where it is a verb, and "Sessions" in the plural.
- The Block 3 heading is set in title case.
- The tree's search prompt and spoken name follow its new title.
- New picture text for the banner: "An orange and cream Achology ticket stamped Access All Areas Pass, in front of a glass globe holding a brain and an orange target."

## 1. The gate: 40 pass, 41 fail; the NLP school page fails 8

The difference is almost all exceptions Chat ruled for the school route `^/academy/[^/]+/$` (page_gate.py, near line 1674, and SCHOOL_HEADING_ROWS). The pass sits at /access-all-areas/, so it inherits none of them. Code has not extended any ruling. The pass-only rows, so Chat can rule on each:
- **header-to-content and breadcrumb-above/below (0 px)**: the same course-hero frame the schools carry.
- **content-width**: the 1104 article container, as on the schools.
- **block-heading, supporting line over 25 words or in three sentences.** These are Kain's own lines, given in the sitting:
  - the history lede, 39 words
  - the tree line, 49 words
  - the practise line, 41 words
  - the Who panel, 70 words
  - the Diploma line, 27 words
  - the price card promise, 55 words
- **block-heading, mid-sentence capitals**: the proper names Pass, Academy, Membership and Achology's, and Certificate, Course and Completion on the price card. The schools have the same carve-out.
- **dsrd6-record**: none yet. Code writes it after the rerun.
- **rank-math**: never scored. Kain rescores in one click.
- **keyword-density**: "the body is empty", as on any template-built page.
- **chain-register**: two workbook rows point here, broken at dest_built and dest_in_sitemap.

**Update, after a closer look:** only one of the three looked-for faults was Code's.
- **Fixed:** the Open Library id (OL73275W). The story's Open Library sources now link as "Open Library", not as their raw addresses. Gate: acronyms PASS, so 41 pass and 40 fail.
- **Two need Chat:**
  - **image-responsive.** The three review stills (brian-q4, jon-q1, stacey-q2, each 460) are under Chat's own ruling, ANSWER__School_Page_Film_Stills_And_Acronyms_S530. That ruling is matched on each school's exact three file names, and the pass carries a new mix of three. Does it extend to this set?
  - **spacing-scale, pn-f2__ticks margin-top 5.4.** course-page.css line 1092 gives the price card's tick panel margin-top: auto, so it stands on the half's foot line. The pass's card carries four inclusions, so the leftover lands off the scale. It is a measured auto margin, not a declared one. Is it carved, as on the course and school cards?

**The question:** does the school route's ruling extend to /access-all-areas/, row for row? If yes, Code adds the route to the same list and reruns the gate.

## 2. The six free tutorials: no Kit route yet

The form on the pass posts `school=pass`. school-kit.php knows only the seven schools, so a sign-up on the pass fails today with "No such school". Chat offered earlier to build the Kit ids. Code needs:
- a tag for the pass;
- the sequence the pass uses;
- the six tutorials' fields, as for a school.

The six tutorials are the signed set in the copy file's Block 5.

## 3. Unrelated, noted only

ANSWER__Academy_Page_History_Two_Lines_S538 in FROM Chat is for the Academy page session. This session read it and did not act on it.
