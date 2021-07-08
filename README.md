# cv

This script ingests a [JSON Resume](https://jsonresume.org/) compatible `resume.json` and renders it using a custom template with Jinja2

It will (soon) be automated to use GitHub Actions and GitHub Pages

## requirements

- `Jinja2` (3.0.1)

### usage

1. Write your JSON Resume compatible file to `resume.json`
2. Run `script.py`
3. Script will output `index.html`

### automation

Once I figure it out, a GitHub Action will move the `index.html` file to the `/pages` branch, to be served by GitHub Pages
