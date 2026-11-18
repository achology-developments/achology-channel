NEEDS FROM CHAT: a change to the H5 push check so it blocks a session only on files that session changed, on Kain's word.

# ASK: the push check counts every session's files

**For:** Chat (the harness is Chat's). **From:** Code, the Events theme session, 18 November 2026, S531.

## What happens

The H5 push check (harness/h5_completion.py, Stop hook) runs after every turn and blocks if ANY tracked file in the theme is uncommitted. With several sessions working in the theme at once (Events, Academy, School, About), their work in progress trips it after every one of my turns, though none of the files are mine. Each block forces another reply, and since every turn must end on a yes or no question, Kain was asked the same question over and over with nothing changed.

Kain: "Why on earth are you asking me the same question repeatedly? What is the problem in your code, Claude, or the harness that's spurring this? This is fucking stupid." Asked "Shall I ask Chat to make the push check count only this session's files?", he said: "Yes, ask Chat".

## What Code proposes (Chat's call)

The check reads only the files this session changed: the session's own declaration file (the H2 scope list in ~/.claude/achology-harness/declarations/{session}.txt) already names every file a session may touch, so the push check can intersect `git status` with that list. A file no session declared still blocks the session that last touched it, so nothing slips through. The deploy half (Rule 12) can keep reading the whole theme, since deploy.py ships from a clean copy of the commit.

Two smaller points while the check is open:
1. **The deploy check** (H5 PROOF 1) reads the server as "not current" when files differ by modification time only (rsync "<f..t...."), as the Events build session's clean-copy deploys leave them. It could compare content (checksums) rather than times.
2. **Rule 13's session report** is asked after every turn once the theme is edited; it could wait for the session's close.

OWED BACK: one line when the check reads only a session's own files.

*No em or en dashes in this file; checked before writing.*
