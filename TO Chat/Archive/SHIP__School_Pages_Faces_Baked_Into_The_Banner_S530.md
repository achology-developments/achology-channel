> Disposition, Chat S480, 23 Nov 2026: record; archived. No board card moved.

**Needs from Chat: nothing to act on. For the record: Kain's final look for the faces on the school pages' story banner, which replaces the one shipped at 0.708.274.**

# SHIP: the school banner's faces baked into the cream, on 0.708.281 (S530 side session, 20 November 2026)

**What changed.** At 0.708.274 the faces stood along the banner's edges at half strength (SHIP__School_Pages_Faces_On_The_Story_Banner_S530). Kain then ruled two things, which now govern. First, no face behind any words: "there needs to be more kind of cream behind all the text ... the images are fighting for attention with the actual text". Second, after a round that shaped cream around each word: "This is patchy ... it just needs to be kind of like a ... rounded corner ... these images were just meant to be baked into the cream ... not replacing it". Three rounds were rendered (round-fclear.js, round-fhug.js, round-fbake.js); he chose Soft of the last: "Yes, build 2".

**What a reader sees.** The banner's cream is one smooth ground. The faces lie inside it, grey, at a fifth of their strength, within one soft rounded curve from each top corner, gone before the chapter label, title, year and the five stages. Measured on six schools, every chapter: at 1280 and up the words start 263 in and the stages 148 down; from 1024 to 1279 the curve is smaller, as the words start 175 in. Below 1024 there are no faces and the banner keeps its faint marks. NLP is unchanged everywhere (no wall).

**How.** school-page.css, the block "THE FACES ON THE STORY'S BANNER", rewritten: the wall's mask is two radial curves at the top corners; the faces' strength is .2. The markup and tools/school_faces.py are unchanged. Deploy CURRENT at 0.708.281, commit a5fef4f6, pushed; the three preview rounds are committed (df3ab091, 5ca50482, 36dbd2f9).

**The Academy page.** At Kain's request the Academy page final tests session is building the same faces into the Academy history banner on the same classes, with an 'academy' list in tools/school_faces.py. It has the rules above and the version.

**For DSRD 7 or DSRD 8, if you keep such a rule:** on a banner that carries words, a background picture is baked into the ground at low strength and kept wholly clear of every word inside a soft rounded shape; it never sits behind text and never patches the ground around words. Kain's words above are its source.

**Touched after the build, on Kain's words, and signed.** At 0.708.283 every face a tenth stronger (.22), and the top row's third face from each edge lifted ("more prominent"); at 0.708.284 a softer, rounded lift over the fourth top face ("a softer ... merge ... So we can see a bit more of the face") and a rounded lift at each bottom corner, each measured clear of the title (62 down, 263 in) and the stage names (100 in, 182 down); at 0.708.285 the full look from 1200, where the banner already stands at its full width (Kain's Safari is 1253 wide and was showing the smaller curve), and the Academy's curve shortened for its higher stage names. **Signed** by Kain on the built CBP page at 0.708.285, 20 November 2026: "Yes, it's right".

*No em or en dashes in this file; checked before writing.*
