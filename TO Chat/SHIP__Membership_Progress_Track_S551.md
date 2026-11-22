This needs Chat to know the Membership page's member levels block shipped at 0.708.373, and to hold one item for the sweep list.

# Ship brief: the Membership member levels, The Progress Track (Code, S551, 22 November 2026)

**What changed.** Block 5 on /membership/, "From Your First Session to Master Achologist", now shows the six member badges as The Progress Track. This is improvement 6 of the ten Kain asked for in a whole-page review.
- The badges grow from 76 to 132 and start in grey.
- Beneath them sit six Achology bubbles, growing from 16 to 26 and shading from grey to orange, on a 2px line that stops short of each one.
- When the block scrolls into view, the line fills, each bubble pulses as it is reached and its badge comes into colour. It plays once.
- Each step card lights its badge on hover, and each badge its card.
- Without the script, or for visitors who ask for less motion, the row simply stands lit.
- No words changed.

**Why.** Kain: the six badges were "just kind of information sitting there. It's just lifeless." He chose The Progress Track from four rendered options (round-climb.js). Then he asked for three changes: no haze behind the nodes, a thinner line, and the bubbles graded in size and colour from left to right. "The progress track is perfect."

**Files.** previews/membership-page/build.py (takes_you) and memb.css Block 5, carried into membership.css and data/membership-page/main.json by tools/membership_page_data.py. The new membership-ladder.js, loaded by membership-setup.php. page_gate.py's image-responsive exception for this page went from 187 to 181, by name and value.

**Checked.** On the build site at 1280 the bubbles sit under their badges and each line stops 6 short of the bubbles either side. The tallest badge stands 24 under the lead line, the house gap. At 375 the badges stand one size (Master a step larger), the track steps aside and nothing scrolls sideways. The page gate reads 44 pass and 1 fail. The fail is rank-math, which waits on Kain's one click.

**For the sweep list.** Kain ruled the same day that no improvement may leave an orphan: a design must reach every page with a block doing the same job. The Accreditation page's level ladder (acc-ladder) does a related job, so whether it takes the Progress Track is a sweep for Chat to brief. The whole map of the ten improvements and their reach is in previews/membership-page/audit-s551/reach.html. Code has changed nothing on Accreditation.
