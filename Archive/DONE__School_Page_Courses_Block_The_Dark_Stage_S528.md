> CHAT DISPOSITION, S471: Acted on. Pick 32 written home in DSRD 9 section 44; the supporting line ruled site-wide in ANSWER__Academy_Beliefs_Lower_Blocks_And_School_Pick_32_S471.

Needs: Chat to write Kain's school pick 32 home in DSRD 9 section 44, and to rule one site-wide question on the Lead with Bar component (section 3 below). Nothing here is a question for Kain.

# DONE: The Courses in This School is The Dark Stage; its button is the family's; its supporting line fills its row (Code, theme session S528, 16 November 2026)

## 1. Kain's ruling, pick 32

On his read of the School of Cognitive Behavioural Psychology, with a picture of the block: "this block here is letting down the entire page. How would you propose this block gets improved?" Shown four whole directions in the Change Viewer (round-crs in the school page previews folder: the chosen course tightened; the shelf; the path; the dark stage), he said: "I like the dark stage option actually, Claude, but again, I'm going to ask you to please ensure that your measurements are correct, that you're using full width of columns when it comes to placing text. Like the subheading is literally for some reason crammed into half of the page ... You don't seem to be using or making the correct use of our buttons. We have essentially an entire suite of buttons designed for the website and links, and you don't seem to be using it."

## 2. What changed, on all seven school pages

- **The dark stage.** The list stands as it did. The chosen course stands on the brand dark (the footer dark), its picture melting into the panel, its name at 28 on 1.25 (24 on a phone), its line at 18 in white at 0.9, its three figures one quiet row with a hairline between them in place of three sand tiles. The same panel opens under a course's name on a tablet and a phone. No word changed.
- **The button.** Explore This Course is now the site's main button (DSRD 7 section 5.1): written as btn btn-primary with its arrow by the school page data tool, so the button script gives it the disc. Its own paint is gone from the school stylesheet. Measured: 46 tall, the action orange, 4.55 to 1 under its white words.
- **The supporting line.** See section 3.

Files: school-page.css, no-lone-words.js, tools/school_page_data.py, the seven school data files, style.css. Theme 0.708.127 to 0.708.130, last commit 3fddbe5b, pushed, deployed, cache purged; the deploy tool's three proofs passed each time.

**Changed, verified 7 of 7.** Measured on the build site in WebKit on all seven schools at 1443, 837 and 393 (previews/school-page-s482/measure_stage.py): no sideways scroll; the panel on the dark; the name 28 (24 on a phone); the button the family's main button on every school at every width; no page error. Two pictures read by eye, the CBP school at 1443 and 393.

## 3. Why the supporting line stood in half its width, and one question for Chat

The line always had its container's full width (measured: 1122 in a 1104 column with its bar). Two things in no-lone-words.js cut a two row line near the half:
1. Any block of 140 letters or fewer is given balanced rows by the script, on the element itself, which outranks the stylesheet. This block's line on the CBP school is 137 letters, a few words too long for one row at 1104.
2. With that gone, the measured lay still set the last two rows evenly to give the last row its four words.
"Pretty" was tried and measured in Safari: it also sets a two row line near the half.

Built, on school pages only: a block's supporting line (the Lead with Bar) wraps plainly, and its last row is mended by the script's own "fill" lay (S526), which takes words from the row above only and leaves that row as full as it goes. Measured after: where a line takes two rows, its first row reaches 76 to 101 per cent of its container on every school at every width (it was 54 on the CBP school at a computer).

**The question.** Kain's full container ruling of 16 November is site-wide in his words ("This is a site-wide thing"). The same halving will be on every page whose supporting line is a little over one row. Should the Lead with Bar take this rule on every page? It is one condition in no-lone-words.js (the school page test removed), and a sweep by the harness's rules, so it needs your brief and Kain's word on rendered pages.

## 4. Named plainly, not done

- **The page's other controls are still outside the button family.** Kain: "you haven't applied our button standards to this entire page." Read today: buttons.js dresses controls by class, and the school page's own controls (the course list rows, the knowledge tree's topic rows, resource links and Show All link, the practice rows' plus signs, the story's Choose a Course button, which carries a mark that makes the button script skip it) are not in its lists. Only this block's button is fixed. A measured audit of the whole page against DSRD 7 sections 4 (space) and 5.1 (buttons) is owed and not run; several of those controls have no member of the family and go to Kain as options under section 5.1's own rule.
- **The knowledge tree's spacing.** Kain: "different spacing between those lines and the lines in the space above, which just makes the block feel ... crammed and a little bit dirty." Not measured yet; part of the same audit.
- **The viewer proof was flaky on this round until two page behaviours were held still in the round's prepare:** the figures that count up (under the film, in the free block), and a least width the students block gives its figures, measured before or after the heading face loads, so the same page came out 55 or 63 wide. The second is a small real inconsistency on course and school pages. Found with previews/school-page-s482/look_diff.py, which names the parts that differ inside the viewer; it may be worth the factory's keeping.

Board card: the School page template.

OWED BACK: one line when pick 32 is home, and your ruling on section 3's question.

*No em or en dashes in this file; checked before writing.*
