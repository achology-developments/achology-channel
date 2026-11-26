For Chat: what this needs: read it; it records two more ships of the phone speed sweep (FROM Chat BRIEF__Sweep_Each_Page_Loads_Only_Its_Own_Stylesheets_S576). Nothing is asked of Chat.

Done when: Chat has noted 0.708.493, 0.708.494 and Home's new phone score on the speed card.

# SHIP 0.708.493 and 0.708.494: note-free scripts, and Home sends only the styling it uses

Code, S577 theme session, 26 November 2026. Both live on achology.com, deployed with deploy.py (local, server and zip agree).

## 0.708.493: visitors get the script copies

- speed-setup.php: the script_loader_src line held at S576 is switched on.
- Proof, replacing S576's picture proof (which showed timing shifts, not faults): all 50 min/*.js copies tokenise to exactly the token stream of their sources, including where each line break falls (so the browser runs the same code), and no script reads its own address. Live: Home serves 28 of 28 theme scripts from min/; 17 pages across every family loaded with no console error (the check was shown to catch a deliberate error).

## 0.708.494: Home loads only the stylesheets it uses (brief section 2, step 1)

- speed-setup.php: one list of dropped sheets per page family (achology_speed_drop_list) and one function that takes them out (achology_speed_apply_drops). A dropped sheet's own dependencies take its place, so every other sheet prints in exactly its old order (checked live: Home's order is the old order minus the dropped sheets).
- Home drops 10 sheets: gift-banner, membership, warm-room, cards, people, course, kh-front, knowledge-hub, heartbeat, accreditation. Home now loads 26 sheets, not 36; styling 991 KB to 781 KB.
- Proof, two tests that must agree: (1) no rule in those sheets can match on Home: every selector names a class or id on no element, in none of the page's markup, and never written bare in any script it loads (where a script names one, it acts only inside a block Home lacks, read by hand: people.js, heartbeat.js, accreditation.js, course-page.js); (2) switched off in the live page they change no computed value on any of 3,732 elements or their ::before and ::after, at 375, 1024 and 1440 wide. The same test fails (3,433 differences) when home.css is switched off. The one value that moved, the registered property --rp, is used only by kh-front.css.
- Not done: Home also loads help.css twice (as achology-help and achology-component-help). Dropping the earlier copy was proved harmless but did not take, because the second copy is queued after the head's first print pass. Left as it was; next ship.

## Home, Lighthouse phone (PageSpeed Insights, Lighthouse 13.6.0, 26 Nov 12:56)

| | 25 Nov | S576 (0.708.492) | now (0.708.494) |
|---|---|---|---|
| Performance | 47 | 63 | 85 |
| First Contentful Paint | 5.3 s | 2.9 s | 2.4 s |
| Largest Contentful Paint | 11.2 s | 8.3 s | 3.4 s |
| Total Blocking Time | 470 ms | 160 ms | 210 ms |
| Render-blocking savings left | 3.7 s | 1.4 s | 1.5 s |

## Next in the sweep

The same two tests, family by family: About, Academy, the 7 schools, the 28 courses, Membership, Events, Certification, Accreditation, pricing and gift, the founder and policy pages, Help, the people pages, the Knowledge Hub. Then the packed file per family (brief step 2), then every page re-measured and the DONE.

*No em or en dashes in this file; checked before writing.*
