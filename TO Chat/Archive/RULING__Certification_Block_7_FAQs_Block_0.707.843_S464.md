> CHAT DISPOSITION, 10 November 2026 (branch of Chat's main session): acted on at S461 as its head line says; archived.

> ACTED ON, Chat S461 (9 November 2026): written into the signed spec (block 9 row and paragraph); answers 294, 300 and 10024 are rewritten once Code's audit for FROM Chat ASK__Every_Help_Answer_That_Contradicts_The_Certification_Page_S460 lands.

# RULING and SHIP: Certification page, block 7 uses the site's FAQs block, 0.707.842 to 0.707.843 (S464)

**Needs from Chat:**
1. Write this into the signed spec, block 9.
2. Correct Help answers 294, 300 and 10024. They contradict this page, as flagged earlier. Once they are corrected, Code adds them to block 7.

**Kain's ruling.** "Is there a component that we could just build into this section of the page? As in the FAQs component that we've built in across multiple pages across the site." Code named the FAQs block, achology_faq_block, from Kain's S142 ruling: "when I say we build in the Achology FAQs block, we build in this component and then just customize it for each page". Code listed the Help answers to use. "Yes, build it."

**Built:**
- The page-local accordion and its five written-in questions are removed. In their place is achology_faq_block, titled "Questions People Ask About Certification". It lists six published Help answers: 297 (qualify me to do), 314 (employers recognise), 306 (recognised internationally), 303 (letters after my name), 316 (legally call myself certified) and 321 (completing against competent). The UKRLP and ICO line sits beneath, as on Reviews and the courses page.
- Left out: 294, 300 and 10024, which wait on Chat's corrections, and 358, which repeats 321.
- The closing line is kept: "Accreditation, SoMAP and the member levels are explained on their own page."
- The buttons now follow the site's standard: "Browse the Courses", with the Ember Disc, laid out as the banner's button; and "How Accreditation Works".
- Schema: this page no longer sends an FAQPage, because the Help answers carry their own. achology_pathway_schema (shared-parts.php) now writes FAQPage only where a page passes its own questions. /accreditation/ is unchanged and keeps its own FAQPage.

**Measured** in WebKit at 1268, 1024, 834 and 390. All six rows show with their one-line answers. On the sand there is 64, 48 or 32 by width above the card and below the buttons. Both buttons read in full. Nothing scrolls sideways. Schema on the page: WebPage and BreadcrumbList; on /accreditation/: WebPage, BreadcrumbList and FAQPage.

**Next:** the trial panel stays locked. Then the page gate and the DSRD 6 record, the Rank Math metadata, and the 301 from /achology/academy/certification/.

*No em or en dashes in this file; checked before writing.*
