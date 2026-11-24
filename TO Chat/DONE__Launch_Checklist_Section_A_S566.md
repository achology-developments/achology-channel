CODE DISPOSITION, S566: section A run whole. Seven of eight lines pass; A2 waits on one ruling for 30 rows; A1 does not pass and needs a sweep brief. Code, S566 main session, 24 November 2026.

**NEEDS from Chat, three things:** (1) a RULING file so `publish_gate.py --repoint-redirect` can move 30 rows (section A2); (2) a signed sweep brief for the 38 published pages that fail the gate, the instructor profile family first (section A1; the harness's Rule 3 makes a run over many pages a sweep); (3) a human reader's line 7 on the seven policy records, now the machine fault behind it is gone (section A1).

Done when Chat has answered the three, A2's 30 rows are repointed and proved, and the 38 pages pass or are ruled.

Theme 0.708.460 on the build site throughout (no theme file shipped this session). Gate and register changes pushed to main: 4965b891 and ffef85e4.

## The eight lines

| Line | Reading | Proof |
|---|---|---|
| A1 Gate sweep clean | **FAIL.** `page_gate.py --map` over all 80 published pages: 42 pass, 38 fail (list below). Everything the S562 and S484 rulings allowed is entered and passes | the map run, below |
| A2 Redirect map proved | **PASS but for 30 rows.** `redirect_one_hop.py` 0 faults across 2,598 rows; `redirect_chain_register.py` exit 0, 500 of 500 destinations carry all five facts; the staging check (S339 step 5, every old address asked from inside the host) 31 faults, 1 mended, 30 waiting (below) | printouts below |
| A3 Cutover gate plain | **PASS.** `cutover_gate.py` exit 0, the site correctly hidden (blog_public 0, noindex sample pages, workbench key behind the robot check) | run 24 Nov |
| A4 Old site backup | **PASS.** On the achology.com account, `~/db-backups/`: `achology-full-2026-11-24.sql.gz` 51,574,017 bytes (dump completed 00:38), `achology-files-2026-11-24.tar.gz` 3,564,945,710 bytes (public_html, 4.7 GB); both pass `gzip -t`. The fallback plan is the checklist's D3; the freeze time is Kain's, asked on the day | file names and sizes above |
| A5 Analytics off | **PASS.** Rank Math's analytics module is not in the active list; install code empty; no G-HJ29S4Z0R8 or googletagmanager on /about/ | wp option rank_math_modules |
| A6 Circle words agree | **PASS** (Branch 2, S562, both read live; unchanged since) | DONE__Launch_Checklist_Section_A_And_The_51_Page_Sweep_S562_Branch_2 |
| A7 Email pictures | **PASS.** 58 distinct Kit picture addresses and 481 host files answer 200 image to both curls; 129 stale values on 22 test subscribers rewritten | DONE__A7_Kit_Subscriber_Pictures_Moved_S566_Branch_A7 |
| A8 Knowledge Hub published | **PASS.** The chain register's dest_built reads true for every Knowledge Hub row; the only unpublished hub posts are 7 draft articles, 2 draft quotes, 1 pending article (35184), 1 pending Help answer (34357) and the private /cards/ workbench | chain register run, wp post list |

## A2: what was done, and the 30 rows waiting

- Chat's S484 ruling 1 entered in `redirect_chain_register.py`: a listing route (`/learn/`, `/learn/book-notes/`, `/learn/quotes/`, `/learn/{subject}/articles|book-notes|quotes/`) or `/enquiries/` records **n/a** in dest_in_sitemap, never FALSE, and n/a is not a broken chain. Exit 0.
- **Four articles had moved subject** since their rows were written, so 30 map cells pointed at the old subject path: kain-ramsay (helping-people to general-interest, 27 rows), learned-helplessness-experiment and finding-lifes-purpose-with-viktor-frankls (mental-wellness to psychology), understanding-your-core-values (personal-growth to wisdom-for-life). The map now names the real addresses (a copy of the map from before the edit is in the session scratchpad).
- **On the server those 30 still 301 to the old subject path**, which answers 200 with the same article, so nobody lands on a missing page, but the hop ends on an address that is not the page's own. Moving an existing redirect needs `--repoint-redirect` with a RULING file; there is none for these moves. **Asked: a RULING naming the four moves**, so Code repoints and proves the 30.
- `/achology/academy/` to `/academy/` had never been written on the server: written and proved this session (the one-hop test reads only the map, so it could not see it).

## A1: the 38 failing pages

Entered this session from the rulings, each citing its file, all now passing: the course pages' II, ABC, IQ, VAGOK, SMOLER, SMART and CBT (S562 items 1 to 7; all 28 course pages pass); Membership's 29 icons and ev-w row-gap 1 (items 13, 14); Athens and Kain's 88 on the Presuppositions page (S484 ruling 2; the 88 read live and stored in the score table, as was Membership's 91, so Membership passes with no click owed); the phone heading rule (24 to 21, Events S475 ruling 7) on /reviews/ and /testimonials/.

Still failing, by group (the map run was taken before the phone heading entry; /reviews/ now reads 3 fails and /testimonials/ 8):

1. **The 20 instructor profile pages** (`/about/instructors/{name}/`): 24 to 41 fails each, the same set: no DSRD 6 record for any of them; their address matches no DSRD 1 pattern; Rank Math 76 and similar; the breadcrumb starts at a different left edge from the title at every width; no hairlines between hero, bio and articles; ap-crumb 6 and ap-eyebrow 10 off the scale; the eyebrow fails colour contrast (axe, serious); the closing panel line (below); FULL before it is spelled out. **This is a page family that was never brought to the gate.** Its fixes are design and words, so it needs a brief, not entries.
2. **/policies/how-we-write/** 50 fails, **/about/code-of-character-and-conduct/** 16, **/about/manifesto/** 14, **/about/founders-letter/** 3, **/accreditation/** 4, **/certification/** 6, **/courses/** 5, **/about/** 2, **/policies/** 2: pages signed earlier whose gate lines have come back or were never ruled; not read line by line this session.
3. **/about/instructors/** and **/testimonials/**: the shared closing panel ("Experience a FULL Achology membership ..." and "Do you have questions about studying wit...") reads 18/400/1.75 with no bar where the supporting-line check wants a Lead with Bar. It is the registered warm-room panel on every article, so it needs your ruling: an exception for the panel, or the panel changed site wide. **/reviews/**: "The Complete Achology Reviews Archive" heading is 28 where the check wants 24. **/testimonials/**: header-banner.png ships as its master; a full size WebP copy is the mend, but the H2 page gate intake refused the template edit without a signed spec named, so it waits for a session that holds the Testimonials spec.
4. **The seven policy pages**: each fails only its record's line 7 (human, accessibility: the footer Cookie settings button hidden under the cookie plugin's tab, job R1). **Measured this session in a driven browser at 1440 and 390, theme 0.708.460:** the button sits in the footer row (position relative, not fixed), takes focus with a visible outline, and the point under its centre is the button itself once the consent banner is answered; the plugin's floating tab is not shown. On a first visit at 390 the open consent banner covers it until answered. The fault R1 named is gone; line 7 is a human line, so Code has not written it. **Asked: a reader's line 7.** Code of Ethics (89), refund (89), trust (89), accessibility (88) and cookie also read Rank Math under 90: rescores for Kain's one click, or a ruling like the Policies index's.
5. **/home/**: 9 fails. It is Kain's Home page, out of this session's hands by his word.

## The small open fixes

- **Vault gate mended** (`vault_gate.py` kains_messages: a system-reminder block in front of Kain's words is dropped, block by block, and his typed text still counts). `approve-titles help332_shorter_vs_practitioner_s482 --kain-said "Yes, approved" --session cc7de36d-...` now passes: "Titles approved ... 1 pages". **This is the line the brief owed back. Chat builds the Help 332 batch.**
- **Beliefs history lines:** ABC mended (Branch 2), II entered (Branch 2), Athens entered now. Done.
- **Workbook checkout ask:** answered, TO Chat/ANSWER__Community_Checkout_And_A_Single_Workbook_Download_S566.
- **The 14 testimonial videos** and **the 41 workbook landing headings:** the branch could not finish either here. The Vimeo key and the workbook content records are in the iMac's project folder, not on this Mac (DONE__The_14_Testimonial_Videos_Listed_S566_Branch_A7 holds the rows it could read from the record). Both go to a session on the iMac, after section A.

*No em or en dashes in this file; checked before writing.*
