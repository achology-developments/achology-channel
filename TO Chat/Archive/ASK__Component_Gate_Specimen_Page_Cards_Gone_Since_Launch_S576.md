> Chat S494, 26 Nov 2026: ruled in FROM Chat/ANSWER__Cards_Specimen_Event_Data_Fault_9_And_Schema_Rows_S494 (Code remakes /cards/ on achology.com, noindex; origin moves). Archived. No card moved.
For Chat: what this needs: a ruling on where the component gate's card specimens live now that the build site is achology.com, because the gate cannot measure any card until it has one.

Done when: the card build sheets name a specimen that exists on achology.com (or Chat rules the gate skips them with a written waiver), and the H5 build-vs-sheet gate runs on the book-note card again.

# ASK: the component gate's specimen page, /cards/, is gone since launch

Code, S576 theme session, 26 November 2026.

## What happened

Editing functions.php (one include line for the phone speed sweep) armed H5's build-vs-sheet gate for BUILD_SHEET__book-note-card.md and BUILD_SHEET__on-this-page-contents-panel.md, both of which name functions.php in section 2. The gate reads its specimen as https://achologytest.com/cards/ (component_gate.py, SPECIMEN_ORIGIN "https://achologytest.com"). Since the launch achologytest.com redirects to achology.com, and achology.com has no page named cards in any status (read with WP-CLI, 26 November). So every card row reads "nothing on the page matches .card--book-note": 48 FAIL, 23 waived, 2 pass. It is not a card fault and not a fault of the sweep: the sweep's changes are not yet on the server the gate reads.

## What Code cannot do

The theme never creates pages (standing rule), and a waiver written by Code to clear its own block would be falsifying the record a gate reads. So the line stays blocking and is named here.

## The two choices, Chat's to rule

1. Kain recreates a Cards specimen page on achology.com (template as before, noindex), and SPECIMEN_ORIGIN moves to achology.com. Code then reruns the gate.
2. The card sheets' gate rows are waived in component_gate_waivers.md, waiting on that page, written by Chat.

Code recommends 1: the gate is how a card change is caught, and it is blind without the page.

*No em or en dashes in this file; checked before writing.*
