For Chat. What this needs: nothing to rule. One note for the board: each school and course will want its own film one day.

From Code, the school page theme session (S530 side session), 18 November 2026. Theme 0.708.221 and 0.708.222.

# SHIP: the teaching picture plays the Achology Promotional Video, on schools and courses

**Kain's words:** the picture with a play mark in each page's teaching block "doesn't link anywhere". Until each school has its own film, "we could literally have that video there across all 7 school pages". Then, for the 28 course pages: "Yes, do the same".

**What is built:**
- On all seven schools (0.708.221) and all 28 courses (0.708.222), the teaching picture is now a real button. It plays the Achology Promotional Video, Vimeo 708764177, 2:15, the film above the footer on the live achology.com.
- It opens in the site's video lightbox, the same box and registered close control as the course page's student films. It closes by its X, Escape or a click outside, and focus returns to the picture.
- The picture is drawn exactly as before.
- Its spoken name is "Play the Achology promotional video, 2:15".
- The builders write it: tools/school_page_data.py and tools/course_page_data.py, step 8.

**Proof:** read on CBP and on The CBT Toolkit at 1280 and 390. The button is 440 by 248 at 1280, exactly as the picture was. One lightbox opens with the film. Escape closes it. css_gate passes.

**At launch:** the film's Vimeo embed list holds achology.com, so it plays there. Like every film, it does not play on the build site.

**For the board:** Kain spoke of a film of each school's own one day, perhaps made with a voice tool such as ElevenLabs. Nothing is built for that. It is a later card if he wants it.

*No em or en dashes in this file; checked before writing.*
