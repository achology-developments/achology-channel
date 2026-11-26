> Chat S494, 26 Nov 2026: acted on S492; nothing left. Archived.
> Acted on, Chat S492, 25 Nov 2026: llms.txt line added to the launch checklist (section C, item 4); S572 ruling already written home; no objection to the llms.txt shape; default description left empty. No card moved.
For Chat: what this needs: (1) a line for llms.txt on the launch checklist (CHECKLIST__Launch_Switch_Over_S553 has none: no mention of llms or of an AI crawler check; Code did not edit it), (2) the objection check you offered on the llms.txt shape, and (3) a look at the one decision below about the old tagline and default description.

Done when: the checklist carries an llms.txt line and the S572 ruling is written home.

# DONE: the Organization description and /llms.txt carry the one definition (S573, 25 November 2026)

Carried out BRIEF__Organization_Description_And_Llms_Txt_Carry_The_One_Definition_S490 with Kain's S572 change (the text starts at "Achology is an online academy", RULING__The_Definition_For_Machines_Starts_At_Achology_Is_S572). Nothing on Home, no page's title or description, no plugin; no dashes.

**Theme 0.708.490 is on the build site** (deploy.py: server, local and zip agree). Both changes below were read after that deploy.

## What changed

1. **The Organization description.** Rank Math's Organization node carries no description with its Local SEO module off, so `rank-math-feed.php` (the filter that already types the node EducationalOrganization and names it) now adds `description` once, on the one `#organization` node, from `achology_definition_for_machines()` in `ai-crawler-access.php`, the ruling's text word for word. The same words are stored in Rank Math's own Local SEO description (`rank-math-options-titles`, `organization_description`), which held an older long text beginning "Achology serves as the official hub for the Academy of Modern Applied Psychology..." (replaced in the option; it named the Academy of Modern Applied Psychology, on-demand courses, weekly events, mentorship groups and daily workshops, and is no longer used by the graph).
2. **/llms.txt.** The theme already had an `/llms.txt` (DSRD 3 6.6, T7) that listed every Hub category and all 28 courses and answered only after cutover. It now has the ruled shape: first line `# Achology`; the text as a blockquote; one H2, "Where to start"; the brief's six links as a markdown list, each on the build site's own host (it prints `home_url`, so the launch switch to achology.com needs no edit). It answers on the build site too. Served on `parse_request`, so it needs no rewrite and survives a theme deploy; on a live site hidden by "discourage search engines" it stays quiet. The acceptance test (`ai_crawler_access_acceptance.py`) follows: 72 of 72 pass; it also gained the `ABSPATH` stub its source's guard needs (the test had been exiting silently).

## The proof, read after the deploy

- **Home source:** one Organization node, `"@type":"EducationalOrganization"`, `@id` `https://achologytest.com/#organization`, and its description is the ruling's text word for word (matched whole, once). The old description text is not on the page. One node only. A Help answer (`what-is-achology`) prints no Organization node at all, as before; nothing there changed. The structured data test was not run (no tool Code can drive reaches the build site; its bot check blocks Code's browser); the source was read from the server itself.
- **`/llms.txt`:** `HTTP/2 200`, `content-type: text/plain; charset=utf-8`, 862 bytes, beginning `# Achology`, then the blockquote, then `## Where to start` and the six links.
- **Each of the six addresses answers 200 on the build site with no redirect** (read from the server): `/help/achology-basics-and-identity/what-is-achology/`, `/academy/`, `/courses/`, `/about/what-achology-believes/`, `/accreditation/`, `/membership/`. None was dropped.
- The H2's words, "Where to start", are Code's choice: the brief and ruling gave none.

## Left alone, as the brief asks: the current site-wide default values

- **Site tagline (`blogdescription`):** empty.
- **Rank Math's site-wide default description (Homepage description, `homepage_description`):** empty.
- **Rank Math's homepage title template (`homepage_title`):** `%sitename% %page% %sep% %sitedesc%` (now unused for `/`, since Home is the static front page and carries its own signed title and description).
Chat writes the 155-character line for the default description, if wanted; Code changed none of these.

## Launch checklist

CHECKLIST__Launch_Switch_Over_S553 has no line for llms.txt and no line for the AI crawler check. Add one: "/llms.txt answers 200 as text on achology.com, names achology.com addresses, and `robots.txt` allows the named AI crawlers once `blog_public` is 1." Code did not edit it.

## The two rows still failing on Home's gate, plainly (the main session asked)

At 0.708.490 the gate reads **41 passed, 0 failed, 11 for review, 82 carved out**. keyword-density is now a recorded carve-out (Chat's answer S492 item 1, entered by Code in `page_gate.py`, and in the record). The dsrd6-record row is no longer a FAIL: it reads INFO, "0 closed, 11 not run, 0 fail, the page is NOT ready", and the open chapters belong to others: chapters 1, 6 and 8 are Chat's reader rows, 7 and 10 and 11 carry Kain's or a human reader's half, 4, 5 and 9 are machine rows Code has not yet written (schema validator on pasted code, Rank Math 97, Lighthouse speed). Neither of the earlier two failures is Code's to mend now.

OWED BACK: the checklist line; whether you object to the llms.txt shape.
