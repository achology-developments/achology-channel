NEEDS: Code to place the third card in the About questions band.

**Done when:** the About redraw preview shows a third card titled Recognition and Trust, with the four questions below, each linking to its Help answer address and showing its one line, the card even with the other two at four questions, and nothing live.

# ANSWER: the third card for the About questions band

**Card title:** Recognition and Trust

Why this card: after who we are and how learning works, the next thing a visitor to an About page asks is whether the place is recognised and whether its certificates can be trusted. All four questions say what Achology offers and how to check it, none says what it is not, and none repeats the two existing cards.

| # | Question (the Help answer's own title) | Address | The one line under the question |
|---|---|---|---|
| 1 | Is Achology accredited? | /help/certificates-cpd-accreditation/is-achology-accredited-somap/ | Yes, by SoMAP, whose committee of Master Achologists checks every claim on the accreditation pathway. |
| 2 | Will employers recognise my Achology certificate? | /help/outcomes-and-expectations/will-employers-recognise-achology-certificate/ | Employers who judge what you can do may value it; a job that needs a licence needs that profession's own qualification. |
| 3 | How can employers or clients verify an Achology certificate? | /help/certificates-cpd-accreditation/verify-achology-certificate/ | Scan its QR code, open its link, or enter its Certificate ID at certificates.achology.com/verify. |
| 4 | Are Achology certificates recognised internationally? | /help/certificates-cpd-accreditation/achology-certificates-recognised-internationally/ | They record the same training wherever you live; a regulated profession needs its own licence in every country. |

Post ids, for Code's lookup: 295, 314, 300, 306.

## Sources

- The four titles, addresses and post ids: `MEASURED__All_250_Help_Answers_S117.csv` and the four `HELP__` records (slugs is-achology-accredited-somap, will-employers-recognise-achology-certificate, verify-achology-certificate, achology-certificates-recognised-internationally) in the help-answer folder of the Stock's Content Records. The robot check blocks curl on the build site, so the live search call was not usable; Code is asked to read the four ids off the build site at build, as the other blocks do, and drop any row not published.
- The four one lines are each answer's own post excerpt (post_excerpt in its record), word for word.
- Standard: `RULING__Question_Standard_Helpful_Questions_Site_Wide_S544` (helpful, likely to be asked, who we are and never who we are not) and the topic form in `WORDS__Question_Block_Groups_And_Lines_Site_Wide_20Nov.json`.
- Not duplicated: none of the four is in Who We Are or Learning With Us (ids 218, 255, 273, 257, 281, 260, 397, 411).
- SoMAP in row 1 stays a plain external link to the Society's website, never spelled out beyond the answer's own words.

*No em or en dashes in this file; checked before writing.*
