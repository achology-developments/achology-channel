> CODE DISPOSITION, S568: WAITS ON the signed 24 November cut reaching this Mac; the copies here are the older cuts (004: 2,195,079,854 bytes, 20 Nov; 014: 1,206,980,698 bytes, 21 Nov), and vimeo_replace.py is not here either. Kain said yes to upload (S568).
NEEDS: Code to replace one Vimeo video's file with Kain's approved new cut, under the same id. Approved by Kain; do it now.

Done when: Vimeo 271093599 plays the new 014 introduction (595 s), the old file kept as an earlier version on Vimeo, and DONE__Replace_014_Introduction_On_Vimeo_25_November_2026.md is in TO Chat.

# Brief: replace the 014 course introduction on Vimeo

Chat, 25 November 2026. Kain signed the film ("Counseling skills is very good, Claude. Yeah, sign that off. That's brilliant.") and said "Yes, upload 014". Then, on finding this seat's Vimeo key is read-only: "just simply assign this as a task for code, he's got all the access keys across there. He can upload videos, no problem at all."

**The video.** Vimeo id 271093599, "014-001 Introduction to the Counselling Practitioner Course" (the id in the theme's tools/course_intro_films.json, so the course page keeps its link).

**The new file.** In the project folder: 07. All Achology Videos | Vimeo Exports / Course Introduction Edits / 014-001 / "014-001 introduction.mp4". It is made on the iMac Pro. Before uploading, check your copy is the new one: 1,207,076,058 bytes, 595.33 s, modified 24 November 2026 at 17:03. If your copy differs or is still syncing, wait for it; do not upload an older file.

**How.** Replace the file, never upload a new video: the same id, title and settings. Vimeo's API does it with POST /videos/271093599/versions (upload approach tus), which keeps the old file as an earlier version. The script Chat wrote for this, Video Production Team/_tools/vimeo_replace.py, does exactly that (`vimeo_replace.py 014` checks only; `--upload` replaces); it reads a key from `.env.vimeo-upload` beside `.env` in the Vimeo Exports folder, or the .env itself. Use it or your own way, with your key that has the upload scope.

**Limits.**
- 014 only. The other five (004, 009, 010, 011, 013) wait for Kain's yes on each, which Chat will send as its own brief.
- Never write the key into the channel, a log or a reply.
- Change no title, description, privacy or embed setting.

**Report.** In the DONE file: the time it was replaced, Vimeo's processing status, the duration Vimeo now shows, and that the earlier version is kept.
