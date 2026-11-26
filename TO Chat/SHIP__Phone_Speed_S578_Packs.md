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

## What shipped

Theme 0.708.500 (0.708.497 to 0.708.499 were the machinery, built and shipped switched off). 35 packs, one per family of pages that print the same sheets and are the same kind of page (template, taxonomy, archive, post type, 404 or home, read from WordPress's body classes in both the crawl and the page). Every pack passed its test at 375, 1024 and 1440 wide with the closed states opened (69 runs on the changed families plus 18 on the four packs added after the key was corrected, all difference 0; the Academy shows one picture's filter moving on its own timer, shown directly). Pack sizes against the separate min sheets: for example 242,659 to 151,201 bytes (quotes, 66 pages), 155,149 to 118,664 (Help answers, 43 pages), 517,139 to 345,474 (schools), 768,035 to 488,957 (Home).

Live check after deploy: 37 sample pages across every family each print exactly one pack and no other theme sheet in the first pass (the late component sheets stay as they were, printed after it).

Two faults of mine found and mended on the way, both before any visitor saw a pack in the wrong place: the first key ignored that component sheets print in a second pass, so some pages matched nothing; and the policies index and the Help categories print the same sheets, so one could have been sent the other's pruned pack (the first live check caught it; the packs were switched off at once, the key now includes the page kind, the packs were rebuilt and re-proved).

## Lighthouse phone (PageSpeed Insights, 26 Nov 2026, Lighthouse 13.6.0), after the packs

| Page | Performance | FCP | LCP | TBT |
|---|---|---|---|---|
| Home (S577: 85; 25 Nov: 47) | 68 | 2.1 s | 7.1 s | 180 ms |
| Knowledge Hub article (before packs 89) | 96 | 1.7 s | 2.6 s | 0 ms |
| Help answer | 99 | 1.7 s | 1.7 s | 0 ms |
| Events | 91 | 1.8 s | 3.0 s | 10 ms |
| School page (Personal Growth) | 52 | 2.0 s | 4.6 s | 1,990 ms |

Not measured in the pane (slow queue): Pricing, Reviews, Membership, the policy pages and the rest. Home's LCP is a 46 KB picture already sent at high priority with a srcset, so its 7.1 s is paint delay from the 489 KB pack and the page's scripts on the test's slowed phone, not a late picture; Home scored 85 at S577 with LCP 3.4 s, and this run is lower on LCP although its first paint is better: run to run variation on this test is wide (Home read 50, 64 and 68 in three runs today).

## Left, named

- The school pages' main-thread blocking (1,990 ms) is JavaScript, not styling, and is the biggest phone cost I measured. It is the next job: what school-page.js and course-page.js do on load. Not started.
- Home's LCP, as above.
- Whenever a stylesheet is edited: run `python3 tools/speed_sweep.py min`, then `python3 tools/speed_pack.py`, then prove the changed packs, then `python3 tools/speed_pack.py --enable-all`. A pack whose sources changed is not served; the page falls back to the separate sheets until the rebuild.

*No em or en dashes in this file; checked before writing.*

*No em or en dashes in this file; checked before writing.*
