For Code (any session, S563): what this needs: mend the vault gate so it reads Kain's typed words when the app puts a note in front of them, then record his approval of the Help 332 title.

Done when `vault_gate.py approve-titles help332_shorter_vs_practitioner_s482 --kain-said "Yes, approved" --session cc7de36d-0dbb-4f48-bc45-6f3b59ccef16` passes, and Chat is told so.

**DOCUMENT TYPE:** brief from Chat (S563). An invisible fix, so Kain is not asked.

**The fault.** Kain typed "Yes, approved" in Chat's session cc7de36d on 23 November 2026 at 22:47 (the transcript entry has origin kind "human"). The gate refused it with "not in any of Kain's last 3 messages". In vault_gate.py, kains_messages() joins every text block of a user turn and skips the turn if the joined text starts with "<". The app put a system-reminder block ("Linked sessions now …") in front of his words, so every message like that is lost.

**The mend.** Drop text blocks that start with "<" one at a time and keep the rest, or strip system-reminder blocks before the test. Keep the other guards as they are: tool results, isMeta and sidechains still don't count.

**Already done by Chat.** The titles file is in briefs, as help332_shorter_vs_practitioner_s482_TITLES.json. The page csv is ready. After the approval passes, Chat builds the batch and writes the record.

OWED BACK: one line to Chat when the approval passes.

*No em or en dashes in this file; checked before writing.*
