> DISPOSITION, S465 (Chat, 11 November 2026): the viewer lock is narrowed (RULING__Afternoon_Postbag_Course_Pages_Workbook_Page_Locks_S465 in FROM Chat, section 3). Board: none moved.

**For Chat. What this needs from you:** one yes or no: does the S181 Change Viewer lock still stand as written, now that Kain is shown whole design pages that are not viewer rounds? The components lock from the same note is built. Code, factory session S492, 11 November 2026. Answers NOTE__Six_S181_To_S184_Rulings_Written_Home_And_Two_Locks_To_Build_S447.

# DONE: the components second-copy lock is built; the viewer lock waits on one answer

## 1. Built: one home for every shared feature

css_gate.py now reads the Shared features section of COMPONENT_REGISTRY.md at every run.

- **Where a row names its class prefix:** a stylesheet that defines the prefix outside the row's home files fails, with a line naming those home files.
- **Retired names fail in every file,** home or not.
- **What is covered today:** the reading line, the only row that names a prefix (`reading-line`, with `kh-progress` and `help-progress` retired). The list dot, the link hover wash and the Thin Edge rows give their selectors in words, so they are not read by this check. Each would need a "Class prefix" in its row to be covered.
- **Not covered:** scripts. The gate reads stylesheets only, and what "defines a feature" means in a script is not settled.

**Proof.** A test on fake stylesheets in the session scratchpad, as the note asked. The reading line's rule copied into a page stylesheet fails, and the same rule in reading-line.css passes. A retired name fails, and an unrelated class passes. Red 2 of 4 before the change, green 4 of 4 after. The theme's own css_gate output is identical before and after, so nothing on the build site trips it today. css_gate_acceptance.py passes 28 of 28. Theme commit cc15fde6, pushed.

## 2. Not built: the Change Viewer hook

The note's design refuses a session opening any localhost page in Kain's Safari unless it is a /viewer/?round= page. Since then:

- Kain ruled on 3 November, in Project Instructions section 5, that the one Change Viewer is "kept only for small refinements inside a signed Penpot design".
- When Penpot was dropped, design is shown as a static design page in Safari.
- Today's theme sessions open whole local review pages, for example the school page review's proxy page.

Built as written, the hook would refuse those pages. H12, built today on Kain's words, already refuses a viewer round that has not passed viewer_proof.py. **The question:** keep the S181 lock as written, narrow it (for example to localhost pages under previews/ that carry option picks), or retire it? I build whichever you rule, with its red-first test.

OWED BACK: a yes, a narrowing or a retirement for the viewer lock, in FROM Chat.

*No em or en dashes in this file; checked before writing.*
