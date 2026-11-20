**Needs from Chat: nothing. Your ruling is built and proved; the 14 or 15 older fails on each school page stay the school session's.**

# SHIP: the supporting line's bar wears the school colour on the seven school pages, in the gate (S538, 20 November 2026)

**What changed.** Gate commit 19b83f67. No page changed; the instrument did.
- **`tools/supporting_line_check.py`, the page side:** reads the page's school from the hero's class (the seven codes the switch in school-page.css keys on), and, on each line, the `--scol` in force there, resolved to rgb.
- **`tools/supporting_line_check.py`, `judge()`:** now takes the page's address. Its new `bar_colour_wanted()` holds the bar to the school's primary only where the address matches `^/academy/[^/]+/$`, the hero carries a school code, and `--scol` resolves on the line. Everywhere else it wants the orange, exactly as before. Width and gap are judged as before.
- **Every school colour pass is named,** for example: `line-bar: 2px, school colour (NLP primary), 16 from the words: Kain 19 November 2026, "Yes, they're right", school colour rule`. A failing bar on a school page names the school colour it wanted.
- **The citation** stands beside the DSRD 7 3.3 quote at the top of the tool.
- **`page_gate.py`:** passes the address in, and prints each named pass under supporting-line. No PAGE_EXCEPTIONS row was added, as you ruled.

**Proved able to fail.**
- **The test,** `tools/supporting_line_gate_test.py`, gains five cases, and all 15 pass:
  - the school's own primary passes and is named;
  - orange on a school page fails;
  - another school's primary on a school page fails;
  - a school primary on the Access All Areas Pass fails;
  - orange on the Pass page passes.
- **On the real pages,** through the gate's own mirror, at 1440, 8 lines each:

| Case | line-bar fails | Named school passes |
|---|---|---|
| NLP page as built | 0 | 8 |
| NLP page, bars forced to the brand orange | 8 | 0 |
| NLP page, bars forced to the CBP primary | 8 | 0 |
| Pass page as built | 0 | 0 |
| Pass page, bars forced to the NLP primary | 8 | 0 |

**The gate after:**
- On the seven school pages, `line-bar ... not the orange token` fails now number 0, against 24 a page before. The named school colour passes number 63 across the seven.
- Each school page reads 42 or 43 passed and 14 or 15 failed. Those are the older fails, the school session's (word counts and capitals, the knowledge tree's 32, the film still not lazy, the record line).
- /access-all-areas/ reads 43 passed, 0 failed, on orange.

**The record.** One line is in the School Page DSRD6_RECORD.md, chapter 10, naming your answer and the commit.

**Yours, as you wrote:** the school colour rule into DSRD 7 section 2, with one line under the bar in 3.3.

*No em or en dashes in this file; checked before writing.*
