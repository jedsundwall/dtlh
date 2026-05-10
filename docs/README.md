# Working drafts

This directory holds the thinking behind Downtown Loyal Heights — entity structure, governance, finances, and the precedents we're learning from.

The [homepage](https://dtlh.org) is the pitch: short, opinionated, and aimed at someone deciding whether to engage. **These docs are the sketches**: longer, more provisional, sometimes wrong, and aimed at neighbors and counsel who want to see the work behind the pitch.

Everything here is a draft. Nothing here is legal, tax, or investment advice. Nothing here is an offer of securities. Many of these documents will be wrong in interesting ways, and we'd like to know about it — please [open an issue](https://github.com/jedsundwall/dtlh/issues) or a pull request if you spot something.

## Where things live

- **[current/](./current/)** — what we currently think about each topic (mission, entity structure, governance, finances, securities, etc.). One file per topic. The source of truth for "where things stand."
- **[decisions/](./decisions/)** — dated records of major choices, lightweight ADR-style. Why we picked one path and what we considered.
- **[precedents/](./precedents/)** — notes on the projects we're learning from (NEIC, NYC REIC, Plaza 122, EB PREC, Kensington Corridor Trust, VREC, etc.). What we're borrowing and what's different in our case.
- **[drafts/](./drafts/)** — works in progress. Half-formed thoughts. Things being explored. Read with skepticism.
- **`private/`** *(gitignored, not in this listing)* — local-only working notes that shouldn't be public yet. Not backed up by git.

## Conventions

**File format:** Markdown only. We render to PDF when we need a document for counsel or another formal audience.

**Date prefixes:** `YYMMDD`. Example: `260509-form-wa-nonprofit-trust.md` is May 9, 2026. Used for `decisions/` filenames and any other date-stamped artifact.

**Numbered files in `current/`:** Two-digit prefixes (`00-`, `01-`, `02-`, …) so files sort in a useful reading order. Numbers are stable — we don't renumber when adding a new doc; we just pick the next available number, leaving gaps where appropriate.

## Status labels

Each `current/` document carries a status near the top:

- **SKETCH** — early thinking, may be wrong, posted for discussion
- **WORKING** — actively being refined; expect changes
- **PROPOSED** — ready for review and decision
- **AGREED** — decided, with at least one decision record backing it
- **SUPERSEDED** — replaced by a newer document (which will be linked)

`decisions/` documents carry **PROPOSED**, **ACCEPTED**, or **SUPERSEDED-BY-…**.

## How `current/` and `decisions/` relate

`current/` documents describe the present working hypothesis on a topic. They get updated in place when our thinking changes — but each meaningful change should be backed by a `decisions/` entry that explains the reasoning. That way, anyone reading a `current/` doc can trace its history through the linked decisions.

A `current/` doc that has never had a decision record is just a sketch. A `current/` doc with one or more linked decisions has been deliberately chosen, and reversing it requires writing a new decision record that supersedes the old one.

## How decisions get made — for now

There is no formal governance yet. Until the Trust is incorporated and has a board, decisions are made by Jed Sundwall in consultation with neighbors who've reached out, anchor pledgers, and pro bono legal counsel. Records in `decisions/` capture those consultations and conclusions; they are not commitments enforceable against anyone.

Once the Trust is incorporated, this section gets replaced with the real governance process and a link to the bylaws.

## How to contribute

This is a public conversation. If you live in Loyal Heights or have done work like this elsewhere, and you see something we're missing or getting wrong:

1. Open an [issue](https://github.com/jedsundwall/dtlh/issues) describing what you see.
2. Or send a pull request with proposed changes — markdown only, please.
3. Or email Jed at jedsundwall@gmail.com if a public thread isn't right.

Pull requests get a response within a few days. Counsel will be involved before anything that touches legal structure or securities is changed in a binding way.

## Why these are in the repo and not on the website

The homepage is a pitch document — polished, public, and stable. These docs are the working sketches behind it. Mixing them on the same site would muddy both audiences (people deciding whether to engage with the pitch, vs. people checking the underlying reasoning).

GitHub renders markdown well, and the repo is already public, so anyone can read these without us having to publish anything new. If specific documents become stable enough to want broader visibility, we can surface them on the website later. Until then, the URL to share is the GitHub one.

## A note on legal status

Nothing in this directory is legal, tax, or investment advice. Specific entity structures and securities approaches discussed here are the working hypothesis as of the date of each document. Anything binding will be drafted by counsel and disclosed through formal offering documents.

The homepage's all-caps disclaimer applies to everything here too: this is a concept, not an offering.

## Index of `current/` documents

The full set we expect to have over time. Files marked with a checkmark exist; others are placeholders showing where the thinking will live.

- [x] [`00-formation-memo.md`](./current/00-formation-memo.md) — the speed-run formation memo (260509). The gestalt overview; topical drilldowns below may evolve past it.
- [ ] `01-mission-and-scope.md` — what we're trying to do and why
- [x] [`02-entity-structure.md`](./current/02-entity-structure.md) — the two-entity Trust + LLC model
- [ ] `03-governance.md` — board composition, member rights, voting
- [ ] `04-membership-and-residency.md` — who counts as a Loyal Heights resident, and how we verify
- [ ] `05-capital-stack.md` — phased financing, anchors, community equity
- [ ] `06-securities-strategy.md` — Reg D 506(c), Reg CF, Reg A+, intrastate
- [ ] `07-relationship-to-seller.md` — LOI posture, seller financing, contingencies
- [ ] `08-stewardship-and-mission-lock.md` — what the Trust actually protects, and how

## Index of `decisions/` so far

- [`260509-form-wa-nonprofit-trust.md`](./decisions/260509-form-wa-nonprofit-trust.md) — form Downtown Loyal Heights Trust as a Washington nonprofit corporation under RCW 24.03A. Status: PROPOSED.

## Index of `precedents/`

- [`neic.md`](./precedents/neic.md) — NorthEast Investment Cooperative (Minneapolis, 2011)
- [`nyc-reic.md`](./precedents/nyc-reic.md) — NYC Real Estate Investment Cooperative (2015)
- [`epcit-plaza-122.md`](./precedents/epcit-plaza-122.md) — East Portland Community Investment Trust / Plaza 122 (2017)
- [`kensington-corridor-trust.md`](./precedents/kensington-corridor-trust.md) — Kensington Corridor Trust (Philadelphia, 2019)
- [`ebprec.md`](./precedents/ebprec.md) — East Bay Permanent Real Estate Cooperative (Oakland, 2017)
- [`vrec.md`](./precedents/vrec.md) — Vermont Real Estate Cooperative (2020)

## Index of `drafts/`

- [`site-update-language.md`](./drafts/site-update-language.md) — replacement copy for the *Where This Is* section once the Trust is filed
