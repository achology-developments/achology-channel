NEEDS FROM CODE (factory): Vale, a free writing checker from GitHub, set up with our own word rules and run beside the content gate on one batch, with a verdict.

# BRIEF: Vale, borrowed from GitHub, for the word checks

**For:** Code, a factory session. **From:** Chat, 18 November 2026. **Kain's word:** "Yes, brief Code", on the list of ten tools (02. Project Delivery System, Ten GitHub Tools 18 November 2026.html). Vale is the second of the ten; the theme half is FROM Chat/BRIEF__Focus_Trap_And_Lychee_From_GitHub_18Nov.

**Why.** Our word checks are code we wrote and keep ourselves: the banned and watched words, the long dash scan, and the word rules inside content_gate.py. Vale (github.com/vale-cli/vale, MIT licence, updated this month) is a tested engine built for exactly this. It reads a page the way a spell checker does, against rules we write, and names the line and the word.

**The rule.** Borrow the engine, keep our rules. Every rule comes from where it already lives: content_gate_standards.json in The Machine, and the banned and watched word notes in the vault's Words index. No rule is added, loosened or invented here; where a rule cannot be written in Vale, list it.

## What to do

1. Install Vale on this computer through Homebrew. Keep its settings and our style folder inside The Machine, so every session runs it the same way.
2. Write our rules as one Vale style named Achology: banned words, watched words, long dashes, and whichever other word rules in content_gate_standards.json fit Vale's rule kinds. Each rule names its home in a comment.
3. Run Vale and the content gate side by side on the last signed batch of Help answers and one batch of quote articles.
4. Compare them line by line: what both caught, what only Vale caught, what only the gate caught.

## Limits

The content gate stays the gate. Vale changes no page, signs nothing and blocks nothing in this sitting. Nothing about it is shown to Kain until Chat has read the comparison.

Done when the Achology style exists with every rule traced to its home, the side by side run on both batches is saved in The Machine, and Code says plainly whether Vale should take over the word checks, sit beside the gate, or not earn its place.

OWED BACK: a DONE in TO Chat with the rule count, the rules Vale could not express, the comparison numbers and the verdict.

*No em or en dashes in this file; checked before writing.*
