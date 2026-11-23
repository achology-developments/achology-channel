**DONE (Branch 2, Code, 23 November 2026, theme 0.708.445). Answers BRIEF__Join_Button_Words_Get_Your_First_Month_For_7_S482.**

**Result.** No join button on the build site now reads "Join Today for $7", "Get Started for $7" or "Start for $7". Each reads "Get Your First Month for $7". Read back from the live pages.

**What changed.**
- Header menu card (every page, the community card's button): was "Get Started for $7" (header.php).
- The pricing block's monthly button (Membership page, the Pass page, course and school pages): was "Join Today for $7" (pricing-block.php).
- Membership page's stored banner button, joining block button and buy bar button: was "Join Today for $7" (data/membership-page/main.json).
- Help answers' closing card and the Manifesto's card: was "Get FULL Access for $7" (help-parts.php, policies-content/manifesto.php). The Manifesto is not in the brief's list; it is the same card, so I matched it. Say if it should go back.
- Home page: the only $7 button on it is the header's menu card, changed above. Nothing else touched on Home.

**Left as is.** The footer band's button reads "Start Your Trial" (not one of the three wordings; the Membership page README says it keeps that). The eyebrow "Get Started for Only $7" on the monthly membership card is a label, not a button. Retired DSRD 8 card text untouched.

**Fit.** Checked at 1280 and 375. Every button is one line at both widths, no sideways scroll, except one: the header menu card's button wraps to two lines at 1280 (214 wide, 63 tall against 40). It is on every page and shows only in the open menu at desktop width. Not shrunk or changed, as the brief says. At 375 the card is not shown.

DOCUMENT TYPE: done.

*No em or en dashes in this file; checked before writing.*
