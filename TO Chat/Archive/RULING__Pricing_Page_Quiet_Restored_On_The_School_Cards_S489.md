> CHAT DISPOSITION, S465 night postbag (11 November 2026): DONE. Written into DSRD 9 section 36.9 (pick 6); the sweep is a read-only ask in RULING__Night_Postbag_For_The_Factory_Session_S465.md in FROM Chat, section 5 ask 2; noted in RULING__Night_Postbag_For_The_Theme_Sessions_S465.md in FROM Chat, section 2.6.

**For Chat. What this needs:** note in the pricing page's layout home that Kain's Quiet ruling is live again, and judge whether any other page lost a signed look the same way (section 3). Code, theme session, 11 November 2026 (session id 6b3d208d).

DOCUMENT TYPE: ruling. Not a page spec.

# RULING: Kain's Quiet ruling is put back on the pricing page's school cards

## 1. What was lost

At S127 Kain was shown four ways to give the pricing page a peak and chose Quiet: the seven school cards' buttons outlined, so the Pass card kept the only solid button in the block of eight (written in pricing.css, THE PAGE'S PEAK). When the button family was rolled out its rules outweighed that paint, and the paint was later removed as dead (theme commit 5c4448bb). All eight buttons had been solid since, including on the page he signed at S209.

Code's review list this sitting proposed the Pass as its own full-width band. The same note in pricing.css records that he saw the Pass at full width three ways at S127 (Stage, Lift, Apart) and turned them down for Quiet. The proposal is withdrawn; it should not have been listed before the notes were read.

## 2. His word, and what is built

Shown the loss as one switch in the Change Viewer (the theme's previews folder, pricing-s489, round-qs.js; proved by viewer_proof.py). His words: "Yes, build it". Built at theme 0.708.001 (commit 7c03a875): the seven school buttons carry the button family's outline class in the markup; the Pass keeps the solid one. Read on the build site at 1268, 834 and 390: every button the same size and place as before, the page the same height.

## 3. For you to judge

The button family's rollout outweighed a page-level ruling without anyone choosing that. Whether other pages lost a signed button look the same way is a question for a sweep; Code has not looked beyond this page.

## 4. A deploy fault, mine

The deploy of 0.708.001 also carried the school page session's uncommitted school-page.css to the build site: the file was modified in the shared folder when deploy.py ran, and my command did not stop on it. I did not edit or commit it. That session has been told directly and asked to check the school page and redeploy.

OWED BACK: the layout note, and your call on section 3.

*No em or en dashes in this file; checked before writing.*
