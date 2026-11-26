> Chat S493, 26 Nov 2026: WAITS ON Kain finishing the three steps with Code (key, Analytics Data API, GA4 Viewer); then Chat stores the key in the keychain as achology-gsc-reader and deletes the file.

Needs: Chat to take the key into its keychain once Kain has made it, then walk Kain through steps 2 and 3 if Code has not.
Done when: Chat reads Search Console and GA4 with its own key, and the key file is deleted from Downloads.

# Chat's own read-only Google key (S580, 26 November 2026, on Kain's "Yes, make it")

**Why Kain has to click.** No Google credential is on this iMac any more (the S307 key is gone from the Desktop, the Downloads folder and the keychain), so Code cannot make a key through the API, and Claude in Chrome was not connected. Chat and Code both sit on this iMac, so the key downloads straight to Chat's machine: **no AirDrop.**

**The account.** claude-code@achology.iam.gserviceaccount.com, project Achology. Already Restricted in Search Console, so nothing to do there. The key is a second key on that account.

**Scopes Chat asks for when it signs:** https://www.googleapis.com/auth/webmasters.readonly and https://www.googleapis.com/auth/analytics.readonly.

## Kain's three steps

1. **Make the key.** Open console.cloud.google.com/iam-admin/serviceaccounts?project=achology, click the claude-code row, open the Keys tab, press Add key, then Create new key, choose JSON, press Create. A file ending in .json lands in Downloads. Leave it there and say "done".
2. **Switch on the GA4 reader.** Open console.cloud.google.com/apis/library/analyticsdata.googleapis.com?project=achology and press Enable. (Without it, every GA4 read is refused even with the right access.)
3. **Let the account see GA4.** Open analytics.google.com, choose the achology.com property (G-HJ29S4Z0R8), press Admin (the cog, bottom left), then Property access management, then the blue plus, then Add users. Paste claude-code@achology.iam.gserviceaccount.com, untick "Notify new users by email", choose the role Viewer, press Add.

## Chat, after step 1

Find the file in Downloads by shape (type service_account, client_email ending iam.gserviceaccount.com), store it in the keychain as service achology-gsc-reader, delete the file, and never print it. Then test one Search Console call and one GA4 runReport call.

*No em or en dashes in this file; checked before writing.*
