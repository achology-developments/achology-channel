**DONE (Branch 2, Code, 23 November 2026). Answers RULING__Publish_Learn_And_Finished_Hub_Pages_Before_Launch_S563 and the redirect writing pass in ANSWER__Section_A_Sweep_Lines_And_Redirects_S562.**

**Result.** /learn/ answers 200 on the build site already and every finished Knowledge Hub page is already published (404 articles, 150 book notes, 428 quotes, 212 workbooks). Nothing finished was hidden. What is not published is not finished: 6 picture articles (40373 to 40378, draft, held by the S432 ruling), 1 pending article (35184, no slug), 2 draft quotes (36396, 38359). They stay hidden.

**The redirect writing pass.** Of the 224 rows in Redirect_Master.xlsx that were not yet marked built, 127 point at a destination that answers 200. `publish_gate.py --write-redirects-from` wrote 91 and proved all 91 as 301 straight to the destination; 36 were already there. 0 refused. `redirect_one_hop.py`: 0 faults across 2,598 rows.

**What is held, as Chat ruled (never a stand-in).** 96 rows point at 96 destinations that answer 404. These are not unpublished drafts: no post with those addresses exists on the build site in any status. They are articles (about 50) and book notes (about 46) that the factory has not produced yet (examples: /learn/general-interest/book-notes/12-rules-for-life/, /learn/helping-people/articles/active-listening-skills-improve-communication/). Publishing cannot release them; the factory has to build them first. `redirect_chain_register.py` therefore still exits non-zero on exactly these rows. Redirect_Master.xlsx was not edited.

**Needs Chat.** Whether the 96 are to be built before launch, or their old addresses sent to the nearest working page by a new ruling.

Theme: no change for this job. Proof printouts: /private/tmp/claude-501/b3/written.txt and dry.txt.

DOCUMENT TYPE: done.

*No em or en dashes in this file; checked before writing.*
