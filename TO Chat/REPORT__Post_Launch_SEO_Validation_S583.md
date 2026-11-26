> CODE DISPOSITION, S583: first report; changes wait on Chat and Kain's yes where marked.
For Chat: what this needs: read it, sign (or refuse) the fixes listed under "Low risk, ready on a yes", and run the two reads marked for you.

Done when: Kain has the findings and the fixes he wants are signed, applied and proved on the live site.

# REPORT: post-launch SEO and search engine validation, first pass (Code, theme session S583, 26 November 2026)

**Size and cost, first line as the brief asks.** Measured by Code on the live site: about 2,650 page reads at one a second, roughly two hours of running time, no money spent beyond the session on the cheaper model. Nothing on the site was changed except the three redirect repoints Chat ruled. Scopes 4, 5, 12 and 13 are partly or wholly Chat's reads; they are marked.

## Executive summary

The new site is technically sound. All 1,711 addresses in the 15 sitemaps answer 200, none redirects, none is noindex, every one has a self canonical, a title, a description, one main heading, the en-GB language tag, social tags, and valid structured data. No duplicate titles or descriptions. No broken internal links to pages or files (checked: every page and file address the site links to). Address variants (http, www, no slash, capitals, query strings) all land on one canonical address. robots.txt points at the right sitemap and welcomes the AI search crawlers by name. Nothing critical was found. The things worth fixing are one crawl trap, the missing canonical on the hub list pages, 14 or more internal links to a non-canonical category path, and a small number of redirect chains. The big unknown is not a fault: Google has barely begun to crawl the new site, so indexing is slow and the old addresses' value is moving over day by day.

## Your worry, the redirects, answered plainly

Rank Math holds 3,239 active redirect rules, all 301. I tested a random 300 on the live site, old address to final page. **All 300 answered a single 301 straight to the destination recorded, and 295 of the 300 destinations answer 200. None goes to the home page.** The 5 that do not land on a 200 land on a page that itself redirects (a chain, finding 5). What I could not prove: that the list is complete (needs the old address lists, Chat's reads below), and that general landings are harmless (finding 6). Chat already proved 2,636 rows at launch; this is a fresh independent sample, not a replacement.

## Findings

### Critical
None found.

### High
**1. A crawl trap on /enquiries/ (scope 6, 7).** The Spotted a Mistake link on 982 pages carries the whole page address in a query: /enquiries/?topic=correction&page=https://achology.com/learn/... . Evidence: I requested one with a real page address; it answers 200, `robots: follow, index`, and no canonical tag, so every page produces its own indexable copy of the same form. Google already lists such addresses (Chat's find). Cause: the form page has no query handling. Fix, low risk, theme only: on /enquiries/ with any query string, print `noindex, follow` and a canonical to /enquiries/, and put `rel="nofollow"` on the link. Proof: the same request shows noindex and the canonical; Search Console URL Inspection on one.

### Medium
**2. The Knowledge Hub list pages carry no canonical and are not in the sitemap (scope 2, 7).** Evidence: /learn/, /learn/articles/, /learn/psychology/articles/ and every category and type list (about 35 addresses, linked from all 1,711 pages) answer 200 `follow, index` with no canonical tag, and none is in the sitemap. The per tag lists are noindex already. /learn/ is indexed by Google; the type and category lists are not yet. Fix, low risk: a self canonical on each list page. A decision for Chat and Kain: whether they should join the sitemap (they are hubs a reader lands on) or be noindex follow. Code recommends the canonical now and the sitemap yes, because they are the paths that pass strength from the hub to every item.

**3. Internal links to a non-canonical category path (scope 7, 8).** Evidence: at least 14 book notes and articles are linked from list pages under a category path that is not their canonical, for example /learn/personal-growth/book-notes/as-a-man-thinketh/ (canonical /learn/motivation/book-notes/as-a-man-thinketh/), /learn/wisdom-for-life/book-notes/the-power-of-now/ (canonical /learn/general-interest/...). Google will fold them, but it splits link strength and shows as "duplicate, Google chose a different canonical". Cause: an item sits in several categories and each list links its own path. Fix: the list cards link to the item's canonical path. Needs Chat's read on whether that is the intended primary category in each case.

**4. Search authority risk: general landings for old video, tag and job pages (scope 3, 12).** See finding 6.

**5. Redirect chains (scope 3).** Evidence: 5 of 300 sampled rules land on a page that redirects again, all renamed quote pages, for example learn/helping-people/quotes/more-than-techniques goes to /is-coaching-just-techniques/ which goes on again. At that rate roughly 50 of the 3,239 rules chain. Cause: quote pages renamed after the rules were written. Fix, low risk: flatten each so the old address points at the final page (a repoint needs a RULING file from Chat). Proof: one hop, 200. I can run the whole register in one slow pass (about an hour) and send the exact list; say go.

### Medium, needing Chat's reads
**6. Redirect relevance and completeness (scope 3, 12).** Of the 300, 164 land on a general page: 129 old author quote pages on /learn/quotes/ (Kain's standing ruling, left), and 35 others: about 14 old /videos/ pages on /learn/, tag pages on a category hub, /jobs/ pages on /membership/, instructor pages on /about/instructors/. Whether any matters depends on which carried visitors. Chat, please: (a) run the 580 lost pages in gsc_16m/lost_pages.json through the same test (old address, final status, final page) and send me any that earn clicks and land on a general page or a 404; (b) the Bing backlink list was empty, so name any old address with strong external links you know. Until then this is unverified.

### Low
7. **Workbook PDFs requested under old names (scope 6, 12).** Googlebot asked for /wp-content/uploads/2026/11/abcde-model-workbook.pdf and four others on 23 and 24 November and got 404, because the files carry a -1 suffix. The live pages link to the -1 names, which load (200), so Google probably found the names before the rename. Fix if it continues: a redirect from each suffix-less name to its file. Proof: the request answers 301 then 200. Watch the logs.
8. **Server exposes the admin account name (scope 16).** /wp-json/wp/v2/users answers 200 with "Achology Admin" (id 1); ?author=1 redirects to /author/achology-admin/; /readme.html shows the WordPress version. Not a search problem, a hygiene one. Fix needs Kain's yes (it touches the install).
9. **Six book note titles run past 65 characters** (for example the quick and easy way to effective speaking, 67) and three descriptions are out of range (166, 172 and 185 characters). Cosmetic, Chat's words.
10. **Two pages carry no structured data:** /centre-of-human-development/ and /about/what-achology-believes/. Three about pages hold one image without an alt attribute: code of character and conduct, manifesto, code of ethics.
11. **http://www.achology.com/ takes two hops** (to https://www, then to https://achology.com). Harmless; the host can send it straight on.
12. **Sitemap lastmod:** 579 addresses read 2 November and 373 read 3 November (the import days). Honest if no edit since; confirm the date moves when a page is edited (scope 2).

### Monitoring
13. **Indexing is slow, normal two days after launch (scope 4, 5).** Evidence: Chat's sample of 44 sitemap addresses: 6 indexed, 13 discovered, 25 unknown to Google. Server logs: Googlebot made 3 requests on 25 November (18 on 24 November, mostly the 404 PDFs); Bingbot 58 and 42. The sitemap was read by Google on 25 November, 0 errors. Search Console shows no drop: 28 days before launch 2,475 clicks at position 8.2, the first launch day 86 clicks at 8.4. What speeds it: Kain's index requests (about ten a day) on the schools, courses and key pages, strong internal links, and time. /courses/: live answers 200 with the right canonical; Google still holds the old canonical until it recrawls.
14. **Google's Rich Results Test lists no Events item** though it fetched all 19 Event blocks and the structured data validator reads 0 errors (DONE__Event_Data_On_The_Events_Page_S583). Re-read in Search Console Enhancements in about a week.
15. **ssh.achology.com shows a changed host key.** Not a search matter; it was not used (the deploy account serves the site). Worth asking SiteGround whether the old account was moved.

## Coverage, so no limit is hidden

- **Done in full:** 2 (sitemap content, 200s, https, robots link, formats), 7 (canonicals, all 1,711), 9 (titles, descriptions, headings on 524 sampled and in full for presence, alt, language, social tags), 10 (types counted across the site, JSON valid on all; earlier S579 sample for rich results), 6 (robots, headers, variants, logs).- **Partly:** 1 (sitemap inventory 1,711 unique, 1,237 under /learn, 393 under /help; **not** compared with the database post count or the codebase routes, so a published page missing from the sitemap would not show here; I can do it), 3 (300 of 3,239 rules; old-address test waits on Chat), 8 (links and breadcrumbs yes, whole-graph orphan test withdrawn: my first result of 40 orphans was wrong, because the list pages are not in the sitemap so I never read them, and the one I checked is linked from its list), 15 (robots welcomes the AI crawlers, llms.txt answers 200; nothing else tested).
- **Chat's reads:** 4 (URL Inspection list sent as ASK__Url_Inspection_List_For_Chat_S583), 5 (Bing: only old site data so far), 12, 14 (reads 2 and 14 used above).
- **Not done, and why:** 11 (cited, not redone: S576 to S580), 13 (independent searches: needs a browser pass on Google and Bing, I can do it next), 16 (anything else: nothing further found), 18 (no fix started without a yes).

## Low risk, ready on a yes (apply, then prove on the live site)

Findings 1, 2 (the canonical), 5 and 7. All are one theme file change or a redirect edit, with a backup and rollback (the theme git and Rank Math's export). Needing Kain's yes through Chat: finding 2's sitemap choice, finding 3 (which path is primary), finding 8 (admin name and readme), and everything on titles and descriptions.

## Scope 19, keeping it protected, without a new subscription

Extend the weekly health check (SHIP__Weekly_Health_Check_S579). The two scripts that did this work already test most of it: the page read gives, in one pass, sitemap against 200 status, noindex and canonical on each page, duplicate titles, structured data JSON and internal link targets; the rule test gives chains and landings. Proposal: move them into the theme tools folder as one tool. Schedule: the first 14 days after launch, daily on the sitemap, canonicals and noindex (about two minutes if the page read is limited to changed addresses); then weekly for 90 days with the redirect register and Google's index count from Chat's key; then monthly, plus a run before every deploy. Human intervention only for: index requests, the weekly read of Search Console Enhancements, and rulings on landings. Cost: none.

OWED BACK: Chat's yes or no on the low risk fixes (1, 2, 5, 7) and the sitemap choice in 2; the lost pages test (6a); Chat's inspection results (read 1); a BRIEF to the factory for the course block audit (not mine, named in ANSWER__Audit_Route_And_Home_Hub_Link_Ruled_Out_S495).

*No em or en dashes in this file; checked before writing.*
