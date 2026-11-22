NEEDS FROM CHAT: nothing is blocked on you except the points under "Owed to Chat"; the rest is closed. Answers ANSWER__Gift_Page_Rulings_And_Gate_Fixes_S547 and ANSWER__Membership_Page_Gate_Lines_S544. Code, theme session S550, 22 November 2026, theme 0.708.358 on the build site, proved.

# DONE: the Membership and gift pages' gates, the two gate fixes, the excerpt

Most of this landed in 0.708.353 (S547, commit 72440587, shipped before the Membership session was archived); S550 verified each part against your two answers, reran both gates three times at 0.708.358, and closed the loose ends.

## Gate counts, three runs in a row at 0.708.358

| Page | Result (all three runs) | image-dimensions | image-lcp-candidate |
|---|---|---|---|
| /membership/choose-your-free-course/ | **44 passed, 0 failed, 7 for review, 29 carved out** | pass, all 184 declare the file's size | pass at all three widths |
| /membership/ | **44 passed, 1 failed, 14 for review, 57 carved out**; the one fail is rank-math (post 45034 never scored: Kain's one click) | pass, all 192 | pass at all three widths |

Printouts: Gift Page/page_gate__choose-your-free-course__0.708.358.txt and gate-printouts-S544/page_gate__membership__0.708.358.txt, each beside its DSRD6_RECORD.md, which carries the counts.

## What was checked and is in

- **Gift rulings A, B, E, G, I, K, M** are in page_gate.py by name and value; **D** passes on its own (DSRD 1 names the address); **H** read true on every run, no carve-out; **J** passes; **N**: the theme emits WebPage and BreadcrumbList (Rank Math printed none), chapter 4 reads pass from the built page.
- **Membership groups A, B, D to I** entered as ruled; **C** done by factory S548 (DONE__Membership_Chain_Register_Cells_S547, chain-register passes); **J**: complianz.min.js and the faces answer 200 on the build site directly, so the 502s are the mirror's and are carved for it by file name. **Mend 3.1** shipped in Kain's own words, "Groups Last Between 60-90 Mins" (RULING__Includes_Card_Groups_Last_60_To_90_Minutes_S547); the card's entry reads 38.
- **Gate fix 1, the Related questions list** (publish_gate.py; tools/publish_gate_related_test.py): red 3 of 4 before the change, green 4 of 4 after; the case that must still fail (a body link missing from the page, beside the list) still fails. Rerun today: 4 of 4.
- **Gate fix 2, image-dimensions waits** (image_gate.py; tools/image_gate_complete_test.py): red 3 of 5 before, green 5 of 5 after, covering the slow 160 file (never read as 32, reported not loaded by name), the planted true wrong size (still fails), and an errored picture (never passes). Rerun today: 5 of 5. Two further mends followed: a 60 second total wait, and a lazy picture never fetched reads "nothing to read", not "not loaded".
- **Answer 350's excerpt** is the exact 143-character sentence of your section 3.2, set with its clearance (2cdf037c65629124) and read back from the install today.
- **The two /academy/schools/ links:** footer.php fixed (0.708.358, commit 37414192, deployed, served page read: Schools points to /academy/). **The refund policy's link is NOT fixed:** it is theme content (policies-content/refund-policy.php line 28, "school bundles"), not page content, so there is no WP-CLI change; the page-intake hook refuses the edit because the policy family's rulings carry no PAGE GATE line. Left as it is, nothing worked around. It is one `href` to change; it needs a signed spec with its PAGE GATE line, or Kain's word through the main session.

## Owed to Chat

1. **The refund policy link** above (a spec with a PAGE GATE line, or a ruling that this one-link change may go).
2. **ANSWER__Course_Not_Masterclass_Words_For_Membership_And_Gift_Pages_S549** arrived while S550 was closing. Its six sentences are theme work on these two pages; S550 did not place them. They go to the next theme session, which will reply with a DONE and both gates' counts.
3. **Thirty-five Help answers and one article on the build site carry /academy/schools/ in their body** (found while looking for the refund link). Content, not theme: yours to route.

## Owed to Kain (the main session puts it; nothing asked of him here)

- The "Start for $7" button words on the join card and the path (his banner reads "Join for $7. Cancel Anytime.").
- His signature on the gift Help answer.
- His Rank Math click on post 45034.
- His phone walk and one real send through the gift form, as the records say.

*No em or en dashes in this file; checked before writing.*
