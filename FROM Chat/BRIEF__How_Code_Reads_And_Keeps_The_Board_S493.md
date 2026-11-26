For Code, every session. What this needs: set up GitHub board access on Code's Mac once, then keep the board by the rules below.

Done when: Code's Mac reads the board with `gh project item-list 1 --owner achology-developments`, and every Code close moves its own cards by these rules.

## 1. Access (one time, with Kain)

Chat's Mac uses the GitHub CLI, gh 2.105, signed in as Kain's GitHub account kain-ramsay, token kept in the macOS keychain, scopes gist, project, read:org, repo. Nothing else (no connector, no token in any file).

On Code's Mac:
1. Install gh: `brew install gh` (or put the binary at ~/bin/gh as Chat's Mac does).
2. `gh auth login --web --scopes project,read:org,repo,gist`. It shows a one-time code; Kain types it in his browser while signed in to GitHub as kain-ramsay. Kain approves; nobody pastes a token anywhere.
3. Check: `gh auth status` shows the project scope; `gh project list --owner achology-developments` lists ten projects.

## 2. Where the board is

Organisation achology-developments. The working board is project 1, Achology Web System. Project 2, Achology Developments, is the master board (one card per project); Code does not edit it. Cards are draft issues on the board or issues in achology-developments/achology-board (for example #78 Get Found).

Status column: Backlog, Ready, Building, Checking, Done.

## 3. The rules (the Project Instructions section 3, and Kain's own rulings)

- Every card is one finished thing, with its done test in one line. Status is recorded only on the board.
- A card holds only what is left and its done test. No history: no session numbers, no "done so far", no lists of what was built (Kain, S448: "anything that's done needs to be scrapped, not recorded"). When the work is finished the card goes to Done and leaves the working view.
- Code's limit: at most 2 cards in Building (one theme job, one factory job) and 3 in Ready.
- What Code moves: its own cards, Ready to Building when it starts, Building to Checking when its DONE is written. Code never moves a card to Done: Chat checks it and Kain accepts it. Code may add one line to a card's "what is left" when its own work changes it.
- What Code does not touch: other cards' wording, the Decisions for Kain list, Backlog: Chat, the master board, and any card Chat is checking.
- New work Code finds goes as one line on Backlog: Code, never as a new card, unless Kain asks for a card.
- Card names: an emoji, a plain name, a colon, then what done looks like in plain words, for example "🚀 Google Search Console: Tell Google About The New Site".
- Two dates on every card: Started (set when it enters Building) and Finished (set when it reaches Done).

## 4. Today's work, for Code's first board pass

Chat already recorded IndexNow, the 321 push, the 32 redirects and Clarity against #78 Get Found (Chat will strip that card back to what is left, per the no-history rule). Code's speed sweep (0.708.492 to 0.708.501), finder fixes, click-check fixes (0.708.504/505) and the Achology and SoMAP staging sites: move or close their own cards to Checking with the version in the DONE file, not on the card.

Nothing for Kain beyond the one sign-in in section 1. Questions into TO Chat.
