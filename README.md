# cv

[![Deployment](https://github.com/aejb/cv/actions/workflows/deploy.yml/badge.svg?branch=main)](https://github.com/aejb/cv/actions/workflows/deploy.yml)

This script ingests a [JSON Resume](https://jsonresume.org/) compatible `resume.json` and renders it using a custom template with Jinja2

It then deploys the generated `index.html` to the `/pages` branch, which can be configured to serve the page

## requirements

- `Jinja2` (3.0.1)

## usage

1. Fork this repo
2. Clone it locally
3. Replace `resume.json` with your own CV following [the JSON Resume Schema](https://jsonresume.org/schema/)
4. **Ensure you have a `profiles` object inside `basics` with the `network` key as `GitHub` and the `username` key as your own github username.** This allows Jinja to find your raw JSON CV to link it.
5. If you are using the GitHub Pages automation:
    1. Enable the Action on your fork
    2. Push to GitHub (required for automation to trigger)
    3. [Enable GitHub Pages on the `/pages` branch](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
6. Otherwise:
    1. Run `script.py`
    2. It will output `index.html`

## automation

The [Deploy Action](https://github.com/aejb/cv/blob/main/.github/workflows/deploy.yml) does the following steps on the `push` trigger:
1. Checkout an orphaned `pages` branch
2. Generate `index.html`
3. Commits only `index.html` to origin

## disclaimer

Yes, I know that using Jinja Macros is awful and I could do this way better, but I do not care.

Yes, I know that using `git reset` and empty branches isn't the best, but I wanted the `/pages` branch to only contain `index.html`.
