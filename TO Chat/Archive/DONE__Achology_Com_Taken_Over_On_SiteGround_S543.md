> Disposition, Chat S480, 23 Nov 2026: record; the move order is answered in Chat's S480 answer to the switch-over checklist; archived. No board card moved.

# DONE: achology.com taken over on SiteGround (S543, 20 November 2026)

**What changed.** The old live site, achology.com, now sits in Kain's own SiteGround account, and Code has SSH and WP-CLI access to it (key "claude-code"). This is the old site, not the build site; the build site stays on achologytest.com. No theme ship and no version number: none of this touches the achology theme.

**What Code did tonight, on Kain's word each time:**
1. **Brought the site back.** Every page gave error 500 after the move: `.user.ini` told PHP to load Wordfence's firewall from the previous account's home folder. Repointed to SiteGround's portable path, `/home/customer/...`. Verified live in a browser.
2. **Access tidy.** Kain removed three outside SSH keys (pooka-paul, ivan.shindin@hugeturtle.com, andrei@andrei-lnx). Kept: pooka-marcus and Pooka Remote (Pooka is the support company), SiteGround's three, and Code's.
3. **Speed tidy.** Full database backup first (server, `~/db-backups/`). Cleared 3,486 expired transients and 13,724 old Action Scheduler rows; capped revisions at 3; Memcached switched on (Kain in Site Tools, Code in WordPress). The 814 MB database is real content, not clutter.
4. **A daily crash stopped.** The child theme scheduled a subscription reminder that called WooCommerce Subscriptions, no longer installed; both functions now check for the plugin first. Original kept on the server.
5. **Plugins.** All were up to date. Google Listings & Ads deactivated; three inactive plugins deleted. WooCommerce stays: the old theme's menus and shortcodes depend on it. The old site takes no payments; Circle does.

**Anything needed from Chat.** One thing, when Kain wants it: the rollout plan from the finished build to achology.com. With the domain and hosting now in Kain's own account, the move is ours to plan.
