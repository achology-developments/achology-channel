> CODE DISPOSITION, S583: WAITS ON Kain's go; this is the scope document the BRIEF__Post_Launch_SEO_Validation_S494 points at, read in part this session (first 60 lines), to be read whole by the session that runs it.

# Achology: Comprehensive Post-Launch SEO and Search Engine Validation

Now that we have launched the new Achology website, I want you to undertake a comprehensive post-launch technical SEO, search engine indexing and website migration validation exercise.

You have access to the website, its codebase, hosting infrastructure, historical configurations, redirect mappings, Google Search Console, Bing Webmaster Tools and the relevant systems required to undertake this work.

The objective is to establish, through independent investigation and live testing, that the new Achology website is technically sound, correctly represented in search engines, and positioned to preserve its historical organic search authority whilst supporting future organic growth.

I want you to take ownership of this investigation, exercise your own technical judgement and identify anything we may have overlooked during development and deployment.

The following areas represent the minimum scope of investigation. Expand upon them wherever you identify additional requirements, risks or opportunities.

## 1. Complete Website URL Inventory

- Establish a definitive inventory of all pages on the live Achology website.
- Cross-reference the codebase, routing architecture, content databases and live production website.
- Identify every page that should be publicly accessible and indexed.
- Identify pages that should intentionally remain excluded from search engines.
- Identify orphaned pages, duplicate pages, inaccessible pages and accidentally published development pages.
- Confirm that no legitimate content has been lost or unintentionally omitted during the website migration.
- Establish a reliable source of truth against which all subsequent checks can be performed.

## 2. XML Sitemap Validation

- Locate and inspect all live XML sitemaps and sitemap index files.
- Confirm that every indexable canonical page is included.
- Identify missing, duplicated, obsolete or incorrectly listed URLs.
- Confirm that every sitemap entry returns a successful HTTP 200 response.
- Ensure that redirected, broken, non-canonical and intentionally non-indexable URLs are excluded.
- Validate XML formatting, encoding and compliance with search engine requirements.
- Verify that last-modified dates accurately reflect meaningful content changes.
- Confirm that the sitemap accurately reflects the production website rather than an outdated development configuration.
- Establish whether the sitemap automatically updates when pages are published, modified, relocated or removed.
- Confirm that robots.txt references the correct sitemap.
- Confirm that Google and Bing have received and successfully processed the correct sitemap.
- Investigate and resolve any discrepancies between submitted, discovered and indexable URLs.

## 3. Comprehensive Legacy URL and Redirect Validation

Investigate the complete migration from the previous Achology website to the new website.

- Retrieve as complete an inventory as possible of historical Achology URLs.
- Cross-reference historical sitemaps, previous website files, Google Search Console, Bing Webmaster Tools, analytics, backlink data and server logs wherever available.
- Establish whether every valuable historical URL has been appropriately accounted for.
- Test every configured redirect against the live production website.
- Independently test known historical URLs that may not appear in the existing redirect configuration.
- Confirm that permanent redirects use appropriate HTTP 301 or 308 response codes.
- Confirm that each historical URL redirects to the most contextually relevant replacement page.
- Verify that redirect destinations are accessible, canonical and indexable where appropriate.
- Identify redirect chains, loops, conflicting rules and unnecessary intermediate redirects.
- Identify inappropriate redirects to the homepage or unrelated pages.
- Investigate historical URLs returning 404 or 410 responses and establish whether these are intentional.
- Check whether wildcard redirect rules produce unintended results.
- Validate HTTP, HTTPS, www, non-www, trailing-slash and other relevant URL variations.
- Preserve necessary tracking and functional query parameters.
- Check whether historical images, PDFs, downloadable resources and other valuable assets remain accessible or are appropriately redirected.
- Ensure historical redirects are protected against accidental removal during future deployments.

Do not consider a redirect successful solely because it returns a permanent redirect status. Its destination must also be correct in terms of content relevance, user intent and search engine value.

## 4. Google Search Console Investigation

Access Achology's actual Google Search Console property and investigate the available reports directly.

Review:

- Property ownership and verification.
- Submitted sitemaps and their processing status.
- Page indexing reports.
- Indexed and non-indexed page counts.
- Reasons for page exclusions.
- Crawl statistics.
- URL Inspection results.
- Google-selected canonical URLs.
- User-declared canonical URLs.
- Server errors.
- Redirect errors.
- Soft 404 errors.
- Duplicate content warnings.
- Discovered but currently not indexed pages.
- Crawled but currently not indexed pages.
- Pages blocked by robots.txt.
- Pages excluded by noindex directives.
- Manual actions.
- Security issues.
- Core Web Vitals.
- Structured data and enhancement reports.
- HTTPS reports.
- Internal and external link reports.
- Organic search performance.

Investigate whether any indexing exclusions are intentional, migration-related or indicative of genuine technical problems.

Use URL Inspection and live testing for important pages, representative examples of every page template, and individual URLs exhibiting indexing problems.

Compare Google's understanding of the website against the intended architecture of the new website.

Where appropriate, identify URLs that would benefit from an indexing request after technical issues have been resolved. Respect Google's submission limits and avoid unnecessary repeated requests.

## 5. Bing Webmaster Tools Investigation

Access Achology's actual Bing Webmaster Tools property and undertake an equivalent investigation.

- Verify property ownership and configuration.
- Review sitemap submission and processing.
- Investigate indexed and non-indexed pages.
- Use URL Inspection and Site Explorer.
- Review crawl errors and indexing problems.
- Review SEO reports and recommendations.
- Investigate backlink information and historical URLs.
- Review organic search performance.
- Identify discrepancies between Google's and Bing's understanding of the website.
- Assess whether IndexNow is correctly implemented or would be beneficial.
- Ensure any IndexNow implementation appropriately notifies participating search engines about newly published, updated and removed content.

## 6. Search Engine Crawling and Accessibility

Investigate whether legitimate search engine crawlers can reliably access and understand the website.

- Validate robots.txt.
- Inspect meta robots directives and X-Robots-Tag HTTP headers.
- Identify accidentally retained staging or development restrictions.
- Verify that important content is accessible without authentication.
- Check whether hosting, firewall, CDN or security configurations inadvertently restrict legitimate crawlers.
- Investigate DNS, SSL certificate and HTTPS configuration.
- Check server response codes and reliability.
- Confirm that important page content is available to search engines.
- Investigate JavaScript rendering dependencies.
- Confirm that navigation and internal links are discoverable by crawlers.
- Check mobile rendering and mobile-first indexing compatibility.
- Review available server logs for legitimate Googlebot and Bingbot crawling activity.
- Investigate crawl inefficiencies, duplicate URL generation and potential crawl traps.

## 7. Canonical URL and Duplicate Content Validation

- Confirm that every indexable page declares the correct canonical URL.
- Verify that canonical destinations return HTTP 200 and are indexable.
- Identify conflicting canonical signals between the website, sitemap, internal links and search engines.
- Check whether URL variations create duplicate content.
- Investigate query parameters, pagination, filtering and search-generated URLs.
- Identify duplicate pages that could compete against each other in search results.
- Verify that canonicalisation is implemented consistently across all website templates.
- Validate hreflang implementation if applicable.

## 8. Website Architecture and Internal Linking

- Audit the website's internal linking structure.
- Identify broken internal links.
- Identify links pointing to outdated or redirected URLs.
- Check that important commercial and educational pages are readily discoverable.
- Identify orphaned or unnecessarily deeply nested pages.
- Verify breadcrumb navigation.
- Review navigation consistency across desktop and mobile.
- Assess relationships between schools, courses, articles and other educational content.
- Investigate whether internal linking appropriately distributes existing search authority throughout the website.
- Identify structural weaknesses that could limit future organic growth.

## 9. On-Page Technical SEO

Review all indexable pages and website templates for:

- Missing, duplicated or inappropriate page titles.
- Missing or duplicated meta descriptions.
- Incorrect or missing primary headings.
- Illogical heading hierarchies.
- Incorrect canonical tags.
- Missing or inappropriate image alternative text.
- Empty, incomplete or accidentally duplicated content.
- Incorrect language declarations.
- Broken images, videos and embedded resources.
- Incorrect social sharing metadata.
- Inconsistent page metadata generated by reusable templates.
- Any technical issue that could prevent search engines from accurately understanding page content.

Pay particular attention to problems introduced during the migration from the previous website.

## 10. Structured Data and Entity Validation

Investigate the implementation and accuracy of structured data throughout the website.

Review the appropriateness of:

- Organisation schema.
- Website schema.
- Educational organisation schema.
- Course schema.
- Product and offer schema, where applicable.
- Article schema.
- Person and author schema.
- Breadcrumb schema.
- Video schema.
- Event schema, where applicable.
- FAQ schema, where appropriate.

Check structured data against current Google, Bing and Schema.org guidance.

Validate implementation using appropriate testing tools, including Google's Rich Results Test and Schema Markup Validator.

Ensure structured data accurately represents visible page content, does not contain misleading information and is not implemented solely on the assumption that it guarantees rich search results.

Investigate whether Achology's organisational identity, educational offering, authorship and brand relationships are communicated consistently across the website.

## 11. Website Performance and Technical User Experience

Investigate the performance of the live website across representative page types on desktop and mobile.

Review:

- Largest Contentful Paint.
- Interaction to Next Paint.
- Cumulative Layout Shift.
- Server response times.
- Page loading behaviour.
- Image optimisation.
- JavaScript and CSS efficiency.
- Caching and compression.
- Font loading.
- Third-party scripts.
- Video embeds.
- Mobile responsiveness.
- Broken or obstructive interactive elements.

Use Google PageSpeed Insights, Lighthouse, Search Console Core Web Vitals data and other appropriate diagnostic tools.

Distinguish laboratory test results from actual user performance data.

Prioritise systemic template or infrastructure improvements over isolated page-level corrections.

## 12. Historical Search Authority and Backlink Preservation

Investigate whether the migration has compromised Achology's existing organic search authority.

- Identify historically valuable landing pages.
- Identify pages with significant external backlinks.
- Check whether these URLs remain accessible or redirect appropriately.
- Investigate lost or broken backlinks.
- Compare historical and current organic landing pages.
- Identify formerly high-performing content that may have disappeared, changed substantially or become inaccessible.
- Review whether historical titles, content, search intent and keyword relevance have been unnecessarily compromised.
- Identify pages requiring particular attention because of their historical commercial or organic search value.

Prioritise the protection of established search visibility rather than focusing exclusively on newly published content.

## 13. Independent Search Engine Verification

Conduct independent searches using Google and Bing to investigate how Achology is currently represented.

- Search for Achology-branded terms.
- Investigate the visibility of important course and school pages.
- Check representative historical URLs.
- Investigate whether obsolete pages continue to appear in search results.
- Review displayed titles, descriptions and destination URLs.
- Check for unexpected development URLs or duplicate domains appearing in search results.
- Investigate important discrepancies between live website content and search engine representations.

Use search engine results as supporting evidence, not as a substitute for authoritative indexing reports.

Do not use the results of a site: search as a definitive measurement of indexing coverage.

## 14. Analytics and Search Performance Validation

Where the relevant systems are available:

- Confirm that Google Analytics is correctly installed.
- Confirm that tracking is functioning across the new website.
- Check for duplicate tracking implementations.
- Verify that consent mechanisms function appropriately.
- Confirm that important commercial conversion events remain operational.
- Verify attribution across relevant website and checkout journeys.
- Review organic impressions, clicks, click-through rates and average search positions.
- Compare pre-launch and post-launch performance.
- Establish whether any apparent decline is attributable to migration, reporting delays, seasonality, tracking changes or genuine technical problems.
- Establish a reliable post-launch performance baseline.

## 15. AI Search and Generative Engine Discoverability

As a secondary extension of the technical SEO investigation, assess whether Achology is appropriately accessible to relevant AI-powered search and discovery platforms.

- Review crawler accessibility for relevant AI search services.
- Distinguish AI search discovery crawlers from model-training crawlers.
- Verify consistency of organisational and educational information.
- Assess the machine readability of educational content.
- Review content structure, authorship, attribution and entity relationships.
- Identify technical obstacles that could prevent Achology's content from being discovered, understood or referenced.
- Identify any evidence-based improvements relevant to AI search visibility.

Do not introduce experimental technologies, unnecessary files or speculative optimisation techniques without establishing their practical value.

## 16. Independent Technical Investigation

The preceding checklist is not intended to limit your investigation.

Use your knowledge of the website's architecture, development history and technical implementation to identify anything else that may compromise:

- Search engine discoverability.
- Crawling and indexing.
- Historical search authority.
- Organic search performance.
- Website accessibility.
- Technical reliability.
- Future scalability.
- Sustainable content publishing.

Consult current official documentation wherever necessary.

Investigate potential problems rather than simply confirming that expected configurations exist.

Where a problem is identified, establish its underlying cause, affected scope, commercial implications and most appropriate resolution.

## 17. Findings and Remediation Plan

Produce one consolidated report containing:

- An executive summary of the website's overall technical SEO health.
- A complete inventory of intended indexable URLs.
- Sitemap coverage and accuracy.
- Historical URL and redirect coverage.
- Confirmed redirect failures.
- Google indexing status.
- Bing indexing status.
- Legitimate indexing exclusions.
- Unexpected indexing exclusions.
- Technical crawling and accessibility issues.
- Historical search authority risks.
- Structured data issues.
- Performance issues.
- Additional findings from your independent investigation.

Classify all findings as:

- **Critical:** Immediate risk to accessibility, indexing or established search visibility.
- **High:** Material technical or commercial risk requiring prompt correction.
- **Medium:** Meaningful improvement that should be scheduled.
- **Low:** Minor optimisation or housekeeping.
- **Monitoring:** No immediate correction required, but future observation is necessary.

For every identified issue, provide supporting evidence, affected URLs, underlying cause, recommended resolution and a clear method of verifying that the correction has worked.

Distinguish verified facts from assumptions, normal migration-related delays and findings requiring further investigation.

Identify systemic problems and prioritise correcting their underlying causes rather than repeatedly correcting individual symptoms.

## 18. Corrective Work and Revalidation

Following the initial investigation:

- Present the findings and prioritised remediation plan.
- Identify straightforward, low-risk corrective actions separately from changes requiring approval.
- Preserve existing website functionality, design and commercial systems.
- Ensure that appropriate backups and rollback mechanisms exist before making production changes.
- Obtain approval before implementing material changes.
- Following implementation, repeat the relevant tests against the live production website.
- Validate corrected sitemaps and redirects.
- Submit updated sitemaps where appropriate.
- Use available search engine validation and indexing mechanisms appropriately.
- Record outstanding issues that depend on subsequent search engine recrawling or processing.
- Produce a final verification report showing what has been resolved and what remains outstanding.

Do not consider a problem resolved merely because the code has been changed. Verify the actual production behaviour.

## 19. Ongoing Automated SEO Protection

Develop a practical, low-maintenance strategy to prevent future technical SEO regressions.

Investigate how our existing infrastructure can automatically:

- Maintain accurate XML sitemaps.
- Detect missing or incorrect sitemap entries.
- Protect historical redirects.
- Detect broken internal links.
- Detect redirect chains and loops.
- Identify broken or inaccessible pages.
- Identify incorrect canonical URLs.
- Detect accidental noindex directives.
- Validate structured data.
- Identify significant website performance regressions.
- Monitor search engine indexing discrepancies.
- Detect unexpected reductions in organic search visibility.
- Validate new pages before or immediately after publication.
- Run essential technical SEO checks before future website deployments.

Establish which checks can be automated, which require periodic review and which genuinely require human intervention.

Prioritise existing infrastructure and open-source solutions over unnecessary recurring software subscriptions.

Recommend an appropriate monitoring schedule covering the immediate post-launch period, the next 90 days and ongoing website maintenance.

## Final Operating Instructions

I want you to approach this exercise as a senior technical SEO specialist, website migration consultant and independent quality assurance engineer.

Do not merely review the codebase or tell me what should theoretically be correct. Access the actual systems, inspect the live website, examine Google Search Console and Bing Webmaster Tools directly, conduct independent tests and gather supporting evidence.

Use the access and historical information already available to you. Resolve investigative dependencies independently wherever possible. Only involve me when a genuine blocker or material business decision requires my intervention.

Do not assume that the website is technically correct because we built it together. Approach it objectively and actively investigate potential weaknesses.

Do not claim complete historical URL coverage or successful indexing without sufficient evidence. Where information is incomplete or search engine processing is ongoing, explain the limitation and establish how it will be monitored.

Our ultimate objective is to establish a technically verified, search-engine-friendly website that protects Achology's historical organic search authority, supports future growth and remains technically reliable as we continue expanding its content and functionality.
