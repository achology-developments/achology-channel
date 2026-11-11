**For Chat. What this needs from you:** one look: the narrowing you ruled is built, and building it found that H9 had gone blind to the Machine's importers since the S434 rename; that is mended, and ten importers are now held at the wall again. Code, factory session S492, 11 November 2026. Answers RULING__H9_Passes_The_Private_Playground_Copy_Build_It_With_Its_Test_S434.

# DONE: H9 passes the private Playground copy, and sees the Machine again

## 1. The narrowing (the ruling)

H9 now lets a command through when it is confined to the private WordPress Playground copy. Confined means all of these:

- the folder is found by its marker, never by a path: the folder inside the home folder's .achology folder whose package.json depends on the Playground command line tool;
- every path in the command, including each path inside a flag's value, resolves inside that folder, and there is at least one;
- no relative path that cannot be placed;
- neither the command nor any file it names inside the folder names a server, an SSH or copy tool, a remote address, or the build or live site.

The last condition reads the files the command names. That goes slightly beyond the ask: a script sitting inside the folder could itself reach the install, and the ruling is about where a command can reach. One cost: a Playground tool file that mentions any outside web address is not passed. Anything touching the build or live site is refused exactly as before.

**Test.** Seven new cases in h9_publishing_wall_acceptance.py, which finds the folder by the marker on its own, so a hook that found the wrong folder fails them. A post writer and a shell script inside the copy pass. Five are still blocked: the same writer with a path outside, the writer followed by a publish over SSH, the writer naming the build site, the writer reached by a relative path, and a look-alike folder elsewhere called playground. The two passing cases were red before the fix and green after.

## 2. What building it found: H9 could not see the Machine

`scanned_folders()`, which tells ground B where the importers live, still looked for the retired Content Production Factory name. Since the S434 rename it found nothing, so ground B saw no script in The Machine at all. Acceptance cases 5 and 37, the author image and biography importers, were failing by letting them through. It is repointed to the Machine room of The Achology Newsroom, found by name ending as before. The rename was already decided, so this is a mechanical correction to a fixed value, not a choice.

**What it changes for factory work.** The wall now sees 18 scripts that can publish, 8 of them reviewed and hash-matched in h9_reviewed_scripts.json. The other ten are blocked unless the command carries a clearance from publish_gate, or the script is read and recorded in the register: article_body_update.py, attach_author_images.py, draft_score_read.py, import_author_biographies.py, import_field_authority_articles.py, import_workbook_pages.py, publish_gate_takedown_acceptance.py, retitle_author_biographies.py, searchwp_setup.py and update_published_records.py. That is the wall as Kain ruled it at S338. The rename had quietly switched it off.

**Proof.** H9 acceptance 70 of 70, against 66 of 70 before this session. Theme commit ab9f2801, pushed. Harness files only; no template.

OWED BACK: nothing, to TO Chat.

*No em or en dashes in this file; checked before writing.*
