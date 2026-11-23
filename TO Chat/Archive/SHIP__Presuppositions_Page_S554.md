> Chat S481, 23 Nov 2026: gate lines ruled in FROM Chat/ANSWER__Branch_G_Open_Words_And_Gate_Rulings_S481 section 6. Board: no card moved.
For Chat. What this needs: rule the page gate's open lines on the Presuppositions page (section 3), as you did for /academy/; nothing else is owed.

# SHIP: Achology's Foundational Beliefs and Presuppositions, built into the theme (Code, S554, Branch C)

**Version:** 0.708.411, on the build site at /about/what-achology-believes/ (post 45044). Pushed to main, deployed with deploy.py (local, server and zip agree), zip rebuilt.

**On whose word:** Kain, through the main session: "just build it", on condition that the container, fonts, spacing and structure are right. No signed page spec carrying a PAGE GATE line exists for this page; the build was declared under your copy answers (ANSWER__Presuppositions_Introduction_Block_S552, ANSWER__Presuppositions_History_Expanded_S552), which are "not a page spec", so the intake gate recorded the build as waived, not passed.

## 1. What shipped

- The page in order: the hero; Why We Publish the Beliefs Behind Our Teaching (the Academy's opening block); What Presuppositions Are (About's Answer Tabs); The Seven at a Glance (the Academy's seven-step staircase, each step the hero's jump target); From Plato to Achology (the Academy's history scroll, 19 moments, your words); the article wall and Further Reading; Ten Different Ways (About's block); the questions block.
- Theme files: page-what-achology-believes.php, beliefs-setup.php (each signed block's own sheet and script, unchanged), beliefs-page.css, and the markup in data/beliefs-page/main.json, written by the preview's build.py, with the site address as {{HOME}} so it follows the site to achology.com at the switch.
- Rank Math, set over WP-CLI and read back: title "Achology's Foundational Beliefs and Presuppositions"; description "Everyone lives by foundational beliefs about themselves, human growth and the world. These are the seven presuppositions behind every Achology course." (150 characters, inside DSRD 6 3.2's 155).

## 2. The four checks, measured live in headless WebKit at 1440, 1024 and 375

1. **Container:** every band on the Academy's page container. Heading left and content right: 168 and 1272 at 1440, 48 and 976 at 1024, 20 and 355 at 375, the same on all eight bands.
2. **Fonts:** title 33/700 (28 on a phone); band headings Como 24/600 (21 on a phone); Lead with Bar lines Mulish 18/500; body 16. Off the plain register, each a signed block's own: the Academy opening's paragraphs at 18 (as on /academy/), the staircase numerals 56 (42 on a phone), and 12px labels in the breadcrumb, the Hub tiles, the scroll and Ten Ways.
3. **Spacing:** band padding 64 top and bottom (32 on a phone); heading to lead 16; lead to content 24 on every band. The main session asked for 32; DSRD 7 3.3 and the page gate's supporting-line rule say 24, as the Academy's bands stand, so the page follows DSRD 7.
4. **Structure:** one h1, an h2 per band, no skipped heading level, grounds white and sand in turn under the cream hero with no two neighbours alike, no sideways scroll, no broken picture, no script error.

## 3. The page gate: 44 passed, 43 failed, 10 for review, 7 carved out

Recorded in the page's DSRD6_RECORD.md (About + People Design Prototypes, Presuppositions Page). Code entered no exceptions. Each open line, for your ruling:
- hairline-present (21), header-to-content (3), breadcrumb-above (3), breadcrumb-below (3), spacing-scale about-banner__hero 35 (3): the signed Academy and About band and banner design, the lines you recorded as exceptions on /academy/ (ANSWER__Academy_Page_Gate_Lines_S533 items 1 and 2).
- supporting-line (6): band headings at 21 on a phone, as that answer's item 6.
- spacing-scale b1-pane 18 (1): About's Answer Tabs' own rule.
- image-responsive (1): course-001-540.webp, About's Ten Ways picture, carried unchanged.
- acronyms (1): BCE, CE, ABC and IQ in the history's words (yours).
- keyword-density (1): the template page's empty editor body, the carve-out Pricing, Accreditation and Events take.
- rank-math (1): waits on Kain's one-click rescore.

css_gate: PASS on beliefs-page.css.

DOCUMENT TYPE: ship brief.

*No em or en dashes in this file; checked before writing.*
