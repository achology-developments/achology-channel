**For Chat. What this needs from you:** the DSRD 7 row in ASK__Sweep_Brief_And_DSRD_7_Row_For_The_Question_List_Type_S464; otherwise for the record. Code, S464, 9 November 2026.

# SHIP: the Question List type sweep, 0.707.851 and 0.707.852 (S464)

**What changed.** In help.css, every questions card (`.help-close`) now sets its question at 18/600 on 1.45 and its answer at 16 on 1.55 in soft grey, one step down below 768 (16 and 14). Both use `text-wrap: pretty`. These are the Help category list's own sizes. Before, the card borrowed Card Title 16 and Body Small 14. Done under BRIEF__Sweep_The_Question_List_Type_On_Every_Questions_Card_S464, Kain's order.

**Checked.** In WebKit at 1268, 1024, 834 and 390 on /certification/, /courses/, /reviews/, /pricing/, /help/, a Help category (its card holds routes, not questions, so it is unchanged) and a help answer:
- the sizes are right on every page
- nothing runs sideways
- no last line of one word, once `pretty` was added (0.707.851 left 30 of them)

/contact/ carries no questions card. Deploy proofs agree at 0.707.852.

**Found, not changed.** The questions card's heading bar is cool grey everywhere except Certification, where Kain had it turned white on the sand. On the white pages the grey still marks the bar, so it was left alone. Say if the family should match.

*No em or en dashes in this file; checked before writing.*
