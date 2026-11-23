> Disposition, Chat S480, 23 Nov 2026: answered in FROM Chat/ANSWER__Gate_Lines_And_Open_Rulings_S480 section 1; archived. No board card moved.

What this needs from Chat: rule each group of /about/ gate lines below (exception on the ground named, or a page fault for Code to mend), as ANSWER__Academy_Page_Gate_Lines_S533 did for /academy/, so Code can enter them in page_gate.py and close the machine half.

**DOCUMENT TYPE:** Ask from Code (S556, Branch E, theme session), not a page spec.
**Date:** 2026-11-23

# ASK: the About page's gate lines after the signed redraw

/about/ is now the redraw Kain signed on 23 November (SHIP__About_Page_Redraw_S556), built from the Academy page's own parts: the Academy bands taking turns white and sand, the course page's section bar, the history component, the one reviews block, the questions block and the Where to Start block. The page gate still reads /about/ by the old ruled-column page's rules, so it fails lines that the Academy page carries as Chat's recorded exceptions (page_gate.py, PAGE_EXCEPTIONS for /academy/, from ANSWER__Academy_Page_Gate_Lines_S533). Code has not entered any of them: each is Chat's to rule. Run on the build site at 0.708.398; the full printout is beside the About record.

Code mended the one fault that was the page's own: the answer tabs' list items broke the tab roles for a screen reader (axe, critical); each item is now role="presentation" (0.708.398, no visible change).

## The groups, with the Academy ground each matches

1. **hairline-present**, boundaries 1, 3, 5, 6, 7 and 8 at all three widths: no hairline between bands. The grounds tell the bands apart (Academy, S533 1.1).
2. **hairline-spacing**, boundary 2 (the section bar's own edge) and boundary 4 (sand story band to the white films block, 64 / 48 / 32 below at the three widths, the Academy band's own air). Academy S533 1.1 for boundary 2; boundary 4 is the films block's own band top.
3. **header-to-content** 0 at all widths, **breadcrumb-above** 0 and **breadcrumb-below** 35 (the Cream Hero's own padding, SECTION.about-banner__hero), with **spacing-scale** "about-banner__hero padding-top 35": the signed banner's own top (Academy S533 1.2, the same 35).
4. **spacing-scale**, the rest: b1-pane margin-top 18 (the Answer Tabs pane, signed), kfp-sign__fig and kfp-sign__sub (the Where to Start block's own rules, as Academy S533 1.3), kh-section__header row-gap 12 on the phone (the same block).
5. **content-width**: article-container 1104, the page's one frame inside 48 a side (Academy S533 1.4, the same 1104).
6. **boundary-owner**: boundary 1 padding 16 declared by .snav__link (course-page.css, the section bar), boundaries 2 and 4 padding 64 declared by base.css's band rule: each is a signed component's own space.
7. **supporting-line**: gap from the lead line to the block is 32 under "Achology: What It Is, and Who It's For", "Five Aspects of the Achology Experience" and "Ten Different Ways to Experience Achology" (the Academy band's 32, wants 24); on the phone the Academy band heading is Como 21 (wants 24) for What It Is, The Achology Story, Ten Ways and the questions heading. Same component as /academy/.
8. **icon-registry**: 58 inline drawings in the signed components (the film play buttons, the reviews block's stars and arrows, the Answer Tabs' and Ten Ways' arrows, the history stops). Rule as for the school pages and /academy/, or name what should be drawn by the registry.
9. **image-responsive**: the five film stills (andy-q1, sarah-q2, bea-q4, jon-q3, peter-q5 at 460, their drawn width; the school pages carry the same exception) and course-001-540.webp, the DiMAP picture in the Ten Ways feature card.
10. **acronyms**: AI (the 2023 milestone, an open line since S295), and QR and ID, both in Chat's own line for answer 300 in the Recognition and Trust card ("Scan its QR code ... enter its Certificate ID"). Words are Chat's: rule or reword.
11. **keyword-density**: "the body is empty": the gate looks for the old page's body column, which the redraw no longer has. A gate fix (read the bands) or an exception; Code's to build once ruled.

## What Code does on the answer

Enters each ruled line in page_gate.py by name and value (so a changed value fails again), mends anything ruled a fault, reruns the gate on /about/ and closes the record's machine half.

OWED BACK: Chat's ruling on groups 1 to 11.
