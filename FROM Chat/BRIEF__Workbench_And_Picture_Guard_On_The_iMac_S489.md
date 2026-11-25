For Code (on the iMac): what this needs: install the same workbench and picture guard on the iMac that now runs on the iMac Pro, in the same sitting as BRIEF__Folder_Tidy_iMac_Steps_S489. Answer in TO Chat as DONE__Workbench_And_Picture_Guard_On_The_iMac_S489.

Done when: on the iMac, ~/Achology Workbench exists; com.achology.workbench is loaded and has written heartbeat/kain-s-imac.workbench.txt; a Write of a loose picture into the shared folder is refused live; a session start has written heartbeat/kain-s-imac.folders.txt; and your own screenshot and render scripts (theme previews, vault_gate renders, gate printouts) write to the workbench or a named picture home, each listed in your DONE.

**DOCUMENT TYPE:** brief from Chat (S489, 25 November 2026). Kain's words: "Code has his own workbench on that computer. You have your own workbench on this computer. We have one shared file system that will then remain clean", with Chat "responsible for putting in place a mechanism that guarantees that the file system remains immaculate and in order constantly." He agreed a 5 GB limit, a seven-day clear, nothing on GitHub or in the cloud. Ask Kain nothing directly.

The kit is in the channel: Claude outputs/folder_tidy/workbench_kit (four files). Built and tested on the iMac Pro tonight.

1. Copy picture_guard.py, workbench_keeper.sh and folder_check.py to ~/.claude/achology-tidy/ on the iMac, and the plist to ~/Library/LaunchAgents/, then load it with launchctl bootstrap. It runs daily at 07:30 and at login: deletes workbench files older than 7 days, then the oldest until the workbench is under 5 GB, and writes the workbench health line.
2. Add the three user-level hooks to the iMac's ~/.claude/settings.json, exactly as on the iMac Pro: PreToolUse Write|Edit|MultiEdit runs `picture_guard.py pre` (refuses a picture in the shared folder outside a picture home); PostToolUse Bash runs `picture_guard.py post` with timeout 60 (names pictures a command left in the shared folder in the last ten minutes; it moves nothing); SessionStart runs `workbench_keeper.sh count` in the background (macOS will not let the daily job read Documents, so the mess count runs from Claude). Keep your own harness hooks as they are.
3. Point every script of yours that saves working pictures inside the shared folder at ~/Achology Workbench instead, or at a picture home folder (images, page images, assets, pages, an archive, or a name you add to ALLOWLIST in folder_check.py with its reason). These made most of the 37,000 items the check still counts.
4. Item 8 of the iMac brief stands: the check also runs at close, and a close refuses while it finds anything.

Known limit, named: the Bash check sees pictures that arrived through iCloud from the other computer in the same ten minutes. Its message says to leave those and tell the other seat. Neither seat moves a file the other one made.

*No em or en dashes in this file.*
