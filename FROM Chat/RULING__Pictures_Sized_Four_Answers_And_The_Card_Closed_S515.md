**For Code, theme session S515 or the next theme session, with one line for the factory session. What this needs from you:** act on the four answers below. Section 1 waits on one yes or no from Kain, which the theme session puts to him; sections 2 and 4 are theme work you may start now; section 3 is a gate mend for the factory. Chat, side session opened by Code's theme session S515, 12 November 2026. It answers TO Chat/REPORT__Pictures_Sized_For_Every_Screen_Across_The_Theme_S515.
This session asks Kain nothing. The one decision that is his is written in section 1 as a finished yes or no question for the theme session to put to him.
Model: Opus 5.5 for the theme session, Sonnet for the factory line. Effort: medium.
Done when: each section's done line below is met and named in one DONE in TO Chat.

DOCUMENT TYPE: ruling. Not a page spec. Nothing a reader sees changes.

# RULING: pictures sized for every screen, four answers and the card closed

## 1. The other 128 uploads ending "-v2". Theme session. Chat agrees; it waits on Kain's yes.

**Chat agrees, as one batch, by the five commands you used on the two.** DSRD 7 section 12.3 reads "No dates, no version numbers, no export suffixes", and "-v2" is a version number. The rename is right before launch, while no visitor and no search engine holds any of these addresses.

**What Chat checked first.** No content record in The Stock names a "-v2" picture, and no picture file in The Stock ends "-v2" (read today, outside its Archive). So the build site is out of step with its records, as the two were, and renaming brings it into step. A re-import will not bring an old name back.

**Why it still goes to Kain.** The Shared Rules section 8 says a change that makes a familiar address stop working "goes to Chat first, is agreed by Chat, and is validated by Kain before anything is touched." These are 128 addresses. Put this to him once, in plain words, with nothing else in the same turn:

> 128 pictures on the build site have "v2" at the end of their file names, which the design standard does not allow. I recommend renaming them all now, before launch, because nothing outside the site uses these names and no page will look any different. Shall Code rename them?

**On his yes, the batch, in this order:**

1. List all 128 with the posts that use each, and read every database row, the theme, The Stock and the factory's import tools for each old name. If anything outside the build site's own media rows names an old file, stop and send the list to Chat before any move.
2. For each file: move it to the clean name, point `_wp_attached_file` at it, rebuild its sizes with `wp media regenerate`, remove the old copies. Where a clean name is already taken by another upload, stop on that file and list it; never overwrite.
3. Search and replace the old addresses in post bodies and post meta, if step 1 found any.
4. Read back: no row names an old file, and every clean address answers 200 at its full size and at each of its sizes. Clear the page cache.
5. Render proof as in your report's section 5 on one page of each kind that carries a renamed picture, at 1440, 768 and 390.

**If he says no,** nothing is touched and the 128 stay as they are; send his words to Chat.

**Done when:** his answer is in the DONE in his words, and, on a yes, the five steps' read-back and proof are in it with the count renamed.

The Backlog: Chat line from S438 on three Newsroom pictures ending "v2" (kind-without-being-a-pushover, trust-in-the-workplace, how-irresponsibility-leads-to-personal-disempowerment) closes with this batch: The Stock is already clean, so only the build site's copies are left, and they are among the 128.

## 2. The Help hero pictures. Theme session. Yes, before launch.

**Make the uncropped copies.** DSRD 7 section 12.3 reads "A single fixed-width file is a defect." The reason the Help hero has no srcset is sound, since WordPress's own copies crop the printed name, so the answer is copies of our own, not WordPress's.

1. Make 200 and 300 wide WebP copies of each Help hero picture, scaled whole from the 480 file, never cropped, with tools/make_picture_derivatives.py and its table.
2. Give the Help hero a srcset of 200, 300 and 480 and a size list measured at the widths it is drawn (300 on a computer, 96 on a phone, and the tablet width you measure).
3. If a master wider than 480 exists for these pictures, make a 600 copy too, because a sharp computer screen draws 300 at 600. If none exists, 480 stays the top and you name that in the DONE.
4. Render proof at 1440, 768 and 390 on two Help pages: the printed name shows whole at every width.

**Done when:** every Help hero carries the srcset, the proof shows no name cut and no visible change, and the bytes before and after are in the DONE.

## 3. The profile avatar's alt. Factory session. The alt stays; the gate's reading is mended.

**The alt stays "Kain Ramsay", and the same holds for every person's portrait.** DSRD 7 section 12.3 says a picture carrying information takes alt text describing the information. A portrait's information is whose face it is, so its alt is the person's name. Every portrait in the theme already does this (the profile avatar, the people cards). Section 12.3 also says a file name names its subject, so a well named portrait and its alt will always read the same words. The rule "Alt text is never the filename" is there to catch an alt left as whatever the editor auto-filled, and this is not that.

**So it is a mend to the check's reading, not an exception,** as Chat ruled for the pricing page's supporting lines at S503. No words change, and no page record carries an exception for it.

**The mend, in page_gate's image-alt-wording row:** an alt that reads the same words as its file name still passes when those words are also a person's name printed on the same page, in a heading or in the name line beside the picture. Anything else that matches its file name still fails.

**Proof cases, red first:**

1. The profile avatar kain-ramsay.webp, alt "Kain Ramsay", on a page whose heading is Kain Ramsay: passes.
2. A people card portrait whose alt matches its file name and the card's printed name: passes.
3. A course picture course-hero-011.webp with alt "course hero 011": fails.
4. A portrait kain-ramsay.webp with alt "Kain Ramsay" on a page that prints no such name: fails.

**One more factory line, from your report's section 7:** page_gate matches the profile page /about/instructors/kain-ramsay/ to the Kain Ramsay author article's record by its last slug. Make it match a page to its record by the whole address. Done when the profile page's run resolves to the profile page's own record, or prints that it has none, with a test.

**Done when:** the four cases pass red then green, the profile page's image-alt-wording row reads PASS at every width, and the record match is mended with its test.

## 4. The Image and icon optimisation card. It closes from your report.

**Chat closes Backlog: Code line 12 from your report today.** COMMISSION__Close_The_Image_And_Icon_Optimisation_Card_S392 asked for the theme version, the count of pictures now asking for the size they draw, and each one left with its reason, "an exception, not an open line". Your report gives all three. The three template changes in section 3 are already one line on the theme queue for the sessions that hold those templates, so they are not this card's.

**One leftover needs its own line first, theme session.** Three decorative backgrounds are over DSRD 7 section 12.3's 40 KB budget, and that section reads "A file over its budget does not ship": the Aristotle watermark behind the Manifesto, Ethics and Character pages (69 KB), course 001's artwork behind the About, Testimonials and Reviews gateway tile (66 KB), and the bookshelf behind the book note and workbook heroes (58 KB). Add one line to the theme queue for the stylesheet sweep: each recompressed or given a smaller copy under 40 KB, with its drawn size measured and an image-set line. The closing tiles (27 KB) and the bubble mark (24 KB) are inside the budget; wiring the bubble mark's 176 copy rides on the same line.

**Done when:** that line is on the theme queue, named in the DONE.

## 5. Calls Chat made that Kain may overturn

1. The 128 renames are a yes from Chat, held only for his validation under section 8.
2. A portrait's alt is the person's name, and the gate learns to read it so, rather than every portrait carrying a longer alt.
3. The Help hero copies are made before launch.
4. The card closes now, with the leftovers as lines on the theme queue.

OWED BACK: one DONE naming this file, with Kain's answer to section 1 in his own words, and the done line of each section met.

*No em or en dashes in this file; checked before writing.*
