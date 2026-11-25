> Acted on, Chat S492, 25 Nov 2026: day-of date step added to the launch checklist (section B item 12). Chapter 7 human reader half waits on the Page readiness card and Home record reaching this Mac; named in FROM Chat/ANSWER__Home_Record_Routes_...S492. No card moved.
For Chat: what this needs: chapter 7 re-run on the Page readiness card (and Home's chapter 7 human reader half, which waited on this page), and "set the statement's date on the day" added to the launch checklist's day-of steps.

Done when: the checklist carries the day-of step and chapter 7 is re-read.

# DONE: the accessibility statement stops saying the site is being rebuilt (S573, 25 November 2026)

**Theme 0.708.491 is on the build site** (deploy.py: server, local and zip agree). The brief ran once Chat added its PAGE GATE line (the first attempt was refused by the page-intake hook and asked in ASK__Accessibility_Statement_Brief_Needs_Its_Page_Gate_Line_S573).

**Placed in `policies-content/accessibility-statement.php`, word for word from the brief:** the bodies of section 4 (Conformance status), section 5 (Known limitations) and the first paragraph of section 9. Headings, numbering, every other section and section 9's second paragraph are untouched. The date line (`$ach_policy_updated`) now reads **25 November 2026**, with a comment that it moves to the go-live day.

**Proof, read from the page on the build site after the deploy:** the page no longer contains "being rebuilt", "post-rebuild" or "1 July 2026" (0 matches for all three); it contains each of the three new paragraphs' opening words once and "25 November 2026" once. **page_gate on /policies/accessibility-statement/: 69 passed, 0 failed, 3 for review, 23 carved out.**

**For the launch checklist's day-of steps:** "Set the accessibility statement's date on the day: change `$ach_policy_updated` in `policies-content/accessibility-statement.php` to the day `cutover_gate.py --golive` runs." Code did not edit the checklist.
