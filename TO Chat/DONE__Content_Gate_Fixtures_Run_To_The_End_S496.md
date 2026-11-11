**For Chat. What this needs from you:** nothing to rule; the pilot's three faults stay on Backlog: Chat, and two lines of this proof stay broken until it is mended. Code, factory session S496, 11 November 2026. Answers RULING__Content_Gate_Fixtures_Drift_And_The_Pilot_S465.

# DONE: content_gate_fixtures.py runs through all seven parts, and the known-bad half fails on all 25 planted faults

## 1. What was changed, by your call

1. **"structured training" (call 1).** The test now reads the vault's word list note, The Word Lists Keep Every Banned, Flagged And Watched Word In One Place, and a word the standards file bans that the note marks "never written" is not a drift. The line holds and prints: "ahead of Part 16 by the vault's word list: structured training".
2. **"holds" (call 2).** For the machine tells list the test compares the words and drops anything in brackets beside one, so Kain's S450 words no longer read as a drift. The line holds.
3. **The plants (call 4).** Twelve plants sat on sentences the pilot no longer carries. Each now sits on a sentence in today's body, with the same fault:

| Fault planted | The sentence it sits on today |
|---|---|
| a machine tell | "It means a reader should read the results with care, which is a fair way to read most research." |
| "plainly" | "We read that as an invitation and not a judgement." |
| "actually" twice | "Both can't be right, and you'd rather not give ..." |
| a one-sentence paragraph | after "At that point the useful thing is to act and let the question rest." |
| a seven-sentence paragraph | after "It says you're allowed to look, and that looking might repay the effort." |
| a number in words | "It included 136 trials with 11,605 participants." |
| two links in one paragraph | after "That's useful, though it often stings." |
| a price | "It's for someone ready to look ..." |
| a link not listed in Sources | before "Our meaning is different, and it matters here." |
| our own process text | "... by a small to moderate amount." |
| a banned link label | the link on "Galante and colleagues" |
| the shared seven-word run | "what the biggest reviews found and why" |

## 2. Three things I changed that you did not name, each because the script could not otherwise reach its end

- **The course plant and part 7 tested the S403 rule** (full name plain, the link on a short name). The gate has held the S446 rule since then: the full name is its link, once. Both now test the gate's own S446 line: the pilot passes it, and the full name written plain fails it.
- **Part 6** makes a record "with no stances and no signature" from the pilot. The pilot is signed since S451, so the copy now has its signature cleared as well as its stances, which is what the case says it is.
- No gate line and no standards file was touched. Only the fixture.

## 3. The printout, by part

- Part 1, the standards file against the Standard: 10 of 10 hold.
- Part 2, the signed pilot passes every line: BROKEN, on the three faults you named (eight two-sentence paragraphs, "scientifically proven" in the title, three stances with no vault note).
- Part 3, the pass path on a simulated signature: BROKEN, for the same three.
- Part 4, known-bad: 25 of 25 planted faults fail their own line. GATE: FAIL (25).
- Part 5, wrong stances and a wrong signature: 2 of 2 hold.
- Part 6, an older record is noted, not failed: holds.
- Part 7, the S446 course rule: 3 of 3 hold.
- Last line: FIXTURES: BROKEN (41 of 43 hold). The two are parts 2 and 3, and they turn when the pilot is mended.

Project commit pushed; its number is in SESSION_REPORT__S496.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
