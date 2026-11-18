NEEDS FROM CHAT: nothing now. When the free sign up works, the main Events session says so, and a factory session publishes the answer and places the three link sentences under one clearance.

Done when: post 47453 is a draft on the build site with every field read back equal to its record. It is. The publish and the three links wait on the free sign up.

# DONE: the free event Help answer is on the build site as a draft

**For:** Chat. **From:** Code, factory session S534, 18 November 2026. Answers BRIEF__Events_Page_After_Sign_Up_Words_And_One_Help_Answer_Import_17Nov2026, section 2 and 3, and DONE__Events_Questions_Block_Eight_Answers_Corrected_S531, section 1. Kain was asked nothing.

## 1. The import

**Import count: 1 of 1.** Record HELP__how-to-join-free-achology-event (the help-answer folder of the Stock's content records), as it stands after the S531 re-sign: the holiday line reads "at the same time every week except over holidays", and the record carries its post_excerpt.

- Content gate on the record: GATE: PASS.
- import_help_answers.py plan: PASS, new draft (fields complete to the help-answer standard, address matches /help/{category}/{post_name}/, category on the install, body free of process text, one internal and one outside link, words unchanged by the conversion). One note: the record has no hero picture line, so the answer imports without one, as every recent Help answer has.
- Pushed with import_help_answers.py --push, which can only create drafts: **post 47453, status draft.**
- import_help_answers.py --verify: 1 of 1 verified clean.

## 2. Every field read back over WP-CLI

Read from the install with wp post get, wp post meta list and wp post term list, and compared with the record by script. 0 faults.

| Field | On the install |
|---|---|
| post_status | draft |
| post_type | faq_article |
| post_title | How do I join a free Achology event? |
| post_name | how-to-join-a-free-achology-event |
| post_excerpt | Choose a free event on the Events page, leave your name and email address, and the Zoom link comes by email. No membership is needed. |
| faq_category | events-and-mentorship (term 14), also set as Rank Math's primary category |
| rank_math_focus_keyword | join a free Achology event, then four of the record's query_variants as secondary phrases (the S446 item 6 way) |
| rank_math_title | How to Join a Free Achology Event |
| rank_math_description | To join a free Achology event, choose one on the Events page, enter your name and email address, and press Join This Event. The Zoom link comes by email. |
| post_content | equal to the record's body as converted, character for character, and word for word |

**Tags.** The Help answer post type has only one taxonomy on the install, faq_category, and no Help answer on the install stores a tag in any meta field (checked across every faq_article). So the three tags (understand-your-mind lead, master-your-mindset, communicate-effectively) stay in the record, as they do for every other Help answer; the content gate lists kh_tag as a field outside the help-answer contract.

**The address.** WordPress gives a draft no public address: it lists post 47453 as ?post_type=faq_article&p=47453. The address /help/events-and-mentorship/how-to-join-a-free-achology-event/ comes into being at publish, from the category and post_name above.

**Score.** No Rank Math score is stored on the draft. A score exists only once the page is opened and scored; it is read off the built page after publish and Kain's one-click rescore, and then written into the score table.

## 3. The three link sentences: prepared and held

A visitor following a link to a draft gets a missing page, because WordPress does not show a draft to anyone who is not signed in. So, as the brief says, the three sentences are held and go in with the publish, under the same clearance. All three target answers are published:

| Post | Answer | Sentence, the link on "joining a free Achology event" |
|---|---|---|
| 361 | How do I RSVP to and join Achology live events? | If you would like to try one first, the answer on joining a free Achology event shows how. |
| 350 | What kinds of live events happen inside Achology? | Four of them are free to anyone, and the answer on joining a free Achology event explains the sign up. |
| 354 | How do I choose the right Achology event for my level? | Any of the four free events is a way in, and the answer on joining a free Achology event covers the sign up. |

Each link goes to /help/events-and-mentorship/how-to-join-a-free-achology-event/. They land at the source first (each answer's record), then go through publish_gate.py --update and article_body_update.py, the S531 route.

## 4. Two things for Chat

1. **The keyword register has no row yet for "join a free Achology event".** The brief says the set titles step claims it. It is on no other page today (the nearest is "join a live achology event", post 373's).
2. **stage5_import_checks.py refuses every Help answer** on the article field list (post_status, author, featured_image and the rest) and the article body shape. This one fails it the same way all the others do. The help-answer checks the importer runs are the ones above, and they pass. The script should take a help-answer field list. That is a factory job for the backlog, not done here.

## 5. When it goes public

The main Events session says when the free sign up works (the thank you state, the Kit sequence and the Zoom links). Then one factory session: publish_gate.py --clear on the answer with the three link answers under --update, set post 47453 to publish, place the three sentences, read all four back, and read the score after Kain's rescore.

OWED BACK: nothing now; the score and the three placed links come with the publish.

*No em or en dashes in this file; checked before writing.*
