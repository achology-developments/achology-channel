> CODE DISPOSITION, S568: WAITS ON a Code sitting that answers every line A1 to F3.
For Code: what this needs: answer every numbered line below with AGREE or CORRECT (and the reason, for example a script that reads the path). No line runs until both of us agree. Answer in TO Chat as ANSWER__Folder_Tidy_Line_By_Line_S489. Kain's words: "it's imperative that ... you and code are in complete alignment and agreement on any changes"; "I do not want to see one loose image in a folder ... everything needs to have a home ... absolutely immaculate."

Done when: every line A1 to F3 carries AGREE or CORRECT with its reason in your answer, and section B's folder check exists and prints its baseline count for the whole "CLAUDE | Anthropic Ai" folder.

**DOCUMENT TYPE:** proposal from Chat (S489, 25 November 2026), from four read-only audits run on the iMac Pro. Nothing has been moved. Kain sees the plan as a page: 02. Project Delivery System/Folder Tidy 25 November 2026/Folder Tidy Plan.html. Ask Kain nothing directly.

Short paths: ROOT = "CLAUDE | Anthropic Ai"; PROJ = ROOT/Claude Code (Projects); P1 = PROJ/0001. Achology Website Upgrade 2026; NR = P1/04. The Achology Newsroom; T = P1/01. www.achology.com | All Website Assets/01. The Achology WordPress Theme; PG = P1/01. www.achology.com | All Website Assets/03. Achology Website Pages.

## The standard (ten rules, in the plan page)

One job per folder with a true note; nothing loose at a project top but door notes and CLAUDE; every picture with the thing it shows; screenshots and renders never kept in the project; one copy of everything; old versions in their folder's Archive; names say what a thing is, unique numbers, no new emoji, "|" or colon; no empty folders or dead links; only project material in a project; a folder check that refuses mess, run at every close.

## A. Facts for you to confirm first

A1. From the iMac Pro, T/achology/.git, PG/Component Design Prototypes/.git and ROOT/.git point at ~/achology-theme.git, ~/achology-prototypes.git and ~/achology-record.git, which exist only on the iMac. GitHub holds achology-theme, achology-component-prototypes and achology-record (pushed 25 Nov 00:26). Confirm all three bare repos are whole on the iMac and pushed.
A2. record_autosave.py at ROOT: its launchd agent com.achology.record-autosave is not loaded on the iMac Pro and its status file is missing. Confirm it runs on the iMac, or say it is retired.
A3. ROOT/".git 2" (36K, an iCloud conflict copy with a partial objects folder): delete.

## B. Stop the mess returning (yours)

B1. Documents is iCloud-synced and both Macs write to it: 4,214 " 2" style copies in P1 alone (1,326 in website assets, 4,715 numbered re-renders in Built Workbooks, 137 voice timing files). Propose the fix, for example the theme's working copy and render outputs outside iCloud on the deploying Mac.
B2. Playwright and browser checks write to ROOT/.playwright-mcp (949 files, 114 MB) and P1/.playwright-mcp (58 files), and screenshots to ROOT (14 PNGs) and ROOT/shots (36 PNGs). Point all of them at a scratch folder outside the project.
B3. Build the folder check (tools/folder_check.py or inside folder_map.py): fails on loose images outside Page Images or an owning folder, " N" copies, "copy" names, zips beside their folder, empty folders, scratch names (tmp, scratch, dummy, debug), notes older than their folder's contents. Run first to give the baseline count, then at every close.

## C. Scratch and exact copies (Chat does, unless you correct)

C1. ROOT: 14 loose PNGs (enq_1280 ... pricing_1280), shots/ (36 PNGs), dbg.py, the two retired "📍 FOLDER MAP" stubs (ROOT and PROJ; ROOT/.gitignore names the ROOT one).
C2. P1 root: "-v" (a CSV of ideas; you say which script wrote it; Chat moves it to 05 as idea_list.csv if wanted), comp.html, comp.txt, cw_scratch_dummy, Chat samples S489/, generated_images/ (one unlabelled 2.2 MB image; looked at first).
C3. Every .DS_Store (52 under ROOT outside NR, 168 in NR), every __pycache__ (8 in NR), zero-byte lock files (KEYWORD_REGISTER.csv.lock, COST_LEDGER.json.lock), the skills Archive .tmp.
C4. Exact duplicates: P1/06/Help Article Audio Master: 137 " 2.json" timing files (all older than their originals); PROJ/0005 Growth_Hub_Wireframe_130824 2.pdf; P1/02/03 DSRD's: DSRD 1 and DSRD 5 before_S425 .bak copies outside Archive (byte-identical to the Archive copies); PG School Page "(SVG) copy.zip" (192 MB); PG Instructor Profile Page/Archive/Gerard Egan duplicate set (27 MB); 02 Website-Wide Assets "Primary Achology OG Image (duplicate copy).jpg"; PG Policy Page/Archive "Duplicate share image set"; PG Card System Source Artwork unzipped2 (twin of unzipped); NR Archive/_to_delete; NR/03. The Stock/Data Labs Handover/Archive/_to_delete (126 MB zip leftovers); NR Workbook Cover Images master template .zip beside its folder; NR 99/reading/pending_S446 copy of the Ten Course Sentences note; NR Built Workbooks sheet__*.pdf (30) duplicated in 99/old_sheets_s470/built; PG Knowledge Hub "All Pages in General" 7 screenshots duplicated in Bottom Page Options Block.
C5. Empty folders: PROJ/0002 Educational Publishing System (retired name); T/achology-s566; PG Free Coaching Page, Presuppositions Page, Article Page/Archive/12 Images for Karen's Articles, Our People Page/Page Images/Achology People, the three Search Results "page 2"; NR's 27 (vault Blueprint 04 Machine, 06 Templates, 07 Rulings; Newsroom 13 Requests, 14 Batches; others listed in the audit); PROJ/0003/99. Archive.

## D. Every file a home (Chat moves; you correct any path a script reads)

D1. PROJ/04. The Achology Newsroom (stray, holds 99 Working Papers/idea_list_S457) merged into NR/99 Working Papers/idea_list_S457, then removed.
D2. P1/03. Achology Website Pages (stray second copy): the Certification NEXT_SESSION_PLAN note into PG Certification Page; its three images compared with the real copies, current ones kept in the page's Page Images, the folder removed.
D3. P1/03. Notes for Claude Chat (from Claude Code): one stub saying the channel moved. Remove, with ROOT/.gitignore's line, unless your hooks still need the guard.
D4. P1/99. scratch_S425: confirm the stances_S434 HTML was carried into the vault; then archive into NR/Archive.
D5. ROOT loose files: "Coaching Theme Project Plan.html" and "Our Websites - Where Everything Lives.md" into PROJ/0006 (renamed "0006. Kain Ramsay and Member Websites"); LAUNCH_ROAD_S566.html into P1/02 Launch Papers.
D6. PG loose page-root images (22) into each page's Page Images, renamed for what they show ($1,137.00.png, "Codex Image ..." and "Screenshot ..." names replaced). Video Testimonials Page 14 "889....md" Vimeo transcripts into 05 Spreadsheets/Video Testimonials Transcripts, named by person.
D7. PG _captures_S107 (260 PNG, 199 MB), ARTEFACT__..._Rendered_S079 folders, Upload These 168, Member Photos/baked: into each page's Archive, or deleted where a built page now carries them (your call per folder).
D8. PG gate-printouts-S### (22 folders, about 190 files): one Archive/gate-printouts per page.
D9. P1/02 Project Delivery System: the fourteen dated launch papers at its root and the eight small dated folders into "Launch Papers November 2026"; the six Aug to Oct papers (MAP S302, PLAN S413, PROPOSAL S353, READY_TO_RUN S291, RULEBOOK S302, SPEC S274) into Archive (Concluded Session Papers) unless you say one is live; Project Papers' two 2024 files into P1/08; the Publications PRD and plan under one "Achology Publications" folder; the four stray JPGs in Pricing Family Review into its own images folder; one of the two "Sign This Help Answer" pages archived.
D10. Handover folder: Session 220 to 487 handovers into its Archive, leaving 488 and 489 at the top; finished topic handovers (S460, S465, S512, S515, S417 board cleanup, 11 Nov publishing questions) into Archive; the duplicate "Session 421 Plan" removed; "Handover, Course Pipeline Harness ... 20 November 2026.md" renamed HANDOVER__Course_Pipeline_Harness_20_November_2026.md.
D11. DSRD folder: a DSRD 2/Archive made and its three backups moved in; the DSRD 9 backup in Archive (Superseded Specifications) moved to DSRD 9/Archive.
D12. P1/05: Help_Article_Focus_Keywords_Before_S084.tsv into Help + FAQ Data/Archive; the two Search Console zips beside their folders deleted; the SOMAP Documents duplicated in PROJ/0004 kept in one home (you say which one your scripts read).
D13. P1/08: Etsy Packs added to its note; loose screenshots in Code of Ethics, Code of Conduct and Prospectus into an Archive in each; "Achology Events copy.docx" deleted; "The Achology CPD Handbook 2026:27" renamed "2026-27" if no script names it.
D14. NR Built Workbooks: the 1,050 loose diagram images into Built Workbooks/diagrams; webp/ renamed step_pages_webp if no script reads it; Course Journals logs and lesson JSON into logs/ and lessons/.
D15. NR 99 Working Papers: the 22 loose reading HTML pages into reading/; planning/ S452 to S453 scratch into planning/S452-S453.
D16. NR Stock: the 288 LANE_C__CHECK__ files out of Content Records into a _checks folder (if the gate allows), hub-guide-retired into Content Records Archive, the loose COURSE_001 tracking note into Course Pipeline.
D17. NR vault: the Lexicon CSVs (12 MB) into the Stock if nothing reads them from the vault; the one unlisted 06 Shapes note added to its index; 21 notes given a status line.

## E. Your own ground (you do, after we agree)

E1. T/achology-branch-g-gate-tmp (275 MB, orphaned worktree): git worktree remove.
E2. T/achology-factory (809 MB, 0.708.351): keep or rebuild fresh; your S407 tooling names it.
E3. T root strays: CLAUDE_CODE_AUDIT_REPORT.md into P1/02 Archive; the S515 .sql and .tsv rollback files into P1/05 Archive.
E4. T/achology/previews (1.52 GB, 364 entries, README says 2): previews of built pages removed or archived outside the theme; quote-cards 316 MB, _sweep_sitting 213 MB, booknotes-touches-s178 frames (1,320 " 2" jpgs) first. .gitignore widened (pycache, logs, .php-cache, " 2" files).
E5. NR/02. The Machine/vault_gate/briefs (3.68 GB, 35,282 files, 245 of 256 batches older than ten days): keep what the gate verifies, archive the renders; remove vault_gate/vault_gate/ and briefs/briefs/ strays.
E6. NR api_worker/runs (138 folders, 235 MB): archive, keep COST_LEDGER.
E7. NR Built Workbooks: 4,715 numbered page re-renders (1.24 GB): newest kept under the plain name.
E8. NR 99/pack_sources_S434 and Machine/pack_kits (replaced S447): archive once api_worker's fallback no longer reads them.
E9. P1/02/06. Enforcement Gates: Check Sheets, sheet_records (126), check_sheets.py, check_sheet_source.py, harness_acceptance.py into Retired/; the two Before folders into Backups/; README rewritten.
E10. P1/07 videos: for courses already graded (001 to 004, 009, 010, 011, 013, 014), cut.mp4, cut.sound.wav, cut graded, cut picture graded, colour clips and the "before" folders (about 64 GB in all) to an archive drive on Kain's yes; the 001 Diploma pre-remaster folder (6.3 GB); Course Promo Samples' duplicate 001 folder, segments, "v1 previous passage" folders, _checks frames and batch logs; Video Production Team Footage Inventory stills, Tool Tests pictures and _tools/from_21_Nov_session. Keep _takes, luts, the signed records and transcripts. Cuts for ungraded courses stay until graded.
E11. P1/99. OBSOLETE (17 GB): the Biblical Teaching archive (15 GB) to a personal folder outside ROOT on Kain's yes; the Rebellion PDF duplicate of PROJ/0008 deleted; the rest archived where you judge.
E12. Zips beside their own folders in PG (about 1.9 GB): confirm which side is the master; remove the other.
E13. ROOT/AGENTS.md and .codex: a version behind CLAUDE.md. Retire or regenerate (Kain is asked whether Codex is still used only if you cannot tell).
E14. ROOT/.gitignore and README: the retired folder names and the channel line corrected.

## F. Notes made true (you generate, Chat words)

F1. folder_map.py run over every folder after the moves; the notes it does not own rewritten: NR 99 Working Papers (21 of 22 folders unnamed), NR Archive, Machine, Stock, Built Workbooks, T, T/achology README (listen.js, next phase), previews README, PG (35 pages, now 45), Component Design 000__THE_FOUR_CHROME_COMPONENTS (history), videos (says no videos kept here), Enforcement Gates (three scripts), handover README, DSRD README map, 05, 06 (249 vs 250 MP3s), 08, P1 project map.
F2. New 000__WHAT_IS_IN_HERE notes for PROJ/0003, 0004, 0005, 0007; retired names out of 0009, 0010, 0011, DATA_LABS_MANIFEST and THE_PUBLISH_READY_PIPELINE.
F3. Kain's three decisions (video archive drive, Biblical archive out, 0005 renamed The Wiser People Project) are put to him by Chat; Chat sends you his answers.

## G. Order

B first (the check gives the baseline), then C and D by Chat with your corrections, then E by you, then F, then the check reads zero and Chat shows Kain the before and after.

*No em or en dashes in this file.*
