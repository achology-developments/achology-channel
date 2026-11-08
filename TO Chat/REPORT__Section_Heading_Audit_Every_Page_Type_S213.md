**For Chat. What this needs from you:** the sweep brief for Kain to sign, built from this audit; section 3.6 lists the decisions the brief must make. Code, section heading audit session, 8 November 2026. Read-only: nothing on the site or in the theme was changed.

# REPORT: Section Heading and Supporting Line Audit, Every Built Page Type (S213)

## 1. Method

- Site: achologytest.com (build ground, noindex). Playwright WebKit, 1280 and 390 wide, one page at a time with a 3 second pause, scrolled through once so reveal animations had fired. 29 pages across 26 templates were measured (the full list is in section 4). Computed styles are read from the rendered page; the "class and stylesheet" columns name the last matching rule that sets the font size (heading) or font size (supporting line), found by walking the loaded stylesheets.
- "Block" means an h2, or an h3/h4 followed directly by a sibling element. "Supporting line" is the element directly after the heading. In articles, book notes and quotes the element after an h2 is the first body paragraph, not a designed supporting line, so those rows read as "supporting line = body text" (Mulish 18/400 or 16/400, no edge). They are listed because the standard would have to say whether reading-body h2s take a supporting line at all (section 3.6, decision 3).
- Not counted: page titles (h1, listed but marked), footer headings (site-wide, one rule, see 3.4), and card or item titles (counted per page, not listed).
- Standard compared against: heading Como 24/600 brand dark #354149 (white on a dark band); supporting line Mulish 18/500, line height 1.55, brand dark, 2px orange left edge, 16px inside.

## 2. What is NOT measurable on the build site

These types are not built on achologytest.com yet, so there is no rendered page to measure. A request returns the 404 body (the front page `/` returns status 200 but shows the 404 body, because the theme has no front page template and falls back to the 404 content):

| Type | Address tried | What the site returns | What I used instead |
|---|---|---|---|
| Front page | `/` | 404 body | nothing exists to measure |
| Schools overview | `/schools/` | 404 body | nothing exists |
| School pages | `/academy/mindfulness/`, `/academy/personal-growth/` | 404 | nothing exists |
| Course pages | `/academy/mindfulness/mindfulness-leadership/`, `/academy/life-coaching/life-coaching-certificate/` | 404 | the committed theme source (below) |
| Cards, What Achology Believes | `/cards/`, `/what-achology-believes/` | 404 body | `page-cards.php` exists, page not created |
| Membership, Access All Areas, Free Events, Free Coaching, Academy Schools | their addresses | empty "Archives" fallback | no template yet |

Course page, from committed theme source (`template-course.php`, `course-parts.php`, `course.css`), not rendered: every block heading is `.course-block__title` at `--text-33` (33px) in Como, brand dark; its supporting line is `.course-block__lead` at `--text-18`, mid grey #5e6b75, no edge, no weight set (400). Eight blocks in the template (What You Will Learn, Watch the Introduction Video, Your Instructor, What the Course Covers, Real Learning Experiences, What the Certificate Is, Three Ways to Study, Questions People Ask) use it, plus `.course-optin__title` (21px, no supporting line), `.course-curriculum__heading` (18px, an accordion row) and `.course-qa__h` (accordion). The 24/600 plus Lead with Bar version exists only in the course page preview (picks 220 and 221) and is not in `course.css` yet. A link to a page that is not built is a page to come, not a fault; this section is only a list of what the sweep cannot be proved against yet.

## 3. Summary

### 3.1 Counts

- Built templates measured: 26 (29 pages). Not built or not measurable: front page, schools overview, school pages, course pages (source only), cards, plus five empty address stubs.
- Block rows measured: 201 (counted per heading, 1280 wide; pages that repeat a pattern, such as the policy pages and article h2s, count every heading).
- Block headings that already match the standard (Como 24/600, brand dark or white on a dark band): 135 of 201.
- Supporting lines that match the standard (Mulish 18/500, lh 1.55, 2px orange edge, 16px in): **0 of 201.** No built page has a supporting line in the new style. The closest thing is the About page FAQ answers, a 3px orange edge with 24px padding (an accordion answer, not a block supporting line).
- 12 of the 201 blocks have no supporting line at all (counted as "none" below).

### 3.2 Distinct heading styles in use today (13)

| Count | Style | Stylesheets that set it |
|---|---|---|
| 130 | Como 24/600 #354149 (the standard) | base.css, book-note.css, components.css, enquiries.css, help.css, kh-search.css, kh-subject.css, knowledge-hub.css, people.css, policies.css, pricing.css, testimonials.css |
| 22 | Como 18/700 #354149 | base.css |
| 9 | Como 16/600 #354149 | accreditation.css, certification.css |
| 7 | Como 21/600 #354149 | book-note.css, certification.css, enquiries.css, knowledge-hub.css |
| 7 | Como 18/600 #354149 | policies.css, pricing.css |
| 5 | Como 33/600 #354149 | base.css (the generic h2 at 1280 on the article close band), kh-tag.css |
| 5 | Como 24/600 white (the standard on a dark band) | global-impact.css, policies.css |
| 5 | Como 0/600 (FAQ accordion row h3 wrapping a button, text drawn by the button) | about.css |
| 4 | Como 12/600 #b8460f (small orange caps label) | knowledge-hub.css |
| 4 | Como 12/600 #5e6b75 (small grey label) | pricing.css |
| 1 | Como 12/600 #8a9199 | people.css |
| 1 | Como 18/600 white | pricing.css |
| 1 | Como 16/600 white | enquiries.css |

Mobile: two headings change size at 390 by design (the generic h2 33 to 28 on the article close band; the tag page h3 33 to 24). Everything else is the same at both widths.

### 3.3 Distinct supporting line styles in use today (24, plus "none")

| Count | Style | Stylesheets that set it |
|---|---|---|
| 78 | Mulish 18/400 lh 31.5 #354149, no edge (mostly the body paragraph under an article or policy h2) | book-note, certification, help, knowledge-hub, policies, warm-room |
| 60 | Mulish 16/400 lh 25.6 #354149, no edge | accreditation, certification, policies, testimonials |
| 12 | none | not applicable |
| 11 | Mulish 16/400 lh 25.6 grey #5e6b75, no edge | components, enquiries, policies, pricing, testimonials |
| 6 | Mulish 14/400 lh 22.4 grey #5e6b75 | base, people, policies |
| 5 | Mulish 16/400 lh 25.6 #354149, 3px orange edge, 24px in (About FAQ answers) | about.css |
| 4 | Mulish 12/600 orange caps | book-note, knowledge-hub |
| 4 | Mulish 18/400 lh 28.8 grey | base.css |
| 3 | Mulish 16/400 white | policies |
| 2 each | Mulish 18/600 dark; Mulish 16/400 lh 28 dark; Mulish 16/400 grey lh 24.8; Mulish 16/400 white lh 24; Como 24/700 (pricing price lines) | knowledge-hub, book-note, policies, global-impact, pricing |
| 1 each | Como 28/700 in four colours (pricing figures); Mulish 16/400 lh 26.4 (about); Mulish 12/400 white; Mulish 14/400 grey and dark (enquiries) | pricing, about, enquiries |

No supporting line at 500 weight, and none at line height 1.55, exists anywhere today.

### 3.4 Where the styles live

Heading styles are set in 18 stylesheets: base.css (the generic h1 and h2 rules, which are what most pages fall through to), book-note, components, enquiries, help, kh-search, kh-subject, kh-tag, knowledge-hub, people, policies, pricing, testimonials, accreditation, certification, about, global-impact, plus footer.css for the footer column heads (Como 12/600 #f5a05c, site-wide, outside this standard). Supporting lines are set in the same group plus warm-room.css; for some rows I could not name a rule (the size is inherited, or set in a way my rule walk could not match), marked "?" in the tables.

The closest existing shared pieces are `.policy-next__title`/`__lead` and `.help-popular__heading` with `.kh-section__subtext` (the only two heading-plus-line pairs on more than one template), `base.css h2`, and `.course-block__title`/`__lead` (source only). Nothing is yet a single section heading component.

### 3.5 What stands out

1. The heading is nearly done: 130 of the Como 24/600 headings come from 12 different stylesheets, each with its own rule. The sweep is mostly consolidation, not restyling.
2. The supporting line is not done anywhere. Today it is body copy sized 14, 16 or 18, at weight 400, with no edge.
3. The odd headings (18/700 in base.css on 22 blocks; 16/600 on certification and accreditation; 21/600; 33/600) are the real restyles.
4. Reading templates (article, book note, quote, policy, help answer) put the h2 straight over body text with no designed supporting line. Whether those get one is a decision, not a measurement.
5. Dark bands (policy-next, global-impact, pricing, enquiries) already switch the heading to white; their supporting lines are white 16/400, so the "keeps its light colour" rule needs only the size, weight and edge.

### 3.6 Decisions the sweep brief must make (for Chat; none is put to Kain by Code)

1. **Which headings are "block headings".** The footer column heads (12/600 orange caps), the small caps labels (Table of Contents, Share this Article, pricing and people labels) and accordion rows are not blocks; the brief should list them as exempt so the sweep does not flatten them.
2. **The 22 Como 18/700 headings in base.css, the 16/600 on certification and accreditation, the 21/600 and the 33/600 headings:** each needs a ruling that it is a block heading (moves to 24/600) or a different component (stays).
3. **Reading templates** (article, book note, quote, policy, help answer): does an h2 in running body text take a supporting line, or only the designed blocks (hero-adjacent bands, cards sections, close bands)? Today they have none.
4. **Pricing** has Como 28/700 price lines directly under its headings; they are figures, not supporting lines.
5. **Unbuilt types** (front page, schools, school pages, course page, cards): the brief can name them as "built to the standard from the start" and the course template as the first move, since the committed `course.css` is still 33 and grey.
6. **Order, smallest reach first** (a suggestion for step 4 of Kain's plan): Help hub and answers, Policies and policy family, Reviews, Testimonials, Certification, Accreditation, Pricing, Enquiries, About, Our People, Knowledge Hub subject and tag, then article, book note, quote and search last.

## 4. Tables, one per template

Row format: page, then the block (tag, count of identical rows on that page, an example heading, and "[dark band]" where the background is dark), heading style at 1280 (with the 390 style only where it differs), supporting line style, then the CSS rule and stylesheet that set each (`stylesheet.css` then the selector), then whether it matches the standard. Identical rows on a second page of the same template are not repeated.

### Courses Directory (template-courses.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /courses/ | H2 x1: Start With One of Our Most Popul | Como 24/600 #354149 | none | base.css `h2` | - | heading yes, line no |
| /courses/ | H2 x1: FAQs About Our Online Psychology | Como 24/600 #354149 | none | help.css `.help-close__heading` | - | heading yes, line no |

### Knowledge Hub front (kh-front)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /learn/ | H1 title x1: The AchologyKnowledge Hub | Como 33/700 #354149 | none | kh-front.css `.kf-h1` | - | page title (not a block heading) |

### Knowledge Hub subject page (taxonomy-kh_category.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /learn/psychology/ | H1 title x1: Psychology | Como 33/700 #354149 | Mulish 21/400 lh33.59 #354149 no edge | kh-subject.css `.mx-text .hx-title` | kh-subject.css `.mx-summary` | page title (not a block heading) |
| /learn/psychology/ | H2 x1: The Editor’s Picks | Como 24/600 #354149 | none | kh-subject.css `.bx-picks__h` | - | heading yes, line no |

### Knowledge Hub tag page (taxonomy-kh_tag.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /learn/tags/build-confidence/ | H1 title x1: Build Confidence | Como 33/700 #354149 | Mulish 18/400 lh29.70 #5e6b75 no edge | kh-tag.css `.tgp-ban .tgp-t` | kh-tag.css `.kh-hub .tgp-ban .tgp-sum` | page title (not a block heading) |
| /learn/tags/build-confidence/ | H3 x1: What Are the Signs of Low Self‑E [dark band] | Como 33/600 #354149 (390: Como 24/600 #354149) | Mulish 16/400 lh25.6 #354149 no edge | kh-tag.css `.tgp-l3 .tgp-tb__t` | ? | heading no, line no |

### Article (single-article.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /learn/psychology/articles/william-james | H1 title x1: Who Is William James? His Biogra | Como 33/700 #354149 (390: Como 28/700 #354149) | Mulish 21/400 lh33.59 #354149 no edge (390: Mulish 18/400 lh28.79 #354149 no edge) | base.css `h1` | base.css `p` | page title (not a block heading) |
| /learn/psychology/articles/william-james | H2 x1: Table of Contents | Como 21/600 #354149 | Mulish 12/600 lh16.20 #b8460f no edge | knowledge-hub.css `:is(.kh-article__body, .bn-body) > .kh-aside .` | knowledge-hub.css `.kh-article__body p, .kh-article__body li` | heading no, line no |
| /learn/psychology/articles/william-james | H2 x1: An Introduction to this Great Th | Como 24/600 #354149 | Mulish 18/600 lh31.5 #354149 no edge | knowledge-hub.css `.kh-article__body h2` | knowledge-hub.css `.kh-article__body p, .kh-article__body li` | heading yes, line no |
| /learn/psychology/articles/william-james | H2 x4: William James: Early Years and F | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | knowledge-hub.css `.kh-article__body h2` | knowledge-hub.css `.kh-article__body p, .kh-article__body li` | heading yes, line no |
| /learn/psychology/articles/william-james | H2 x1: Share this Article | Como 12/600 #b8460f | Mulish 16/400 lh25.6 #354149 no edge | knowledge-hub.css `.kh-aside .kh-aside__head--share, .kh-aside__s` | ? | heading no, line no |
| /learn/psychology/articles/william-james | H2 x1: Ready to Further Your Learning? | Como 33/600 #354149 (390: Como 28/600 #354149) | Mulish 18/400 lh28.79 #5e6b75 no edge (390: Mulish 16/400 lh25.6 #5e6b75 no edge) | base.css `h2` | base.css `p` | heading no, line no |
| /learn/psychology/articles/william-james | (2 item or card titles not listed) | | | | | |
| /learn/motivation/articles/robert-greene | (2 item or card titles not listed) | | | | | |

### Book note (single-book_note.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /learn/psychology/book-notes/mans-search | H1 title x1: Man’s Search for Meaning by Vikt | Como 33/700 #354149 (390: Como 28/700 #354149) | Mulish 21/400 lh33.59 #354149 no edge (390: Mulish 18/400 lh28.79 #354149 no edge) | base.css `h1` | base.css `p` | page title (not a block heading) |
| /learn/psychology/book-notes/mans-search | H2 x1: Table of Contents | Como 21/600 #354149 | Mulish 12/600 lh16.20 #b8460f no edge | book-note.css `.bn-body h2` | book-note.css `.bn-body p` | heading no, line no |
| /learn/psychology/book-notes/mans-search | H2 x4: What This Book Is Saying | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | book-note.css `.bn-body h2` | book-note.css `.bn-body p` | heading yes, line no |
| /learn/psychology/book-notes/mans-search | H2 x1: A Question That Deserves an Hone | Como 24/600 #354149 | none | book-note.css `.bn-body h2` | - | heading yes, line no |
| /learn/psychology/book-notes/mans-search | H2 x1: Put this into practice | Como 24/600 #354149 | Mulish 16/400 lh28 #354149 no edge | book-note.css `.bn-body h2` | book-note.css `.bn-body > p:last-of-type` | heading yes, line no |
| /learn/psychology/book-notes/mans-search | H2 x1: Sources | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | book-note.css `.bn-body h2` | ? | heading yes, line no |
| /learn/psychology/book-notes/mans-search | H2 x1: Share this Book Note | Como 12/600 #b8460f | Mulish 16/400 lh25.6 #354149 no edge | knowledge-hub.css `.kh-aside .kh-aside__head--share, .kh-aside__s` | ? | heading no, line no |
| /learn/psychology/book-notes/mans-search | H2 x1: Ready to Further Your Learning? | Como 33/600 #354149 (390: Como 28/600 #354149) | Mulish 18/400 lh28.79 #5e6b75 no edge (390: Mulish 16/400 lh25.6 #5e6b75 no edge) | base.css `h2` | base.css `p` | heading no, line no |
| /learn/psychology/book-notes/mans-search | (2 item or card titles not listed) | | | | | |

### Quote page (single-quote.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /learn/motivation/quotes/why-you-dont-kn | H1 title x1: Why Didn’t I Know Better at the  | Como 33/700 #354149 (390: Como 28/700 #354149) | Mulish 21/400 lh33.59 #354149 no edge (390: Mulish 18/400 lh28.79 #354149 no edge) | base.css `h1` | base.css `p` | page title (not a block heading) |
| /learn/motivation/quotes/why-you-dont-kn | H2 x1: Table of Contents | Como 21/600 #354149 | Mulish 12/600 lh16.20 #b8460f no edge | knowledge-hub.css `:is(.kh-article__body, .bn-body) > .kh-aside .` | knowledge-hub.css `.kh-article__body p, .kh-article__body li` | heading no, line no |
| /learn/motivation/quotes/why-you-dont-kn | H2 x3: An Idea That’s Worthy of Your Co | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | knowledge-hub.css `.kh-article__body h2` | knowledge-hub.css `.kh-article__body p, .kh-article__body li` | heading yes, line no |
| /learn/motivation/quotes/why-you-dont-kn | H2 x1: A Question That Deserves an Hone | Como 24/600 #354149 | Mulish 16/400 lh28 #354149 no edge | knowledge-hub.css `.kh-article__body h2` | knowledge-hub.css `.kh-article__body > p:last-of-type` | heading yes, line no |
| /learn/motivation/quotes/why-you-dont-kn | H2 x1: Share this Quote | Como 12/600 #b8460f | Mulish 16/400 lh25.6 #354149 no edge | knowledge-hub.css `.kh-aside .kh-aside__head--share, .kh-aside__s` | ? | heading no, line no |
| /learn/motivation/quotes/why-you-dont-kn | H2 x1: Ready to Further Your Learning? | Como 33/600 #354149 (390: Como 28/600 #354149) | Mulish 18/400 lh28.79 #5e6b75 no edge (390: Mulish 16/400 lh25.6 #5e6b75 no edge) | base.css `h2` | base.css `p` | heading no, line no |
| /learn/motivation/quotes/why-you-dont-kn | (2 item or card titles not listed) | | | | | |

### Search results (search.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /?s=confidence | H1 title x1: Search Achology | Como 33/700 #354149 | Mulish 16/400 lh25.6 #2d3940 edge 1px #eeeded in0 | kh-subject.css `.mx-text .hx-title` | ? | page title (not a block heading) |
| /?s=confidence | H2 x1: A to Z | Como 24/600 #354149 (390: -) | Mulish 16/400 lh25.6 #354149 no edge (390: -) | kh-search.css `.ks-az-title` | ? | heading yes, line no |
| /?s=confidence | H3 x22: A | Como 18/700 #354149 (390: -) | Mulish 16/400 lh25.6 #354149 no edge (390: -) | base.css `h3` | ? | heading no, line no |

### Help hub (archive-faq_article.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /help/ | H2 x2: Thinking About Learning With Ach | Como 24/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | help.css `.help-page--landing .help-group__label` | ? | heading yes, line no |
| /help/ | H2 x1: Popular Articles | Como 24/600 #354149 | none | help.css `.help-close__heading` | - | heading yes, line no |

### Help category (taxonomy-faq_category.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /help/getting-started/ | H2 x1: All Articles in This Category | Como 24/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | help.css `.help-page--category .help-cat-section-title` | ? | heading yes, line no |
| /help/getting-started/ | H2 x1: Thinking About Learning With Ach | Como 24/600 #354149 | none | help.css `.help-close__heading` | - | heading yes, line no |
| /help/getting-started/ | H2 x1: Experience a FULL Achology membe | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | base.css `h2` | warm-room.css `p.warm-room__body` | heading yes, line no |

### Help answer (single-faq_article.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /help/comparisons-and-alternatives/will- | H2 x5: What has the profession itself s | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | help.css `.help-single__body h2` | help.css `.help-single__body p` | heading yes, line no |
| /help/comparisons-and-alternatives/will- | H2 x1: Other Related Questions | Como 24/600 #354149 | none | help.css `.help-close__heading` | - | heading yes, line no |
| /help/comparisons-and-alternatives/will- | H2 x1: Experience a FULL Achology membe | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | base.css `h2` | warm-room.css `p.warm-room__body` | heading yes, line no |

### Policies index (template-policies-index.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /policies/ | H2 x2: Our Legal Policies | Como 24/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | policies.css `.policy-body h2` | ? | heading yes, line no |
| /policies/ | H2 x1: More About Achology | Como 24/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | policies.css `.policy-body h2` | policies.css `.policy-body p` | heading yes, line no |

### Policy page (template-policy.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /policies/refund-policy/ | H2 x12: Our Approach to Refunds | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | policies.css `.policy-body h2` | policies.css `.policy-page--doc .policy-body > p:not(.founde` | heading yes, line no |
| /policies/refund-policy/ | H2 x2: This Refund Policy at a Glance | Como 24/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | policies.css `.policy-body h2` | ? | heading yes, line no |
| /policies/refund-policy/ | H2 x1: Other Policies | Como 24/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | policies.css `.policy-body h2` | ? | heading yes, line no |
| /policies/refund-policy/ | H2 x1: Questions about this policy? | Como 24/600 #354149 | Mulish 16/400 lh24.79 #5e6b75 no edge | policies.css `.policy-ask__title` | policies.css `.policy-ask__line` | heading yes, line no |
| /policies/how-we-write/ | H3 x5: A real question | Como 18/600 #354149 | Mulish 16/400 lh25.6 #5e6b75 no edge | policies.css `.policy-body .hw-steps h3` | policies.css `.policy-body .hw-steps p` | heading no, line no |

### About (page-about.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /about/ | H2 x2: Achology: What It Is, and Who It | Como 24/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | policies.css `.policy-body h2` | policies.css `.policy-body p` | heading yes, line no |
| /about/ | H3 x5: Why Does Achology Exist? | Como 0/600 #354149 | Mulish 16/400 lh25.6 #354149 edge 3px #ed6922 in24 (390: Mulish 16/400 lh25.6 #354149 no edge) | about.css `.policy-body h3.pfq-h` | ? | heading no, line no |
| /about/ | H2 x1: The Thinking that Drives Acholog | Como 24/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | policies.css `.policy-body h2` | policies.css `.policy-body p` | heading yes, line no |
| /about/ | H2 x1: The Achology Story | Como 24/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | policies.css `.policy-body h2` | policies.css `.policy-body p` | heading yes, line no |
| /about/ | H2 x1: The People Behind Achology | Como 24/600 #354149 | Mulish 16/400 lh26.4 #354149 no edge | policies.css `.policy-body h2` | about.css `.policy-body .founders__text p` | heading yes, line no |
| /about/ | H2 x1: Ten Different Ways to Experience [dark band] | Como 24/600 #ffffff | Mulish 16/400 lh24.79 #ffffff no edge | policies.css `.policy-body h2` | policies.css `.policy-body p` | heading yes, line no |
| /about/ | H2 x1: About Achology Related Questions | Como 24/600 #354149 | Mulish 14/400 lh22.4 #5e6b75 no edge | help.css `.help-popular__heading` | policies.css `.policy-body p` | heading yes, line no |

### Our People (template-our-people.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /about/instructors/ | H2 x3: Achology Management Team | Como 24/600 #354149 | Mulish 14/400 lh22.4 #5e6b75 no edge | people.css `.pp-group__label` | people.css `.pp-group__sub` | heading yes, line no |
| /about/instructors/ | H2 x1: Experience a FULL Achology membe | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | base.css `h2` | warm-room.css `p.warm-room__body` | heading yes, line no |

### Author profile (template-author-profile.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /about/instructors/kain-ramsay/ | H2 x1: Kain’s Writing and Articles | Como 12/600 #8a9199 | Mulish 16/400 lh25.6 #354149 no edge | people.css `.ap-works__label` | ? | heading no, line no |
| /about/instructors/kain-ramsay/ | H2 x1: Experience a FULL Achology membe | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | base.css `h2` | warm-room.css `p.warm-room__body` | heading yes, line no |

### Policy-family long page (manifesto, template-policy.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /about/manifesto/ | H2 x2: What the Manifesto Is and Why It | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | policies.css `.policy-body h2` | policies.css `.policy-page--founder .policy-body > p:not(.fo` | heading yes, line no |
| /about/manifesto/ | H2 x2: Experience the Learning Power of | Como 24/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | policies.css `.policy-body h2` | policies.css `.policy-body p` | heading yes, line no |
| /about/manifesto/ | H2 x1: Our Commitment to the Code of Et | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | policies.css `.policy-body h2` | policies.css `.policy-page--founder .policy-body > p:not(.fo` | heading yes, line no |

### Policy-family long page (code of ethics, template-policy.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /about/code-of-ethics/ | H2 x3: What the Framework Is and Why It | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | policies.css `.policy-body h2` | policies.css `.policy-page--founder .policy-body > p:not(.fo` | heading yes, line no |
| /about/code-of-ethics/ | H2 x1: The Principles That Shape the St | Como 24/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | policies.css `.policy-body h2` | ? | heading yes, line no |
| /about/code-of-ethics/ | H2 x1: An Ethical Framework for Applied | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | policies.css `.policy-body h2` | policies.css `.policy-page--founder .policy-body > p:not(.fo` | heading yes, line no |
| /about/code-of-ethics/ | H2 x1: More About Achology | Como 24/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | policies.css `.policy-body h2` | policies.css `.policy-body p` | heading yes, line no |

### Policy-family long page (founders letter, template-policy.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /about/founders-letter/ | H2 x4: Our Founders' Letter: Achology,  | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | policies.css `.policy-body h2` | policies.css `.policy-page--founder .policy-body > p:not(.fo` | heading yes, line no |
| /about/founders-letter/ | H2 x1: More About Achology | Como 24/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | policies.css `.policy-body h2` | policies.css `.policy-body p` | heading yes, line no |
| /about/founders-letter/ | H2 x1: Do you have questions about stud | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | policies.css `.policy-body h2` | warm-room.css `p.warm-room__body` | heading yes, line no |

### Reviews (page-reviews.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /reviews/ | H3 x1: A Global Learning Movement [dark band] | Como 24/600 #ffffff | Mulish 16/400 lh24 #ffffff no edge | global-impact.css `.gi__heading` | global-impact.css `.gi__lead` | heading yes, line no |
| /reviews/ | H2 x1: Ten Different Ways to Experience [dark band] | Como 24/600 #ffffff | Mulish 16/400 lh24.79 #ffffff no edge | policies.css `.policy-body h2` | policies.css `.policy-body p` | heading yes, line no |
| /reviews/ | H2 x1: FAQs About the Achology Learning | Como 24/600 #354149 | none | help.css `.help-close__heading` | - | heading yes, line no |

### Testimonials (page-testimonials.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /testimonials/ | H2 x1: Nine Achologists. Five Questions | Como 24/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | testimonials.css `.tm-heading` | testimonials.css `.tm-intro` | heading yes, line no |
| /testimonials/ | H3 x1: A Global Learning Movement [dark band] | Como 24/600 #ffffff | Mulish 16/400 lh24 #ffffff no edge | global-impact.css `.gi__heading` | global-impact.css `.gi__lead` | heading yes, line no |
| /testimonials/ | H2 x1: Five Aspects of the Achology Lea | Como 24/600 #354149 | Mulish 16/400 lh25.6 #5e6b75 no edge | testimonials.css `.tm-about-proof > h2` | testimonials.css `.tm-about-proof > p` | heading yes, line no |
| /testimonials/ | H2 x1: Ten Different Ways to Experience [dark band] | Como 24/600 #ffffff | Mulish 16/400 lh24.79 #ffffff no edge | policies.css `.policy-body h2` | policies.css `.policy-body p` | heading yes, line no |
| /testimonials/ | H2 x1: Related Questions | Como 24/600 #354149 | Mulish 14/400 lh22.4 #5e6b75 no edge | help.css `.help-popular__heading` | base.css `.kh-section__subtext, .help-popular__head .kh-` | heading yes, line no |
| /testimonials/ | H2 x1: Do you have questions about stud | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | base.css `h2` | warm-room.css `p.warm-room__body` | heading yes, line no |

### Certification (template-certification.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /certification/ | H1 title x1: Achology Certification | Como 33/700 #354149 (390: Como 28/700 #354149) | Mulish 18/500 lh27.9 #354149 no edge (390: Mulish 16/500 lh24.79 #354149 no edge) | certification.css `.pw-page .pw-hero__title` | certification.css `.pw-page .pw-hero__lead` | page title (not a block heading) |
| /certification/ | H2 x6: Two Certificates, and What Each  | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | policies.css `.policy-body h2` | certification.css `.pw-page .policy-body .pw-sub, .pw-page .polic` | heading yes, line no |
| /certification/ | H3 x1: Certificate of Course Completion | Como 21/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | certification.css `.pw-page .pw-card__title` | certification.css `.pw-page .policy-body .pw-card__body` | heading no, line no |
| /certification/ | H3 x1: Certificate of Achievement | Como 21/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | certification.css `.pw-page .pw-card__title` | certification.css `.pw-page .policy-body .pw-card__body` | heading no, line no |
| /certification/ | H3 x1: What It Is | Como 16/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | certification.css `.pw-page .pw-box__title` | ? | heading no, line no |
| /certification/ | H3 x1: What It Is Not | Como 16/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | certification.css `.pw-page .pw-box__title` | ? | heading no, line no |
| /certification/ | H3 x2: Learning for Yourself | Como 16/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | certification.css `.pw-page .pw-box__title` | certification.css `.pw-page .policy-body .pw-box__text` | heading no, line no |
| /certification/ | H2 x1: Experience a FULL Achology membe | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | base.css `h2` | warm-room.css `p.warm-room__body` | heading yes, line no |

### Accreditation (template-accreditation.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /accreditation/ | H2 x6: How the process works, step by s | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | policies.css `.policy-body h2` | certification.css `.pw-page .policy-body .pw-sub, .pw-page .polic` | heading yes, line no |
| /accreditation/ | H3 x3: Virtual Achologist Led Training  | Como 16/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | accreditation.css `.pw-page .acc-type__title` | accreditation.css `.pw-page .policy-body .acc-type__text` | heading no, line no |
| /accreditation/ | H3 x2: Code of Ethics | Como 16/600 #354149 | Mulish 16/400 lh25.6 #354149 no edge | certification.css `.pw-page .pw-box__title` | certification.css `.pw-page .policy-body .pw-box__text` | heading no, line no |
| /accreditation/ | H2 x1: Experience a FULL Achology membe | Como 24/600 #354149 | Mulish 18/400 lh31.5 #354149 no edge | base.css `h2` | warm-room.css `p.warm-room__body` | heading yes, line no |

### Pricing (page-pricing.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /pricing/ | H2 x1: On-Demand Courses | Como 12/600 #5e6b75 | Como 28/700 lh28 #5e6b75 no edge | pricing.css `.pl1-choice__name` | pricing.css `.pl1-choice__price` | heading no, line no |
| /pricing/ | H2 x1: Discounted Bundles | Como 12/600 #5e6b75 | Como 28/700 lh28 #354149 no edge | pricing.css `.pl1-choice__name` | pricing.css `.pl1-choice__price` | heading no, line no |
| /pricing/ | H2 x1: Access ALL Areas | Como 12/600 #5e6b75 | Como 28/700 lh28 #ed6922 no edge | pricing.css `.pl1-choice__name` | pricing.css `.pl1-choice__price` | heading no, line no |
| /pricing/ | H2 x1: Membership Plans | Como 12/600 #5e6b75 | Como 28/700 lh28 #b8460f no edge | pricing.css `.pl1-choice__name` | pricing.css `.pl1-choice__price` | heading no, line no |
| /pricing/ | H2 x1: Select the Achology Course that  | Como 24/600 #354149 | Mulish 16/400 lh25.6 #5e6b75 no edge | pricing.css `.pricing-section__title` | pricing.css `.pricing-section__line` | heading yes, line no |
| /pricing/ | H2 x1: Achology Schools: Best Value Cou | Como 24/600 #354149 | Mulish 16/400 lh25.6 #5e6b75 no edge | pricing.css `.pricing-section__title` | pricing.css `.pricing-section__line` | heading yes, line no |
| /pricing/ | H3 x1: The Access All Areas Pass [dark band] | Como 18/600 #ffffff | Mulish 12/400 lh19.20 #ffffff no edge | pricing.css `.pricing-bundle__name` | pricing.css `.pricing-bundle__meta` | heading no, line no |
| /pricing/ | H2 x1: The Achology Community: Subscrip | Como 24/600 #354149 | Mulish 16/400 lh25.6 #5e6b75 no edge | pricing.css `.pricing-section__title` | pricing.css `.pricing-section__line` | heading yes, line no |
| /pricing/ | H3 x2: Monthly membership | Como 18/600 #354149 | Como 24/700 lh38.40 #354149 no edge | pricing.css `.pricing-tier__name` | pricing.css `.pricing-tier__price` | heading no, line no |
| /pricing/ | H2 x1: Achology Pricing: Commonly Asked | Como 24/600 #354149 | none | help.css `.help-close__heading` | - | heading yes, line no |
| /pricing/ | (7 item or card titles not listed) | | | | | |

### Enquiries (enquiries.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /enquiries/ | H2 x1: Send Us an Enquiry | Como 24/600 #354149 | Mulish 16/400 lh25.6 #5e6b75 no edge | enquiries.css `.enq-dark h2.enq-h2` | enquiries.css `.enq-dark .enq-intro` | heading yes, line no |
| /enquiries/ | H2 x1: Quick Answers | Como 21/600 #354149 | Mulish 14/400 lh21 #5e6b75 no edge | enquiries.css `.enq-dark .enq-side h2` | enquiries.css `.enq-dark .enq-sub` | heading no, line no |
| /enquiries/ | H3 x1: What Happens Next [dark band] | Como 16/600 #ffffff | Mulish 14/400 lh22.4 #354149 no edge | enquiries.css `.enq-next h3` | enquiries.css `.enq-next dl` | heading no, line no |
| /enquiries/ | H2 x1: Frequently Asked Questions About | Como 24/600 #354149 | none | help.css `.help-close__heading` | - | heading yes, line no |

### 404 (404.php)

| page | block | heading, 1280 (390 if different) | supporting line, 1280 (390 if different) | heading class and stylesheet | line class and stylesheet | matches |
|---|---|---|---|---|---|---|
| /this-page-does-not-exist-audit/ | H2 x1: Where to instead? | Como 24/600 #354149 | Mulish 16/400 lh25.6 #5e6b75 no edge | components.css `.policy-next__title` | components.css `.policy-next__lead` | heading yes, line no |
| /this-page-does-not-exist-audit/ | H2 x1: Popular Questions | Como 24/600 #354149 | Mulish 14/400 lh22.4 #5e6b75 no edge | help.css `.help-popular__heading` | base.css `.kh-section__subtext, .help-popular__head .kh-` | heading yes, line no |
**OWED BACK:** the sweep brief for Kain to sign (Chat to Code, theme session). Nothing is owed from Chat to this audit.

*No em or en dashes in this file; checked before writing.*
