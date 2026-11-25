# RULING: Home course finder (block 4) results as two-column cards, and its top tidied (S571)

**From:** Code, S571 (theme session), 25 November 2026. **Authority:** Kain, in the sitting. **Owning document:** the Home course finder's signed brief and DSRD 9's Home entry for block 4.

## 1. The results are a two-column card grid

Kain asked Code for a plain review of the block as a gateway, then handed over ChatGPT's reference: "a compact two-column grid ... six product cards across three rows ... strictly a presentation-layer redesign". He said "OK" to building it as one switch, and on the proved round: "Yes, Claude, this is much, much better."

Built (finder-block.css, section S571 cfG; finder-block.js): each card has its school colour edge, kind, name and figures, then a hairline, with the price on the left and the action words on the right. The data, filters, quick picks, Pay In Full or Monthly, links and Show all are unchanged. Six cards in three rows of equal height; one column under 768. The cards use the site's card edge and shadow tokens.

**Words for Chat to confirm:** the action words come from the reference he handed over: Explore Course, Explore Pass, Explore Membership. A school bundle shows "Explore School", which Code wrote to follow the same pattern; the reference has no school card. Please confirm or replace it.

## 2. The top is tidied

Kain: "just tidy up the top of the block ... I think we've kind of got a hairline in there that maybe not be necessary." Code proposed three tidies; Kain: "Yes, build them", then on the proved round: "Yes, keep it".

- The hairline over the cards is removed; the count row stands 24 above the cards.
- The filter bar stands on the cards' edges (no longer 32 past them), with its words in line with the cards' words.
- The quick picks and the count row sit 16 apart.

## Still open, for Chat's view

Code's own review raised a bigger point that Kain has not yet ruled on: the block opens with six dropdowns and does not pick up the three stages Home sets up in blocks 2 and 3. Code suggested leading with those stages. This is recorded here only, not proposed as work.

Preview only, nothing in the theme. Branch: refs/heads/branch-f/home-s570.
