> Disposition, Chat S487, 24 Nov 2026: read; the four answers accepted, section 4 answered in FROM Chat/ANSWER__Knowledge_Hub_Build_And_Page_Check_Asks_S487; card #98; archived.
For Chat: what this needs: read the four answers below; two small things are put back to you (sections 3 and 4). Card #98.

# DONE: the Home page's Knowledge Hub belt, built from the signed mock-up (Code, S567 branch session, 24 November 2026)

**Answers:** FROM Chat BRIEF__Home_Knowledge_Hub_Block_Signed_S486. **Where:** the Home preview on branch-f/home-s558 (previews/home-page-s558), between the members' films block and the questions block, in Kain's order of S567 (hero, Who Is Achology?, Voices, Gateway, free events, the films, the Knowledge Hub belt, questions, close). Nothing is in the theme.

## 1. What was built, and the proof

- **The block is the mock-up's own markup**, word for word (heading with its curly apostrophe and the phone break after "Right Now,", the line, the five-tab switch, the two arrows, the foot button), held in blocks.py, with the twenty tiles inside it drawn on the build site (section 2).
- **The stylesheet is kh-block.css** (kh.css in the preview) with two changes only: the library behind the band is the signed one (13) alone, its twelve trial settings taken out and its rule written on .hk itself; and the arrows' white rest no longer needs `!important` (section 5).
- **The script is kh-block.js** as the mock-up ran it.
- **Measured against the mock-up** (measure_kh.js, WebKit, fonts loaded, every picture loaded on both): every element of the block compared one by one for its place, size, font, size, weight, line height, colour and background, at 1440, 1024 and 375. **0 differences at all three** (301, 302 and 306 elements), block heights 728, 726 and 742 on both.
- **Behaviour, on the build:** the switch shows twenty under Everything and five of its own kind under each other tab, aria-pressed following; each arrow press moves exactly one card (282 at 1440, 238 at 1024); back from the first goes to the end, on from the last goes to the first; no arrows on a phone, which swipes; twenty links, each its own published page.
- **Kain sees it** in the Change Viewer as one Before and After switch (Before: the page without the belt), viewer_proof 5 measured, 0 failed.

## 2. The tiles, through the one home

kh_tiles.php runs on the build site through `wp eval-file`. For each of the twenty addresses it finds the post and draws its tile with `achology_kh_subject_grid_html()`, the function /learn/'s walls draw with. Three things that home does not draw were added. Each is named here so you can tell which words came from where:
- **The summary on articles and quote articles.** The home prints a summary (bx-sub) only for book notes and workbooks, from their excerpt. For articles and quote articles the tile takes the record's own search description. **All ten of your signed summaries for those cards are that field word for word**, and all ten book note and workbook summaries are their excerpts word for word. So no word on any card is typed by hand.
- **The quote article's tile.** The walls draw a quote as the quote card itself, not as an article tile. So the quote tile is the article tile's markup with the quote's own featured image, the picture its page shows (its Download button hands out the JPG of the same card). Its label, title and reading line come from the same home functions.
- **The workbook's foot line**, your "Free PDF · Four Parts" (section 4).

For the preview only: the build site answers any browser it has not seen with its bot check, so a picture taken straight from its uploads can come back as a page. The twenty pictures are copied once from the build site's disk over SSH into the preview folder (img/kh, not committed). The theme build draws them in place and needs none of this.

## 3. The four questions

1. **kh-subject.css and the book shelf.** The preview loads kh-subject.css whole, through kh-block.css's own @import, as the mock-up did. html.bg-book is set on the page. Read rule by rule, it draws only `.bk` covers and book note tiles, and on Home those exist only in the belt, so it touches nothing else on the page. For the theme build my call is to move the tile rules to a shared file rather than load all of kh-subject.css on Home; I will report that build separately. `data-hk-shelf` is read by no stylesheet or script in the theme, so it was left off.
2. **Quote articles with no picture of their own:** 6 of 428 published. All six have no featured image, so their sharing image falls back to the default: how-do-you-turn-rejection-into-something-positive, how-do-you-stop-taking-on-other-peoples-problems, where-do-limiting-beliefs-come-from, does-growth-really-happen-outside-your-comfort-zone, why-does-open-mindedness-matter, why-do-we-put-others-on-a-pedestal. None of them is among the belt's five.
3. **The quote articles' reading line** is drawn by `achology_kh_words_line()`. That counts the content's words at 200 a minute, which is exactly what single-quote.php prints for the page's own facts (the same field, the same formula), so the two cannot differ. All five quote cards read the same as your signed lines (978, 862, 923, 836 and 953 words, 5 minutes each). The ten article and book note lines also match yours to the word.
4. **The workbook line.** Each workbook record carries `workbook_parts` (its parts written out, four in each of the five) and `workbook_step_pages` (four step pages). So "Four Parts" is the record's own count. No record carries a page count or a time, so nothing truer is on file. Your line is placed as written. If you would rather draw it from the record, the count of `workbook_step_pages` gives "Four Parts" for all five today.

## 4. Two things put back to you

- **Two off-scale spaces in the signed stylesheet:** the switch tabs' 18 side padding, and the belt's 20 top margin (4 more of the row's own shadow room makes 24 to the cards). Kain's standing scale ruling says off-scale values are snapped and reported. Your brief says to match the mock-up box for box. I kept the signed values, marked them as one-offs, and report them here. Say whether to snap the 18 to 16 and the 20 to 16 (which moves the cards up 4); either takes one line.
- **The 1279 width** where the arrows step half over the edge is also off the system's widths. It is marked as the signed belt's own edge.

## 5. The arrows, the clean way

The icon button script (buttons.js) leaves alone any control that already carries `data-bf`. The two arrows carry it in the markup, so they keep their signed white rest with the cards' shadow, and their orange hover, with no `!important`. In the mock-up the arrows took the family's mark (bf-icon) and were held white against it. Their measured boxes and colours are the same in both.

## 5a. Changed after Kain's review: the arrows outside the cards below 1280

Kain reviewed the built belt the same day. Below 1280 the signed arrows sat half over the cards, and the left one covered the first title ("How" read "ow"). That afternoon he had ruled the same fault on the Membership belt: "the arrows are just very close to the side of the cards. Doesn't look quite right". His newer word overturns the signed half-over-the-edge rule. **From 768 to 1279** the arrows now stand at the container's own edges, and the belt narrows by an arrow and 24 on each side. So they sit outside the cards with 24 clear and never leave the screen. The cards shrink a little to make room. Phones keep the swipe.

Measured: 24 clear on both sides, and the arrows on screen, at 1440 (arrows at 100 and 1340), 1280 (20 and 1260), 1024 (48 and 976, four cards) and 768 (32 and 736, three cards). 1440, 1280 and 375 still show 0 differences from the mock-up. At 1024 and 768 the belt now differs from it by this ruling. One more fault was fixed at 768: the Quote Articles tab's icon was squeezed to a dot; it now keeps its 16. Please write the arrows' new rule into DSRD 9 section 45.26 with Kain's words.

## 6. Also this session, the films block

Kain's yes to the films cards at the review card's height. They are measured to the hundredth of a pixel against the Voices card in the same column: 393 at 1440, 419 at 1024 (470 once the reviews have turned), and 320.75, 343.14 and 320.75 at 375. His three column titles are placed (Learning Experience, Self-Directed Study, Learning with Others), with the films placed under them by the question each answers. The films' Before and their switch are taken out.

*No em or en dashes in this file; checked before writing.*
