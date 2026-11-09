> CODE DISPOSITION, S464: WAITS ON Chat's HOLD LIFTED line, then a factory session (read in full by the Certification theme session, which does no workbook work).
> STARTS ONLY WHEN Chat writes "HOLD LIFTED" on the line below this one. Until then, read it and ask questions in TO Chat, but build nothing. (The 86 are signed; the last strict rebuild is clearing short shared phrases, which may change a few words in a few records.)
> HOLD: not yet lifted.

**For Code. What this needs from you:** put all 86 signed workbooks on the build site, each with its landing page, its finished PDF, its cover picture and its search fields, then report in TO Chat. Chat, Session 460, 9 November 2026. This brief replaces BRIEF__Build_Import_And_Score_The_33_Signed_Mindset_Mastery_Workbooks_S458 (now folded in here) and lifts the document build hold that brief and the S442 queue carried.

## 1. What is finished and where it is

- **86 workbook records, every one signed by Kain** to the Workbook Standard (Sessions 458 to 461): 04. The Achology Newsroom/03. The Stock/Content Records/workbook. Read each record's fields, its Landing page body and its Page fields (new) table directly, as your importer already does; no upload CSV is needed (upload_contracts.json: "the upload CSV is retired as the import path").
- **86 finished document pairs** (PDF and HTML, one per record, named by the record's post_name): 04. The Achology Newsroom/03. The Stock/Built Workbooks. These are the final documents. Never rebuild them from records yourself, and never use any older copy.
- **The design every PDF follows** is The Workbook Design Standard (signed by Kain, Session 460), which now records every ruling, including the edge-to-edge cover photograph, the new page 2 Inside this workbook blocks, the bubble beside the page number and the sales back cover. Workbook orange #E2662B is a registered exception in DSRD 7 section 1.

## 2. What changed since your last workbook import (S206 and S458)

- **Every one of the 86 documents is new.** All 52 older workbooks were rewritten in full and rebuilt; their old PDFs, their `_pages` folders and the 260 files in Built Workbooks/webp (dated 2 November) are out of date and must be replaced, not reused.
- **33 Mindset Mastery workbooks (records 005-002 to 005-039) have no posts on the site yet.** They are new pages.
- **Karpman** (draft 44805) and **The Ladder of Inference** (draft 40321) exist as drafts and are updated in place.
- **One title changed, on Kain's word** ("Yes, small w", Session 460): 006-032 is now "Being Honest with Yourself Workbook: Free Worksheet" in post_title and rm_seo_title. Its address, honesty-with-yourself-workbook, and post 42895 are unchanged.
- **No address changed** anywhere (Kain kept every approved name and address). Every post_name in the records matches its PDF's file name.
- **The landing page body** of most records was rewritten to the 350 to 450 word band and the section standards of DSRD 2 section 1.7.

## 3. The job, in order

1. **Widen your importer** (02. The Machine/import_workbook_pages.py) from the 52 in vault_gate/briefs/workbooks_02/READING_LIST.json to all 86 signed workbook records in Content Records/workbook. A record counts only when its signed line carries Kain's signature; refuse any other.
2. **Make the pictures from the final PDFs, for all 86:** page 1 (the cover) and the four step sheets, rendered from each PDF in Built Workbooks into a `{slug}_pages` folder, then WebP at 816 px wide within DSRD 7 section 12.3's budgets (cover 60 KB, step sheets 80 KB). Replace the old webp files. The cover snapshot is the post's featured image, with the record's cover_alt as its alt text. If DSRD 9 section 37 or the theme also expects the 1200 by 630 share image (DSRD 7: "Workbook 3D renders"), make it from the same cover; if that export is not specified well enough to build without a decision, ask Chat in TO Chat and carry on with everything else.
3. **Push:** create the 33 new posts and update the 53 existing ones (posts 42727 to 43073 and the two drafts) with every field your importer already fills: post_content (the Landing page body), workbook_subtitle, workbook_parts, workbook_step_pages, source_course and associated_course, author, the rank_math title, description and focus keyword, the featured image, and pdf_file (upload the new PDF and attach it, replacing the old attachment so no old PDF stays reachable).
4. **Verify** every page with your importer's --verify, then the DSRD 6 page gate with its written record per page, and read Rank Math off each built page. Workbooks publish at the bar you already applied at S458 (86); a page under it is listed with its failing tests and stays a draft, and Chat mends its record.
5. **Publish** every page that passes, on the build site only. New pages go in as drafts first and are published only after their check passes.
6. **Inbound links:** the 99 inbound links the S458 brief listed for the Mindset Mastery workbooks, plus any page that linked to an old workbook address (none changed, so these should hold).

## 4. Known, and not part of this job

- The Kit email form on the workbook page is still a placeholder (the S178 note). Delivering the PDF by email stays on its own card; until then pdf_file holds the PDF. Say in your report what the page does today when someone asks for the workbook.
- Every workbook's back cover links to its course checkout and the community; course links return page not found until launch, which is expected and tested on launch day.
- Ikigai has no figure inside it, on Kain's word; that is correct.

## 5. Your report

One DONE file in TO Chat: the count created, updated and published; every page under the bar or held, with its reason; the picture count made and replaced; anything you could not settle; and the post numbers of the 33 new pages. Chat then updates the Full Editorial List and the board.
