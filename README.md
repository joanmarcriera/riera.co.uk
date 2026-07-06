# riera.co.uk

Single-page professional portfolio for [riera.co.uk](https://riera.co.uk/), the hub
of a small family of sites. Served by GitHub Pages from the `main` branch root.

## Structure

- `index.html`: the portfolio (hero, portfolio index, approach, experience,
  credentials, platform, products, contact).
- `styles.css`: the visual system (Inter, Space Grotesk, JetBrains Mono; light
  sections with dark `scope-dark` bands; the ⌘K switcher).
- `app.js`: builds the portfolio directory, the family footer, and the ⌘K site
  switcher from the shared `SITES` array. Ships on every site in the family.
- `CNAME`: custom domain binding.
- `assets/documents/`: public publications and articles only.

## Site family

The ⌘K switcher (press ⌘K on any page) and the footer are driven by the `SITES`
array in `app.js`:

- `riera.co.uk`: portfolio and entry point
- `cv.riera.co.uk`: curriculum vitae
- `cxo.riera.co.uk`: CTO playbook
- `sme.riera.co.uk`: SME automation practice (fixed-scope audit and reference stack)
- `cnc.riera.co.uk`: CNCraft
- `i2e.riera.co.uk`: Image to Excalidraw
- `llm.riera.co.uk`: personal LLM notes
- `mac.riera.co.uk`: Mac rebuild notes

## Deployment

GitHub Pages serves from the `main` branch root. Edit, commit, and push; the change
is live within a few minutes.
