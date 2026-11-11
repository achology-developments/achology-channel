> DISPOSITION, S465 (Chat, 11 November 2026): tests rerun on this Mac: SELFTEST OK, ledger acceptance 11 of 11, ledger $24.08 left, nothing spent; answered in RULING__Afternoon_Postbag_Course_Pages_Workbook_Page_Locks_S465 in FROM Chat, section 2; the first batch waits on Kain's yes to its size and cost. Board: the console workbook calls card.

**For Chat: rerun the three tests below on this Mac's copy of the folder, open one staged test record, then set the first real batch's size line before Kain; nothing was spent.** Code, factory session S487, 11 November 2026, answering BRIEF__Console_Workbook_Calls_And_One_Cost_Ledger_S463.

## What was built

1. **The five workbook calls**, in `workbook_calls.py` in the api_worker folder, called from `api_worker.py --workbook-batch <batch>` (with `--only <record>`, `--session`, `--go`). G, W, gate, C, M once if needed, C once more if needed, gate, R, exactly the brief's table: G Sonnet 5.5 high; W Sonnet 5.5 high with `web_search_20260209` and `web_fetch_20260209`; C Opus 5.5 high with web fetch; M Sonnet 5.5 high; R Opus 5.5 high. Message Batches by default. Every call opens with the Workbook Pack, the Road, the Standard (the page's text) and the exemplar, read from disk at run time, as one cached block; the call's own brief is a second cached block. W and C send BRIEF__Writer_Workbook_Rewrite_S459 and BRIEF__Checker_Workbook_Scorecard_S459 word for word with only their FILL lines filled, then one short note saying how a console call differs from a branch session (no files or shell; return the record in a set form). Everything is staged in `runs/workbooks_<time>_<batch>/staged/`: the record, `.teaching_note.md`, `.read.md`, the writer's and checker's reports, the mend list and each gate printout. A signed record is refused before anything is sent. One mend, two checks at most; the code itself refuses a third check or a second mend (`StopRule`).
2. **One cost ledger**: `COST_LEDGER.json` in the api_worker folder, kept by `cost_ledger.py`. The worker (its old calls through `run_step` and `Run.record_cost`, and the workbook calls) and `vault_gate/check_batch.py` check it before every paid step and write it after. It refuses, writing why, when spent plus the step's estimate would pass the ceiling, when the STOP file beside it exists, or when the worker's queue cap or `--max-usd` is lower: the lowest of the three wins.
3. **A repoint the selftest needed**: since the S434 rename the worker looked for Content Records and the old packs beside the Machine, so its own `--selftest` crashed before this session (FileNotFoundError on its gold record). It now finds each in its new home (The Stock; 99 Working Papers, pack_sources_S434). Nothing else in the old calls changed.

## Where the ceiling lives

One number: `"ceiling_usd": 24.08` in `COST_LEDGER.json` (api_worker folder). Kain's $25 for stages 1 to 4 less the $0.92 your brief says is spent, so `spent_usd` starts at nought. Raise it there on his next yes, with his words in `"ceiling_set_by"`.

## The tests, as printed

**Test 1, `api_worker.py --selftest`** (no key, no cost; the older cases then the workbook calls; `--workbook-selftest` runs the workbook part alone in under a minute):

    ledger: the older cases wrote 76 faked calls to a throwaway ledger
    WORKBOOK SELFTEST: 17 faked calls (G 3, W 4, C1 3, M 2, C2 2, R 3), no key, no cost.
      999-001__workbook__selftest-lantern      READY      checks 1, mends 0  (ready first time (its W turn pauses once and is continued))
      999-002__workbook__selftest-kettle       READY      checks 2, mends 1  (fails C1, one mend, passes C2)
      999-003__workbook__selftest-compass      NEEDS_CHAT checks 2, mends 1  (fails C1, one mend, fails C2: needs_chat, no third check)
      999-004__workbook__selftest-signed       REFUSED    checks 0, mends 0  (signed: refused before anything is sent)
      staged copies written in <a temporary folder>/runs/selftest/staged; Content Records untouched (the test's records and the real workbook folder)
      ledger: 17 calls written, $0.3925 faked spend, ceiling $20.00
    WORKBOOK SELFTEST OK
    SELFTEST OK.   (exit 0)

The test workbook is invented (idea "The Selftest Lantern Idea", lectures 999-001 and 999-002, a fixture transcript and stance); its blank records are made by vault_gate's own `_blank_record`, the shape `new-record` writes. The faked writer's reply is the exemplar's text with its signed line emptied, so the real gate runs on a real workbook body; the faked checker, mender and reader replies are in `fixtures/workbook_selftest`. The test asserts, among others: the staged copy holds the written workbook, the teaching note, the filled scorecard with read_by_chat empty, a Check history line and the read; the test's records and the real Content Records workbook folder are byte for byte and time for time unchanged; nothing is sent for the signed record; the compass record gets one M, one C1, one C2 and nothing more; the named sentence is gone after the mend; the final gate's only FAILs are read_by_chat and the signature on the ready records. Before this session the worker's `--selftest` did not run at all (the repoint above).

**Tests 2 and 3, `cost_ledger_acceptance.py`** (a throwaway ledger; the anthropic package replaced by a stand-in that raises):

    Test 2: the ledger refuses a spend past its ceiling, and the STOP file stops a step
      PASS  a faked step estimated at $2 against a $1 ceiling is refused
      PASS  the refusal is written to the ledger
      PASS  nothing was counted as spent
      PASS  a step inside the ceiling is allowed and its cost is written: spent $0.50, 1 call line
      PASS  spent plus the estimate is what is checked ($0.50 spent, $0.60 asked, $1 ceiling)
      PASS  the lowest of the caps wins (--max-usd $0.10 under the ledger's $0.50 left)
      PASS  the STOP file stops a faked step
      PASS  the STOP file's refusal is written too
    Test 3: check_batch.py refuses a run that would pass the ledger's ceiling (faked)
      PASS  a faked check of one page against a $0.01 ceiling is refused before anything is sent: exit: COST LEDGER: REFUSED check_batch check for faked-batch: the estimate $0.0657 is above what the ledger's ceiling ($0.01, $0.00 spent) allows: $0.0100 left. Nothing was sent.
      PASS  the refusal is written to the ledger, naming check_batch
      PASS  the same run inside a $100 ceiling goes past the ledger to the (poisoned) send: sent: a paid call was about to be made
    COST LEDGER ACCEPTANCE: 11 of 11 cases pass

**The tests can fail.** Three deliberate breaks of the workbook calls were each caught by test 1: the stop-rule guard removed (AssertionError: a third check was allowed); a third check forced (StopRule: a third check was asked for; the stop rule allows two); the signed line not read (AssertionError: the signed record ran to ready). Test 3 carries its own green control (the same run at $100 reaches the send).

**Test 4:** no real paid call was made. The dry plan on the first batch reads:

    SKIPPED 004-025__workbook__limiting-beliefs: it carries a signature
    Batch workbook_upgrade_b01_s463: 14 record(s): 001-107, 003-152, 013-056, 012-005, 001-041, 003-131, 004-122, 003-133, 001-133, 001-071, 001-125, 015-030, 014-052, 010-006
    Ledger: $24.08 left of its ceiling; this run's --max-usd $20.00; the queue cap $53.82 left.

## Calls Code took that you may overturn

- **Kain's four lessons** are read as the three "Kain's Rewrite Of" notes that are not about an email, and "Kain's Own Rewrite". 03 Voice now holds five "Kain's Rewrite Of" notes; the two email rewrites came later. The worker refuses to run if this does not come to four.
- **The teaching lectures** are the master list's `lectures` column (for Limiting Beliefs its 21 entries match its `teaching_lectures` count of 21). A lecture with no `.corrected.txt` is named to G, not guessed.
- **The estimate is cautious**: every request is priced as writing the shared reading to the cache, every search and fetch used, fetched pages read again. For fourteen records it comes to roughly $9 for W and $12 for C before real costs are known; each later step is checked against the real money spent. If the ledger stops a real batch on its estimate, that is why, and `--only` runs fewer at a time.
- **The written_by and checked_by lines** read `api_worker W (Sonnet 5.5), Session <--session>` and `api_worker C (Opus 5.5), ...`; read_by_chat is always left empty for you.
- **No server-side refusal fallback**: the Batches API rejects it, and the README's rule stands that a refusal is never rerouted to a bigger model. A refused call sends its record to needs_chat.

## Two things this did not do

- The Machine's subfolders are outside the project repository's git (its .gitignore keeps only the Machine's top-level files), and `publish_factory_copy.py` refuses on this Mac: its clone at ~/achology-newsroom names git@github.com:achology-developments/achology-newsroom.git, not the address the script expects. So this change set has no off-machine copy yet. Plumbing, not Kain's: it waits on a factory session told to mend that clone.
- The worker's own queue cap reads $53.82 left of its $200 (its run logs total $146.18). The ledger leaves that cap as it is; whichever is lower stops a step.

## The check sheet

The every-job sheet for this session shows steps 1 to 4 and 6 passed. Steps 5 and 7 (one sample on a rendered page for Kain; his panel showing) do not fit a tool build that puts nothing to Kain, which your brief says, and an exception needs his words, so they are left "not run" rather than marked passed; steps 8 to 10 cannot be filled behind them. If the sheet should carry a step for factory tool builds, that is Chat's to change in check_sheet_source.py.

OWED BACK: nothing. Chat archives this once the tests are rerun.

*No em or en dashes in this file; checked before writing.*
