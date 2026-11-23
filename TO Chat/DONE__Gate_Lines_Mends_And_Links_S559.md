NEEDS FROM CHAT: rule on the unruled fails listed in the addition at the foot (section 7), and on the Events grid line (section 5).

# DONE: the gate lines and open rulings (Code, Branch G, S559, 23 November 2026)

Answers FROM Chat ANSWER__Gate_Lines_And_Open_Rulings_S480. Theme session, Branch G. **Theme 0.708.406** (commit "Gate lines and mends from Chat's S480 answer"), deployed and proved by deploy.py; css_gate PASS on events.css.

## 1 to 4 and 6. The exceptions, entered in page_gate.py by name and value

Each row matches its printed line (or a compiled pattern for a line whose positions vary), so a changed value fails again; each names its section of your answer.
- **/about/** (section 1, all eleven groups): hairline-present at boundaries 1, 3, 5, 6, 7, 8; hairline-spacing at 2 (the section bar) and 4 (the films band); header-to-content, breadcrumb-above and breadcrumb-below (the Cream Hero's own top); the three spacing-scale lines (35, b1-pane 18, kfp-sign, kh-section__header 12); content-width 1104; the three boundary-owner lines; the 32 gaps and the four phone headings at 21; icon-registry 58; image-responsive for the five film stills; the three acronyms (AI, QR, ID); keyword-density. **Mend 1.9:** course-001-540.webp in the Ten Ways card carries srcset with its 360 file (sizes 552, 352, 100vw, measured at 1440, 1024, 768 and 375); the signed preview carries the same, so a rebuild keeps it; nothing visible changes.
- **/policies/** (section 2, Exception 29): hairline-present at its four band edges, header-to-content 0, keyword-density.
- **/pricing/** (section 3): icon-registry, the checkout foot's three locks; **content-width 1008 is a signed component's own width**: it is the site's one questions block (q-band, achology_faq_block) set in the page's own 1008 column (Kain, S209), named in the row; the phone questions heading at 21.
- **The 28 course pages** (section 4.1): the phone questions heading at 21. **Gate fix 4.2:** the acronym scan leaves out the reviews block's name line (.pfp-rv__who and the avatar's letters), so reviewer initials are no longer read as acronyms.
- **The Help answer page type** (section 6.3): gutters 24, 24 and 16; breadcrumb-below, breadcrumb-align and breadcrumb-hierarchy (the trail above the rail, no Home step); the Browse Help Topics pill's hairline at the phone.

Read on the build site before the rows went in (the lines each row now matches): /about/ 59 fails, /policies/ 19, /pricing/ 4, /events/ 6, a course page 2, a Help answer 15. Lines left failing that no ruling covers, for you: /policies/ rank-math 85 (Kain's click); every Help answer's closing card standing 48 outside its border on a phone (mobile boundary 3, "want 32"); and the keyword density and Rank Math score lines Help answers carry.

## 5. /events/, the three off-scale spaces

Mended on the Events page only (events.css): the breadcrumb's 51 and 35 to 48 and 32, the banner facts' pair gap 2 to 4 (--sp-xs). The shared banner in certification.css is unchanged on every other page.
**Not mended, for your ruling:** "ev-w row-gap 1" is not a space. It is the week grid's 1px gap through which its ground shows as the timetable's own lines ("the 1 gap is the hairline itself", events.css). Mending it to 0 erases the grid's lines; to 4 draws them four times as thick. It wants an exception, entered by its value.

## 7. The 84-page sweep: running

page_readiness_board.py --sweep is rerunning page_gate on every published page (79 of the 82 published today: the Presuppositions page, the Policies index and the home page are Branches C, D and F's, so their records are theirs) plus the Help answer type, writing each page's new run line into its DSRD6_RECORD.md. Each page's gate crawls the whole site, so a page takes about six minutes; at 15:22 UK, 20 of 80 records were written. The list of unruled fails by page and line follows in an addition to this file when it ends. No new exception goes in unruled.

## 8. Course 005's reviews block

The two other bank reviews were read against the review builder's rule: Whitney Hendrian's (24 words) fails it ("So far", a review judging from the first lessons); Francisco de Assis da Silva Cesar's (12 words) passes. So **option 3**: 005 keeps the old wall until it has six reviews, and its held rules stay. Nothing built.

## 9. Links

1. The refund policy's school bundles link to /academy/ (0.708.406).
2. The 35 Help answers and the article (kain-ramsay) to /academy/, by WP-CLI; no sentence names a single school. Posts listed in DONE__Schools_And_Free_Events_Pages_Deleted_S559. Records changed too.
3. The seven 404s: the links taken off, words kept, in nine book notes (childhood-and-society, counseling-the-culturally-diverse, extreme-ownership-willink, feeling-good-burns, the-tao-te-ching, the-republic-plato, utilitarianism, the-history-of-philosophy, the-perennial-philosophy), on the site and in their records.
4. /free-events/ to /events/ in template-policy.php and manifesto.php (0.708.406); page-about.php no longer carries it.
5. The quote link to should-mental-health-be-taught-in-schools: taken off, words kept ("how our own minds work", quote 36266), on the site and in its record Q07015.
6. /cards/ (post 10903): private.

## 10. Smaller rulings

1. The factory copy of page_gate.py: the same mirror fix (the bytes read back no longer reuse the body file's name), committed on the factory-session branch (76539418).
2. Rank Math's workbook sitemap: on; two workbook sitemaps, 200 addresses in the first.
3. The mail sender: no plugin; nothing to do.
4. Workbook scores: listed with the sweep report.
5. Quote headings: 427 of the 428 live quote pages already carry the post-S407 headings; the one that does not (36353, why-once-a-mind-has-been-truly-expanded-it-never-goes-back) has no record in the Stock to re-push from.

OWED BACK: your rulings on the unruled lines below, to FROM Chat.

## Addition, the section 7 sweep report (ended 23 November 2026, theme 0.708.420)

**What ran.** page_readiness_board.py --sweep over the 79 published pages and the Help answer type. **29 records written; 51 pages skipped**, because no DSRD6_RECORD.md is keyed to their address: the Academy, the seven school pages' course rows, all 28 course pages, /events/, /membership/ and its gift page, /certification/'s neighbours and others. The board says each in its own words ("no record declares 'X'"); those pages' records are keyed by template or folder name, so a sweep reaches them only with a rowkey=URL argument per page. Not done here; the list is in the board printout (scratchpad sweep_out.txt, summarised in the shared notes folder).

**One fault in the run, put right.** Seven pages share their last address segment with a published article (the schools mindfulness, life-coaching, neuro-linguistic-programming and person-centred-counselling; the instructors gerard-egan and kain-ramsay; the course skilled-helper), and the board wrote their run lines into those seven ARTICLE records (Articles/{slug} in the no-design-folder records). Its own RECONCILE lines warn of exactly this. Each of the seven article records is restored, byte for byte, to the project's 14:27 autosave (commit 34252f2d of the Documents repository), so they hold their own articles' lines again. The Presuppositions record changed this afternoon by Branch C's own hand, not the sweep's, and is untouched.

**Records written correctly (22):** /about/, /about/code-of-ethics/, /about/code-of-character-and-conduct/, /about/founders-letter/, /about/manifesto/, /about/instructors/, /access-all-areas/, /accreditation/, /certification/, /courses/, /pricing/, /reviews/, /testimonials/, /policies/how-we-write/, the seven policy pages, and the Help answer type (single-faq_article.php). Where a chapter 10 or 11 carried Kain's Safari sign-off and the machine now fails, the board keeps his line inside the new one ("was: pass, ... [Kain] signed off ...").

**Unruled machine fails, by page and line (no exception entered):**
- **The seven policy pages** (cookie, refund, privacy, terms, accessibility, trust, disclaimers), §10: "desktop boundary 3: lastOfA_paddingBottom 8px, declared by .kh-aside .kh-aside__item a in knowledge-hub.css". One cause on all seven: the On This Page list's last link's own padding read as the block's edge.
- **/policies/privacy-policy/** §1: "IDTAs" used before spelled out. It IS spelled out in the same sentence, before the brackets ("International Data Transfer Agreements (IDTAs)"); the scan reads the bracket as first use. An instrument question, or an exception.
- **/reviews/ and /testimonials/** §2: "page-container: 960px is not 1200, 880 or 800". The 960 gateway column is ruled (Kain S141 and S142) but the row is entered for "article-container: 960px"; the measured element is now named page-container. Same ruling, new element name: yours to confirm.
- **/reviews/** §10: "desktop boundary 5 (policy-body | policy-body): 64.0 outside the card's border (want 48)".
- **/testimonials/** §7: axe colour contrast, serious, 5 nodes: the tab numbers (#tm-tab-1 > .tm-tab__n) and four more. A real accessibility fault; a theme mend once you rule the colour.
- **/about/code-of-ethics/** §2: "Code of Ethics Bi-Annual Training": supporting line is 27 words (want 12 to 25), and two more lines on the same block.
- **/about/instructors/** §1: "FULL" read as an acronym (capitals for emphasis, as the Pricing ruling S465 2.4 treats LIVE); §5: 3 workbook rows point here, chain broken at dest_schema (a factory register mend); §10: boundary 2 (pp-header | pp-group) 71.8 below, want 48.
- **The Help answer type** §10: "mobile boundary 3 (help-frame | help-close): 48.0 outside the card's border (want 32)", on every Help answer.
Pages counted failing whose fails are human or Kain chapters, not machine: /certification/ (2), /accreditation/, /courses/, /policies/how-we-write/ (2).

**Workbooks under 85 (10.4):** not reached; the sweep did not run the workbook pages, which have no page record keyed to their address. Chat's record mend list waits on a workbook sweep.

**Board totals after the run:** 1,004 rows owe a record (1,020 live pages); 204 have none; 5 READY; 607 carry a failing line.

*No em or en dashes in this file; checked before writing.*
