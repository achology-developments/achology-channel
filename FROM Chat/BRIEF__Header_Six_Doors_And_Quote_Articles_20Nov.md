CODE DISPOSITION, S544: DONE. Kain signed direction B ("Yes, B"); built and deployed at 0.708.343 and 0.708.345 with Quote Articles renamed, measured at every width and state; answered in TO Chat/SHIP__Header_Mega_Menu_S544.md and RULING__Header_Mega_Menu_Direction_B_S544.md.
NEEDS: Code to design the site's mega menu from scratch to one consistent standard, put it to Kain on a rendered mock-up, then build the signed header, the phone menu and the Quote Articles name change, and send one DONE with the proof. Rewritten at the close of Chat's Session 478, replacing this file's earlier text, which built panels Kain then withdrew.

Done when: Kain has signed one mega menu design whose four panels are the same width and the same height on a rendered mock-up, the build site's header and phone menu match it and DSRD 8 section 18.22, no reader-facing "Wise Quotes" or "Ultimate Pass" is left in the theme, header.css passes its gate, and the DONE carries the built header read at 1280, 1024, 960 and 375 against the signed mock-up.

# BRIEF: redesign the mega menu from scratch, then build the header (Chat, Session 478, 20 November 2026)

**For:** Code, a theme session of its own, after the footer brief or beside it (the footer is footer.php and footer.css; this is header.php and header.css). **From:** Chat. **Card:** Header and Mega Menu Review.

## Why this comes to you

Chat spent Session 478 on the menu and failed. It changed one panel at a time in answer to Kain's comments, and ended with three panels of three different shapes and sizes. Kain closed the session and gave the work to you. In his words: "this is a mega menu. We just need a mega menu strategized and then built, or designed and built ... It just needs to be consistent. Each menu just needs to be the same size ... We don't have to use the current components ... it needs thought through and fucking redesigned from scratch ... We can use some of the components, but we don't have to." He wants a collaborator who puts in full design effort and proposes. He does not want to be asked how to think.

## What is already settled (do not reopen)

All of this is in DSRD 8 section 18.22. Read it first.

1. **The six doors,** in this order: Academy (/academy/), Membership (/membership/), Knowledge Hub (/learn/), Pricing (/pricing/), About (/about/), Help (/help/). Then search and Sign In. Kain: "yes". The six words never wrap from 960 up.
2. **The phone menu,** Kain's own list, with Chat's two fixes, which he accepted: "yes".
   - Academy: The Academy, Online Courses, Access All Areas Pass, Certification, Accreditation.
   - Membership: Membership, Live Events, Code of Ethics.
   - Knowledge Hub: Knowledge Hub Home, Latest Articles, Quote Articles, Book Notes, Workbooks, Hub Search (the Knowledge Hub search; confirm its address).
   - Pricing: one link.
   - About: About Achology, Student Reviews, Testimonial Videos, The Manifesto.
   - Help: Help Centre (/help/), Enquiries (/enquiries/).
3. **Learn for Free is out** of the whole header. It joined the free community tier, which is ending (Kain: "Yeah, take it out").
4. **Quote Articles is the one name** for that kind of page (Kain: "yes"). Change these reader-facing words, and leave code comments as history:
   - header.php's card and phone link.
   - learn-listing.php line 128: "Achology's wise quotes offer" becomes "Achology's quote articles offer". These are Kain's S175 words; only the name changes.
   - shared-parts.php line 1559: "Browse Quote Articles and Enlightening Articles".
   - people-setup.php line 198: "Content Lead for Quote Articles".
   - **The "Achology Wise Quotes" logo on each quote picture stays** (Kain: "Yes, keep it"). Do not touch it.
5. **Ultimate Pass becomes Access All Areas Pass** wherever the header shows it, so the product has one name.

## What you design: the computer panels, from scratch

**The one requirement:** the four panels (Academy, Membership, Knowledge Hub, About) are one consistent design. Each has the same width, the same height, the same grid, the same card and the same place for an offer. A panel never looks empty, and never carries filler to reach a count.

**The content** starts from Kain's phone list for each door, so the computer and the phone agree. You may propose adding to a computer panel, for example the seven schools under Academy, where it helps a reader and the standard still holds. Say why in one line. The links must be real pages on the build site.

**How to put it to Kain.** This is what failed at Chat's seat, so follow it closely.
1. Write the panel standard first (width, height, grid, card, offer place) and apply it to all four panels before he sees anything.
2. Design three whole directions from scratch. Each shows all four panels open, side by side on one page, at computer width, with the phone menu beside them. Render them in the one Change Viewer, or as one mock-up page, built only from DSRD 7's tokens.
3. Check each direction yourself before he sees it:
   - every panel the same width and height;
   - no card name wrapping;
   - nothing sideways at 960, 1024, 1280 and 1440;
   - focus visible;
   - tap targets of at least 24 on the phone;
   - the six words on one line.
4. Show him one thing at a time. Give one recommendation and its reason, in a few short sentences, and end on one yes or no question. Agree words in words, as a numbered list when he asks; he was angry at being given a page of decisions at once. Never claim it is right until you have measured it.
5. On his signature, write the standard into DSRD 8 section 18.22 in place of the withdrawal note, and build.

**Use the visual-design-craft and page-design-brief skills.**

## Research to start from (gathered by Chat's helper, Session 478)

- **Nielsen Norman Group, mega menus.** Show every option in labelled groups, with no scrolling, and each option once. Open after about half a second of rest, and close about half a second after the pointer leaves. Each top item also links to a plain page listing its options. (nngroup.com/articles/mega-menus-work-well)
- **Baymard.** About 10 links in a list at most. Group headings are links.
- **Nielsen Norman Group, menu design.** Open on click as well as hover. Use familiar labels. Show where the reader is.
- **Sites in the field.** Beck Institute and ICF give certification its own named place. Mindvalley and positivepsychology.com give membership its own door. iPEC and ICF keep utilities (log in, search) apart from the main items, with one button for the main action.

## The starting point and what not to copy

- **The bar and phone list:** MOCKUP__Header_Six_Doors_20Nov.html in the Header + Footer folder (Component Design Prototypes). Use it for the bar and the phone list only. Its computer panels are the withdrawn ones; do not build them.
- **The header as served** at 0.708.266 is header_as_served_0.708.266.html in the same folder. build_header_six_doors_20Nov.py beside it shows how Chat assembled the mock-up from the theme's own files.
- **Chat's audit of the current header:**
  - Academy, Events and Membership had no place in the menu.
  - The phone menu lacked the pass, /learn/ and the subject pages.
  - Five addresses appeared twice.
  - The pass had two names.
  - /academy/schools/ is still written in shared-parts.php, 404.php, pricing-parts.php, commerce-cards.php and kh-front-setup.php. Point those at /academy/ while you are in the theme.

## Fold in

FROM Chat/ANSWER__Tray_Points_Settled_S478, items 1 and 2: the five header.css spaces annotated to DSRD 8 s18.21 (they may change with the redesign, so annotate what you keep), and the dead border word at line 470.

## Checks before the DONE

- css_gate on header.css passes.
- Every address in the header answers 200 on the build site.
- At 375, the phone menu's lists open and close, focus is trapped, and every target is at least 24.
- At 1280, the four panels measure the same width and height; give the numbers. Keyboard: every panel opens on focus and closes on Escape.
- The built header is shown to Kain in a new Safari tab, never over a tab he has open, for his last look.

*No em or en dashes in this file; checked before writing.*
