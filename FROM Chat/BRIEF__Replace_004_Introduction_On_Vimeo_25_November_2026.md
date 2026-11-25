NEEDS: Code to replace one Vimeo video's file with Kain's approved new cut, under the same id. Approved by Kain; do it now.

Done when: Vimeo 463798782 plays the new 004 introduction (1082 s), the old file kept as an earlier version on Vimeo, and DONE__Replace_004_Introduction_On_Vimeo_25_November_2026.md is in TO Chat.

# Brief: replace the 004 course introduction on Vimeo

Chat, 25 November 2026. Kain watched the full film and said "yes, sign it off", after asking that Vimeo uploads go to Code ("he's got all the access keys across there").

**The video.** Vimeo id 463798782, "004-001 Introduction to the NLP Master Practitioner course" (the id in the theme's tools/course_intro_films.json, so the course page keeps its link).

**The new file.** In the project folder: 07. All Achology Videos | Vimeo Exports / Course Introduction Edits / 004-001 / "004-001 introduction.mp4". It is made on the iMac Pro. Before uploading, check your copy is the new one: 2,195,378,742 bytes, 1081.84 s, modified 24 November 2026 at 01:34. If your copy differs or is still syncing, wait for it; do not upload an older file.

**How.** Replace the file, never upload a new video: the same id, title and settings. Vimeo's API does it with POST /videos/463798782/versions (upload approach tus), which keeps the old file as an earlier version. The script Chat wrote for this, Video Production Team/_tools/vimeo_replace.py, does exactly that (`vimeo_replace.py 004` checks only; `--upload` replaces); it reads a key from `.env.vimeo-upload` beside `.env` in the Vimeo Exports folder, or the .env itself. Use it or your own way, with your key that has the upload scope.

**Limits.**
- 004 only (014 has its own brief). The other four (009, 010, 011, 013) wait for Kain's yes on each, which Chat will send as its own brief.
- Never write the key into the channel, a log or a reply.
- Change no title, description, privacy or embed setting.

**Report.** In the DONE file: the time it was replaced, Vimeo's processing status, the duration Vimeo now shows, and that the earlier version is kept.
