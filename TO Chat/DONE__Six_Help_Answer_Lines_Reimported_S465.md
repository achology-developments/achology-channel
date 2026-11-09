**For Chat. What this needs from you:** nothing; this closes BRIEF__Reimport_Six_Help_Answer_Lines_S461. Code, factory, S465, 9 November 2026.

# DONE: the six Help answer lines are on the build site

## What was done

For the six posts below, only `post_excerpt` was written, from the signed record, with a plain `wp post update` (the Help importer's own update road does not carry post_excerpt for an answer that is not Achology-only, so I did not use it; no body, title, search field, status or picture was touched). Before writing, each record's post_id and address were checked against the post (6 of 6 match). After writing, each post's excerpt was read back from the site and equals its record word for word (6 of 6).

## The six excerpts as the build site shows them

- **316** call-myself-certified-achology-credentials: "You can describe yourself as Achology-certified, naming the certificate you earned; it is never a licence or a regulated title."
- **314** will-employers-recognise-achology-certificate: "Employers who judge what you can do may value it; a job that needs a licence needs that profession's own qualification."
- **315** will-clients-take-achology-certificate-seriously: "Clients mostly judge you, not your certificate; it shows them what you studied and practised."
- **306** achology-certificates-recognised-internationally: "They record the same training wherever you live; a regulated profession needs its own licence in every country."
- **303** post-nominal-letters-achology-certificates: "No. Achology awards no letters for after your name, because letters suggest a qualification a certificate doesn't give."
- **321** course-completion-vs-competence: "Completion means you finished every lesson; competence shows when you use what you learned with a real person, without a script."

## On the Certification page

The questions block already lists these six by post number beside 297 (template-certification.php, the `ids` array), so nothing was placed: the live page at /certification/ now shows all six new lines under their questions, read from the page itself. 294, 300 and 10024 are still left out. 41428 (are-psychology-certificates-worth-it) still shows its question with no line under it on the page: its record has no answer line yet, and taking it out of the `ids` array is the Certification theme session's change (this factory session touches no theme file).

## One thing the Help audit found that bears on this

The record bodies of 294, 300 and 10024 already read correctly, but their posts on the build site still carry the old contradicting sentences. See DONE__Help_Answers_Against_The_Certification_Page_S465, section 2: those need a re-import of their current records, not a rewrite.

*No em or en dashes in this file; checked before writing.*
