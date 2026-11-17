For Chat. What this needs: one line on the school page's board card: audit-s528's open and close controls are in the button family.

From Code, theme session, a side session of S530, 17 November 2026. Shipped 0.708.148 to the build site, zip rebuilt.

## What changed, and why

Kain's S530 order for the school page names "every open and close control to the family's ringed plus" (audit-s528.html, item 2).

- **The twelve practise rows** drew a bare plus. They now wear the button family's open and close mark (buttons.css section 9, picks 15 and 17): a hairline ring with its plus, turning orange and to a minus when a row is open. Nothing on the page moves.
- **Who This School Is For** was a button that opened nothing, because this version of the note always shows its words, and a screen reader heard it as a collapsed control. On the school pages it is now plain heading words. Course pages keep their own note unchanged.

## Measured

On the built page in WebKit, all seven schools at 1440, 834 and 390, against a record taken before the change: 21 of 21, no fault (no row or block moved by half a pixel, every row carries the family mark at 28, a press opens the line with the orange minus, a second press shuts it, the heading holds no button).

## Call Code made that Kain may overturn

- The Who heading made plain rather than given a plus, because pressing it never did anything.

## Follow-up for a later sitting

The course pages' Who This Course Is For heading carries the same dead button in the same version of the note; changing it is a course page job, not done here.

OWED BACK: nothing.

DOCUMENT TYPE: ship brief.

*No em or en dashes in this file; checked before writing.*
