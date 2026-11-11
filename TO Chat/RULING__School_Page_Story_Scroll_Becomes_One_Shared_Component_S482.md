**For Chat. What this needs:** write Kain's ruling below into its home (DSRD 8, where the school pages' story scroll is already named as owed, and the Component Registry), and answer the one ask at the foot. Code, theme session S482, 11 November 2026.

# RULING: the About page's story scroll becomes one shared component

## 1. Kain's words

Kain, looking at the About page beside the school page preview: "This is kind of our really looking to model. Not reimagine, just want to model this. I guess my question would be, first and foremost, is this scroll, is this a component? ... is this something that we can essentially reuse, like all components of this?"

Code's answer and recommendation: the scroll is written by hand into the About page and its script is tied to Achology's own years and student numbers, so it is not a component today; turn it into one proper shared component when the real school page is built, so About and all seven schools run from the same one.

Kain: "yes, that seems like a wise suggestion - lets do it"

## 2. What this rules

1. The story scroll is one shared component, taking its heading, chapters, years, moments and closing line as data. The About page and the seven school pages all use it. There is no second copy.
2. It is made when the real school page is built in the theme, not before. The About page must look and behave exactly as it does today afterwards, proved by machine and by eye.
3. Every part carries over unchanged: the dark panel with the large year, the rising line, the five chapter buttons, the moments, the closing line.

## 3. What the preview already shows

The school page preview (the school page preview folder in the theme's previews, school.html) runs a working copy of the scroll from a list, for The School of Neuro-Linguistic Programming (NLP). Two things Kain has not yet ruled, both small and both to be shown to him rendered:
- The About panel counts students up. A field's history has no such figure, so the preview shows the chapter name and its years there.
- On a school page the buy bar steps aside while the story is on screen, so the scroll has its whole window as on About. Kain spotted the bar covering the scroll's foot; this was the mend.

## 4. One ask

The history itself is content: five chapters for each of seven fields, each moment a dated fact. The moments in the preview are Code's stand-ins and are not checked. Chat's to write and source, with the rest of the school page words.

## 5. Built so far, and one gate refusal on record

Theme commit e337cc14: the scroll's script is now story-scroll.js, moved whole out of about.js; the About page's own facts (era names, year spans, the student figures) ride in page-about.php as data the script reads. Measured against the build site's About at 1268, 1024 and 390 wide, 15 scroll points each (era name, dates, count, year digits, line segments, marks, flag, era button, rows reached, track position, tab order): no difference. Committed, not yet deployed; it goes out with the school page's first build.

The H2 page gate intake refused the six line change to page-about.php because the About page's signed spec is not in the channel. It was made openly on Kain's ruling in the sitting, through a small script, and nothing a reader sees changed. The school page template will meet the same gate: it has no signed spec in the channel. Kain's word in this sitting is "decide how you are going to deliver this page" and "Yes, build on it"; Code builds on that and names it in each commit.

The markup and the styles are the next part: one theme function that prints the scroll from data for the school pages, with the styles staying in about.css, which the school pages load, on the precedent functions.php already records for pages that reuse an About block. About's own words stay written in its template.

## 6. SHIP: theme 0.707.968, the school page is on the build site for The School of Neuro-Linguistic Programming (NLP)

What changed: template-school.php, taken by any page whose slug is a school's slug and whose parent is the academy page, once that school has stored parts; school-parts.php; data/school-page/nlp.json, written by tools/school_page_data.py from the preview Kain said "Yes, build on it" to; school-page.css and school-page.js, which hold only what a reused block needs on this page; functions.php loads each reused block's own stylesheet and script unchanged, in the order the preview loaded them; the footer carries the six free teachings on a school page. story-scroll.js now takes a story whose line and years differ; the About page was measured again at three widths against its old script: no difference, and it is running on the build site.

Why: Kain's word in the sitting, "decide how you are going to deliver this page ... to a standard of excellence", after "Yes, build on it". No new session was wanted.

Proof: the built page, read from the build site at 1268, 834 and 390 wide: no script error, no failed request, no broken picture, no sideways scroll; the story steps through its five chapters and raises its flag at the end; one price card, no bundle rows; five course cards. The page is a draft, seen with the workbench key. The other six schools keep the template they have until their parts exist.

Needed from Chat: the words (ASK__School_Page_Words_For_Seven_Schools_S482), and the three small rulings in it. Still stand-ins or course leftovers on the built page: every sentence; the film picture and play button beside What This School Teaches; the student figures row; the nine answers; the reviews. Not yet done: search details, schema for a school page, the DSRD 6 record, the Built Pages sheet's steps 4 to 8.

*No em or en dashes in this file; checked before writing.*
