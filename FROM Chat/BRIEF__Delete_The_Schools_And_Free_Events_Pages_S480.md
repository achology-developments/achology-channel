For Code's main session (S552), one small launch job for a branch. What this needs: remove two unused pages, on Kain's word, with nothing left pointing at them.

Done when the WordPress pages "Schools" (/academy/schools/) and "Free Events" (/free-events/) are in the WordPress trash, /academy/schools/ answers one 301 to /academy/ and /free-events/ one 301 to /events/, no published post, page, theme file, menu or sitemap links either old address, and a DONE in TO Chat lists every link changed.

# BRIEF: delete the Schools and Free Events pages (Chat, Session 480, 23 November 2026)

Model and effort: Opus 5.5, xhigh. The branch asks Kain nothing.

**Kain, today:** "we have a page called Schools that isn't going to be getting used anymore. So we need that safely deleted and removed. Make sure it's not linked to any other page ... We've got a page called Free Events, and we've got a page called Events. Events is the page that's ranked, and Free Events is not going to be getting built. So we need those two pages to get deleted and removed as well."

**Order, so nothing breaks:**
1. Change every link first. From Chat's sweep today: /academy/schools/ is linked from the refund policy (policies-content/refund-policy.php), about 35 Help answers and one article (already in ANSWER__Gate_Lines_And_Open_Rulings_S480 section 9); /free-events/ from page-about.php, template-policy.php, policies-content/manifesto.php and the Help answer where-should-i-start-with-achology. Point each to /academy/ (or the one school's own page where the sentence names a single school) and to /events/. Search again after; list anything else.
2. Redirects: one 301 each, as above, in Rank Math and Redirect_Master.xlsx. Repoint any older row that led to either address, so nothing goes two hops.
3. Move both pages to the WordPress trash (not a permanent delete, so they can be restored if ever needed), through publish_gate.py --retire.
4. Regenerate the sitemap and confirm neither address is in it.

Chat changes the same two links in the Kit emails itself (the Roundup welcome email links /free-events/; the email footers link /academy/schools/).

OWED BACK: the DONE above.

DOCUMENT TYPE: brief.

*No em or en dashes in this file; checked before writing.*
