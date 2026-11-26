For Chat: what this needs: read it; item 5 of the agreed string is built and scheduled. Nothing is asked of Chat; from Monday 30 November a REPORT__Weekly_Health_Check_<date>.md lands in TO Chat each Monday morning.

Done when: Chat has noted where the weekly report comes from and what it holds.

# SHIP: the weekly health check (item 5)

Code, S579 theme session, 26 November 2026. Tool: `tools/health_check.py` in the theme repo (not a runtime file). Schedule: `~/Library/LaunchAgents/com.achology.healthcheck.plist` on Kain's Mac, every Monday 06:00 (run on wake if the Mac was asleep). Its own figures are kept in `~/.achology-health/` for the week to week comparison.

What it does, changing nothing on the site: reads every address in the sitemaps and fetches each page one at a time, 2 seconds apart, stopping after four refusals in a row (about two hours in all); checks every link those pages carry, once per address, with sites that do not answer listed apart from pages that are gone; reads Rank Math's 404 log for the last seven days; runs Lighthouse (phone) on one page of each of twelve kinds for the score, the vitals and every console error; writes the report into TO Chat beside last week's figures.

Proved with its quick mode on 26 November (20 pages, 40 links, all twelve speed runs): every part ran and wrote its report. Two findings from that run, for the record: the 404 log shows 14 missing addresses asked for this week, mostly old /product/ course addresses (the redirects card); and the Academy page's largest paint read 5.2 s in that run and 3.2 s in a second run, so it is in the wide-variation range and the weekly figure will settle it.

*No em or en dashes in this file; checked before writing.*
