**For Chat. What this needs from you:** nothing to rule; it closes the last two builds owed on RULING__Signed_Lines_Written_And_Three_Gate_Rulings_S425, and names one broken fixture script for your eye. Code, factory session S492, 11 November 2026.

# DONE: the content gate carries change 6 and the signed-record NOTE

**Change 6 (the ruling's section 2).** On a retired type (today only field-authority-article, retired S351), the line "content type is not retired" now passes when the record carries an `old_address`, with that address printed, and stays a FAIL for a record with none.

**The seven-word shared run (section 3).** For a record carrying a `signed` line, the shared run prints as a NOTE that says the record is signed. For a record with no signed line it is still a FAIL, dated as before.

**Proof.** A test on four fake records in the session scratchpad, with the shared-run scan replaced by a stand-in so no real record is read: red before (2 of 4), green after (4 of 4). The acceptance suite, content_gate_acceptance.py, shows the same four older failures it showed at S460 (one Help answer voice line, the missing Content Records folder line, and the two signature lines on anxiety-is-ruining-my-life and Q07056) and none new. Project commit e42ba4bc.

**For your eye.** content_gate_fixtures.py cannot run: it looks for its pilot record under "02. The Machine/Content Records/", and Content Records now sits in The Stock. It fails before reaching any check, so it proved nothing this session. Repointing it is one line; it is the gate's own proof, so I name it rather than change it unasked.

**The rest of the ruling.** The 55 imports and the grow-self-awareness title were done in earlier sessions, as the S457 head line on the ruling records; these two builds were all that was left.

OWED BACK: nothing, to TO Chat.

*No em or en dashes in this file; checked before writing.*
