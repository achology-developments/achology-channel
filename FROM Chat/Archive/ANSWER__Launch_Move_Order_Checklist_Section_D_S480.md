CODE DISPOSITION, S559: DONE, written into the checklist by Branch G (section D, A4, B2, B3, B11); answered in DONE__Launch_Move_Section_D_Filled_S559.md
For Code's main session (S552) and Branch B. What this needs: fill section D of CHECKLIST__Launch_Switch_Over_S553 from the rulings below, and set B2, B3 and B11 to match.

Done when the checklist names one method and one order, and the database search in ruling 5 is run and reported.

# ANSWER: the launch move, section D ruled (Chat, Session 480, 23 November 2026)

The order of the move is now written into PLAN__Rollout_From_Build_Site_To_Achology_Com (Project Delivery System folder), section "The order of the move". It follows SiteGround's two written answers of 22 November (SiteGround Support Answer 22 November 2026, same folder). Read that section; this file is the short form.

1. **The method.** No copy of the build install is made anywhere. SiteGround support moves the domain achology.com from the old hosting plan to the build site's plan (achologytest.com) and makes it that plan's primary domain, in one change they perform, booked by Kain for the launch hour. B2 reads that way. B3 adds: SSL Manager shows the certificate (it can take up to 72 hours to reissue), the DNS zone is compared with the copy exported before the move, Google Workspace mail is tested both ways, and the site cache is cleared and warmed.
2. **achologytest.com after the move.** Every achologytest.com address answers with a 301 to the same path on achology.com. It is never left open as a second copy of the site.
3. **The old install.** It moves to a temporary address on its own plan before the switch, behind no public link, and stays one fallback week. Then Kain cancels only the old hosting plan. The domain and its DNS records are never deleted. The full backup of A4 is kept after the plan is cancelled, on Kain's machine as well as the server.
4. **Email records.** The DNS zone lives with the domain, not the plan, so SPF and DKIM do not change. Export the zone before, compare it after. The SPF and DKIM tidy is after launch.
5. **Stored build-site links.** Before the day, search the build site's database and theme for achologytest.com and replace each with achology.com at the switch (a search and replace run as part of B2, read back). For Kit and Circle, guide Kain one step at a time through their forms, emails and settings; list what you find first.

Calls Chat made that Kain may overturn: the 301 for achologytest.com, and keeping the old site one week.

OWED BACK: one line when section D is filled, and the count from the search in ruling 5.

DOCUMENT TYPE: answer.

*No em or en dashes in this file; checked before writing.*
