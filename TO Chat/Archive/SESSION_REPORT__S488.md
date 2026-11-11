**DISPOSITION (Chat, Session 465, 11 November 2026):** read as the board index. The board has no pricing page card; the sitting's work is written home in DSRD 7 section 5.1 and DSRD 8 section 42, its two points answered in FROM Chat/RULING__Postbag_Rulings_For_The_Theme_Sessions_S465, and the two answer lines it names are on Backlog: Chat.

**For Chat. What this needs:** update the Pricing page board card from the lines below. Code, theme session, 11 November 2026 (session id caad3927). The number was claimed at the close, not the open: the sitting opened on Kain's single instruction and the report file was not written first, which is this session's own break of Rule 13.

DOCUMENT TYPE: REPORT

# SESSION REPORT S488: the pricing page review sitting

Kain's instruction at the open: review the pricing page top to bottom, give one list of every improvement, then make them with him. Every line below rests on the theme's git log unless marked hand added.

## Finished, each on Kain's yes in the sitting (board card: Pricing page)

1. fbc340b5, 0.707.960. The course tabs and the payment switch mended to the Fire Slide standard (DSRD 7, pick 7); the S209 underline removed. File: DONE__Pricing_Page_Tabs_And_Switch_Mended_To_The_Fire_Slide_11_November_2026.
2. f789bc2b, 0.707.961. The plus mark stands 9 clear of its words on the seven school cards and the Pass card.
3. 0a070921, 0.707.962. Title case on five labels: Monthly Membership, Annual Membership, Unlock All Courses, Join Free, Pay in Full.
4. c1682d14, 0.707.965. The learning block's step cards show their numbers whole on a phone; the round icons are left out there. Shared component, so the Knowledge Hub front page takes it too. File: RULING__Learning_Block_Step_Cards_Whole_Numbers_On_A_Phone_11_November_2026.
5. d5698f93, 0.707.971. 237 lines of rules no markup can match removed from pricing.css (the old dark Pass panel and the plan pills' clear mark). The proof and its limit are in the commit message: css_deletion_proof.py refused a verdict on this page, so the check was made in one WebKit page load at 1268.

## Found and not changed (hand added)

- The review list given to Kain held 23 items. Four were withdrawn to him as wrong after measuring: the small links' tap height (they pass by spacing), the Pass picture (the file is 380 wide, shown at 201), the three widths (panels bleed so the words share one edge), and the tabs' screen reader state (aria-pressed is set). A fifth, the top cards' three price colours, was withdrawn as deliberate.
- Page gate on /pricing/ at 0.707.965: 48 passed, 15 failed, 13 for review. The fails: spacing-scale (the 96 boundary and the learning block's spaces), block-heading on the four top cards and the Pass card, the DSRD 6 record (3 not run, 3 fail), the accessibility scan (the in-sentence link's faint line, put to Chat in the DONE above, and the cookie plugin's button), orphan, rank-math (never scored), keyword-density.

## Not finished

- The pricing page's DSRD 6 record is not updated for today's five changes. Not finished: the machine chapters need a fresh gate run written in, and section 10 names the tabs with their old look.
- The prototype in the Pricing Page folder shows the page before today. Not finished: the re-export as APPROVED, already a theme queue line.
- Left on Kain's list: links that open in two different ways (item 8), the page's length on a phone (item 13), the two questions with no answer line (Chat's words), the superseded declarations in pricing.css, the 27 inline style attributes, and the style sheets the page loads and does not use (site-wide, on the theme queue).
- Tablet: the tab row is 702 wide in a 674 column, so the last tab's end is cut by 28 until the row is slid. Put to Chat in the DONE above.

## Deploy notes (hand added)

- The 0.707.965 deploy ran from a clean worktree with file times matched to the theme folder, because another session had uncommitted About page files in the folder. The worktree and its stray zip are removed.
- This session's stop hooks were blocked four times by other sessions' uncommitted files (About page, course page data) and once by the build-versus-sheet gate during another session's deploy; each was named to Kain in one line and none of those files was touched.

OWED BACK: the board card updated; Chat's answers to the two points in the DONE and the one in the RULING.

*No em or en dashes in this file; checked before writing.*
