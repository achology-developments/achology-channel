NEEDS FROM CHAT: two things. (1) Write the signed field on HELP__choose-free-course-annual-achology-membership.md through your signing road (Kain's yes is RULING__Publish_Free_Course_Answer_And_Test_Claim_S480), so Code can import and publish it. (2) Reconcile section D ruling 4 (SPF and DKIM do not change) with the journey brief's B3 line (SPF gains SiteGround's sender; DKIM added); both are now written in the checklist.

# DONE, two items waiting: the free course journey, five gaps (Code, Branch G, S559, 23 November 2026)

Answers FROM Chat BRIEF__Free_Course_Journey_Gaps_Closed_S480, RULING__Publish_Free_Course_Answer_And_Test_Claim_S480 and ANSWER__Gateway_Words_Replaced_In_Seven_Help_Answers_S480. Theme session, Branch G. **Theme 0.708.404**, commit on main "Pricing questions: ... a course for life", deployed and proved by deploy.py.

## 1. The emails

- **Read on the build site:** wp_mail sends From `wordpress@achologytest.com`, name "WordPress" (WordPress's default; no theme filter and no mail plugin changes it), through the host's own sendmail (`/usr/sbin/sendmail -t -i`). After the switch the same code sends From wordpress@achology.com. Karen's alert carries Reply-To the member; the member's confirmation carries Reply-To Karen Ramsay <karenramsay@achology.com>.
- **The TEST claim (Kain's yes):** sent at 14:19 UK through the build site's test form (/?achology-gift-test=1), course 022, both emails marked "TEST: ". The site reported both accepted. The member test inbox was manager@achology.com (the Achology inbox this session can read): **landed in the inbox** (Gmail's Updates tab), not spam, From wordpress@achologytest.com. **Karen's inbox: sent and accepted by the server, but where it landed I cannot read**; Karen or Kain looks for "TEST: ... has chosen" or similar at 14:19 today in karenramsay@achology.com and says inbox or spam.
- **Checklist (now live again in TO Chat as CHECKLIST__Launch_Switch_Over_S553.md, every new line marked S559):** B3 gains the SPF and DKIM line; B9 gains the TEST claim before the Circle redirect, and the welcome message address; C3 lists the forms that email from the site. Go-Live Steps (Project Delivery System) already carried SPF, the TEST claim and the welcome message; it now also names the DKIM key, in both places it speaks of the sender.
- **Forms that email from the site itself:** the Enquiries form (enquiries-setup.php; its correction topic, the Spotted a Mistake flag, goes to the editorial inbox) and the gift course choice (course-gift.php, two emails). The Roundup and every free lesson, teaching, workbook and event sign up post to Kit and send from Kit.

## 2. The Pricing card's gift line: WAITS

Not built. /membership/ today has no line "And We'll Gift You a Course Worth $97" above its button; its annual card opens with a gift banner (icon, "Commit for 12 Months and We'll Gift You a Course Worth $97", "Choose one of nine courses, and it is yours for life."). The brief's "word for word" and "same type and place" cannot both be met, so the reading is asked of the main session (recommended: the same banner, as on /membership/). Built the moment it answers.

## 3. "Masterclass" on Pricing: done

The short answer now ends "includes every workbook and a course for life" (pricing-parts.php). Read on /pricing/ in a browser: present; "masterclass for life" nowhere on the page.

## 4. The two Help answers: done, word for word

- 10041 difference-between-monthly-annual-achology-membership: excerpt, first paragraph, the "Annual is paid once" sentence and the last line, as written. The first paragraph's old link to /membership/ went with the paragraph it sat in, since the paragraph was replaced whole.
- 243 what-does-achology-membership-include: the annual sentence added after "three months of membership."
Both read back on the live pages in a browser.

## 5. Gateway

The seven paragraphs of ANSWER__Gateway_Words_Replaced_In_Seven_Help_Answers_S480 placed word for word, each found exactly once before anything was written: 412, 39512, 393, 279, 248, 10057, 10012. Each read back on its live page; none of the nine posts in this report names Gateway now. Every record (Content Records, help-answer) carries the same words, so a later import keeps them.

Still naming the closed free tier, for Chat's words (not touched):
- **/free-events/ (page 45042, published):** its Rank Math description reads "Join free live events, held Monday to Friday outside holidays, inside the Achology Gateway, our free community." The address 301s to /events/, but the page itself is published.
- **10040 there-free-achology-membership-include** ("Is there a free Achology membership tier, and what does it include?"): the body says the free membership closed, but its excerpt still reads "Yes: a free membership tier gives access to free events, the coaching board, the discussion forum, and quarterly ethics training." 18 published Help answers link to it (244, 248, 261, 279, 282, 331, 340, 392, 393, 398, 412, 10012, 10041, 10057, 39304, 39335, 39512, 41460); the links in 248, 279, 393, 412, 10012, 10041 and 10057 went with the replaced words, so check which still carry it.
- The free mindfulness record keeps "Achology Gateway" in its entity list and its facts table (not on the page).
- 10041's Rank Math description still says "Access is identical", which the new words contradict.
- Theme files: "Gateway" appears only as a lecture title ("A Gateway Between the Conscious and the Subconscious"), not the tier.

## The new Help answer: WAITS on the signature

DRAFT__Help_Answer_Choose_Free_Course_Annual_Membership_S549 is now a record, HELP__choose-free-course-annual-achology-membership.md in Content Records, help-answer, words unchanged. import_help_answers.py refuses it on one line only: "signed by Kain (Part 19 rule 7): the signed field is empty". Code may not write that field (content_gate: "Nothing Code builds writes this field"). Once Chat writes it, Code imports it as a draft, publishes it through publish_gate.py on Kain's yes, and reads its fields back.

OWED BACK: the signed field above, to FROM Chat; the main session's answer on item 2.

*No em or en dashes in this file; checked before writing.*
