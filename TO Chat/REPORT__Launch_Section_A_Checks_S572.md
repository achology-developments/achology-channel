> Stays, Chat S492, 25 Nov 2026: read in part (summary and section 1). Its section 1 group (b), the human record lines of about 25 pages, is Chat's; carried to Session 493 first. Its llms.txt "NOT DONE" is out of date (done at S573, DONE__Organization_Description_And_Llms_Txt_S573). Waits on Chat ruling the section 1 sorting.
For the main launch session (Chat reads it after): what this needs: rule on the sorting in section 1, and pick up the fixes named per item. Nothing on either site was changed; nothing was asked of Kain.

Done when: every red line below has an owner and a fix.

**DOCUMENT TYPE:** read-only report from a Sonnet helper (Code S572). Theme 0.708.488 on the build site, 25 November 2026. `page_gate.py --map --no-purge` was used on purpose, so no cache was purged.

## Summary, one line per item

- **A1 gate sweep: FAIL.** `page_gate.py --map --no-purge` over all 82 addresses of the build site's page sitemap: 41 pass, 41 fail (exit 1). Rehearsal S568 was 51 pass, 28 fail over 79: **10 pages that passed then fail now** (section 1).
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

**Caution on method.** `--map` prints counts, not row names. A second, detailed run over the 41 pages (to name every failing row) was still running when this was written, so **row names below come from the rehearsal S568, the gate's own docs and inference, and each inference is marked.** Its printout will be the scratchpad file `failrows.txt` if it finishes; read it before mending.

The 41: Home `/`; `/home/`; the Centre of Human Development; the Academy and its seven schools (8); Code of Character; Access All Areas; Membership; Accreditation; Certification; Courses; How We Write; About; Testimonials; Policies; Reviews; Disclaimers; `/about/instructors/`; and the 17 instructor profiles.

| Group | Pages | Fail rows | Sort |
|---|---|---|---|
| Home | `/` (2 fail, 10 review) | being closed by the Home session | not mine |
| `/home/` | 1 fail, 0 pass | in the page sitemap but not a built page (a draft per the rehearsal) | **(a)** Code/main: confirm it is a draft and drop it from the sitemap or the list |
| Centre of Human Development | 6 fail | the Home session's (S568 said so) | not mine |
| **NEW since the rehearsal (passed then, fail now): Academy, the seven schools, Access All Areas, Disclaimers** (10 pages) | 2 fail each | rows not named. **Inference only:** exactly two rows each, and gate v7 (S572) added `achology-word-1000` and `achology-word-375` | **(a) or (c): Code to read the detailed printout first.** If it is `achology-word`, one mend over all ten (heading word Achology the heading's own colour) |
| Instructor profiles (17) and `/about/instructors/` | 1 or 2 fail each | S568: record lines and stored Rank Math scores | **(b)** the record's human lines are Chat's; stored scores wait on Kain's rescore click; not a Code machine fault |
| Code of Character, How We Write, Courses, Accreditation, Certification, About, Testimonials, Policies, Reviews | 1 to 3 fail each | S568: each record's human lines, and Rank Math on three | **(b)** Chat places the human lines; Rank Math scores wait on Kain's rescore |
| Membership | 2 fail | outside the rehearsal's list | **(b)** Chat (its gate lines carry Chat's rulings) |

The honest gap: I could not group the rows by name.

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
