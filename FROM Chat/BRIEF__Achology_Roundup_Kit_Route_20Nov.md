CODE DISPOSITION, S541: DONE. Built at 0.708.267 (roundup-kit.php, tag 26223648), test sign-up read back, welcome email sent; DONE__Achology_Roundup_Kit_Route in TO Chat.
NEEDS: Code to build the site side of the Achology Roundup sign-up (form 3), so a sign-up reaches Kit and starts the welcome email. The visible block on the homepage is not built from this brief.

# BRIEF: the Achology Roundup sign-up reaches Kit

From Chat, 20 November 2026. For a theme session.

Model: Claude Opus 5.5. Effort: high.

## Why

Form 3, the general mailing list, is now the Achology Roundup (Kain, 20 November 2026, written into DSRD 4 section 5.1). It is a newsletter sent only when there is news, never on a schedule. Kain signed its welcome email the same day ("Yes, put it in"), and it is published in Kit. Nothing on the site sends anyone to it yet.

## What is already in Kit (Chat, 20 November 2026)

- Sequence 2979796, "Website Achology Roundup Welcome", sent from manager@achology.com, Europe/London.
- One email, 10623097, "Welcome to the Achology Roundup", published, sent the moment a reader joins (0 hours). It greets the reader with Kit's own first name field ("Hi there" where it is missing) and reads no custom field.
- The tag is DSRD 4's `Website Newsletter Signup`. Read its id from Kit; if it does not exist yet, create it with that exact name.

## What to build

1. **A Kit route for the Roundup,** written the way school-kit.php and course-kit.php already work, with no Kit script on the page. It takes a first name, an email address and the consent tick; sends Kit the first name in Kit's own first name field; tags the reader `Website Newsletter Signup`; adds them to sequence 2979796; and records the consent the way form 6 does, in `consent_text`.
2. **The form's fields and words are the workbook form's,** because every sign-up on the site asks alike (DSRD 4 section 5.1): "Your Name", "Email Address", a tick box, then the button. The tick box reads "Send me the Achology Roundup and Achology's emails." The button reads "Join the Roundup". The error lines follow the workbook form's.
3. **The thank-you line** after a sign-up reads: "Thank you, {first name}. Your welcome email is on its way to your inbox."
4. **Do not draw the homepage block.** Block 7, Stay in Touch, has no signed look (Kain's Penpot ruling of 3 November 2026: no signed frame, no build). Build the route, and give it a plain test form on a page no visitor reaches, so it can be proved before the block is designed.

## The test

One real sign-up through the test form, as manager+roundup-test@achology.com, first name "Roundup Test". Read back from Kit: the subscriber exists with that first name, carries `Website Newsletter Signup`, sits in sequence 2979796, and Kit records email 10623097 sent. Then send Chat the read-back.

## What Chat checks afterwards

The subscriber in Kit, the tag, the sequence, and the welcome email as it arrives.

Done when: a test sign-up through the site's Roundup route is in Kit with its first name, its tag and the sequence, and Kit shows the welcome email sent.

OWED BACK: one DONE in TO Chat with the theme version, the tag's id, the route's file name and the Kit read-back above.

*No em or en dashes in this file; checked before writing.*
