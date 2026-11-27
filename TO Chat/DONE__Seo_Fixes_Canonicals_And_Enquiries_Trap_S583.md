> CODE DISPOSITION, S583: DONE. Answers REPORT__Post_Launch_SEO_Validation_S583 findings 1 and 2, on Kain's "Yes, apply them".
For Chat: what this needs: nothing, except the sitemap choice for the list pages (the report's finding 2) when you and Kain decide.

# DONE: the /enquiries/ crawl trap closed and a canonical on every Knowledge Hub list page (Code, theme 0.708.519)

Deployed and proved on the live site with fresh addresses, one request a second.

- **/enquiries/ with a query string** (the Spotted a Mistake address): `<meta name="robots" content="follow, noindex"/>` and `<link rel="canonical" href="https://achology.com/enquiries/" />`. Proved on /enquiries/?topic=correction&page=<an article address>&z=1. The clean /enquiries/ still reads `follow, index` with its own canonical.
- **The Spotted a Mistake link** on every Knowledge Hub page now carries `rel="nofollow"` (read on the live Abraham Maslow article).
- **Hub list pages:** /learn/, /learn/psychology/articles/ and a numbered list page (/learn/psychology/workbooks/page/2/) each print one canonical naming themselves, `follow, index` as before; /learn/ and the article list were checked for a single canonical tag. The thank-you page is left alone; a sort or query string on a list now names the clean address.
- **Files:** knowledge-hub-setup.php (`achology_kh_virtual_canonical`), enquiries-setup.php (canonical and both robots filters), knowledge-hub-parts.php (nofollow), style.css (version).
- **Not changed, for your and Kain's word:** whether the list pages join the sitemap (the report recommends yes). The authority for this DONE is TO Chat RULING__Kain_Yes_Apply_The_Low_Risk_Seo_Fixes_S583.

OWED BACK: your word on the sitemap choice for the list pages.

*No em or en dashes in this file; checked before writing.*
