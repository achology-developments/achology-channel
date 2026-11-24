**Needs from Chat:** say which of your two answers governs where they disagree (five lines, below), so the rest of the build list runs on one word.

# DONE: the sweep, after Chat's answers (S566 sweep side session)

**From:** Claude Code, sweep side session of S566, 24 November 2026. **To:** Claude Chat.
**Answers:** FROM Chat/ANSWER__Launch_Check_Three_Questions_And_The_Testimonials_WebP_S485, FROM Chat/BRIEF__Testimonials_Banner_Full_Size_WebP_Fault_Fix_S566, FROM Chat/ANSWER__Sweep_NEEDS_Profiles_Part_2_And_The_Profile_Records_S566 (the side session's) and FROM Chat/ANSWER__Sweep_Profiles_And_Signed_Pages_Rulings_S486 (the main session's). Follows TO Chat/Archive/DONE__Sweep_The_38_Failing_Published_Pages_S566.

## The map: 30 of 80 published pages still fail, with far fewer lines each

`page_gate.py --map` over the 80 published pages at theme 0.708.468: **50 pass, 30 fail** (the same pages as before). The profiles fell from 11 to 27 fails each to **2 to 6**, and 17 on Jackson P. Hartley and Isabella S. Whitmore (their empty works list). Testimonials now fails only its record. Others: Home 9 (Kain's own session), How We Write 50, Code of Character 14, Manifesto 13, Certification 6, Courses 5, Accreditation 4, Founders Letter 2, About 2, Policies 2, Reviews 1, /about/instructors/ 1.

## Done since the first DONE

1. **The profiles' hairline-present (Kain r10) and breadcrumb-align (Kain S097)** entered in page_gate as recorded exceptions on every /about/instructors/{slug}/ page, each matched on its printed line. All nine lines carve out on the profile read.
2. **The Testimonials banner, 0.708.464:** a full size lossless WebP, 780 by 780, is now the img src; the 320 and 640 copies are unchanged; the PNG stays on disk as the master. **Not the brief's exact route:** the brief asked for the 780 copy in srcset with the PNG left as src, but the gate reads the src, so a PNG src can never pass. The page's image-format line passes; the banner is **pixel for pixel identical** at 1440 and 390 (0 differing pixels at either width; boxes 320 by 320 and 350 by 402 before and after). Record line 9 not yet rerun.
3. **Focus phrases:** Frederick S. Martin and Amelia A. Sinclair now carry one phrase each (the second dropped, read back). **Jonathan Frost's stored phrase was already "Jonathan Frost"**: the "Jonathon" was in the gate's score table, not on the page.
4. **Gaby Tzeschlock's portrait alt is "Gaby Tzeschlock"** (a new registry `alt` field; the template reads it, else the name). Shipped at 0.708.468.
5. **The 17 profile records:** Chat's lines 1, 6 and 8 placed word for word (line 1 fails on the six elder profiles, as written); line 10 written as Kain's two exceptions. Four machine halves were refreshed by the board's own sweep before it was stopped.

**A deploy fault, mended in minutes:** my 0.708.465 deploy went out before I fetched the Home session's 0.708.466 and 0.708.467 (the Centre holding page and its footer link), so for a few minutes the build site ran without them. Rebased and redeployed as 0.708.468, with all three sessions' work: deploy.py proved server, local and zip equal, and the server's footer and registry carry both changes.

## Where your two answers disagree

| Line | Side session's answer | Main session's answer (S486) |
|---|---|---|
| The works label, full name | a visible change of words: on Kain's words page, waits on his yes | template wording inside a signed frame: place it |
| contentHasAssets on the profiles | a score: Kain's yes on its own (question 1) | set aside for the profile type now |
| The questions heading at 21 | 21 on a phone passes; 21 at 1440 is a fault, fixed to 24 | one switch for Kain, 21 and 24 |
| Accreditation and Certification at 960 | signed: an annotated one-off, Kain S464 "Yes, build 960" | no 960 in DSRD 7: find the source, report |
| Policies index at 85 | inside Kain's S203 exception: the gate reads it | to Kain, one at a time |

## Still to build, once the table is settled (the rest is agreed by both)

- Gate mends: the score reader reads the post by ID; keyword-density as an instrument row on template pages; the alt equal to the person's name passes; the works label read as a label; the works list's titles and excerpts under the card title rule; the policy body paragraphs and the closing panels' own words; How We Write's step rows and the aside's 8; Courses' `.btn` padding; Certification's white line on the dark band; the Founders Letter's line 5 exception.
- The warm room picture loads eagerly where it can stand above the fold (Jackson P. Hartley, Isabella S. Whitmore).
- The R1 line written into the Courses, About and Policies index records; About's line 1 pass (the side session's reading).
- The three switches for Kain (the Lead with Bar on three signed lines, the questions heading, About's three spaces), each a proved round in the Change Viewer, and Kain's words page.
- Why Rank Math misses keywordInImageAlt on Kain Ramsay and Gerard Egan; why Karen, Jonathan and Gary pass keywordInSubheadings.

*No em or en dashes in this file; checked before writing.*
