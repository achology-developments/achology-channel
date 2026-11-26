For Chat: what this needs: read it; it records step 2.2 of the phone speed sweep (FROM Chat BRIEF__Sweep_Each_Page_Loads_Only_Its_Own_Stylesheets_S576, section 2 step 2). Nothing is asked of Chat.

Done when: Chat has noted the packed stylesheets and how they are made, kept and proved.

# SHIP: one packed stylesheet per page family (step 2.2)

Code, S578 theme session (Sonnet), 26 November 2026. The sweep was widened to this session by Kain's ruling relayed from the main session ("One task delivered through one session").

## What it is

`tools/speed_pack.py` reads the live site slowly (one page at a time, a 2 second pause, stops after four refusals), groups pages by the exact list of theme stylesheets their head prints first, and for every group writes `pack/<name>.css`: those sheets' minified copies joined in print order, without any rule no page of the family can match. `pack/manifest.json` names each pack's family and the md5 of every source sheet it was made from. `pack/enabled.json` lists the packs proved and switched on. The theme's own stylesheets stay the canonical, edited files; a pack is generated, never edited by hand.

## How a rule is left out (the written keep-list, brief section 2 step 3)

A rule goes only when every selector in its list names a class or id that is on no element of any sampled page of the family, is written in no script the family loads (whole word, or a prefix a script builds on), and is written in no shared PHP file of the theme. Kept always: selectors with no class or id; at-rules other than empty media blocks; every class that names a state (open, closed, error, sent, thanks, loading, active, current, selected, checked, disabled, expanded, held, lit, visible, hidden, is-, has-, and the like) and the cookie banner, menu, skip-link and screen-reader prefixes. 336 live pages were sampled (every page, every subject and category, a spread of articles, book notes, quotes, workbooks and answers).

## How a page gets its pack (speed-setup.php)

At wp_print_styles, the page's printed theme sheets are listed in order; if that list equals a pack's family, the pack is enabled, every source sheet still has the md5 the pack was made from and a current min copy, and no sheet has an inline style or a media condition, the separate sheets are replaced by one pack link. Otherwise the page is sent the separate sheets as before: slower, never wrong. Sheets a renderer enqueues later (the component sheets, printed in a second pass) are left as they are. `?achology_nopack=1` shows a page without its pack, for the crawl and the proofs.

## How each pack was proved (brief section 4)

For a sample page of each family, at 375, 1024 and 1440 wide: every closed state a visitor can open without leaving the page is opened first (all details, every expander button, the menu button), then the page's computed style of every element and its before and after is taken; the family's separate sheets are switched off and the pack switched in; the style is taken again; the difference must be 0. The test is shown to fail when the wrong pack is switched in (2,089 differences on Events with the centre page's pack). Pointer hover is switched off in the test, because a hover state recomputes between the two readings and is not the pack. On the Academy, one picture's grey-scale filter changes on a timer with nothing switched (the faces light in turn), shown directly; it is not the pack.

RESULT TABLE AND LIVE CHECK: written below when the final run has finished.

*No em or en dashes in this file; checked before writing.*
