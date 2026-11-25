> CODE DISPOSITION, S569 (side session, 25 November 2026 10:50): WAITS ON the new file reaching this Mac. The local 013-001 introduction.mp4 is the OLD cut (615,052,318 bytes, modified 20 November 22:56), not the brief's 614,609,310 bytes of 25 November 07:38, and vimeo_replace.py is not in Video Production Team/_tools here. Nothing uploaded.
NEEDS: Code to replace one Vimeo video's file with Kain's approved new cut, under the same id. Approved by Kain; do it now.

Done when: Vimeo 623329116 plays the new 013 introduction (304.12 s), the old file kept as an earlier version on Vimeo, and DONE__Replace_013_Introduction_On_Vimeo_25_November_2026.md is in TO Chat.

# Brief: replace the 013 course introduction on Vimeo

Chat, 25 November 2026. Kain watched the remade film with the centred close shot and said, in Chat: "yes, sign off both" (009 and 013).

**The video.** Vimeo id 623329116, the Hypnotherapy Practitioner Course introduction (the id in the theme's tools/course_intro_films.json, so the course page keeps its link).

**The new file.** In the project folder: 07. All Achology Videos | Vimeo Exports / Course Introduction Edits / 013-001 / "013-001 introduction.mp4". It is made on the iMac Pro. Before uploading, check your copy is the new one: 614,609,310 bytes, 304.12 s, modified 25 November 2026 at 07:38. If your copy differs or is still syncing, wait for it; never upload an older file.

**How.** Replace the file, never upload a new video: the same id, title and settings. POST /videos/623329116/versions (upload approach tus) keeps the old file as an earlier version. Chat's script Video Production Team/_tools/vimeo_replace.py does exactly that (`vimeo_replace.py 013` checks only; `--upload` replaces). Use it or your own way, with your key that has the upload scope.

**Limits.**
- 013 only. Never write the key into the channel, a log or a reply.
- Change no title, description, privacy or embed setting.

**Report.** In the DONE file: the time it was replaced, Vimeo's processing status, the duration Vimeo now shows, and that the earlier version is kept.
