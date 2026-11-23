> Code, Branch 2 (third), 23 November 2026, S562. Section A of CHECKLIST__Launch_Switch_Over_S553 run line by line, and ruling 5.9's sweep of the launch pages that were skipped (ANSWER__Branch_G_Open_Words_And_Gate_Rulings_S481, section 5 item 9). Nothing switched, nothing designed. Theme read live on the build site: 0.708.435 (Branch 1's Six Day Free Lessons deploy; nothing of this branch's is newer than 0.708.434).

# Section A result, line by line

| Line | Result | Proof |
|---|---|---|
| A1 Gate sweep clean | **NOT CLEAN.** The 39 launch pages (below) leave the lines in the list further down; the earlier sections' lines (seven policy pages, /reviews/, /testimonials/, /about/instructors/, Code of Ethics, Presuppositions) are in the DONE of Help 327, still unruled | the sweep printout |
| A2 Redirect map proved | **NOT YET.** Read-only chain register: 2,598 rows, 562 destinations, **113 broken**, almost all Knowledge Hub pages (articles and book notes under /learn/) that answer 404 and are not in the sitemap, plus /learn/, /learn/book-notes/, /learn/general-interest/book-notes/, /enquiries/ (not in the sitemap). I did not run the writing pass (`--write-redirects-from`) because those destinations are unpublished; that is a publish decision (the 28 unpublished articles, S432) | chain register report |
| A3 Cutover gate plain run | **PASS.** Exit 0, site correctly hidden (blog_public 0, noindex on the sampled pages, workbench key 202 on the live host) | cutover_gate.py printout |
| A4 Old-site handover plan | **NOT DONE.** Needs Kain's hands in SiteGround (a full backup of the old achology.com into ~/db-backups/ and the frozen window). Not attempted from here | none |
| A5 Analytics hazard kept off | **PASS.** Rank Math's active modules on the build site are seo-analysis, sitemap, rich-snippet, role-manager, ai-visibility, redirections, 404-monitor, instant-indexing and the plugin's other integrations; the Analytics module is not active | wp option rank_math_modules |
| A6 Circle redirect words agree | **PASS** on the facts. The Help answer (post 47660) and the gift page both say one course of your choice, yours for life, nine courses, the name and email joined with, added within 24 hours. One note below (the word Masterclass on the gift page's nine cards) | both read live |
| A7 Every email picture answers 200 | **FAIL.** The static pictures pass (44 emails: 10 sequences and the Roundup draft; github.io logos, fonts and the free-lessons community picture, plus Kit's own filekitcdn logo in the four free-event sequences; all 200 with an image or font type to both the GoogleImageProxy and Outlook tests). **The per-subscriber pictures do not**: the fields course_cover, lesson_N_still and teaching_N_still hold achologytest.com addresses (read on three Kit subscribers) and those answer SiteGround's 202 robot check to both tests (tested: course-007-square-480.jpg, achology-free-lesson-007-1.jpg, achology-free-teaching-pgd-6.jpg). Workbook fields were empty on the sampled subscribers so were not tested | /private/tmp/claude-501/b2s/email_images.md |
| A8 Six lines added S559 | (the checklist's A1 to A7 are the seven lines; no more were found in the file) | |

So section A does **not** pass: A1, A2, A4 and A7 are open. A3, A5 and A6 pass.

# Ruling 5.9: the launch pages, measured

Run: page_gate on the build site through its local mirror, headless, 39 pages: /academy/, the seven school pages, the 28 course pages, /events/, /membership/ and its gift page /membership/choose-your-free-course/. I did not write the DSRD 6 records (the board's own sweep names a record per row; these pages are served by shared templates and the records hold nothing new from this run). **Passing outright: 30 of 39**, including every school page and 22 of the 28 courses.

# The unruled lines, one list, word for word

Acronyms (DSRD 6 section 1), five course pages and one more, each on a line the gate reads before a first spelling out:
1. "II" on **all six** failing course pages: "Toni-Lee Hazlett, Senior Achologist II, Canada", in a verified-student review. Not an acronym: a rank numeral in a person's title. Recommend an exception by the same reading as "Book II" (Roman numeral). Which is it?
2. "CBT" on /academy/cognitive-behavioural-psychology/cbt-mental-health/: "The opening section builds self-awareness for CBT, with the Johari…" (the full name is on the page further up the course description; the gate reads this sentence first). Send the first spelling or rule it.
3. "ABC" on /academy/cognitive-behavioural-psychology/cbt-toolkit/: "…introduces Cognitive Behavioural Therapy (CBT) and the ABC model of how thoughts…". Same ABC as the beliefs page.
4. "IQ" on /academy/life-coaching/life-coaching-blueprint/ ("emotional IQ and growth") and /academy/personal-growth/self-belief-emotional-intelligence/ ("Welcome to the Emotional IQ and Assertiveness Masterclass"): the same IQ as your ruling 6 on the Presuppositions page (a real name, "Emotional IQ"). Recommend the same exception.
5. "VAGOK" on /academy/neuro-linguistic-programming/beginners-guide-nlp/: "The Basic NLP Communications Model (+ VAGOK)". A lesson title, no spelling out beside it.
6. "SMOLER" on /academy/person-centred-counselling/hypnotherapy-practitioner/: "Read non-verbal communication using the SMOLER skills adapted f…".
7. "SMART" on /academy/personal-growth/goal-setting-action-planning/: "Build a vision board using the SMART vision boarding p…".
8. From the Presuppositions page (ruling 6): the 1962 timeline sentence "In 1962, Albert Ellis sets out his ABC model in Reason an…" is **visible text**; send the words for "ABC" or rule it. The fifth acronym the gate reads on that page is "II" (Book II in the sources list, "Nicomachean Ethics, Book II."): a Roman numeral; same ruling as 1.

/events/ (the same five lines as the Help 327 DONE, unchanged):
9. Supporting-line, phone: the heading "Practical Answers Before Your First Even[t]" reads Como 21, weight 600; the gate wants 24. (Is 21 on a phone the ruling here, as on the other pages' supporting lines?)
10. Breadcrumb-below, tablet and mobile: 32 declared, wants 48. The S480 Events mend left 32. Mend to 48, or rule 32?
11. Orphan: the gate's crawl missed 2,219 pages (three Help pages answered HTTP 502), so it will not give a verdict. This is the instrument; it needs a quiet rerun, not a ruling.
12. Chain-register: one workbook row points at /events/ and its five facts are not recorded (rerun of the register's writing pass, once the pass is allowed to run).

/membership/ and its gift page:
13. spacing-scale "ev-w row-gap 1" (desktop) on /membership/: the events week grid's 1px hairline, the same line as your ruling 5.1 on /events/. Recommend the same exception, by value.
14. icon-registry on /membership/: 29 inline SVGs neither drawn by the registry nor a recorded exception (the course-hero ripples, play and video marks q-play q-video, the r-spec icons, others). They are the course-page and rail icons now in the pricing family. Rule them in the registry or send the drawn replacements.
15. rank-math on /membership/: post 45034 has never been scored (Kain's tool).
16. chain-register on /academy/ (3 rows), /events/ (1) and /membership/ (37 rows): dest facts not recorded. These clear when A2's writing pass runs.
17. old-address on /membership/choose-your-free-course/: no redirect row points at it and live-site-urls.csv cannot be read, so the gate reads "unknown" as a fail. The page is new, so no old address is expected. Rule it a new page, an exception by name.

Other findings for you, outside the gate lines:
18. The gift page's nine course cards carry "Masterclass" in six titles (for example "Self-Belief, Emotional Intelligence and Assertiveness Masterclass"). They are the course product names, so I changed nothing; if Kain's "no masterclass written" rule reaches these titles it is a words question.
19. A7: the achologytest.com pictures in Kit's subscriber fields answer a 202 robot check. Moving them to the github.io picture host (item 4 of BRIEF__Email_Images_Must_Load_Past_The_Robot_Check_S480) is a separate piece of work that touches the site code that fills the fields and the stored fields of every subscriber so far; I have not started it.

# Not done here
- A1, A2 and A4 stay open as above. A2's writing pass waits on the publish decision for the unpublished Knowledge Hub pages.
- page_gate.py in the achology-factory folder is untouched (the factory session owns it, the main session's word).
- Content Records help-answer edit and the two Newsroom commits (bbe0856c, 9a922447): see the closing message to the main session.

*No em or en dashes in this file; checked before writing.*
