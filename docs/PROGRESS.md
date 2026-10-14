# Progress and release record

## Approved GitHub SSH staging setup — 14 October 2026

Authorized the dedicated public key through cPanel and verified pinned-host SSH login. Created the GitHub `production` environment with a main-only branch policy and five SSH connection secrets; readback confirms their names and policy. Added a manually dispatched workflow that validates the selected successful main build, provenance, safe ZIP contents and hashes before transferring ZIP/manifest into a fresh private staging directory. Six regression tests and Bash syntax pass; independent critical review found no blocking or major issues. No PR triggers or live activation were added. End-to-end run verification follows after push. [Implementation and verification](PRODUCTION-SSH-PLAN-2026-10-14.md).

## Hosting backup and private production staging — 14 October 2026

Recovered browser access and continued the authorized cPanel preparation. Confirmed working Terminal, SSH/SFTP/SCP tooling and provider SSH port 2223; rsync is not on the account PATH. Created/read-checked a private active-site archive, downloaded it and matched its SHA-256; downloaded and integrity-checked the database, matching all 62 live tables. Restored the root entry point and WordPress routing file into a separate check folder and matched hashes. Exported 65 published legacy page/post URLs, including candidate theme/demo routes that need explicit migration decisions. Uploaded the clean `f66ada9` CI candidate privately and verified all 65 extracted files on Rumahweb. Production remains WordPress; no public-root replacement, root redirect change or new public staging URL. The owner subsequently approved dedicated SSH key authorization and GitHub environment secret setup; those are now configured, as recorded above. [Detailed hosting findings](PRODUCTION-DEPLOYMENT.md#hosting-continuation--14-october-2026).

## Production root preparation — 14 October 2026

Owner requested preparation for `https://arayainternusa.co.id/`. Read-only cPanel inspection verified `public_html` and the PHP entry-point redirect to `araya/`; SSH/Terminal/Git interfaces are available, but external SSH and the activation layout remain unverified. Added an isolated production build, target-aware indexing/canonical/OG/schema/sitemap checks, publication allowlist, ZIP/checksum/provenance packaging, and CI checks/artifact retention before preview deployment. No live upload workflow or credentials were enabled. [Deployment findings and runbook](PRODUCTION-DEPLOYMENT.md); [implementation plan](PRODUCTION-PLAN-2026-10-14.md). Local production tests (5), existing experience tests (6), loading tests (3), counter/date checks and both target validators pass. Independent review caught the preview crawl/noindex interaction and generated-date source-provenance issue; both fixed and re-reviewed with no remaining major finding. No PR-triggered workflows remain. Production WordPress remains unchanged.

Preparation release [21f6e36](https://github.com/hakiimm8/arayaweb/commit/21f6e367c727066263756e62f4df2ca9480fa8dc) pushed to main. [Actions run 38514257998](https://github.com/hakiimm8/arayaweb/actions/runs/38514257998) succeeded, including validation, production artifact retention and Pages publication. Downloaded the CI production package locally and verified all 65 file checksums, ZIP checksum, source commit and `source_tree_dirty: false`. Artifact name: `araya-production-21f6e367c727066263756e62f4df2ca9480fa8dc`; approximately 2 MB. This is a checked site payload, not a completed hosting cutover; the runbook's access, backup, routing and activation prerequisites still apply.

## Final service-sector repetition cleanup — 14 October 2026

Removed the missed per-sector Noris/ComAp promotions, What to send us lists and Discuss work buttons from all three service disclosures. All 30 service scopes remain; Brand Partners and final Contact are shared once. Regression test first failed in each sector and now passes; browser confirms zero repeated action blocks. [Details and evidence](SERVICE-SECTOR-CLEANUP-2026-10-14.md). Published release [3aecf59](https://github.com/hakiimm8/arayaweb/commit/3aecf59c63a5e53bf56404fab648a031f1c11958); [Pages deployment](https://github.com/hakiimm8/arayaweb/actions/runs/38511742944) succeeded. Published homepage matches the artifact and all three sector-removal checks pass.

## Loading, counters and original branding — 14 October 2026

Investigated late pictures and recent animation delays. Added matching hero preloads/early low-priority small images; removed large-wrapper fades/delays. Added finite project/age counters, preserved Jakarta rollover, removed Leadership and changed tab branding. Traced owner company-profile artwork into sharp header/tab SVGs. Tests and independent review pass. See [diagnosis, decisions and verification](LOADING-COUNTERS-AND-BRANDING-2026-10-14.md). Published release [fe80362](https://github.com/hakiimm8/arayaweb/commit/fe80362574d96b1ec99cc1d8cae81e9f760cea15); [Pages deployment](https://github.com/hakiimm8/arayaweb/actions/runs/38509655085) succeeded. Fourteen deployed files return 200 and match the verified artifact.

## Simplified brand guides and motion — 14 October 2026

Owner-directed simplification removes repeated actions, task layers, cross-page promotion and extra menu choices. Noris has two visible product groups; ComAp Contents has Applications and Products. Added motion, removed logo pause controls, corrected labels/nav/office sentence, removed duplicate service equipment lists and added and many more. See [current decisions and verification](BRAND-SIMPLIFICATION-AND-MOTION-2026-10-14.md). Published release [b54d1fa](https://github.com/hakiimm8/arayaweb/commit/b54d1faeef1f1fa868c08ed2fc93f2f6989083f5); [Pages deployment](https://github.com/hakiimm8/arayaweb/actions/runs/38506164232) succeeded. All eleven deployed HTML/sitemap/style/script files return 200 and match the verified artifact. Earlier navigation descriptions below are historical.

## Brand content flow and Contents — 14 October 2026

Reviewed both long guides; added grouped detailed Contents and persistent return access. Noris task choices now precede the catalogue. All 18 ComAp applications, 14 total product families, diagrams and contextual enquiries retained. Local build, checks, five experience tests, automatic-year tests and independent review passed. See [findings and evidence](BRAND-CONTENTS-2026-10-14.md). Published release [612181c](https://github.com/hakiimm8/arayaweb/commit/612181cb62b6a613146359a656194f44c303252d); [Pages deployment](https://github.com/hakiimm8/arayaweb/actions/runs/38499051427) succeeded. All eleven published HTML/sitemap/style/script files return HTTP 200 and match the verified artifact.

## Single landing page and automatic years — 14 October 2026

Implemented one Araya landing page plus dedicated Noris/ComAp guides. Common requests removed; full services and enquiries are on the homepage. Legacy service bookmarks redirect to their matching anchors. Automatic company age/copyright follow Jakarta time, including New Year and resumed tabs. Company labels are Noris Group GmbH and ComAp a.s. Local/static/clock tests and independent review passed; see [implementation record](LANDING-AND-DATES-2026-10-14.md). Published release [dac0b92](https://github.com/hakiimm8/arayaweb/commit/dac0b92eac714fead13f1d2957faa0487d1b5b53); [Pages deployment](https://github.com/hakiimm8/arayaweb/actions/runs/38477724617) succeeded. All eleven published HTML/sitemap/script/style files checked return 200 and match the verified artifact. Earlier six-page content architecture below is historical.

## Approved copy decisions — 14 October 2026

Implemented owner selections and the follow-up certified wording. Age is 17 years in 2026. Marine has ten scopes; ComAp publishes eighteen applications. Preview-only visible footer text removed. See [Content decisions](CONTENT-DECISIONS-2026-10-14.md). Published release [c92ba45](https://github.com/hakiimm8/arayaweb/commit/c92ba4524cb85d2354bda8f8dd159478cbca7b93); [Pages deployment](https://github.com/hakiimm8/arayaweb/actions/runs/38475579209) succeeded. All six published HTML routes return 200 and match the local verified artifact. Earlier working-practices wording below is historical and superseded.

## Branch office correction — 14 October 2026

Removed Sidoarjo-based team wording. Added the owner-confirmed Sidoarjo and Jakarta (Townhouse PIK) branch offices to the shared contact details, About copy and structured locations. Exact Jakarta unit/street/postal details were not supplied. Release [ff94e52](https://github.com/hakiimm8/arayaweb/commit/ff94e522261fed5e63a1df2cd14d43ab4f5fd064) deployed successfully in [Pages run 38473939229](https://github.com/hakiimm8/arayaweb/actions/runs/38473939229). Published homepage returns 200, includes Townhouse PIK and omits the old team wording. Local six-page checks and structured-location assertions passed.

## Experience improvements — 14 October 2026

Implemented and verified professional company positioning, persistent inner-page navigation, contextual enquiries, contrast/type/disclosure fixes and additional motion. Certifications omitted at the owner’s request. Full change and evidence record: [Implemented improvements](IMPROVEMENTS-2026-10-14.md). Website-content release [921909b](https://github.com/hakiimm8/arayaweb/commit/921909bf355c1ec6454f63127ea26a12e378daa1) deployed successfully in [Pages run 38473028516](https://github.com/hakiimm8/arayaweb/actions/runs/38473028516). All six HTML routes and both shared assets return 200 and match local verified bytes. Hosted browser re-opening failed; visual/interaction evidence is local.

## Initial NORINET research — 9 October 2026 (historical)

Read and rendered both pages of the owner's supplied brochure; explained the onboard gateway, cloud monitoring, vessel/fleet dashboards, reports and integration. Recorded the printed V01.02 / October 2019 revision, compared it with the current manufacturer noriNet page, and saved suggested website wording and limits in [NORINET research](NORINET-RESEARCH.md). That initial research commit was documentation only. It is superseded by the implemented NORINET section recorded below.

Updated 9 October 2026, Asia/Jakarta. Historical session evidence; no ongoing monitoring or fresh production audit is implied.

## Reference-only content — 9 October 2026

Owner direction: the new site must not show Araya claims that the reference (live arayainternusa.co.id and the company profile PDF) does not make. Reviewed every statement on the home, marine, industrial and automation pages against both sources; details and the removed/kept lists are in [Content sources](CONTENT-SOURCES.md#reference-only-content-rule--9-october-2026).

- **Home:** feature strip, "Selected clients" sentence and trademark note removed (owner request). Hero, "What we do" and clients copy rewritten from the reference mission and "Partners Who Trust Araya Internusa" wording. Common requests now say "Fire alarm & monitoring" and "Generator systems". Schema description and `knowsAbout` follow the same terms.
- **Marine:** tank/cargo monitoring card removed (11 scopes). Scopes trimmed to reference wording; fire doors added.
- **Industrial / Automation:** scope descriptions trimmed to reference wording; design/commissioning claims removed.
- **Not changed:** layout and styling, apart from removing the strip and right-aligning the logo Pause button now that the note beside it is gone. Noris/ComAp manufacturer content and owner-supplied 1,500+, regions and WhatsApp kept.
- **Checks:** `build.py`, `check.py`, `node --check` passed. Screenshots of home, marine, industrial and automation at 1440px and 390px over local HTTP: no horizontal overflow, no console errors.

## Reproducible build — 9 October 2026

`tools/build.py` hashed the raw bytes of `site.css`/`site.js` for the `?v=` cache-bust query. On a Windows checkout (`core.autocrlf=true`) those files have CRLF line endings, so a rebuild changed the hash in all six pages without any content change. The hash now normalises CRLF to LF first; a Windows rebuild reproduces the committed pages byte for byte (`git status` clean, CSS `2e2316f7ac`). No page content, styling or behaviour changed. The "Current release" table below was also corrected to list the Automation page and the current scope counts.

## Content restructure — 9 October 2026

Deployed from `main` at [`541345c`](https://github.com/hakiimm8/arayaweb/commit/541345c62dee0caf8a15f0d7c3ae8ede2b389291) in [Pages run 37896406947](https://github.com/hakiimm8/arayaweb/actions/runs/37896406947), which succeeded. All six routes, `sitemap.xml` and the new assets return 200 on the published preview. The published logo strip loads all 14 images and animates at 1440px and 390px; it stays static with reduced motion.

Owner direction: keep the existing design, change content only; English only; show what Araya does and its clients instead of per-project case studies; present Araya as multi-brand, with Noris and ComAp as featured partners; keep the long brand guides but tidy their content; improve SEO. A redesign was trialled and rejected ("too mainstream"); none of it ships.

- **Home:** WhatsApp-first hero CTAs instead of brand buttons, and concrete feature strip (guarantee, specialist backup, one team). About now includes the founding story and leadership. The services section has three cards plus 12 "common requests" deep links. New Our Clients section (logos, 1,500+, regions), and brand partners plus a multi-brand equipment list.
- **Service pages:** Marine (12 scopes), Industrial (8) and the new Automation & Electrical page (12), each with an "equipment we work on" list, featured partner technology and an enquiry checklist.
- **Brand guides:** positive wording replaces internal caveats. Fixed enlarge-diagram accessible names and the diagram viewer's default source link.
- **SEO:** titles ≤60 characters; ProfessionalService/LocalBusiness schema with address and hours; BreadcrumbList, Service and FAQPage schema; 1200×630 JPEG share image; Twitter card; `sitemap.xml`. Preview remains `noindex, nofollow`.
- **Performance (no visual change):** the `js` class is now set inline, removing the mobile layout shift. Correctly proportioned logo file, responsive hero/card images and correct image dimensions.
- **Checks:** `python tools/check.py` passed (6 pages). Local screenshots at 1440px and 390px showed no overflow and no console errors. Local Lighthouse mobile: home 100/95/100/66, ComAp 99/96/100/66, CLS 0 (was 0.262). SEO 66 reflects intentional noindex.
- **Client logo strip (follow-up):** seven client logos from higher-quality sources scroll continuously, pause on hover, and have a Pause/Play button (WCAG 2.2.2). A static, wrapped row is shown when the visitor prefers reduced motion. All 14 logo images (two copies for seamless looping) load at 1440px and 390px; logos are not lazy-loaded because sideways-clipped images would not load. See CONTENT-SOURCES.md for sources.
- **Still open from the audit (design decisions deferred):** 9–11px text, orange-on-grey contrast and the "2009" badge contrast.

## Published baseline before 14 October improvements

- **Preview:** https://hakiimm8.github.io/arayaweb/
- **Website-content commit:** [`541345c62dee0caf8a15f0d7c3ae8ede2b389291`](https://github.com/hakiimm8/arayaweb/commit/541345c62dee0caf8a15f0d7c3ae8ede2b389291).
- **Deployment:** [Pages run 37896406947](https://github.com/hakiimm8/arayaweb/actions/runs/37896406947), succeeded.
- **Production:** https://arayainternusa.co.id/araya/ remains unchanged.
- **Design:** original Araya artwork and orange/charcoal/white Space Grotesk styling.
- **Publication:** only `public/`; all six pages intentionally `noindex, nofollow`.

The scope table below reflects the 14 October published implementation. The historical 541345c baseline above had twelve Marine scopes; the current release carries the reference-only eleven-scope version.

| Page | Implemented scope |
| --- | --- |
| [Home](https://hakiimm8.github.io/arayaweb/) | WhatsApp-first hero, founding story and leadership, three service cards with 12 common-request links, client logos (7 clients; desktop motion/mobile grid), owner-supplied 1,500+ total and Indonesian regions, featured partners plus multi-brand equipment list, contacts. |
| [Marine](https://hakiimm8.github.io/arayaweb/marine/) | 10 scope areas: alarms, safety, engines, generators, propulsion, navigation, automation, cranes, HVAC/refrigeration, and retrofit. Equipment list, featured partners, enquiry checklist. |
| [Industrial](https://hakiimm8.github.io/arayaweb/industrial/) | 8 scope areas: machinery, wire-cut/EDM, cutting, production machines, cranes, generators, electrical and automation. Equipment list, featured partners, enquiry checklist. |
| [Automation & Electrical](https://hakiimm8.github.io/arayaweb/automation/) | 12 scope areas: PLC, SCADA, instrumentation, panels, drives, motors, hazardous area, protection, power, earthing, gensets and electronics. Nine equipment groups, featured partners, enquiry checklist. |
| [Noris](https://hakiimm8.github.io/arayaweb/noris/) | Eight product areas: speed, temperature, pressure, instruments, signal processing, noriMos, noriStar and noriNet. Brand profile, product pictures in every family, applications, references, enquiry brief and FAQs. |
| [ComAp](https://hakiimm8.github.io/arayaweb/comap/) | 18 detailed applications across marine, power generation and smart energy, plus six product areas: engine control, paralleling/load sharing, marine PMS, single-generator control, InteliSCADA and WebSupervisor. Brand profile, product pictures in every family, applications, references, enquiry brief and FAQs. |

WhatsApp is owner-supplied +62 81326396262, linked as https://wa.me/6281326396262. No enquiry message was sent during checks.

## Release history

The initial entries were recorded on 8 October 2026; subsequent navigation work is listed below them. Commits/runs identify the evidence more precisely than inferred times.

| Commit | Change | Deployment evidence |
| --- | --- | --- |
| `1102b80` → `a0a1dc6` | Existing-style homepage and initial brand pages; accessible orange contrast and sticky navigation correction. | [37751836932](https://github.com/hakiimm8/arayaweb/actions/runs/37751836932), succeeded for `a0a1dc6`. |
| `1f771a3` | Initial public audit/handoff documentation. | Documentation update; page-content baseline unchanged. |
| `c5dcb49` | Owner WhatsApp added to shared contact section. | [37754660622](https://github.com/hakiimm8/arayaweb/actions/runs/37754660622), succeeded. |
| `1465575` | Noris instruments/sensors; ComAp engine control/PMS/load sharing; owner project count and geography. | [37756296482](https://github.com/hakiimm8/arayaweb/actions/runs/37756296482), succeeded. |
| `2b45cc4` | Recreated SVG logo. **Rejected by owner and superseded; do not restore.** | [37775308617](https://github.com/hakiimm8/arayaweb/actions/runs/37775308617), succeeded historically. |
| `5495ed6` | Original transparent logo restored unchanged, original lockup proportions corrected; rejected SVG removed. | [37778054483](https://github.com/hakiimm8/arayaweb/actions/runs/37778054483), succeeded. |
| `7f169d7` | Marine/industrial pages, homepage scopes, initial product portfolios/images, CSS content-hash URL. | [37781023786](https://github.com/hakiimm8/arayaweb/actions/runs/37781023786), succeeded. |
| `e866993` | Researched dedicated brand guides, product indexes, profiles, applications, enquiry briefs and accessible FAQs. | [37782440114](https://github.com/hakiimm8/arayaweb/actions/runs/37782440114), succeeded. |
| `b34794b` | Consolidated documentation index, release history and current-state notes. | Documentation-only; public artifact unchanged. |
| `030a205` | Separate Noris/ComAp header links and homepage buttons. Header arrangement superseded by the following owner request; separate homepage buttons retained. | [37866938106](https://github.com/hakiimm8/arayaweb/actions/runs/37866938106), succeeded; published navigation checks passed. |
| `f19cc41` | noriNet remote vessel/fleet monitoring, official dashboard and zoomable architecture diagram, flow explanation, selection inputs and FAQ. | [37880869568](https://github.com/hakiimm8/arayaweb/actions/runs/37880869568), succeeded; published checks passed at 1280/390/360px. |
| `c37c534` | Ten additional application diagrams (13 total) and accessible fit/zoom viewer, with native original-image fallback. | [37879114243](https://github.com/hakiimm8/arayaweb/actions/runs/37879114243), succeeded; published diagram/viewer checks passed. |
| `52d954e` | Detailed ComAp application guide: 19 explanations, three system diagrams, application-first navigation and expandable sections. | [37878202684](https://github.com/hakiimm8/arayaweb/actions/runs/37878202684), succeeded; published application checks passed. |
| `de91d39` | Eleven new manufacturer images; all 13 brand product sections illustrated, credited and lazy loaded. | [37868242535](https://github.com/hakiimm8/arayaweb/actions/runs/37868242535), succeeded; published desktop/mobile image checks passed. |
| `b51bc47` | Brand Partners dropdown containing separate Noris/ComAp links; header/footer links generated from shared brand data. | [37867253415](https://github.com/hakiimm8/arayaweb/actions/runs/37867253415), succeeded; published dropdown checks passed. |

The early navy design concepts and two generated logo attempts were not used in the current site. Preserve the restored original symbol and lettering.

## Verification evidence

| Check | Recorded result |
| --- | --- |
| Build/static audit | `python tools/build.py` and `python tools/check.py` passed; five routes, local assets/fragments, metadata, one H1, alt text, font, publication exclusions and no-PR workflow checked. |
| JavaScript / whitespace | `node --check public/assets/site.js` and `git diff --check` passed on the website release. |
| Brand layouts | Local and published pages checked at 1280×900 and 390×844 in separate headless Edge via bundled Playwright; Browser plugin/skill unavailable. |
| Runtime/assets | No page/console/HTTP errors, broken images or horizontal overflow observed in the final brand checks. Original logo and product photographs loaded. |
| Interaction | Homepage → Noris → ComAp passed; product-index anchors reached content below sticky header; FAQs opened/closed with Enter; WhatsApp destinations matched owner number. |
| Correction | Mobile application text initially occupied a narrow column. Grid placement fixed; repeat checks confirmed readable 299px content width at 390px. |
| Earlier service release | All five routes checked at desktop/mobile widths; homepage → marine → ComAp and mobile menu Escape closing passed. |
| Brand Partners dropdown | Local and published checks across all five routes at 1280px, 1024px and 390px passed: destinations, opening by click/Enter, Escape focus return, outside-click closing, mobile close after navigation, independent homepage buttons and no-JavaScript navigation. No overflow/page/console/HTTP errors. |

Local evidence is retained as `brand-guides-published-{noris,comap}-{1280,390}.png` and corresponding product/application/FAQ screenshots. Earlier five-route evidence uses `project-details-published-`. Full local verification notes and scripts are retained by the owner, outside this repository.

Latest navigation screenshots use `brand-dropdown-published-{1280,1024,390}.png`. The owner selected Brand Partners for future expansion; Noris and ComAp remain individual entries and dedicated pages. Native details/summary supplies the dropdown, with scripted closing/focus behaviour. JavaScript URLs now include a content hash as well as CSS URLs. Follow [Brand maintenance](BRAND-MAINTENANCE.md) to add a future partner; homepage featured cards are maintained separately.

## Evidence limits and open work

- Original production Lighthouse lab baseline: performance mobile 37/desktop 76; SEO 83 on both. Raw reports were not retained. No new production speed or ranking measurement is claimed.
- Static preview checks do not validate WordPress/Elementor editing, PHP/database behaviour, mail delivery, calling, production hosting or every browser/viewport.
- Distributor relationship, 1,500+ project total and geographic coverage are owner statements. Product portfolios are manufacturer examples, not confirmed stock, blanket approvals, exclusivity or completed Araya installations. Exact sources and image provenance are in [Content sources](CONTENT-SOURCES.md).
- Before production rollout: review copy/product scope, contact delivery and image permissions; establish verified backup and administrator/database access; apply selected content/settings changes; address demo URLs, metadata/schema/sitemap, contact destinations and performance findings from [Project notes](PROJECT-NOTES.md).
- Keep `/araya/` for the first release; review redirect or domain-root migration separately. Rerun comparable production audits and retain reports after deployment.

## Maintenance and publishing

Edit shared pages in `tools/build.py`, researched brand data in `tools/brand_profiles.py`, brand rendering in `tools/brand_pages.py`, styling in `public/assets/site.css` and menu behaviour in `public/assets/site.js`. Rebuild generated HTML after source changes. Manufacturer image refetch is optional via `tools/fetch_brand_assets.py`.

Validate the changed desktop/mobile flow, then publish the preview by pushing the reviewed change to `main`. Pages deploys on default-branch pushes or manual dispatch; no `pull_request` or `pull_request_target` triggers. Documentation-only pushes can redeploy the same public artifact. Record website-content commit separately from later documentation commits. Never include skip-CI instructions in merge commits.

For a preview rollback, revert the unwanted site commit on `main`, push, and verify the resulting Pages deployment. Select a known accepted release; the recreated-logo commit is rejected. Production rollback is separate and requires its own verified files/database backup.

After each change, update this record with request, sources, decision, affected routes/files, checks, defects/corrections, commit/run and pending work. Keep historical entries labelled when superseded.


## Product pictures — 9 October 2026

Owner requested more pictures on the Noris and ComAp pages. Added six Noris assets (marine temperature probes, pressure transmitter, noriMeter instrument, signal-processing devices, noriMos display and noriStar controls) and five ComAp assets (InteliDrive 700 Marine, InteliGen 1000 Marine, InteliLite 4 AMF 25, InteliSCADA and WebSupervisor). Each of the 13 product families now has a captioned, manufacturer-linked picture; the existing speed-sensor and InteliGen 500 G2 hero assets are reused in their product sections. New WebP assets total 285,534 bytes; below-hero images use lazy loading, async decoding, explicit dimensions and contain fit. Existing design, original logo, menu, contacts and preview noindex retained.

Local static/build/JavaScript/whitespace checks passed. Headless Edge via bundled Playwright checked both brands at 1280×900 and 390×844: all 26 product figure checks loaded, intrinsic dimensions matched, alt text and linked credits present, contain fit and lazy loading applied, no overflow or page/console/HTTP errors. Brand Partners navigation and keyboard Escape focus return passed. Screenshot review confirmed readable desktop/mobile product layouts. Local evidence: `brand-pictures-local-*.png`, `brand-pictures-local.json`, `check-brand-pictures.cjs` and manufacturer contact sheet, retained outside the public repository. Published release verification is recorded in the current-release entry when deployed. No new Lighthouse measurement or performance-score improvement is claimed.

Published verification: Pages run 37868242535 succeeded for de91d39. The same image checks passed on GitHub Pages at 1280x900 and 390x844: 26 loaded figures, correct dimensions/alt/source credits, no overflow or runtime/HTTP errors, and Brand Partners navigation/focus passed. Evidence: `brand-pictures-published-*.png` and `brand-pictures-published.json`, stored locally.


## Detailed ComAp applications — 9 October 2026

Owner requested application detail following screenshots of the ComAp Applications menu. Added an application guide before products: Marine (4), Power generation (10, including a dedicated synchronisation/load-sharing explanation) and Smart energy management (5). All 19 explanations have a purpose, typical system, control functions, example families, enquiry inputs, related anchors and a manufacturer source. Added three credited manufacturer system diagrams (128,048 bytes), full-size links, group navigation, native expandable sections, and application hash opening. Existing Araya style/logo, product photos, contact destinations, partner menu and preview noindex remain.

Sources and scope distinctions are in COMAP-APPLICATIONS.md. Spot Price Dispatch is explicitly identified as currently available in Australia and Singapore, not offered as an Indonesian tariff service. Specialist applications are manufacturer portfolio examples, not additional Araya project-history, certification or inventory claims.

Local build/static audit, JavaScript syntax and whitespace passed. Browser checks in headless Edge via bundled Playwright passed at 1280x900, 768x900, 390x844 and 360x844: all 76 application instances opened/closed by keyboard, four explanation fields each, group navigation, direct hashes, related application opening, product CTA, owner WhatsApp destination, three loaded diagrams with correct dimensions, larger-image tabs and no horizontal overflow or page/console/HTTP errors. Native application expansion also passed with JavaScript disabled. Existing Noris/ComAp product-image and Brand Partners navigation/focus checks passed at 1280/390px. Visually inspected desktop/mobile hero, marine overview, PMS and BESS explanations. Local evidence prefix: comap-applications-local-; source JSON and scripts/screenshots retained outside this repository. No Lighthouse or production ranking remeasurement was performed.

Published application release: 52d954e04a60c6442b7e9408594a41779640c30d deployed successfully in Pages run 37878202684. Repeat application QA passed on GitHub Pages at 1280/768/390/360px: all 19 entries per width, keyboard expansion, group/deep/related/product links, diagram dimensions and full-size views, WhatsApp, no overflow/runtime/HTTP errors and native expansion without JavaScript. Evidence prefix comap-applications-published-. Static public-doc links also passed.


## Expanded diagrams and viewer — 9 October 2026

Owner requested the manufacturer diagrams, supplying the marine AC PMS screenshot. Added ten contextual diagrams alongside the three existing group drawings: marine DC/hybrid power, shore connection, auxiliary engine, mechanical/electric propulsion, prime power, off-grid hybrid, CHP, fuel cells and BESS. The thirteen diagrams are unchanged official WebP images, credited and linked to source pages. New assets total 398,948 bytes; inline images are lazy loaded with explicit dimensions and descriptive alt text.

Added a native dialog with Fit, 100–300% zoom, image scrolling, source/title display, Close/Escape/backdrop handling, background scroll lock and keyboard focus return. Image links remain usable without JavaScript. Application explanations and original Araya styling/photography/logo are retained. Sources and viewer maintenance are documented in COMAP-APPLICATIONS.md and BRAND-MAINTENANCE.md.

Local static/build/JavaScript/whitespace checks passed. Existing application checks passed at 1280/768/390/360px and product-picture/Brand Partners checks at 1280/390px. Diagram QA covers all thirteen images at 1280/390/360px: loading, title/source binding, fit dimensions, zoom limits and reset, scrolling, focus containment, Close/Escape/backdrop, scroll unlock and focus return. No JavaScript fallback opens the local image in a new tab. No page/console/HTTP errors or page overflow observed. Two pre-publication defects were reproduced and corrected: Fit initially constrained only width for tall diagrams (BESS image 651px vs 588px available), and browser Tab traversal temporarily moved to the document body at the modal boundary. Fit now includes height and explicit Tab wrapping retains focus. Local evidence prefix diagram-viewer-local-, updated application evidence comap-applications-diagrams-local.json, and diagram-regression.json; screenshots/source contact sheet retained outside the public repository. No Lighthouse or production SEO score is claimed.

Published diagram release c37c5342309f7fafbf0371aeb5672d9088c43f24 deployed successfully in Pages run 37879114243. Repeat checks passed on GitHub Pages for all thirteen diagrams at 1280/390/360px: loading/source/title, fit within height and width, zoom limits/reset, scroll, focus containment/return, Close/Escape/backdrop and no-JavaScript original-image fallback. No page overflow or page/console/HTTP errors. Evidence prefix diagram-viewer-published-. Public local-document links passed.


## NORINET implementation — 9 October 2026

Added noriNet as Noris's eighth product area: manufacturer dashboard picture, full-width vessel-to-shore architecture diagram, collection/interface/cloud flow, MQTT telemetry and VPN service explanation, selection inputs, application anchor and noriMos comparison FAQ. The shared diagram viewer now attributes the selected brand correctly. Two unchanged manufacturer WebP assets total 91,210 bytes; no owner PDF is publicly redistributed.

Local checks passed in headless Edge at 1280/390/360px: finder/anchor, both images and actual dimensions, Fit/zoom/scroll, keyboard focus containment and Escape return, Close, FAQ, owner WhatsApp, no-JavaScript image fallback, ComAp source-credit regression, and no runtime/HTTP errors or horizontal overflow. Static build/check and JavaScript syntax passed. Source and historical brochure-version details are in NORINET-RESEARCH.md. Website-content commit f19cc41c7c599d42f6d2b165aa19822d1baf9594 deployed successfully in Pages run 37880869568. The same NORINET checks passed on the published site at 1280/390/360px, including both brand credits and the no-JavaScript fallback. Evidence prefix: norinet-published-.
