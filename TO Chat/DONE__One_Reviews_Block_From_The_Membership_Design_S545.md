**DONE: SWEEP__One_Reviews_Block_From_The_Membership_Design_S542, with WORDS__Reviews_Block_Headings_Lines_And_Control_S542. Needs from Chat: the course 005 ruling (TO Chat ASK__Course_005_Reviews_Block_S545), then the DSRD 8 entry and build sheet the brief's section 9 names. Nothing needs Kain.**

# DONE: one reviews block on every page (Code, S545, 21 and 22 November 2026, theme 0.708.350)

## What is on the build site

- **The one block** on the seven schools, the Access All Areas Pass, 27 course pages and /membership/: the head and figures each page had, rows of one video beside two reviews, the button "Show More Reviews and Videos" (2 rows shown on the schools, the Pass and the courses), then the two link cards **Read All Student Reviews** and **View All Member Testimonials** (Kain's titles, every page; Student Reviews first on school, course and Pass pages, Member Testimonials first on Membership). Membership shows its one row, no button.
- **Kain's answers, all in TO Chat RULING__One_Reviews_Block_Signed_And_The_Two_Card_Titles_S542:** two rows on the courses and the Pass ("Yes, two rows"); no quote under the school, course and Pass videos ("yes"); the button's words ("Yes, use that"); "video first" ("Yes, video first") and then, on the built NLP page, overturned: the videos step across the rows again ("Yes, put it back"): row 1 video, review, review; row 2 review, video, review; row 3 review, review, video. Then "Yes, it's right" on NLP at 0.708.350.
- **The course line** is Chat's new one on all 27: "Reviews from students who have taken this course, along with videos of members sharing what they've gained." One row at 1280; its last row holds four or more words at 768 and 390.
- **Course 005** (Mindset Mastery) keeps its old wall: one review on its page, three in the review bank, one chosen. ASK__Course_005_Reviews_Block_S545 is open.

## Where it lives (one home)

- Markup: `tools/reviews_block.py`, `block()` and `place()`. The school, course and Pass data tools and Membership's `build.py` all draw through it, so no tool can put the old wall back. **A Code call, Chat may overturn:** no PHP function `achology_reviews_block()` was built. Nothing draws the block at runtime; every page stores it as markup written by the tools, so a PHP copy would be a second home that could drift from the first.
- Look: the `rvb` rules in `course-page.css` (Membership's memb-wall, -vid, -rv, -who and -way rules, moved and renamed). `memb.css` and `membership.css` keep none of them. Registered in the component styles gate (`rvb-rows`, pass on Membership, the Pass and a course page).
- Behaviour: `course-page.js` holds the rows past the count from 768 up, shows the button (drawn hidden, so without the script every row shows and no button), opens every held row on one press, removes the button, moves focus to the first opened card, and fits the opened cards again. The phone's two swipe rows gather every video and every review from inside the rows, held ones too.
- **Two Code calls inside the signed look, Kain may overturn:** on a phone the link cards' icon disc steps aside, because Kain's longer titles broke onto two lines beside it (0.708.348); the cards stack on a tablet, as the signed CBP look showed.

## The catch (section 6 step 5)

Searched the theme (runtime files and tools) and the 36 data files for `pf-foot--two`, `class="pf-go"`, "Watch Student Testimonials", the old course line, `.pfp-wall>:nth-child(`, and memb-wall, memb-way and memb-vid in memb.css and membership.css. Every hit left is course 005 and the rules held for it:

```
HIT pf-foot--two                 course-page.css x3   (the marked block held for 005)
HIT pf-foot--two                 data/course-page/005.json x1
HIT pf-go                        data/course-page/005.json x2
HIT Watch Student Testimonials   data/course-page/005.json x1
HIT old course line              data/course-page/005.json x1
HIT Read All Student Reviews as a text link data/course-page/005.json x1
memb-wall, memb-way, memb-vid in memb.css and membership.css: none
.pfp-wall>:nth-child( : none
```

## What step 6 deleted, and what it held

- **Deleted:** the phone ordering rules `.pfp-wall>:nth-child(7), :nth-child(8) {display:none}` and the four `order` rules for children 4, 5, 6 and 9 (course-page.css); `two_ways_on()` and `REVIEWS_FOOT` (tools/course_page_data.py); the `pf-foot--two` rules written by `tools/course_page_flatten.py`'s THEME_CSS_FOOT; Membership block 6's rules and its six tablet and phone lines (memb.css, carried to membership.css).
- **Held, not deleted, for course 005 alone:** `.pfp-wall`, `.pf-foot`, `.pf-go` (with its hover and focus), `.pf-foot--two` and the old wall's two width steps, moved unchanged into one marked block in course-page.css. They go the day 005 moves.

## Section 7, the checks

1 and 9, **the DSRD 6 gate**, page_gate.py at 0.708.350 on every page moved, plus 005 and Membership. No fail is in the reviews block. The fails it reads belong elsewhere: the questions block's heading at 21 on a phone (supporting-line, every course page, the questions sweep's block, shipped at 0.708.298 before this sweep); pictures not yet loaded when read (image-dimensions, the instrument's wait, being mended by the Membership session at S547); curriculum acronyms (VAGOK, ABC, SMOLER, SMART, IQ) and words the reviews always carried (reviewer initials RA and SP, "Senior Achologist II" on Toni-Lee Hazlett's film), each on the page before this sweep; a file answering 5xx once on three pages; course 017's art not lazy; Membership's ten, its own session's open groups. Six pages that first read wrongly (three drew without their styles, two read as a redirect, CBP a gutter) were run again and are given as they ran the second time.

| Page | Gate | Fails, by row | Reviews block fails |
|---|---|---|---|
| cognitive-behavioural-psychology | 43 passed, 1 failed | image-dimensions (pictures not yet loaded when read) | none |
| life-coaching | 44 passed, 0 failed | none | none |
| mental-health | 44 passed, 0 failed | none | none |
| mindfulness | 44 passed, 0 failed | none | none |
| neuro-linguistic-programming | 44 passed, 0 failed | none | none |
| person-centred-counselling | 44 passed, 0 failed | none | none |
| personal-growth | 43 passed, 1 failed | image-dimensions (pictures not yet loaded when read) | none |
| access-all-areas | 43 passed, 0 failed | none | none |
| membership | 41 passed, 10 failed | acronyms (a curriculum acronym or a reviewer initial); assets-load (a file answered 5xx once); breadcrumb-below (see printout); chain-register (see printout); icon-registry (see printout); image-dimensions (pictures not yet loaded when read); rank-math (see printout); supporting-line (the questions block heading on a phone) | none |
| authentic-confidence | 37 passed, 2 failed | acronyms (a curriculum acronym or a reviewer initial); supporting-line (the questions block heading on a phone) | IN THE BLOCK |
| beginners-guide-nlp | 37 passed, 2 failed | acronyms (a curriculum acronym or a reviewer initial); supporting-line (the questions block heading on a phone) | IN THE BLOCK |
| cbt-mental-health | 37 passed, 1 failed | supporting-line (the questions block heading on a phone) | none |
| cbt-practitioner | 37 passed, 1 failed | supporting-line (the questions block heading on a phone) | none |
| cbt-toolkit | 37 passed, 2 failed | acronyms (a curriculum acronym or a reviewer initial); supporting-line (the questions block heading on a phone) | IN THE BLOCK |
| clarity-purpose-effectiveness | 37 passed, 2 failed | acronyms (a curriculum acronym or a reviewer initial); supporting-line (the questions block heading on a phone) | IN THE BLOCK |
| communication-social-intelligence | 36 passed, 2 failed | image-dimensions (pictures not yet loaded when read); supporting-line (the questions block heading on a phone) | none |
| counselling-skills-practitioner | 37 passed, 1 failed | supporting-line (the questions block heading on a phone) | none |
| diploma-modern-applied-psychology | 37 passed, 1 failed | supporting-line (the questions block heading on a phone) | none |
| emotional-iq-social-skills | 36 passed, 2 failed | image-dimensions (pictures not yet loaded when read); supporting-line (the questions block heading on a phone) | none |
| entrepreneurship-business | 36 passed, 2 failed | image-dimensions (pictures not yet loaded when read); supporting-line (the questions block heading on a phone) | none |
| goal-setting-action-planning | 36 passed, 3 failed | acronyms (a curriculum acronym or a reviewer initial); image-dimensions (pictures not yet loaded when read); supporting-line (the questions block heading on a phone) | IN THE BLOCK |
| healthy-marriage-relationships | 37 passed, 2 failed | image-dimensions (pictures not yet loaded when read); supporting-line (the questions block heading on a phone) | none |
| hyper-focus-productivity | 36 passed, 2 failed | image-dimensions (pictures not yet loaded when read); supporting-line (the questions block heading on a phone) | none |
| hypnotherapy-practitioner | 37 passed, 2 failed | acronyms (a curriculum acronym or a reviewer initial); supporting-line (the questions block heading on a phone) | IN THE BLOCK |
| life-coaching-blueprint | 36 passed, 2 failed | image-dimensions (pictures not yet loaded when read); supporting-line (the questions block heading on a phone) | none |
| life-coaching-certificate | 36 passed, 2 failed | image-dimensions (pictures not yet loaded when read); supporting-line (the questions block heading on a phone) | none |
| mental-health-practitioner-diploma | 36 passed, 2 failed | assets-load (a file answered 5xx once); supporting-line (the questions block heading on a phone) | none |
| mental-toughness-resilience | 36 passed, 2 failed | image-dimensions (pictures not yet loaded when read); supporting-line (the questions block heading on a phone) | none |
| mindfulness-leadership | 35 passed, 6 failed | assets-load (a file answered 5xx once); image-dimensions (pictures not yet loaded when read); image-lazy-below-fold (course art not lazy); supporting-line (the questions block heading on a phone) | none |
| mindfulness-mental-health | 37 passed, 1 failed | supporting-line (the questions block heading on a phone) | none |
| mindfulness-practitioner-diploma | 37 passed, 1 failed | supporting-line (the questions block heading on a phone) | none |
| mindset-mastery-self-discovery | 37 passed, 1 failed | supporting-line (the questions block heading on a phone) | none |
| nlp-master-practitioner | 37 passed, 1 failed | supporting-line (the questions block heading on a phone) | none |
| nlp-practitioner | 37 passed, 1 failed | supporting-line (the questions block heading on a phone) | none |
| self-belief-emotional-intelligence | 36 passed, 6 failed | acronyms (a curriculum acronym or a reviewer initial); image-dimensions (pictures not yet loaded when read); supporting-line (the questions block heading on a phone) | IN THE BLOCK |
| skilled-helper | 37 passed, 1 failed | supporting-line (the questions block heading on a phone) | none |
| skilled-helper-practitioner | 37 passed, 2 failed | assets-load (a file answered 5xx once); supporting-line (the questions block heading on a phone) | none |

2, **the register.** The control is the button family's standard: 600 14 Como, 41 tall, 12 by 24, the same as the banner, buy block and bar buttons (the 46 secondary in the course cards is that panel's own size). Measured on CBP at 1280: heading to line 16, line to figures 24, figures to rows 32, row to row 24, rows to button 32, button to cards 32, as Membership's 24 and 32.

3, **widths.** 1280: two rows shown, three across, the videos stepping, the cards in a row even (403 on CBP, 341 on course 001). 768: each video 704 wide over its own two reviews at 340. 390: the two swipe rows hold every video (3) and every review (6), no button, nothing scrolls sideways. Checked on CBP, NLP, the Pass and course 001; Membership at 1280 one row of three at 352, no button.

4, **the button.** Mouse and keyboard: every held row opens (3 of 3), the button leaves, focus lands on the first opened card (the video on row 1's first card, the first review's turn on a stepped row 3), no review cut (0), Next review turns an opened card.

5, **without the script:** the button is drawn `hidden` and the rows are held by the script alone, so every row shows and no button is drawn.

6, **the two cards** open /reviews/ and /testimonials/, each with a 200; hover lifts 3 with the hover shadow, the focus ring is 2 orange at 2, and on a phone they stack.

7, **each page's own videos and reviews, in today's pairs** (checked against the stored pages before the move; nothing outside each block changed):

| Page | Each video with its two reviews, rows 1 to 3 |
|---|---|
| cbp | Stacey Anderson with William D. and Ollie S.; Peter Welch with Betty D. and Kylei R.; Andy Nelson with Dhiksha S. and Margaret L. |
| lc | Brian Boyle with Melissa O. and Colleen N.; Bea Fernández García with Sharena R. and Stuart R.; Peter Welch with Rajiv B. and Kylei R. |
| mh | Sarah Furnell with Martina B. and Angelo E.; Peter Welch with Kylei R. and Dhiksha S.; Stacey Anderson with Jacqueline R. and Marcie M. |
| miw | Brian Boyle with Tracy C. and Albert C.; Jon Frost with Martina B. and Rajiv B.; Alec Wells with Kylei R. and Purdey S. |
| nlp | Jon Frost with Akshay A. and Daniela A.; Brian Boyle with Ahliel S. and Kylei R.; Bea Fernández García with Tanita R. and Marcie M. |
| pc | Andy Nelson with Melissa O. and Amy P.; Jon Frost with Myriam T. and Gladys G.; Derek Seller with Sadagopa R. and Kylei R. |
| pgd | Alec Wells with Laurie P. and Laszlo F.; Bea Fernández García with Miah L. and Daniel M.; Derek Seller with Myriam T. and Mark L. |
| Pass | Jon Frost with Akshay A. and Daniela A.; Stacey Anderson with Ahliel S. and Ollie S.; Brian Boyle with Kylei R. and Marcie M. |
| 001 | Lee Ashby with Kylei R. and Luis T.; Nuala McCann with Jahaziel M. and Hope W.; Toni-Lee Hazlett with Prince H. and Daniel G. |
| 002 | Lee Ashby with Daniela A. and Ellen V.; Nuala McCann with Tanita R. and Stephen D.; Toni-Lee Hazlett with Barbara L. and Courtney U. |
| 003 | Lee Ashby with Akshay A. and Walt B.; Nuala McCann with Anna O. and Deepa S.; Toni-Lee Hazlett with Robin W. and Juwon O. |
| 004 | Lee Ashby with Mari L. and Ahliel S.; Nuala McCann with Robert B. and Muzaffar S.; Toni-Lee Hazlett with Sandor P. and Manuel C. |
| 005 | Lee Ashby, Marcie M.; Nuala McCann; Toni-Lee Hazlett |
| 006 | Lee Ashby with Ollie S. and Margaret L.; Nuala McCann with Iran T. and Graham N.; Toni-Lee Hazlett with Marilyn P. and Vivienne P. |
| 007 | Lee Ashby with William D. and Plamena I.; Nuala McCann with Sheikh O. and Darren K.; Toni-Lee Hazlett with Khanyisa L. and Shea P. |
| 008 | Lee Ashby with Dhiksha S. and Eileen L.; Nuala McCann with Denise S. and Alicia W.; Toni-Lee Hazlett with Tracey W. and Lisa W. |
| 009 | Lee Ashby with Stuart R. and Kayla S.; Nuala McCann with Asi E. and Michael E.; Toni-Lee Hazlett with Dave H. and Janisse N. |
| 010 | Lee Ashby with Sharena R. and Maria S.; Nuala McCann with Peryal T. and Patricia C.; Toni-Lee Hazlett with John B. and Kurt M. |
| 011 | Lee Ashby with Melissa O. and Julia G.; Nuala McCann with Linda H. and Eva I.; Toni-Lee Hazlett with Wentzel C. and Edward K. |
| 012 | Lee Ashby with Colleen N. and Elisabeth K.; Nuala McCann with Daniel G. and Maria S.; Toni-Lee Hazlett with Ruth B. and Leslie S. |
| 013 | Lee Ashby with Amy P. and Michelle A.; Nuala McCann with Hunter K. and Christina B.; Toni-Lee Hazlett with Linda P. and Raphaella H. |
| 014 | Lee Ashby with Gladys G. and Sadagopa R.; Nuala McCann with M S. and Chris M.; Toni-Lee Hazlett with Julia G. and Mtendere K. |
| 015 | Lee Ashby with Tracy C. and Albert C.; Nuala McCann with Jennifer E. and Helen D.; Toni-Lee Hazlett with Jeanette F. and Chelsea W. |
| 016 | Lee Ashby with Martina B. and Madelynan D.; Nuala McCann with Firoza M. and Marisa K.; Toni-Lee Hazlett with Tahera A. and Barbara G. |
| 017 | Lee Ashby with Purdey S. and Giedre L.; Nuala McCann with Clement B. and Harlan B.; Toni-Lee Hazlett with Chris W. and Zach O. |
| 018 | Lee Ashby with Angelo E. and Jacqueline R.; Nuala McCann with Sian B. and Reshma K.; Toni-Lee Hazlett with Asha G. and Sharon G. |
| 019 | Lee Ashby with Laszlo F. and Ekta P.; Nuala McCann with Gabor S. and Akash T.; Toni-Lee Hazlett with Hakeem A. and Paulo K. |
| 020 | Lee Ashby with Laurie P. and Lillian N.; Nuala McCann with Murtaza C. and Carolynn B.; Toni-Lee Hazlett with Jan H. and SP C. |
| 021 | Lee Ashby with Daniel M. and Andy H.; Nuala McCann with Catarina S. and Erick C.; Toni-Lee Hazlett with Marin B. and Kathrin B. |
| 022 | Lee Ashby with Rajiv B. and Simran K.; Nuala McCann with Kathy P. and Danielle B.; Toni-Lee Hazlett with Joanne C. and RA V. |
| 023 | Lee Ashby with Betty D. and Omar R.; Nuala McCann with Lina M. and Sheyla M.; Toni-Lee Hazlett with Binbin D. and Tim B. |
| 024 | Lee Ashby with Myriam T. and Charles T.; Nuala McCann with Sriram N. and Agnese G.; Toni-Lee Hazlett with Sara B. and Danilo P. |
| 025 | Lee Ashby with Miah L. and Radhika K.; Nuala McCann with Shobande M. and Kim N.; Toni-Lee Hazlett with Kiana P. and Arnold E. |
| 026 | Lee Ashby with Mark L. and Firoza M.; Nuala McCann with Greg C. and Eunisse J.; Toni-Lee Hazlett with Paulo O. and Bipin S. |
| 027 | Lee Ashby with Sandor P. and Irina S.; Nuala McCann with Tetiana K. and Brianna N.; Toni-Lee Hazlett with Jean-maurice A. and David V. |
| 028 | Lee Ashby with Scott D. and Elijah T.; Nuala McCann with Scott M. and Tessa M.; Toni-Lee Hazlett with Cesar M. and José M. |

8, **the supporting lines.** School and Pass lines unchanged. The course line: one row at 1280; at 768 two rows, last row "sharing what they've gained." (four words); at 390 three rows, last row "members sharing what they've gained." (five). No line to report.

## Records

The reviews line is written pass, with this run's numbers, in the School Page, Course Page and Access All Areas Page records (S545 sections at each record's foot). Membership's record is its own session's.

## Owed back to Chat (section 9 is Chat's)

- The course 005 ruling.
- The DSRD 8 entry for the block, section 14 pointed to it, DSRD 9's course reviews entry pointed to it, and the build sheet in Component Design Prototypes.

*No em or en dashes in this file; checked before writing.*
