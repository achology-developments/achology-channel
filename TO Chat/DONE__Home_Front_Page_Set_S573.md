For Chat: what this needs: your word on the one row still failing that is not Code's (keyword-density, the empty post body), and on keywordInImageAlt if you want Home's pictures given alts.

Done when: keyword-density has its template-page carve-out for Home (or a ruling), and Home's record chapters are filled by their runners.

# DONE: Home set as the build site's front page (S573, 25 November 2026)

**Kain's words** (put to him by the main session, relayed): "Yes, set it", to "Shall I set your Home page as the site's front page on the build site?"

**Done, on achologytest.com only, over WP-CLI, two options and nothing else.** Read back from the install:
- `show_on_front`: **posts to page**
- `page_on_front`: **0 to 45038**

No other setting, no page and no Rank Math Homepage field was changed. To put it back: `show_on_front` posts, `page_on_front` 0. Cache purged by the gate's own purge before each run. `/` still answers with Home: the gate's route reached the same page, its address row passes, and the carved-out count is unchanged at 81, which depends on Home's own blocks, so it did not become another template. (The one check Code could not run is `wp eval`, which the publishing wall refuses.)

## The five rows, before and after (page_gate on https://achologytest.com/, theme 0.708.488)

| Row | Before | After |
|---|---|---|
| meta-title | read "Achology TEST Site \|" (20 chars) | **PASS** 59 chars: Achology: Understand Yourself, Then Help Others Do the Same |
| meta-description | FAIL 0 chars (missing) | **PASS** 150 chars: Achology is an online academy that teaches practical psychology. Learn at your own pace, apply each idea to your own life and help others do the same. |
| rank-math | FAIL score 67, under the bar of 90 | **PASS** score 97, at or over the 95 target, keyword `achology` |
| keyword-density | FAIL the body is empty | **FAIL** the body is empty, unchanged |
| dsrd6-record | FAIL 0 closed, 10 not run, 1 fail (chapter 3, the missing description) | found; the sweep rewrote chapter 3 from the passing rows, and the rest are human or Kain's rows, not run by design |

Gate totals: before this change 39 passed, 4 failed; after **41 passed, 2 failed**, 10 for review, 81 carved out. The two failures are keyword-density and dsrd6-record's open chapters.

## Rank Math, re-read (nothing saved; table row 45038 now `97 settled achology`, and in Home's record)

97. At 67 seven body tests failed; at 97 they pass. **The one failing test is keywordInImageAlt**, as Chat's answer foresaw: every picture in Home's stored blocks is decorative (alt empty). The score is over 95 so nothing is owed, but if you want it at 100 name the pictures that carry meaning and Chat writes their alts. No signed word was changed.

## What the analyser reads as the body

With Home as the front page the theme's feed fetches `/` and hands the analyser the words inside Home's `<main>` (the page's own blocks, not the empty post body). That is why the content tests flipped to passing. **keyword-density still fails** because the gate's row reads the stored post body, which is empty; the template-page carve-out the Courses, Accreditation and Policies pages take is not yet entered for Home. That carve-out is Chat's to extend; Code has not added it and has done nothing further.
