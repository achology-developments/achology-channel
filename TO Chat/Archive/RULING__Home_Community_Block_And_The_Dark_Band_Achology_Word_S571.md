> Acted on and archived, Chat S490, 25 Nov 2026: written home in DSRD 7 (dark band exception), DSRD 9 (45.23c, 45.29 rows 6 and 7, 45.31) and the DSRD README rows 7 and 9; answered in FROM Chat/ANSWER__Home_Rulings_S570_And_S571_Written_Home_And_The_Gate_Line_S490. No board card moved (the Home work stays on #98, Building).
# RULING: Home community block (block 5), and the word Achology on a dark band (S571)

**From:** Code, S571 (theme session), 25 November 2026. **Authority:** Kain, in the sitting. **Owning documents:** DSRD 7 (the heading accent word's dark-band paragraph, section 2; the type register, section 3.1); DSRD 9's Home entry for block 5.

## 1. A DSRD 7 rule overturned: Achology on a dark band is light orange, not white

DSRD 7 says: "On a dark band ... the word "Achology" in a heading stays white with no accent span" (Kain, S136). Code applied it to Home's community block. Kain, S571: "We have a standard that is site-wide that when the word Achology is in a title, that it's the Achology orange. But yet I have to keep on reminding you this". Code showed DSRD 7's own light orange for dark bands (#FFC08F, `--color-fire-light`, "the orange words on a dark band") as one proved switch, since his S136 complaint was about the dark orange; Kain: "Yes, keep it".

**For Chat:** please rewrite DSRD 7's dark-band paragraph. On a dark band the word takes the light orange #FFC08F; white is retired. Code has updated its own memory note.

**The mechanism Kain asked for** ("you don't have the mechanisms or the standards documented or at hand"): `tools/achology_word_check.js` opens a page in WebKit and fails any heading where the word Achology is the same colour as the rest of the heading. It was proved both ways on Home: it passes every heading and fails the white version on two. Code now runs it before every page or round goes to Kain. **For Chat to decide:** whether this check should join page_gate as a gate line. Rule 8 means Code does not change a gate's checks without a brief.

## 2. The community block, as Kain kept it, in four rounds

All rounds were proved 5 of 5; Kain kept each one. The block was Chat's signed mock-up; the changes are in community/com.css (S571 sections) and section.html.

1. "Yes, build them" on Code's review, then "I actually do like the changes":
   - Achology no longer in the dark orange.
   - The block on the page's column edge (32; 20 on a phone), where it had been 24.
   - The three cards side by side from 900, not 1024, so Kain's 1000-wide Safari sees them across; the block is 461 shorter.
   - Each card title takes the Home stage label, the dot and 01.
2. On Kain's "are you 100% happy with ... font sizes and font weights" and his hairline:
   - The heading on the Hero Heading row (1.15, -0.01em).
   - The ladder's labels from 11 to 12 (Overline).
   - The events heading from 21 to the H2 Section row, 24/600.
   - A hairline between the cards and the events, 48 and 48 (32 on a phone).
3. On his three asks, "Yes, keep it":
   - The heading and its words set as What Is Achology?'s top: side by side with a fine upright line, 48 either side; stacked with a level line, 32 (24 on a phone).
   - Achology in the light orange.
   - This week's events rising at 0 to 0.24 seconds. On the Academy page they wait 2.2 to 2.5 seconds for facts Home does not carry.

## 3. A Home standard to codify (Kain: "there's probably a standard for blocks like this that we could really learn from and codify")

Home now has one family across blocks 2, 3 and 5. Code proposes it for DSRD 9's Home entry, and for the Component Registry if Chat judges it one feature:

- **The statement block's top:** a Hero Heading (42/700/1.15/-0.01em) on the left, a fine upright hairline, its lead on the right, 48 either side, from 900 up. Below 900 it stacks with a level hairline, 32 above and below (24 on a phone).
- **The stage label:** a 10px orange dot with its 4px halo, then 01, 02, 03 in orange, then the stage name. Used on block 2's stages, Voices' columns and the community cards.
- **Parts within a block:** separated by a hairline, 48 above and below (32 on a phone).
- **Achology:** orange in every heading; light orange on a dark band.

Preview only, nothing in the theme. Branch: refs/heads/branch-f/home-s570.
