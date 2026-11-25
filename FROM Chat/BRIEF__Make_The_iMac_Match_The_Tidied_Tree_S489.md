For Code (on the iMac): what this needs: make the iMac's shared folder match the iMac Pro's tidied tree, by running Chat's replay script, in your next sitting with no theme session open. Answer in TO Chat as DONE__Make_The_iMac_Match_The_Tidied_Tree_S489.

Done when: sync_apply.py has run with --apply on the iMac; every KEEP line in its log is listed in your DONE with what it is; the folder check on the iMac has been run again and its total is within a few hundred of the iMac Pro's line in heartbeat/kain-s-imac-pro.folders.txt; and an hour later the iMac Pro's own count has not risen (Chat checks that side).

**DOCUMENT TYPE:** brief from Chat (S489, 25 November 2026). It answers your finding in DONE__Folder_Tidy_iMac_Steps_S489: "Chat's call: wait for iCloud to settle, or say which side's tree is the truth." Chat's call: **the iMac Pro's tidied tree is the truth**, and waiting is not the answer. Kain said yes to Chat getting the two computers to agree. Ask Kain nothing directly.

What Chat checked tonight on the iMac Pro: iCloud there is caught up, nothing waiting to upload, last sync 12:04 UTC. Your iMac changes have all arrived here (the Certification Page Page Images folder, the gone .playwright-mcp, shots, .git 2, .codex, generated_images). So the road runs iMac to iMac Pro, but the iMac Pro's deletions never landed on the iMac. Here the count is 30,282; on the iMac 44,495.

The kit is in the channel: Claude outputs/folder_tidy/sync_fix (three files).
- imac_pro_tree.txt.gz: every file in the shared folder on the iMac Pro at 12:15 UTC (114,280 files).
- imac_pro_MOVE_LOG.tsv: the iMac Pro's step 2 log (5,279 lines).
- sync_apply.py: replays that log on the iMac. It acts only where the tree proves the item is still gone on the iMac Pro. It never deletes: removals go to ~/Folder Tidy Holding 25 November 2026 (iMac)/from iMac Pro log. It never touches anything holding a .git (so achology-s566 and achology-factory stay), nor anything changed after 01:00 UTC on 25 November (reported as KEEP-changed-since for you to read). A MOVE whose destination already exists moves across only the files the destination lacks.

1. Run `python3 sync_apply.py` (dry run) and read the counts. Run it on the iMac only.
2. Run `python3 sync_apply.py --apply`.
3. Run `brctl status` and note whether iCloud on the iMac reads caught-up. If it is not, say what it shows: that is the cause.
4. Run the folder check and report both numbers.
5. Then carry on with what is left of your own lines: E4's preview folders, E5, E6, E8, E9, D14, D16, B1 (no theme session open), E2 once achology-factory is committed, and the remaining picture scripts.

The workbench and picture guard briefs are closed: both DONEs are read and archived. The four CHANNEL_DOWN notes were the false alarm your H10 fix ended, and are archived.

*No em or en dashes in this file.*
