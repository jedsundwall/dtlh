# Speed-run formation memo

**Re:** Forming a credible legal entity for DTLH so anchor pledges can firm up
**Date:** 260509

> **Snapshot.** This memo captures the strategic thinking as of the date above. Topical drilldowns continue in the other [`current/`](.) documents and may be more up-to-date than what's here.

## 1. The bottom line

You don't need the final structure this week. You need an entity that exists, has a name, has a bank account, and has a Washington Secretary of State filing number, so the anchor who said "we'd need a clearer indication of a legal structure" has something to point at. That entity is a Washington nonprofit corporation called something like *Downtown Loyal Heights Trust*, formed under [RCW 24.03A](https://app.leg.wa.gov/RCW/default.aspx?cite=24.03A), filed with the Secretary of State for $30 (online), effective the day it's filed. You can have it within a week.

The Trust is the public face and the long-term governance shell. **It is not where investor capital flows.** Investor capital flows into a separate Washington LLC, formed when (and only when) you have a real deal and securities counsel has papered an offering. That LLC is controlled by the Trust. This two-entity pattern is what NYC REIC, EPCIT/Plaza 122, and Kensington Corridor Trust all use.

The single most important hire is **securities counsel**, separate from the probono corporate lawyer. The probono lawyer can incorporate the Trust this week. Securities counsel is a months-long relationship that designs Phase 1 (anchors) and Phase 2 (community equity) without painting you into a corner.

## 2. What "credibly receive pledges" means right now

Three different things sit under that phrase, and each unlocks a different urgency.

**Non-binding indications of interest.** This is what your $1.4M tracker is. Today it lives in your inbox and a spreadsheet. To "receive" them more credibly you need (a) an entity name to attach the pledge to, and (b) a one-page Indication of Interest form with the right disclaimers. You do *not* need the entity to be capable of holding investor money yet — the pledges aren't money. **This is the email you got.** The anchor wants to see structure, not wire money.

**Predevelopment donations.** Once securities counsel, an appraiser, and a real estate attorney engage, you'll burn through $50K–$150K before signing anything with the seller. That money is best raised as charitable contributions to the Trust — or to a fiscal sponsor while the Trust is waiting on 501(c)(3) recognition.

**Investor capital.** Don't take any until securities counsel has papered the offering. Doing this wrong is the single fastest way to turn a great story into an SEC enforcement action. Plan for this 60–90 days out, not now.

## 3. Recommended structure

Two entities. The Trust (a Washington nonprofit corporation under RCW 24.03A) holds long-term governance and the mission lock. The LLC (a Washington LLC under RCW 25.15) owns the real estate and issues investment interests. The Trust is the sole manager of the LLC. Loyal Heights residents become members of the Trust and elect its board. Investors hold economic interests in the LLC. Only resident members vote on matters reserved to the Trust.

The LLC has three classes of economic interests:

| Class | Holders | Rights |
|-------|---------|--------|
| **A — Anchor** | Accredited investors (Phase 1) | Preferred return + observer rights; no member-level voting |
| **N — Neighbor** | Anyone, residency-agnostic (Phase 2) | Economic only — distributions and appreciation |
| **V — Voting** | Loyal Heights residents only | Voting on LLC matters not reserved to the Trust; paired one-to-one with Trust membership |

Full rationale and open questions in [`02-entity-structure.md`](./02-entity-structure.md).

The short version of *why this and not something else*:

- **Two entities, not one.** A nonprofit holding $50M of debt-financed investment real estate runs into UBIT (under IRC §514), private benefit, and excess-business-holdings problems hard. Governance shell on top, taxable entity beneath, is clean.
- **Nonprofit corp, not perpetual purpose trust.** Pennsylvania has explicit PPT enabling statutes; Washington does not. Don't add experimental governance plumbing to an already-novel project.
- **Nonprofit + LLC, not a Washington cooperative.** Washington's cooperative securities exemption is narrower than the California, Vermont, and Minnesota statutes that NEIC, VREC, and EB PREC took advantage of. California's purpose-built AB 816 (2015) was drafted explicitly for community real estate cooperatives. Washington has no equivalent.

## 4. Precedents to draft from

The site already cites NEIC, NYC REIC, VREC, and EPCIT. Each gets a deeper drilldown in [`../precedents/`](../precedents/).

- **[NorthEast Investment Cooperative](../precedents/neic.md)** (Minneapolis, 2011) — closest precedent in spirit. Their Articles of Incorporation are public and define the resident-only voting class plus non-voting preferred classes for outside capital. That share-class architecture is directly portable to the LLC operating agreement.
- **[East Portland Community Investment Trust / Plaza 122](../precedents/epcit-plaza-122.md)** (Mercy Corps NW, 2017) — the canonical Phase 1 / Phase 2 capital stack: $220K from the sponsoring nonprofit + $230K subordinated debt from impact investors + $900K first-lien bank mortgage = $1.2M acquisition. Anchors slot directly into the sub-debt position, scaled up. A bank-issued letter of credit backstops investor downside in Phase 2.
- **[NYC Real Estate Investment Cooperative](../precedents/nyc-reic.md)** (2015) — closest *organizational* precedent. Pre-formation public survey produced $1.2M in non-binding pledges. Public launch event drew 350 attendees, 200 signed up that day. They incubated under fiscal sponsorship by Flux Factory for ~2.5 years while waiting for the NY AG's Real Estate Finance Bureau to approve them taking investment money.
- **[Kensington Corridor Trust](../precedents/kensington-corridor-trust.md)** (Philadelphia, 2019) — closest *governance* precedent. Two tethered entities (perpetual purpose trust + 501(c)(3)). Their 9-seat Trust Stewardship Committee composition formula is directly copyable: 2 residents, 2 small-business owners, 2 community leaders, 2 youth (16–21), 1 nonprofit-board crossover.
- **[East Bay Permanent Real Estate Cooperative](../precedents/ebprec.md)** (Oakland, 2017) — their SEC Form 1-A filing is the most complete public US filing for a community real estate cooperative. Effectively a free template for offering-circular disclosures, share-class definitions, and lock-up provisions.
- **[Vermont Real Estate Cooperative](../precedents/vrec.md)** (2020) — bylaws are public. Single-state membership = intrastate exemption = no SEC filing for the membership/voting layer.
- **Sustainable Economies Law Center.** They publish [free templates](https://www.theselc.org/templates), a [Legal Structures for Radical Real Estate primer](https://www.theselc.org/legal_structures_for_radical_real_estate), and the [Radical Real Estate Law School library](https://www.theselc.org/radical_real_estate_law_school_resources). Closest thing to a national clinic for this work.

## 5. Securities path

Where the work gets technical, and where you need a securities lawyer separate from a corporate one.

### Phase 1 — anchor investors (~5 × ~$1M, accredited only)

The right exemption is **Reg D Rule 506(c)**, not 506(b). Why: 506(b) prohibits general solicitation, but you've already general-solicited via dtlh.org, the My Ballard article, and the flyers/yard signs. You can't put the toothpaste back in the tube. 506(c) explicitly allows general solicitation, requires 100% accredited purchasers, and requires "reasonable steps to verify" accreditation. A March 2025 SEC no-action letter clarified that issuers can satisfy verification by setting a high minimum investment ($200K+ for individuals counts as a reasonable step). At $1M anchor commitments you sail past that. File Form D within 15 days of the first sale, plus a Washington DFI notice filing.

### Phase 2 — community equity ($10K and up)

Three real options, decide later:

- **Reg CF (federal crowdfunding).** Caps at $5M / 12 months. Lighter disclosure than Reg A+. Must run through a registered funding portal. Probably the right answer for the first community round.
- **Reg A+ Tier 1.** Up to $20M. State-by-state coordination, but no SEC review of the offering circular. Heavier disclosure (audited financials usually). EBPREC's filing is the template. **Reg A+ Tier 2** goes up to $75M and is the right vehicle if Phase 2 gets large.
- **Washington intrastate crowdfunding** ([RCW 21.20.880](https://app.leg.wa.gov/rcw/default.aspx?cite=21.20.880), WAC 460-99C). Up to $1M / 12 months for WA-resident investors. $600 filing fee. Probably too small to be the only Phase 2 vehicle but useful as a complement for a residents-only voting tranche.

### Voting shares to residents only

Whatever Phase 2 vehicle you use, the *voting* tranche (Class V) should be a separate, very small instrument ($100–$1,000) sold only to verifiable Loyal Heights residents under either the Washington intrastate exemption or the cooperative-style exemption (if you go that route). Treating voting and economic rights as separate instruments is what makes "anyone can invest, only residents vote" legally clean.

### One thing not to do

**Do not accept any money** — even "pledges" — into a personal account, the Trust's account, or anywhere else before securities counsel has papered an offering. Refunds become non-trivial fast. Keep the $1.4M as non-binding indications of interest until offering documents exist. The site's current ALL-CAPS disclaimer is good and should stay.

## 6. Two-week / thirty-day / sixty-day plan

### Days 1–10

- File Articles of Incorporation, *DTLH Trust, Inc.*, with WA Secretary of State (RCW 24.03A). $30 if you certify <$500K initial gross revenue. Same-day effective.
- Adopt initial bylaws. Pick three incorporators / initial directors — yourself plus two anchors or trusted neighbors.
- Apply for an EIN (free, online, ~10 minutes).
- Open a bank account at Verity Credit Union (Loyal Heights branch is a few blocks from the corner) or Beneficial State Bank.
- Engage a fiscal sponsor for tax-deductible donations until the IRS recognizes 501(c)(3). Sustainable Seattle, SEED Seattle, or 501 Commons are likely fits.
- Update dtlh.org "Where This Is" section with the entity name, registered agent, and updated disclaimer (draft language in [`../drafts/site-update-language.md`](../drafts/site-update-language.md)).
- Ask probono lawyer for a securities counsel referral. Davis Wright Tremaine, Perkins Coie, K&L Gates, and Stoel Rives all have Seattle securities practices and probono programs.

### Days 10–30

- Engage securities counsel. Initial scope: Phase 1 Reg D 506(c) offering structure, including the operating LLC formation timing.
- Draft an Indication of Interest form with disclaimers and structured intake. Send to existing pledgers.
- Convene a founding board: 5–7 people. Mix: Jed (founder/chair-for-now); 1–2 anchor representatives; 2–3 Loyal Heights residents (rotate in younger neighbors; KCT-style youth seats are worth the friction); 1 advisor with real estate or community-finance experience.
- File Form 1023 (501(c)(3)) or Form 1024-A (501(c)(4)). 1023 is slower (~6–9 months) but unlocks tax-deductible donations directly.
- Have a real estate consultant draft a development pro forma.
- Send a non-binding LOI exploration to the seller via the Trust + a real estate attorney.

### Days 30–60

- Form *DTLH Holdings, LLC* under RCW 25.15 when securities counsel signals readiness. Manager-managed; sole manager is the Trust.
- Securities counsel finalizes Reg D 506(c) Subscription Agreement, PPM, and accreditation verification process.
- Convert indications of interest into actual subscriptions for the anchor round.
- Submit a non-binding LOI to the seller through the LLC, contingent on closing the Phase 1 raise and on standard diligence.
- Begin Phase 2 design with securities counsel.

By Day 60: a Washington nonprofit corp, an operating LLC, $1M+ of papered anchor commitments, an LOI to the seller, and a Phase 2 plan in counsel's hands. **A credible counterparty in commercial real estate terms.**

## 7. Punch list for your probono lawyer

Hand them this section directly. It assumes a generalist corporate / nonprofit lawyer in Washington.

### Immediate (this week)

1. File Articles of Incorporation for *DTLH Trust, Inc.*, a Washington nonprofit corporation under RCW 24.03A. Use the [SOS form NP_PS_24.03A_AOI](https://www.sos.wa.gov/sites/default/files/2023-10/NP_PS_24.03A_AOI.pdf). Purpose clause should be drafted to support both 501(c)(3) and (c)(4) eligibility — e.g., *"to promote the long-term well-being of the Loyal Heights neighborhood through community-owned real estate, civic engagement, and other charitable and social-welfare activities."* Include the IRS-required dissolution-of-assets clause.
2. Identify a registered agent.
3. Draft initial bylaws. Required provisions: resident-only membership eligibility (define "Loyal Heights resident" by zip code or precise boundary — align with the Loyal Heights Community Association); board of 5–7 elected by members; staggered terms; conflict-of-interest policy (IRS-style); whistleblower policy; document-retention policy. Reserve an amendment process that requires both board and member approval.
4. Apply for EIN.
5. Refer Jed to a Seattle securities counsel — preferably someone with private-fund + real-estate-syndication experience. Explicitly *not* a generalist corporate lawyer.
6. Refer Jed to one or two fiscal sponsor options for receiving tax-deductible predevelopment donations while the 501(c)(3) is pending.

### 30–60 days

7. Form *DTLH Holdings, LLC* under RCW 25.15 when securities counsel signals readiness. Manager-managed; sole manager is the Trust. Operating agreement to be drafted by securities counsel with the three-class structure noted in section 3.
8. File Form 1023 (or 1024-A) with IRS for tax-exempt status.
9. File WA Secretary of State Charity Registration if soliciting donations.
10. Standard tax-exempt org corporate hygiene: organizational meeting minutes, conflict-of-interest acknowledgments from each director, EIN/state tax registrations.

### Templates to ask SELC for or to start from

11. NEIC Articles of Incorporation (public PDF, link in [`../precedents/neic.md`](../precedents/neic.md)) — for the resident/non-resident share-class language.
12. EBPREC Form 1-A on EDGAR (link in [`../precedents/ebprec.md`](../precedents/ebprec.md)) — for offering circular and share-class drafting.
13. SELC's [free Templates page](https://www.theselc.org/templates) and [Bite-Sized Legal Guides](https://www.theselc.org/bite-sized-law).
14. Mercy Corps NW Plaza 122 case study (link in [`../precedents/epcit-plaza-122.md`](../precedents/epcit-plaza-122.md)) — share with whoever underwrites the eventual bank LOC.

### Things to confirm with WA DFI before any solicitation

15. Whether a separate Washington notice filing is required alongside the federal Form D for Reg D 506(c).
16. Whether the cooperative-style RCW 21.20.320(15) / WAC 460-44A-200 exemption is usable for a small resident-only voting tranche even though the entity is not formally a cooperative.
17. Whether the WA intrastate crowdfunding exemption ([RCW 21.20.880](https://app.leg.wa.gov/rcw/default.aspx?cite=21.20.880)) is realistic for a real estate offering at the scale you contemplate.

## 8. Risks and things to watch

- **General solicitation has already occurred.** Fine for Reg D 506(c), Reg A, and Reg CF, but it forecloses 506(b) for any new investors who came to you via the site. Don't let anyone tell you to "switch to 506(b)" — that ship has sailed.
- **"Pledges" as informal IOUs.** Track them in writing with a dated indication-of-interest form. Make the disclaimers loud. The site's current ALL-CAPS disclaimer is good and should stay; make the form's disclaimer match.
- **Anchor diligence on the seller.** $8.8M is the *list* price. Get an independent appraisal before committing real money. Keep the public posture of "we don't have a credible offer to make yet" even after the entity is formed; it telegraphs discipline.
- **Resident definition.** Define it precisely in the bylaws and operating agreement. Use the Loyal Heights Community Association boundary or a specific zip-code list. Litigation over membership eligibility has sunk co-ops before.
- **Anchor governance creep.** The site says any anchor wanting an LLC board seat will get one. Be careful not to staple board seats to dollars in a way that gives anchors veto power over Trust-driven decisions. Reserve "major decisions" (sale of the asset, change of mission, dissolution) to the Trust regardless of how cap-table economics shake out.
- **IRS UBIT and private benefit.** A 501(c)(3) holding LLC interests where neighbors get distributions risks failing the "private benefit" test. Securities counsel and tax counsel should pressure-test this together. Pick the cleanest path with counsel.
- **"Trust" in the entity name.** Washington restricts "Bank" hard and "Trust" softer (regulated trust companies engaged in fiduciary services). A nonprofit using "Trust" as a moniker is generally OK, but counsel should confirm before filing. Alternatives: *Loyal Heights Community Trust, Inc.* or *Downtown Loyal Heights, Inc.* with "DTLH Trust" as a public brand.

## 9. Site update language

Once the entity is filed, replace the second-to-last paragraph of the *Where This Is* section. Draft language is in [`../drafts/site-update-language.md`](../drafts/site-update-language.md).

## 10. Addendum (260510): seller financing

Conversation that came after the original memo: the church seller may be open to seller financing. This changes the Phase 1 math materially. If the church carries paper for ~80% of the purchase price, the equity needed for acquisition drops from ~$5M to ~$1M, which fits comfortably into a single Reg D 506(c) round.

Drilldown lives in [`07-relationship-to-seller.md`](./07-relationship-to-seller.md) (planned). Key starting-point terms to anchor a conversation:

| Term | Aggressive ask | Reasonable middle | Likely worst-case |
|---|---|---|---|
| Down payment | 10% ($500K) | 15–20% ($750K–$1M) | 25%+ ($1.25M+) |
| Interest rate | 3–4% (mission-aligned, below market) | Applicable Federal Rate (~4.5% mid-term as of 2026) | Market (6–7%) |
| Term | 10 years, no balloon | 7 years with year-5 balloon | 5-year balloon |
| Amortization | Interest-only | 25-year amortization with balloon | 15-year amortization |
| Subordination to construction lender | Yes, automatic | Yes, with consent not unreasonably withheld | Conditional / negotiated |
| Restrictive use covenants | Generic prohibitions only | Specific positive uses + generic prohibitions | Detailed approval rights over tenants |
| Right of repurchase on default / use change | Standard cure rights | Yes, with formula-based price | Yes at original price |

**The one term that's existential: subordination.** When you go to a construction lender for $30–40M, that lender will demand a first lien. The seller note has to be willing to subordinate. If the church refuses, the seller note has to be paid off before construction can start. Get subordination committed in writing in the LOI, not as a "we'll figure it out later."

## Sources and links

### Washington statutes & regulators
- [RCW 24.03A — WA Nonprofit Corporation Act](https://app.leg.wa.gov/RCW/default.aspx?cite=24.03A)
- [WA SOS Articles of Incorporation form NP_PS_24.03A_AOI](https://www.sos.wa.gov/sites/default/files/2023-10/NP_PS_24.03A_AOI.pdf)
- [RCW 23.86 — Cooperative Associations](https://app.leg.wa.gov/rcw/default.aspx?cite=23.86&full=true)
- [RCW 23.100 — Limited Cooperative Associations](https://app.leg.wa.gov/RCW/default.aspx?cite=23.100&full=true)
- [RCW 21.20.310 — Securities exempt from registration](https://app.leg.wa.gov/rcw/default.aspx?cite=21.20.310)
- [RCW 21.20.880 — Intrastate crowdfunding](https://app.leg.wa.gov/rcw/default.aspx?cite=21.20.880)
- [RCW 25.15 — WA LLC Act](https://app.leg.wa.gov/RCW/default.aspx?cite=25.15)
- [WA DFI Crowdfunding FAQ](https://dfi.wa.gov/crowdfunding/crowdfunding-frequently-asked-questions)
- [WA DFI Securities Exemption Tables](https://dfi.wa.gov/securities-registration/securities-exemption-tables)

### Federal securities
- [SEC: Rule 506(c) general solicitation](https://www.sec.gov/resources-small-businesses/exempt-offerings/general-solicitation-rule-506c)
- [SEC: Assessing accredited investors under Reg D](https://www.sec.gov/resources-small-businesses/capital-raising-building-blocks/assessing-accredited-investors-under-regulation-d)
- [Paul Hastings: 2025 SEC Reg D 506(c) verification guidance](https://www.paulhastings.com/insights/client-alerts/sec-provides-updated-guidance-reducing-burden-for-rule-506-c-verification-requirement)

### Fiscal sponsorship (Seattle)
- [501 Commons — Fiscal sponsorship summary](https://www.501commons.org/resources/tools-and-best-practices/starting-a-nonprofit/fiscal-sponsorship-summary)
- [Sustainable Seattle — Fiscal Sponsorship](https://sustainableseattle.org/programs/fiscal-sponsorship/)
- [Seattle Parks Foundation — Become a Partner](https://www.seattleparksfoundation.org/community-partners/become-a-partner/)
- [SEED Seattle — Intermediary Services](https://www.seedseattle.org/intermediary-services/)

---

*This memo is a working draft. It synthesizes public materials and is not legal, tax, or investment advice.*
