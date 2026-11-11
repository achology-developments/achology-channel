> CHAT DISPOSITION, S465 night postbag (11 November 2026): DONE. Rulings 10 to 14 are written into DSRD 2 section 2.5, items 17 to 19, DSRD 8 and the Component Registry; the four points answered in RULING__Night_Postbag_For_The_Theme_Sessions_S465.md in FROM Chat, section 4.

**For Chat. What this needs:** write Kain's rulings below into DSRD 2 section 2.5 and DSRD 8's story scroll entry, rule the four points in section 3, and know the school's story is now built from your signed words. Code, theme session S497 (the school page story block), 11 November 2026.

DOCUMENT TYPE: ruling. Not a page spec.

# RULING: the school page's story of the field is built as Kain designed it

## 1. Kain's rulings, in his words (11 November 2026)

10. **The polish: five kept, the firelight not.** "I'm going to say yes to most of your recommendations ... I love the moments rise in, the mark where you are, the moments as cards, chapters in the fire frame. I really like that. Tightened by measure, really like that. The firelight top and bottom, I'm not convinced with that ... it kind of just makes the text a little bit harder to read."
11. **The top and bottom are a pair, wider than the scroll.** "It's meant to be a scroll. So naturally, the top of the scroll and the bottom of the scroll should be technically wider than the actual scroll within itself ... the top banner just seems really crammed ... Ideally, both would be the same kind of depth, and succinct ... assigning our kind of font and spacing standards and rules, just to these two kind of blocks as well." The mark on the closing panel should not "disappear behind the top half as it scrolls up. It kind of stops at a certain point."
12. **The word to build.** Shown the pair as two switches: "Yes, build it".

13. **Links on the four course moments.** On the built block: "you haven't built in links. Links through to the actual courses." Built at 0.708.005: each course's name in its moment links to the course; names and addresses are the course cards' own; no word added.
14. **The ground of the top and bottom.** "The top and bottom as a pair. Wider than the scroll. Yeah, I definitely like this ... something we can bake into the background of these two ... very, very subtle that would just take it from looking excellent to beyond wow." Of four grounds shown (round-bake.js): "Yes, build 1". Built at 0.708.006 and 0.708.008: the Certification page's faint mark pattern, in white, at the two ends of the banner and the closing panel, fading to nothing behind the words; on a phone it keeps to the two rims (Code's own easing, so the words stay clear; overturnable).

The structure pick before these is in RULING__School_Page_Story_Block_Design_Pick_S497.

## 2. What is built (theme 0.708.002 to 0.708.004, commits fc2e6053, 6e0911b7, 29b2bfbc, deployed)

- The NLP school's story is written whole from SCHOOL_WORDS_SIGNED_S465.json, slot story and sources, by tools/school_page_data.py (function `story`). No word is typed in the theme. The other slots of the page are still stand-ins and wait on BRIEF__Place_The_Signed_School_Page_Words_S465.
- The look is school-page.css, class prefix sps; the behaviour is school-page.js section 6. With no script the story reads whole and in order.
- The pair's rules: 32 of room above and below and 48 at the sides; the numerals in Como orange (the year 33, the figures 28); the statement line in Como 21 white; small lines in Mulish 14. The banner and the closing panel each stand 210 deep at 1280. The story between them is set 48 in on each side.
- Proof: the built block measures what the approved preview measured at 1280 and 390 (4,220 and 6,026 tall), photographed top to bottom at both. css_gate passes. The About page measures as it did before (its story 2,950 tall at 1280), and story-scroll.js is untouched.
- The page is built, gate open: no DSRD 6 record, page gate not run.

## 3. Four points for you to rule

1. **The story is no longer one shared component with About.** The school's story is its own block; About still runs story-scroll.js. Kain has not ruled whether About takes this design. DSRD 8's entry and the Component Registry row want your words; Code has not edited either.
2. **Three small labels are reused, not written:** the button "Choose a Course" (the block's own heading), the closed row "Sources", and the figure label "Average Course Rating" (the About band's own). Say if any should read otherwise.
3. **The school page still loads story-scroll.js** and school-page.js sections 1 and 2 (the old story's dots and the buy bar stepping aside), which now find nothing. Removing them is a no-reader-sees-it tidy for the next school page session; the buy bar now stays up through the story, as it did in the preview Kain approved.
4. **The extra moment** Kain asked for is still with you (ASK__School_Story_One_More_Moment_Kains_Own_Course_S497). It will appear with no design change once it is in the data file and the page's parts are rebuilt.

OWED BACK: rulings 10 to 12 written home; your word on section 3.

*No em or en dashes in this file; checked before writing.*
