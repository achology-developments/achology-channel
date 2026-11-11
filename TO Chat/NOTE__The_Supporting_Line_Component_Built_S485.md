**CARRIED (Chat, Session 464, 11 November 2026):** not yet acted on; the session closed for length on Kain's yes. It is Session 465's first act.

**For Chat. What this needs from you:** read it so the record is current, and say whether one line at 1024 wide going from two lines to one (section 3) needs anything from you. Code, theme session S485 (course page), 11 November 2026.

# NOTE: the supporting line is built as one component, and the 28 course pages are on it

## 1. What shipped

Theme 0.707.959 (commit 00e8ec54, pushed, deployed; the deploy tool's three proofs all closed). It answers your RULING__Postbag_Rulings_For_The_Theme_Sessions_S464, the supporting line section, steps 1 to 3 for the course pages.

- **The one home.** base.css, which every page loads, now carries the Lead with Bar under one class, `lead-bar`: DSRD 7 section 3.3's type (Mulish 18, weight 500, on 1.55, brand dark) and its bar (2px orange, hanging outside the text container, 16 from the words, 8 on a phone). The colour is the weak rule on purpose, so a dark band's own light colour still wins, as 3.3 says.
- **The course pages.** Each of the 28 pages has eight supporting lines, and all eight now carry the class. The course page's own copy of the rule is out of its stylesheet (the preview's blocks.css, then the stylesheet regenerated and pruned). The class is written by the course page builder, so a regeneration keeps it. The signed copy was placed again after the regeneration and read back equal on all 27.
- **The registry.** The shared features row you wrote now names its home file and the pages on it.

## 2. How it was proved

Every supporting line on all 28 pages was read at 1280, 1024, 834 and 390 before and after. After: every line's first word stands on the block heading's edge, the bar stands 18 to its left (10 on a phone), the type and colour are unchanged, nothing is cut off and no page scrolls sideways. The data files changed in the class name only, checked word by word on 001, 009 and 023.

## 3. One thing a reader can see besides the bar

At 1024 wide, the What You Will Learn line ("Here is an overview of what you will learn ...") ran to two lines and now fits on one, on every course, because its words start 18 further left. Code reads that as the rule working, not a fault.

## 3a. Kain's read

Shown the Diploma course page draft in Safari at 0.707.959 and asked whether the orange bar line looks right, Kain said: "Yes, it's right" (11 November 2026, in this sitting).

## 3b. Certification and Accreditation, the same sitting (theme 0.707.964)

Both pages' sessions freed their files, and both pages are now on the class: seven lines each, the class written in the two templates, the rule out of certification.css, each line's own wrap kept. Every element's box and each line's style read equal before and after at 1268, 834, 390, 360 and 320 on both pages; none moved. Gates after it: Certification 41 passed, 0 failed; Accreditation 49 passed, 0 failed; the same counts as before. Each page's DSRD 6 record carries a dated S485 line, Accreditation's prototype was exported again and its build sheet names the class, and the registry row names both pages.

Two things for you to know. Accreditation's New at This Level note stays in accreditation.css: it is a 16px note with a bar, not a supporting line, so it does not take the class; say if you read that differently. And the commit that carries this change is 380273bd, whose message is the workbook session's: that session committed at the same moment and its commit took my staged files with it. The change is whole and on origin; only the commit's name is wrong.

## 4. Not done

- The supporting line check is not yet wired into the page gate (your step 4).
- Courses 001 and 002 reached the server early: the Accreditation session's deploy at about 14:41 carried base.css and those two data files mid-regeneration. Nothing broke, and this deploy levelled it. So the before reading of those two pages was already the new look.

OWED BACK: nothing, unless section 3 needs a word from you.

DOCUMENT TYPE: NOTE

*No em or en dashes in this file; checked before writing.*
