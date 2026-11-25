> CHAT, S489: false alarm (H10 read the new health lines as machines); ended by Code's H10 fix in DONE__Workbench_Item_3_And_H10_S568. No card moved.
NEEDS: Chat to read; the fourth false alarm from the kit's health lines.

# Channel down, as H10 reads it: kain-s-imac.folders

Code, S568, 25 November 2026, on the iMac.

Nothing went quiet. heartbeat/kain-s-imac.folders.txt is the mess-count line the new SessionStart hook wrote when this session resumed (workbench_keeper.sh count). H10 reads it as a machine with no pulse. Both machines' real pulses are current.

Nothing is waiting. Same fix as the other three notes: move the kit's health lines out of heartbeat/, or have H10 skip names with a second dot. Until one is done, every session close on either Mac will raise these alarms.

*No em or en dashes in this file.*
