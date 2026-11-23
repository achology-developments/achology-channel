> Disposition, Chat S480, 23 Nov 2026: Pricing lock answered in FROM Chat/ANSWER__Gate_Lines_And_Open_Rulings_S480 section 3; archived. No board card moved.

**DOCUMENT TYPE:** Session report, not a page spec.
**Date:** 2026-11-23

# Session report S553 (Branch A, theme: Membership improvements and the Pricing checkout foot)

What this needs from Chat: keep the board current; one gate line below is Chat's to rule.

Assembled from the git log of branch-a/membership-s553 (each pushed to main and deployed). Board card for all: the Membership page and the Pricing page.

- 0.708.389, commit 5bc4f483: free event tickets carry the Events Boarding Pass lines (Academy and Membership band). SHIP__Membership_Free_Tickets_Pass_Stub_S553.
- 0.708.390, commit 990967c8: the week timetable's pulse, today's column and the next event's live line (Events and Membership). SHIP__Membership_Timetable_Pulse_S553.
- 0.708.391, commit 84596a4f: Chat's four bold openings in the Membership opening block. SHIP__Membership_Opening_Block_S553.
- 0.708.392, commit 27a88e5a: the Members band on Light Sand, every band now differs from its neighbour. SHIP__Membership_Band_Rhythm_S553.
- 0.708.393, commit 9a86a267: the questions block's hover arrow (site-wide block). SHIP__Membership_Questions_S553.
- 0.708.394, commit 2d101bec: the course pages' section bar under the Membership banner. SHIP__Membership_Guide_Bar_S553.
- 0.708.395, commit 0b3c5165: the checkout foot on the Pricing Pass card and both plans; the foot's one home, checkout-foot.css. SHIP__Pricing_Checkout_Foot_S553.
- 0.708.396, commit 8c68dedd: the Includes tiles lead somewhere; the bold openings made an optional field of the opening block's builder. SHIP__Membership_Tiles_S553.
- Improvement 8 was dropped before the session (Kain). Left out by the main session's ruling: per-kind colour marks on the timetable, the questions block's topic icons and ask card with a face, the opening block's icons and larger figures.

**Gate, run at 0.708.395 (page_gate.py).**
- /membership/: 42 passed, 1 failed, 14 for review, 59 carved out. The one fail is rank-math (post 45034 never scored): Kain's one-click rescore. Built, gate open: §3 (rank-math).
- /pricing/: 50 passed, 3 failed, 17 for review, 95 carved out. (1) icon-registry: the checkout foot's lock, three times, the same lock Chat already recorded as an exception on Membership at S551 ("the two checkout feet's locks, the Diploma card's own glyph from the Pass page's data"); the Pricing record needs the same exception line, Chat's to rule, Code or Branch B to enter. (2) content-width: a page-container of 1008, and (3) supporting-line: the questions heading at 21 on a phone; neither is from this session's change (the site-wide questions block), both named for the page's record. Built, gate open: §2, §10 (those lines).

Not finished: nothing of Branch A's list; the gate lines above wait on rulings and Kain's click.
