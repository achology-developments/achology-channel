NEEDS FROM CHAT: read for the record; one fact to weigh (item 2, the page was published, not a draft). Nothing to answer.

# DONE: free coaching leaves the Achology website (Code, Branch G, S559, 23 November 2026)

Answers FROM Chat BRIEF__Free_Coaching_Leaves_The_Achology_Website_S480. Theme session, Branch G (launch jobs). Theme version on the build site: **0.708.402, unchanged**, because no theme file needed changing (item 3). Nothing deployed for this job.

## 1. Redirects, one hop each

- /free-coaching/ now has its own Rank Math row (written through publish_gate.py --write-redirect), 301 to /membership/.
- /free-life-coaching/ was a 301 to /free-coaching/. Repointed to /membership/.
- 27 more rows pointed at /free-coaching/: /jobs/, /job-category/free-sessions/ and 25 old /jobs/{listing}/ addresses (the old free session listings, S247 ruling). Each repointed to /membership/, so none goes through two hops. Not named in the brief; done because the brief's own redirect makes them two hops otherwise.
- Proof, asked from the build site's own server without following (my Mac is getting SiteGround's robot check, 202, for every page today, which is job 4's problem): all 29 addresses answer 301 to https://achologytest.com/membership/. Printout in the shared notes folder, branch-g-launch.
- Redirect_Master.xlsx: the 28 rows (Core pages row 17, Jobs rows 2 to 28) now read /membership/ with an S559 note; /free-coaching/ added as Core pages row 29; the Summary range moved to match. The copy before the change is in the master file's Archive folder, Redirect_Master__pre_S559_free_coaching_2026-11-23.xlsx.

## 2. The page (one fact for Chat)

The brief said the free coaching page "stays a draft". It was **published** (post 45040, "Free Coaching"). Taken to draft through publish_gate.py --retire, clearance 7bf9b6557caa2176, which first proved the 301 covers its address. Nothing built for it.

## 3. The footer

Nothing to remove. The footer rebuilt from Kain's signed mock-up of 20 November has no HELP & SUPPORT column and no Free Coaching link; the bottom row reads Help Centre, Enquiries, Privacy, Terms, Cookies, All Policies. Read on the build site in a browser at 1280 and 375 on /enquiries/: no footer link names free coaching or /free-coaching/. Pictures footer-1280.png and footer-375.png in the shared notes folder, branch-g-launch.
Gate on one page (/enquiries/, page_gate.py): links-resolve PASS, 52 checked, all resolve. The page's other fails are its own, unchanged and already in its record (hairlines, supporting lines, header-to-content, gutters).

## 4. Links taken off, words kept

The three Help answers, each one link, on the build site and in its record (Content Records, help-answer):
- 10016 cips-when-need-them: "the Get Free Coaching board"
- 10019 many-times-coach-same-person-cips: "the Get Free Coaching board"
- 10020 offer-free-coaching-someone-outside-achology: "to offer free coaching to someone"

Search after: no published post, no post meta and no option carries /free-coaching/ or /free-life-coaching/. No theme file that reaches the server names it (two gate scripts name it as a pattern; they never ship).
Left for Chat to judge, not touched: seven Help answers link the Help answer /help/events-and-mentorship/offer-free-coaching-someone-outside-achology/ (315, 325, 326, 346, 10019, 39317) or achology-membership-free-coaching-included (342, 350). Those are Help answers, not the page, and their words are Chat's.

## 5. Sitemap

Rank Math's page sitemap still listed /free-coaching/ from its cache; regenerated (wp rankmath sitemap generate). No free-coaching page address in any sitemap now. The two Help answers above with free-coaching in their slugs are still listed, as Help answers.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
