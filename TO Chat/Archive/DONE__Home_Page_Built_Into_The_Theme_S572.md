> Chat S494, 26 Nov 2026: answered; Home live and signed. Archived.
> Stays, Chat S491, 25 Nov 2026: read; answered by the side session's ANSWER and now written home. Waits on Code setting the search words and entering the gate rows.
> Stays, Chat (side session of S573), 25 Nov 2026: read whole; answered in FROM Chat/ANSWER__Home_Search_Words_And_Hairline_Ruling_S573. Waits on Code setting the words and the gate exceptions, and on Kain's two answers through Code.
For Chat: what this needs: rulings on the Home page's open gate rows below, and the page's Rank Math words (focus keyword, search title, description), so Code can close its DSRD 6 record.

Done when: each open row below has a ruling or an exception from Chat, and the search words are in FROM Chat for Code to set over WP-CLI.

# DONE: the Home page is built into the theme and on the build site (S572, 25 November 2026)

**Theme 0.708.484, deployed.** deploy.py: all PHP parses on the server; 23 files sent; cache purged; server, local and zip agree. Kain's words: "Yes, build it", then "Yes, deploy it".

**What shipped.** `front-page.php` and `home-setup.php` (WordPress picks the template for the front page; no page was created), `home.css` (the signed preview's sheets flattened to his picks by `tools/home_page_flatten.py`), seven `home-*.js` scripts, `data/home-page/` (the stored blocks and the course finder's data), the Achology word rows in `page_gate.py`, the questions renderer's column name through `wp_kses_post`, and two shared additions (`panel_title` in `global-impact.php`, a count-up guard in `course-page.js`). Built by a Sonnet branch session to the signed preview, merged with main, and proved in WordPress Playground against the preview at 1440 and 375: all nine blocks the same height to the pixel. Its full report: `previews/home-page-s558/BUILD_REPORT_S572.md` in the theme.

**Status: built, gate open.** page_gate on https://achologytest.com/ this session. Passing rows include address, breadcrumb, orphan, mixed content, acronyms, image format, alt and dimensions, and both new Achology word rows. Open rows:

1. **hairline-present and hairline-spacing**, at every block boundary and all three widths. Home's grounds take turns (DSRD 9 45.29) and the statement card makes one turn itself (45.32), so the gate's "a hairline, 48 above and below, at every boundary" does not describe this page. Ask: an exception for Home, or the row taught 45.29.
2. **accessibility-scan:** one colour contrast failure on three labels in the community block's rooms (`.c5-lab`). A real fault; Code mends it next sitting unless Chat rules otherwise.
3. **rank-math and keyword-density:** post 45038 is unscored and has no body. Ask: the page's focus keyword, search title and description.
4. **image-responsive:** 72 pictures carry no srcset (the films' card backgrounds and the statement's bubble among them). Code's to mend.

**Not done, carried from the build report.** The Knowledge Hub tile summary "at 14": neither session could tell what 14 measures; ask. The course finder's data is the preview's 39 products, not yet drawn from `courses-setup.php` (brief S487 item 2). The belt's tiles, Voices, the films and the finder's shell are stored markup, refreshed by `tools/home_page_data.py`, not drawn live. Not yet judged by Kain in Safari on the build site.

**The build-against-sheet gate (H5) stopped this session's close, on rows Home did not touch.** component_gate.py after the deploy: book-note card 48 failed and course card 44 failed (the /cards/ specimen pages draw neither card: "nothing on the page matches .card--book-note" and ".card--course"); section-heading tile 3 failed (no `.help-popular__glyph` inside `.policy-tile` on Code of Ethics); review card 1 failed (`.rv-card__attr` margin-top: sheet 20, built 24 on /reviews/). None of these files is in this change set (`page-cards.php`, `cards.css`, `reviews.css` and the policy sheets were not in the merge), so Code has added no waiver and changed nothing: these wait on a factory session to find when each went red, and on Chat for any ruling. One related fact for the review card's sheet: on Home only, Kain ruled the Voices card's space above the student's name from 20 to 16 ("Yes"); the shared card and its sheet still say 20.

OWED BACK: the rulings on rows 1 and 3, what "14" measures, and who takes the four red components above.
