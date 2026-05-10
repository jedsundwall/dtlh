# Entity structure

**Status:** PROPOSED
**Last updated:** 2026-05-09
**Decision records:** [260509 — Form the Trust as a Washington nonprofit corporation](../decisions/260509-form-wa-nonprofit-trust.md)

## Summary

We are sketching a two-entity structure: a **Washington nonprofit corporation** ("the Trust") that holds long-term governance and the mission lock, and a **Washington limited liability company** ("the LLC") that owns the real estate and issues investment interests. The Trust is the sole manager of the LLC. Loyal Heights residents become members of the Trust and elect its board. Investors hold economic interests in the LLC. Only resident members vote on matters reserved to the Trust.

This is a working hypothesis. Counsel will pressure-test the specifics, and several open questions are listed at the bottom.

## The two entities

### Downtown Loyal Heights Trust, Inc. *(working name)*

A Washington nonprofit corporation under [RCW 24.03A](https://app.leg.wa.gov/RCW/default.aspx?cite=24.03A). Filing fee ~$30 online. As of 2026-05-09: not yet filed. Expected within 7–10 business days of that date.

What the Trust does:

- Holds the manager interest in the LLC.
- Defines membership eligibility — Loyal Heights residents, with boundary specified in bylaws.
- Members elect the Trust's board of directors (5–7 seats).
- Reserves "major decisions" (sale of the asset, change of mission, dissolution) so they require Trust + member approval, regardless of LLC cap-table economics.
- Public face of the project. Holds the bank account. Receives tax-deductible donations once 501(c)(3) is recognized; receives them via a fiscal sponsor in the interim.

What the Trust does **not** do:

- Sell securities.
- Hold investor capital intended for the LLC's offerings.
- Distribute profits to members. Membership is a governance role, not a financial one.

The Trust will pursue 501(c)(3) recognition via Form 1023 within 27 months of formation (deadline for retroactive recognition). 501(c)(4) is a fallback if civic-engagement / lobbying activity becomes important enough to need it; that decision is deferred.

### Downtown Loyal Heights Holdings, LLC *(working name)*

A Washington limited liability company under [RCW 25.15](https://app.leg.wa.gov/RCW/default.aspx?cite=25.15). To be formed only when securities counsel signals readiness — likely 30–60 days after the Trust, contingent on a real deal pipeline and papered offering terms.

Manager-managed. Sole manager: the Trust. Three classes of economic interests:

| Class | Holders | Rights | Sold under |
|-------|---------|--------|------------|
| **A — Anchor** | Accredited investors (Phase 1) | Preferred return + observer rights on the LLC's manager-board; no member-level voting | Reg D 506(c) |
| **N — Neighbor** | Anyone, residency-agnostic (Phase 2) | Economic only — distributions and appreciation, no governance | Reg CF, Reg A+, or WA intrastate |
| **V — Voting** | Loyal Heights residents only, paired one-to-one with Trust membership | Voting on LLC matters not reserved to the Trust | Small-dollar instrument under WA intrastate or cooperative-style exemption |

This delivers the homepage's "anyone can invest, only residents vote" promise: economic returns are open; governance is local.

## Why this structure

### Why two entities, not one

A nonprofit holding $50M of debt-financed investment real estate generates Unrelated Business Income Tax (UBIT) under [IRC §514](https://www.law.cornell.edu/uscode/text/26/514), complicates 501(c)(3) compliance via private-benefit and excess-business-holdings concerns, and makes anchor tax treatment messy. The cleanest separation is a governance shell (the Trust) on top of a taxable entity (the LLC) that holds the asset.

Precedents: NYC Real Estate Investment Cooperative (a New York not-for-profit corporation with per-property special-purpose-entity LLCs) and East Portland Community Investment Trust (a sponsoring 501(c)(3) plus a property-holding C-corp) both use this separation. Our model is closest to NYC REIC's.

### Why a nonprofit corporation, not a perpetual purpose trust

Kensington Corridor Trust in Philadelphia uses a perpetual purpose trust + 501(c)(3) hybrid. Elegant, but Pennsylvania has explicit PPT-enabling statutes; Washington does not. Few Seattle lawyers have drafted PPTs, and the project doesn't need extra legal novelty in its plumbing. A standard nonprofit corporation is well-trodden, fast to file, and templates are widely available.

### Why nonprofit + LLC, not a Washington cooperative

Washington has cooperative association statutes ([RCW 23.86](https://app.leg.wa.gov/rcw/default.aspx?cite=23.86&full=true) and [RCW 23.100](https://app.leg.wa.gov/RCW/default.aspx?cite=23.100&full=true)) and a cooperative securities exemption ([RCW 21.20.320(15)](https://app.leg.wa.gov/RCW/default.aspx?cite=21.20.310) / [WAC 460-44A-200](https://www.law.cornell.edu/regulations/washington/WAC-460-44A-200)). The exemption covers non-transferable membership interests but is narrower than the California, Vermont, and Minnesota statutes that NEIC, VREC, and EB PREC took advantage of. California's purpose-built statute (AB 816, 2015) was drafted explicitly to enable community real estate cooperatives. Washington has no equivalent.

Nonprofit + LLC delivers the same governance outcome — resident control, mission lock, broad investor participation — with stronger securities footing.

### Why three classes of LLC interests

Adapted from NorthEast Investment Cooperative's share-class architecture (see [precedents/neic.md](../precedents/neic.md)): a voting class restricted to residents, plus non-voting classes for outside capital. Splitting governance and economic rights is what makes "anyone can invest, only residents vote" work cleanly under securities law — the voting tranche is sold separately, in small amounts, to verifiable residents only.

## Open questions

These are the things counsel and the founding board will need to settle. Each will get a decision record when resolved.

- **Exact legal name.** Washington restricts certain words ("Bank" hard, "Trust" softer). "Downtown Loyal Heights Trust, Inc." may be fine, but counsel should confirm before filing. Alternatives: *Loyal Heights Community Trust, Inc.*; *Downtown Loyal Heights, Inc.* with "DTLH Trust" as a public brand.
- **Member voting mechanics.** Should the Trust be member-managed (members elect the board directly) or board-managed with members getting a vote on a narrower set of decisions? Member-managed matches the homepage promise and is the working assumption.
- **Resident definition.** Most likely defined by a precise neighborhood boundary (using the Loyal Heights Community Association map or specific zip codes). To be drafted in bylaws.
- **501(c)(3) vs. 501(c)(4).** Likely (c)(3) with fiscal sponsorship in the interim. Defer until the lobbying / civic-engagement scope is clearer.
- **Anchor rights at the LLC board.** The homepage says any anchor wanting an LLC board seat will have one. Be careful that this doesn't create de facto veto power; major decisions should remain reserved to the Trust regardless of cap table.
- **REIT election.** At $50M scale with 100+ shareholders, electing private REIT status (as EPCIT did) may meaningfully simplify Phase 2 economics. Defer to tax counsel.
- **Construction-phase governance.** Senior construction lenders will demand covenants that effectively control major decisions during the build. Make sure those covenants bite at the LLC level only and don't leak up into the Trust.

## Precedents informing this

- [NorthEast Investment Cooperative](../precedents/neic.md) — share-class architecture for resident-only voting
- *(planned)* NYC Real Estate Investment Cooperative — two-entity structure (nonprofit corp + per-property LLCs)
- *(planned)* East Portland Community Investment Trust / Plaza 122 — Phase 1 / Phase 2 capital stack mechanics
- *(planned)* Kensington Corridor Trust — board composition, trust-enforcer concept
- *(planned)* East Bay Permanent Real Estate Cooperative — share classes and offering circular drafting
