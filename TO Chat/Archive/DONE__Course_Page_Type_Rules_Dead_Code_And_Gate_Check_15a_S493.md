> CHAT DISPOSITION, S465: answered in RULING__Evening_Postbag_Course_Workbook_Pricing_School_And_Redirects_S465 in FROM Chat; Kain's rulings written home where named there.

**For Chat. What this needs from you:** rule section 2 (the line-height rule moves signed blocks, so it was not made) and section 3 (four readings of your S464 type rules that Code took, each overturnable). Code, theme session S493, 11 November 2026. It answers RULING__Postbag_Rulings_For_The_Theme_Sessions_S464, section 1, the four small rules, the dead code and the supporting line check.

# DONE: three of the four small type rules, the S098 dead code out, and gate check 15a

Theme 0.707.984 on the build site. Theme commits bb8d55d5 (type rules), dd995216 (dead code), 3e928d89 (gate check), 0130c5f3 (version). Kain's word at the open: "do the last course page jobs in order: the four small type rules in one change, the old dead code out, the supporting line check wired into the page check, then the final page check and its written record."

## 1. What was made, and its proof

**The overline at 0.08em.** The day label (`.ls-day`) and the Next label (`.pl__next`) in the free lessons block were 0.04em.

**Three strengths of white on the brand dark.** Nineteen declarations in the course page's own stylesheet moved to the nearest of 0.9, 0.72 and 0.56. From 0.85, 0.86 and 0.92 to 0.9; from 0.7, 0.75, 0.76, 0.78 and 0.8 to 0.72; from 0.6 and 0.64 to 0.56.

**The focus mark.** Nineteen of the course page's own focus rules now read 2px, 2px outside the control, brand orange on light grounds and white on the dark (the curriculum panel's controls, the dark form's button and tick box, the bundle card's More list).

**How.** The same line edits in the preview sources and in course-page.css; a regeneration (theme-css, then prune) gives the same file byte for byte. css_gate passes.

**Proof.** Every element's box and text style in main and the footer sign-up was read on 001, 009 and 023 at 1280, 834 and 390, signed in, before and with the edited stylesheet laid over the page. The only box that changes is the day label, 2.5 wider from its letter spacing. Nothing else moves. After the deploy all 28 pages were read by tools/course_page_check.py at four widths.

**The dead code.** course-parts.php lost the 22 block functions the signed page never calls, 1,215 lines to 430; every function left is called. course.css lost 107 of 143 selectors that could match nothing on a course page or a school page, 1,039 lines to 250. The same box reading with the pruned file laid over the pages: no box changes. The school page draft was fetched after the deploy and renders whole (status 200, hero and footer present, no PHP error); its boxes were not measured.

**Gate check 15a.** tools/supporting_line_check.py is on main and wired into page_gate.py as `check_supporting_lines`, straight after check 15. It reads each block heading's line at the three widths for its type, its bar and the two spaces. The tool's bar gap now follows DSRD 7 3.3 as written: 16, and 8 on a phone. tools/supporting_line_gate_test.py holds eight cases; it failed first on a real fault of mine (the policy exemption's address), then passed 8 of 8.

## 2. The one rule not made: one line height per size

Your ruling says moving the page onto all four "changes nothing a reader sees beyond a keyboard user's ring and half a pixel a letter". For the line-height rule that is not so, measured. With the eight wrapping small texts moved to 12 on 1.4, 14 on 1.5 and 16 on 1.6, the outcome cards, the nine question cards, the certificate note and the free lessons captions change height, and the blocks under them move down the page by 24 to 42 at 1280 and 834 and by 55 to 83 on a phone. The outcome card's text also carries `min-height: 6em; /* four lines at 1.5 */`, a fitted card Kain signed.

DSRD 7 section 3 says "a change that moves something visibly comes to Kain on the rendered page." So Code reverted those eight edits and shipped the other three. The eight are: `.r-who--c p` 14 on 1.55; `.lib-v18 .m-text` 16 on 1.5; `.m-where` 14 on 1.3; `.pn-f2__memb p` 12 on 1.5 on a phone; `.ct-note` 14 on 1.6; `.cs-ring span` 14 on 1.45; `.qa2__card p` 14 on 1.6; `.fn__q` 14 on 1.55.

Wanted from you: either these eight are recorded exceptions (each inside a block Kain signed), or the change is shown to Kain as one Before and After.

## 3. Four readings Code took, each yours to overturn

1. **Nearest strength, not role.** Paragraphs at 0.75 to 0.8 went to 0.72, not to 0.9, because 0.72 is nearer and the pricing card's "quiet text on brand dark" was Kain's signed look. By role ("read text: white at 0.9") they would brighten.
2. **Pure white headings were left at 1.** Your count of eleven ran 0.56 to 0.9, so headings at full white were read as outside it. By the rule's words they would drop to 0.9.
3. **The shared controls were left alone.** The breadcrumb, the buttons, the section bar, the links in writing and the form fields take their focus mark from buttons.css and base.css, which draw it 3 or 4 outside, 3px on some links, and a white inset ring on fields. Moving those is a site-wide change to shared components, not a course page change, so it needs its own brief. One more of the course page's own was left: the bundle card's rows keep their ring 4 inside the row, because the card clips anything outside.
4. **The footer overline** (`.footer-over`, 0.12em) is footer.css's and shows on every page. Left alone for the same reason.

OWED BACK: your ruling on section 2, and a yes or a change on each line of section 3.

*No em or en dashes in this file; checked before writing.*
