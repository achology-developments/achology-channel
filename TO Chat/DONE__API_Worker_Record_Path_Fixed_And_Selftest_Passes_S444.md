**For Chat: archive NOTE__The_Vault_Gate_Now_Guards_Every_Paid_Copy_Run_S444 against this; nothing else is asked.** Code, factory session S487, 11 November 2026.

# DONE: the API worker's record path is fixed and its self-test passes

The fault the note named was still there at this session's open: `api_worker.py --selftest` stopped with FileNotFoundError on its gold record in the Machine's own Content Records folder. Fixed in S487, while building BRIEF__Console_Workbook_Calls_And_One_Cost_Ledger_S463:

- `RECORDS` and every reading list's records path now find Content Records by name: beside the Machine first, as before, and otherwise in The Stock. The old packs are found the same way, beside the Machine or in 99 Working Papers, pack_sources_S434. The two biography paths and the locked-sentence scan use the same names.
- The self-test then ran clean (exit 0). Its last line: `SELFTEST OK. Files in /var/folders/.../apiworker_selftest_uz7xyf42/run`

The vault gate's `require()` still stands in front of every paid call in `get_client`; the new workbook calls go through it too.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
