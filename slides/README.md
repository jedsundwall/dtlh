# DTLH slides

[Slidev](https://sli.dev) decks in Downtown Loyal Heights branding, following the same pattern as `ops-re/brand/slidev-theme-radiant`: one shared brand **addon** (`slidev-theme-dtlh/`) holding fonts, colors, the wordmark component, and the footer mark — so each deck is just a folder with a `slides.md` (plus its own `images/` if needed), not a full copy of Slidev.

## Branding

Everything mirrors `layouts/index.html` on dtlh.org:

- Cream `#F1ECE2` background, ink `#252321` text, deep pink `#B53050` headings/accents, muted `#5C4F46`
- **Germania One** for headings and the wordmark, **Source Serif 4** for body text, system mono for eyebrow labels
- Fonts are copies of `static/fonts/` — the site remains the canonical source; if the site's fonts change, re-copy them into `slidev-theme-dtlh/fonts/`
- Helper classes from the site: `.eyebrow`, `.deck-rule`, `.tagline`, `.banner`; components: `<DtlhWordmark>`
- A faint "DTLH" mark sits bottom-right on every slide (suppress per-slide with `hideLogomark: true` in that slide's frontmatter)

## Starting a new deck

Create `slides/<deck>/slides.md` with headmatter:

```yaml
---
theme: default
addons:
  - ./slidev-theme-dtlh
---
```

(Slidev resolves addon paths one level *up* from the deck folder — so from `slides/<deck>/` the base is `slides/`, and the addon is `./slidev-theme-dtlh`, not `../…`.)

## Running a deck

Install the shared toolchain once:

```
cd slides/slidev-theme-dtlh && npm install
```

Then, from the repo root:

```
slides/slide.sh slides/pitch          # dev server
slides/slide.sh slides/pitch build    # static build
slides/slide.sh slides/pitch export   # PDF
```

`node_modules/`, `dist/`, and exported PDFs are gitignored. Hugo ignores this folder entirely — nothing here affects the website build.
