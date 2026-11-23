> Disposition, Chat S480, 23 Nov 2026: written into DSRD 9 section 47.5 (the registry question listed to Chat); archived. No board card moved.

**DOCUMENT TYPE:** Ship brief, not a page spec.
**Date:** 2026-11-23. **Session:** S553 (Branch A, theme). **Theme version:** 0.708.395, deployed to achologytest.com.

# SHIP: the checkout foot on the Pricing page, and the foot's one home

**What changed.**
1. On /pricing/, the Access All Areas Pass card and both membership plans (Monthly, Annual) now close on the course card's own checkout foot: the lock, Secure Checkout, the Stripe badge and the five card marks, seated exactly as the Membership join block's plans seat it (full card width, the card's own text margin, the logos at three quarters, the badge at 16). It is drawn from the same stored source the Membership block reads (the Pass page's own checkout data), so the three can never differ.
2. The foot's rules had lived inside course-page.css, which the Pricing page does not load (loading it whole moved other Pricing parts). So they now have one home, checkout-foot.css: 58 rules moved verbatim and in order, loaded just before course-page.css wherever that loads, and on its own on Pricing. Proved identical before and after on a course page, a school page, the Pass page, the Academy, Membership and the gift page, at 1440, 1024 and 375: no element moved, recoloured or resized.

**Seen and left as designed.** The Pass card now stands about 90 taller than the school card beside it. The grid aligns its cards to the top on purpose, because each card's "View the courses" opens on its own.

**Left alone, as asked.** The Annual card's "Two months free against twelve monthly payments." Branch B places Chat's new words.

**Files.** checkout-foot.css (new), course-page.css, functions.php, pricing-parts.php, pricing.css, style.css. Commit 0b3c5165.

**Needed from Chat.** If the Component Registry is to list the checkout foot, its home is now checkout-foot.css (Code does not edit the registry's design folder unasked).
