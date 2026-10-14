# SEO review: new Araya design, brand pages and services

Historical audit baseline. On 15 October the owner selected authorised distributor and approved implementation of other improvements. See [implemented changes and remaining inputs](SEO-IMPROVEMENTS-2026-10-15.md); the ratings and content measurements below describe the pre-improvement version.

Reviewed 14 October 2026, Asia/Jakarta. Source: `1772a6f0046862780dbf221f4b887083c11f0794` (website content release `d6235ea`). This is an analysis; no website copy, metadata, indexing setting or hosting configuration was changed.

## 1. Scope and limits

Inspected the published GitHub Pages homepage, Noris and ComAp pages; their source HTML, links, assets and structured data; and a freshly built production candidate. Compared the current WordPress homepage at `https://arayainternusa.co.id/araya/`. Checked manufacturer partner/contact sources and current Google documentation.

The new design is **not live on the company domain**. The company root and the tested `.com` address currently resolve to the existing WordPress site. All three GitHub preview pages intentionally use `noindex, nofollow`. Their content can be assessed, but they should not be expected to rank. The production candidate has `index, follow`, company-domain canonicals and a three-page sitemap. These settings still need verification after live deployment. [Google: noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing).

No Search Console, Business Profile, analytics, query-volume or backlink database was connected for this review. Search-result observations are not a ranking survey. No claim of top positions, monthly demand, domain authority or measured conversions is made.

PageSpeed API returned HTTP 429. No new Lighthouse/Core Web Vitals score is available. The 9 October lab scores belong to an older release and are not reused as current results. Asset sizes below are source-byte inventories, not measured transfer sizes, page-load times or real-user performance.

## 2. Manual readiness score

These are subjective checklist scores for the **new production candidate's SEO preparation**, not Google/Lighthouse scores or forecasts of ranking. Actual preview indexing is intentionally disabled. Unmeasured performance, traffic and backlink authority are excluded.

| Criterion | Maximum | Araya home | Noris | ComAp |
| --- | ---: | ---: | ---: | ---: |
| Crawlable HTML, working links/assets, metadata infrastructure | 20 | 18 | 18 | 18 |
| Title and snippet targeting | 15 | 5 | 7 | 7 |
| Match to commercial search intent | 20 | 11 | 13 | 14 |
| Useful, distinct subject content | 20 | 10 | 15 | 16 |
| Company identity and published evidence of its role | 15 | 9 | 7 | 7 |
| Internal navigation and enquiry journey | 10 | 8 | 8 | 8 |
| **Total / 100** | **100** | **61** | **68** | **70** |

The strongest part is the technical foundation. The largest gaps are generic titles, insufficient emphasis on Araya's supplier role, very short service explanations and limited published project/appointment evidence. Brand scores are higher because they have relevant product families, application explanations and diagrams. ComAp's larger scope is useful but can also dilute the marine/engine/generator purchase intent.

## 3. Technical and on-page findings

| Area | Finding | Assessment/action |
| --- | --- | --- |
| Fetching | All three published preview pages return HTTP 200. | Pass for availability. This does not establish Google indexing. |
| Rendering | Primary text, headings and all service/application details are already in HTML. | Good: content does not need a click or API fetch to exist. |
| Indexing | Preview is noindex/nofollow; production candidate is index/follow. | Correct separation. Publish the production target, then inspect real responses. |
| Canonicals | Each production content page canonicalises to its own company-domain route. | Good. Also resolve `/index.html`, slash, HTTP/HTTPS and hostname variants with a coherent redirect strategy. |
| Sitemap/robots | Production candidate sitemap contains `/`, `/noris/`, `/comap/`; its robots advertises that sitemap. | Good candidate. The currently tested company-root `/robots.txt` and `/sitemap.xml` return 404. This does not prove that no subdirectory/plugin sitemap exists. A robots 404 is not itself an indexing block. |
| Titles | `Home - PT Araya Internusa`, `Noris - PT Araya Internusa`, `ComAp - PT Araya Internusa`. | Unique but commercially weak. Title lengths of 25–26 characters are not the problem; omitted subject/supplier information is. |
| Descriptions | Unique descriptions: 132, 149 and 155 characters respectively. Brand descriptions already say distributor in Indonesia. | Good baseline. Descriptions should explain actual supply/engineering scope; Google can select another snippet. No fixed character count guarantees appearance. |
| Headings | One H1 per new page, with semantic section/group/item hierarchy. | Good. Brand H1s identify technology but not Araya's distributor role. Make the opening copy unmistakable without restoring the owner-removed INDONESIA company-label suffix. |
| Service disclosures | All 30 scope descriptions remain in HTML and in mobile layout. | Keep the clean design. Accordions are not inherently an SEO defect. [Google mobile content guidance](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing). |
| Page architecture | Services share the homepage; old service routes are compatibility redirects. | Consistent with the owner's single-landing-page choice. Individual hashes do not provide independent titles/metas/canonicals. The homepage can rank for multiple terms, but targeting is less focused than distinct useful service documents. |
| Internal links | Shared navigation/footer link to both brand routes; brand Contents links to products/applications; local asset/fragment validator passes. | Good. No need to restore repeated CTAs or shortcut blocks. Relevant service-to-product context can be conveyed in concise prose. |
| Structured data | ProfessionalService/company details; three homepage Service nodes; brand BreadcrumbList and FAQPage. | Useful infrastructure; JSON parses and production URLs pass checks. No live Rich Results Test or Search Console validation was performed. Do not treat schema as proof of authorisation or a ranking guarantee. |
| FAQ expectation | Brand FAQs are useful human explanations. | Google reports FAQ rich results discontinued from May 2026. FAQ markup is not a current rich-result opportunity. [Google changelog](https://developers.google.com/search/updates#may-2026). |
| Images | New home has alt and width/height on all 24 image elements, including repeated client logos. Brand content images have descriptive alt/dimensions; each page's dimensionless image is the on-demand diagram viewer placeholder. | Good. No need to stuff place/brand keywords into every portrait or decorative image. |
| Language | English-only content, `lang="en"`; no Indonesian equivalent/hreflang. | Opportunity for Indonesian query intent, not a technical penalty. Consider separate `/id/` versions if scope expands; avoid hidden keyword lists. [Google multilingual guidance](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites). |
| Local identity | Sidoarjo/Jakarta, supplied addresses, phone, WhatsApp, email and hours are present; company schema includes locations. | Good website foundation. Business Profile ownership, categories, reviews and directory consistency remain unverified. Do not invent a Jakarta street/unit or use geographic wording that conflicts with the owner voice. |
| Measurement | No GSC/analytics evidence reviewed. | After launch, track brand/service queries, indexed canonical pages and enquiry conversions. Use actual query data to prioritise additional content. |

## 4. What improved over the current WordPress site

Fresh HTML inspection of the old homepage finds no H1, an automatically assembled long description, and only one body mention each of Noris and ComAp. It contains a general Certified and Authorized Partner claim, without a brand-specific appointment explanation. Of 42 image elements, 31 have missing/empty alt and 23 lack explicit dimensions; decorative images require individual review rather than assuming all 31 need descriptive text.

The new design adds dedicated brand documents, clear company/service headings, contextual products and diagrams, consistent contact details and relevant image alternatives. Its homepage HTML is approximately 27KB versus approximately 346KB for the fetched WordPress homepage, before compression. This is evidence of a leaner document, not a speed score.

Source inventory for the new design:

| Page | Approximate text words including navigation/footer | Default early-image source bytes |
| --- | ---: | ---: |
| Home | 930 | 567,092 |
| Noris | 1,189 | 236,816 |
| ComAp | 2,913 | 312,312 |

Responsive candidates, caching, compression and viewport change actual transfer. Shared CSS is about 59KB, site JS 12.5KB, date JS 1.5KB and the font 22KB. These are useful engineering checks; they do not establish current LCP/INP/CLS. [Google CWV guidance](https://developers.google.com/search/docs/appearance/core-web-vitals).

## 5. Distributor and authorised-partner search intent

### Current gap

Each brand description includes “distributor in Indonesia”, but each brand's visible body says “distributes” once; there is no clear visible distributor heading or introductory commercial proposition. Its H1 and title present a technology guide. Google can understand related word forms, so the absence of the exact noun is not an exact-match requirement. The practical problem is whether a buyer can quickly recognise **Araya's role, location, supply scope and engineering capability**.

Manufacturer history should support the page after that company proposition. Add two or three concise sentences focused on the actual Araya offer, then retain the existing application/product explanations and final contact section. No per-item CTAs are needed.

### Recommended targets and draft metadata

| Page | Primary query theme | Supporting themes | Proposed title |
| --- | --- | --- | --- |
| Home | Marine and industrial automation services Indonesia | ship electrical repair, control-system retrofit, industrial machinery service | Marine & Industrial Automation Indonesia \| Araya Internusa |
| ComAp | ComAp distributor Indonesia | supplier ComAp, controller genset ComAp, InteliGen, InteliLite AMF, synchronisation/sinkronisasi genset, load sharing, marine PMS | ComAp Distributor Indonesia \| Engine & Power Control \| Araya |
| Noris | Noris distributor Indonesia | supplier sensor Noris, speed/RPM sensors, temperature/pressure instruments, noriMos AMS, noriStar, noriNet | Noris Distributor Indonesia \| Sensors & Automation \| Araya |

Suggested ComAp introduction: **“PT Araya Internusa distributes ComAp controllers in Indonesia, with engineering support for engine control, generator synchronisation, load sharing and power management.”**

Suggested Noris introduction: **“PT Araya Internusa distributes Noris instruments, sensors and marine automation systems in Indonesia, supported by professional engineering experience and international technical backing.”**

These use the owner's distributor statement. They are drafts, not implemented changes or independently verified appointment assertions. Descriptive concise titles are preferable to generic Home/brand-only labels; avoid repeating variants merely to force keywords. [Google title guidance](https://developers.google.com/search/docs/appearance/title-link).

### “Authorised” is a specific relationship, not another spelling of distributor

- Use **authorised distributor**, **authorised partner**, **service partner** or **system integrator** only according to the current appointment's actual designation, brand, territory, product scope and validity. A general certification claim does not establish that brand relationship.
- British **authorised** and American **authorized** are both valid. “Authorise partner” is not the correct label. There is no reason to repeat both spellings for SEO.
- Do not claim sole/exclusive/national exclusivity without evidence. A different distributor or a manufacturer subsidiary does not rule out Araya's own appointment.
- The reviewed [Noris worldwide partner directory](https://www.noris-group.com/company/locations/our-partners-worldwide) does not show Araya or an Indonesia entry in its returned text. The reviewed [ComAp contact directory](https://www.comap-control.com/contact/) does not name Araya. The ComAp page primarily lists group offices, so absence there is especially inconclusive. No current Araya appointment was independently confirmed in these sources; no finding of non-authorisation is made.
- ComAp's official [Indonesia subsidiary announcement](https://www.comap-control.com/insights/comap-opens-a-new-subsidiary-in-indonesia/) states a Jakarta subsidiary was launched in October 2025. Commercial positioning should make Araya's own engineering/supply value clear, without implying Araya is ComAp's headquarters or only Indonesian channel.
- If an appointment exists, a current manufacturer listing linking to Araya and a publishable appointment statement would improve both buyer trust and verifiable entity connections. Supplier shipments or a company-supplied claim alone do not prove authorised status.

## 6. Services: content and keyword assessment

All 30 listed scopes have explicit headings. Their individual descriptions are only 5–14 whitespace-separated words each. They communicate breadth, but offer little distinctive explanation of faults, work performed, deliverables, project constraints or completed outcomes. There is no minimum SEO word count: expand only where useful to buyers.

Maintain the single landing page. Strengthen selected high-value scope descriptions in the existing disclosures and include genuine project evidence when available. Priorities below are editorial/business-intent judgements, not search-volume research. “Present—brief” means the topic exists but is not supported by a dedicated, in-depth service document.

| Sector | Existing scope | Suggested query theme (not volume-validated) | Current support |
| --- | --- | --- | --- |
| Marine | Fire alarm, general alarm & monitoring | Fire alarm kapal; ship alarm and monitoring repair | Present—brief (14 description words) |
| Marine | Engine safety devices | Engine safety system kapal; engine alarm/protection service | Present—brief (13 description words) |
| Marine | Engines & engine monitoring | Marine engine repair; engine control repair kapal | Present—brief (14 description words) |
| Marine | Generator systems | Generator kapal; marine generator repair and control | Present—brief (14 description words) |
| Marine | Manoeuvring, CPP & bow thrusters | Manoeuvring control, CPP and bow-thruster service | Present—brief (7 description words) |
| Marine | Navigation & public address | Autopilot / gyro compass service; marine public address | Present—brief (7 description words) |
| Marine | Electrical panels, PLC & SCADA | Marine electrical panel; PLC / SCADA kapal | Present—brief (11 description words) |
| Marine | Deck cranes & deck machinery | Deck crane repair; cargo/deck machinery service | Present—brief (9 description words) |
| Marine | AC & refrigeration systems | AC kapal; marine refrigeration repair | Present—brief (9 description words) |
| Marine | Retrofit of obsolete systems | Marine automation retrofit; obsolete system replacement | Present—brief (13 description words) |
| Industrial | CNC lathes & milling machines | Jasa service mesin CNC; CNC lathe/milling repair | Present—brief (10 description words) |
| Industrial | Wire-cut & EDM machines | Service wire-cut / EDM; industrial machine repair | Present—brief (8 description words) |
| Industrial | NC gas & plasma cutting | NC gas / plasma cutting machine service | Present—brief (9 description words) |
| Industrial | Hobbing, casting & moulding | Hobbing / continuous-casting / moulding machine repair | Present—brief (11 description words) |
| Industrial | Crane supply & repair | Service crane industri; overhead / portal crane repair | Present—brief (14 description words) |
| Industrial | MV/LV generators | MV / LV generator service; generator industri | Present—brief (8 description words) |
| Industrial | Panels & motor controls | Industrial panel / motor-control repair | Present—brief (11 description words) |
| Industrial | PLC, HMI & instrumentation | Industrial PLC / HMI / instrumentation service | Present—brief (8 description words) |
| Automation & Electrical | PLC & software | Jasa programming PLC; PLC replacement / retrofit | Present—brief (11 description words) |
| Automation & Electrical | SCADA & HMI software | SCADA / HMI integration and software service | Present—brief (9 description words) |
| Automation & Electrical | Process control & instrumentation | Process instrumentation and control service | Present—brief (7 description words) |
| Automation & Electrical | Panels, switchboards & MCC | Panel listrik, switchboard and MCC service | Present—brief (14 description words) |
| Automation & Electrical | Soft starters & VFDs | VFD / inverter and soft-starter service | Present—brief (5 description words) |
| Automation & Electrical | Electric motors | Electric motor service; motor listrik industri | Present—brief (5 description words) |
| Automation & Electrical | Hazardous-area apparatus | Hazardous-area electrical equipment service | Present—brief (5 description words) |
| Automation & Electrical | Electrical protection | Protection relay service; electrical protection | Present—brief (14 description words) |
| Automation & Electrical | Transformers, UPS & chargers | Transformer / UPS / battery charger service | Present—brief (6 description words) |
| Automation & Electrical | Surge protection, earthing & PFC | Earthing, surge protection and power-factor correction | Present—brief (12 description words) |
| Automation & Electrical | Generators & generating sets | Genset / generating-set service | Present—brief (5 description words) |
| Automation & Electrical | Electronic card repair | Industrial electronic-card repair; repair PCB industri | Present—brief (8 description words) |

### Owner-mentioned services not clearly represented in the current homepage

- **Engine overhaul:** engine repair is present, but overhaul is not explicitly explained.
- **AMS:** generic alarm/monitoring appears at home and noriMos/AMS is stronger on Noris; the homepage could name alarm monitoring systems naturally.
- **Water-level monitoring:** no specific homepage service explanation.
- **Cargo monitoring system:** no specific homepage service explanation.
- **Steering:** manoeuvring/CPP/bow thrusters are present; steering service is not separately named.
- **Generator synchronisation and automatic start/stop:** strong ComAp explanations, but generic generator service descriptions on the homepage do not clearly connect to those project scopes.

These came from the owner's earlier list. Confirm the current scope and add factual wording where applicable; do not quietly widen the offer based on a manufacturer's full application catalogue. Existing ComAp examples should remain clearly identified as manufacturer applications, not evidence of Araya installations.

## 7. Trust, off-page and migration

The client logos, leadership portraits, founding year and owner-reported 1,500+ projects support identity. Add a few permission-cleared project examples with equipment/system, problem, Araya scope and outcome. Exact certifications are still unspecified; do not invent badge names or imply class/product approvals from general company certification.

No broad backlink audit was conducted. Prioritise relevant manufacturer, customer, shipyard and industry references. Buying generic links or creating thin city keyword pages is not recommended.

Before root deployment, map the actual old WordPress service/about/contact URLs to their equivalent new content. Relevant consolidated services can redirect to the new homepage/section; removed unrelated demo/shop/blog pages should not all redirect blindly to Home. Use permanent server redirects where possible and verify the new canonical, indexability and sitemap. [Google migration guidance](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes).

The tested `.com` address already redirects to the current `.co.id/araya/` endpoint. Fresh check supports redirect consistency today, rather than claiming two live duplicate homepages based on older search snippets. Audit www/non-www and HTTP variants at cutover. No Change of Address is needed merely for moving `/araya/` to `/` within the same domain.

## 8. Priorities

1. **Before launch:** improve the three titles and brand opening propositions; confirm the exact appointment terms before any authorised claim; finalise old-to-new URL mapping and verify the production target after activation.
2. **Next content pass:** improve generator synchronisation/AMF, AMS, engine work, PLC/SCADA, panels and retrofit explanations; resolve the missing owner-mentioned scopes. Preserve the existing visual simplicity.
3. **Trust:** add a small number of real case studies and exact credentials when available; secure relevant manufacturer/industry references.
4. **After launch:** connect/verify Search Console and Business Profile, submit the production sitemap, inspect canonicals and measure queries/leads. Obtain fresh mobile performance evidence.
5. **If Indonesian acquisition matters:** consider professionally translated Indonesian versions with their own URLs and appropriate language annotations. Additional dedicated service pages are optional future work only if useful content and query evidence justify them; they are not a prerequisite for keeping the approved landing-page design.

Raw HTML, headers, parser output, asset inventories and the PageSpeed 429 response are saved privately in the owner's docs under `evidence/seo-20261014/`. JSON schema parsing and the repository production validator passed; passing those tests does not prove Google rich-result eligibility or ranking.
