> Chat S494, 26 Nov 2026: A4 proved and launch done. Archived.
> Acted on, Chat S492, 25 Nov 2026: A4 line of CHECKLIST__Launch_Switch_Over_S553 now carries this proof. No card moved.
For Chat: what this needs: mark line A4 of CHECKLIST__Launch_Switch_Over_S553 as proved, with the proof below. Nothing else.

Done when: the checklist's A4 line carries this proof.

# DONE: launch checklist A4, the old site's backup is on Kain's Mac and proved (Code S572, 25 November 2026)

Kain's words in the sitting: "I want us to turn this website on ... deliver this checklist, not just create a checklist", then, asked whether to take the full backup of the old site onto his Mac now, "Yes, back it up"; asked about a second copy in iCloud Drive, "Yes, iCloud too". Read only on the old site: nothing on achology.com was changed beyond writing the two backup files into its own `~/db-backups` folder.

**The two files, taken 25 November 2026 from the old achology.com:**
- `achology-full-2026-11-25.sql.gz`, 51,594,645 bytes: the whole database (`wp db export`), 245 tables in the dump against 245 on the install, ending "Dump completed on 2026-11-25 20:17:40"; gzip test clean on the server and on the Mac; sha256 `2e3f86accedb8ba7a9a64b2597a5eeaf32a86c098b5c9209c6cd2d788d450c65` on both.
- `achology-files-2026-11-25.tar.gz`, 3,567,277,339 bytes: the whole `public_html` (4.7 GB unpacked). sha256 `1e85505d1ef7b4268d8eb3c9152055d591abcae1ccb1fc93b970086fef778251` on both. Opened and listed on the Mac: 67,874 files, the same count as `find public_html -type f` on the server. tar closed with its warning "public_html/wp-content: file changed as we read it" (the site was running); the file count matching is the proof nothing was dropped.

**Where they are:** on the Mac in the home folder, folder "Achology Old Site Backup 25 November 2026" (outside the project folder and outside iCloud); a second copy in iCloud Drive in a folder of the same name, same two byte counts (its upload to iCloud runs on its own and was not confirmed finished); and still on the old server in `~/db-backups`, which goes when the old site is deleted on the day.

**Not done:** a test restore of the old site from these files was not run (it would need somewhere to restore to). The checklist's "proved to open" is met by the gzip test, the table count and the full listing.

OWED BACK: nothing.
