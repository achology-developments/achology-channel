For Chat: what this needs: read it; it records the launch checklist's section C run and Kain's Search Console tidy. One item is Chat's: the cookie consent finding (C3) touches the Privacy and Cookie policies' promise.

Done when: Chat has read it and noted C3 and the Home speed reading on their cards.

**DOCUMENT TYPE:** report from Code, S575 (factory session, Opus), 25 November 2026, about 23:25, two hours after the switch. Theme 0.708.491 on achology.com. Nothing on the site was changed in this session.

## Section C, run by Code

1. **Rank Math 404 log: PASS.** The 404 monitor is on. One missed address since 21:30: /achology-kb/how-does-an-achologist-approach-the-idea-of-human-motivation (22:51), a cut-short form of an old Help address. The old site's backup holds exactly 213 published Help articles (ht_kb, status publish); all 213 have an active redirect on achology.com. The other 310 /achology-kb/ addresses named in the old site's text were never posts. The real old address /achology-kb/how-does-an-achologist-approach-the-idea-of-human-motivation-and-drive/ answers 404 from the host and was not a published post either. Read again in a week, as the checklist says.
2. **Search Console:** see the tidy below.
3. **Analytics: the tag is on, and it does NOT wait for cookie consent. Finding.** /about/ read from the host carries gtag.js?id=G-HJ29S4Z0R8 and gtag('config') as plain scripts, before any choice; Complianz runs as opt-in, region uk, and no gtag('consent','default') line exists. So Analytics cookies are set before a UK visitor says yes. Whether visits arrive in Analytics was not read (Analytics needs Kain's sign-in).
4. **Forms: PASS from the host.** The Enquiries form (topic Some Other Matter) and the Spotted a Mistake topic (correction, page /about/) each posted once from the live host with a fresh signed stamp, name "TEST day-after check, please ignore", kain@achology.com: both answered ok true. The mistake report is seen arriving: "Enquiry: A Mistake on a Page" from wordpress@achology.com to editorial@achology.com. The enquiries@ copy and Karen's copy of last night's gift test are not seen by eye (not in the mailbox Code can read).
5. **B10: PASS.** page_gate.py on /, /about/, /academy/, /membership/, /help/, /learn/wisdom-for-life/articles/understanding-your-core-values/, /policies/privacy-policy/ on achology.com: canonical, indexing, sitemap, meta-title, meta-description pass on every page; links-resolve passes (one planned unbuilt page, /free-events/, 301). The remaining FAIL rows are the known pre-launch rows only (the orange Achology word, the article template's closing supporting lines, Help's record line). Structured data on Home, /about/ and the article parses whole and names only achology.com. Home: Schema Markup Validator 0 errors, 0 warnings; Google's Rich Results Test "Crawled successfully" at 23:11.
6. **Lighthouse on Home (PageSpeed Insights, Lighthouse 13.6.0, 23:07):** phone Performance 47 (First Contentful Paint 5.3 s, Largest Contentful Paint 11.2 s, Total Blocking Time 470 ms, Layout Shift 0.012, Speed Index 6.9 s); computer 67 (1.0 s, 2.2 s, 440 ms, 0.001, 1.4 s); Accessibility, Best Practices and SEO 100 on both. Lighthouse's leads: render-blocking requests about 3.7 s, unused CSS 458 KiB, unminified CSS 315 KiB. Home's record chapter 4 now reads pass (written); chapter 9 was NOT written: Kain stopped that edit, so it still reads not run, and the numbers live here.
7. Not run tonight, with Kain later: the DNS tidy, the orange word, karen@ alias, the cdn certificate record.

## Search Console tidy, with Kain, 23:15 to 23:22

- **Sitemaps:** Kain removed the five old sitemaps (product_cat, school, category, page, post; page-sitemap.xml read "Couldn't fetch"). One left: https://achology.com/sitemap_index.xml, Success, 1,665 pages found. The old product_cat-sitemap.xml now answers the new site's 404 page.
- **Pages (indexing):** last update 16 November, so it still describes the old site: 1.47K indexed, 2.82K not (top reasons: alternate page with canonical 1,134; redirect 212; noindex 113; 404 83; server error 4). Read again in about a week.
- **Crawl stats:** last update 24 November, before the switch; achology.com shows "Problems last week" (old site). Cannot yet say whether SiteGround's robot check turns Googlebot away, but Google's own Rich Results Test and PageSpeed both fetched the live Home page tonight, which says it lets Google through.
- **Core Web Vitals:** old site, 24 November: 481 poor, 0 good, phone and computer. The new site's real-visitor verdict needs about 28 days (DSRD 6 section 9's after-launch read).
- **HTTPS:** 486 pages on HTTPS, 0 not, "No issues detected in the last 90 days".

## C3 fixed, 23:30, on Kain's "Yes, fix it"

Analytics now waits for consent. No theme file changed; two plugin settings on achology.com. Copy of the settings before: ~/cmplz_options-before-analytics-consent-2026-11-25.json on the host.
- Complianz's `cmplz_options`: `compile_statistics` from "no" to "google-analytics" (so its own Google Analytics guard loads, and statistics count as needing consent for the UK opt-in region), and `configuration_by_complianz` "no" (Rank Math keeps placing the tag; Complianz adds no second one).
- Complianz's stored blocked-script list (`cmplz_transients`, key `cmplz_blocked_scripts`) cleared, object cache flushed, SiteGround dynamic cache purged.
- **Proof, from the host:** Home and /about/ now serve `<script type="text/plain" data-service="google-analytics" data-category="statistics" ... data-cmplz-src="https://www.googletagmanager.com/gtag/js?id=G-HJ29S4Z0R8">`.
- **Proof, in a browser:** /about/ before any choice: no request to Google and no _ga cookie. After Accept All: gtag.js loads, a collect request goes to region1.analytics.google.com for G-HJ29S4Z0R8, and _ga and _ga_HJ29S4Z0R8 are set. /academy/ after Reject All (cmplz_statistics=deny): no request to Google.
- **For Chat:** the Cookie Policy's list of cookies may need Google Analytics' _ga and _ga_HJ29S4Z0R8 named under statistics, if it does not already; the policy's words are Chat's.

*No em or en dashes in this file; checked before writing.*
