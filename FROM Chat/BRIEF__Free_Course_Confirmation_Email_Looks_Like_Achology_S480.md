CODE DISPOSITION, S554: WAITS ON Branch G building the free course emails; Branch C read it in full and has no part in it.
For Code's main session (S552), Branch G. What this needs: make the free course emails look and read like Achology. Kain saw the TEST confirmation at 14:19 today and Chat judged it not ready.

Done when a new TEST claim through the build site's test route arrives From "Achology" at a real Achology address, in the same designed layout as the Kit emails (logo top and foot, the cream heading band, Mulish body, the dark footer), with the words below, landing in the inbox; a picture of it and of Karen's alert in a DONE in TO Chat.

# BRIEF: the free course confirmation email looks like Achology (Chat, Session 480, 23 November 2026)

Model and effort: Opus 5.5, xhigh. The branch asks Kain nothing.

**What Kain saw (manager@achology.com, Important, 14:19):** From "WordPress" (wordpress@achologytest.com), plain text, no logo, no design, and the line "If it has not appeared after 24 hours, reply to this email and we will sort it out." Kain's rule today: "we're not open to replies. We don't want replies."

**The fixes, in course-gift.php:**
1. **Sender:** From name "Achology", from manager@achology.com (the address every Kit email already sends from; it exists and receives). Use a wp_mail_from and wp_mail_from_name filter scoped to these two emails, or set the headers; never leave "WordPress". Keep the member's email Reply-To on Karen's alert only.
2. **Design:** send the member's confirmation as HTML in the same layout as the Kit emails (the Roundup welcome email 10623097 is the model: logo, orange rule, cream heading band, Mulish 17 body, dark footer with the white logo), with a plain text part beside it. Pictures from the email picture host of BRIEF__Email_Images_Must_Load_Past_The_Robot_Check_S480 once it exists; until then the same addresses the Kit emails use.
3. **Words, member confirmation (replacing the email_body; the heading band reads "Your Free Course"):**
   - Hi {first name},
   - Thank you for joining Achology Membership for the year, and for choosing {course}.
   - We add each free course to a member's account by hand, so please allow up to 24 hours. Once it is there, it is yours for life, even if your membership ever ends.
   - If it has not appeared after 24 hours, let us know through our enquiries page at achology.com/enquiries/ and we will put it right.
   - Warm wishes, Karen Ramsay, Achology.com
   No line invites a reply. The subject stays "You chose {course}".
4. **The thank-you line on the page** ("... and we have emailed you to confirm.") stays.
5. **Karen's alert** stays plain text (it is for Karen only), From "Achology Website", with the member as Reply-To as now.
6. Update WORDS__Membership_Page_S537.json's gift email_body to the words in 3, so the record and the code agree.

OWED BACK: the DONE above.

DOCUMENT TYPE: brief.

*No em or en dashes in this file; checked before writing.*
