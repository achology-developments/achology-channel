CODE DISPOSITION, S571: WAITS ON a quiet sitting of its own; the brief rules out doing it in a Home sitting, and S571 is the Home sitting.
For Code: what this needs: two small jobs on the build site, in a quiet sitting that does not touch the Home page. One, set the Organization description to Achology's one definition. Two, make an llms.txt at the site root that opens with it. Then one DONE with the proof below. Card: the website board, new line under #98's neighbours; no column move needed. Kain said "Yes, send them" (S490, 25 November 2026). Ask Kain nothing; a branch or session never asks him a question, and anything you need goes to Chat in FROM Code.

**DOCUMENT TYPE:** brief from Chat (S490, 25 November 2026). Plan behind it: 02. Project Delivery System/PLAN__Making_The_Definition_The_Answer_To_What_Is_Achology_S490.md, steps 2 and 4.

**Vault notes this job rests on:** "What Achology Is and Why It Exists" in The Newsroom Vault's 01 Beliefs (the one definition; nothing may say it differently). DSRD 3 section 6 (AI visibility: allow-all crawlers, llms.txt as a cheap launch item, the organisation typed as an online academy, never a place). No writing is asked of you: the words below are Kain's, final.

## The words, word for word

> We are taught many things in life, but rarely how to understand ourselves or direct our lives with purpose. Achology is an online academy that teaches practical psychology, helping people recognise how their beliefs shape their thinking, influence their emotions and guide their behaviour. By studying at your own pace, applying what you learn to your own life and practising with others, you develop the understanding and skills to make wiser decisions, build healthier relationships and help others do the same.

Do not reword it, shorten it, join its sentences or add to it. Practical psychology stays "practical" here; the course and school names keep "applied" (Kain's ruling, S490).

## Job 1. The Organization description

1. Find where the site's Organization entity (name "Achology", the logo and social profiles, set in Rank Math and retyped by rank-math-feed.php, DSRD 3 section 4) takes its description. Set it to the paragraph above, whole. If the entity has no description field today, add one the way the theme already adds to the graph, without a new plugin.
2. Do not touch any page's own search title or meta description. The Home page's belongs to the Home session and Kain's signing. If Rank Math's site-wide default description or the site tagline is a different field from the Organization description, do not change it: report its current value in the DONE and Chat will write a 155-character line for it.
3. Check the graph still validates: the page source of the Home page and one Help answer, the Organization node carries the description, no duplicate Organization node, no new warning in the structured data test you already use.

## Job 2. llms.txt at the site root

1. Make `/llms.txt` on the build site, plain text, served with a 200 and a text content type. Where it is made (theme, server rule or a file the deploy places at the root) is your call; it must survive a theme deploy.
2. Its first line is the paragraph above, whole, as one paragraph. After one blank line, a short list of links, one per line, each with a plain label and the full address on the build site's own host (switched to the live host by the launch checklist):
   - What is Achology? (/help/achology-basics-and-identity/what-is-achology/)
   - The academy and its seven schools (/academy/)
   - All 28 courses (/courses/)
   - What Achology believes (/about/what-achology-believes/)
   - Accreditation (/accreditation/)
   - Membership (/membership/)
   Confirm each address opens on the build site before you list it; drop any that does not and say so in the DONE.
3. Add llms.txt to the launch checklist's line for the AI crawler check (CHECKLIST__Launch_Switch_Over_S553) only if a line for it is missing; tell Chat in the DONE either way. Do not edit the checklist yourself; Chat owns it.

## Do not

Touch the Home page, any page's design or any page's words. Add a plugin. Add any claim, price, count or promise that an assistant or search engine will quote the paragraph. Use an em or en dash anywhere.

## Done when (the proof, read from the thing itself)

- The Home page's page source shows the Organization node with the paragraph as its description, one Organization node only.
- `https://<the build site>/llms.txt` returns 200, begins with the paragraph, and every listed address opens.
- A theme deploy afterwards leaves both in place (read after the deploy, not before).
- One DONE in TO Chat: the two fields or files changed, the version deployed, the current value of any default description left alone, and OWED BACK.

## OWED BACK

The DONE above, and the current site-wide default description and tagline values if they differ from the Organization description.

*No em or en dashes in this file; checked before writing.*
