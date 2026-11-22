> CODE, 22 November 2026, factory sitting. Kain's ask: find the 404s on the build site and correct them.

# DONE: Link audit of achologytest.com

**Report page:** previews/link-audit-s546/index.html in the theme folder (open in Safari).

**How:** every published URL (1,654, plus the homepage) read from the server itself at one page per third of a second; 19,024 distinct build-site addresses (links, pictures, stylesheets, scripts) then checked once each; second full crawl after the fixes. No picture, stylesheet or script 404 anywhere. External sites and the live achology.com were not touched. No theme file changed, so no theme deploy.

**Counts:** 9 broken before, 7 now. 39 links fixed. 0 waiting on unbuilt pages.

## 1. Fixed (post content and one stored setting, link text only; DB backup ~/db-backups/achologytest-before-link-fix-2026-11-22.sql.gz on the server)
- 26 old-site absolute links (https://achology.com/...) made site-relative where the path exists here: 2 Help answers (in 49 Help answers' Related questions) and 24 Academy diploma, article and book note paths (in hundreds of quotes, articles, book notes).
- achology.com/learn/schools/nlp/ (404) to /academy/neuro-linguistic-programming/.
- 4 old-site addresses with changed slugs to their current ones: self-awareness-and-personal-growth to why-is-self-awareness-important; the Asch, Milgram and Little Albert experiment articles to their /learn/.../articles/ addresses.
- /learn/psychology/articles/aaron-beck/ (404) to aaron-beck-the-pioneer-who-revolutionized-cognitive-psychology.
- 6 quote links on old slugs (redirects worked) now point straight at the current quote.
- /free-events/ in one stored setting to /events/.

## 2. Needs a choice (7 still 404; the article does not exist here)
- /learn/psychology/articles/what-is-identity-formation/ (book note childhood-and-society)
- /learn/helping-people/articles/cultural-encapsulation-in-counselling/ (counseling-the-culturally-diverse)
- /learn/personal-growth/articles/how-to-take-accountability-at-work/ (extreme-ownership-willink)
- /learn/mental-wellness/articles/recognising-cognitive-distortions/ (feeling-good-burns)
- achology.com/learn/wisdom-for-life/articles/how-to-reason-through-difficult-decisions/ (the-republic-plato, the-tao-te-ching, utilitarianism), still absolute
- achology.com/learn/wisdom-for-life/articles/what-is-philosophy-and-why-does-it-matter/ (the-history-of-philosophy), still absolute
- achology.com/learn/wisdom-for-life/articles/what-is-self-awareness/ (the-perennial-philosophy), still absolute

Also: /cards/ is a published page (post 10903) that answers 404 to visitors; nothing links to it. /free-events/ is still linked from the About page, Manifesto and two Help answers via theme files (page-about.php, template-policy.php, policies-content/manifesto.php); it redirects to /events/, so it works; changing it is a theme edit, left for a theme session. One quote link redirects to the articles list (should-mental-health-be-taught-in-schools).

## 3. Waiting on unbuilt pages
None. No link on the build site points at a homepage section or the beliefs page that does not exist yet.
