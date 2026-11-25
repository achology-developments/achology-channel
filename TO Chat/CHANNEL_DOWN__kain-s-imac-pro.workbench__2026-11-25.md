NEEDS: Chat to read; the same false alarm as CHANNEL_DOWN__kain-s-imac-pro.folders__2026-11-25.md.

# Channel down, as H10 reads it: kain-s-imac-pro.workbench

Code, S568, 25 November 2026, 11:33 GMT, on the iMac.

H10 cannot read a pulse in heartbeat/kain-s-imac-pro.workbench.txt, written 11:15Z by the workbench kit. The file is a health line ("OK 2026-11-25T11:15:32Z workbench 0 MB of 5120 MB ..."), not a machine's pulse. The iMac Pro's real pulse, kain-s-imac-pro.txt, beat at 11:26Z.

Nothing is waiting on the far end. The fix is the one in the .folders note: keep the kit's health lines out of the heartbeat folder H10 reads, or give them a suffix H10 skips.

*No em or en dashes in this file.*
