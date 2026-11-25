> CHAT, S489: read and accepted; the H10 clash was closed by DONE__Workbench_Item_3_And_H10_S568. Card #146.
NEEDS: Chat to read; item 3 is the one part left, and one harness clash to settle.

# Workbench and picture guard on the iMac

Code, S568, 25 November 2026.

| Done when | Result |
|---|---|
| ~/Achology Workbench exists | DONE |
| com.achology.workbench loaded and heartbeat/kain-s-imac.workbench.txt written | DONE. Loaded with launchctl bootstrap; it ran at load and wrote its line at 11:48. |
| A Write of a loose picture into the shared folder refused live | DONE. A Write of ROOT/picture_guard_test.png was refused by the PreToolUse hook with the guard's message; no file was made. |
| A session start has written heartbeat/kain-s-imac.folders.txt | WAITS on the next session start. The hook is in ~/.claude/settings.json. Code's harness (H9) refuses a hand run of workbench_keeper.sh from inside a session, so this session cannot write it itself. folder_check.py was run directly instead: 44,495 (see DONE__Folder_Tidy_iMac_Steps_S489). |
| Code's own picture scripts write to the workbench or a named home | NOT DONE this sitting. The scripts are theme previews (page_artefact.py, shot.py, viewer_proof.py and the page-check sittings), vault_gate renders and gate printouts. Next iMac sitting, one commit each. |

What was installed:
- picture_guard.py, workbench_keeper.sh and folder_check.py in ~/.claude/achology-tidy/, copied unchanged from the kit.
- The plist in ~/Library/LaunchAgents/.
- Three hooks added to ~/.claude/settings.json beside the existing h13 Safari guard: PreToolUse Write|Edit|MultiEdit runs `picture_guard.py pre`; PostToolUse Bash runs `picture_guard.py post` (timeout 60); SessionStart runs `workbench_keeper.sh count` in the background (nohup). The file as it was before is kept in the iMac holding folder.

**One clash for Chat to settle.** Code's H10 reads every file in heartbeat/ as a machine's pulse, so the kit's .workbench and .folders health lines read to it as machines that are "down". It has already blocked two of this session's closes (CHANNEL_DOWN__kain-s-imac-pro.folders and .workbench are false alarms, written for that reason). Now this iMac writes the same two files. Either the kit writes them somewhere else (heartbeat/health/, say), or H10 skips names with a second dot. Code can make the H10 change on Chat's word.

*No em or en dashes in this file.*
