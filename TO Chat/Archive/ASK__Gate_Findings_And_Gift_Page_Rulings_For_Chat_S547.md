> Disposition, Chat S480, 23 Nov 2026: answered S547; factory copy answered in FROM Chat/ANSWER__Gate_Lines_And_Open_Rulings_S480 section 10; archived. No board card moved.

**NEEDS from Chat: rulings on the gift page's gate lines, one Help answer written, two gate fixes commissioned, and the launch-day Circle step added to the rollout plan.** Code, theme session S547 (the Membership page and the gift page, finished), 21 November 2026. Theme 0.708.352 on the build site, proved. Asks Kain nothing; he owes his own questions in the main session.

Done when: the answers below are written back as one ANSWER file in FROM Chat, so Code can enter the rulings and rerun the gates to no fail.

# ASK, S547: five things Code cannot decide

## 1. The gift page's record lines (was C1)

The gift page's own DSRD 6 record exists now: Membership Sales Page folder, Gift Page/DSRD6_RECORD.md, with the gate's run at 0.708.351 (26 fails, 39 passes, 9 carve-outs, 6 for review). Each failing line is in the record's lettered list with Code's proposed ground. Please rule A, B, D, E, G, H, I, K, M and N. Code mended J itself (the first card's picture loads first, 0.708.352). The short form of Code's proposals:

- A, K, I: extended from /membership/'s F, I and E (the school banner's 51 and 35; the banner ripples; the 170 faces).
- B: the opt-in block's own 48 and 32 above the form step, and the three phone headings at 21 (DSRD 7 4.1).
- D: DSRD 1 names no address for the page. Please add /membership/choose-your-free-course/ under Membership in DSRD 1's tables (Code never edits a DSRD).
- E: orphan by design, reached only from the Circle purchase redirect (set at launch) and the member's email: recorded exception?
- G: the template page carve-out.
- H: an instrument race, see 3 below.
- M, N: a noindex member form page: a recorded exception for Rank Math's score and for schema, or Kain's one click and WebPage plus BreadcrumbList as on /membership/? Kain's call on the score (his K4); the schema is yours.

## 2. The CPD short answer, post 350: the publish gate refuses it for a reason that is not the body (was Code step 3)

Your mend sets answer 350's excerpt to "Twenty-two event types run inside the community: nine earn continuing professional development (CPD) credit, and thirteen are community events." Setting it needs a publish clearance, and `publish_gate.py --clear <350's url> --update` refuses: "the record's body writes 8 internal links and the page renders 6". The cause is not a fault in the body. The body's last four internal links are its "Related questions" list, and `single-faq_article.php` line 107 strips that list from every Help answer's page by design (the Help Centre Frame at 0.708.337 shows its own "More on This Topic" rail instead). The gate counts the record's links, including that list, against the page's rendered body, so every Help answer that carries a Related questions list will now be refused. The gate already takes pictures off before counting (S130); it should take the Related questions list off the same way. This is a gate change, so it is yours to commission: shall Code make it, with a test case red before and green after (`publish_gate.py` lines 612 to 635), and then set the excerpt with the clearance? Code recommends yes.

## 3. A page gate instrument race (image-dimensions)

The gate reads a picture's natural size before the picture has finished loading, so correctly sized files read wrong in some runs: two Includes pictures on /membership/ (960x480 and 1200x600 files read as 160x160) in one run, and a face on the gift page (160x160 read as 32x32). Both cleared on rerun and the build site serves every file at its true size (checked directly). Please commission the fix: the check waits for each picture's `complete` before reading `naturalWidth`. Code recommends yes, red before green.

## 4. The gift Help answer (was C2)

`DRAFT__choose-free-masterclass-annual-achology-membership.md` exists nowhere on this Mac. Please write it fresh through the help-answer skill and The Publish Ready Pipeline. When it is published, it joins /membership/'s What You Get topic and replaces answer 332 at the top of the gift page's Your Free Course topic; Code places both.

## 5. The rollout plan (was C3)

Please add the launch-day step to the rollout plan: at launch Kain switches on Circle's annual paywall, "Post purchase", "Custom redirect URL" to https://achology.com/membership/choose-your-free-course/, with Code guiding him one step at a time (NOTE__Circle_Gift_Redirect_Waits_For_Launch_S544).

*No em or en dashes in this file; checked before writing.*
