CODE DISPOSITION, S559: WAITS ON Kain making a host outside SiteGround (a public GitHub repository with Pages, or a SiteGround support exemption), asked of the main session; finding and inventory in REPORT__Email_Images_Need_A_Host_Outside_SiteGround_S559.md
For Code's main session (S552), urgent, one branch. What this needs: every picture our Kit emails show must load for email programs, which today often get SiteGround's robot check instead of the picture.

Done when each address below answers 200 with an image type (not 202 text/html) to `curl -A "GoogleImageProxy"` and to `curl -A "Mozilla/5.0 (Windows NT 10.0) Outlook"`, and a DONE in TO Chat gives the final addresses for Chat to place in every Kit email.

# BRIEF: email pictures must load past the robot check (Chat, Session 480, 23 November 2026)

Model and effort: Opus 5.5, xhigh. The branch asks Kain nothing.

**Kain's report:** the logo comes through in some Kit sequences and not in others.

**Chat's finding (curl, 13:50 UK today):** all ten Kit sequences (44 emails) take their logos from `https://achologytest.com/wp-content/uploads/2026/06/Achology-Brand-Logo-Orange-Grey.png` and `.../Achology-Brand-Logo-White-White.png`, and their fonts from `https://achologytest.com/wp-content/themes/achology/fonts/`. Fetched as Google's image proxy or as Outlook, both logos answer **202 text/html, 237 bytes**: SiteGround's robot check (`/.well-known/sgcaptcha/`), not the picture. achology.com answers the same way today. So whether a reader sees the logo depends on whether their email program's fetch is let through, which is why it is patchy.

**The job:**
1. Make the pictures emails use load for any fetcher, without the robot check, on the build site now and on achology.com after the switch. Your call how: a path the bot check skips, SiteGround's CDN, or a static host outside SiteGround. Never turn the bot check off for the whole site.
2. Cover every picture an email uses, not only the two logos: the workbook covers (`subscriber.workbook_cover`), the teaching and lesson stills (`subscriber.teaching_n_still` and the course lesson equivalents) and any other image the Kit custom fields point to. List where each lives today.
3. Give Chat the final address for each logo. Chat updates every Kit email the same hour. If the custom fields' values must change, change them at the source that fills them and say so.
4. Add one line to the launch checklist section A: "Every email picture answers 200 image to the email fetch test".

OWED BACK: the DONE above, with the curl printout for each address.

DOCUMENT TYPE: brief.

*No em or en dashes in this file; checked before writing.*
