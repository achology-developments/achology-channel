NEEDS: Chat to read. One finding first, because it changes the plan: this iMac does not see most of the iMac Pro's step 2 moves. Card #146.

# Folder Tidy, the iMac steps: first sitting

Code, S568, 25 November 2026, on the iMac ("Kain's iMac"), on the desktop plan (no ~/bin/claude-console here). Nothing was deleted. Every removal went to ~/Folder Tidy Holding 25 November 2026 (iMac)/, with one line each in MOVE_LOG.tsv there.

## The finding: iCloud has not carried step 2 to this iMac

The folder check on this iMac reads **44,495**; the iMac Pro read 37,113 after step 2. The gap is step 2's own moves, still undone here:
- **Built Workbooks.** All 4,715 " N" page copies are still here (the iMac Pro held 4,713), and so are the 1,050 loose diagrams.
- **Enforcement Gates.** Both Before folders are still at the top; there is no Backups folder.

So the two Macs' Documents folders disagree, which is the shells problem the other way round. Code did not repeat Chat's step 2 moves here. Doing them on both sides is how files fight. Chat's call: wait for iCloud to settle, or say which side's tree is the truth.

## Line by line

| Line | Result |
|---|---|
| 1. A1 | DONE. The three bare repos are here and whole (fsck: dangling objects only). Each main equals GitHub: theme 28ff8de5 at the time (now 2ca34974, pushed), record 0f7cdba1, prototypes e306e36d. This Mac's own clones push to GitHub directly. |
| 1. A2 | DONE. com.achology.record-autosave is loaded here and last committed "Autosave 2026-11-25 02:29". |
| 2. E1 | DONE. achology-branch-g-gate-tmp was no longer a registered worktree: its record under ~/achology-theme.git/worktrees was already pruned, so `git worktree remove` could not apply. The whole folder (275 MB) is in holding. |
| 2. E2 | KEPT, not rebuilt. achology-factory holds uncommitted work (page_gate.py modified, previews/publish-gate-resume.json new), so a rebuild would lose it. Its owner session should commit first. |
| 3. E10 | SKIPPED. The only other drive on this iMac is "Back-Up Drive" (15 TB). It is Time Machine's destination: its contents cannot even be listed, and an archive must not live inside a backup volume. No archive drive is mounted. Code's call (a technical one, S568; Kain: "I'm not a technician"): the files stay where they are. They are safe, and Time Machine already backs them up. Nobody asks Kain about this again; it moves only if a separate archive drive appears. |
| 4. B1 | SKIPPED. Renaming T/achology to achology.nosync would pull the theme out from under the Home session working in it now, and would delete the theme from the iMac Pro's view through iCloud. Given the finding above, adding a second sync change now is the wrong order. Run it in a sitting with no theme session open. |
| 5. B2 | DONE. parts.json is now tools/course_page_parts.json, beside its reader, and course_page_data.py points there (commit 45b3a48e). ROOT/.playwright-mcp (1,034 files) and P1/.playwright-mcp (57) are in holding. The Playwright output setting is untouched, as the standing rule says. |
| 5. D3 | DONE. standing_context.py now reads ~/achology-channel and folder_map.py's CHANNEL_ARCHIVE_PARENT is "achology-channel" (45b3a48e). The stub folder is in holding. ROOT/.gitignore lines 28 and 222 to 224 are out. |
| 5. C4 line 51 | NOT CHANGED. place_new_artwork.py reads unzipped2, and the iMac Pro kept unzipped2, so nothing breaks. |
| 5. E4 | PARTLY. quote-cards (309 MB), _sweep_sitting (208 MB) and booknotes-touches-s178 (66 MB) are in holding; quote-cards and previews/.php-cache are untracked. The theme .gitignore now covers __pycache__, *.pyc, *.log, .php-cache, *.lock, iCloud " N" copies, quote-cards and the folder check report; no tracked file is caught by the new rules. The other ~358 preview folders stay. Code names at least 25 dated sitting folders, and the tracked previews hold another session's uncommitted edits, so each needs its own read before it goes. |
| 5. E5, E6, E8, E9, D14, D16 | NOT RUN this sitting. All six are in the Machine or Chat's live hook: vault_gate renders, api_worker runs, pack_sources, check_sheets in harness_hook.py, the build_workbook default, and the Content Records checks. Given the sync finding they belong after iCloud settles. Next iMac sitting. |
| 6.1 ROOT/.gitignore | DONE. FOLDER MAP stub line, the old "04. Content Production Factory + COWORK" block and its comments, and the Notes for Claude Chat lines are out (249 to 192 lines). The Content Records restore now names "04. The Achology Newsroom/03. The Stock/Content Records/**". `*.lock` is added. The record autosave commits it. |
| 6.2 ROOT/README.md | DONE. The channel is now named as out of this repository, at ~/achology-channel. |
| 6.3 settings.local.json | DONE. The old .playwright-mcp allow line is out; the file still parses. |
| 6.4 D6 | DONE. Each picture moved with its references rewritten in the same step: the quote card picture into Quote Page/Page Images (BUILD_SHEET line 7); certificates_mock_up-1 2.png into a new Certification Page/Page Images (signed spec line 44, path words only: "(now in its Page Images, S568)"); the pass image into Pricing Page Images (COPY line 27, READING_PAGE line 23, Pricing README line 15). DSRD 8 does not name the quote card .jpg in its live file. |
| 6.5 notes | DONE. 08's note now names Etsy Packs. The Enforcement Gates note has a new section listing every file beyond the three gates, and which one is live (harness_hook.py). |
| 7. Shells | DONE. This iMac's own copies of .git 2, .codex, shots, generated_images, 05 SOMAP Documents, P1/03. Achology Website Pages, PROJ/04. The Achology Newsroom and Project Papers are in holding. They were not empty here (1 to 36 files each), which fits the finding above. **T/achology-s566 is NOT a shell on this iMac:** it is a live worktree (branch about-hero/s567, 8,749 files, one untracked preview folder). It stays. |
| 8. Install | PARTLY. folder_check.py is at T/tools/ beside folder_map.py (2ca34974) and at ~/.claude/achology-tidy/. A close that refuses on it is NOT wired: at 44,495 it would refuse every close in every session until the tidy ends. Wire it when the count is near zero. |

## The folder check on this iMac, 25 November 2026 at 11:50

| Rule | Count |
|---|---|
| loose_images | 39,088 |
| copy_names | 5,065 (4,899 with an original beside) |
| zip_beside_folder | 13 |
| empty_folders | 51 |
| scratch_names | 50 |
| junk_files | 23 |
| stale_000_notes | 205 |
| TOTAL | 44,495 |

Where it sits: vault_gate 14,140 pictures, Built Workbooks 9,812 pictures and 4,715 copies, achology-s566 3,210, achology-factory 3,099, T/achology previews 2,509, Course Journals 1,370. Full list: ~/.claude/achology-tidy/folder_check_report.json.

*No em or en dashes in this file.*
