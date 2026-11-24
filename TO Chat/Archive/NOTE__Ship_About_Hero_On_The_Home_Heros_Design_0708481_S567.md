> Disposition, Chat S487, 24 Nov 2026: read with its ruling, written home as above; archived.
For Chat: what this needs: read it; three small confirmations in section 4 and the fold-back owed in section 5. Card #32 (About is in the launch page check).

Done when: section 4's three lines carry an answer or a head line.

**DOCUMENT TYPE:** ship note from Code (theme side session of the S567 page-check sitting, the About hero, 24 November 2026). **Answers:** nothing in FROM Chat; Kain's own idea and pick (RULING__About_Hero_On_The_Home_Heros_Design_Kains_Pick_S567). Peer sessions checked at the open: the Membership banner session (local_e263812a, working in membership.css and its own preview files, not about.css) and the Home sessions (home-page-s558, not touched); none worked in the About files.

## 1. What shipped, theme 0.708.481

The About page's hero is now the Home hero's design: one dark band with the breadcrumb, the title, the line and one button on the left, the page's own wall of the field's thinkers faint behind the words, and the film (Vimeo 708764177, the page's own picture of it) easing in from the right and playing inside the band. Pressed, the band grows to hold the film at the column's width, the picture grows into a card with the faces rising round it; the cross or Escape returns the banner. About's words are exactly the page's own: "About Achology", the line "Since 2014, our learning platform has taught 695,578 people across 216 countries about the human mind, communication and self-awareness. Watch the film, then read how Achology began.", the button "Read the Achology Story". Nothing drafted. The button is now the button family's orange primary (as on Home and Membership), not the outline secondary on cream. The page below the banner is unchanged.

Built from: a new hero-film.css (the Home hero's design as a component at a page's own depth, lifted from the Membership banner's rules and the Home hero's S565 rules), the existing hero-film.js, the swap of the banner part only in data/about-page/main.json (previews/about-hero-s567/about_banner_s567.py), and about-setup.php switching the sheet and script on for the About page. about.js's back-to-top now counts the band as the hero.

## 2. The round Kain chose from (proved, 11 measured, 0 failed)

Four whole options in the Change Viewer (previews/about-hero-s567/round-ahero.js): 1 the Home hero (the pick), 2 the film as a card on a wall of faces, 3 the film as a crisp split screen, 4 the film behind the words. Kain: "Option 1, the Home hero."

## 3. Measured on the build site (the mirror, 1440, 1024, 390)

Title Como 33/700 (28 on a phone), line Mulish 18/500 (16), the line three rows on a computer; 48 above the breadcrumb (32 on a phone), 24 to the title, 24 to the line, 32 to the button, 64 under it on a computer; the band 377 deep at 1440 and 1024, 625 at 390; no sideways scroll; one h1; played and closed at 1440. page_gate on /about/ at 0.708.481: 48 pass, 1 fail, 10 for review, 80 carved out; the one fail is the DSRD 6 record (6 closed, 3 not run, 2 fail), as before this change. css_gate on hero-film.css: pass. deploy.py: local, server and zip agree at 0.708.481. Two things the gate asked on the way, both mended: the phone's breadcrumb sat 48 below the header and now sits 32; the button's phone size (about.css forces 12) is held at 14 by a rule of higher reach.

## 4. Three lines for you (not for Kain)

1. **page_gate.py, About's breadcrumb-below rows.** The dark band keeps the 24 below the breadcrumb that the Courses band carries as Kain's S137 ruling, recorded by you at S445 (DSRD 7 4.3 Exception 15). I entered the same recorded exception for the three widths on About, citing both. Please confirm it, or tell me what the title should sit at.
2. **header-to-content on About** (0.0px, "want 48"): kept as the signed top-of-banner exception you ruled at S480 1.3, its words changed from "Cream Hero" to the banner's own top. Confirm.
3. **The DSRD 6 record's open chapters** (§2, §3, §4, §5, §9, lines the record carries from before this change) are not mine to close in this change set; About reads "built, gate open" on them as it did at 0.708.478. Say whether the About redraw's record is next.

## 5. Owed fold-back and a follow-up for the Membership session

- **Component registry and fold-back (The Harness, Rule 14):** hero-film.css is now a component used on two pages (About and Membership, Home next). It needs its row in the Component Registry and its design folder's prototype and build sheet; I have not written them (outside this change set's files). Chat or the next theme session writes them.
- **membership.css still carries a copy of the same band's rules** (its "S567" block) and does not load hero-film.css. The Membership session should switch Membership to hero-film.css and delete its copy, so the registry gate does not meet two homes. The one place the two differ: hero-film.css puts the breadcrumb 32 below the header on a phone (the page gate's line); Membership's copy keeps 48 and will meet the same gate line.

OWED BACK: your answer to section 4's three lines.
