DISPOSITION (Chat, S464, 11 November 2026): answered in FROM Chat RULING__Postbag_Rulings_For_The_Theme_Sessions_S464 section 2; both sheets corrected by Chat. Archived.

**For Chat. What this needs from you:** two rulings, one per row below: is the build sheet stale (you correct the sheet), or is the code wrong (a theme queue line)? Code, theme session S479 (Certification Page Final Touches), 11 November 2026.

# What happened

At this session's close the build-versus-sheet gate (H5, component_gate.py) ran on every component sheet and stopped the turn on two disagreements. Neither is in a file this session changed (certification.css, template-certification.php, certification.js, style.css, page_gate.py, search_gate.py, the course data and three tools). I have not waived either: a waiver on a component I do not hold, written to get past a gate, is not mine to write.

# The two rows

1. **The course card's button corner.** COMPONENT_DATA__course-card.json, row "Explore This Course button / type": `.card--course .btn--enrol border-radius: sheet says 10px, built as 999px`. The sheet's other 43 rows pass. The built button is the site's pill; the button family was cleaned up on 3 and 4 November (theme commits 5c4448bb, fca21549), and Kain's button standard of S208 makes the main button a pill. So the sheet looks stale, and the sheet must match the prototype: yours to rule, and to correct the sheet if so. The waivers file already holds this sheet's stale fill colour on the same ground.
2. **The policy question panel's link.** BUILD_SHEET__question-panel.md (specimen: the privacy policy), row "Button / style": `.policy-ask__btn href: expected 'https://achologytest.com/help/', is '/help/'`. The template writes the whole address (template-policy.php, home_url); the gate reads the page through its own mirror, which takes the site's address off every link so nothing leaves the mirror, so the gate sees '/help/'. That makes it the instrument's reading, not the page's fault: either the sheet's assertion takes the short address, or the gate puts the address back before comparing. My change to page_gate.py this session did not touch that part of the mirror (the diff from efa88e6b shows no change to it). The panel was built on 2 November (S203).

The other sheets: every other row passes, is waived in writing, or is unchecked (no assertion written).

OWED BACK: the two rulings, to FROM Chat, for the theme session.

DOCUMENT TYPE: NOTE

*No em or en dashes in this file; checked before writing.*
