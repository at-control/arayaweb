# Araya project notes

Latest release: [fe80362](https://github.com/hakiimm8/arayaweb/commit/fe80362574d96b1ec99cc1d8cae81e9f760cea15), earlier picture discovery, lighter text motion, finite metric counters, scalable original logo/tab branding and Leadership removal. See [diagnosis and verification](LOADING-COUNTERS-AND-BRANDING-2026-10-14.md). Earlier release labels below are historical.

Current release: [921909b](https://github.com/hakiimm8/arayaweb/commit/921909bf355c1ec6454f63127ea26a12e378daa1), 14 October 2026. Professional positioning, navigation/enquiry improvements and motion are recorded in [implementation notes](IMPROVEMENTS-2026-10-14.md). The earlier release notes below are historical.

Recorded 8 October 2026, Asia/Jakarta. Historical observations from the project session; not a fresh audit or ongoing monitoring.

## Current state and records

Latest website release `f19cc41` deployed successfully in [Pages run 37880869568](https://github.com/hakiimm8/arayaweb/actions/runs/37880869568). Noris now has eight product areas including noriNet remote vessel/fleet monitoring, with a manufacturer dashboard and full-width system diagram. Diagram zoom and source credits work for both brands. Local and published Edge checks passed at 1280/390/360px, including image dimensions, anchors, keyboard/modal behaviour, owner contact, no-JavaScript fallback and no runtime/HTTP errors or overflow. See NORINET-RESEARCH.md for the brochure revision, explanation and implementation; CONTENT-SOURCES.md records both unchanged assets.

Earlier website release `c37c534` deployed successfully in [Pages run 37879114243](https://github.com/hakiimm8/arayaweb/actions/runs/37879114243). ComAp has thirteen manufacturer application diagrams with fit/zoom viewing, scrolling, linked credits, native fallback and keyboard close/focus handling. Local and published checks passed for all thirteen at 1280/390/360px. Source provenance and viewer maintenance are recorded in COMAP-APPLICATIONS.md and BRAND-MAINTENANCE.md.

Earlier application-guide release `52d954e` deployed successfully in [Pages run 37878202684](https://github.com/hakiimm8/arayaweb/actions/runs/37878202684). ComAp now leads with 19 detailed applications across Marine, Power generation and Smart energy management, three manufacturer system diagrams and application-first navigation. Local and published checks passed at 1280/768/390/360px, including keyboard/native expansion, hashes, diagram views and enquiry/product links. See COMAP-APPLICATIONS.md for source and scope details.

Earlier product-picture release `de91d39` deployed successfully in [Pages run 37868242535](https://github.com/hakiimm8/arayaweb/actions/runs/37868242535). Every Noris/ComAp product section now has a real manufacturer picture; 11 new WebP assets total 285,534 bytes. Local and published desktop/mobile image checks passed. Exact sources and usage boundaries are in CONTENT-SOURCES.md.

Earlier navigation release `b51bc47` deployed successfully in [Pages run 37867253415](https://github.com/hakiimm8/arayaweb/actions/runs/37867253415). The owner selected a **Brand Partners** dropdown with separate Noris and ComAp entries. Header/footer brand links and generated brand routes use shared BRANDS data; homepage brand buttons remain separate. Local/published checks across all five routes at 1280px, 1024px and 390px passed, including keyboard/Escape focus, outside-click closing, mobile navigation, direct hero links and no-JavaScript navigation. No overflow/page/console/HTTP errors. Future-partner instructions: [Brand maintenance](BRAND-MAINTENANCE.md). The preceding brand-guide release described below remains historical; content is retained.

The preview contains five routes: home, marine, industrial, Noris and ComAp. Brand-guide content commit `e866993` deployed successfully in [Pages run 37782440114](https://github.com/hakiimm8/arayaweb/actions/runs/37782440114). Brand guides include product indexes, profiles, applications, enquiry briefs and FAQs; published desktop/mobile checks passed. Original logo restored; recreated SVG is superseded. Production remains unchanged.

See [documentation index](README.md), [progress and releases](PROGRESS.md) and [content sources](CONTENT-SOURCES.md). Earlier three-page notes below are historical. Owner WhatsApp is now shared across all five pages.

## Purpose and decisions

Improve PT Araya Internusa's website and discoverability for Noris and ComAp in Indonesia. The owner states the distributor relationship; authorization/exclusivity, specific supplied models and support commitments remain unverified.

The owner selected the CURRENT LIVE website style: orange, charcoal and white, Space Grotesk, original logo and project photographs. The earlier navy mockups are superseded.

- Production: https://arayainternusa.co.id/araya/
- Preview: https://hakiimm8.github.io/arayaweb/
- GitHub Pages is a static review preview. Production WordPress is unchanged.
- VM staging is optional; not used for this release.
- No pull_request or pull_request_target Actions triggers. Publish on push/main or manual dispatch. No skip-CI merge instructions.

## Recorded production audit

Single Lighthouse 13.5.0 lab runs on 8 October 2026, approximately 08:30 Jakarta. Not field data or ranking measurements. Temporary raw reports were not retained; rerun and retain reports for future comparisons.

| Category | Mobile | Desktop |
| --- | ---: | ---: |
| Performance | 37 | 76 |
| Accessibility | 87 | 87 |
| Best practices | 96 | 96 |
| SEO | 83 | 83 |

Mobile LCP was 11.90 s, TBT 860 ms and CLS 0.089. The LCP element was cookie-notice text, so the observation includes the cookie-overlay layout.

Main findings:

- Weak Noris/ComAp positioning and no dedicated brand pages found in the original audit.
- Generic homepage title, long description, headings/image alternatives needing review, placeholder structured-data properties.
- Indexable demo/sample pages in the sitemap.
- Large external slider images, many CSS/JS requests, cross-origin errors and theme-demo asset references.
- Footer email/phone destinations did not match their displayed business details.
- Domain root redirected temporarily (302) to /araya/. Keep /araya/ initially; treat a root migration separately.
- Live loading overlay blocked exact screenshot comparison during preview work.

## Initial preview completed — historical baseline

- Homepage plus distinct Noris and ComAp pages with descriptive titles/headings and contact routes.
- Responsive layout/menu, Escape close/focus return, keyboard focus, reduced-motion support, optimized local images/font.
- Corrected preview contact destinations to match the original displayed details; calling/mail delivery not tested.
- Relevant orange text/button fill darkened to #cb4800 after independent accessibility review (approximately 4.70:1 contrast against white).
- Main vessel/control-room images reduced from approximately 2.9 MB combined to 234 KB. File-size reduction is not a measured production performance improvement.
- Desktop/mobile, deployed nested routes, metadata, image alt text, local assets/fragments and public artifact exclusions checked.
- Initial reviewed preview commit: a0a1dc6; Pages workflow run 37751836932 succeeded.

Only public/ is deployed. Preview uses noindex,nofollow. This does not test WordPress/Elementor/PHP, production hosting, form delivery or search rankings. Preservation follows observed live styling and original assets; exact pixel fidelity to the live page was not verified.

## Next steps

Contact update, 8 October 2026: the owner supplied WhatsApp +62 81326396262 and requested its publication. Added the displayed WhatsApp number and direct https://wa.me/6281326396262 link to the shared contact section on all three preview pages. No WhatsApp message was sent.

1. Review preview content and confirm distributor wording, supplied products, support scope and contacts.
2. Obtain WordPress administrator/database access and verified files + database backup before production edits.
3. Apply reviewed content/settings and custom code selectively to WordPress; avoid overwriting a current production database with an older copy.
4. Clean up demo URLs, titles/descriptions, schema, headings, internal links and sitemap.
5. Optimize production assets/scripts and investigate cookie/preloader issues.
6. Recheck production contact paths/crawlability/mobile rendering; rerun comparable Lighthouse measurements and retain evidence.

## Maintenance

Project/brand detail expansion, 8 October 2026: owner supplied typical marine work including fire alarms, AMS, engine overhaul/control, generator synchronisation and auto start/stop, panels, PLC/SCADA, water-level and cargo monitoring, navigation, steering/manoeuvring, cranes and retrofit. Added marine and industrial detail pages and homepage scope summaries. Industrial grouping also follows Araya's existing machinery/crane/automation service descriptions. Noris and ComAp pages now show manufacturer product-family examples, selection details, attributed product images and links to relevant project scopes. No named completed projects, model-stock claims or blanket certifications were added. Sources and image provenance: [Content sources](CONTENT-SOURCES.md). Preview now contains five pages. Stylesheet URL includes a content hash to refresh changed styling without losing the original logo fix.

Original logo restoration, 8 October 2026: the owner rejected the recreated SVG because it changed the brand symbol. Found an existing transparent original, logoaraya4.png, in the website uploads. Copied it unchanged as araya-logo-original.png (291×52); matching SHA-256 confirms identical bytes. Shared header, footer and Organization schema now use that original artwork. Display aspect ratio is 238:52, taken from the original opaque lockup, to correct the transparent upload's horizontal stretch and keep the circular mark round. The header block remains #ee5c03 and the image has no opaque orange rectangle. Removed the rejected SVG and its recreation script. Preserve the original mark, letterforms and proportions in future work; do not redraw or reinterpret them. Earlier ImageGen attempts were also rejected and never published.

Project experience update, 8 October 2026: the owner supplied the figure of more than 1,500 projects and coverage including Sumatra, Jawa, Kalimantan, Sulawesi, and Papua. The homepage now presents “1,500+ projects across Indonesia” and these five regions. This is an owner-provided aggregate; no per-region counts or individual project/client claims were added.

Brand emphasis update, 8 October 2026: at the owner's request, homepage and brand pages now highlight Noris Group GmbH instruments/sensors (speed, temperature, pressure, indicators and signal processing), and ComAp engine control, power management and load sharing. Manufacturer descriptions were checked against the sources below. Exact model/feature compatibility and availability remain subject to confirmation; no blanket feature or authorization claim was added.

Edit shared copy/templates in tools/build.py, researched brand data in tools/brand_profiles.py and brand rendering in tools/brand_pages.py; regenerate with `python tools/build.py`. Check the artifact with `python tools/check.py` and `node --check public/assets/site.js`, then inspect changed desktop/mobile views. Update the progress/source records alongside changes.

Full technical findings and handoff notes are stored in the owner's local workspace. This public summary excludes hosting account information, local machine paths, credentials, databases and backups.

## Sources

- https://www.noris-group.com/industries/shipbuilding
- https://www.noris-group.com/industries/machinery-and-equipment
- https://www.comap-control.com/products/controllers/
- https://uk.comap-control.com/application-areas/marine/engine-control/
- https://www.comap-control.com/products/extended-features/extended-feature-load-sharing-power-management/
- https://developer.wordpress.org/advanced-administration/upgrade/migrating/
- https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages

## Dedicated brand-page expansion — 8 October 2026

Owner requested further manufacturer research and complete individual brand pages. Noris now has seven indexed product areas: speed, temperature and pressure sensors; analogue instruments; signal processing; noriMos monitoring; and noriStar propulsion control. ComAp now has six: InteliDrive engine supervision, InteliGen paralleling/load sharing, marine power management, InteliLite single-set/standby control, InteliSCADA and WebSupervisor. Each page has a manufacturer profile, real product hero image, section navigation, applications, an Araya enquiry brief, and three accessible native details/summary FAQs. All facts and model examples are linked to manufacturer references; see CONTENT-SOURCES.md. Original Araya artwork and existing style retained. No product images or logos were generated. Preview remains noindex, production unchanged. Brand copy/layout is maintained in tools/brand_profiles.py and tools/brand_pages.py, rendered by tools/build.py.


## Manufacturer product pictures — 9 October 2026

Both dedicated brand guides now show a relevant manufacturer image for every product family: seven Noris sections and six ComAp sections. Eleven additional WebP assets accompany the two existing hero images. Pictures have descriptive alt text, model/example captions, source-page credits, explicit dimensions and lazy loading. Real equipment and manufacturer example software screens are used; they do not represent Araya inventory or completed projects. See CONTENT-SOURCES.md for exact asset URLs and PROGRESS.md for checks.


## Application-led ComAp guide — 9 October 2026

The owner requested detailed application explanations beyond generic module pictures. The ComAp page now places 19 explanations in Marine, Power generation and Smart energy management groups before its six product-family sections. Each details the system, control functions, example families and selection inputs. Three manufacturer diagrams illustrate PMS, standby and hybrid systems. Application menus work by keyboard, direct links and without JavaScript; sources and regional limits are recorded in COMAP-APPLICATIONS.md.


## Expanded manufacturer diagrams — 9 October 2026

ComAp now has thirteen explanatory diagrams, with ten additional application-specific drawings and a fit/zoom viewer. Figures stay linked to the original local image for JavaScript-free use, and manufacturer credits remain visible. Native dialog focus, source/title updates, zoom/scroll, closing and mobile fit are verified; exact assets and implementation notes are in COMAP-APPLICATIONS.md.
