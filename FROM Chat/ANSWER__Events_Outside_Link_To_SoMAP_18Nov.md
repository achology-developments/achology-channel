> CODE DISPOSITION, S531: WAITS ON the Events build side session (events-theme-build) adding the sentence and its SoMAP link, the gate count, and the score after Kain's rescore; passed to it by the main Events session.
NEEDS FROM CODE (theme, the Events session S531): one outside link added to /events/ in the kinds lead, then Kain's rescore read back.

# ANSWER: the Events page's Rank Math bar is not lowered; an outside link is added

**For:** Code, the Events theme session (S531). **From:** Chat, 18 November 2026. Answers DONE__Events_Signed_And_Scored_S531, section 2.

**Kain's word.** Asked whether the Events page's bar should be 74, or an outside link added instead, he answered: "No, add a link" (18 November 2026). So the site bar of 90 stands for /events/, and no page-type bar is set.

**This overturns one line of the spec.** SPEC__Events_Page_And_The_22_Event_Pages_S471, section 9, said every link on the page is on the site. From today the page carries one outside link, to SoMAP. Chat has written this into the spec.

## The change

1. **Where.** The kinds lead (words.json, kinds.lead), under "The Kinds of Event You Can Join". It must be in the page's own HTML, not in the ticket, because the ticket is drawn by events.js and Rank Math does not read it.
2. **The words.** Add one sentence after the two already there:

   > Every CPD credit a member claims is checked by the Society of Modern Applied Psychology.

   The lead becomes 51 words. The fact is REF 1 section 5.1. The sentence never calls SoMAP independent (REF 1, Kain, 10 November 2026). Chat's call inside Kain's "add a link"; he may overturn it.
3. **The link.** "the Society of Modern Applied Psychology" links to https://thesomap.org, opening in a new tab with rel noopener, in the same pattern as the SoMAP link on /certification/ (template-certification.php, line 146), with its hidden "opens in a new tab" words for screen readers.
4. **The gate.** Change the kinds lead's matched word count in page_gate.py from 36 to 51.

## Proof

Read /events/ at 1270 and 375: the lead has no short last line, and the link has a focus ring. axe reports 0 violations. Then ask the main session for Kain's one-click rescore, and read the stored score and the failing tests off the install as before.

Done when /events/ carries the sentence and its link on the build site, the gate matches 51, and the new stored score is read back with its failing tests.

OWED BACK: one line in TO Chat with the version, the new score and what still fails.

*No em or en dashes in this file; checked before writing.*
