# riera.co.uk · CLAUDE.md

**Purpose:** Static portfolio hub and site-family directory for riera.co.uk and related properties. Single-page app (SPA) serving 12+ linked sites via GitHub Pages, with keyboard-driven site switcher and unified design system.

## How to run/test

No build step. Edit HTML/CSS/JS, test locally:

```bash
# Serve locally (Python 3)
python3 -m http.server 8000

# Or Node (http-server)
npx http-server

# Visit http://localhost:8000
# Press ⌘K (or Ctrl+K) to test the switcher
```

Test across browsers/devices before pushing to `main`; changes deploy to live within minutes via GitHub Pages.

## Layout & conventions

- **index.html** — Single-page career profile for recruiters. Sections: hero (availability, CV download), delivery record, experience, credentials, projects, home lab, contact. Career facts come only from the master CV in the CV workspace; the withdrawn "35 to 9" and "94%" transfer figures must never return. No em dashes in page text. The CV is served from `assets/marc-riera_cv.pdf`. Social meta tags for OG/Twitter cards. Font preload: Space Grotesk, Inter, JetBrains Mono from Google Fonts.
- **app.js** — Builds three components on DOMContentLoaded:
  - **Directory** (`#directory`): no longer on the hub page (the function is a no-op without the element); the hub's Projects list is static HTML reusing the `.directory` styles.
  - **Footer** (`#foot-grid`): compact family grid with URL + tag per site.
  - **Switcher** (`#switcher-list`): full ⌘K dialog with num, title, desc, URL.
  - Keyboard handler: ⌘K / Ctrl+K opens switcher; Escape closes. Marks current site via `data-site` on `<html>` + `.is-current` class.
- **styles.css** — Shared design tokens:
  - Color: oklch (neutral light/dark, accent via CSS variables).
  - Typography: --font-display (Space Grotesk), --font-body (Inter), --font-mono (JetBrains Mono).
  - Sections use `.scope-dark` class for dark bands.
  - Light/dark mode: CSS custom properties, no media-query-only theming.
- **assets/** — Images (og-card.png, apple-touch-icon.png) and public PDFs (academic publications).
- **SITES array** (app.js, line 7) — Source of truth. Each site:
  - `id`: unique identifier; matches `data-site` on each site's `<html>`.
  - `num`: sequential tag (00–11).
  - `url`: human-readable domain.
  - `href`: full URL.
  - `title`, `desc`, `tag`: display text and category label.

## Gotchas & conventions

1. **data-site must match:** Each site in the family (e.g., cv.riera.co.uk) declares `<html data-site="cv">` so the switcher can mark itself as current. Mismatch breaks highlighting.
2. **SITES array is the source of truth:** Changes to the directory, footer, or switcher all source from the array in app.js. Update it once; three components rebuild on page load.
3. **GitHub Pages deployment:** Push to `main` branch; no secrets, no env files, no build step. Changes live in <5 minutes.
4. **Fonts from Google Fonts:** `index.html` loads Space Grotesk, Inter, JetBrains Mono via `link rel="preload"` for performance. Update the `href` in `<link>` if adding or removing font weights.
5. **oklch color space:** All colors defined in oklch in styles.css. Override by changing CSS custom properties at `:root` (e.g., `--accent-h`, `--accent-c`, `--accent-l`).
6. **No external dependencies:** Vanilla JS, no build tool, no npm. Keeps deployment footprint minimal.
7. **Keyboard handler is global:** ⌘K and Escape work anywhere on the page. Test on both Mac (⌘) and Windows/Linux (Ctrl).
8. **Social meta tags:** OG and Twitter Card tags hardcoded in `<head>`. Update them if site URL, description, or preview image changes.

## Testing checklist before push

- [ ] Switcher opens/closes (⌘K / Escape)
- [ ] Current site highlighted in switcher + footer
- [ ] All 12 sites link correctly
- [ ] Fonts load from Google Fonts (check Network tab)
- [ ] OG preview renders in social-media preview tools
- [ ] Favicon displays on tab
- [ ] Mobile: responsive at 375px and 1200px+ widths
