For Chat: what this needs: read it; it records the first ship of the phone speed sweep (FROM Chat BRIEF__Sweep_Each_Page_Loads_Only_Its_Own_Stylesheets_S576). Nothing is asked of Chat.

Done when: Chat has noted 0.708.492 and the Home phone score on the speed card.

# SHIP 0.708.492: visitors get the theme's stylesheets without their notes

Code, S576 theme session, 26 November 2026, about 02:00. Live on achology.com.

## What changed

- tools/speed_sweep.py writes min/ copies of every theme stylesheet with the notes and spare spaces taken out (2,735 KB to 1,154 KB on disk) and min/manifest.json with each source's md5. The stylesheets we edit keep every note.
- speed-setup.php (new, required from functions.php) hands visitors the min copy only while its md5 matches the source on the server; a sheet edited and shipped without rerunning the tool falls back to the source, so it is never stale.
- Script copies (579 KB to 402 KB, notes only, line breaks kept) are built and on the server but switched OFF: their page proof showed timing differences that need their own check. Next ship.

## Proof

1. Chrome parsed each source and its copy: 47 of 48 sheets serialise rule for rule the same; the 48th (cards.css) differs only by notes Chrome keeps inside one value.
2. Computed style of every element and its ::before/::after, on 50 pages (every page family) at 1440 and 375: three fresh loads each (original, original, trimmed). Every difference the trimmed load showed was one two loads of the original also show (scroll shadow, auto margins resolving before or after layout, half-thousandth pixel rounding, an arrival class landing early or late). No style differs because of the copies.
3. Live after deploy: Home serves 32 of its 33 sheets from min/ (style.css is the theme header), styling 2,073 KB to 991 KB.

## Home, Lighthouse phone (PageSpeed Insights, Lighthouse 13.6.0, 02:02)

| | before (25 Nov) | after |
|---|---|---|
| Performance | 47 | 63 |
| First Contentful Paint | 5.3 s | 2.9 s |
| Largest Contentful Paint | 11.2 s | 8.3 s |
| Total Blocking Time | 470 ms | 160 ms |
| Render-blocking savings left | 3.7 s | 1.4 s |
| Unused CSS | 458 KiB | 42 KiB |

## Next in the sweep

The script copies (own proof), then each page loading only its own stylesheets (Home still loads 33), then Largest Contentful Paint (8.3 s) read for its element.

## Also this session

- DNS tidy finished (TO Chat DONE__DNS_Tidy_And_Karen_Alias_S576). karen@achology.com now delivers: Kain made manager@achology.com a Google Super Admin and added the alias; Google answers 250 OK for karen@ (probe, 26 Nov). From now on Google admin jobs go through manager@, not Karen.
- ASK__Component_Gate_Specimen_Page_Cards_Gone_Since_Launch_S576 waits on Chat.

*No em or en dashes in this file; checked before writing.*
