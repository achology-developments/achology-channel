> CODE DISPOSITION, S530: WAITS ON the other theme sessions (Events, Academy, About) reading it; read whole by the school page side session.
NEEDS FROM CODE: nothing; this tells every theme session the H5 push check now blocks a session only on theme files it edited itself and has not committed or pushed (Kain, S531: "Yes, ask Chat"); theme commit 5bc90684, on origin.

Done when: each theme session has read this line; nothing else is owed.

# DONE: the push check counts only this session's files

**For:** Code, every theme session (Events, Academy, School, About). **From:** Chat, 18 November 2026, answering ASK__Push_Check_Counts_Only_This_Sessions_Files_S531.

**The rule.** A tracked uncommitted file blocks a session only when that session edited it (H4's ledger) and the edit is still uncommitted: the file still holds exactly what the session's last edit left, or no commit has carried it since that edit. Unpushed commits block only when one holds a file as this session left it. An unreadable repo, and any fault in the check itself, still block. Other sessions' work in progress, in a file you never touched or in a shared file such as style.css that you edited and committed before it changed again, no longer stops your turn.

**Why not the H2 declaration.** It names what a session may touch, and sessions often declare the same shared files, so it would have kept the cross-blocking exactly where it began.

**Known limit.** H4 sees the edit tools only, so a theme file changed through the shell is not in the ledger. That was already true: the check never armed on a shell write alone.

**Proof.** harness/h5_push_scope_acceptance.py, 21 cases both ways, driving the real H4 to write the ledger, written after an independent review whose findings (a partial commit passing on time alone, an unpushed shared file still cross-blocking, a crash that passed) are all fixed and re-read with no blocker. The real Stop hook through its launcher: a session owning an uncommitted about.css was refused (exit 2) and a session owning only a committed file passed (exit 0) while other sessions' files sat uncommitted.

**Found on the way, not mended here.** `git status` in the theme now takes about two minutes: 90 seconds of it is git re-reading every file's state ("refresh index"), on every run. The push check gives git 15 seconds, so while this lasts every theme session's check says the repo could not be read and blocks. That was true before this change too. The cause is on this machine's disk, not in the check; worth a look by whoever next touches the theme's git setup.

The two smaller points in the ASK (the deploy check's time-only differences; the Rule 13 notice every turn) are on Backlog: Chat.

Also committed in the same change: the "nearly is not a claim" line in harness/h5_completion.py from Chat's S475 session, so H5 and the sister check in Enforcement Gates agree.

*No em or en dashes in this file; checked before writing.*
