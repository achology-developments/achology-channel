NEEDS: Code to put the hidden "(opens in a new tab)" note inside every new-tab source link on the seven school pages and the Access All Areas Pass page, rebuild their stored data, and gate each page after. Nothing visible changes.

# SWEEP BRIEF: the source links' new-tab note on eight pages

**From:** Chat, 19 November 2026. **To:** Code. **Signed:** Code asked Kain in its S538 theme session, "Shall the source links' note go on the school pages and the Pass page too?", and Kain answered **"Yes, all of them"** (19 November 2026). This is the signed sweep brief Harness Rule 3 needs, the record of his word.
**Answers:** mend 2 of ANSWER__Academy_Page_History_Gate_Rulings_S538, which Code made on the Academy only at 0.708.256, because the sweep needed this brief.

## The pages, exactly eight

1. The School of Neuro-Linguistic Programming (data/school-page/nlp.json)
2. The school whose data is cbp.json
3. The school whose data is pc.json
4. The school whose data is lc.json
5. The school whose data is mh.json
6. The school whose data is miw.json
7. The school whose data is pgd.json
8. The Access All Areas Pass page, /access-all-areas/

Each school page is the one at /academy/{its school}/ that school_page_data.py builds from that file; Code's own map of file to address holds, and the names are DSRD 5's. knowledge-tree.json in the same folder is not a page and is not in this sweep. The Academy page is done already and is not touched.

## The change

- **School pages:** in `tools/school_page_data.py`, the `source()` function puts the note inside each new-tab link, in both of its link forms (the bare address and the "doi:" form), just before `</a>`, exactly as on the Academy at 0.708.256: `<span class="screen-reader-text"> (opens in a new tab)</span>`. A source with no link gains nothing.
- **The Pass page:** in `tools/pass_page_data.py`, its `sources()` does the same to each new-tab source link.
- No word anyone sees changes, and no other link changes. The link's address, its visible text, `target` and `rel` stay as they are.

**What it derives, named before it runs (Harness Rule 3).** The stored data each script writes for its eight pages, and the html each page publishes from it. Nothing else reads these links: no record cross-links to them, and no transcript, caption or file is derived from them.

## Done when

Every new-tab source link on the eight pages, read back on the build site, carries the hidden note inside the link, and none shows it on screen. Each page's stored data is rebuilt, and each page's DSRD 6 gate is re-read after with no new fail. The count of links changed is given for each page.

## OWED BACK

One SHIP naming, for each of the eight pages, the links changed, the gate's result after, and any page refused with its reason.

*No em or en dashes in this file; checked before writing.*
