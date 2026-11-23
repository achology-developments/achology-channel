> Chat S480, 23 Nov 2026: stays in TO Chat as the live launch checklist; waits on launch day. Section D is ruled in FROM Chat/ANSWER__Launch_Move_Order_Checklist_Section_D_S480 and RULING__Nothing_Of_The_Old_Site_Is_Kept_S480; the branch filling it writes those rulings in.
> Back in TO Chat as the live checklist, Code S559 (Branch G), 23 November 2026: the S480 launch jobs add lines to it (each marked S559). Earlier head line kept below.
> Disposition, Chat S480, 23 Nov 2026: section D ruled in FROM Chat/ANSWER__Launch_Move_Order_Checklist_Section_D_S480; the order written into PLAN__Rollout_From_Build_Site_To_Achology_Com; archived. No board card moved.

**NEEDS from Chat: read once, rule on section D, add the order of the move to the rollout plan.** Code, Branch B of the 23 November 2026 launch plan, S553. Nothing in this file has been done; nothing is switched. It is a checklist prepared from PLAN__Rollout_From_Build_Site_To_Achology_Com (Project Delivery System folder) and the channel's earlier cutover thinking, so launch day is a short, proved step once the Home page is signed.

# Launch switch-over checklist

Each line says what is done, who does it, and the proof that closes it. Code guides Kain one step at a time on anything that needs his hands.

## A. Before the day (Code, no switch touched)

1. **Gate sweep clean.** page_gate.py --map over every published page; every fail fixed or ruled as an exception; each page's DSRD 6 record current. Proof: the printout.
2. **Redirect map fully written and proved on the build site.** Redirect_Master.xlsx: 2,595 rows; the S496 reading is 2,364 verified; the 231 rows whose destination pages were not yet published need `publish_gate.py --write-redirects-from` rerun on the full map once their pages are published. Then `redirect_chain_register.py` (exit 0), `redirect_one_hop.py` (0 faults), and the S339 step 5 staging check, green. Proof: the three printouts.
3. **The cutover gate reads clean in its plain run.** `cutover_gate.py` (site correctly hidden, exit 0), so the --golive run on the day is only the flip's proof.
4. **Old-site handover plan in SiteGround.** The old achology.com is in Kain's own account (SESSION S543). Before the move: a fresh full backup of its files and database (database backup path `~/db-backups/` on that account), kept; the old site frozen read-only for the move window. Proof: backup file names and sizes.
5. **Google Analytics hazard kept off.** Rank Math Analytics (G-HJ29S4Z0R8) stays OFF on the build site until step B7.
6. **Circle redirect words agree.** The Help answer "How do I choose my free course with annual Achology membership?" and the gift page agree on what a new annual member is told (Chat's ANSWER and DRAFT__Help_Answer_Choose_Free_Course_Annual_Membership_S549).

## B. Launch day, in this order (Code guides Kain)

1. Freeze the old site (no edits, no orders; it takes no payments, Circle does).
2. Move the new site onto achology.com (see D1: method not yet ruled).
3. Certificates and DNS answer for achology.com and www; https works everywhere. Proof: a browser opens https://achology.com/ and https://www.achology.com/ on the new theme.
   - **Site mail sender (S559, BRIEF__Free_Course_Journey_Gaps_Closed_S480 item 1).** achology.com's SPF gains SiteGround's sender for the new plan (today it reads `v=spf1 ip4:192.168.0.0/16 include:_spf.google.com include:mail.zendesk.com ~all`; achologytest.com's own record names `include:achologytest.com.spf.auto.dnssmarthost.net`), and the new plan's DKIM key for achology.com is in the zone. The site sends with WordPress's own mail through the host's sendmail, From wordpress@ the site's domain (read on the build site, S559). Note for Chat: section D ruling 4 says SPF and DKIM do not change on the day; this line is the one exception the journey brief asks for, and Chat reconciles the two.
4. **Search visibility on:** `blog_public` 0 to 1 (Settings, Reading) on the live install. Then `cutover_gate.py --golive` must exit 0: no blanket Disallow in robots.txt, sitemap reachable and naming real addresses, sample pages (/about/, /policies/privacy-policy/, /help/) carry no noindex, canonicals present, and `/cards/?workbench=specimen-page-s267` on achology.com answers 404. Proof: the printout.
5. **Redirects on.** The map applied through Rank Math's Redirections module on the live install; spot-check a sample of old quote, author, article and course addresses to one hop (301 straight to the final page); `redirect_one_hop.py` rerun against the live map.
6. **Sitemap.** The Rank Math sitemap index answers on achology.com; submitted in Search Console; the Knowledge Hub is in it (an S079 finding to confirm closed).
7. **Analytics and Search Console on.** Rank Math Analytics and Search Console connected on the live domain only, never before.
8. **Speed Optimizer image handling on** (compression, WebP, lazy loading), after content is final.
9. **Circle annual paywall redirect.** Before it goes on (S559, journey brief item 1): one claim through the live gift form marked TEST reaches Karen's inbox and a member test inbox, in the inbox and not spam; if not, stop and tell Chat (the fix is a sender route through Google Workspace). Then: Post purchase tab, Custom redirect URL set to https://achology.com/membership/choose-your-free-course/ (Kain's hands, Code guides one step at a time, per NOTE__Circle_Gift_Redirect_Waits_For_Launch_S544). The address first opened in a browser by Code. Proof: Circle's preview or one test annual path lands on the page with its nine cards; Code checks the Help answer and the redirect agree before the day closes. Also (S559, journey brief): add https://achology.com/membership/choose-your-free-course/ to the annual member's welcome message in Circle, so a member who closes the tab can find the page again (Kain's hands, Code guides).
10. Re-run the checks the build site could not: DSRD 6 section 4 schema check (the build site's captcha wall blocked it), the indexing consistency reading, the links-resolve check on the live host.
11. The old site's handover: the old install is left intact, off the domain, behind no public address, until Chat rules how long it is kept (D3).

## C. Day-after checks (Code)

1. 404 log in Rank Math reviewed after one day and one week; any old address not in the map is added.
2. Search Console: coverage and sitemap status read; Analytics receiving.
3. Email set (sender domain records) and any form that posts to Kit or the course-gift mail confirmed from the live host. The forms that email from the site itself (S559): the Enquiries form (enquiries-setup.php; its correction topic, the Spotted a Mistake flag, goes to the editorial inbox) and the gift course choice (course-gift.php: Karen's alert and the member's confirmation). The Roundup and the free lesson, teaching, workbook and event sign ups post to Kit and send from Kit, not from the site.

## D. Not decided anywhere I can find; Chat rules, then these lines are filled

The rollout plan itself says the order of the move is "still to be written with Kain". These are the open choices, listed, not chosen:

1. **The method of the move:** point achology.com's DNS and domain at the build site's SiteGround account, or copy the build install into the achology.com account over the old one. Either changes B2, B3 and the old site's fate.
2. **The achologytest.com hostname after launch:** left noindex and password-free, redirected to achology.com, or taken down.
3. **How long the old install is kept** and where.
4. **The email records** (SPF, DKIM) if the domain's hosting account changes.
5. **Kit, Circle and other places that hold achologytest.com links:** a one-time search for any stored address that points at the build host.

*No em or en dashes in this file; checked before writing.*
