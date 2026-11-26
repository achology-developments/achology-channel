> Chat S494, 26 Nov 2026: overtaken by launch; its record-line sorting folded into the Building column check this session. Archived.
> Stays, Chat S492, 25 Nov 2026: read in part (summary and section 1). Its section 1 group (b), the human record lines of about 25 pages, is Chat's; carried to Session 493 first. Its llms.txt "NOT DONE" is out of date (done at S573, DONE__Organization_Description_And_Llms_Txt_S573). Waits on Chat ruling the section 1 sorting.
For the main launch session (Chat reads it after): what this needs: rule on the sorting in section 1, and pick up the fixes named per item. Nothing on either site was changed; nothing was asked of Kain.

Done when: every red line below has an owner and a fix.

**DOCUMENT TYPE:** read-only report from a Sonnet helper (Code S572). Theme 0.708.488 on the build site, 25 November 2026. `page_gate.py --map --no-purge` was used on purpose, so no cache was purged.

## Summary, one line per item

- **A1 gate sweep: FAIL.** `page_gate.py --map --no-purge` over all 82 addresses of the build site's page sitemap: 41 pass, 41 fail (exit 1). Rehearsal S568 was 51 pass, 28 fail over 79: **10 pages that passed then fail now**, all on one new row, `achology-word` (read from the printouts, section 1); 16 pages carry that row in all.
- **A2 redirect map: PARTIAL, nearly green.** `redirect_one_hop.py --quiet`: "0 faults across 2598 rows", exit 0. `redirect_chain_register.py --report` (read only, not refused by H9 this time): "500 of 500 destinations carry all five. 0 have an incomplete chain." exit 0. Redirect_Master.xlsx: 2,598 rows, **2,505 verified, 93 still "ruled"** (the checklist said 231 waiting; 138 were written since). The S339 step 5 staging check: not run. The 93 wait for `publish_gate.py --write-redirects-from`, which writes, so I did not run it. Every destination of theirs passes the register, so they no longer wait on unpublished pages (Code's job).
- **A3 cutover gate: PASS (as designed).** `cutover_gate.py` plain, exit 0; closing lines: "The site is hidden, deliberately ... This is the expected state of the build ground". sitemap 1712 addresses; robots.txt 200.
- **A4 old-site backup: already done by the main session.** Folder "Achology Old Site Backup 25 November 2026" in the home folder: `achology-full-2026-11-25.sql.gz` 51,594,645 bytes and `achology-files-2026-11-25.tar.gz` 3,567,277,339 bytes (3.4 GB total), dated 25 November 20:17 and 20:20. Proof is in DONE__Launch_A4_Old_Site_Backup_On_The_Mac_S572. I only listed the folder.
- **A5 Analytics off: PASS.** On the build site `rank_math_modules` lists no `analytics` module. The front-end source of `/`, `/about/` and `/help/` carries no `G-HJ29S4Z0R8`, no googletagmanager and no `gtag(`. Note for B7: the stored option `rank_math_google_analytic_options` still holds measurement_id G-HJ29S4Z0R8 and the Search Console profile `sc-domain:achology.com`; inert while the module is off.
- **A6 Circle words agree: PASS.** Gift page (`/membership/choose-your-free-course/`, 200): "thank you for joining for a full year ... one course of your choice ... enter the name and email address you joined with, and we will add your chosen course to your account within 24 hours". Help answer 47660 (`/help/membership-and-pricing/choose-free-course-annual-achology-membership/`, 200): "After you join ... for the year, you're taken to a page called Choose Your Free Course, where you pick one of nine courses, enter the name and email address you joined with, and Achology adds it to your account within 24 hours". Same page name, nine courses, 24 hours, yours for life.
- **A7 email pictures: NOT RUN.** The test is `curl -A GoogleImageProxy` and `-A "...Outlook"` from this Mac, and SiteGround's robot check turns that away; I did not try to get round it. It needs a route that is not this Mac, and the list of pictures each Kit email shows, which I do not hold.
- **A8 Knowledge Hub published: PASS.** The register's dest_built (all five facts) is OK for `/learn/` and every Knowledge Hub destination: 500 of 500. Published on the build site: article 404 (6 draft, 1 pending), book_note 150, quote 428 (2 draft), workbook 212, faq_article 377 (1 pending).
- **A9 the 45 film posters: PASS.** Named in Home's DSRD6_RECORD.md line 13 ("image-responsive, 71 pictures: 45 film posters ... a 920 frame to be taken from the player at cutover") and in checklist item 9.
- **Organization description and llms.txt (BRIEF S490): NOT DONE.** `/llms.txt` on the build site answers **404** (no file at the root either). Rank Math's `homepage_description` is empty; the definition ("We are taught many things in life ...") appears only as Home's hero text, not in the graph; the graph has one EducationalOrganization node, no description read from it. Home's meta description reads "Achology is an online academy that teaches practical psychology. Learn at your own pace, apply each idea to your own life and help others do the same." `knowledgegraph_name` is "Achology Transactions Ltd"; the site tagline read empty. Code's disposition on the brief says it waits for a quiet sitting.

## 1. A1 detail: the 41 failing pages

**Method (update, row names now read).** The detailed `page_gate.py --no-purge` run finished; row names below are read from its printouts (scratchpad `failrows_clean.txt`, `failrows2_clean.txt`, grouped in `grouped.txt`), not inferred. The two pages Home and `/home/` were not re-run (Home is the Home session's; `/home/` is not a built page). One limit: my first re-run matched a few truncated addresses to the wrong page, so I re-ran `/about/`, `/policies/`, `/membership/`, `/about/instructors/`, Karen Ramsay and Declan Fitzpatrick by hand; the other profiles' rows come from the first run, where five profiles (Karen, Amelia, Jackson, Isabella, Declan) show only the `rank-math` row.

The 41: Home `/`; `/home/`; the Centre of Human Development; the Academy and its seven schools (8); Code of Character; Access All Areas; Membership; Accreditation; Certification; Courses; How We Write; About; Testimonials; Policies; Reviews; Disclaimers; `/about/instructors/`; and the 17 instructor profiles. Only four failing row names exist among them:

**Row 1: `achology-word-1000` and `achology-word-375` (one fault, read at two widths): 16 pages. (a) a real fault Code can mend.** A heading sets the word Achology in the heading's own colour; the ruling (S571) wants it orange, light orange #FFC08F on a dark band. One mend in the shared heading CSS should cover all 16; none of the 16 is mended yet, and the rule's own checker is `tools/achology_word_check.js`. **These are the 10 pages that passed in the S568 rehearsal and fail now (gate v7 added the row, S572):** Academy (1 heading), the seven schools (2 each), Access All Areas (4), Disclaimers (1). **Six more carry it on top of their other rows:** Accreditation (2), Courses (1), Testimonials (1), Reviews (1), About (3), Membership (4). Examples named by the gate: "Practise With a Partner Collaborative Practice ..." on the schools, "What You Can Expect to Learn at Achology" on Access All Areas, "Achology Courses" on Courses, "About the Achology Brand" on Disclaimers, "About Achology" and "Achology Origins" on About.

**Row 2: `rank-math`: 19 pages. (b) waits on Kain's rescore click, plus one (a).** 17 instructor profiles: Karen Ramsay 76, Gaby Tzeschlock 73, Benjamin Lockwood 87, and 82 on Jonathan Frost, Gary Kennedy, Erika Nadeau, Andrew Nelson, Alec Wells, Amelia Sinclair, Jackson Hartley, Isabella Whitmore, Frederick Martin, Evelyn Montgomery, Declan Fitzpatrick, Charlotte Avery (bar is 90). **Not (b):** the Centre of Human Development (post 47676) and Code of Character (post 46067) read "has never been scored: it is not in the score table"; those are (a) for Code (one score run and entry in the score table, by the rule that only Code writes a score).

**Row 3: `dsrd6-record`: 23 pages. (b) Chat's human lines, with Kain rows.** Counts as printed ("closed / not run / fail"): Centre 0/10/1; Code of Character 5/3/3; Accreditation 4/5/1; Certification 9/0/2; Courses 2/6/2; How We Write 8/0/1; Testimonials 0/7/4; Reviews 6/3/2; About 6/3/2; Policies 10/0/1; `/about/instructors/` 3/6/2; and these profiles at 1 fail each: Jonathan Frost, Gary Kennedy, Gaby Tzeschlock, Erika Nadeau, Andrew Nelson, Alec Wells, Gerard Egan, Kain Ramsay (3 fail), Frederick Martin, Evelyn Montgomery, Charlotte Avery, Benjamin Lockwood. The record lines are Chat's and Kain's; Code only writes what they return.

**Row 4: Centre of Human Development only, 4 more rows ((a) Code or the Home session):** `meta-description` 157 characters (limit 155), `address` ("matches no address DSRD 1 names"), `orphan` ("the crawl missed 2053 pages ..." with 404s such as /company/achology/), and `keyword-density` ("the body is empty": the same template-page carve-out Chat ruled for Home in ANSWER S492, not yet entered for the Centre). Its other rows are recorded carve-outs.

**Sort in one view:**
- **(a) Code can mend:** `achology-word` on 16 pages (one mend), the Centre's four rows, and the Centre and Code of Character score entries.
- **(b) Chat or Kain must rule or do:** the `dsrd6-record` human and Kain rows on 23 pages; 17 profile scores below 90 (Kain's rescore click).
- **(c) a gate row to teach (exception):** none seen except the Centre's `keyword-density`, which wants the template-page carve-out Chat already ruled for Home.
- **Home** (2 fail) and the Centre's wider rows are the Home session's; `/home/` (1 fail) is a sitemap entry, not a built page: Code to confirm it is a draft and drop it from the sitemap.

Also found: `BRIEF__Accessibility_Statement_Stops_Saying_The_Site_Is_Being_Rebuilt_S492` is still open, so that page still says it is being rebuilt; it must be done before launch.

## 2. Old site coverage

Read only, over SSH and WP-CLI on the old achology.com (permalinks `/%category%/%postname%/`, Yoast). Every published post of every public type, every term of every public taxonomy, every author with published posts, and the home. Normalised to lower case, path only, trailing slash, then compared with Redirect_Master's `old_url` column.

- **Old-site addresses read: 9,859 (9,777 distinct). Redirect_Master rows: 2,598.**
- **Fully covered (0 missing):** posts 157; pages 34 of 35; products 37; books 80; ht_kb 213; videos 168; schools 7; instructors 2; publications 1; resources 2; job openings 25; and the non-empty terms of category, post_tag (127), quote_author (506), quote_topic, video-series, video-categories, ht_kb_category, book_categories, product_tag, resource_cat, job-category, ld_topic_category.

**Missing, with a suggested destination from the map's own patterns:**

1. **achology-quotes, 7:** `/achology-quotes/` + benjamin-disraeli, newt-gingrich-2, johann-wolfgang-von-goethe-4, erich-fromm, carl-jung-3, anne-frank-2, alain-de-botton-10. The map sends 976 of its other quote rows to **`/learn/quotes/`**; suggest the same.
2. **Author archives, 30:** `/author/` + alec-wells, alicia, andrew-nelson, assiakoss, beatriz-fernandez, cosmina, derek-seller, ejcc, emmeline-van-zyl, euansimplicity-marketing-co-uk, gabriele-tzeschlock, jamesmeetsimplicity-com, jeffrost, jennifer-anne-yvette-carrion, karen, marketing-team, mary-nel, matthew-day, melcyp7, new-thinking-new-life-now, pookaadmin, priya-mohannair, reiss-julien, rupali-tanna, sri-wahyuni, stacy-anderson, tinasax, tonilee, web-team, yifan-nairn. The map's 9 `/author/` rows go to `/about/instructors/` or a profile; suggest **`/about/instructors/`**, or the profile for alec-wells, andrew-nelson, gabriele-tzeschlock and karen. Yoast leaves author archives indexable when the author has posts.
3. **Home `/`:** no row, correct (same address on the new site).
4. **Product category with products, 1:** `/product-category/achology/the-school-of-neuro-linguistic-programming/`; the map sends its other 12 product categories to `/courses/` or a school; suggest **`/academy/neuro-linguistic-programming/`**.
5. **Empty terms (no posts), no row:** 306 post_tag, 38 resource_cat, 51 ld_course_tag, 15 ld_course_category, 10 ht_kb_tag, 9 quote_author, 3 product_cat (community-subscription, event, new-template-2023), 2 product_tag (bundle, community), 1 each of job-category, ld_lesson_tag, video-series. Suggest the destination of their non-empty siblings (tags to the category hub, product_cat and tags to `/courses/`, resource_cat to `/membership/`, quote_author to `/learn/quotes/`, LearnDash ones to `/academy/`). Chat's call whether an empty archive needs a row.
6. **Not indexable, members-only, no row:** LearnDash topics 6,219, lessons 370, quizzes 17, certificates 80 (Yoast noindex true on all four) and jet-menu 19 (noindex). Suggest **`/academy/`** as one catch-all, or let them fall to the 404 page. Chat's call.
7. **No pretty address (query-string only):** elementor_library 71, jet-form-builder 10. Nothing to redirect.
8. **Guessed, not in the records:** `/blog/`, `/shop/`, `/cart/`, `/checkout/`, `/my-account/`, `/feed/`. The WooCommerce page IDs are not published pages in the records. The old site's Yoast sitemap index itself could not be read (curl from the host to itself answered 000), so the comparison is from the database, not the sitemap.

Full lists, one address per line: scratchpad `coverage_missing.txt`; patterns used: `coverage_patterns.txt`.

**Map rows whose destination does not answer 200 on the build site: none.** The register measured 500 distinct destinations, all built with all five facts. Two rows point off-site or are ruled gone and carry no chain.

## 3. What stands between today and launch day

1. A1: 41 fails; 10 are new since S568 (Academy, seven schools, Access All Areas, Disclaimers); Code reads their row names first. The rest wait on Chat's human lines, Kain's rescore click and the Home session.
2. A2: write the 93 rows (`publish_gate.py --write-redirects-from`), run the S339 step 5 check, then re-run the register and one-hop.
3. A7: needs a route that is not this Mac.
4. The Organization description, the tagline and `/llms.txt`.
5. Section 2 items 1 to 6: Chat's rulings, then the rows.
6. The accessibility statement's "being rebuilt" text.

OWED BACK: rulings on section 2 items 1 to 6; whether Home and `/home/` stay in the A1 list; whether the LearnDash members-only addresses are meant to fall to the 404 page.

*No em or en dashes in this file; checked before writing.*
