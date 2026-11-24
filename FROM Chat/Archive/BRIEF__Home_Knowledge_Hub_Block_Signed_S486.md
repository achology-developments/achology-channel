> CODE DISPOSITION, S567: DONE. Built in the Home preview between the films and the questions (Kain's order), 0 measured differences from the mock-up at 1440, 1024 and 375; answered in full, the four questions included, in DONE__Home_Knowledge_Hub_Block_S567.md.
For Code: what this needs: build the Home page's fourth block, the Knowledge Hub belt, exactly as its signed mock-up, under the proof block in the Home preview, and compare the build against the mock-up at 1440, 1024 and 375 before Kain looks. Answer with a DONE.

Done when: the block stands under the proof block with no measured difference from the mock-up at 1440, 1024 and 375; the switch filters the belt; the arrows move it one card and run round both ways; every one of the twenty cards opens its page; and your DONE answers the four questions at the foot.

**DOCUMENT TYPE:** brief from Chat (Session 486, 24 November 2026). **Card:** #98 (Homepage: Sign And Build The Front Page). **Kain's word:** "Yes, sign it", on the whole block in his side panel, after shaping it over a long sitting (his words are in DSRD 9 section 45.26).

**Read first.** DSRD 9 section 45.26 (what is signed, item by item). DSRD 8 section 6 and kh-subject.css (the tiles, bx-tile, as /learn/ draws them, with html.bg-book). DSRD 7 sections 3.0, 3.3 and 5 (the tab track). courses-directory.css .cd-band::before (the picture that fades in from the right, which the library copies).

**The spec is the mock-up.** Folder "Home Knowledge Hub Block 24 November 2026" in FROM Chat:
- home-kh-final.html: your Home preview with the road, the proof block and this block in place.
- kh-block.css: the block's rules. Everything else is the tiles' own (kh-subject.css), the lead bar, the second choice button.
- kh-block.js: the switch and the belt, about twenty lines.
- kh-signed-20.json: the twenty cards in order (kind, address, title, summary, reading line, picture). Picture addresses point at the build site; the quote images are each quote article's own download JPEG.
- kh-img: the five quote images as the mock-up used them, for your measuring only.
- build_kh_block.py: how the mock-up was made.

**What to build.**
1. Heading and line are Kain's own words, word for word, including the curly apostrophe. On a phone the heading is 21 and breaks after "Right Now,".
2. The switch is the signed tab track at the full container width, five equal tabs, buttons with aria-pressed. It filters the belt by kind.
3. The belt: four cards across the container, 24 apart; arrows outside the container, 24 from the cards, level with their middle; white at rest with the cards' shadow (the mock-up holds them against bf-icon's transparent rest with !important: find the clean way); each press moves one card; past the last, back to the first, and back from the first, to the end. Under 1280 the arrows sit half over the edge; a tablet shows three; a phone swipes with no arrows.
4. The cards are the tiles as /learn/ draws them, with the book shelf on. The only Home rules: picture zones in the quote image's shape (2400 by 1260), covers at 82 in 100 of it; tiles as columns the row's height; the summary on every card, three lines; the reading line at each card's foot.
5. The library: the theme's bookshelf image, the right 62 in 100 of the band, fading leftwards from 55 in 100, greyscale, sepia .55, brightness 1.04, opacity .10; on a phone from below at .06.
6. Draw the tiles through the one home that draws them on /learn/, never a hand copy. The block wants a PHP part or a data tool, your call.

**Four things to settle and report.**
- kh-subject.css on the Home page, and the book shelf class: load it whole, or move the tile rules to a shared file; scope bg-book to the block if it touches anything else on the Home page.
- The rejection quote article (/learn/mental-wellness/quotes/how-do-you-turn-rejection-into-something-positive/) has no quote image and its sharing image is the default. Say how many quote articles lack one.
- The quote articles' reading line is read from each page's facts ("978 words", "5 Min Read"). Draw it from the same field the page uses, so the two never differ.
- The workbook line "Free PDF · Four Parts" is Chat's wording; if a workbook record carries a truer fact (pages, minutes), say so.

*No em or en dashes in this file; checked before writing.*
