> Disposition, Chat S484, 24 Nov 2026: faces 021, 026 and 027 go to Kain at the Membership sign; written on card #99.

**DONE (Branch 2, Code, 23 November 2026). Answers BRIEF__Membership_Banner_Real_Faces_Cropped_To_Match_S482. Theme 0.708.452, on the build site and pushed.**

**Which files.** The real members' photos are face-001 to face-028, not 032. Faces 029 to 032 are already tight (detector box 128 to 140 wide on the 160 tile, the same as the AI faces) and I left them as they were. 033 onward untouched.

**How.** Haar face detection on all 136 AI faces gave the target: face box 132 of 160 wide, centred at 79.5 across and 87 down. Each real photo was scaled and shifted so its detected box matches that, greyscale, 160 by 160, same file names, WebP. I looked at every result on the sheet. 018 and 019 needed the crop window held inside the picture (the face sits near the left or right edge).

**Soft or loose, for Chat to rule.** Only the 160 tiles exist here, not the originals, so every tighter crop is an upscale. I capped the upscale at 1.7 times. Faces 026 and 027 (the two women whose faces are small in the tile, needing 2.3 times) are capped, so their faces fill about 99 of 160 instead of 132: they sit looser than the rest. Face 021 needed 1.84 and is capped the same way. If Kain wants them tight, they need larger source photos, or they can be dropped from the grid.

**Sheet.** Faces 001 to 048, old above new, 16 across: `Membership_Banner_Faces_Before_And_After_S563.png` in this folder.

**Banner checked.** At 1440 and 1024 the wall shows the new crops; at 375 the wall is not drawn (phone shows the picture alone, as before). Nothing else on the page moved.
