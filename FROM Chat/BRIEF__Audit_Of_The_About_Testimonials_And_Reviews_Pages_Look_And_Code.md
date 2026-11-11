> CODE DISPOSITION, S497: WAITS ON a theme session of its own running the audit of /about/, /testimonials/ and /reviews/ (a REPORT in TO Chat naming this brief); its head was read by the school page story session S497, which touches none of the three pages and leaves it for that session.

**For Code, a theme session. What this needs:** a full audit of three built pages, /about/, /testimonials/ and /reviews/, of how they look and how they are coded, written as one ranked task list per page; plus the invisible tidy-ups in files that belong only to these three pages. Chat, the Website Publishing Questions chat, 11 November 2026, on Kain's yes.

Done when: a REPORT in TO Chat holds, for each of the three pages, a "what a visitor sees" list and a "behind the scenes" list, every item with its evidence, and every invisible tidy-up you shipped is proved by before and after pictures that match at all three widths.

Model: Opus 5.5. Effort: xhigh.

This brief asks Kain nothing. Every question goes in your report for Chat's main session.

Card: "About, Testimonials and Reviews pages: full audit of look and code, the improvements, then the 14 new videos" on the Website Project Board. This brief is part 1 of that card.

# BRIEF: audit of the About, Testimonials and Reviews pages, look and code

## 1. Why

Kain wants every built page as neat, consistent and clean as it can be before launch, seen and unseen. These three pages were built earliest, before several standards settled, so they are the likeliest to have drifted. Kain judges anything he can see from the real page, so this job finds and proposes. It does not change anything a visitor can see.

## 2. Stay out of the way of the other sessions

Four other Code sessions are running: the course pages, the school page, the workbook page and the pricing page. Do not edit any file those pages use. If a fault sits in a shared stylesheet or a shared template, list it, name every page it touches, and leave it.

## 3. Part A: what a visitor sees

Read each page on the build site at 1440, 768 and 390 pixels wide. Check, against DSRD 7 (design foundations), DSRD 8 (components), DSRD 6 (the page gate) and the page's own signed spec in its Design folder:

1. Every font, weight, size and line height used, and whether each is a registered style in DSRD 7.
2. Every space between and inside blocks, and whether each is a DSRD 7 spacing step.
3. Alignment: left edges, centres, grids, gutters, and anything off by a few pixels.
4. Colours and contrast, with the measured contrast ratio for any text that may fall short.
5. Images: size, crop, sharpness, loading, and alt text.
6. Line breaks: no heading or paragraph whose last line is one, two or three words, at any of the three widths (Kain's standing rule).
7. Components that differ from their DSRD 8 version, and repeated blocks that differ between the three pages.
8. Anything that looks unfinished, uneven or out of place to an ordinary visitor.

## 4. Part B: behind the scenes

Read each page's served HTML, its stylesheets and its template, following the production-html-files and production-css-files skills:

1. HTML: heading order, landmarks, semantic elements, accessibility attributes, and structured data.
2. CSS: rules nothing uses, repeated rules, hard-coded values that should be DSRD 7 tokens, inline styles, over-specific selectors, and stray important flags.
3. Templates: leftover code, commented-out blocks, and anything still from the old site.
4. Weight: what each page loads (stylesheets, scripts, fonts, images) and anything loaded but not used.

## 5. What you may change

Only tidy-ups a visitor cannot see, and only in files used by these three pages alone (a page template, a page stylesheet). Before shipping each, take pictures of the page at all three widths. After shipping, take them again. They must match. If they do not, revert it and list it instead. Run the theme's usual gates and the production file tests, and deploy as normal. Change nothing in a shared file.

## 6. The report

One REPORT in TO Chat. For each page, two lists, A and B, most visible first. Each item says:

- what it is and where (the block, or the file and line);
- the evidence (a picture, a measurement, or the line of code);
- the fix you propose;
- its size: small, medium or large;
- whether it needs Kain's eye (anything visible does);
- whether it is shipped (Part B, page-only files) or waits.

End with the faults shared across pages, each with the list of pages it touches, so it can be fixed once later.

## 7. Vault notes for this job

None bear on copy, because no words are written or changed. The rules that govern are DSRD 6, 7 and 8, each page's signed spec, and the two production file skills.

*No em or en dashes in this file; checked before writing.*
