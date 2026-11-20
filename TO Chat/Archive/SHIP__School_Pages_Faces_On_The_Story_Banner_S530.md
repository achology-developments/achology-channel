DISPOSITION (Chat, Session 478, 20 November 2026): for the record. NLP's face wall goes on Backlog: Code's After Launch list (it needs portraits with rights). The tool's old tree words are the school session's to keep level. Archived.

**Needs from Chat: nothing to act on. For the record: a new look on six school pages (the faces on the story's banner), signed by Kain on the rendered round; and one change to the shared viewer proof.**

# SHIP: the faces on each school's story banner, on 0.708.274 (S530 side session, 20 November 2026)

**What changed.** Kain asked whether the Academy banner's wall of faces could come into the school pages, "showing the people that are kind of referenced within the schools ... We're not creating anything new". Four ways were rendered in the one Change Viewer on six school pages (round-face.js): The Strip, The Banner Wall, In Each Chapter, The Cast. He chose the Banner Wall: "the banner wall is exactly what I'm looking for. I think that's stunning", and asked it to "edge in a bit further" along the banner's top. Four depths were rendered (round-fwall.js); he chose Three Columns In: "Yes, build 3".

**What a reader sees.** The history block's banner (the sand panel with the chapter name, the year and the five stops) carries faces along its two edges, five columns of three a side, grey at half strength, fading toward the words across and toward the stops downward, where the banner's faint marks stood. On a tablet the two edge columns only; on a phone one faint column at the right. Nothing moves and no size or space changes.

**Whose faces.** Every face is one of the Academy wall's own, with that wall's crop. Each school's twelve stand at the edges: first the people its own history names, in story order (for CBP: Seneca, Ellis, Aaron T. Beck, Judith Beck, Hayes), then people its field drew on, then Kain, whom every history names in its last chapter. Further in, the Academy wall's best known fill the space. The lists are in tools/school_faces.py, overturnable line by line.

**NLP has no wall.** None of its founders (Bandler, Grinder, Erickson, Satir, Perls, Bateson) is among the theme's portraits; several are living, so their portraits need pictures with rights. Its banner is unchanged until those exist. Worth a line on Backlog: Chat if you want NLP to match.

**How.** tools/school_faces.py writes the wall; tools/school_page_data.py places it in each school's stored parts. Each of the six stored files differs from before by the wall alone (proved); NLP's is byte for byte unchanged. school-page.css draws it. The pictures are the small sizes, fetched only when near.

**Proved.** The built CBP banner matches the chosen round at 1440, and holds at 768 and 390 (WebKit). Both school colour checks pass on all seven. Deploy CURRENT at 0.708.274; commits 928bed60 (the build) and 7382a2eb, 9cef4e6f (the two rounds), pushed.

**Found on the way, for the record.** tools/school_page_data.py still writes the knowledge tree's older words (title "The [subject] Knowledge and Learning Tree") over the ones Kain signed on 19 November in data/school-page/knowledge-tree.json. This job kept the signed file as it was; the next session that rebuilds a school page must do the same, or the tool's words should be brought level with the signed file.

**The shared viewer proof.** tools/viewer_proof_run.js no longer fails a round when WebKit reports a request to the page's own site "due to access control checks", which is a request cut off as the viewer moves its frame on (the library cards, fetched as their block nears the screen since the clean-up at 0.708.266). It notes it instead. Every other page error still fails; the proof's acceptance test passes in full.

**Your S478 points for the school page session (ANSWER__Tray_Points_Settled_S478, section 4)** are taken next by this session, before Kain's whole-page signature: the record's chapter 7 line for the guarantee ring, and the 14 to 17 gate fails put to you by name.

*No em or en dashes in this file; checked before writing.*
