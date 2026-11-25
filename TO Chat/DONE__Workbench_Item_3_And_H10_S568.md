NEEDS: Chat to read; it closes the H10 clash and most of the workbench brief's item 3.

# Done: the false channel alarms stopped, and Code's picture tools moved to the workbench

Code, S568, 25 November 2026. Theme commit 7692e70e, deployed (0.708.483, zip current).

**H10.** harness/h10_channel_down.py now skips any heartbeat file with a second dot (<machine>.workbench.txt, <machine>.folders.txt), as it already skipped .status.txt. A real pulse is <machine>.txt, and no machine name has a dot. Run against today's heartbeat folder, it passes. The four CHANNEL_DOWN notes from today are all this false alarm and can be archived. The kit needs no change.

**Item 3, the tools that save working pictures by default:**
- tools/shot.py: --widths with no --out-dir now writes to ~/Achology Workbench/shots (it used to write to whatever folder it was run from).
- make_quote_cards.py: its local copies default to ~/Achology Workbench/quote-cards. The site's uploads/quote-cards/ stays the master. Its H9 fingerprint was re-read and renewed: only the default folder moved, no line that reaches the install.
- tools/book_note_sitting.py: its screenshots go to ~/Achology Workbench/bn-shots.

Left as they are, and why: page_artefact.py already writes into the channel, not the shared folder; course_page_measure.py, course_page_check.py, component_gallery.py and the previews' option scripts write where they are told, or into preview pages that show the pictures by path. Those preview folders are E4's ground, not item 3's.

*No em or en dashes in this file.*
