> Disposition, Chat S480, 23 Nov 2026: not for launch, both signed as built; a line on Chat's Small Jobs (#12); archived. No board card moved beyond the comments named.

This needs Chat to know the Membership join block shipped at 0.708.369; nothing is asked of Chat except one note below.

# Ship brief: the Membership join block, Lifted on Dark (Code, S551, 22 November 2026)

**What changed.** The join block "Choose How You Join" on /membership/ (post 45034) was rebuilt on the build site at theme 0.708.369.
- It now sits on the brand dark band, with the plans as white cards lifting off it (Kain chose Lifted on Dark, round-join2.js option 3).
- The Annual card is crowned by an orange Gift Banner carrying the offer (round-gift.js option 1).
- The Pass card's neuron fires above the Monthly plan. A pathway runs from it into the gift banner, and each spark lands there and lights the card's ring (round-fire.js option 3, "Yes, build 3"). The orange haze behind the card is gone.
- Every line is Chat's signed plain words, placed word for word (ANSWER__Membership_Join_Block_Plain_Words_S551). The old gift lines are out of the card.

**Why.** Kain asked for "your best design work" on the block, said the free course should be made "a bit of a song and dance", and ruled that every offer line be plain, with nothing left to work out.

**Files.** previews/membership-page/build.py (join), memb.css Block 7, membership.css and data/membership-page/main.json (written by tools/membership_page_data.py), the new membership-join.js, and membership-setup.php, which loads it.

**Checked.** Measured on the build site at 1280 and 375. Computer: the spark path is drawn and the prices stand at 42. Phone: annual first, then monthly, then the list; no sideways scroll, and the neuron stays small in the corner with no path. The first gate run failed the lead at 26 words. Chat's 24-word lead (ANSWER__Membership_Join_Lead_25_Words_S551) was placed at 0.708.370, deployed and pushed, and the gate was rerun: 44 pass, 1 fail. The one fail is rank-math (post 45034 never scored), which was already the page's only failing line and waits on Kain's one click.

**One note for Chat.** The join prices stand at 42, as Kain chose them on the rendered round, not the pricing card's 24 (the pricing.css note says two membership prices on one site cannot be two sizes). If the /pricing/ membership card should follow, that is Kain's call. Code has changed nothing there.
