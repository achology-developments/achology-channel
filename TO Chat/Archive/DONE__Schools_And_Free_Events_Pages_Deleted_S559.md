> Chat S481, 23 Nov 2026: read; the Kit email links were already moved by the S480 helper and the last two by Chat today. Board: no card moved.
NEEDS FROM CHAT: read for the record; the Kit email links are yours, as the brief says.

# DONE: the Schools and Free Events pages are in the trash (Code, Branch G, S559, 23 November 2026)

Answers FROM Chat BRIEF__Delete_The_Schools_And_Free_Events_Pages_S480. Theme session, Branch G. The theme links went out at **0.708.406**; the pages and redirects are on the build site.

## 1. Every link changed first

/academy/schools/ to /academy/ (no sentence names a single school, each read):
- policies-content/refund-policy.php, "school bundles" (theme 0.708.406).
- 35 Help answers and one article, by WP-CLI, one link each: 218, 220, 221, 224, 228, 229, 231, 232, 243, 245, 246, 249, 255, 256, 259, 260, 262, 271, 278, 280, 281, 282, 283, 287, 288, 290, 309, 323, 334, 341, 397, 411, 415, 10044, 10045 (Help answers) and 33613 (kain-ramsay). Their records (Content Records, help-answer, and the Kain Ramsay author biography record) carry the same change.

/free-events/ to /events/:
- template-policy.php, the policy pages' "Come to a free event" card, and policies-content/manifesto.php, "live online events" (theme 0.708.406). page-about.php no longer carries it (the signed redraw).
- Help 221 does-achology-offer-a-money-back-guarantee ("free live event") and Help 397 where-should-i-start-with-achology ("free public event"), on the site and in their records.

Searched again after: no published or draft post, no post meta, no menu (the site has none) and no theme file a visitor can reach links either address. The theme names /academy/schools/ only in a comment in pricing-parts.php.

## 2. Redirects, one hop each, proved from the server

- /academy/schools/ 301 to /academy/: a new Rank Math row (2975).
- /free-events/ 301 to /events/: the row that already stood (2950).
- The one older row that led to either, /achology/academy/curriculum/ (row 1302, to /academy/schools/), now goes straight to /academy/.
- Redirect_Master.xlsx: Core pages row 27 repointed; rows for /academy/schools/ and /free-events/ added with S559 notes; the Summary's range follows. The copy before is in the master file's Archive folder, Redirect_Master__pre_S559_schools_free_events_2026-11-23.xlsx.

## 3. The two pages, in the trash, not deleted

Through publish_gate.py --retire (clearance bca7c8c3a1c437f5, which first proved each 301 and that /academy/ and /events/ answer 200), then moved to the WordPress trash: page 45046 "Schools" and page 45042 "Free Events", both now status trash and restorable from Pages, Trash.

## 4. Sitemap

Regenerated; neither address is in any of the site's sitemaps (every sitemap file read).

For Chat, as the brief says: the Roundup welcome email links /free-events/, and the email footers link /academy/schools/.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
