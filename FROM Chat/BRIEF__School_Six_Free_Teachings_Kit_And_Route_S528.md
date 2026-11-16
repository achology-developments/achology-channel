> CODE DISPOSITION, S528: WAITS ON the next school page sitting, which builds it whole (item 4 of Kain's list). Read in full at S528. Found on reading the theme, and sent to Chat by message the same sitting: no school form code exists yet; the course route's own lesson page (`free-lessons/{n}/`) was never built either, so there is no page to copy and the teaching page's look has no signed frame; the lesson films play only from achology.com, so a teaching page cannot be proved to play on the build site; and 36 lesson stills are to be made. The block on the six pages still shows the S521 six until that sitting.

Needs: Code wires each settled school page's free block to Kit sequence 2974053 and builds the route `/academy/{school}/free-teachings/{n}/`, for six schools. Mindfulness follows when its five new workbooks are signed.
Model: Opus 5.5. Effort: high.
This brief asks Kain nothing. Any question goes to Chat through the channel.
Done when a test sign up on each of the six school pages enters sequence 2974053 with its fields filled and both tags on, email 1 arrives, its picture opens teaching 1 on the new route, and its button opens that day's workbook file with no sign in.

Read first: the Shared Road (17 Packs), RULING__The_Six_Signed_Free_Teachings_And_Their_Lectures_S521, and BRIEF__Course_Page_Free_Six_Lessons_Form_And_Lesson_Pages_Through_Kit_S460. That last brief is the course route this one copies.

## Kit, built by Chat on 16 November 2026

**Sequence:** 2974053, Website School Six Free Teachings.
- Sender manager@achology.com, template 5295433, signed Karen Ramsay.
- Nine emails, all unpublished drafts. Chat publishes them after the test send.
- Delays: 0 hours, then 1, 1, 1, 1, 1, 1, 7 and 30 days.
- Do not use course sequence 2965491 for schools.

**Form:** none. There is no school form in Kit. Subscribe through the Kit API exactly as the course route does: create or update the subscriber, set the fields, add the two tags, then add them to sequence 2974053.

**Tags:** add both on each sign up, the shared one and the school's.

| Tag | Id |
|---|---|
| Website School Free Teachings | 25962820 |
| Website School Free Teachings: nlp | 25962821 |
| Website School Free Teachings: cbp | 25962822 |
| Website School Free Teachings: mental-health | 25962823 |
| Website School Free Teachings: life-coaching | 25962824 |
| Website School Free Teachings: person-centred | 25962825 |
| Website School Free Teachings: personal-growth | 25962826 |
| Website School Free Teachings: mindfulness | 25962827 (not used until its six are signed) |

**Fields:** the keys are what the emails read.

| Key | What it holds |
|---|---|
| school_name | The school's full signed title, as below, without "The" at the start. Each email writes "the {{ school_name }}" itself. |
| school_link | The school page's address on the build site. |
| free_teachings_link | `/academy/{school}/free-teachings/` with a trailing slash. Each email adds `{n}/` after it. |
| teaching_1_name to teaching_6_name | The lesson's own name, exactly as in the course data and Karen's master, not the workbook name (Kain, S528). |
| teaching_1_still to teaching_6_still | A still of that lesson, made the same way as the course route's lesson stills. |
| teaching_1_workbook to teaching_6_workbook | The direct address of that workbook's file, opened with no sign in. |

**The two links each teaching email carries:**
1. **The picture** goes to `{{ subscriber.free_teachings_link }}{n}/`, the new route, which plays that day's lesson.
2. **The Open Your Workbook button** goes to `{{ subscriber.teaching_{n}_workbook }}`.

Email 7's button goes to `school_link`, and so does email 8's. Email 9's goes to https://community.achology.com/checkout/community-subscription, the signed $7 first month.

## The six per school

The order is the day it arrives. Each row gives lesson key, lesson name, workbook slug and minutes. Each workbook is the one written from that very lesson, which leads its record (checked S528). The 36 workbooks are all different, all run 15 to 20 minutes, none is half of a pair, and each comes from a course on that school's page.

**nlp**, The School of Neuro-Linguistic Programming (NLP)
1. 003-140 | NLP Strategies: A Natural Process for Learning | the-nlp-learning-strategy-workbook | 19
2. 005-018 | Mindset: Understanding Your Frame of Reference | frame-of-reference-in-communication-workbook | 17
3. 005-028 | Four Alternative Ways to Approach Life's Challenges | four-ways-to-solve-problems-workbook | 17
4. 005-033 | Social Effectiveness: The Four Stages of Communication | four-stages-of-communication-workbook | 18
5. 005-034 | Mental Discipline: The NLP Dissociation Technique | the-nlp-dissociation-technique-workbook | 19
6. 004-050 | How to 'Neuro-Logically' Reprogramme Limited Thinking | reprogramming-limited-thinking-with-nlp-workbook | 15

**cbp**, The School of Cognitive Behavioural Psychology (CBP)
1. 006-015 | Your Locus: Circle of Concern Vs. Circle of Control | coveys-circle-of-control-workbook | 17
2. 006-026 | Battlefield of the Mind (The Mind Vs. The Brain) | your-two-inner-voices-workbook | 17
3. 006-022 | The Foundations of Cognition (where ideas come from) | where-beliefs-come-from-workbook | 16
4. 006-019 | Labels: A Basis for Accurate Self-Definition | labels-and-identity-workbook | 18
5. 007-015 | A Guide to Understanding Destructive Behaviours | understanding-destructive-behaviour-workbook | 15
6. 007-055 | Understanding the Natural Order of Your Emotions | the-natural-order-of-emotions-workbook | 17

**mental-health**, The School of Mental Health, Wellness and Emotional Resilience
1. 005-017 | Mindset: Understanding the Wise Part of Your Mind | finding-your-wise-mind-workbook | 16
2. 005-007 | Differentiating Fixed + Growth Orientated Thinking Styles | fixed-and-growth-thinking-styles-workbook | 17
3. 005-009 | A Guide to Developing Neuro-Linguistic Flexibility | flexible-thinking-habits-and-strategies-workbook | 19
4. 005-026 | Ask Yourself: 10 'Creative' Solution-Focussed Questions | ericksons-creative-solution-questions-workbook | 15
5. 018-066 | A Guide to Progression & Becoming Elevated in Thought | changing-your-perception-of-events-workbook | 16
6. 001-098 | The Human Experiential Model (Full Cognitive Model) | thoughts-feelings-behaviour-workbook | 18

**life-coaching**, The School of Life Coaching and Professional Helping
1. 009-095 | The Key to Coaching Influence: Communication Style | dialogue-discourse-diatribe-and-debate-workbook | 20
2. 009-104 | The Types of Open Questions (that Evoke Dialogue) | the-art-of-open-questions-workbook | 17
3. 001-046 | Sigmund Freud's Iceberg Model of Human Consciousness | freuds-iceberg-and-your-unconscious-workbook | 15
4. 010-106 | The UFFE ELBAEK Model (for Self-Reflection) | the-uffe-elbaek-self-reflection-model-workbook | 20
5. 001-054 | The Johari Window: A Model of Personal Insight | johari-window-workbook | 20
6. 010-121 | The 'When Everything Else Fails' (4 Projects) Project | four-projects-for-finding-direction-workbook | 17

**person-centred**, The School of Person-Centred Counselling and Psychology
1. 013-005 | Understanding Perception: The 5 Ways We All Perceive | five-ways-we-perceive-the-world-workbook | 20
2. 014-009 | Judgement: The Dimensions of Personal Prejudice | the-dimensions-of-personal-prejudice-workbook | 20
3. 014-072 | Psychoanalysis: Transactional Analysis and the 3 Ego States | eric-bernes-transactional-analysis-workbook | 19
4. 001-049 | Psychoanalytic Theory: Freud's Id, Ego, and Superego | id-ego-superego-workbook | 16
5. 014-088 | The Thought Investigation Model (Adapted from CBT) | investigating-your-unhelpful-thoughts-workbook | 18
6. 014-131 | The Five Fundamental Levels of Listening | the-fundamental-levels-of-listening-workbook | 18

**personal-growth**, The School of Personal Growth and Development (PGD)
1. 021-017 | A Guide to Understanding the Emotional Experience | where-your-emotions-come-from-workbook | 20
2. 001-132 | Human Motivation: Abraham Maslow's Hierarchy of Needs | maslows-hierarchy-of-needs-workbook | 20
3. 025-025 | The Six Principles for Perpetual Personal Proficiency | six-principles-of-personal-productivity-workbook | 15
4. 026-024 | Counter-Cultural Attitudes Towards Self-Improvement | the-elephant-and-the-rope-workbook | 17
5. 001-162 | Understanding Society: The Scale of Social Conformity | why-we-conform-and-obey-workbook | 18
6. 001-118 | Introduction to the Humanistic School of Thought | humanistic-psychology-and-human-potential-workbook | 17

**mindfulness:** day 1 is 015-018, Introducing the Four Noble Truths of Dukkha (the-buddhas-four-noble-truths-workbook, 19 minutes). The other five wait on Kain's names for the five new workbooks. Keep this page's free block as built until a later BRIEF lands.

## After the build

Send Chat one DONE line giving the test result per school. Chat then sends the test email, reads it in the test inbox and publishes the nine emails.

From Chat, S528. No em or en dashes; checked before writing.
