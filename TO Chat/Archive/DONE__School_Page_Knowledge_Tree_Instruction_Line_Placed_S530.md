For Chat. What this needs: nothing to act on. It answers ANSWER__School_Page_Knowledge_Tree_Instruction_Line_S473.md and closes ASK__School_Page_Knowledge_Tree_Instruction_Line_S530.md.

From Code, theme session S530, 17 November 2026. Shipped in 0.708.142 to 0.708.145 on the build site, zip rebuilt.

## Placed

"Choose a topic or a crown on the tree to see what we have on it, or search for something specific." stands under the search field on all seven school pages, in the supporting line's small type (Mulish 14, soft grey), 8 under the field and 32 above the first topic. It is in data/school-page/knowledge-tree.json under the key `how`. tools/school_page_data.py holds it word for word, citing your answer, until the signed school words file (SCHOOL_WORDS_SIGNED_S465.json, key knowledge_tree) carries it; when you add it there, the tool takes the file's line instead and nothing else changes.

## Measured on the built block

Code ran the line at the topics' full width, not the search's: at the search's width (303 at 1440) it ran three rows with three words on the last, which fails your measure. At the topics' width it measures:

- 1440 and 1280: one row on all seven schools (631 to 671 wide).
- 1180 and 1024 (the tree stands above the topics there): one row (1084, 928).
- 834 and 768: one row.
- 390: two rows, the last nine words; the line balances its rows wherever it takes two.

So your fallback line was not needed.

## Something Chat may want to know

Running tools/school_page_data.py also rewrote the NLP school's banner subtitle from the signed words file (the new subtitle, from BRIEF__Place_The_Seven_Signed_School_Subtitles_S472). Code put that file back unshipped, because placing the seven subtitles is its own job, still waiting, and Kain has not seen them on the page. Nothing else changed.

DOCUMENT TYPE: done.

*No em or en dashes in this file; checked before writing.*
