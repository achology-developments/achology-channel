> Disposition, Chat S480, 23 Nov 2026: record; nothing owed; archived. No board card moved.

# DONE: Membership chain-register cells (factory S548, for theme session S547)

21 November 2026. Factory session, Chat's group C ruling in ANSWER__Membership_Page_Gate_Lines_S544 ("Refresh the 8 workbook rows' dest_built and dest_in_sitemap cells from the install").

## What changed

Redirect_Master.xlsx, the two cells dest_built and dest_in_sitemap on the 8 rows whose new_url is /membership/, each FALSE before and TRUE now. Nothing else in the workbook was written; the other three facts on those rows were already TRUE. No theme file touched, nothing deployed, nothing published.

| Tab | Row | old_url |
|---|---|---|
| Core pages | 21 | /achology/achology-membership/ |
| Miscellaneous | 4 | /cips-session-agreement-form/ |
| Miscellaneous | 5 | /cips-session-feedback-form/ |
| Miscellaneous | 6 | /cips-coaching-preparation-form/ |
| Miscellaneous | 7 | /cips-session-creation-form/ |
| Miscellaneous | 8 | /pals-session-feedback-form/ |
| Miscellaneous | 25 | /product-category/membership/ |
| Miscellaneous | 29 | /resource_cat/achology_community_resources/ |

How the values were read: the register's own functions (redirect_chain_register.py), measured on the build site achologytest.com. /membership/ answers 200 (460,717 bytes, not the placeholder) and is listed in the sitemap (1,172 addresses read, every sub-sitemap answering). The page's indexable, schema and course-route facts also read TRUE. No row is left failing, so none is sent back.

## The gate line

`python3 page_gate.py --json https://achologytest.com/membership/` at theme 0.708.351:

`PASS chain-register: 8 workbook rows point here, all five facts recorded and true`

The run's other lines, for S547 and not touched here: 42 PASS, 58 CARVE-OUT, 14 INFO, 4 FAIL. The 4 FAIL: links-resolve (one 502 on /help/events-and-mentorship/mentoring-opportunities-achology-membership/), image-dimensions (face-024, face-045, face-052 and one more read as other sizes, the same mirror-502 picture fault the brief warned of, not a real mismatch), acronyms (II, ruled a recorded exception in group B), rank-math (post 45034 not yet in the score table, Code's own scoring step from a built page).

*No em or en dashes in this file; checked before writing.*
