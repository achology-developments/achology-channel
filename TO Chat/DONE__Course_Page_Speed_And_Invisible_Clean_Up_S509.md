**For Chat: read the record lines named here. What this needs:** one word on section 4's two lines for Kain, which the main session (S498) puts to him; nothing else. Code, theme session S509, 12 November 2026, a side run started from the course page session S498 on Kain's "yes" to it ("what is it that you can just go and do all by yourself now in one sitting without asking me for permission").

DOCUMENT TYPE: done.

This file asks Kain nothing.

# DONE: course page speed, the dead rules, the gate's lead-bar line, and what was not run

## 1. Course pages, built and deployed, nothing a reader sees changed

**Theme 0.708.045, commit 7dadd52f, deployed from a clean copy; local, server and zip agree.**

- **course-page.css: 146 declarations out (46 whole rules, four emptied media blocks), 205,090 bytes to 201,078 (199,189 once the rules were out, plus a header note saying what was done and how it was proved).** Each one is beaten, always, by another declaration in the same file: the same elements (":root X" matches what "X" matches), the same or a wider media context, and equal or greater weight. So none could ever win, on any page, in any state. Every value that does the beating (92) is kept by Chrome and WebKit (CSS.supports). Rules a state the script sets waits on stay, since only a rule on the same elements can beat them; the review pool's late markup needs no special care for the same reason.
- **Course pages no longer load people.css (56 KB, one of the files that held first paint).** Not one of its 124 rules can match an element of a built course page, or any class or id a script on the page could add. One line in functions.php, section 6i.
- **Proof, computed style:** on all 28 published pages, each loaded once, at 1280, 1024, 834 and 390, resting, mid-scroll and after clicking each control the page script answers (about 40 states a page, 1,150 in all), every element's whole computed style and its ::before and ::after read the same with the old sheet and with the new one swapped in place. Chrome parsed all 1,226 rules of the new file. A planted 1 pixel margin was caught. One state on 022 at 834 had a late card arrive mid-read; run again, it reads the same. people.css switched off: the same on 001, 012 and 027, 115 states.
- **Proof, pictures:** WebKit, whole pages of 001, 012, 018 and 028 at 1280, 834 and 390, motion off, old and new, twice. Equal everywhere except the film stills at 834 on 001 and 012 (largest step 28 of 255). An old-against-old run in the same order shows the same faint difference, so those stills move between loads by themselves. 012 at 1280 differed once in its first run and matched in the second and in the control.
- css_gate passes the file. The record's printouts: gate-printouts-S509 beside the course page record (proof_28_pages_s509.txt, pictures_s509.txt, gate_001_s509.txt).

## 2. The gate on 001, and Lighthouse

- **page_gate on course 001: 36 passed, 1 failed (the record itself), 8 for review, 1 not built yet, 35 carved out.** It was 35 passed, 3 failed at S502.
- **Lighthouse 13.6.0, course 001, signed out, phone, slow 4G, twice: 52 then 84** (S502: 73 and 80). First paint 2.2 and 2.1 s, largest paint 4.2 and 4.1 s, total blocking 2,559 then 100 ms, layout shift 0.010 and 0.012. The first run's blocking time is the machine: its load stood at 5.5 and 7.0 on six cores with other sessions' browsers running. Render-blocking style now costs about 0.9 s (was about 1.1); unused style 136 KB (was 153). Reports in the session's scratch folder only. Written into chapter 9 of the course page record.

## 3. Not built, and why

- **course-page.css still holds first paint.** The theme's own way of not blocking is to print a sheet at the foot of the page (shared-parts.php, achology_enqueue_component_style). Its own note says it is for blocks that close a page and that anything above the fold stays in the head. This sheet styles the hero's refinements, the section bar and the buy bar's hidden state, so printed at the foot the buy bar would show for a moment on first paint. Splitting the sheet in two would still flash on tall screens. That is a change a reader could see, so it is not built.
- **The other site-wide sheets on a course page are almost all unused at load:** components.css (1 KB used of 119), cards.css (none of 109), help.css (none of 106), policies.css (0.1 of 71). Each still has rules that could match something the page's scripts build, or a shared block, so none can simply go. That is site-wide loading, a sweep across page types, and outside this run.

## 4. Two lines for Kain, through the main session (yes or no)

1. "Course pages could show their first picture about half a second sooner if the page's own styles loaded after the top of the page, but the buy bar would blink at the bottom for a moment as the page opens. Shall we leave it as it is?" Code recommends yes, leave it.
2. "Six of the new lesson questions run past the edge of their row on a phone, as twelve others already did. Shall the phone keep the last two words together instead of four, so none runs past?" Code recommends yes; it changes where long questions break on a phone, and has not been measured or built. (Detail in DONE__Course_Pages_354_Signed_Lesson_Questions_Placed_S509, section 3; Chat may prefer to mend the six words instead.)

## 5. Step 2 of the run: other built pages

- **Enquiries (its own sheet and script, no session holds it): already clean.** Every one of enquiries.css's 181 rules can match on the page or on markup its script builds, and its four animations all play. Nothing to take out, so no commit and no deploy.
- **Not run, each for a reason:** Certification, Accreditation, the Courses page, About and the course sheets are shared with the school pages, whose session is open and building with those blocks, so a "matches nothing" reading there could break its work. Pricing, the workbook family (knowledge-hub.css, kh-band.css, workbook.css), and About, Testimonials and Reviews belong to open sessions or wait on your S466 ruling. The Knowledge Hub's tag, subject, book note and quote templates each serve hundreds of pages, so a "matches nothing" reading needs a full crawl; that is its own job. The safe collapse used on the course sheet finds at most 2 KB in any other theme sheet (kh-front.css 1.8 KB, kh-subject.css 1.7 KB), not worth a deploy each.

## 6. The theme queue

- css_gate.py passes `lead-bar` at 18 on a phone by name, and refuses 16 (your night ruling, section 2.3). Six cases in css_gate_acceptance.py, four red first, 34 of 34 green after. Theme commit 2aa6ef02, tooling only. Line struck.
- Struck with evidence, both shipped by S502 and never struck: "1 lesson" (commit 7ed3deec) and the three block-heading exceptions (commit d9046650).

## 7. The lesson questions

Done in its own file: DONE__Course_Pages_354_Signed_Lesson_Questions_Placed_S509.

OWED BACK: a word on section 4, carried by the main session to Kain.

*No em or en dashes in this file; checked before writing.*
