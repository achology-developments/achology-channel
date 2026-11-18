NEEDS FROM CODE (theme): two free GitHub tools brought in, Focus Trap for the event ticket and Lychee for the link crawl, each proved on the build site.

# BRIEF: Focus Trap and Lychee, borrowed from GitHub

**For:** Code, a theme session. **From:** Chat, 18 November 2026. **Kain's word:** "Yes, brief Code", on the list of ten tools (02. Project Delivery System, Ten GitHub Tools 18 November 2026.html). This brief carries the first and third of those ten; Vale, the second, goes to the factory in its own brief.

**The rule for both.** Borrow a tested tool rather than write our own. Each one goes in on its own, earns its place on a real job, and comes out again if it does not. Nothing is loaded from another site: copy the file into the theme or install the tool on this computer.

## 1. Focus Trap, on the Events ticket

**Why.** Chat's keyboard walk on /events/ at 0.708.184: the ticket carries aria-modal, but Tab from its Close button leaves it for the kinds cards behind the dark screen (FROM Chat/ANSWER__Events_Week_Line_And_About_Rulings_18Nov, section 3). That section is answered by this one.

**What.** focus-trap (github.com/focus-trap/focus-trap, MIT licence, version 7 or the latest stable). Copy its built file into the theme and enqueue it only on pages that open a ticket or other dialog. Use it for the Events ticket: Tab and Shift Tab stay inside while it is open, the page behind is inert, and Escape, the close mark and the dark screen still close it and return focus to the event that opened it. If the theme already has its own trap code for any other dialog, say where, and move it to focus-trap in the same change only if no visible change follows.

**Proof.** The keyboard walk on /events/ at computer and phone width: open a ticket with Enter, Tab ten times, and every stop is inside the ticket. axe still reports 0 violations. The page weighs no more than the library's size, said in bytes.

## 2. Lychee, for the link checks

**Why.** The Events orphan check stops on the same 2,219 pages, each answering 502 through the mirror (DONE__Events_Five_Word_Fixes_And_Reader_Mends_S531, section 3). The school story source links were checked one by one in a browser because publishers refuse simple fetches (BRIEF__School_Story_Source_Links_S475).

**What.** lychee (github.com/lycheeverse/lychee, Apache licence), installed on this computer through Homebrew. Run it against the build site from its sitemap, at a polite rate, with retries for 502 and 429, and a real browser user agent. Keep its settings in one file in the theme's tools folder so every session runs it the same way.

**Proof.** One run over the whole build site, saved beside the Events record: pages read, links checked, links broken, links the host refused. Compare it with the orphan crawl's last run and say which pages each one reached. Then say plainly whether Lychee replaces the orphan crawl's fetch, works beside it, or does not earn its place.

## Limits

No change Kain can see on any page. No new plugin in WordPress. Whatever Lychee finds broken is listed, not mended in this sitting; Chat rules what to mend.

Done when the Events ticket keeps Tab inside it on the build site, and the first whole-site Lychee run is saved with Code's verdict on it.

OWED BACK: a DONE in TO Chat with the version, the walk, the bytes added, the Lychee numbers and the verdict.

*No em or en dashes in this file; checked before writing.*
