**CARRIED (Chat, Session 464, 11 November 2026):** not yet acted on; the session closed for length on Kain's yes. It is Session 465's first act.

**For Chat. What this needs:** write Kain's ruling below into the learning block's home (DSRD 8 or the block's design folder, whichever owns it), and say if a fold-back export is wanted. Code, theme session, 11 November 2026 (the pricing page review sitting; session id caad3927).

DOCUMENT TYPE: RULING

# RULING: on a phone, each step card of the learning block shows its number whole, and the round icon is left out (theme 0.707.965)

## 1. Kain's words

Shown two pictures of the four step cards at phone width, as built and as proposed, with the plain statement that the change reaches the pricing page and the Knowledge Hub front page on phones only: "Yes, build it" (11 November 2026).

## 2. What was wrong

Below 768 each card's picture is a strip 112 wide at the card's height. The drawing (145 by 100) was sliced about its middle, so the strip showed the drawing from 42 to 103 of its 145 units. The big step number sits at 10 to 45, so every number was cut; the icons sit at 26, 58, 92 and 121, so step one's was missing, two and three showed whole and four's was cut. Measured in WebKit at 390 on /pricing/ and on /learn/; the same on both, so the fault was the shared component's, not a page's.

## 3. What was built (commit c1682d14, kh-front.css, the block's home file)

Below 768 only: the drawing keeps its own 145 by 100 at the strip's height and the strip shows its left side, so the number stands whole on all four cards; the icon's circle and glyph are not drawn. From 768 up nothing changes (read back at 834 and 1268: icons drawn, the picture as before).

Proof on the build site at 0.707.965: on /pricing/ and /learn/ at 390, all four numbers lie wholly inside their strips, no icon is drawn, and the page has no sideways scroll. css_gate passes on kh-front.css.

## 4. How it was deployed, named because it was not the usual road

Another session had unfinished, uncommitted About page files in the theme folder (about.js, functions.php, page-about.php, story-scroll.js). To ship only committed work, the deploy ran from a clean worktree of the commit, with each file's time matched to its twin in the theme folder first so the server's file times agree with the folder's. The worktree and the stray zip it wrote are removed. The zip beside the theme folder will read stale by that session's one new file until that session deploys.

## 5. Also in this sitting, each on Kain's yes, all on /pricing/

- 0.707.961: the plus mark on the seven school cards and the Pass card stands 9 clear of its words (it stood 1).
- 0.707.962: title case on five labels: Monthly Membership, Annual Membership, Unlock All Courses, Join Free, Pay in Full. "Unlock All courses" had been typed as Kain gave it at S127; he approved the change by name today.

OWED BACK: the ruling written home; your word on whether a prototype export is wanted for the block's phone state.

*No em or en dashes in this file; checked before writing.*
