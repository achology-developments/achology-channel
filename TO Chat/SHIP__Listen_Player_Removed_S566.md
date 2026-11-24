For Chat: what this needs: one line in DSRD 7's icon registry retired (the audio icons), and nothing else; this is a ship brief for your record.

**DOCUMENT TYPE:** ship brief from Code (S566 side session, 24 November 2026). **Theme version:** 0.708.474, deployed with deploy.py, all three proofs current (server, zip and version agree). **Kain's word:** "yes" in the S566 main session, to "Shall I remove that switched-off audio player code from the theme too?", the same night the 250 Help audio files were deleted from the build site.

**What went, and nothing Kain can see changed.**
1. listen.js, the read-aloud script, deleted, and its enqueue taken out of functions.php. It was sent to every Help answer for nothing; it is no longer sent and the file is gone from the server.
2. The reading bar component in shared-parts.php loses the Listen control's markup and its five arguments (audio, timings, speaks, body, label). The bar now always draws the joined arrangement (writer first, then the facts), which is exactly how it drew without a control. The S109 and S110 rulings in its comments are kept.
3. The three site-wide audio icon functions left faq-icons.php: achology_icon_volume (Lucide Volume2), achology_icon_pause (Lucide Pause) and their shell achology_audio_icon_wrap.
4. The control's own CSS left components.css (.ach-listen, .ach-listen__btn and its icon, .ach-listen-active, and the two phone lines for them), and .ach-listen__btn left the secondary button family's selector lists in buttons.css and buttons.js. The bar's writer and facts rules keep their class names (.ach-listen-bar, .ach-listen__reader and the rest), because the bar still carries them.

**Proof.** Every element box on a Help answer, a book note, a quote article and an article, at 1440 and 390, measured before and after the deploy: 8 views, 0 elements moved, element counts equal. css_gate passes on components.css and buttons.css; every PHP file parses on the server's own PHP; no em or en dash in the added text.

**For your record, a finding (no action asked of Code).** No template calls achology_reading_bar() today, and none of the four page types measured draws the bar at all. The component stands, as the brief asked, but it has no caller. Whether it returns to a page, or goes too, is Chat's to put to Kain if it matters.

**Owed by Chat.** The DSRD 7 icon registry line (section 5.2, registered 14 July 2026) naming the three audio icons, Volume2, Pause and Square, for "any audio control anywhere on achology.com", now names icons the theme no longer holds. Code did not edit the DSRD.

*No em or en dashes in this file; checked before writing.*
