**Needs from Chat: nothing to build; one words question waits on Kain, and one record line.**

# SHIP: the school pages' courses block is the Light Card, on 0.708.228 (S530 side session, 18 November 2026)

**What changed.** On all seven school pages, the block The Courses in This School no longer stands on the dark stage (Kain's pick 32, S528). The chosen course is now a white card with the site's card shadow, beside the list of courses. Each course is one row of two lines: its name on the left, its price over its hours on the right. The rows share the card's height, so the list and the card end level. The enrolment note is one slim band across the whole block underneath, on the banner's warm cream. On a tablet and a phone the same white card opens under the chosen course's name.

**Why.** Kain, with a picture of the Life Coaching block: "the background of this is kind of grey, so it kind of contradicts the card at the top, and also just the size of it ... this block lets down the entire page." He saw four lighter designs in the Change Viewer (round-cdeep), chose the Wide Card, then said: "I do prefer the light card. I like that structure."

**Whole pictures.** Each course picture is shown whole at its own shape, 640 by 336, never cropped. Kain: "why are you cropping the image ... Why on earth would you not just want to use the full image". The dark stage had cut about a third from the sides of the picture on Life Coaching.

**The title.** On all seven schools it now reads "The Five Courses Included Within This School" (Six on Life Coaching, Twelve on Personal Growth). Kain gave these words himself: "it needs to read the 5, 6, 12 courses included within this school". They are written by tools/school_page_data.py.

**Depth.** At 1280 the block went from 933 to 826 on Life Coaching, and from 1,549 to 980 on Personal Growth.

**Waiting.** The supporting line under the title is unchanged. Kain said he wants one generic line for all seven schools and "maybe in fact I'll come up with a solution for that". The chat-school-subtitles session holds that work.

**For the record.** The DSRD 6 gate's accepted-findings list in page_gate.py still names the old headings ("The Five Courses in This School" and its sisters) for its supporting-line rows. They will read as new findings on the next gate run and want renaming to the new title. That file is not in this session's scope.

**In passing.** Running tools/school_page_data.py rewrites data/school-page/knowledge-tree.json with straight apostrophes and a key moved. The committed file has curly ones. I put the file back as committed and shipped nothing from it. Its words source may want the curly marks.

**Signed.** Kain, on the built block in Safari, 18 November 2026: "Yes, it's right".

**Then, on 0.708.229 (commit b82c194f).** Kain, comparing the five, six and twelve course schools: "apply the same spacing rules as what you've applied to the school pages that have 6 ... it just looks a little bit crammed". He also said the floating card "should just sit and stop scrolling in parallel with the bottom of the 12th course", not over the enrolment band. Personal Growth's rows went from 64 to 104 (Life Coaching's are 102). The card is now held inside the list's own column, so it comes to rest level with the twelfth course. The block is 1,460 deep at 1280.

Theme commit 897027ae, pushed. Deployed and proved: local, server and zip agree on 0.708.228. Measured in WebKit on all seven schools at 1280, 834 and 390: new title, white card, whole picture, no sideways scroll.
