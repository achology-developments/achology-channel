> READ, Chat branch (10 November 2026): ships so far written into the Accreditation signed spec; the session is still open, so this report stays until its close.

**For Chat. What this needs from you:** nothing yet; this report fills as the session ships.

Code, S469 (theme session, the Accreditation page, Opus 5.5), opened 10 November 2026. Number claimed at the open; the full report is written at the close. Ship briefs for this session are carried here. Jobs, Kain's own, in order: the member levels as a neat grid with the member badges; a strip of testimonial videos; a closing strip on SoMAP with placeholder words.

# SHIP: Accreditation, the member levels as The Table with the member badges, theme 0.707.891

- **What changed:** section 4's ladder is now a neat table. Each level carries its own official member badge where its number was; the level names are a step smaller (Como 18, was 21); the four figure names are said once as column heads on a computer; Verified Member starts the climb; a row turns white with rounded corners under the pointer; Maintaining Master Achologist Status carries the Master Achologist badge with a renew mark; the line under the table is rewritten to fill two lines. Every word and figure inside the levels is unchanged.
- **Why:** Kain, on the block: "it's a big cream block ... could be designed to a much higher standard, so it looks more like a grid ... we're missing an opportunity here because we have member badges". He picked The Table from four designs, then gave three changes and picked Badge and Renew from four marks.
- **New words for Chat to read:** the Verified Member line "Where every member begins, and where everything starts to count." and the foot "Every member begins as a Verified Member, and each level after that is earned through checked sessions. Master Achologist is the last level, kept by meeting a set of activities each year. Read about all six member statuses and keeping Master Achologist status." Both Code's, approved by Kain on screen.
- **One for Chat:** the official first badge reads "Certified Achologist", where the page and REF 1 call the level "Achologist". The badges are achology.com's own pictures, now in the theme's images/accreditation folder.
- **Record:** PICKS.md picks 22 to 24. Commit 0c4fe7b7. Three deploy proofs passed. Checked on the build site at 1268 and 390.

# SHIP: Accreditation, the member video strip, theme 0.707.892 and 0.707.893

- **What changed:** a new section straight after The Three Kinds of Practice: "Why Practice Matters, in Our Members' Own Words", three of the site's member video cards (Brian Boyle, Peter Welch, Bea Fernández García answering the Testimonials page's peer-learning question), the question shown over the cards, "Senior Achologist" under each name, and a link to the Testimonials page. 0.707.893 is a one-line fix that brought the standing up under each name as previewed.
- **Why:** Kain: "a strip of testimonial videos, just to bring a bit more life to the page". He chose the place, then On White from four framings, then all four of Code's worked-up toggles.
- **Shared component:** achology_member_voices in shared-parts.php gains an optional 'rank' line; only a page that passes it shows it. /testimonials/ measured unchanged on the build site.
- **New words for Chat to read:** the heading and the line "Three Senior Achologists on what practising with other members has given them." (Code's, approved by Kain on screen). The quotes and transcripts are /testimonials/' own.
- **One for Chat, found in passing, not this job:** css_gate fails certification.css line 58 (a phone size of 16 where the rule expects 21); it fails the same before this session's change.
- **Record:** PICKS.md picks 25 and 26. Commits 5192ed23 and 7b63c53a. Three deploy proofs passed each time. Checked on the build site at 1268 and 390, one video played.

# SHIP: Accreditation, the video strip composed with the page, theme 0.707.894

- **What changed:** the strip is now a heading, one bar line and the cards, like every section on the page. The question label and panel are gone and the bar line carries the question: "We asked three Senior Achologists what value they have found in studying with other members." "Senior Achologist" under each name is grey. The link reads "Watch More Members Talk About Learning With Achology" and sits at the bottom right.
- **Why:** Kain: "the left-hand side of the column is ... overloaded with lines ... I don't feel that you've designed this block to complement the larger context of the page", and the old link words gave no reason to click. His picks from three toggles and four wordings.
- **New words for Chat to read:** the bar line and the link (Code's, approved by Kain on screen). The line written at 0.707.892 is withdrawn.
- **Record:** PICKS.md pick 27. Commit 7bce859f. Three deploy proofs passed. Checked on the build site at 1268 and 390.
