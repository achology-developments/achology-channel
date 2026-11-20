NEEDS: Code to teach `tools/supporting_line_check.py` that on the seven school pages the supporting line's bar wants the school's own primary (`--scol`, read on the line itself), report each such bar as a named school colour pass with Kain's words, and keep the brand orange as the want everywhere else, Access All Areas included. Do not carve the line-bar rows out in PAGE_EXCEPTIONS. Do not turn the bars back to orange.

Done when: the gate on all seven school pages reads no `line-bar ... not the orange token` fail and prints each bar as a named school colour pass; a bar in orange or in another school's colour on a school page fails, and a school colour on /access-all-areas/ fails, each proved once on the mirror; and the School Page DSRD6_RECORD.md, chapter 10, carries one line naming this answer.

# ANSWER: school colours and the supporting line's bar (Chat, S538, 20 November 2026)

Answers Code's flag in SHIP__School_Story_Figures_S538 (TO Chat): 24 `line-bar ... not the orange token` fails on each of the seven school pages at theme 0.708.263, every block's supporting line at desktop, tablet and mobile.

## The ruling: (a), a recorded exception on the school route, matched by the instrument

The bar is right. It wears the school's colour because Kain signed that it should. The gate is behind the page, not the page behind the gate.

## Its ground, in Kain's words

- He asked for one strategy before anything was built: "It can be subtle, but it needs to be consistent".
- Code put all 147 marks on one map, COLOUR_MAP__School_Pages_School_Colours_19Nov.html (School Page folder). The map's rows for every block read "The rule beside the supporting line. Today: Orange. Under the rule: School colour." Kain: "Yes, build it".
- On the built pages at 0.708.257, 19 November 2026: "Yes, they're right". After the price section change, at 0.708.258: "Yes, it's right". The rule as he signed it: "On a school page every marker is the school's colour; only the things you press stay orange", the primary "for lines and fills (rules beside supporting lines, ...)". Source: SHIP__School_Pages_School_Colours_S530 (TO Chat).
- DSRD 7 section 3.3 names the bar "a 2px orange edge (`--color-orange`)". That was written before 19 November, for the site. On the seven school pages Kain's later signature replaces orange with the school's primary for this one mark. The width, the hang and the 16 (8 on a phone) are untouched: "It is a colour change only: nothing moves and no size or space changes."

## Why not (b) or (c)

- **Not (c).** The bars are what Kain signed twice. Turning them back would undo his signature.
- **Not (b) on its own.** Reading `--color-orange` at the line would pass any page that redefines the token locally, signed or not, and pass it silently. The gate exists to catch a look nobody signed.
- **Not a PAGE_EXCEPTIONS carve-out of the line-bar rows.** That row also judges the bar's width and its gap. A carve-out would hide a wrong width or a wrong gap on all seven pages from today on.

## Exactly what Code changes

1. **In the measuring script** (`supporting_line_check.py`, the page-side function), for each line also read, on the line element itself, its computed `--scol`, resolved to rgb the same way `token` is now. Read which school the page is from the hero's class (`.course-hero.school--nlp`, `--cbp`, `--lc`, `--pc`, `--miw`, `--mh`, `--pgd`), the same seven codes the switch in `school-page.css` keys on (about line 1360). Pass both into the record.
2. **In `judge()`**, the colour the bar is held to:
   - if the page's path matches `^/academy/[^/]+/$` AND the hero carries one of the seven school codes AND `--scol` resolves on the line: the bar must equal that school's `--scol`. Width (2px) and gap (16, 8 on a phone) are judged exactly as now.
   - everywhere else, the root `--color-orange`, exactly as now.
   So the Access All Areas Pass, which shares the template and has no school code, still wants orange, and a school colour there fails. A bar in any other colour on a school page fails. A school page whose bar is still orange fails too, because the rule is consistent or it is nothing.
3. **Report it by name, never as a silent pass.** When the school rule decides the row, the gate prints it as passing on the named rule, for example: `line-bar: 2px, school colour (NLP primary), 16 from the words: Kain 19 November 2026, "Yes, they're right", school colour rule`. A failing bar on a school page names the colour it wanted, the school's primary.
4. **Carry the citation in the tool's own text** beside the DSRD 7 3.3 quote at the top of the file: on the seven school pages, the school's primary in place of orange (Kain, 19 November 2026, school colours signed on the built pages; Chat, this answer).
5. **Prove the instrument can fail** before you trust it: on the mirror, set one school page's bar to the brand orange and one to another school's primary; both must fail. Set the Access All Areas Pass bar to a school primary; it must fail. Put them back.
6. **Run the gate on all seven and on /access-all-areas/.** The 24 line-bar fails a school page go; the 14 older fails stay and stay the school session's. Write one line in the School Page folder's DSRD6_RECORD.md, chapter 10: the line-bar row now holds the bar to the school's primary on Kain's signed school colour rule, with this answer named.

## Chat's own part, not Code's

The school colour rule is not yet in DSRD 7 section 2, which SHIP__School_Pages_School_Colours_S530 asked for. Chat writes it there, with one line in section 3.3 under the bar saying that on the seven school pages the bar wears the school's primary. Code does not wait on that to change the instrument: this answer is the ruling it cites.

*No em or en dashes in this file; checked before writing.*
