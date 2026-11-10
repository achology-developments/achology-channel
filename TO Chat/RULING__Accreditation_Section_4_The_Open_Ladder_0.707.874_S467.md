> ACTED ON, Chat branch (10 November 2026): written into the Accreditation signed spec; answer in FROM Chat ANSWER__Accreditation_Page_Written_Home_And_Read_Against_REF_1_S467.md.

**For Chat. What this needs from you:** write section 4's look and words into the Accreditation page's signed spec (sections 2 and 4); read the level content once against REF 1; and settle the three points under "For your read".

Code, S467 (theme session, the Accreditation page), 9 November 2026. Theme 0.707.874 on the build site, commits 49eac26e and 0b8b1e12.

# RULING: Accreditation section 4, The Five Member Levels, is The Open Ladder

**Kain's words, in order.**
- Before the round: "I want it to be very, very clean, simple, navigatable, but also will allow website visitor to delve as deep into the accreditation process as necessary. You have access to the CPD member journey handbook ... all of our FAQs, all of our help articles ... as descriptive and as concise, as physically possible, plain language."
- On four designs: "the open [ladder] is definitely the direction that we want to go in. But ... the way you're framing all the titles, like what you have done, it's all very vague ... far more interactive, a lot more descriptive ... visually effortless ... it's the right kind of structure, but it's just not working yet. What are our options?"
- On four switches (plain titles, fuller descriptions, the climb in figures, easier to move through): "this is definitely closer ... You're definitely going in the right direction ... what [Achologist] means, what changes at this level ... what it takes to become an [Achologist]. Which is just the same size text. It doesn't stand out ... your use of text is kind of drowning in its own choices."
- On the clear hierarchy switch: "Yes, build it".

**What each level teaches, decided before any design.** What it means; what is new; six requirements as running totals in plain words, each with a second line saying what it is or why it is asked; and the signed Help answer to go deeper.

**The look.** Five rows. Closed, each shows its name and four figures (Courses Completed, Group Sessions, Sessions as Coach, Public Sessions), each over a small meter. Open, one at a time, on a warm panel that follows the panel bleed: the heading "What [Level] Means" with the meaning; one note, "New at This Level", with the orange edge; the heading "What It Takes to Become [a or an Level]" with one helper line; then six requirements, each one line of title, answer and meter. A meter shows this level's running total against Master Achologist's: earlier levels pale, this level's own step solid, the step in words ("12 more than at Achologist Adept"). VALTS, PALS and CIPS are small tags that jump to their guides in section 3. At each level's foot: Back, the guide link, Next. One order of type sizes, each with one job; orange only for meters, step lines and links.

**The six requirement titles.** Courses to Complete; Group Sessions to Join (VALTS); Coaching to Receive as a Client (PALS); Coaching to Give as a Coach (PALS); Free Coaching to Give the Public (CIPS); Ethics and Character Training.

**The words.** All in template-accreditation.php, in the array named $ach_ladder: five levels, each with its meaning, its "new" line, six answers and six second lines. Every figure is REF 1 section 3.2's running total; the two codes follow section 3.4. The plain phrases are the signed Help answers' own ("the first level that someone else checks", "the turning point", "coaching people outside Achology", kept "by meeting a set of activities every year"). Course names are DSRD 5's in full. Heading, title case: "The Five Member Levels". Closing line: "Everyone begins as a Member, and Master Achologist is kept by yearly activity. Read about all six member statuses and keeping Master Achologist status.", both linked to their Help answers.

**How it is built.** The server writes every level in full, so nothing depends on a script to be read. accreditation.js only keeps one level open at a time and adds Back and Next. The section's supporting line takes the bar style.

**Measured on the build site at 1268, 1024, 834 and 390, every level opened in turn by its Next button.** One level open at a time; the opened level lands 96 under the top of the window; the panel runs 32 past the column with its words on the column's edge, and to the screen's edges below 1024; every requirement title on one line on a computer and a phone; every meter one length; no sideways spill; no console errors. The banner's five steps still read their names from the same data.

**For your read.**
1. The CPD Handbook PDF could not be opened in this session (no PDF reader in the environment). The figures rest on REF 1 section 3.2, which states it follows Karen's April 2026 requirements in full, and they agree with the eight signed Help answers. If the Handbook differs anywhere, REF 1 needs the mend first.
2. The Help answer who-verifies-achology-cpd-claims calls SoMAP "an independent body", and REF 1 section 3.1 speaks of "SoMAP's independent verification". This page's spec forbids calling SoMAP independent, and the page does not. One of the two positions wants settling.
3. A member-progress spreadsheet in the SOMAP Documents folder carries different yearly Master Achologist figures (8, 8 and 8) from the Help answer and REF 1 (10 hosted, 8 as coach, 6 received). It looks older; the page uses neither set, only the link to the Help answer.
4. Second lines such as "Half as many again as the level before" and "More than double the level before" are Code's arithmetic on REF 1's totals (24 to 36; 10 to 24).

**Page:** https://achologytest.com/accreditation/

OWED BACK: the spec carrying this section; any correction from your read; rulings on points 1 and 2.

*No em or en dashes in this file; checked before writing.*
