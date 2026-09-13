# Soumen Ghosh - academic website

A lightweight, six-page website for GitHub Pages. Generated HTML is included, so deployment requires no build service, packages or theme dependencies.

## Publish

1. Create a public repository named `soumenca.github.io` under `soumenca`. Initialise it with a README and grant the connected GitHub app access to this repository.
2. Upload this package's contents at the repository root (not inside a parent folder).
3. In Settings > Pages, choose Deploy from a branch, `main`, `/ (root)`, then Save.
4. The website will be at https://soumenca.github.io/ once GitHub finishes deployment.

Keep the Google Site online until this address is verified, then add a prominent link to the new website on the Google Site. Update profile links after launch.

## Edit

- `content.json`: existing research, publication, teaching, news and biography content.
- `tools/build.py`: shared page layout, homepage and publication source links.
- `assets/site.css`: responsive design.
- `assets/site.js`: mobile menu and publication filtering.
- `assets/Soumen_Ghosh_CV.pdf`: public CV download. Replace this file to update the CV.

After editing content, run `python3 tools/build.py`, then commit the regenerated HTML with the content changes. No Python dependencies are required. To preview, run `python3 -m http.server 8000` and open http://localhost:8000.

## Content decisions

CDU is an Adjunct Lecturer appointment from September 2026 and is not listed as teaching experience. Supervision does not state student counts. The CVIP 2025 paper is listed as published, with a preprint link. Jobs Outside the Bubble is described as an invitation, without an unconfirmed event date. The named commercial lung-imaging product and manuscript MRI figure are not included. Student-era resources remain on the historical Google Site rather than being copied here.

The portrait is stored locally at `assets/soumen-ghosh.png`. The site uses no analytics, remote fonts, or external scripts. GitHub Pages itself has its own hosting/privacy terms.
