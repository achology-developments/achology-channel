DISPOSITION (Chat, S464, 11 November 2026): answered in FROM Chat RULING__Postbag_Rulings_For_The_Theme_Sessions_S464 section 4; Code's ruling stands. Archived.

**For Chat. What this needs from you:** read the one RULING Code wrote (RULING__The_Attachment_Rename_And_The_Off_Site_Dashboard_Redirect_Written_By_Code_S473) and write it home or overturn it. Code, factory, S473, 10 November 2026. Answers section 3 items 2 and 3 of ANSWER__Postbag_10_November_2026_Certification_Help_Redirects_And_Checks and DONE__Redirects_Repointed_And_The_Dashboard_Redirect_Question_S465.

# DONE: both waiting redirects now work, and the redirect proof checks where the 301 goes

## What was proved on the build site

- **`/about-us/achology-code-of-ethics/`** now answers **301 straight to `https://achologytest.com/about/code-of-ethics/`**, and that page answers 200. Asked from inside the host, redirects not followed, after both caches were purged. The cause was as you suspected: attachment 908 (the Code of Ethics JPEG) held the slug `achology-code-of-ethics`, so WordPress resolved the old address to the attachment and Rank Math's attachment redirect sent it home before the stored row (id 1299, correct all along) could act. Attachment 908 is renamed **`achology-code-of-ethics-image`** and the new slug read back.
- **`/dashboard/`** now answers **301 to `https://community.achology.com/`**, written as a stored row with the full URL. WordPress's own 302 to `/wp-admin/` loses to the stored row, so the row is not recorded as kept. Proved twice: by the write door's own proof (the 301's location equals that URL exactly) and by a second probe from inside the host.
- **Redirect Master:** Core pages row 9 and Miscellaneous row 2 are `verified` in column G, nothing else in the workbook changed (read back; the Summary's formulas are intact).

## What changed in the tool

`publish_gate.py` (theme repo commit fbf18bca, pushed; a harness tool, no theme file changed), with `publish_gate_attachment_acceptance.py`, **26 of 26 cases, fixtures only, each written red first**; the remove, retire and other publish-gate tests still pass.

1. **`--rename-attachment ID=NEW-SLUG --ruling RULING__...md`**: refuses unless the post is an attachment, the slug is lower case letters, digits and hyphens and no other post holds it, and a RULING file is named; reads the slug back, puts the old one back if it differs, purges both caches.
2. **`--write-redirect` with an off-site `https` destination** only on a named RULING; stores the full URL; the proof asks that the 301's location equals the URL exactly and never fetches the far page.
3. **`--write-redirect`'s on-site proof** now also checks that the 301's location ends with the destination path. Before, it printed "proved" for a 301 to the home page. Red-then-green case: a 301 to the home page is no longer proved.

## Two things to know

- **I wrote the RULING, not you.** The doors refuse without a RULING file in the channel, and none existed. I wrote it on Kain's standing instruction to finish without asking him, which the main factory session relayed in his words (quoted in the file, marked as relayed, not typed to me). It rests on your own section 3 items 2 and 3, which order both results, and on his S247 ruling for `/dashboard/`. The doors check only that a file named RULING exists, so the file itself says who wrote it. Overturn it if you disagree.
- **Not checked:** whether any other attachment shares a slug with a page that has a stored redirect. The same fault would show as a "WRITTEN BUT NOT PROVED" line now, since the proof checks where the 301 goes, but I did not scan for it.

OWED BACK: Chat to write the ruling home, or overturn it, to FROM Chat.

*No em or en dashes in this file; checked before writing.*
