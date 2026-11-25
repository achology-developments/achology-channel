For Chat: what this needs: read it; it is the launch day record, written as each step is proved. Nothing asked of Chat yet.

Done when: every section B step below carries its proof and time.

**DOCUMENT TYPE:** done from Code, S574 (main launch session, Opus), 25 November 2026. Theme 0.708.491 on the build site.

## Section A, closed

- **A1 gate map:** 41 of 82 fail (REPORT__Launch_Section_A_Checks_S572). Eleven are the orange Achology word in headings (Academy, seven schools, Access All Areas, Membership, Disclaimers; gate rows achology-word-1000 and -375, read by page_gate on /academy/, /policies/disclaimers/, a school and /membership/). **Kain, 21:40, in his words: "I don't care. Let's pick that up post-launch."** The other 30 are record lines and stored scores (17 profiles and /about/instructors/, nine older pages), Home's schema and speed rows, the /home/ draft and the Centre page.
- **A2 redirects: PASS.** The 93 "ruled" rows: dry run read 92 already on the server, now marked verified in Redirect_Master; the 93rd, /publications/fdsfds/ to None, is junk and refused. The coverage check's 38 missing old addresses (7 quotes, 30 author archives, 1 product category), on Kain's "Just do it right now": written by `publish_gate.py --write-redirects-from`, "proved 38 of 38 written; 0 not proved", added to Redirect_Master. Quotes go to the author's biography where the map already does so, else /learn/quotes/; authors with a profile to it (alec-wells, andrew-nelson, gabriele-tzeschlock to gaby-tzeschlock, karen to karen-ramsay), the rest to /about/instructors/; the NLP product category to /academy/neuro-linguistic-programming/. Then `redirect_one_hop.py`: "0 faults across 2636 rows"; `redirect_chain_register.py --report`: "504 of 504 destinations carry all five. 0 have an incomplete chain."
- **A3:** `cutover_gate.py` plain, exit 0, hidden as designed (S574 run).
- **A4:** backup on the Mac re-listed (sizes match the A4 proof); DNS of achology.com read from ns1.siteground.net and saved beside it as dns_achology_com_before_move.txt. The iCloud copy was still uploading at 21:00.
- **A5, A6, A8, A9:** pass (section A report).
- **A7:** passed at S566 (DONE__A7_Kit_Subscriber_Pictures_Moved_S566_Branch_A7); not re-run, the test cannot run from this Mac.
- **Accessibility Statement:** placed at 0.708.491 by the home-gate helper; its date is set again on the day (day-of step for the checklist).
- **Kain, on Site Health:** the opcode cache and Memcached go on straight after the move ("Yes, after the move").

## Section B

- **B1 freeze, 21:20:** Kain's "Yes, start the switch"; the old site takes no edits from now (it takes no payments).
- **B2 DNS zone kept, 21:25:** Kain's six screenshots of the DNS Zone Editor (every record, after Load More) saved in "Achology Old Site Backup 25 November 2026/DNS screenshots"; every named record also read in full from ns1.siteground.net into dns_achology_com_before_move.txt beside the backup. Note: achology.com and www are SiteGround CDN records on the old site; ssh, ftp, autodiscover and autoconfig point at the old server 35.214.126.15; test.achology.com points at the new server 35.214.30.153. The iCloud copy of the backup read as uploaded at 21:27 (no file pending).
- **B11 old site deleted, 21:32:** Kain's "yes", then Confirm on SiteGround's Delete Website achology.com page ("Your website achology.com has been successfully deleted from your plan Hosting Plan"). **Finding, 21:33:** the delete took achology.com's whole DNS zone with it: ns1 and ns2.siteground.net now answer REFUSED for achology.com (the .com registry still names them), so no MX, no A, no Google records answer. Mail to the domain is delayed (senders retry) until the zone is back. Every record is held in the saved copy.
- **Before B2, 21:35:** the build site's database exported on the host and copied to the Mac (achologytest-before-domain-change-2026-11-25.sql.gz, 33,925,960 bytes, gzip clean), because SiteGround's Change Primary Domain warns earlier site backups are lost.
- **B2 Change Primary Domain, 21:37:** Kain pressed Confirm and Continue; SiteGround: "Your new primary domain for the website is achology.com". The site folder on the host is now ~/www/achology.com/public_html; siteurl and home read https://achology.com. Dry run of the stored address change (posts, postmeta, options, guid skipped): **1,975** (postmeta 1,971, options 4, posts 0). SiteGround's change had already rewritten the post bodies and most options (S568 dry run read 4,438: posts 2,242, postmeta 1,976, options 220). At 21:38 SiteGround's name servers still answered nothing for achology.com.
- **B3 the new zone, 21:39:** SiteGround's name servers answer a fresh default zone: achology.com and www A 35.214.30.153 (the new site's server), MX mx10/20/30.antispam.mailspamprotection.com (SiteGround mail, wrong for Google Workspace), SPF "v=spf1 +a +mx include:achology.com.spf.auto.dnssmarthost.net ~all". None of the saved Google, SendGrid, Amazon SES, Zendesk or Circle records exist. Restoring from the saved copy, MX first.

*No em or en dashes in this file; checked before writing.*
