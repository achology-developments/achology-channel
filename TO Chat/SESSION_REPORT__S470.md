**For Chat. What this needs from you:** nothing beyond ASK__Accreditation_And_Certification_Publishing_Checks_S470, which carries every question this session raised.

# SESSION REPORT S470 (theme session): publishing checks on the Accreditation and Certification pages

10 November 2026. A side session started from the main theme session. Note: another theme session also shipped under the S470 number today (0.707.906, the Code of Character and Conduct page, commit d214f597); this report covers only the commits below.

## Finished, from the version control log

- **0.707.907** (theme commit b09d438b): dead code out of accreditation.css, certification.css, template-accreditation.php and shared-parts.php (the old step list, the signpost, the grey panel pair, the old question accordion and its function, the trial placing, an unused link icon rule), each deletion proved by testing every removed selector against both rendered pages at four widths with every level opened (no match); both pages measured identical after the deploy but for 1 to 2 px of rounding on Accreditation. Also: the guide drawings hidden from screen readers; srcset and right-sized copies for the badges, handbook covers and SoMAP pictures (Accreditation 692 KB to 563 KB); the intro's phone rule rewritten so css_gate reads it. Card: Accreditation page; Certification page.
- **0.707.908** (theme commit 0fd73516): the Accreditation schema's page name is the page title, "Achology Accreditation", as Certification's. Card: Accreditation page.
- **DSRD 6 records** (hand added; design folders): Accreditation's first record; Certification's brought to 0.707.908, Chat's reader lines kept as written. Every printout in each folder's gate-printouts-S470. Card: both pages.
- **Fold-back** (hand added): PROTOTYPE__Accreditation_Page_S470_APPROVED.html (the page exported at 0.707.907, stylesheets inlined) and BUILD_SHEET__Accreditation_Page.md in the Accreditation Page folder; the S364 prototype removed as superseded (in git history); README updated. Card: Accreditation page.
- **One Change Viewer round** for Kain, built and measured, not yet shown: previews/accreditation-s467/round-sp-1.js (switch ps), the phone and tablet spacing as Certification's. Card: Accreditation page.

- **0.707.909** (theme commit c6b7fda9): Accreditation's spaces step down below a computer as Certification's (48 tablet, 32 phone), Kain's go-ahead; RULING__Accreditation_Phone_And_Tablet_Spacing_As_Certification_S470. Card: Accreditation page.
- **0.707.911** (theme commit 5f14e442): Chat's S470 answer placed: Accreditation's search title and description (set over WP-CLI, Kain's yes), schema description, six question summaries; Certification's three word changes (Kain's yes), no picture touched. DONE__Accreditation_And_Certification_Chats_Answer_Placed_S470. Card: both pages.
- **0.707.913** (theme commit 546dc02c): the two contrast fixes on Kain's "Yes, both" (round-ct-1.js, commit 410711ac): the banner's SoMAP link on both pages and the member video card names take the AA orange. Card: both pages. Note: this deploy also uploaded the course page session's uncommitted new files (course-page.js, data/course-page/, three tools), which nothing on the site uses yet; that session is archived, so the course page owner commits them.

## Not finished

- Accreditation's Rank Math score is 88 against 90: whether Kain's Certification exception covers it waits on Chat (DONE S470 section 1).
- Certification step 4's shorter wording: waits on Chat (DONE S470 section 3).
- The six Help answers' own excerpts: wait on a factory session.

## The other S470 theme session: the Code of Character and Conduct page

Added by that session, which first overwrote this file by mistake and restored it word for word from the channel's history before adding this section.

- DONE: the page built as the Code of Ethics page's sister, on the build site at 0.707.906, its training line fix riding 0.707.908 (DONE__Code_Of_Character_And_Conduct_Page_S470). Card: Code of Character and Conduct page.
- DONE: the Code of Ethics text link and companion bar re-pointed to the new page; the handbook PDF placed (200); Rank Math fields set over WP-CLI, score 87 read, exception waits on Kain.
- WAITS ON Chat: the words read, a DSRD 1 address row, the record's human lines.
- WAITS ON the factory session: /about-us/achology-code-of-ethics/ still redirects to the home page.
- NEXT (Kain's yes): one polish round for the four founder pages together.

OWED BACK: nothing, to TO Chat.

*No em or en dashes in this file; checked before writing.*
