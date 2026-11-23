> Disposition, Chat S480, 23 Nov 2026: card 06 is the free events card on /about/, /reviews/ and /testimonials/ at 0.708.403, as briefed. The finding (two Code of Ethics cards on the free tier link) is answered in FROM Chat/ANSWER__Code_Of_Ethics_Card_Words_S480. Archived.

NEEDS FROM CHAT: read for the record; one finding at the foot (two other links still go to the closed free Circle tier).

# DONE: About, Ten Ways card 06 is the free events (Code, Branch G, S559, 23 November 2026)

Answers FROM Chat BRIEF__About_Ten_Ways_Card_06_Free_Events_Not_Coaching_S480. Theme session, Branch G. **Theme 0.708.403**, commit 77797ec4 on main, deployed and proved by deploy.py (server, zip and version agree).

## What changed

Card 06 now reads, word for word: "06", "Join a FREE Live Learning Event Every Week", "If you can't spend money yet, join one of four free live events each week, open to everyone.", and opens /events/. Same look, size, place and icon as signed; nothing else in Ten Ways moved; card 10 untouched.

Ten Ways is drawn in two places, and both changed:
- /about/ (the signed redraw): data/about-page/main.json. The signed preview it is lifted from (previews/about-redraw-s544/about.html) took the same words and link, so a rebuild by tools/about_page_data.py keeps them.
- /reviews/ and /testimonials/ (the Ten Ways grid, achology_site_routes() in shared-parts.php).

## Proof, on the build site in a browser at 1280 and 375

On /about/, /reviews/ and /testimonials/ at both widths: card 06 carries the words above and href /events/; the old "FREE 1-1 Coaching" words appear nowhere on the page; no link in the page body goes to the invitation_token join address; style.css serves at ver=0.708.403. Pictures about-card06-1280.png and about-card06-375.png in the shared notes folder, branch-g-launch.

## For the other branches

The Homepage preview (Branch F) and the Presuppositions preview (Branch C) were not touched. Any preview that lifts Ten Ways from the build site takes the new card on its next refetch; one that copies it by hand needs the words above.

## Finding, not touched (outside this brief)

Two more links still go to the closed free Circle tier (community.achology.com/join?invitation_token=...): the Manifesto's Code of Ethics card in policies-content/manifesto.php, and the matching Code of Ethics card in shared-parts.php ("Watch the Code of Ethics Training", "free to watch with a free level of Achology membership"), both through the same address as ACHOLOGY_COMMUNITY_JOIN_URL in functions.php. Their words are Chat's to rewrite.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
