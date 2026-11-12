**DISPOSITION (Chat, Session 467, 12 November 2026): ACTED ON.** Asks 2 and 5 ruled in FROM Chat/RULING__Postbag_Answers_S497_To_S513_S467 lines 4 and 1; ask 1 is a Backlog: Chat line (the sweep brief, for Kain to sign); asks 3 and 4 need nothing more. Archived.

**For Chat. What this needs from you:** read the five answers to the read-only asks of RULING__Night_Postbag_For_The_Factory_Session_S465 section 5, and rule the free tier sweep from list 1. Code, factory session S510, 12 November 2026. Nothing was changed anywhere for these five: every one was read only.

This file asks Kain nothing. Nothing below is his until Chat has written the sweep brief that DSRD 4 section 1.6 asks for.

# DONE: the five read-only asks, S510

How it was read: the theme at main (deployed copy, read only); the build site over WP-CLI, read only (table prefix qbk_); rendered build site pages fetched one at a time, never more than one a second; achology.com never touched. Asks 1 to 3 were read by three Sonnet helpers inside this session and each result was checked against its files by Code.

## Ask 1. Where the free Circle tier is promised (with what would stand in its place today)

DSRD 4 section 1.6, word for word: "**The free Circle tier is ending (Kain, Code's S489 pricing sitting, 11 November 2026; written by Chat, Session 465, evening).**" and "So nothing comes off a page until what stands in its place, if anything, is decided for that place. Chat's sweep brief names each place from Code's list with what takes its place, and Kain signs it." The join address form is the community join link with an invitation_token, and the product name line reads "Achology Gateway (the Circle free tier)."

Count: 10 theme places, of which 7 print today; 25 Help answers and 2 empty page shells in WordPress; 1 schema Offer at 0.00 that a signed record promises and the theme never built. Pricing is clean: no Join Free, no Gateway, no free membership; the free_signup key in pricing-parts.php is read by nothing.

### Table A: the theme

The constant ACHOLOGY_COMMUNITY_JOIN_URL (functions.php line 19) holds the join address; six places read it and two write it out in full. "Paid link" below means the community subscription checkout (the $7 first month, already printed in the footer and the header nudge); "pricing" means /pricing/.

| Place | Template | Words as they stand | Where they live | What would stand in its place today |
|---|---|---|---|---|
| A1. Desktop menu card, every page | header.php 185 to 187 | "Learn for Free" / "Access FREE Events + Training Every Week" (join address) | Theme; also DSRD 8 section 18.20 and DSRD 1 carry the row | The paid link (the nudge "Get Started for $7" is in the same header, header.php 93 to 94), or /pricing/, or /learn/ |
| A2. Phone menu, every page | header.php 371 | "Learn for Free" (join address) | Theme; DSRD 8 Academy sub-link list | As A1 |
| A3. Help answer close, every Help answer page | help-parts.php 55 to 60 (the 'support' branch) | "Ask An Achologist Anything" / "Ask our current students and members about their experiences with learning at Achology." (join address) | Theme | The row beside it, "Contact Achology Support" (help-parts.php 50 to 53) |
| A4. Help pre-purchase pair, does NOT print | help-parts.php 113 to 116 | "Start Learning for Free" / "Join Achology now for free and start taking part in learning events" | Theme (dead branch since S091); DSRD 1 section 8 still describes it | Its sibling "Get FULL Access for $7" (lines 119 to 123) |
| A5. Policy page Where Next panel | template-policy.php 553 to 558 | "Join the free community" / "Learn with people from 216 countries" (join address, lock icon) | Theme; DSRD 9 (copy approved S282), DSRD 7 (lock icon key) | The panel's other two rows: "Read the latest articles" and "Come to a free event" |
| A6. Code of Ethics page | shared-parts.php 919 (address written out) | "Watch the Code of Ethics Training" / "The full training is free to watch with a free level of Achology membership" | Theme | The Certification pathway row the other policy pages use |
| A7. Ten Ways block on About, Reviews, Testimonials | shared-parts.php 1531 to 1535 | "Get Access to FREE 1-1 Coaching and Workshops" / "If you can't spend money, you can still take advantage of FREE learning events hosted by senior Achology members." | Theme | The next card, "Trial a FULL Achology Membership for 30 Days" (1544 to 1548), and the pricing card |
| A8. Manifesto events pair | policies-content/manifesto.php 83 to 85 (address written out) | "Start Learning for Free" / "Join Achology today for free and begin participating in learning events" | Theme | Its sibling "Get FULL Access for $7" (90 to 91) |
| A9. The constant | functions.php 19 | the address | Theme; DSRD 4 section 1.6 | Nothing reads it once A1, A2, A3, A5, A7 are decided |
| A10. Pricing data key, prints nothing | pricing-parts.php 78, free_signup | none | Theme | Nothing needed |

### Table B: WordPress on the build site (all published; Help answers are type faq_article)

| Place | Words as they stand | Where | What would stand in its place today |
|---|---|---|---|
| B1. Help answer 10040, the answer that defines the tier | Title "Is there a free Achology membership tier, and what does it include?"; excerpt "Yes: a free membership tier gives access to free events, the coaching board, the discussion forum, and quarterly ethics training."; "free tier" six times in the body | post_title, post_excerpt, post_content; term register DSRD 2 section 2.24 | Help answer 226's $7 first month half; /pricing/ |
| B2. Help answer 226 | Title "Does Achology offer a free trial or introductory rate?"; excerpt "Yes, there is a free membership tier plus a $7 first month of full Achology Membership."; Rank Math description and focus phrase "Achology free trial introductory offer" | post fields and rank_math meta | The $7 first month it already carries |
| B3. Help answer 39335, the one body holding the join address | "You can join Achology Gateway for free ..."; "Achology Gateway is the free membership, and joining costs nothing." | post_content | The paid link or the course pages |
| B4. 16 Help answers naming "Achology Gateway" | 248, 261, 279, 340, 393, 398, 412, 10012, 10023, 10041, 10057, 39304, 39327, 39335, 39512, 41460; for example 261 "Achology Gateway is the community's free level, and joining it costs nothing", 41460 "Achology Gateway is the free tier, needing only a free account and no payment" | post_content | The paid link and /pricing/; 10012 and 10023 can point at Certification and Accreditation; 248 and 392 lean on cost, where the 14-day guarantee in 261 stands |
| B5. 9 Help answers naming the free tier without "Gateway" | 226, 243, 244, 282, 331, 392, 10035, 41441 (plus 10040) | post_content | The $7 first month named beside it (244 already pairs them) |
| B6. Page 45040 /free-coaching/ (empty shell) | Rank Math description "Get free coaching on the coaching board inside the Achology Gateway, our free community ..." | rank_math meta | Kain's page to build with Chat (DSRD 4 section 1.6); nothing until then |
| B7. Page 45042 /free-events/ (empty shell) | Rank Math description "Join free live events ... inside the Achology Gateway, our free community." | rank_math meta | As B6 |

Clear on the build site: no menu item, no ACF or Rank Math schema meta, no widget or option holds the join address or an Offer at 0.

### Table C: schema at 0.00

- C1, not the tier: the workbook schema's Offer at price 0 (schema-parts.php 400) is the free workbook file and stays.
- C2: DSRD 9 records as closed (S381) "an Offer named 'Free Membership' at 0.00". The theme never built it (page-pricing.php 71 to 75 says so). It is a signed record promising something that does not exist; Chat's to strike when the sweep is ruled.

### Signed records that carry the tier (for the sweep brief)

DSRD 4 sections 1.5, 1.6, 11 and its capture list and homepage block 7; DSRD 2 term register; DSRD 1; DSRD 7 (lock icon); DSRD 8 (menu rows); DSRD 9 (policy panel, pricing Offer); DSRD 6; REF 1. No COPY or Signed file outside the archives carries the phrases.

### Next to the tier, not the tier (free coaching and free events wording)

The header nudge (header.php 93), the footer's "Free Coaching" link, About's "FREE Learning Workshops Open to the Public" (page-about.php 431 to 432), the policy panel's "Come to a free event", the accreditation page's member duty "Free coaching you give to someone outside Achology", several Help answers (342, 346, 350, 397, 10016, 10019, 10020, 10056), Testimonials line 302, and a Kit tag named "Free Member". These do not name the tier; listed so the sweep can decide them. Not read in full.

What could not be checked: the rendered About, Reviews, Testimonials, Manifesto and Code of Ethics pages (rows A5 to A8 read from the theme only); Circle itself and the Kit tag; a promise worded without the searched phrases.

## Ask 2. Button rulings the button family may have outweighed

Why the family wins: buttons.css is enqueued last (priority 999, functions.php line 1125) and sets colour, background, border colour, radius, shadow and underline with !important under :root :is(...). Only course-page.css and school-page.css print after it. So any page rule on those properties without !important loses, whatever its specificity. Every verdict below rests on reading that specificity and the removing commits, not on computed style.

| Page | The ruling | Renders today | Verdict | Evidence |
|---|---|---|---|---|
| Course and bundle cards (card sheet, book note and tag pages) | S061, Kain: school accent border at rest, school hover fill ("Yes, I like it!"); pick 14, school colours "don't contradict" | Orange frame, no school colour; markup carries only btn--learn-more | Outweighed, then deleted as dead | Paint removed in theme commit 5c4448bb (commerce-cards.php 341, 439, 570) |
| Every page, header Sign In | S096, Kain: orange border, orange fill on hover (header.css) | A white pill with the fire frame | Outweighed, then deleted as dead | 5c4448bb |
| Help answers, the Listen button | Hover fill, and an is-playing border and tint | is-playing is still set by listen.js 212 and nothing paints it | Outweighed, then deleted as dead | 5c4448bb |
| Book note side panel button | S113 to S115, Kain: "make that the same Achology dark grey", hover to the footer dark | White with the fire frame | Outweighed, then deleted as dead | 61268984 |
| About, Reviews, Our People and author profile hero buttons | S044 and S238: the outline button fills on hover (about.css 176, 715) | The hover fill and white label are forced off | Outweighed (rules still in the file, dead) | specificity reading |
| Pricing, seven school buttons | S127 Quiet | Outline | Holds (restored at 0.708.001) | |
| Pricing, four opening cards | S122 and S128 | Family outline class | Holds, superseded by Kain's S489 pick | 33ec651b |
| Warm room, workbook capture, course hero and others | size and place only | Agree with the family | Holds | |

Five outweighed. Not settled: whether Kain's family picks 4 and 5 meant to replace the Sign In, Listen, About and book note looks (pick 14 plainly keeps school colours); the kinds button hover (S177) and the A to Z lift (S180) removed in fca21549 and 13225d8d; three more buttons (kh-aside__btn--stroke, pricing-tier__cta, rv-bar__go). Restoring any of these is a look on a built page, so it is Kain's eye through a theme session, never this session.

## Ask 3. The two longest "Where This Workbook Comes From" parts, with all 86 counts

DSRD 2 section 1.7, word for word: "**Words.** Sections 1 to 5 carry 350 to 450 words in all (Kain, S411), section 5 taking roughly a third." The same section says "Three short paragraphs" for it, with no figure.

The two longest: **Bloom's Taxonomy of Learning Workbook (post 43735), 140 words**, and **Maslow's Hierarchy of Needs Workbook (post 43784), 139 words**. Across the 86: least 110, middle 126, most 140. None is over 150 (a third of 450); four are under 117 (a third of 350): Glasser's Choice Theory 110 (43742), Six Domains of Self-Concept 111 (43845), Putting Learning Into Action 116 (43073), Inner Authority and Outer Authority 116 (42783). Every count is from the built page's stored content: the part under that heading to the next heading, the heading not counted. The rule gives no limit for section 5 alone, so whether 140 sits inside it turns on the whole of sections 1 to 5, which was not counted here.

All 86, longest first, post id then words: 43735 140; 43784 139; 45127 135; 45182 135; 45224 134; 45189 134; 45273 134; 45245 134; 42904 134; 43756 132; 45231 132; 45203 132; 45175 132; 45113 132; 45210 132; 43852 131; 42867 131; 45168 131; 43749 131; 45196 131; 42874 130; 42741 130; 45148 130; 45134 129; 45217 129; 43777 129; 45266 129; 45252 129; 45259 129; 43798 128; 42881 128; 42797 128; 42769 128; 42727 128; 45064 128; 45154 128; 42888 127; 42846 127; 42804 127; 43805 127; 45238 127; 42999 126; 42818 126; 42811 126; 42748 126; 43770 126; 45055 126; 43024 125; 42734 125; 45078 125; 45141 125; 43763 124; 43045 124; 42895 124; 42853 124; 42832 124; 42825 124; 42762 124; 40321 124; 43791 124; 45161 124; 42839 124; 43826 123; 42973 123; 42790 123; 44805 123; 45048 123; 43838 122; 43812 122; 42860 122; 45071 122; 42755 121; 45099 121; 45120 121; 42953 120; 42926 120; 45085 120; 45106 119; 43859 118; 42776 118; 45092 117; 43819 117; 43073 116; 42783 116; 43845 111; 43742 110.

## Ask 4. Pricing and the Founders' Letter scores

score_run.py read each page in its editor and saved nothing; theme on the build site 0.708.040 to 0.708.041 across the run.

- **Pricing, post 36845: 85.** Failing or short: keywordInPermalink 0 of 5, keywordInSubheadings 0 of 3, keywordInImageAlt 0 of 2, lengthContent 5 of 8. Every other test full.
- **Founders' Letter, post 10887: 91.** Failing or short: keywordInContent 0 of 3, keywordInSubheadings 0 of 3, lengthContent 2 of 8, contentHasAssets 4 of 6. At 91 it is over the site page bar of 90.

This answers DONE__Four_Site_Pages_Wording_Fixes_And_Scores_S462 for these two. The address and the length tests are the two Kain has ruled on elsewhere (an address is never changed for a score, S051; length is never met by padding); which apply to Pricing is Chat's.

## Ask 5. The 41 redirect rows

The folder truth is **42 rows, not 41**. Traced by reading the Redirect Master and the site's redirect table (qbk_rank_math_redirections), then asking the build site for each of the 42 without following, one a second.

- The site holds 2,923 active redirects: 2,364 match a Master row marked verified with the same destination; **42 match a Master row still marked "ruled"**; 517 are redirects the Master does not hold at all (516 under /learn/, 1 under /help/: the rebuild's own internal moves, which the Master was never meant to list). 2,364 plus 42 plus 517 is 2,923.
- **All 42 were written in one batch on 11 November 2026 at 17:51:25, and every one answers 301 to exactly the destination its Master row names (42 of 42).** All six destinations answer 200: /free-coaching/, /membership/, /academy/schools/, /certification/, /access-all-areas/, /accreditation/.
- Which side is right: **the site.** Each row is built and proved; the Master's status cell lags at "ruled" and should read "verified". By sheet: Jobs 27 (all to /free-coaching/), Miscellaneous 10, Core pages 4, Courses and commerce 1.
- The 42 old addresses: /free-life-coaching/, /achology/achology-membership/, /achology/academy/curriculum/, /achology/academy/certification/, /product/achology-access-all-areas-pass-bundle/, /jobs/ and 25 /jobs/ pages, /job-category/free-sessions/, five /cips- and /pals- form pages, two /resources/ rewards pages, /product-category/membership/, /product-tag/all-access/, /resource_cat/achology_community_resources/.

Nothing in the Master was changed: the sweep brief, section 4, says "Change nothing in the Redirect Master. Chat rules the rows from your list." (The night postbag's ask 5 said "mark the workbook"; the later brief governs.) If Chat rules the 42 to verified, a factory session types them in one change. Note for the free tier sweep: 28 of the 42 point at /free-coaching/, an empty page shell (Table B6).

OWED BACK: Chat's sweep brief for the free tier (ask 1), Chat's word on the five outweighed buttons (ask 2), and Chat's ruling on the 42 Master rows (ask 5).

*No em or en dashes in this file; checked before writing.*
