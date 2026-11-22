This needs Code to build the Membership page's join block, "Choose How You Join" (/membership/, post 45034), from this file: every line below is signed by Chat and placed as written.

Done when the join block on the build site carries every line below, word for word, measured at computer and phone width, and Kain has been shown the built block in Safari.

# The Join Block's Plain Words, Signed (Chat, S551 branch, 22 November 2026)

**What governs these lines.** No content type pack covers a selling block, so DSRD 2 and the Achology Content Standard govern, with Kain's rule of 22 November 2026 that every line is "clear, concise, and comprehensible, not open to guesswork". Each line says what you pay, how often, and what you get, so a stranger understands it on one read with no sums. Every figure is from DSRD 4: section 1.4 ($7 for 30 days, then $34.50 a month; $345 a year; no refunds; cancel any time; annual renews annually), section 13 (every workbook with annual membership; the gift of one $97 masterclass for life, chosen from nine). The $69 saving is 12 x $34.50 = $414 less $345, which the line now states as a comparison, so the reader never has to work it out.

## Lead

Pay $7 for your first 30 days, then $34.50 a month. Or pay $345 once for 12 months, $69 less than 12 monthly payments of $34.50.

## Monthly card

- **Name:** Monthly Membership
- **Price:** $7 for 30 days
- **Pill:** $7 Trial
- **Sub:** Then $34.50 a Month Until You Cancel
- **Button:** Start for $7 (unchanged; it waits on Kain's own text)
- **Terms:** After your first 30 days, you pay $34.50 every month until you cancel.

## Annual card

- **Ribbon:** Best Value
- **Name:** Annual Membership
- **Price:** $345 per year
- **Pill:** Save $69
- **Sub:** Compared With 12 Months at $34.50 (replaces "Two months free against twelve monthly payments"; it reads straight on from the pill: Save $69, compared with 12 months at $34.50)
- **Button:** Subscribe for 12 Months (unchanged)
- **Terms:** You pay $345 once for 12 months, and you get every workbook in the library. It renews at $345 a year until you cancel.

## Gift Banner, across the top of the Annual card

- **Headline:** Commit for 12 Months and We'll Gift You a Course Worth $97
- **Line under it:** Choose one of nine courses, and it is yours for life.

The figure is $97, not "up to $100": DSRD 4 section 13 names the gift as one of the nine $97 masterclasses, courses 019 to 027, so "worth $97" is exact. Headline in title case, the small words (for, and, a) in lower case. It keeps Kain's own words, commit and gift.

## The old gift lines: dropped

"Plus a course of your choice, yours for life." and "Choose one of nine courses, each worth $97." come out of the Annual card. The banner now says both, and saying them twice on one card is clutter. They stay in the `gift` key of WORDS__Membership_Page_S537.json (card_line, card_detail) for any other place that uses them.

## Under both cards

Membership payments are not refunded, but you can cancel at any time to stop every future payment. Read the refund policy.

("Read the refund policy" keeps its link to the refund policy page.) The old line's "Annual subscription renews annually" is dropped here because the Annual card's terms now say it in plain words, and "community subscriptions" becomes "membership payments", the product's own name (DSRD 4 section 1.4: Achology Membership). The facts are post 240's (no refund once access begins, cancel to stop every future payment) and DSRD 4 section 1.4.

## Lines kept as they were, and why

Monthly Membership, $7 for 30 days, $7 Trial, Best Value, Annual Membership, $345 per year and Save $69 already say what you pay and what it is, on one read, and are DSRD 4 section 13.1's signed card copy. The two buttons are unchanged by the brief.

## The free gates, run by Chat before signing

- **Banned and watched words:** every line scanned against content_gate_standards.json (banned_always, machine_tells_always, machine_tells_flag, banned_rules_7_8, watched_words, banned_link_labels): no hit.
- **Dashes:** no em dash, en dash or other dash in any line.
- **Copy measure, characters with spaces:** lead 128 (old 103); monthly sub 36 (old 28); monthly terms 70 (old 79); annual sub 33 (old 47); annual terms 118 (old 131); banner headline 58; banner line 53; under both cards 122 (old 123). Only the lead grows, by one short row at most at the block's measure; Code measures its rows at every width after placing it.
- **Voice measure and body_guard:** not run, because these are short card lines and labels, not running prose; both tools measure prose paragraphs and would read nothing true here.

**Signed:** Chat, S551 branch, 22 November 2026, to Kain's plain words rule of the same day.

OWED BACK: Code places these words, measures the block at computer and phone width, and shows Kain the built block in Safari.
