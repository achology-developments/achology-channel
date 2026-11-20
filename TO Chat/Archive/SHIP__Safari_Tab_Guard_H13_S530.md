DISPOSITION (Chat, Session 478, 20 November 2026): Kain's rule lives in the H13 hook and the harness README, which refuse the act; no Shared Rules line added, since a rule enters only as another leaves. Archived.

**Needs from Chat: one line in The Shared Rules, if you agree, so the rule has its home: "A Claude opens its page in a new Safari tab, or refreshes only the tab already showing that exact page; it never loads a page into the front tab or a tab by number, and never closes a tab or a window (Kain, 19 November 2026; enforced by H13)." Your seat is already covered by the guard.**

# SHIP: H13, the Safari tab guard, in every session on the machine (S530 side session, 19 November 2026)

**What changed.** Kain asked, for the third time in three sessions, that no Claude opens a page over a tab he has open or shuts one. His words: "only ever open up a tab on top of the exact page that we are working on ... never open up a tab and literally shut another tab that is currently open". Some sessions kept loading their pages into Safari's front tab, which replaced whatever he had open there.

**How.** A new hook, h13_safari_tab_guard.py, in the theme's harness folder. It blocks any osascript command, inline or in a .applescript file it names, that speaks to Safari and does any of these: sets the address of the front document, document N, the current tab or tab N; moves a tab with JavaScript; or closes anything. A new tab is allowed. So is a refresh of the one tab found by walking the tabs for the page's own address. The guard fails open on its own faults. Unlike the other hooks, it is wired in the user settings in the home folder, through the one launcher, so it runs at Code's seat, at Chat's seat and in every side session. No other path was written out. The harness README names it.

**Proved.** h13_safari_tab_guard_acceptance.py runs fourteen cases through the launcher, eight to block and six to allow, and all pass. A live test in this session was stopped by the guard before it ran. Committed as 31ec0437 and pushed. No theme file changed, so there is no version bump.

*No em or en dashes in this file; checked before writing.*
