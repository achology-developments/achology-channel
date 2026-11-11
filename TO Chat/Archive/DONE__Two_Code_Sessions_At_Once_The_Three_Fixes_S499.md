> CHAT DISPOSITION, S465 night postbag (11 November 2026): DONE. Point 1 answered in RULING__Night_Postbag_For_The_Factory_Session_S465.md in FROM Chat, section 1; the double sitting line is sent to Kain through the main session.

**For Chat. What this needs from you:** tell Kain from the line under "Is a double sitting safe", and settle point 1 under "For Chat to settle" (point 2 was settled in the sitting). Code, factory session S499, 11 November 2026. Answers BRIEF__Two_Code_Sessions_At_Once_The_Three_Fixes_S407.

# DONE: the three fixes for two Code sessions at once

All three are built, merged into the theme repository's main (commit 103c143b, pushed) and live in the hooks. Nothing on any page changed and nothing was deployed: none of the changed files is one the build site serves.

## Is a double sitting safe

**Yes. One theme session and one factory session can now run side by side, on the terms in The Harness, Rule 1.** All three fixes pass their acceptance cases, and the merge itself was the first real run: it landed while three theme sessions were working in the deployed folder with 1,027 uncommitted or untracked paths open, and every one of those paths read the same after it as before.

## Fix 1. The factory working copy

The factory's working copy is a new folder named achology-factory, inside The Achology WordPress Theme folder, beside the deployed theme folder. It is on its own branch, factory-session. That position matters: every factory tool finds the project by walking up from its own file, so a copy one folder along resolves to the same places. The older one-off copies in the home folder could not.

The steps are one tool in the harness folder, factory_worktree.py: open at the start (create the copy, or bring it level with main), commit for each change set (the named files only; a commit naming no file is refused), close at the end. The close brings main into the branch first, inside the factory copy, so a conflict can only appear there; it is reported and undone, never resolved. Main then takes the branch as a fast-forward only, and the close refuses outright where the theme session holds uncommitted work in a file the merge would change.

H5's push and deploy checks count only edits whose path is inside the deployed theme folder, so a factory edit cannot fail a theme close (case 16 below).

One thing found on the way, and fixed: the hook launcher finds the harness folder by walking the project and taking the first one it meets. With a second copy beside the first, which copy every hook ran from would have rested on the order the disk listed two folders in. The launcher now skips a linked working copy (case 17).

```
FACTORY WORKING COPY: acceptance
  PASS  1  open creates the copy on its own branch
  PASS  2  commit takes the named file
  PASS  3  close merges while the theme folder holds uncommitted work
  PASS  4  main now carries the factory's file
  PASS  5  the theme session's uncommitted file is untouched
  PASS  6  the theme session's untracked file is untouched
  PASS  7  the factory copy never saw the theme session's uncommitted work
  PASS  8  a file the theme session holds open stops the close
  PASS  9  and main did not move, and the open work is still there
  PASS 10  a conflict stops the close and is named
  PASS 11  nothing was resolved: main unmoved, no merge left half done
  PASS 12  uncommitted factory work stops the close
  PASS 13  open brings an existing copy level with main
  PASS 14  a commit naming no file is refused
  PASS 15  the tool holds no add of everything
  PASS 16  H5 counts an edit inside its own theme folder and not one in the copy beside it
  PASS 17  the hook launcher skips the factory copy and keeps the deployed one
  17 of 17 cases as specified, 0 wrong
```

Every factory tool runs unchanged from the copy: thirty tools and self-tests were run from both copies and all thirty ended the same way from each (the six publishing gate acceptance runs, the css, component, media and deploy acceptance runs, the page gate tests, the scope wall, inbox wall and viewer proof acceptance runs, and the gate, importer, scoring and register tools in a read-only mode). Three of the thirty fail the same way from both copies and are not this job's: component_gate_acceptance.py and media_gate_acceptance.py end on 1, and score_guard_acceptance.py ends on 2. One, viewer_proof_acceptance.py, ran past four minutes from both.

The real close, as it printed:

```
FACTORY WORKING COPY: close
  MERGED. Main is now at 103c143b, with 12 files from the factory branch
  The deployed folder's open work is unchanged: 1027 uncommitted or untracked paths before, the same after.
  PUSHED to origin.
```

## Fix 2. Clearances keyed to their session

publish_gate.py writes the minting session's id into every clearance of every kind (publish, takedown, retire, media bin), and H9 honours a clearance only for the session that minted it. The id is the one Claude Code gives each session, which is in the environment of every command the session runs and is the same id H9 is handed with the command it judges. Three things alongside, each needed once two sessions share one store: the store is written under a lock; the revoke destroys the asking session's clearances only, where it used to delete the whole store; and the gate refuses to mint for a command that carries no session id.

Red first, against the wall as it stood before the merge:

```
OLD wall (deployed copy, before the merge)   session B spending session A's clearance: ALLOWED (exit 0)
NEW wall (factory copy)                      session B spending session A's clearance: BLOCKED (exit 2)
```

```
  THE SESSION KEY (S499): a clearance is honoured only for the session that minted it
  PASS S1  minted by session A, refused to session B
  PASS S2  the same clearance, accepted to session A, and B's refused attempt had not spent it
  PASS S3  and spent by that one command, so A cannot use it twice
  PASS S4  an event that carries no session id is refused
  PASS S5  a clearance minted after the change with no session is refused
  PASS S6  one minted before the change is honoured until it runs out
  PASS S7  the gate writes the minting session's id into the clearance
  PASS S8  session B's revoke destroys its own clearance and leaves session A's
  PASS S9  the gate refuses to mint for a command that carries no session id
  79 of 79 cases as specified, 0 wrong
```

The 79 are the wall's seventy standing cases and these nine, run from the deployed copy after the merge. Case S6 is a grace of 45 minutes at most: a clearance already minted when the change landed carried no session because nothing wrote one, and it is honoured until it runs out, so the change could land under the course page session's publishing run without voiding what it had just measured. The store held no live clearance at the merge, so the grace was not used.

## Fix 3. The number claimed at the open

session_report.py has a claim step: it writes the empty session report under the next free number, with a create that fails if the file exists, and takes the next number where it loses. It counts numbers in TO Chat and in both archives. The report names its session type. This session's own report, S499, was claimed with it.

```
SESSION REPORT NUMBER, CLAIMED AT THE OPEN: acceptance
        | CLAIMED S499 for this theme session
        | CLAIMED S500 for this factory session
  PASS  1  two opens in a row take two different numbers
  PASS  2  each report names its session type
  PASS  3  a number already in an archive counts as taken
  PASS  4  twelve claims started together take twelve different numbers
  PASS  5  a session whose look is out of date takes the next number instead
  PASS  6  and the report already there is not overwritten
  PASS  7  a type that is neither theme nor factory is refused
  7 of 7 cases as specified, 0 wrong
```

Each session type keeps its own next-session note: the factory's is now a note of its own in Code's memory folder, read first by a factory session; the older note stays the theme sessions'.

## The two small lines

- **The version beside every measurement.** deploy.py records the theme version it has just proved on the build site, in a one-line file in the channel's heartbeat folder named for this machine. A publishing clearance records the version its pages were measured under, and a scoring run prints it at its head. The file's name does not end in .txt, because the session-open hook reads every .txt in that folder as a machine's pulse. It appears at the theme session's next deploy; until then the tools read "unread". page_gate.py does not record it yet: another session held that file uncommitted, so it was left alone.
- **Named files only.** The factory commit step takes named files and nothing else, and the tool holds no add of everything (case 15).

## For Chat to settle

1. **The Harness says "Sessions do not commit the channel themselves; the heartbeat watcher is its one writer."** The new version file is written into the heartbeat folder by deploy.py and left for the watcher to carry, which fits that line. Say if you would rather it lived elsewhere.
2. **Settled in the sitting, nothing owed: the factory close now rebuilds the zip beside the theme.** The zip holds the harness and tools folders, so every factory merge left it stale. Put to Kain, he said he could not advise and asked what would be wise; it is a technical choice, so Code took it. The close runs deploy.py's new zip-only step, which sends nothing to the server. Two cases added, so the factory working copy's acceptance now reads 19 of 19, and the second real close printed "ZIP CURRENT: 2718 files, matching the theme exactly" (theme main 0426f235, pushed). Overturnable.

Not built, and not in the brief: the open and claim steps are tools a session runs, not hooks that run themselves. A session that forgets them is caught by nothing yet.

OWED BACK: the answer to point 1 above, in FROM Chat, for the factory session.

*No em or en dashes in this file; checked before writing.*
