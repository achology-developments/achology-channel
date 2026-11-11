> CHAT DISPOSITION, S465: answered in RULING__Evening_Postbag_Course_Workbook_Pricing_School_And_Redirects_S465 in FROM Chat; Kain's rulings written home where named there.

**For Chat. What this needs from you:** write Kain's ruling home, and rule on the three questions in section 4. Code, theme session S494, 11 November 2026.

**DOCUMENT TYPE:** ruling. Not a page spec.

# RULING: the workbook page's Browse More line takes the Lead with Bar, and Kain's word on the side panel

## 1. Kain's words

Kain, on the built Karpman workbook page, 11 November 2026: "I have literally interacted with you in multiple sessions now, talking about a component for titles and subtitles that have like an orange hairline outside of the container. And I'm looking at the Browse More Achology Workbooks block that should apply to. And it hasn't been applied. It hasn't you haven't applied it to that. Any reason why?"

## 2. The reason, as told to him

The component was built at S485 (base.css, class lead-bar) and switched on for the course pages, Certification and Accreditation. Every other page was left waiting for a sweep brief. Browse More's line was still the shared block header's small grey line (`kh-section__subtext`, 14, soft grey, 2 under its heading).

## 3. Built (theme 0.707.988, commit 80f5515d, deployed)

- The line under Browse More Achology Workbooks carries class `lead-bar`: Mulish 18, weight 500, 1.55, brand dark, the 2px orange edge outside the column, 16 under its heading (one rule in workbook.css lifts the header's 2 to 16 for this block).
- Measured on the build site at 1280, 1024, 834 and 390: the words stand on the heading's edge (148, 77 at 834, 20 on a phone), the bar outside it (130, 59, 10), 16 under the heading at every width, no sideways scroll. One line at 1280, two at 1024 and 834, three on a phone.
- The space under the line is the block header's own 32, where DSRD 7 section 3.3 says 24. Left as it is: the stack of covers beside the list is placed against that space.
- css_gate passes workbook.css. The page's DSRD 6 record has a line for the change.

## 4. For your ruling

1. **The same block on the other pages.** The read-next block under quote pages and book notes, and every other `kh-section__subtext` line across the Knowledge Hub and Help, still shows the small grey line. Kain's S481 ruling says the bar is for every page. Is a sweep brief coming, and does it cover this small grey line everywhere or only supporting lines under block headings?
2. **Centred blocks.** On this page How This Workbook Helps You Learn and Ready to Further Your Learning have centred headings with a centred line. A bar hanging to the left of centred words has no signed look. Do centred blocks keep their line as it is?
3. **The 32 under the line** against section 3.3's 24, on this block.

## 5. Kain on the side panel, not built, for the record

Kain, same message, on the right-hand column (cover, name, email, tick box, button): "it just doesn't look designed. It doesn't look polished. It looks scrappy, especially with the tick box ... this is the last part of this page. We need to kind of really fine-tune". Code agreed and offered him four whole designs of the column in the Change Viewer, as the hero was done at S486. His answer is awaited.

OWED BACK: the ruling written home in DSRD 7 section 3.3 or the workbook page spec, and your answers to section 4.

*No em or en dashes in this file; checked before writing.*
