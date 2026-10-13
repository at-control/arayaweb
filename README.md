# Araya design preview

Static review preview for PT Araya Internusa, preserving the existing website's orange/charcoal/white industrial styling and Space Grotesk typography.

Preview: https://hakiimm8.github.io/arayaweb/

Saved audit findings, design decisions, verification results and next steps: [Project notes](docs/PROJECT-NOTES.md).

Start with the [documentation index](docs/README.md), [progress/release record](docs/PROGRESS.md) and [content sources](docs/CONTENT-SOURCES.md). Latest website-content release: [c92ba45](https://github.com/hakiimm8/arayaweb/commit/c92ba4524cb85d2354bda8f8dd159478cbca7b93). The 14 October experience improvements are recorded in [implementation notes](docs/IMPROVEMENTS-2026-10-14.md); current deployment status is in the progress/release record.

## Files

- `public/`: the complete published site, with home, marine, industrial, automation & electrical, Noris and ComAp pages, plus `sitemap.xml`.
- `tools/site_content.py`: company content: service pages, clients, multi-brand equipment lists and homepage common requests.
- `tools/prepare_site_assets.py`: client logos, date-stamp-free responsive photos, the share image and the proportioned logo.
- `tools/build.py`: shared HTML template and page copy. Run `python tools/build.py` after editing.
- `tools/brand_profiles.py` and `tools/brand_pages.py`: researched brand content and dedicated brand-page layout.
- `tools/comap_applications.py`: 18 published application explanations grouped by marine, power generation and smart energy management.
- `.github/workflows/pages.yml`: publishes `public/` on push to main or manual dispatch. No PR triggers.

The build templates require Python 3.12 or newer.

To preview locally, serve `public/` with a static HTTP server. WordPress and PHP are not required for this preview.

The **Brand Partners** dropdown and footer brand links are generated from `BRANDS` in `tools/brand_profiles.py`. See [adding a future partner](docs/BRAND-MAINTENANCE.md). The homepage has individual Noris and ComAp buttons.

## Scope and sources

This is a public design preview with noindex,nofollow metadata. The production WordPress site remains at https://arayainternusa.co.id/araya/. Preview hosting performance does not represent production WordPress performance.

Existing Araya logo, engineering photographs, company history, and displayed business contacts come from the owner's supplied website files and live site. Email/phone destinations have been aligned with their displayed labels; deliverability has not been tested. No enquiry is automatically sent. Service and brand links stay within the preview, with separate links to manufacturer references and the current website.

Marine and industrial pages describe project scopes provided by the owner and the existing service pages. They are capability descriptions, not invented named case studies. Product families, example models, and 14 manufacturer product images have source attribution in [Content sources](docs/CONTENT-SOURCES.md). Model availability and project suitability require discussion with Araya.

Dedicated Noris and ComAp guides include manufacturer background, a product-family index, application guidance, an Araya enquiry brief and accessible expandable FAQs. Noris covers eight product areas; ComAp covers six. These are Araya's brand guides for Indonesia; manufacturer links lead to current product details and documents.

The owner states that Araya distributes Noris and ComAp in Indonesia. Authorization, exclusivity, specific product availability and warranties are not asserted. General certification wording is owner-approved; specific certification names, issuers and scope have not been provided.

Manufacturer application sources checked 2026-10-08:

- https://www.noris-group.com/industries/shipbuilding
- https://www.comap-control.com/products/controllers/

Space Grotesk is distributed under the SIL Open Font License; see `public/assets/fonts/OFL.txt` and https://github.com/google/fonts/tree/main/ofl/spacegrotesk.

WordPress files, database exports, private configuration, backups and logs are not part of this repository or deployment artifact.

ComAp now leads with an expandable application guide and real manufacturer system diagrams before the product catalogue. See [application sources and scope](docs/COMAP-APPLICATIONS.md).

Noris includes noriNet remote vessel monitoring, a manufacturer dashboard picture and a zoomable vessel-to-shore system diagram. See [NORINET research and implementation](docs/NORINET-RESEARCH.md).
