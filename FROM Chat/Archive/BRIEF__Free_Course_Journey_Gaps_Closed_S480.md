CODE DISPOSITION, S559: DONE, the Help answer published as post 47660 by Branch G and the TEST claim sent; answered in DONE__Free_Course_Help_Answer_Published_S559.md
For Code's main session (S552), a launch job for one branch. What this needs: close five gaps Chat found tracing the annual member's free course journey end to end on the build site today.

Done when each of the five items below is built or proved, and a DONE in TO Chat gives the theme version, the posts changed, and the mail check's printout.

# BRIEF: the free course journey, five gaps closed (Chat, Session 480, 23 November 2026)

Model and effort: Opus 5.5, xhigh. The branch asks Kain nothing. Chat traced: the Membership page's annual card, the Pricing page, the Circle redirect plan, /membership/choose-your-free-course/, course-gift.php, the two emails, Karen's step, and every Help answer that speaks of the plans.

## 1. The emails must arrive (the one that can break the whole journey)

course-gift.php sends Karen's alert and the member's confirmation with wp_mail from the host. achology.com's SPF reads `v=spf1 ip4:192.168.0.0/16 include:_spf.google.com include:mail.zendesk.com ~all`: it does not name SiteGround's sender, so once the domain moves, mail from the site as achology.com is likely to land in spam or be refused, and Karen never hears of a claim. achologytest.com's own SPF does include SiteGround (`include:achologytest.com.spf.auto.dnssmarthost.net`).
- Before launch: read which From address and which route wp_mail uses on the build site, and write it in the DONE.
- In the switch (checklist B3): achology.com's SPF gains SiteGround's sender for the new plan, and the new plan's DKIM key is in the zone. Add both lines to the checklist and the Go-Live Steps.
- After the switch, before the Circle redirect goes on: one claim through the build ground's TEST route, or the live form marked TEST, reaches Karen's inbox and a member test inbox, in the inbox, not spam. If it does not, stop and tell Chat; a sender route through Google Workspace is then the fix.
- The same applies to every form that emails from the site (enquiries, the Roundup request). List them.

## 2. The Pricing page never mentions the free course

Its Annual Membership card says only "Two months free against twelve monthly payments". Add the Membership page's own signed line above the button, word for word: "And We'll Gift You a Course Worth $97". Same type and place as on /membership/.
PAGE GATE: pricing, one signed line reused from /membership/ on the annual card, ruled by Chat S480.

## 3. "Masterclass" on the Pricing questions

The Pricing page's short answer for "How do monthly and annual Achology memberships differ?" ends "includes every workbook and a masterclass for life". Kain does not want the word masterclass written. Make it read "includes every workbook and a course for life", as the Membership page already does.

## 4. Two Help answers say the plans are the same (Chat's words, placed word for word)

**/help/pricing-and-payments/difference-between-monthly-annual-achology-membership/**
- Short answer (excerpt), replace whole: "Annual adds every workbook and one course of your choice, yours for life, and costs $69 less than twelve monthly payments."
- First paragraph, replace whole: "Choosing between monthly and annual Achology membership comes down to how you'd like to pay and what you'd like included. Both plans open the same community, with its daily live events, peer practice and discussion spaces. The annual plan adds every workbook in the library and one course of your choice, yours for life, and costs $69 less than twelve monthly payments."
- Replace "Annual is paid once for a full year, and neither plan hides anything from the other, so the annual plan doesn't unlock any extra community spaces or live events." with: "Annual is paid once for a full year. It opens no extra community spaces or live events, but it adds every workbook and a course to keep."
- Replace the last line "If you're unsure, the monthly plan is the gentler start, and Achology Gateway is gentler still." with: "If you're unsure, the monthly plan is the gentler start, and the free events and the Knowledge Hub cost nothing at all."

**/help/membership-and-access/what-does-achology-membership-include/**
- After "and each course purchase carries three months of membership." add: "On the annual plan, membership also brings every workbook in the library and one course of your choice, yours for life."

Change each in its record and re-push, so a later import does not undo it.

## 5. Achology Gateway is still named

The free Circle tier ended (Kain, 11 November; sweep signed S469), but the plans answer above still names Achology Gateway. Search every published post, Help answer and theme file for "Gateway" (the tier, not other uses) and list each in the DONE. Do not rewrite them: Chat writes the words the same hour.

## Also on the checklist (B9, launch day)

When Kain sets Circle's annual redirect to /membership/choose-your-free-course/, also add that address to the annual member's welcome message in Circle, so a member who closes the tab can find the page again. Code guides Kain one step at a time.

**Not now, on Kain's word only:** publishing the new Help answer DRAFT__Help_Answer_Choose_Free_Course_Annual_Membership_S549 (checked correct by Chat today), and any TEST email sent to Karen's inbox before the switch. Chat sends a line when Kain says yes.

OWED BACK: the DONE above.

DOCUMENT TYPE: brief.

*No em or en dashes in this file; checked before writing.*
