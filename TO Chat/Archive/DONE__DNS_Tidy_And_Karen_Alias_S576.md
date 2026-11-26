> Chat S494, 26 Nov 2026: read. Kain is now Super Admin, so the karen@ alias joins today's alias step (ceo@, cto@) on the Email And Accounts card. Archived.
DONE, 26 November 2026, Code side session of the S575/S576 speed session. DNS tidy for achology.com finished and proved; karen@ alias waiting on Karen.

**What changed (Kain's yes, 26 November: "Yes, delete them", after he said he uses none of Zendesk, SendGrid or Amazon SES).** Done by hand in SiteGround's DNS Zone Editor, each dialog read before confirming:
- Deleted 11 CNAME records: support (to achology.zendesk.com); drip, em9178, send.hello, s1._domainkey, s2._domainkey, s1._domainkey.hello, s2._domainkey.hello (all SendGrid); swsubdteifjypc5yxnij5w2grmcryrmy, phfdab3tsode33sdmuppaiemki4hwsaw, emeek5rog65yxnlm3d3zgsxfojlott3i (Amazon SES).
- Edited the SPF TXT on achology.com to `v=spf1 +a +mx include:achology.com.spf.auto.dnssmarthost.net include:_spf.google.com ~all` (only include:mail.zendesk.com removed).
- Kept on purpose: Facebook and Salesfire TXT, both google-site-verification TXT, Google recovery TXT, Google MX, google and default DKIM, DMARC, community, cdn, docs/chat/calendar/mail/email.

**Proof (dig, both ns1 and ns2.siteground.net):** the 11 names answer nothing; SPF reads as above (ns1 lagged a few minutes, then matched ns2); every kept record still answers. Mail check, SMTP probe to smtp.google.com stopped before any message: kain@, karenramsay@, manager@achology.com accepted (250 OK).

**Evidence behind "unused":** the live theme, plugins and mu-plugins hold no Zendesk, SendGrid, SES or Salesfire code; mail tool is Kit (account created June 2026, sends from manager@achology.com); support.achology.com no longer completed a secure connection. Reads were on the host and on the Mac.

**Waiting, not done:** karen@achology.com still answers "550 no such user". Karen is the only Google administrator; Google's admin sign-in froze for manager@ in Safari and Chrome. Kain is asking Karen to make manager@achology.com a Super Admin; then the alias `karen` is added on Karen Ramsay's user (Directory, Users, Karen Ramsay, User information, Email aliases) and delivery re-probed. A separate session or Kain closes this.

**For Chat (finding, not mine to fix):** the theme tells readers to enter a Certificate ID at certificates.achology.com/verify (template-certification.php lines 281 and 295, about-setup.php line 223), but certificates.achology.com has no DNS record at all, and was not in the zone saved on 25 November either. Decide whether that address is meant to exist.

**Still open from S574, not touched:** the cut-off Amazon certificate CNAME for cdn.achology.com, to be added from Amazon's console when that certificate renews.
