**CHAT DISPOSITION, Session 467, 12 November 2026: ACTED ON.** Chat placed the 81 unmatched pieces (MAP__The_81_Unmatched_Pieces_Placed_S467.csv, School Page folder), showed Kain all seven schools' lists on one rendered page, and he said "yes". The fill is briefed in FROM Chat as BRIEF__Fill_The_81_Unmatched_Pieces_Schools_S467. The knowledge tree block itself stays with its own card.

**For Chat. What this says:** the schools field is on the build site and filled for 987 published pieces from your map; 81 published pieces are not in the map and are listed below for you to place. Code, factory session S516, 12 November 2026. It answers BRIEF__Knowledge_Tree_Fill_Each_Pieces_Schools_From_The_Map_S466. It asked Kain nothing.

DOCUMENT TYPE: DONE. Not a page spec.

# DONE: the schools field filled from the map

## 1. How the theme reads the field

- **Name:** `schools`, on posts of type `article`, `book_note`, `quote` (the quote articles) and `workbook`. Read with `get_post_meta( $id, 'schools', true )`, or `get_field( 'schools' )` once the theme is deployed.
- **Shape of the value:** a PHP array of school slugs, stored serialized in post meta, for example `["mental-health","mindfulness","personal-growth"]`. Sorted alphabetically. One to three slugs a piece.
- **The seven slugs, exactly as in the map and as in /academy/<slug>/:** `cognitive-behavioural-psychology`, `life-coaching`, `mental-health`, `mindfulness`, `neuro-linguistic-programming`, `person-centred-counselling`, `personal-growth`. Note these are the full slugs, not the short keys in SCHOOL_WORDS_SIGNED_S465.json (`cbp`, `nlp`, `person-centred`).
- **Owner-editable:** a checkbox field named Schools is added to all four ACF field groups (acf-json, theme main 24e55546, pushed). Each piece also carries the hidden `_schools` reference to its field key. The field definition reaches the build site's editing screen with the next theme deploy; the values are already in the database and work without it.
- **Nothing else was written on any piece.** No title, body, status, date or other meta changed. The only theme files touched are the four acf-json field groups.

## 2. Read back from the database (published pieces, per school and per kind)

| School | Articles | Book notes | Quote articles | Workbooks | Total |
|---|---|---|---|---|---|
| cognitive-behavioural-psychology | 72 | 31 | 51 | 38 | 192 |
| life-coaching | 64 | 22 | 74 | 1 | 161 |
| mental-health | 71 | 48 | 222 | 35 | 376 |
| mindfulness | 70 | 50 | 191 | 1 | 312 |
| neuro-linguistic-programming | 72 | 9 | 2 | 34 | 117 |
| person-centred-counselling | 68 | 25 | 72 | 8 | 173 |
| personal-growth | 83 | 95 | 303 | 8 | 489 |
| **Pieces carrying the field** | **324** | **150** | **427** | **86** | **987** |

The school rows add up to more than the piece counts because a piece may sit in up to three schools (500, 280, 915 and 125 memberships). All 987 values were compared one by one with the map: 0 mismatches.

Published on the build site by kind: 404 articles, 150 book notes, 428 quote articles, 86 workbooks (1,068). Filled: 987. Not filled: 81 (section 3).

## 3. Published pieces the map does not name (81: 80 articles, 1 quote article)

All 150 book notes and 86 workbooks matched. These 81 carry no `schools` field yet; Chat places them by hand. Slug, title and category as recorded on the site; the tags are the pieces' own.

| Kind | Slug | Title | Category and tags |
|---|---|---|---|
| article | a-c-grayling | Who Is A. C. Grayling? His Biography, Ideas and Life Works | kh_category: General Interest; kh_tag: Understand Your Mind; kh_tag: Find Purpose &amp; Direction; kh_tag: Unlock Personal Growth; kh_tag: Deep Dive |
| article | abraham-maslow | Who Is Abraham Maslow? His Biography, Ideas and Life Works | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Find Purpose &amp; Direction; kh_tag: Unlock Personal Growth; kh_tag: Deep Dive |
| article | alain-de-botton | Who Is Alain de Botton? His Biography, Ideas and Life Works | kh_category: Wisdom for Life; kh_tag: Understand Your Mind; kh_tag: Develop Emotional Intelligence; kh_tag: Find Purpose &amp; Direction; kh_tag: Build Mental Resilience |
| article | alan-watts | Who Is Alan Watts? His Biography, Ideas and Life Works | kh_category: Wisdom for Life; kh_tag: Build Confidence; kh_tag: Find Purpose &amp; Direction; kh_tag: Practice Mindfulness; kh_tag: Learn Mindfulness |
| article | alfred-adler | Who Is Alfred Adler? His Biography, Ideas and Life Works | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Improve Relationships; kh_tag: Grow Self-Awareness; kh_tag: Overcome Self-Doubt; kh_tag: Deep Dive |
| article | applied-psychology | Applied Psychology: What It Is and How It Works in Real Life | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Grow Self-Awareness; kh_tag: Unlock Personal Growth |
| article | aristotle | Who Is Aristotle? His Biography, Ideas and Life Works | kh_category: Wisdom for Life; kh_tag: Understand Your Mind; kh_tag: Build Confidence; kh_tag: Lead With Impact; kh_tag: Communicate Effectively |
| article | arthur-schopenhauer | Who Is Arthur Schopenhauer? His Biography, Ideas and Life Works | kh_category: Wisdom for Life; kh_tag: Find Purpose &amp; Direction; kh_tag: Build Mental Resilience; kh_tag: Master Your Mindset; kh_tag: Deep Dive |
| article | behavioural-psychology | Behavioural Psychology: How Behaviour Is Learned and Changed | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Master Your Mindset; kh_tag: Break Negative Thinking |
| article | bertrand-russell | Who Is Bertrand Russell? His Biography, Ideas and Life Works | kh_category: Wisdom for Life; kh_tag: Understand Your Mind; kh_tag: Find Purpose &amp; Direction; kh_tag: Deep Dive |
| article | brendon-burchard | Who Is Brendon Burchard? His Biography, Ideas and Life Works | kh_category: Motivation; kh_tag: Find Purpose &amp; Direction; kh_tag: Deep Dive |
| article | brene-brown | Who Is Brené Brown? Her Biography, Ideas and Life Works | kh_category: Helping People; kh_tag: Build Confidence; kh_tag: Improve Relationships; kh_tag: Help Others Grow; kh_tag: Unlock Personal Growth |
| article | cal-newport | Who Is Cal Newport? His Biography, Ideas and Life Works | kh_category: Motivation; kh_tag: Improve Relationships; kh_tag: Master Your Mindset; kh_tag: Deep Dive |
| article | carl-jung | Who Is Carl Jung? His Biography, Ideas and Life Works | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Grow Self-Awareness; kh_tag: Research-Based; kh_tag: Deep Dive |
| article | charles-duhigg | Who Is Charles Duhigg? His Biography, Ideas and Life Works | kh_category: Personal Growth; kh_tag: Find Purpose &amp; Direction; kh_tag: Deep Dive |
| article | cognitive-behavioural-therapy | CBT Explained: How Cognitive Behavioural Therapy Works | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Grow Self-Awareness; kh_tag: Master Your Mindset |
| article | cognitive-psychology | Cognitive Psychology: How We Think, Learn and Remember | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Master Your Mindset; kh_tag: Break Negative Thinking |
| article | communication-skills-and-language-patterns | Communication Skills and Language Patterns: A Working Guide | kh_category: Motivation; kh_tag: Improve Relationships; kh_tag: Communicate Effectively |
| article | dan-ariely | Who Is Dan Ariely? His Biography, Ideas and Life Works | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Grow Self-Awareness; kh_tag: Deep Dive |
| article | daniel-goleman | Who Is Daniel Goleman? His Biography, Ideas and Life Works | kh_category: Psychology; kh_tag: Develop Emotional Intelligence; kh_tag: Deep Dive |
| article | developmental-psychology | Developmental Psychology: How We Grow and Change Across Life | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Grow Self-Awareness; kh_tag: Navigate Life Changes |
| article | don-miguel-ruiz | Who Is Don Miguel Ruiz? His Biography, Ideas and Life Works | kh_category: Personal Growth; kh_tag: Understand Your Mind; kh_tag: Improve Relationships; kh_tag: Communicate Effectively; kh_tag: Grow Self-Awareness |
| article | emotional-intelligence-and-social-skills | Emotional Intelligence and Social Skills: How to Build Both | kh_category: Wisdom for Life; kh_tag: Develop Emotional Intelligence; kh_tag: Improve Social Confidence |
| article | entrepreneurship | Entrepreneurship: What It Really Takes to Build Something | kh_category: Personal Growth; kh_tag: Achieve Your Goals; kh_tag: Start &amp; Grow a Business |
| article | erich-fromm | Who Is Erich Fromm? His Biography, Ideas and Life Works | kh_category: Wisdom for Life; kh_tag: Understand Your Mind; kh_tag: Find Purpose &amp; Direction; kh_tag: Deep Dive |
| article | erik-erikson | Who Is Erik Erikson? His Biography, Ideas and Life Works | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Grow Self-Awareness; kh_tag: Navigate Life Changes; kh_tag: Deep Dive |
| article | friedrich-nietzsche | Who Is Friedrich Nietzsche? His Biography, Ideas and Life Works | kh_category: Wisdom for Life; kh_tag: Understand Your Mind; kh_tag: Find Purpose &amp; Direction; kh_tag: Grow Self-Awareness; kh_tag: Master Your Mindset; kh_tag: Deep Dive |
| article | gabor-mate | Who Is Gabor Maté? His Biography, Ideas and Life Works | kh_category: Helping People; kh_tag: Understand Your Mind; kh_tag: Deep Dive |
| article | gerard-egan | Who Is Gerard Egan? His Biography, Ideas and Life Works | kh_category: Helping People; kh_tag: Lead With Impact; kh_tag: Help Others Grow; kh_tag: Communicate Effectively; kh_tag: Deep Dive; kh_tag: Learn Counselling |
| article | goal-setting-and-action-planning | Goal Setting and Action Planning: How to Set Goals That Hold | kh_category: Helping People; kh_tag: Achieve Your Goals; kh_tag: Overcome Feeling Stuck |
| article | grow-self-awareness | How to Grow Self-Awareness | kh_category: Helping People; kh_tag: Grow Self-Awareness; kh_tag: Unlock Personal Growth |
| article | healthy-marriage | Healthy Marriage: What Makes One, and How Couples Keep It | kh_category: Personal Growth; kh_tag: Improve Relationships; kh_tag: Strengthen Your Partnership |
| article | howard-gardner | Who Is Howard Gardner? His Biography, Ideas and Life Works | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Help Others Grow; kh_tag: Deep Dive |
| article | human-nature-and-behaviour | Human Nature and Behaviour: Why People Do What They Do | kh_category: General Interest; kh_tag: Understand Your Mind; kh_tag: Overcome Feeling Stuck |
| article | humanistic-psychology | Humanistic Psychology: What It Is and Why It Still Matters | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Grow Self-Awareness; kh_tag: Unlock Personal Growth |
| article | hypnotherapy | Hypnotherapy: What It Is, How It Works and What It Cannot Do | kh_category: General Interest; kh_tag: Help Others Grow; kh_tag: Communicate Effectively; kh_tag: Grow Self-Awareness |
| article | irvin-yalom | Who Is Irvin Yalom? His Biography, Ideas and Life Works | kh_category: Psychology; kh_tag: Help Others Grow; kh_tag: Deep Dive; kh_tag: Learn Counselling |
| article | james-allen | Who Is James Allen? His Biography, Ideas and Life Works | kh_category: Personal Growth; kh_tag: Find Purpose &amp; Direction; kh_tag: Achieve Your Goals; kh_tag: Master Your Mindset; kh_tag: Learn Mindfulness |
| article | jean-piaget | Who Is Jean Piaget? His Biography, Ideas and Life Works | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Help Others Grow; kh_tag: Deep Dive |
| article | john-c-maxwell | Who Is John C. Maxwell? His Biography, Ideas and Life Works | kh_category: Personal Growth; kh_tag: Lead With Impact; kh_tag: Deep Dive |
| article | john-dewey | Who Is John Dewey? His Biography, Ideas and Life Works | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Deep Dive |
| article | john-stuart-mill | Who Is John Stuart Mill? His Biography, Ideas and Life Works | kh_category: Wisdom for Life; kh_tag: Understand Your Mind; kh_tag: Find Purpose &amp; Direction; kh_tag: Deep Dive |
| article | jonathan-haidt | Who Is Jonathan Haidt? His Biography, Ideas and Life Works | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Deep Dive |
| article | jordan-b-peterson | Who Is Jordan B. Peterson? His Biography, Ideas and Life Works | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Build Confidence; kh_tag: Find Purpose &amp; Direction; kh_tag: Deep Dive |
| article | joseph-campbell | Who Is Joseph Campbell? His Biography, Ideas and Life Works | kh_category: General Interest; kh_tag: Understand Your Mind; kh_tag: Break Negative Thinking; kh_tag: Deep Dive |
| article | judith-s-beck | Who Is Judith S. Beck? Her Biography, Ideas and Life Works | kh_category: Mental Wellness; kh_tag: Understand Your Mind; kh_tag: Help Others Grow; kh_tag: Break Negative Thinking; kh_tag: Deep Dive |
| article | kain-ramsay | Who Is Kain Ramsay? His Biography, Ideas and Life Works | kh_category: General Interest; kh_tag: Help Others Grow; kh_tag: Communicate Effectively; kh_tag: Unlock Personal Growth; kh_tag: Deep Dive; kh_tag: Learn Life Coaching |
| article | leadership-and-influence | Leadership and Influence: How Good Leaders Win Trust | kh_category: Mental Wellness; kh_tag: Lead With Impact; kh_tag: Help Others Grow |
| article | leo-tolstoy | Who Is Leo Tolstoy? His Biography, Ideas and Life Works | kh_category: Wisdom for Life; kh_tag: Find Purpose &amp; Direction; kh_tag: Deep Dive |
| article | life-coaching | Life Coaching: What It Is, How It Works and Who It Is For | kh_category: Helping People; kh_tag: Find Purpose &amp; Direction; kh_tag: Help Others Grow; kh_tag: Communicate Effectively |
| article | limiting-beliefs-and-mindset | Limiting Beliefs and Mindset: How Beliefs Shape Your Life | kh_category: Motivation; kh_tag: Master Your Mindset; kh_tag: Break Negative Thinking |
| article | malcolm-gladwell | Who Is Malcolm Gladwell? His Biography, Ideas and Life Works | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Achieve Your Goals; kh_tag: Communicate Effectively; kh_tag: Research-Based |
| article | mark-manson | Who Is Mark Manson? His Biography, Ideas and Life Works | kh_category: Mental Wellness; kh_tag: Build Confidence; kh_tag: Deep Dive |
| article | martin-seligman | Who Is Martin Seligman? His Biography, Ideas and Life Works | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Deep Dive |
| article | mental-wellbeing | Mental Wellbeing: What It Is and How to Look After Yours | kh_category: Mental Wellness; kh_tag: Support Mental Health; kh_tag: Manage Stress &amp; Anxiety |
| article | mindfulness | Mindfulness: What It Is, How It Works and How to Begin | kh_category: Wisdom for Life; kh_tag: Practice Mindfulness; kh_tag: Grow Self-Awareness |
| article | nassim-nicholas-taleb | Who Is Nassim Nicholas Taleb? His Biography, Ideas and Life Works | kh_category: General Interest; kh_tag: Understand Your Mind; kh_tag: Deep Dive |
| article | neuro-linguistic-programming | Neuro-Linguistic Programming: What NLP Is and How It Works | kh_category: Motivation; kh_tag: Master Your Mindset; kh_tag: Unlock Personal Growth; kh_tag: Overcome Feeling Stuck |
| article | person-centred-counselling | Person-Centred Counselling: What It Is and How It Helps | kh_category: General Interest; kh_tag: Improve Relationships; kh_tag: Help Others Grow; kh_tag: Support Mental Health |
| article | philip-zimbardo | Who Is Philip Zimbardo? His Biography, Ideas and Life Works | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Improve Social Confidence; kh_tag: Deep Dive |
| article | plato | Who Is Plato? His Biography, Ideas and Life Works | kh_category: Wisdom for Life; kh_tag: Build Confidence; kh_tag: Find Purpose &amp; Direction; kh_tag: Communicate Effectively; kh_tag: Unlock Personal Growth; kh_tag: Deep Dive |
| article | psychoanalysis | Psychoanalysis: What It Is and How It Works Today | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Grow Self-Awareness; kh_tag: Master Your Mindset |
| article | purpose-and-direction | Purpose and Direction: How to Choose and Build Yours | kh_category: Motivation; kh_tag: Find Purpose &amp; Direction; kh_tag: Navigate Life Changes |
| article | resilience-and-mental-toughness | Resilience and Mental Toughness: How They Are Built | kh_category: Personal Growth; kh_tag: Build Mental Resilience; kh_tag: Master Your Mindset |
| article | rick-hanson | Who Is Rick Hanson? His Biography, Ideas and Life Works | kh_category: Mental Wellness; kh_tag: Understand Your Mind; kh_tag: Build Mental Resilience; kh_tag: Manage Stress &amp; Anxiety; kh_tag: Deep Dive |
| article | robert-cialdini | Who Is Robert Cialdini? His Biography, Ideas and Life Works | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Lead With Impact; kh_tag: Communicate Effectively; kh_tag: Deep Dive |
| article | robert-greene | Who Is Robert Greene? His Biography, Ideas and Life Works | kh_category: Motivation; kh_tag: Find Purpose &amp; Direction; kh_tag: Master Your Mindset; kh_tag: Deep Dive |
| article | ryan-holiday | Who Is Ryan Holiday? His Biography, Ideas and Life Works | kh_category: Motivation; kh_tag: Find Purpose &amp; Direction; kh_tag: Build Mental Resilience; kh_tag: Practice Mindfulness; kh_tag: Deep Dive; kh_tag: Learn Mindfulness |
| article | self-confidence | Self-Confidence: What It Is and How You Build It | kh_category: Personal Growth; kh_tag: Build Confidence; kh_tag: Overcome Self-Doubt |
| article | self-discipline-and-mind-management | Self-Discipline and Mind Management: How to Govern Yourself | kh_category: Wisdom for Life; kh_tag: Increase Productivity; kh_tag: Build Self-Discipline |
| article | sigmund-freud | Who Is Sigmund Freud? His Biography, Ideas and Life Works | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Find Purpose &amp; Direction; kh_tag: Grow Self-Awareness; kh_tag: Research-Based; kh_tag: Deep Dive |
| article | simon-sinek | Who Is Simon Sinek? His Biography, Ideas and Life Works | kh_category: Motivation; kh_tag: Build Confidence; kh_tag: Find Purpose &amp; Direction; kh_tag: Lead With Impact; kh_tag: Deep Dive |
| article | skilled-helper | The Skilled Helper Model: Egan's Three Stages Explained | kh_category: Helping People; kh_tag: Improve Relationships; kh_tag: Help Others Grow; kh_tag: Communicate Effectively |
| article | social-psychology | Social Psychology: How Other People Shape What You Do | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Improve Relationships; kh_tag: Grow Self-Awareness |
| article | steven-pinker | Who Is Steven Pinker? His Biography, Ideas and Life Works | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Deep Dive |
| article | steven-pressfield | Who Is Steven Pressfield? His Biography, Ideas and Life Works | kh_category: Motivation; kh_tag: Build Confidence; kh_tag: Build Mental Resilience; kh_tag: Grow Self-Awareness; kh_tag: Unlock Personal Growth; kh_tag: Deep Dive |
| article | thich-nhat-hanh | Who Is Thich Nhat Hanh? His Biography, Ideas and Life Works | kh_category: General Interest; kh_tag: Practice Mindfulness; kh_tag: Manage Stress &amp; Anxiety; kh_tag: Deep Dive; kh_tag: Learn Mindfulness |
| article | values-and-decision-making | Values and Decision Making: How to Choose Well | kh_category: Personal Growth; kh_tag: Find Purpose &amp; Direction; kh_tag: Achieve Your Goals |
| article | viktor-frankl | Who Is Viktor Frankl? His Biography, Ideas and Life Works | kh_category: General Interest; kh_tag: Understand Your Mind; kh_tag: Find Purpose &amp; Direction; kh_tag: Help Others Grow; kh_tag: Deep Dive |
| article | william-james | Who Is William James? His Biography, Ideas and Life Works | kh_category: Psychology; kh_tag: Understand Your Mind; kh_tag: Find Purpose &amp; Direction; kh_tag: Grow Self-Awareness; kh_tag: Research-Based; kh_tag: Deep Dive |
| quote | why-once-a-mind-has-been-truly-expanded-it-never-goes-back | Why Once a Mind Has Been Truly Expanded It Never Goes Back | kh_category: Mental Wellness; kh_tag: Grow Self-Awareness; kh_tag: Master Your Mindset; kh_tag: Unlock Personal Growth; kh_tag: Beginner-Friendly |

## 4. The two skipped rows (step 6)

- `how-psychological-thinking-has-transformed-over-the-years`: no post of that slug exists on the build site in any status. Nothing written.
- `where-did-life-coaching-come-from`: no post of that slug exists on the build site in any status. Nothing written.

## 5. The other map rows not written (for your count)

The map holds 1,075 rows. 987 were written. The other 88 are:

- **2** the skipped rows above.
- **75 workbook rows** with no workbook post yet (the S465 workbook import has not landed them).
- **4 article rows with no post:** `is-mental-health-an-illness`, `is-mental-health-getting-worse`, `mental-health-and-mental-wellbeing`, `the-seven-levels-of-human-awareness`.
- **7 rows whose post is a draft, so not published and not written:** six articles (`how-does-mental-health-affect-sleep`, `how-to-improve-mental-wellbeing`, `is-mental-health-genetic`, `mental-health-without-therapy-or-medication`, `should-mental-health-be-taught-in-schools`, `why-mental-health-is-important-in-everyday-life`) and one quote article (`what-is-transference-in-psychology`).

The fill is one re-runnable script: say the word and the drafts and the later workbooks are filled once they are published.

## 6. Not done, by the brief

The knowledge tree block is not built and no theme page file was touched. Two other unpublished posts are outside the map (one draft quote article, one pending article with no slug) and were left alone.

*No em or en dashes in this file; checked before writing.*
