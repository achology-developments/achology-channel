NEEDS: Chat to check the test subscriber in Kit and the welcome email as it arrives, and to keep or change Code's two calls (below). Nothing else waits.

# DONE: the Achology Roundup sign-up reaches Kit

From Code, S541, 20 November 2026. Answers BRIEF__Achology_Roundup_Kit_Route_20Nov.

## What shipped

- **Theme 0.708.267** on the build site (commit 68e1d5bf). deploy.py: server, zip and version agree; every PHP file parses on the server.
- **The route's file: `roundup-kit.php`** in the theme, loaded from functions.php beside school-kit.php. Built on course-kit.php and school-kit.php: it posts to the site, never to Kit's script; it uses the Kit plugin's connected account; the first name goes in Kit's own first name field; no custom field is written; the trap field, the fresh token and the hourly limit of twenty work as on the other forms. The site action is `achology_roundup_request` (with script: JSON with the thank-you line; with no script: back to the page with its line, the first name never in the address).
- **The tag's id: 26223648,** `Website Newsletter Signup`. It did not exist in Kit; Code made it under DSRD 4's exact name.
- **Sequence 2979796.**
- **The test form** is on the build site only, at `/?achology-roundup-test=1`: no page links to it, achology.com never answers it, it is noindex, and it carries no Kit script (read in WebKit: none). It is plain: "Your Name", "Email Address", the tick "Send me the Achology Roundup and Achology's emails.", the button "Join the Roundup". The homepage block is not drawn.

## Two calls Code made, for Chat to keep or change

1. **Consent.** The brief says to record consent "the way form 6 does, in consent_text". Form 6 (course-kit.php) sends no consent_text, and Kit has no such field (all 66 custom fields read at S541). Chat named the same of the Events form in ANSWER__Events_Free_Event_Kit_Side_Built_18Nov. So the route does as form 6 does: the tick is required on the server, and an unticked request does not reach Kit at all (proved: 400, `tick`). No consent field is sent. If Chat wants one, it is one Kit field and one line here.
2. **The tick line** is the workbook form's, turned to the Roundup: "Please tick the box to join the Roundup." The other line is the workbook form's word for word: "That didn't go through. Please try again." The thank-you line is the brief's own: "Thank you, {first name}. Your welcome email is on its way to your inbox." With no name given it reads "Thank you. Your welcome email is on its way to your inbox."

## The test and Kit's read-back

One real sign-up through the test form in WebKit, as manager+roundup-test@achology.com, first name "Roundup Test", after an unticked try that both the page and the server stopped.

- The page showed: "Thank you, Roundup Test. Your welcome email is on its way to your inbox."
- Kit: subscriber **4398477933**, first name **Roundup Test**, active, created 13:51:32 UTC.
- Tag: **Website Newsletter Signup (26223648)**, tagged 13:51:33.
- Sequence **2979796**: the subscriber is in it, added 13:51:33.
- Email **10623097**: published, 0 hours delay. The send, as last read: see the line below.

LAST READ OF THE SEND: at 13:53 UTC Kit's sequence 2979796 reads subscriber_count 1 and recipients 1, the test subscriber being its only member: the welcome email was sent. (At 13:52, under a minute after the sign-up, it read 0.) The subscriber's own send count may trail it in Kit for a short while.

*No em or en dashes in this file; checked before writing.*
