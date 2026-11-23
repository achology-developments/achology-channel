> Disposition, Chat S480, 23 Nov 2026: record; superseded by S544 Membership, S547 and S550; archived. No board card moved.

**NEEDS from Chat: items 2, 4 and 8 below (rulings and the words file), and a Chat seat for the next Membership session to open on day one.** Code, S543 (the Membership page session), 20 November 2026.

# SESSION REPORT, S543: the Membership page

Theme at **0.708.324** on the build site. The page is /membership/ (post 45034), built from the preview `previews/membership-page/build.py` and stored by `tools/membership_page_data.py` into `data/membership-page/main.json`, drawn by `template-membership.php` and `membership-setup.php`.

## Finished this session (one line each)

- The members block (The School Block, "Yes, build 1").
- The join block as the Includes Rail pricing block, annual recommended (option 4).
- The annual gift: lifetime access to one $97 masterclass (courses 019 to 027), chosen on a form that emails Karen (karenramsay@achology.com) and the member; `course-gift.php`; tested on the build site at /?achology-gift-test=1.
- The questions block, Sorted by Topic ("Yes, build 4"), now three answers under each topic (What You Get gained 350 and 342).
- The whole page built into the theme (`template-membership.php`, `membership-setup.php`), Rank Math title, description and focus set over WP-CLI.
- The banner, all in Kain's words and signed: title "Achology Membership and Subscription Plans"; subtitle "Learning comes to life in the Achology community. Weekly group discussions and workshops build relationships, deepen understanding, and make personal growth inevitable."; button "Join for $7. Cancel Anytime."; no price line and no figures line; a faint wall of 170 grey faces (28 members, 142 AI) behind the picture at computer width.
- The first block in Kain's words: heading "What Achology Membership Can Give You"; line "Achology hosts a community shaped by collaborative learning, in which ideas are tested, discussed, and integrated into people's lives."
- The "What is Achology" film's own cover: the Zoom call of nine people faded back, a line globe in front, the play button on top (signed).
- The lone-word script no longer evens the Membership banner subtitle (`no-lone-words.js`); the school banners keep it.

## What stands between this page and finished

1. **Code: the phone and tablet check** of the whole page (390 and 768), every block, measured before Kain sees it. The build site's robot check turns away a phone browser; use the mirror (`previews/school-page-s482/proxy.py`, port 8482) or the tablet width.
2. **Chat: the DSRD 6 gate fails.** The last full run on the built page was 41 pass and 55 fail. Most fails are the gate reading card text as supporting lines, and proper-name capitals. Others: breadcrumb and spacing rows inherited from the school banner; the phone heading at 21 where the gate wants 24 (the site uses 21); badge images 120x124 with no srcset; the icon registry; the acronym "II". Code reruns the gate on 0.708.324 and writes the Membership DSRD6_RECORD honestly, naming each blocking line; Chat rules the exceptions.
3. **Kain: the one-click Rank Math rescore** (never driven by Code).
4. **Chat: the gift Help answer.** The draft `DRAFT__choose-free-masterclass-annual-achology-membership.md` (side-session-notes) goes through the publish pipeline; then its id joins What You Get (the questions answer's link points to /help/ until then).
5. **Kain, one choice: the choose-your-course page** where an annual member picks the gift course (the form exists; the page around it is not designed). Show him a rendered mock-up first.
6. **Kain's hands, after item 5: Circle's annual paywall**, Post purchase tab, switch on "Custom redirect URL" to the choose-your-course page. Guide him one step at a time.
7. **Kain, one question still unanswered:** the Pricing page reads "$0 trial" against DSRD 4's $7.
8. **Chat: bring WORDS__Membership_Page_S537.json into line** with the banner and first block words above (Kain's own, placed as given).
9. **Kain: his phone walk and whole-page signature** in Safari.
10. **Then launch.** The page is finished on the build site; going live on achology.com is the separate rollout thread (S543 side session, with Chat).

## Other sessions touching this page

- The S542 reviews sweep (`SWEEP__One_Reviews_Block_From_The_Membership_Design_S542`) will move the members block's `memb-wall`, `memb-vid`, `memb-rv`, `memb-who` and `memb-way` rules out of `memb.css` into one shared block. Whoever runs it must rebuild the Membership page after and measure it against today's.
- S541's branch 3 (course intro videos) may add a line about what visitors can watch on the Membership page.

*No em or en dashes in this file; checked before writing.*
