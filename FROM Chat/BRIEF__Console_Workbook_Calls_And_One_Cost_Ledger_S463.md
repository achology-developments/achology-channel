> CODE DISPOSITION, S487: DONE. The five workbook calls and the one cost ledger are built and tested with no paid call; DONE__Console_Workbook_Calls_And_One_Cost_Ledger_S463 in TO Chat carries each test's printed result and where the ceiling lives.

**For Code, a factory session. What this needs:** the API worker taught to write new workbooks (five calls: gather, write, check, mend, read) and one cost ledger every paid tool draws on, each proved by its own test, then one DONE in TO Chat. Chat, Session 463, 11 November 2026.

This session asks Kain nothing. Every question goes to Chat in TO Chat, as an ASK, and the work carries on where it can.

Model: Opus 5.5. Effort: xhigh.

Done when the worker's selftest shows each of the five calls running on one staged test workbook with no paid call, the ledger refuses a spend past its ceiling in a test, and one DONE in TO Chat names each test and its printed result.

---

## 0. Read first, in this order (they govern the workbook every call writes)

1. **The Workbook Pack** (The Newsroom Vault, The Newsroom, 17 Packs): "The Workbook Pack, Read Whole Before Proposing, Planning or Writing Any Workbook". It governs every brief each call sends.
2. **The Shared Road** (same folder), steps 8 to 13: the calls stand in for steps 8 (write), 12 (the check) and 13 (the read).
3. **The Words notes:** Kain's four rewrite lessons in 03 Voice (the notes whose names begin "Kain's Rewrite Of" and "Kain's Own Rewrite").
4. **The Workbook Standard** (99 Working Papers, reading folder, session_458_workbook_standard_and_plan.html) and **The Workbook Design Standard** (99 Working Papers, standing_documents_S434). The build tool applies the second; this brief does not touch it.
5. **The run books** in 99 Working Papers, workbook_standard_s458: RUNBOOK__Workbook_Upgrade_Programme_S462, section 4, stage 3, items 1 and 2 (this brief is those two items and nothing else); RUNBOOK__New_Course_Workbooks_S460, Kain's word at its foot; and the writer and checker briefs beside them (BRIEF__Writer_Workbook_Rewrite_S459, BRIEF__Checker_Workbook_Scorecard_S459), which are what calls W and C send.
6. **The API worker's README** (02. The Machine, api_worker folder): what the worker does today, its stop rules, its cap and its STOP file.

## 1. Why

Kain said "yes" to 133 new workbooks, one per idea, in nine batches of fifteen, and that the volume runs on the console, never on his weekly plan (Project Instructions, section 3, the limits). Today the worker refuses workbooks: they "wait for their packs", it refuses any signed record, and it has no second writing round. The first fifteen are named this session; fourteen of them run on the console the day this is done.

## 2. Kain's words this rests on

- "we have all these old workbooks in courses that all need upgraded to our current standard ... That is the task", and "I would like us to deliver this workbooks task" (Session 462 close); "Yes, start" (Session 463 open).
- "Yes, one per idea" (Session 462).
- "Yes, start", for stages 1 to 4 of the plan, under $25 (Session 462). $0.92 is spent. **This is the only console spend he has approved.** The ledger's ceiling is set from his yes, never by Code or Chat: set it to $25 less what is spent, and say in the DONE where the one number lives so Chat can raise it on his next yes.

## 3. What to build

### 3.1 Five workbook calls in the API worker

Each call writes to a staged copy in the worker's runs folder, never into Content Records; a signed record is read, never written. Each call's prompt opens with the Workbook Pack, then the Road, then the Workbook Standard, as files read from disk at run time, never pasted copies. Prompt caching on those three and on the exemplar (DRAFT__005-020_anchoring_rewrite_S458, in workbook_standard_s458).

| Call | Model and effort | What it does | Input | Output |
|---|---|---|---|---|
| **G, gather** | Sonnet 5.5, high | Reads every lecture transcript the idea's row marks as teaching it and writes one teaching note: the idea's parts, steps and examples as the lectures teach them, with the lecture code beside each point | the idea's row from MASTER_LIST__Workbook_Upgrade_S462; the corrected transcripts (07. All Achology Videos, transcripts) | `<record>.teaching_note.md` beside the staged record |
| **W, write** | Sonnet 5.5, high, with the server web search and web fetch tools | Writes the workbook whole into the blank record `new-record` made, by BRIEF__Writer_Workbook_Rewrite_S459 as sent to the branch writers, from the teaching note; every reference opened live through web fetch, its address kept | the staged blank record, the teaching note, the stance notes the record names | the staged record, body written, `## Scorecard` holding only the written_by line |
| **C, check** | Opus 5.5, high, with web fetch | Fills the twelve-row scorecard by BRIEF__Checker_Workbook_Scorecard_S459, every reference opened live; never the same call or conversation as W | the staged record | the scorecard rows and one `## Check history` line |
| **M, mend** | Sonnet 5.5, high | One pass over C's FAIL rows only: each named sentence rewritten whole, never patched; the scorecard never touched | the staged record and its FAIL rows | the staged record; then C runs once more; still failing goes to `needs_chat` |
| **R, read** | Opus 5.5, high | Reads every page against Kain's four lessons and the Pack's "What has gone wrong before", and lists each sentence that fails with why | the staged record | `<record>.read.md`; never edits the record |

The free gate runs after W and after M, by script: `content_gate.py <staged record> workbook`. The record goes to `ready` only when the gate's only FAILs are the scorecard's read_by_chat line and the signature (expected before Chat reads and Kain signs). Every other FAIL is `needs_chat`.

**The stop rule** (the S461 rule, the plan's section 8): one mend pass, one more check at most, then `needs_chat`. No loop runs a third time.

**Batch mode:** `--workbook-batch <batch>` takes the vault gate batch folder (02. The Machine, vault_gate, briefs) and runs every record in it that has no signature, through G, W, gate, C, M once if needed, C once more if needed, gate, R. Message Batches API by default, as now. `--only <record>` runs one.

### 3.2 One cost ledger

One file in the api_worker folder that every paid tool reads before a paid call and writes after it: the worker, and `check_batch.py` in vault_gate. It holds the ceiling, the total spent, and one line per call (time, tool, record, call, model, tokens, dollars). Before any paid step, the tool checks spent plus that step's estimate against the ceiling and stops, writing why, if it would pass it. The STOP file stops every tool on the ledger. The worker's own queue cap and `--max-usd` stay, and the lowest of the three wins.

## 4. The tests (each run by Code and printed in the DONE)

1. `--selftest` extended, no key and no cost: one invented test workbook (not a real idea) runs G, W, C, M, R with each call's reply faked from a fixture; it proves the staged copy is written, Content Records is untouched, a signed record is refused, M runs once only, and the third check never happens.
2. A ledger test: ceiling $1, a faked step estimated at $2 is refused and the refusal is written; the STOP file stops a faked step.
3. `check_batch.py` refuses a run that would pass the ledger's ceiling (faked).
4. One real paid call is **not** made in this brief. Chat runs the first real batch once Kain has said yes to its size line.

## 5. What this brief does not do

Stage 3's other ten items (idea-level records, retire, redirects, course copies, the Udemy copy, Drive filing per lecture, the gate's ruled changes, new refusals, the PDF field check, the publishing list) are not in this brief. Today's tools file each new workbook under the lecture that teaches its idea most fully (RUNBOOK__New_Course_Workbooks_S460, its foot), so nothing here waits on them.

## 6. What Chat checks afterwards

The DONE's printed test lines against a fresh run of each test in this Mac's copy of the folder; the ledger file and its one ceiling number; one staged test record opened to see the five outputs.

OWED BACK: one DONE in TO Chat (DONE__Console_Workbook_Calls_And_One_Cost_Ledger_S463), its first line saying what Chat must do with it, with each test's printed result and where the ledger's ceiling lives.

DOCUMENT TYPE: BRIEF

*No em or en dashes in this file; checked before writing.*
