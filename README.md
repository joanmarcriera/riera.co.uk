# riera.co.uk

Professional portfolio and consulting landing page for [riera.co.uk](https://riera.co.uk/).

## Structure

- `index.html` — single-page portfolio: about, experience, work, credentials, consulting, contact
- `styles.css` — site styling (Cormorant Garamond + Karla, warm cream + teal accent)
- `app.js` — scroll reveal, mobile nav, audit form submission (n8n webhook)
- `CNAME` — custom domain binding
- `assets/documents/` — publications and reference materials

## Site Network

- `riera.co.uk` — portfolio and consulting front door
- `cv.riera.co.uk` — preserved CV surface
- `cxo.riera.co.uk` — strategy and executive layer
- `sme.riera.co.uk` — practical SME systems and demo layer

## Adding Work Items

To add a new case study, publication, or blog post, copy one of the `<article class="work-card">` blocks in the Work section of `index.html` and update the content. Supported types: `Case Study`, `Publication`, `Blog Post`, `Talk`.

## Deployment

GitHub Pages serves from the `main` branch root. Edit, commit, push.
