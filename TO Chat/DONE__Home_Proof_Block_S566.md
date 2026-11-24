For Chat: what this needs: nothing to build; read the three answers below and rule on the 012 refile (answer 2). Card #98.

Done when: Chat has read this and ruled on answer 2.

**DOCUMENT TYPE:** done from Code (Home session, S566, 24 November 2026). **Answers:** FROM Chat BRIEF__Home_Proof_Block_Signed_S486.

## What was built

Voices From Every Stage of the Road stands under the Who Is Achology? road block in the Home preview (branch-f/home-s558, commit 9f01fe8d; previews/home-page-s558, blocks.proof()). Nothing in the theme; nothing else on the page moved.

- **One home kept.** Every card is drawn from the NLP school page's stored card (data/school-page/nlp.json), exactly as build_proof.py drew it; the two link cards are tools/reviews_block.ways('school'). reviews_block.block() has no shape for three stage columns, so no Home kind was added to it; the card markup is still never typed by hand.
- **The same as the mock-up.** proof_compare.py: the block's markup is identical, character for character (119,625 characters, 30 cards, 27 held in the page's own markup), and its sheet is proof.css unchanged. measure_proof.js, WebKit, every element of the block (1,757 to 1,763 boxes): **0 boxes differ at 1440, 1024 and 375**; block height 783, 809 and 1,645 on both.
- **The brief's measures, built:** heading to line 16, line to stage names 24, stage name to card 16, title to words 16, verified line to course 8, cards to the link cards 32, band 64 below (65 above to the heading's ink, as in the mock-up); the three reviews' words start on one line at 1440 and 1024; nothing scrolls sideways at 375.
- **The turning:** every card turns through its stage's ten and comes back to its first at every width; the corner mark is a button named Next review; the room the cards hold never shrank.
- **Titles:** all thirty sit on one line at 1440 and 375. At 1024 two wrap to two lines, in the mock-up too: "Better Prepared to Make Changes" and "More Confidence in Serving Clients". Left as signed; shorten them if you want one line at 1024 as well.

## The three questions

1. **The last-line breaks.** Confirmed: a review that turned in had none laid (0 breaks on every turned card). Fixed in proof.js, the one change from the mock-up: when a held review shows, each of its text blocks is laid through the shared script's own call, window.achologyLastLine(el). Measured after: turned cards now carry their breaks (1 to 3 per card), the boxes at load are still identical to the mock-up.
2. **Course 012.** 250 rows are filed under 012 (Skilled Helper Practitioner Training); **66 of them speak of hypnosis or trance** (Wanda Amos, May 2017, and Daisy Gallop, June 2018, among them), and only **2 name Egan or the Skilled Helper**. None is a copy of a 013 row (013, the Hypnotherapy Practitioner Course, holds its own 250). The dates run 2017 to 2019 almost entirely. So the likely fault is that a second set of hypnotherapy reviews was filed under 012 on import, not 66 strays. **Proposed fix:** check the 250 against the source export by review id; refile every hypnotherapy one to 013 (or to the hypnotherapy course it came from), in reviews.csv.php and the imported review posts together, then let the course pages' and schools' live counts recount. A theme data job for a factory session with a signed brief; it changes nothing on the Home block (none of the thirty is a 012 review).
3. **4,517 or 4,516.** **4,516 is right.** Kain ruled it at S054 ("move the figure to 4,516", shared-parts.php achology_figures()) when review post 29170, a mis-imported Udemy review of a nutrition course, was removed; the live archive count is 4,516. The file reviews.csv.php was never trimmed, so it still holds 4,517 rows. The fix is to take that one row out of the file so the two agree.

## Also this session

- **Centre sign-up proved in Kit:** Kain's own address now carries tag 26381995 (Website Centre of Human Development Launch Notify). The form reaches Kit; the earlier empty read was the tag count's lag.
- RULING__Footer_Link_The_Centre_Coming_2027_S486 (rewritten version, the fire glare) is read; it is a theme job for its own change set and is not started.

*No em or en dashes in this file; checked before writing.*
