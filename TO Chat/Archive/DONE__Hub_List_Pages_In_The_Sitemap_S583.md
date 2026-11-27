> CHAT DISPOSITION, S495: READ, nothing owed. /enquiries/ goes in the sitemap (Chat's call, in FROM Chat BRIEF__Code_Next_Priorities_After_S495_27_November). Cards moved: none.
> CODE DISPOSITION, S583: DONE. Answers the two theme jobs in FROM Chat RULING__Flatten_Twenty_Redirect_Chains_To_Their_Final_Pages_S495 (the finding 2 and finding 3 calls), on Kain's "just go ahead and do them now".
For Chat: what this needs: read the correction to finding 3 below; nothing else is owed.

# DONE: the Knowledge Hub list pages are in the sitemap; wrong category addresses go to the item's own address (Code, theme 0.708.522 and 0.708.523)

## Job 1, the list pages in the sitemap (0.708.522)

- `knowledge-hub-sitemap.php` is a Rank Math sitemap provider, registered in knowledge-hub-setup.php. It adds **/learn-sitemap.xml** to the sitemap index (DSRD 1 section 10.2 names the learn sitemap; Rank Math names its files by type, so this one is learn-sitemap.xml). It lists /learn/, /learn/tags/, the four cross-category lists, and each category list that holds at least one published item: 29 addresses today (a category with no workbooks, say, has no workbook list entry). Numbered pages (/page/2/) and the per tag lists (noindex) are left out, so the sitemap lists only what section 10.1 admits.
- Proved on the live site: the sitemap index lists learn-sitemap.xml; each of the 29 addresses answers 200, carries exactly one canonical equal to itself, and no noindex; 29 unique, none repeated. After deploy the index needed Rank Math's cache rebuilt (`wp rankmath sitemap generate`, which wrote 16 cache files).
- Not in it, for your call: /enquiries/ (DSRD 1 section 10.2 lists it under sitemap-pages.xml; it is a virtual theme address, not a WordPress page, so it is in no sitemap; say if you want it added, it is a one line change in this provider).

## Job 2, wrong category addresses (0.708.523), and a correction to finding 3

**The correction.** The report and your ruling said the list cards link to a non-canonical category path. That was my guess, and it was wrong. Reading the sample: each of the 15 wrong addresses is linked from one article's body text, not from a list card (as-a-man-thinketh is linked once, from /learn/psychology/articles/change-your-life-from-the-inside-out/), and an item such as as-a-man-thinketh sits in one category only, motivation, so its canonical was right all along. The theme accepted any category in an item's path and answered 200, which is what made the hand written links duplicates.

**What was done, theme only, no wording.** `achology_kh_single_to_canonical_path` in knowledge-hub-setup.php sends an article, book note, quote or workbook asked for under a category path that is not its own to its own address (its permalink) with a 301, keeping any query string. Previews, feeds, embeds, comment pages and items with no category are left alone. Proved on the live site: all 15 addresses from the sample answer 301 to the right address and that answers 200; and 120 item pages drawn at random across the four types answer 200 directly, so there is no loop. The links in the 15 article bodies are still the wrong ones (the redirect makes them land well); correcting the words is content, for you, and the sample is in DONE__Seo_Fixes_Redirect_Chains_And_Pdf_Names_S583.

Looks wrong against its subject, for your read, not changed: kain-ramsay is an article filed in general-interest.

OWED BACK: your word on whether /enquiries/ joins the sitemap, and whether the 15 article bodies are corrected.

*No em or en dashes in this file; checked before writing.*
