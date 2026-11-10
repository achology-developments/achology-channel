> CHAT DISPOSITION, 10 November 2026 (branch of Chat's main session): acted on at S461 as its head line says; archived.

> ACTED ON, Chat S461 (9 November 2026): the page check and the eight movements written into the signed spec (blocks 4 to 10 paragraph), replacing section 5's motion line for this page.

**For Chat. What this needs from you:** nothing; for the record on the Certification card. Code, S464, 9 November 2026.

# SHIP: Certification page check (0.707.853) and bells and whistles (0.707.854), S464

**Kain's finishing order, all three passes** ("have a look at the whole page and do bells and whistles"; then "Yes, build all eight").

**1. Page check, 0.707.853.**
- Spacing measured in every section at 1268, 1024, 834 and 390: 64, 48 and 32, heading to supporting line 16, supporting line to content 24. All correct.
- Three one-word last lines tied with no-break spaces: the section 2 card title "Course Completion", the block 5 card title "Professional Development", and the section 6 heading "Your Certificate".
- On a phone, the close's heading and line and the FAQs heading are back on the page's own sizes (24 and 18). Code had stepped them down earlier, out of line with the other sections.

**2. Dead code.** None. Every class in certification.css is still used, some by the Accreditation page, which loads the same file.

**3. Bells and whistles, 0.707.854.** One movement per block, each tied to what the block means:
- **Banner:** the certificate pair tilts toward the pointer (at most 6 degrees), and the proof tiles ring on hover.
- **Section 2 cards:** each card lifts and its marks drift on hover, and the two step numerals light in turn.
- **Four steps:** the numerals arrive one to four and the line draws from each to the next.
- **Is and Is Not:** the rows settle in turn, and a row warms to sand under the pointer.
- **Which path cards:** the card lifts and its certificate straightens.
- **Verification card:** plays once (the address bar fills, the tick pops with a pulse, then the details and the certificate appear).
- **FAQs:** the rows settle in, and the Q. steps forward on hover.
- **Close:** the certificate pair tilts like the banner's.

Reveals start hidden only when certification.js sets html.cm-ready, which it never does under reduced motion or without IntersectionObserver.

**Checked.** In WebKit at all four widths: after every block plays, the layout matches the reduced-motion page exactly, nothing is left below full opacity, nothing runs sideways, and the tilt is live. Deploy proofs agree at 0.707.854.

*No em or en dashes in this file; checked before writing.*
