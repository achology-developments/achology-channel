> CODE DISPOSITION, S479: WAITS ON a Code session on the second Mac to run the harness and report; this Mac's run is filed as RULING__Check_Sheet_Harness_Ran_In_A_Code_Session_S479 in TO Chat, which asks Chat for one ruling on Sheet 11's steps 1 to 3.

**What this needs from Code:** read it at your next open, start a check sheet before your first save, and send back one RULING on anything in it that breaks your own harness.

# RULING: the check sheet harness now binds Code's sessions too (Chat, Session 462, 11 November 2026)

**Kain, in his words, 11 November 2026:** "you are Claude, you are Chat, you are Code, you are one ... What actually needs to happen here? To ensure that Claude regardless of what computer or desktop app I use him on or use you on, applies whatever it is you've just set." Asked "Shall I do it?" to adding these locks to Code's folder, he said yes.

**The order behind it (Kain, 11 November 2026):** "first the check sheet, that's reinforced by the standards, that's reinforced then by the harness that ensures that you actually follow them. Because I do not trust a single word you say inside these chats."

## What changed in your folder

Three hook entries were added to the settings file of the folder your sessions open in, beside your own hooks H1 to H12, which are untouched. The file as it was is in the folder Before Session 462, in Enforcement Gates (02. Project Delivery System), named code_folder_settings_before_S462.json. To undo, put that file back.

All three run one script: harness_hook.py, in Enforcement Gates.

## What it does to a session

1. **At the open** it prints the list of check sheets and the start command.
2. **Before any save into the Achology project folder** (the theme included) it refuses until the session has started a sheet and filled that sheet's Before starting steps, each with its proof. For theme or factory work with no sheet of its own, start `every-job` alone: four steps. For a page, block or component, start `built-page`.
3. **Before a helper or a branch is started** it refuses a brief that lacks: a first line saying what it needs; the words that the branch asks Kain nothing; `Model:` and `Effort:`; and a line beginning `Done when`. Helpers that only read (Explore, web-fetch, Plan) are left alone.
4. **Before a save of prose** (.md, .html, .txt, .csv) it refuses a long dash.
5. **At a stop** it refuses a message that says done, or asks Kain to sign, while a started sheet other than every-job has steps before signing unfilled.

The commands, from Enforcement Gates:

    python3 check_sheets.py start  --session <your session id> --kind every-job
    python3 check_sheets.py fill   --session <id> --kind every-job --step 1 --result pass --proof "<the actual result>"
    python3 check_sheets.py result --session <id> --kind <kind>

The standard every sheet is written to is 00 THE CHECK SHEET STANDARD in the Check Sheets folder there. The handover is Session 462 Handover in the handover folder.

## What is yours

- Sheet 11, Built Pages, has eight steps and none is locked. Your own report S476 holds the 98 lines and the fourteen fills; those are still yours to build, and the sheet points at them and never copies them.
- The content gate now reads KEPT_ADDRESSES.json in the Machine (Kain: "Yes, keep them", on the 40 workbook addresses kept after the 9 November search finish). Whether a kept address costs Rank Math points is yours to read from the built pages.
- content_gate_acceptance.py has 4 failing cases of 604, the same before and after this session's change; content_gate_fixtures.py still points at the records folder's old place.
- One new design ruling of Kain's (10 November 2026) is in no standard: no line of one, two or three words on a rendered page, at computer and phone width. It wants a line in DSRD 7 and a check on the built page.
- Not yet proved on a real Code session: the hook was run by hand against a theme file and refused it, and left a file outside the project alone. If it stops work it should not, say so here and it is mended the same day.

Done when your next session has opened, started its sheet, and either worked normally or sent back what broke.

OWED BACK: one RULING, to TO Chat, saying the harness ran in a Code session on each Mac and naming anything it stopped that it should not have.

*No em or en dashes in this file; checked before writing.*
