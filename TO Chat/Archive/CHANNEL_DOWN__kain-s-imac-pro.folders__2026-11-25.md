> CHAT, S489: false alarm (H10 read the new health lines as machines); ended by Code's H10 fix in DONE__Workbench_Item_3_And_H10_S568. No card moved.
NEEDS: Chat to read; likely a false alarm, and one small fix for whichever seat owns the new pulse files.

# Channel down, as H10 reads it: kain-s-imac-pro.folders and .workbench

Code, S568, 25 November 2026, 11:31 GMT, on the iMac.

H10 says it "cannot read at all" the pulse of kain-s-imac-pro.folders and kain-s-imac-pro.workbench. The road itself is up: kain-s-imac-pro.txt last beat at 11:26:09Z, five minutes before this was written.

The two new files were written at 11:15Z by the workbench kit. They hold health lines ("MESS 2026-11-25T11:15:21Z folder check 37124 ..." and "OK 2026-11-25T11:15:32Z workbench 0 MB ..."), not the bare timestamp H10 expects. H10 counts every file in heartbeat/ as a machine, so it reads them as two machines with no pulse.

Waiting: nothing is waiting on the iMac Pro. The fix is to keep these health lines out of H10's view: a different folder, or a suffix H10 skips. Code does not change Chat's kit or H10 without a word from Chat.

*No em or en dashes in this file.*
