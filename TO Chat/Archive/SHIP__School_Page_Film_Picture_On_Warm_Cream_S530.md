DISPOSITION (Chat, Session 478, 20 November 2026): for the record. Archived.

For Chat. What this needs: nothing to rule. The teaching film's picture now sits on warm cream, on all seven schools and all 28 courses.

From Code, the school page theme session (S530 side session), 18 November 2026. Theme 0.708.227.

# SHIP: the teaching film's picture sits on warm cream

**Kain's words:** "are you happy with the background image ... the grey background ... I know it kind of ties in with the dark block that we have further down the page". Code said no. The artwork is drawn on a clear ground, so the dark slate showed through it and turned the smoke and the orange muddy. It was also the only dark thing in the top half of the page. Kain saw four light panels in the Change Viewer (round-qbg.js in the school page preview folder; the proof passed with 11 measured and 0 failed): Warm Cream, White, School Tint and Soft Grey. He answered "Yes, build cream".

**What is built:**
- In course-page.css, .q-video now has var(--color-warm-cream) behind it, the banner's own cream, in place of --color-dark-footer.
- The slate wash over the picture (.q-video::after) is gone. It was there so a white play button would hold, and the play button is orange on every school and course (lib-v18).
- It is one shared rule, so all seven schools and all 28 courses changed together. Kain was told before he chose. css_gate passes.

**Proof:**
- The NLP school and The CBT Toolkit were read on the build site at 0.708.227.
- On both, the panel reads rgb(253, 250, 248) and there is no wash.
- The artwork's edges melt into the cream, and the play button holds.

**For the record:** DSRD 8 or the course page's build sheet may still name the dark panel for this component. If either does, it wants the cream written in.

*No em or en dashes in this file; checked before writing.*
