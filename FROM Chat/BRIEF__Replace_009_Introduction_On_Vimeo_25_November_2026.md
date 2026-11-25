NEEDS: Code to replace one Vimeo video's file with Kain's approved new cut, under the same id. Approved by Kain; do it now.

Done when: Vimeo 846963215 plays the new 009 introduction (595.66 s), the old file kept as an earlier version on Vimeo, and DONE__Replace_009_Introduction_On_Vimeo_25_November_2026.md is in TO Chat.

# Brief: replace the 009 course introduction on Vimeo

Chat, 25 November 2026. Kain watched the remade film with the centred close shot and said, in Chat: "yes, sign off both" (009 and 013).

**The video.** Vimeo id 846963215, the Life Coaching Certificate Course introduction (the id in the theme's tools/course_intro_films.json, so the course page keeps its link).

**The new file.** In the project folder: 07. All Achology Videos | Vimeo Exports / Course Introduction Edits / 009-001 / "009-001 introduction.mp4". It is made on the iMac Pro. Before uploading, check your copy is the new one: 1,207,611,720 bytes, 595.66 s, modified 25 November 2026 at 05:39. If your copy differs or is still syncing, wait for it; never upload an older file.

**How.** Replace the file, never upload a new video: the same id, title and settings. POST /videos/846963215/versions (upload approach tus) keeps the old file as an earlier version. Chat's script Video Production Team/_tools/vimeo_replace.py does exactly that (`vimeo_replace.py 009` checks only; `--upload` replaces). Use it or your own way, with your key that has the upload scope.

**Limits.**
- 009 only. Never write the key into the channel, a log or a reply.
- Change no title, description, privacy or embed setting.

**Report.** In the DONE file: the time it was replaced, Vimeo's processing status, the duration Vimeo now shows, and that the earlier version is kept.
