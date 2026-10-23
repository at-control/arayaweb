# Google Ads Preparation Plan — PT Araya Internusa

**Status:** audit and proposal for review; implementation and campaign launch are not authorised by this document.  
**Audit date:** 21 October 2026, Asia/Jakarta.  
**Primary domain:** https://arayainternusa.co.id/  
**Repository:** https://github.com/hakiimm8/arayaweb  
**Source inspected:** local `main`, commit `f4a3803d438ba0ff0d0b909bacba5c9bf23042cc`.

At completion of the **21 October planning audit**, only this document had been added to the repository. No production files, tracking tags, hosting settings or advertising accounts had been changed; no campaign or deployment had been created or triggered, and nothing had been pushed. Subsequent authorised account-setup progress is recorded below. A push to `main` currently triggers preview checks and automatic production promotion, so this document remains saved locally for review.

### Follow-up — 22 October 2026

- The owner initially reported no existing Ads, GA4 or GTM setup. Edge inspection subsequently confirmed a cancelled legacy Google Ads account under the owner's chosen Google login; its existing advertising belongs to a different business and must not be reactivated or repurposed for Araya.
- The owner explicitly authorised starting a **new Google Ads account** under that login and permitted Edge inspection/control. This is an extension to the original planning-only scope for account setup; it does not authorise campaign creation/launch, advertising spend, production changes or deployment.
- The owner clicked Google's **Create New Account** confirmation. Google Ads customer ID **115-719-0739**, named **PT Araya Internusa**, was verified in the account dashboard. The Campaigns page explicitly reported the account active, with no enabled campaigns and **0 drafts in progress**. GA4 and GTM creation took place subsequently, as recorded below.
- Entered **PT Araya Internusa** and `https://arayainternusa.co.id/` instead of the unrelated prefilled business/profile. Replaced Google's generated business description with the confirmed engineering scope, removed robotics, boats/watercraft and maritime-freight suggestions, and added industrial automation services. The business-information step has now advanced.
- Used **Skip** for optional Google-product connections rather than confirming the preselected Business Profile and YouTube channel. The phone field displayed Araya's published `(031) 7877990`. Final linked-product state should be checked in the completed account; skipping a setup step is not evidence of every underlying account link.
- Found and selected **Set up an account only** on the advertising-goal screen. The confirmation screen showed **Indonesia**, **(GMT+07:00) Jakarta Time** and **Indonesian Rupiah (IDR)**. The owner subsequently completed the remaining setup and reported payment done; the account dashboard is now accessible. No payment details were entered by the agent.
- Fresh billing-summary inspection after that report shows **Available funds: IDR0**, **Payments: IDR0** for October, and **You haven't made any payments yet** under Last payment. Account setup completion is verified; receipt/settlement of money is not. Do not claim a funded account, invent a payment amount or ask the owner to pay again without checking whether they completed billing details only or actually transferred funds.
- Google's final setup screen generated Ads Google tag **AW-18531101906**. It has not been installed on the website. The embedded Tag Manager interface is not evidence that a dedicated GTM web container or GA4 property has been configured. Production code, tracking deployment and advertising launch remain outside the authorised scope.
- The owner explicitly excludes YouTube advertising. The existing plan remains Google Search only; the earlier clarification of search results versus banners on other websites has not yet been answered. No placement settings have been applied because no campaign is running.
- The owner clarified billing is **prepay/manual payment**. This records the owner's payment mode; it does not establish that a deposit has settled beyond the last observed zero balance.
- The owner then authorised **GA4 and Google Tag Manager setup**, and requested browser-only control instead of whole-screen automation. The Edge extension connection was verified and used for subsequent tab interactions. Some DOM calls timed out; tab screenshots and accessibility controls allowed progress without desktop capture.
- Analytics inspection under the chosen login found an existing Firebase account with two unrelated properties; no Araya property appeared in that account picker. Those properties were left unchanged. The Tag Manager Accounts tab showed no existing accounts/containers.
- Prepared a new Analytics account **PT Araya Internusa**, property **Araya Website - GA4**, **Indonesia / (GMT+07:00) Jakarta Time / Indonesian Rupiah (Rp)**. Industry: **Business & Industrial**. Employee range: **11–100**, explicitly confirmed by the owner. Objectives: **Generate leads** and **Understand web and/or app traffic**. All four optional account data-sharing choices are off. Reached the Indonesia Terms of Service dialog before the owner approved acceptance.
- Prepared Tag Manager account **PT Araya Internusa**, country **Indonesia**, container **arayainternusa.co.id**, platform **Web**, anonymous data sharing off. Reached its Terms of Service dialog before the owner approved acceptance.
- Both setups reached their terms screens before acceptance. Browser-only screenshots: `../docs/evidence/google-ads-audit-20261021/ga4-terms-prepared-20261022.jpg` and `../docs/evidence/google-ads-audit-20261021/gtm-terms-prepared-20261022.jpg`.

#### Approved account creation and configuration

- The owner explicitly approved both Google Terms of Service and the displayed Data Processing Terms at action time. Accepted both and verified successful account creation; no additional acceptance is pending for these two creation steps.
- **GA4 account:** PT Araya Internusa, account ID **412910120**. **Property:** Araya Website - GA4, property ID **560191836**. **Web stream:** Araya Website, `https://arayainternusa.co.id`, stream ID **16182653195**, Measurement ID **G-WMBDHTFPBJ**. Created one stream only. Do not use the unrelated Firebase property's Measurement ID.
- **GTM account:** PT Araya Internusa, account ID **6399236451**. **Web container:** arayainternusa.co.id, internal container ID **283134459**, public container ID **GTM-NK3C3RVZ**, default workspace ID **2**.
- The GA4 stream's saved Enhanced Measurement settings show **Page views and Scrolls only**. Disabled automatic outbound clicks, site search, form interactions, video engagement and file downloads. Contact events will have one explicit implementation; clicks must stay diagnostic/secondary rather than being represented as qualified inquiries.
- Saved draft tag **GA4 - Araya - Base** (tag ID **3**) using Google's official **Google Analytics** Web-stream template for **G-WMBDHTFPBJ**. Trigger: **Initialization - All Pages**. Advanced consent settings explicitly require **analytics_storage** before firing, in addition to Google's built-in consent checks. GTM reports **3 workspace changes** after saving; the template also manages destination/container settings, so this is not a count of three custom tags.
- The new Google Analytics template is the name presented in the current GTM interface; it connects the Web stream and uses the container's Settings tab. The older generic Google-tag instructions should be reconciled with this interface at installation. No custom/community template was installed.
- **Not published or installed:** no GTM Submit/Publish, website source change, Git commit/push, production deployment, new Ads campaign or advertising spend. GA4 explicitly reports collection inactive/no recent data, as expected before installation. Consent behavior and contact-event runtime are not yet tested. Account creation is complete; website measurement is not active.
- Before installation: review destination/container collection settings, implement the approved privacy/consent flow, load GTM only after the relevant permission in basic mode (so initialization runs after consent), add the single canonical contact-event implementation and its tag, keep previews isolated, then test and publish only with production authorisation. GA4–Ads linking, Ads destination configuration and conversion imports remain pending.
- Analytics' picker disappeared after onboarding and the embedded installation panel remained blank. The GTM universal picker exposed the verified Araya account/property entry and its actual Analytics link; navigation through that link and Admin → Data streams restored access to stream details. No duplicate Analytics account/property was created to work around the UI issue.
- Reviewed the GTM container's separate **Manage automatic event detection** activity (internal activity ID **2147480577**). Its initial defaults enabled more collection than the GA4 stream. Saved a draft with **Scrolls on** and **browser-history page views, outbound clicks, form interactions, video engagement and file downloads off**. Normal page-load page views are controlled by the base tag; turning off browser-history events prevents treating this static website's section navigation as additional page loads. Runtime behavior still requires verification after installation.
- Reopened the saved base tag and verified **G-WMBDHTFPBJ**, **Initialization - All Pages**, **Require additional consent for tag to fire → analytics_storage**, disabled Save (no unsaved edits), and **3 workspace changes**. Kept both created-account tabs open for the owner. Evidence: `../docs/evidence/google-ads-audit-20261021/ga4-stream-created-20261022.jpg` and `../docs/evidence/google-ads-audit-20261021/gtm-base-draft-created-20261022.jpg`.
- The GTM Settings destination row recognises **Araya Website / G-WMBDHTFPBJ / 1 tag / Optimized: Yes**, while **External account link** shows **Not linked**. That label must be investigated during integration; it is not proof of GA4–Ads linking or cross-product settings synchronisation. No linking permission was granted during this account-creation step.

## Contents

1. [Executive summary](#1-executive-summary)
2. [Current website assessment](#2-current-website-assessment)
3. [Advertising objectives](#3-advertising-objectives)
4. [Recommended service priorities](#4-recommended-service-priorities)
5. [Geographic targeting strategy](#5-geographic-targeting-strategy)
6. [Campaign structure](#6-campaign-structure)
7. [Keyword strategy](#7-keyword-strategy)
8. [Advertisement copy recommendations](#8-advertisement-copy-recommendations)
9. [Landing-page strategy](#9-landing-page-strategy)
10. [Conversion tracking architecture](#10-conversion-tracking-architecture)
11. [Website technical improvements](#11-website-technical-improvements)
12. [Budget and testing strategy](#12-budget-and-testing-strategy)
13. [Future expansion plan](#13-future-expansion-plan)
14. [Implementation checklist](#14-implementation-checklist)

## 1. Executive summary

**Recommendation:** prepare one Google Search campaign covering Surabaya, Sidoarjo and Gresik, with four service ad groups, Indonesian and English language targeting, and an average budget of Rp100,000/day. Concentrate on companies requesting programming, repair, troubleshooting and retrofit work. Validate keywords and bids through the actual Google Ads account before spending.

The website is a credible starting point: a lightweight static architecture, real engineering photographs, identifiable company management, service coverage, clear contact details, and separate Noris and ComAp guides. Keep its orange, charcoal and white identity. A rebuild is unnecessary.

**It is not yet ready for a measured lead-generation campaign.** There are no Google analytics/advertising tags in the inspected source or live HTML, no contact form, no linked privacy notice, and no demonstrated way to join an advertising click to a qualified inquiry. WhatsApp clicks are measurable interactions once tracking is installed; they do not prove a message was sent.

Before a controlled pilot:

- Implement and validate production-only measurement, privacy disclosures and the agreed consent behavior (D01–D03).
- Establish an inquiry log, qualification rules and an accountable person handling inquiries (M03).
- Link ads directly to `.co.id` service sections. Verify campaign parameters on every actual final URL (D04). The `.com` redirect currently loses both path and query data.
- Complete Keyword Planner validation, campaign configuration, ad review and an approved spending ceiling (M01–M06).

**Next improvement:** one focused Indonesian automation landing page, reusing existing components, for PLC/HMI/SCADA and related control work. Do not immediately create four overlapping pages or restore long paragraphs to the homepage.

Budget correction: Rp100,000 × 30 days is Rp3,000,000, but Google's usual full-month limit for an unchanged average daily budget is **30.4 × Rp100,000 = Rp3,040,000**. For most campaigns, a day can be billed up to **Rp200,000**. Taxes and other charges must be checked separately. These are platform spending rules, not forecasts of leads. [Google: average daily budgets](https://support.google.com/google-ads/answer/6385083?hl=en).

## 2. Current website assessment

### 2.1 Evidence, method and limitations

**Verified:** fresh HTTP GETs, live desktop/mobile inspection and source reads on the audit date. Desktop viewport: 1280 × 900; mobile: 390 × 844. Browser sizing was restored afterward. No inquiries were sent. HTTP probes used synthetic diagnostic campaign values and a clearly fake click identifier; these are not advertising performance data.

**Owner-provided claims:** 1,500+ projects, founding year 2009, certification, international technical backing and authorised distributor status. They appear on the site; this audit does not independently validate project totals, certification scope or manufacturer appointment documents. Exact credential names and permission to publish named project evidence remain outstanding.

**Unknown:** account conversion history, actual demand, CPC, ad competition, conversion rate, qualified-lead cost, sales cycle, margins, response speed and current Google Ads/GA4/GTM account configuration. Public source inspection cannot establish whether old accounts exist.

Evidence was saved outside the repository at:

`C:/Users/hakim/codex/araya-work/arayaweb/docs/evidence/google-ads-audit-20261021/`

This includes `http-audit.json`, `resource-audit.json`, live HTML, robots/sitemap snapshots, a PageSpeed error response, mobile DOM evidence and the screenshots listed below. It will not be included in a production package.

### 2.2 Contact journey and visual review

| Step | Observed behavior | Health / advertising implication | Screenshot |
|---|---|---|---|
| 1. Arrive on desktop or mobile home | Engineering positioning, company identity, ship image and WhatsApp project CTA are visible. | **Good general introduction.** Broad marine emphasis is less specific to a factory PLC repair search. | `01-desktop-home.png`, `02-mobile-home.png` |
| 2. Open mobile Menu → Our Services | Opens `index.html#services`; menu closes and services are accessible. | **Working.** Buyer must choose a sector and open its disclosure. | `03-mobile-services.png` |
| 3. Expand automation services | PLC/HMI/SCADA and related scopes appear as short descriptions in a single mobile column. | **Working, with friction.** Existing copy is deliberately concise; do not lengthen all 32 descriptions. | `04-mobile-automation-expanded.png` |
| 4. Enter directly at `/#automation-plc` | JavaScript opens the parent disclosure; query parameters remain on entry. | **Useful pilot destination.** Bypasses the general introduction; does not provide a focused quotation journey. | `09-mobile-plc-direct-entry.png` |
| 5. Menu → Contact Us | Reaches `#contact`; WhatsApp and email buttons are visible. | **Working.** No form, qualification step or confirmation of an actual inquiry exists. Phone is also present farther down the contact block. | `05-mobile-contact.png` |
| 6. Brand Partners → ComAp | Opens `/comap/`; Applications contents link reaches `#applications`. | **Working, informational.** Suitable for ComAp research; not the default destination for generic PLC services. | `06-mobile-comap.png`, `07-mobile-comap-applications.png` |
| 7. Open Noris guide | Manufacturer, sensors and automation scope are clear; footer service link returns to the correct homepage section. | **Working, informational.** Keep separate from initial generic service targeting. | `08-mobile-noris.png` |

The settled mobile samples showed no horizontal page overflow; the document measured 375 CSS px inside a 390 px viewport including the scrollbar. No major clipping was visible in the sampled hero, services, contact or brand introductions. This is a sampled review, not a complete device or accessibility certification. Smooth scrolling and counters have transitional states; screenshots were reviewed after settling.

Accessibility positives include a skip link, native service disclosures and an exposed mobile menu state. Future tracking/landing additions should retain keyboard access, focus behavior, contrast and reduced-motion support. Do not add modal lead capture or obscure the page with intrusive contact widgets. Client-logo autoplay has reduced-motion handling; no claim of full autoplay accessibility conformance is made.

### 2.3 Content, positioning and credibility

| Area | Verified finding | Assessment / action |
|---|---|---|
| Services | 12 marine, 8 industrial and 12 automation/electrical scopes in `tools/site_content.py`; all 32 are generated into homepage HTML. | Good breadth. Paid targeting should isolate the relevant commercial need. |
| PLC/HMI/SCADA | Programming, repair, retrofit and monitoring are explicitly presented. | Strong initial advertising fit; exact expertise by platform/project should be confirmed before model-specific ads. |
| Industrial repair | Machinery, crane, generator, panel and control-system work are covered. | Use control/machinery repair intent; avoid indiscriminate consumer repair queries. |
| Electrical control | Panels, MCC, instrumentation, motor controls and VFDs are present. | Relevant; distinguish service inquiries from DIY wiring and component-price shopping. |
| Marine automation | AMS, engine control, generators, steering, monitoring and retrofit are present. | Maintain a narrow, separate ad group. Broad mechanical overhaul is outside this initial campaign theme. |
| Credibility | Founding year, leadership portraits, work photos and seven client logos are visible. | Helpful, but no detailed named case study establishes PLC-specific delivery outcomes. Add owner-approved evidence later (D08). |
| Certification / partners | General certification and technical backing are stated; Noris and ComAp use owner-approved “authorised distributor”. | Do not invent credential names, class approvals, exclusivity or guaranteed OEM support. Retain appointment/credential records for any advertising claims. |
| Language | Website content and HTML language are English. | Indonesian ads would land on English content; a concise Indonesian service introduction or focused landing page is recommended (D06). |
| Contact | `+62 813 2639 6262`, `+62 31 7877990`, `cs@arayainternusa.com`. | The email's `.com` domain is not inherently a problem. Owner must verify monitored delivery and routing. |

### 2.4 Architecture, SEO and routing

| URL / component | Live result | Conclusion |
|---|---|---|
| `/`, `/noris/`, `/comap/` | HTTP 200; self-referencing `.co.id` canonicals; `index, follow`. | Correct basic production indexing signals. Actual indexing/rankings require Search Console. |
| `/marine/`, `/industrial/`, `/automation/` | HTTP 200 compatibility documents; script redirects to homepage fragments. | These are not standalone service landing pages. Avoid them as paid final URLs. |
| `/araya/` | HTTP 301 → root. Diagnostic query lost. | Old home route is retired correctly, with an attribution limitation (D05). |
| `.com` and `www.com`, HTTP and HTTPS | HTTP 301 → `https://arayainternusa.co.id/`. Query lost. `/noris/` and `/comap/` tests also went to root. | Canonical domain is reached, but equivalent path and campaign attribution are lost. Hosting redirect needs review (D05). |
| Primary HTTP and `www.co.id` | HTTP 301 → equivalent primary root; diagnostic query retained. | Good in tested root variants. |
| Direct primary root with query | HTTP 200; query retained. | Use this host directly for ads. |
| `robots.txt` | HTTP 200, allows crawling and references production sitemap. | Good. A user-agent simulation of desktop/mobile AdsBot received HTTP 200, but does not prove access from Google's infrastructure. |
| `sitemap.xml` | HTTP 200; only the three substantive pages, lastmod 2026-10-15. | Appropriate current route set. Build-date-based lastmod should eventually reflect meaningful changes (D12). |
| Synthetic nonexistent page | HTTP 404. | Good; no blanket homepage fallback. |
| Internal navigation | 25 distinct internal path/fragment destinations from the three live pages matched fetched page IDs. | No missing destination found in this bounded check; external contact delivery and every external source link were not tested. |

Titles and descriptions exist and differ by page. Homepage title: “Marine & Industrial Automation Indonesia | Araya Internusa”. Noris/ComAp titles include “Authorised Distributor Indonesia”. The site includes organization/service-related structured data and manufacturer information. These are useful SEO foundations, not proof of rankings, eligibility for enhanced search results or an Ads Quality Score.

The GitHub Pages build intentionally uses `noindex, nofollow`; production configuration in `tools/build.py` overrides the preview base to the company root and uses `index, follow`. Do not advertise the preview domain. Do not mistake preview metadata for a production defect.

### 2.5 Loading and Core Web Vitals

**Verified source strengths:** static HTML, local font, deferred first-party JS, responsive hero preload, WebP service imagery, image dimensions and lazy-loaded lower-priority content. No analytics/advertising scripts were found by a repository search or live script inventory.

Fresh individual resource responses, requesting compression:

| Resource | Received payload | Observation |
|---|---:|---|
| Homepage HTML, identity encoding | 28,480 bytes | Content available without client-side rendering. |
| Hero `ship-1400.webp` | 67,784 bytes | About 66 KiB; mobile may select a different responsive variant. |
| `team.webp` | 80,522 bytes | Eager, low fetch priority. |
| `marine.webp` / `industrial.webp` | 91,638 / 85,762 bytes | Eager, low fetch priority. |
| `control-room-1400.webp` | 116,348 bytes | About 114 KiB; responsive variants exist. |
| Versioned CSS / JS | 11,604 / 3,475 bytes | Brotli responses observed. |
| Font | 22,288 bytes | Self-hosted WOFF2. |

These are individual HTTP payloads, not a browser waterfall, page transfer total, render time or mobile performance score. Sample HTML request durations were roughly 1.5–1.6 seconds including the whole request/read; **they are not TTFB measurements** and cannot establish typical customer speed.

All sampled resources returned `Cache-Control: no-cache`, which permits caching with revalidation; it does not mean “never stored”. Repeated revalidation can add latency. Improve cache policy with release-safe asset versioning (D07). Do not assign year-long immutable caching to unversioned image paths that may change.

**Measurement unavailable:** the fresh mobile PageSpeed API request returned HTTP 429 quota exceeded. No Chrome DevTools trace capability was available. Therefore LCP, INP, CLS and Lighthouse scores are **ungraded**, not passed. Before scale-up, measure homepage, the actual paid destination and contact/menu interactions on a throttled mobile profile; add field monitoring only if warranted. Use p75 targets LCP ≤2.5 s, INP ≤200 ms and CLS ≤0.1. Field data may be unavailable at low traffic; lab results cannot establish field INP. [Google web.dev: Core Web Vitals](https://web.dev/articles/vitals).

## 3. Advertising objectives

### 3.1 Define a qualified inquiry

A human-reviewed inquiry is qualified when it concerns an identifiable business, vessel or industrial site; describes equipment/service needs within Araya's scope; includes a workable location and contact route; and can progress to technical assessment or quotation. An available drawing, nameplate or planned work window helps, but should not be compulsory on first contact.

Exclude spam, recruitment, courses, student help, free software requests, unrelated household repairs and duplicate follow-ups from the qualified count. Keep disqualified reasons for keyword learning.

### 3.2 Measurement hierarchy

1. **Qualified inquiries:** deduplicated by sales review; primary business outcome.
2. **Cost per qualified inquiry:** advertising spend divided by attributed qualified inquiries, with unattributed inquiries disclosed separately.
3. **Qualified inquiry rate:** attributed qualified inquiries / ad clicks; also monitor landing-session rate separately and label the denominator.
4. **Search relevance:** reviewed search terms matching commercial engineering needs, within Google's reporting visibility.
5. **CTR:** useful for relevance, not a substitute for lead quality.

Also report quote requests, quotations issued, won work, response times and lead-to-quote progression when available. No target CPL, lead volume or return is asserted without business economics and measured data.

### 3.3 Resolve the conversion definitions in the brief

The brief initially lists WhatsApp, forms and phone inquiries as primary, then correctly distinguishes successful/qualified inquiries from clicks. Use the latter interpretation:

- **Primary candidate:** verified qualified lead, imported with supported attribution; or a genuinely successful form submission as a clearly labelled provisional lead outcome if a form is later approved.
- **Secondary:** WhatsApp click, telephone click and email click. An answered call is stronger evidence than a click, but duration alone still does not establish qualification.
- **Not a lead:** page view, service expansion, scrolling, logo interaction or a brand-page visit.

If no reliably attributed primary action exists at launch, use a controlled click-based pilot and a manual lead register. Do not tell Smart Bidding that contact clicks are qualified leads just to supply a conversion signal.

## 4. Recommended service priorities

Retain the four themes as ad groups within one campaign. Keep campaign spend flexible. The proposed proportions are a reasonable **testing hypothesis**, not validated demand or an enforceable ad-group budget allocation.

| Ad group | Initial planning share | Recommendation / boundary |
|---|---:|---|
| PLC / HMI / SCADA | 40% | First priority: programming, troubleshooting and retrofit. Own software/control-logic intent. |
| Industrial control repair / retrofit | 25% | Keep, narrowed to machinery control/electrical troubleshooting. Own machine fault/modernisation intent; do not duplicate generic PLC phrases. |
| Electrical panels / drives | 20% | Keep panels, MCC, VFDs and motor-control services. Exclude household installations and hobby circuits. |
| Marine automation / AMS | 15% | Keep as a small, exact-intent test. Exclude generic ship jobs, vessel purchases and unrelated consumer marine terms. |

At Rp100,000/day these shares correspond to planning averages of Rp40,000 / Rp25,000 / Rp20,000 / Rp15,000; Google will not respect those amounts automatically inside one campaign. Review actual share weekly. If demand is too thin or the repair and PLC groups repeatedly attract the same inquiries, combine them into “Industrial automation” and keep electrical and marine groups separate. If budget becomes insufficient, prioritise PLC and industrial repair before expanding coverage.

Do not initially add a separate instrumentation, brand-distribution, general engine-overhaul or nationwide campaign. Those can be assessed later. Noris sensors and ComAp generator controls are relevant capabilities, but brand procurement is a different search intent from PLC repair.

## 5. Geographic targeting strategy

Configure **Surabaya, Sidoarjo and Gresik** using the available Google geographic entities. Inspect the map and selected entity type: a city and a regency may cover different areas. Record the actual location IDs; none are invented here. Do not also target all Indonesia or all East Java.

Set inclusion to **Presence: people in or regularly in the targeted locations**. Presence is based on Google's inferred signals, so it is not a guarantee of the equipment's location or a strict GPS boundary. Ask where the site/vessel is when qualifying inquiries. [Google: advanced location options](https://support.google.com/google-ads/answer/1722038?hl=en).

Use Indonesian and English languages. This setting reflects languages Google believes users understand; it does not restrict a user to typing a query in that language or guarantee the language of the ad they see. Supply separate Indonesian and English ad variants and inspect results. [Google: location and language settings](https://support.google.com/google-ads/answer/1722072?hl=en).

One regional campaign is preferable to three small city campaigns initially. Review clicks, spend, qualified inquiries, actual project location and cost per qualified inquiry by area. Report small samples and inferred-location limitations explicitly. Do not exclude a city after one unqualified inquiry.

## 6. Campaign structure

### 6.1 Proposed configuration, not an account import

```yaml
campaign: ARAYA | Search | East Java Core | Engineering Leads
status: NOT_CREATED
primary_domain: https://arayainternusa.co.id/
network: Google Search
search_partners: off_for_initial_test
display_expansion: off_if_present
locations: [Surabaya, Sidoarjo, Gresik] # confirm geographic entities/IDs in account
location_inclusion: Presence
languages: [Indonesian, English]
currency: IDR
account_timezone: Asia/Jakarta # verify account settings before setup
average_daily_budget_idr: 100000
bidding: Maximize Clicks with an explicitly reviewed CPC bid limit
cpc_bid_limit: TO_VALIDATE_IN_KEYWORD_PLANNER
initial_matches: [exact, phrase]
ai_max_and_final_url_expansion: off_for_controlled_initial_test
auto_tagging: enabled_after_validation
schedule_proposal: Monday-Saturday 08:00-17:00 WIB
ad_groups:
  - 01 | PLC HMI SCADA
  - 02 | Industrial Control Repair
  - 03 | Panels Drives Electrical
  - 04 | Marine Automation AMS
```

The schedule matches published opening hours; confirm someone answers then. It is a proposal, not a promise of emergency or 24-hour service. Extend hours only if inquiries are handled or callbacks are reliable. Do not exclude mobile or make unsupported demographic exclusions. Optional audience segments should be observation-only at first.

Start with **Maximize Clicks plus a CPC cap**, strict queries and a small test window because trustworthy conversion history is unknown. This bids for clicks, so quality must be controlled through keywords, exclusions and human review. Set the cap from account forecasts and acceptable test spend; do not invent a rupiah figure. Manual CPC is an alternative if available and actively managed. Too-low caps can prevent useful traffic. [Google: Maximize Clicks](https://support.google.com/google-ads/answer/6268626?hl=en).

Move toward Maximize Conversions only after the selected primary action works, is genuinely useful and arrives consistently within an understood qualification delay. There is no universal “30 conversions means ready” rule applied here. Start without a speculative target CPA. Do not optimise toward page engagement or WhatsApp clicks.

Keep budgets, locations, schedules, bids and naming editable in Google Ads. No code deployment should be necessary to add a city or change an advertising budget. Keep automated recommendations from silently broadening keywords, URLs or goals; review account automation settings before launch.

## 7. Keyword strategy

### 7.1 Match and intent rules

The following are **research candidates**, not proven high-performing keywords. Start with a small subset validated for service fit and availability. Square brackets denote exact match; quotation marks denote phrase match. Exact match can match the same meaning/intent and phrase match can match the meaning of a phrase, so neither is a literal-only filter. Close variants still require search-term review. Do not activate broad match initially. [Google: keyword matching](https://support.google.com/google-ads/answer/7478529?hl=en), [close variants](https://support.google.com/google-ads/answer/9342105?hl=en).

**P1:** explicit service, repair or programming need. **P2:** relevant but broader/ambiguous system intent. These are intent priorities, not CPC or competition estimates. Avoid bare `PLC`, `SCADA`, `automation`, `inverter` or `marine` as initial keywords.

### 7.2 Candidate list and landing mapping

All fragments below use the primary domain: `https://arayainternusa.co.id/`.

| Group | Exact candidates | Phrase candidates | Intent / priority | Initial destination |
|---|---|---|---|---|
| PLC programming | `[jasa programming plc]`, `[jasa plc surabaya]`, `[jasa plc sidoarjo]`, `[jasa plc gresik]` | `"jasa programming plc"`, `"plc programming service"` | Contractor/programming, P1 | `/#automation-plc` |
| PLC faults | `[jasa troubleshooting plc]`, `[service plc industri]` | `"plc troubleshooting service"` | Repair/fault diagnosis, P1 | `/#automation-plc` |
| HMI / SCADA | `[jasa programming hmi]`, `[jasa scada]`, `[jasa programming scada]` | `"hmi programming service"`, `"scada programming service"` | Software/integration, P1; generic SCADA P2 | `/#automation-scada` |
| Machinery controls | `[jasa troubleshooting mesin industri]`, `[service kontrol mesin industri]` | `"industrial control system repair"`, `"jasa perbaikan kontrol mesin"` | Business repair, P1 | `/#industrial-automation` |
| Retrofit | `[jasa retrofit mesin industri]`, `[retrofit plc mesin]` | `"industrial automation retrofit"`, `"jasa upgrade kontrol mesin"` | Upgrade/retrofit, P1 | `/#industrial-automation` |
| Automation contractor | `[jasa otomasi industri surabaya]` | `"jasa automation industri"` | Contractor, P2; validate scope | `/#automation-plc` |
| Panels / MCC | `[jasa panel kontrol industri]`, `[service panel kontrol]` | `"industrial control panel service"`, `"jasa panel mcc"` | Panel engineering/repair, P1 | `/#automation-panels` |
| Drives | `[service inverter industri]`, `[jasa perbaikan vfd]` | `"industrial vfd repair"`, `"service motor control industri"` | Drive/motor control service, P1 | `/#automation-drives` |
| Instrumentation | `[jasa instrumentasi industri]` | `"industrial instrumentation service"` | System/service, P2; hold until capacity/demand checked | `/#automation-instrumentation` |
| Marine controls | `[service automation kapal]`, `[jasa otomasi kapal]` | `"marine automation service"`, `"marine control system retrofit"` | Vessel engineering service, P1 | `/#marine-automation` |
| Marine AMS | `[service ams kapal]`, `[jasa alarm monitoring kapal]` | `"ship alarm monitoring system"`, `"marine alarm system repair"` | Repair P1; generic system procurement P2 | `/#marine-alarms` |

Start with roughly 5–8 selected keywords per active group, including the strongest Indonesian terms and a few English equivalents. The table is a candidate pool, not a recommendation to turn on every variation. Do not multiply every term by every city and match type. Exact and phrase duplicates overlap; introduce phrase variants where they add useful discovery.

Assign ambiguous PLC retrofit terms to the PLC group first; machinery fault terms to industrial repair; panel/VFD terms to electrical. Do not add aggressive cross-negatives at launch that could suppress “repair PLC panel mesin”. Use actual routing problems before adding narrow ad-group negatives.

### 7.3 Shared negative list

Use a campaign list for this service campaign, rather than permanent account-wide exclusions that might block a future recruitment/training business initiative.

| Negative type | Proposed starting entries | Reason / caution |
|---|---|---|
| Broad, clear irrelevant intent | `lowongan`, `loker`, `magang`, `internship`, `internships`, `vacancy`, `vacancies`, `karir`, `career`, `careers`, `skripsi`, `makalah`, `kursus`, `pelatihan`, `tutorial` | Jobs, student work and training. Confirm Araya is not advertising training in this campaign. |
| Phrase, irrelevant combinations | `"tugas kuliah"`, `"tugas akhir"`, `"belajar plc"`, `"plc course"`, `"plc courses"`, `"plc training"`, `"free download"`, `"download gratis"`, `"software crack"`, `"service ac rumah"`, `"mesin cuci"`, `"inverter mobil"` | Block unwanted context without excluding all software or all inverter work. |
| Exact, only when observed | `[apa itu plc]`, `[pengertian scada]`, `[diagram plc sederhana]` | Informational searches; add variants based on actual reports. |

Negative broad requires all listed words in any order; phrase requires the phrase in order; exact blocks only the complete matching query. Negative matching differs from positive matching and does not expand to all close variants/synonyms. Check Indonesian/English and singular/plural variants; review live results. [Google: negative keywords](https://support.google.com/google-ads/answer/2453972?hl=en).

Do not blanket-exclude `software`, `program`, `manual`, `harga`, `sensor`, `Siemens`, `ComAp` or `Noris`: legitimate buyers can use those terms. Do not exclude “maintenance” just because a search might be an employment query. Add proven irrelevant combinations instead.

### 7.4 Keyword Planner validation — account access required

Run separate Indonesian and English research for the selected three areas and Google Search network. Record the date, selected entities, language, network and historical period. Save search-volume estimates, top-of-page bid ranges, competition and forecasts with their geographic scope. Planner competition concerns advertisers, not organic SEO difficulty. Its forecasts are estimates; they do not validate Araya's conversion rate. [Google: Keyword Planner](https://support.google.com/google-ads/answer/7337243?hl=en), [forecast interpretation](https://support.google.com/google-ads/answer/3022575?hl=en).

Check both service-specific and regional forms, remove off-scope suggestions and inspect low-volume eligibility. If city detail is sparse, use regional data for context and label it accurately; do not present regional/national figures as city estimates. The output should determine the initial subset, CPC cap and whether marine receives a separate initial test or is deferred. Search-result browsing alone cannot establish these metrics.

## 8. Advertisement copy recommendations

### 8.1 Copy rules

Responsive Search Ads support 3–15 headlines of up to 30 characters and 2–4 descriptions of up to 90 characters; display paths allow 15 characters each. The drafts below meet those character limits, including spaces. They are alternatives for review, not promises of approval or performance. [Google: responsive search ads](https://support.google.com/google-ads/answer/7684791?hl=en).

Use separate Indonesian and English RSAs so assembled assets remain coherent. Each Indonesian draft has eight headlines and three descriptions; each English draft is a minimum complete alternative with three headlines and two descriptions. Expand English assets only with useful, distinct wording. Do not mix the two languages within one asset pool. Language targeting does not guarantee language-perfect serving; review ad/query performance after launch.

Avoid “24/7”, instant response, guaranteed savings, cheapest/best, unsupported project outcomes, named certifications, OEM authorisation for other brands or stock availability without evidence. Do not use “local engineers”, “Sidoarjo backup team” or “standardised” positioning. “Authorised distributor” remains owner-approved for Noris/ComAp but is unnecessary in these generic service ads.

### 8.2 RSA drafts

**01 | PLC HMI SCADA** — final URL: `https://arayainternusa.co.id/#automation-plc`; display paths `plc-scada` / `services`.

| Asset | Indonesian draft |
|---|---|
| H1 | Jasa Programming PLC |
| H2 | Jasa HMI dan SCADA |
| H3 | Troubleshooting PLC Industri |
| H4 | Retrofit Sistem Kontrol |
| H5 | Otomasi untuk Industri |
| H6 | PT Araya Internusa |
| H7 | Surabaya Sidoarjo Gresik |
| H8 | Diskusikan Kebutuhan Anda |
| D1 | Pemrograman, perbaikan dan retrofit PLC untuk kebutuhan otomasi industri Anda. |
| D2 | Integrasi HMI dan SCADA untuk monitoring, alarm dan kontrol operator. |
| D3 | Kirim model peralatan dan kebutuhan proyek. Hubungi PT Araya Internusa. |

| Asset | English draft |
|---|---|
| H1 | PLC Programming Services |
| H2 | HMI and SCADA Integration |
| H3 | PT Araya Internusa |
| D1 | PLC programming, repair and retrofit for industrial automation systems. |
| D2 | Discuss your equipment, control requirements and project location with Araya. |

**02 | Industrial Control Repair** — final URL: `https://arayainternusa.co.id/#industrial-automation`; paths `industrial` / `control-repair`.

| Asset | Indonesian draft |
|---|---|
| H1 | Perbaikan Kontrol Mesin |
| H2 | Troubleshooting Mesin Industri |
| H3 | Retrofit Otomasi Industri |
| H4 | Upgrade Sistem Kontrol |
| H5 | Servis Kelistrikan Industri |
| H6 | PT Araya Internusa |
| H7 | Surabaya Sidoarjo Gresik |
| H8 | Bahas Kendala Mesin Anda |
| D1 | Perbaikan kontrol dan kelistrikan mesin untuk kebutuhan industri. |
| D2 | Modifikasi dan retrofit sistem otomasi. Sampaikan kendala peralatan Anda. |
| D3 | Diskusikan model mesin, lokasi dan rencana pekerjaan bersama Araya. |

| Asset | English draft |
|---|---|
| H1 | Industrial Control Repair |
| H2 | Machinery Control Retrofit |
| H3 | PT Araya Internusa |
| D1 | Repair and retrofit of machinery controls and industrial electrical systems. |
| D2 | Share the equipment model, fault symptoms and work location with our team. |

**03 | Panels Drives Electrical** — final URL: `https://arayainternusa.co.id/#automation-panels`; paths `control-panels` / `services`. VFD-specific keyword final URLs can use `/#automation-drives` after destination testing.

| Asset | Indonesian draft |
|---|---|
| H1 | Jasa Panel Kontrol Industri |
| H2 | Servis Panel dan MCC |
| H3 | Perbaikan VFD Industri |
| H4 | Sistem Kontrol Motor |
| H5 | Instrumentasi Industri |
| H6 | PT Araya Internusa |
| H7 | Surabaya Sidoarjo Gresik |
| H8 | Diskusikan Sistem Anda |
| D1 | Supply, perbaikan dan modifikasi panel kontrol serta motor-control centre. |
| D2 | Layanan VFD, soft starter dan instrumentasi untuk sistem industri. |
| D3 | Kirim model peralatan, kendala dan lokasi. Diskusikan kebutuhan dengan Araya. |

| Asset | English draft |
|---|---|
| H1 | Industrial Control Panels |
| H2 | VFD and Motor Control Service |
| H3 | PT Araya Internusa |
| D1 | Supply, repair and modification of control panels, switchboards and MCC systems. |
| D2 | Discuss industrial drives, instrumentation and motor-control requirements. |

**04 | Marine Automation AMS** — final URL: `https://arayainternusa.co.id/#marine-automation`; paths `marine` / `automation`. AMS-specific keywords can use `/#marine-alarms`.

| Asset | Indonesian draft |
|---|---|
| H1 | Jasa Otomasi Kapal |
| H2 | Alarm Monitoring Kapal |
| H3 | Retrofit Kontrol Kapal |
| H4 | Servis Kelistrikan Kapal |
| H5 | Kontrol dan Monitoring Mesin |
| H6 | PT Araya Internusa |
| H7 | Surabaya Sidoarjo Gresik |
| H8 | Bahas Kebutuhan Kapal Anda |
| D1 | Perbaikan dan retrofit kontrol, monitoring serta kelistrikan kapal. |
| D2 | Layanan alarm monitoring dan sistem otomasi untuk kebutuhan kapal Anda. |
| D3 | Sampaikan sistem, lokasi kapal dan rencana pekerjaan kepada Araya. |

| Asset | English draft |
|---|---|
| H1 | Marine Automation Services |
| H2 | Ship Alarm Monitoring Systems |
| H3 | PT Araya Internusa |
| D1 | Repair and retrofit of vessel automation, alarm monitoring and control systems. |
| D2 | Share the vessel location, equipment details and planned work with Araya. |

Do not automatically pin every headline; review combinations for duplication. Final URLs must remain on `.co.id`, show the described service and pass expanded-URL testing. When D06 is available, update relevant ads to the focused Indonesian landing page and align the displayed language.

### 8.3 Other assets

- **Callouts:** `Marine & Industrial`, `PLC, HMI & SCADA`, `Repair & Retrofit`, `Sidoarjo & Jakarta`. Each is within 25 characters; use only where relevant. [Google: callout assets](https://support.google.com/google-ads/answer/6079510?hl=en).
- **Call asset:** use the verified company phone and staffed schedule. Confirm number verification and reporting availability in the account before enabling. Keep real business identity consistent.
- **Business name/logo:** use the existing company name and original Araya asset, subject to account eligibility and verification.
- **Sitelinks:** defer broad sitelink expansion until genuinely useful distinct destinations exist. Do not fabricate several pages or advertise unrelated brand guides simply to fill asset slots. Existing about/contact fragments can be assessed in the Ads editor, but serving and policy eligibility are not assumed. A contact destination should be an actual site section/page, not a `mailto:` final URL.

## 9. Landing-page strategy

### 9.1 Initial decision

| Proposed topic | Existing destination | Decision |
|---|---|---|
| Industrial Automation | `/#automation-plc` and automation service group | Reuse for a restricted pilot; one focused Indonesian automation page is the preferred improvement. |
| PLC, HMI & SCADA | `/#automation-plc`, `/#automation-scada` | Combine with industrial automation initially; a second overlapping generic page is unnecessary. |
| Troubleshooting & Retrofit | `/#industrial-automation` | Reuse initially. Create a distinct page only if inquiries/search intent support original, specific content. |
| Marine Automation | `/#marine-automation`, `/#marine-alarms` | Reuse for narrow keywords; separate paid page later if marine demand warrants it. |
| Noris / ComAp distribution | `/noris/`, `/comap/` | Keep informational guides; future brand procurement ads should use the appropriate brand page, not generic service ads. |

Direct scope fragments expand their disclosure. Overview fragments such as `/#automation-services` stop at the service overview and do not themselves expose every scope. The existing root remains one HTML page: fragments do not create distinct SEO pages or independent page metadata. GA4 should record a separate `landing_section` value if distinguishing scope-level entry is needed.

### 9.2 Recommended first focused page (D06)

**Proposed URL, not currently implemented:** `https://arayainternusa.co.id/layanan/otomasi-industri/`.

Use a concise Indonesian service page covering PLC/HMI/SCADA, controls troubleshooting, panels and retrofit with clearly separated sections. Preserve the company's existing shell, colours, font, real photos and footer. Suggested order:

1. H1: “Jasa PLC, HMI, SCADA dan Otomasi Industri”; short line identifying industrial buyers and Surabaya/Sidoarjo/Gresik service availability, after owner confirmation.
2. Compact scope: programming, diagnosis, integration and retrofit; explain which problems a business can bring.
3. Genuine project/work image and one approved example: equipment, problem and actual scope. Do not invent outcomes or name clients without permission.
4. Brief capabilities/credibility: company experience, confirmed technical backing and supplied credentials only.
5. A single final inquiry block: WhatsApp, email and phone. Ask for equipment, problem and location. Keep the existing site's preference against repeated CTA blocks; a header Contact link can reach this block.
6. Business identity, office information and accessible privacy notice.

Keep the homepage's short generic service paragraphs. This page supplies paid-search context without adding lengthy explanations to all 32 scopes. Avoid a duplicate “PLC page” unless it provides distinct content and a distinct customer need. Proposed future marine route: `/layanan/otomasi-kapal/`; hold it until evidence warrants it.

### 9.3 Route and SEO safeguards

New routes require generator output, canonical/title/description and language configuration, deployment routing/allowlist updates, link validation and live verification; adding a source file alone will not make the route reachable. `shell()` currently assumes one directory depth, so nested `/layanan/.../` assets and navigation need root-relative production URLs or computed depth. Retain correct GitHub Pages preview prefixes.

For genuinely distinct public service content, use a self-canonical and include it in the production sitemap. If a later temporary experiment duplicates existing content, choose its canonical/noindex strategy deliberately. Preserve old scope hashes and compatibility behavior. Never make an ad final URL a 200-status JavaScript redirect, the retired `/araya/`, a preview link or the `.com` forwarding domain. Google requires working, crawlable, matching destinations; organic indexing itself is not a prerequisite for running a Search ad. [Google: destination requirements](https://support.google.com/adspolicy/answer/6368661?hl=en).

## 10. Conversion tracking architecture

### 10.1 Proposed setup

```text
Google Search ad → direct .co.id destination with auto-tagging / approved URL parameters
    → consent-aware production GTM container → one GA4 Google tag
    → classified contact-click events (secondary)
    → actual inquiry received in WhatsApp / phone / email
    → restricted inquiry register + human qualification
    → supported, deduplicated offline qualified-lead import where attribution exists

Optional later: approved form → successful delivery response → generate_lead
```

Use GTM as the single tag installation path. Do not install direct `gtag.js` alongside an equivalent GTM Google tag. Add the approved container through `tools/build.py` only for production; previews/local development should not send data to the production property. Container and measurement IDs are public identifiers, but API credentials and CRM/export secrets must never enter static JS or Git.

Configure the Google tag for GA4 and the required Ads destination. Confirm click-ID persistence with the Google tag's linking capability; add a separate Conversion Linker only if required by the chosen configuration. Google's current guidance says a container that loads a Google tag on every page does not also need a Conversion Linker tag. [Google: Conversion Linker](https://support.google.com/tagmanager/answer/7549390?hl=en).

### 10.2 Event specification

| Event / record | Exact condition | Allowed non-personal dimensions | Ads role |
|---|---|---|---|
| `page_view` | Normal page load; one owner for automatic page-view firing | Page path, sanitised location | Diagnostic only |
| `contact_click` | One user click on an allowlisted WhatsApp, tel or mailto link | `contact_method`, `cta_location`, `service_group`, `landing_section` | Secondary; separate observation actions by method if useful |
| `service_detail_open` | User opens a service disclosure | `service_group` | Optional diagnostic; not a lead |
| `generate_lead` | Optional future form receives a confirmed successful response from the submission/delivery service | `form_id`, `service_group`; no entered text | Provisional primary only when selected instead of qualified-lead optimisation |
| `qualified_lead` | Human verifies a unique inquiry and its scope | Recorded in restricted business register; approved supported import fields only | Preferred primary once attribution/import is validated |
| `quote_issued` / `won_work` | Sales record reaches that stage | Internal lead/order reference, genuine value if maintained | Later business reporting; do not count every stage as another primary acquisition |

For click classification inspect the actual clicked anchor via `closest('a[href]')`; accept the exact WhatsApp host/number and company `tel:` / `mailto:` targets. Use static data attributes for CTA location and service classification rather than sending link text, full URLs, phone numbers or message text. A shared footer contact click does not prove which service is wanted; retain `unknown` unless the page/entry context supports a category.

GA4 enhanced measurement can already emit outbound `click` events for WhatsApp. Either disable automatic outbound measurement for this controlled setup or keep it diagnostic and exclude it from lead/key-event imports; make one deliberate `contact_click` event the canonical contact metric. Do not attach both a custom-JS click listener and a second GTM link trigger that fire the same event. [Google: outbound clicks](https://support.google.com/analytics/answer/13566436?hl=en).

If a form is added, neither a submit-button click nor automatic `form_submit` proves successful delivery. Fire the lead event after confirmed acceptance and a unique submission reference; handle errors without firing it. Reopening or refreshing a success page must not create another lead. [Google: enhanced measurement events](https://support.google.com/analytics/answer/9216061?hl=en).

### 10.3 Primary actions, deduplication and attribution limits

- Set inquiry-type Ads actions to **Count: One** where supported. This limits repeat conversions per ad interaction/action; it does not deduplicate the same prospect across phone, WhatsApp, forms and offline imports. Use the business register to merge duplicates. [Google: counting options](https://support.google.com/google-ads/answer/3438531?hl=en).
- Choose one primary acquisition stage for a campaign. Prefer qualified lead when measurable; otherwise a successful form lead can be provisional. Keep earlier contact clicks and later sales stages secondary unless the bidding objective is deliberately changed.
- Import a given online outcome once: choose GA4 import or a native Ads conversion tag as its primary measurement source. Do not count both. Keep any comparison action secondary and clearly labelled.
- Configure campaign goals explicitly. A secondary action can still enter bidding if placed in a custom goal; avoid that configuration. Confirm settings after GA4 imports rather than trusting defaults. [Google: primary/secondary actions](https://support.google.com/google-ads/answer/11461796?hl=en).
- Set a documented conversion window based on the observed sales cycle; a 30-day starting hypothesis needs owner/account review. Store inquiry/qualification times with timezone. Imports remain subject to supported identifiers, windows, eligibility and diagnostics.

**WhatsApp limitation:** website JS sees the departure click, not the message, conversation, equipment details or qualification. Ordinary `wa.me` links do not automatically send a GCLID back to Araya. Do not claim click-to-chat-to-sale attribution without an implemented correlation mechanism.

For the pilot, staff can record source and an optional non-personal reference supplied by the customer. A campaign/service marker in a reviewed prefilled message can help classify voluntarily sent inquiries, but the user can remove it and the marker is not proof of a unique paid click. Record such attribution as “self-reported/reference”, separate from deterministic matched attribution.

For later deterministic imports, an approved form or secure lead workflow must associate an opaque reference with a supported click ID in a restricted first-party record. A manually maintained private spreadsheet can be the lead register; no website database is required. Do not put raw GCLID or personal details in WhatsApp message URLs, public analytics dimensions or committed files. Do not infer a match just from similar timestamps. Without a link between inquiry and click, mark it **unattributed** and do not upload a fabricated match.

Google currently documents up to 90 days from the associated click for GCLID offline uploads and 63 days for enhanced lead conversions; the selected conversion window may be shorter. Validate the current Data Manager/import method in the account and upload promptly. Enhanced conversions involve user-provided data and require separate privacy/permission decisions; hashing does not make collection anonymous. They are not the initial default. [Google: offline import guidance](https://support.google.com/google-ads/answer/15081888?hl=en), [GCLID setup](https://support.google.com/google-ads/answer/7012522?hl=en).

**Phone:** Indonesia appears in Google's current forwarding-number availability list. This does not prove availability for Araya's account or number. Test call asset/website call reporting and routing before use. Use a verified connected-call outcome as secondary initially; a duration threshold is not qualification. Match qualified calls through a supported process, without counting both call and qualified-call stages as primary. If unavailable, retain tel-click observation and a manual inquiry log. [Google: forwarding numbers](https://support.google.com/google-ads/answer/2382961?hl=en).

### 10.4 Campaign parameters

Enable Ads auto-tagging. Use a **final URL suffix**, not an unnecessary redirecting tracking service. Proposed suffix, with no leading `?`:

```text
utm_source=google&utm_medium=cpc&utm_campaign=araya_ej_services&utm_id={campaignid}&utm_content={adgroupid}_{creative}&utm_term={keyword}&adgroup_id={adgroupid}&match_type={matchtype}&device={device}&network={network}
```

`{keyword}` identifies the matched keyword where supplied, not necessarily the user's actual query. `{creative}` is the ad identifier. Use Ads reports for campaign/ad-group/keyword breakdown; retain a readable name-to-ID configuration. Empty/unsupported fields must be handled. GA4 does not automatically expose every arbitrary query parameter as a report dimension; explicitly map only useful non-personal fields. [Google: ValueTrack](https://support.google.com/google-ads/answer/6305348?hl=en).

Test the expanded URL in Ads: the query must precede the fragment, for example `https://arayainternusa.co.id/?utm_source=google&utm_medium=cpc#automation-plc`. Auto-tagging adds applicable click IDs; do not manufacture them. Avoid duplicate UTM parameters or manual values that conflict with the intended linked Ads attribution. Initial landing-section context must be captured deliberately because fragment navigation need not create a new page view.

Internal links sometimes navigate from `/` to `/index.html` without the original query. Preserve entry attribution through the approved consent-aware tag/session design before navigation; do not add UTMs to internal links and reset acquisition attribution. Verify GCLID and applicable `gbraid`/`wbraid` handling through supported Google tooling rather than manually copying IDs everywhere. Query loss on `.com`, legacy `.co.id/araya/` and JS compatibility redirects is documented separately (D05). [Google: sitewide-tag troubleshooting](https://support.google.com/google-ads/answer/9148089?hl=en).

### 10.5 Privacy and data controls

Publish an accessible notice explaining company identity, inquiry handling, analytics/advertising recipients, purposes, retention, choices and a contact route before activating the planned tracking. Review applicable Indonesian privacy requirements with the business's responsible adviser; this document does not determine legal compliance.

Choose and document the consent approach before tags load. Conservative baseline: block nonessential Google measurement until the relevant permission is granted, retain normal contact functionality if declined, and offer an accessible way to change the choice. GTM is not a consent banner. Consent Mode communicates choices and changes tag behavior; advanced mode can send cookieless signals, so it is not equivalent to no data transfer. Google has specific EEA/UK/Switzerland obligations for users there, even when the advertising target is Indonesia. [Google: Consent Mode](https://developers.google.com/tag-platform/security/concepts/consent-mode), [EU user consent policy](https://www.google.com/about/company/user-consent-policy/).

Do not send names, email addresses, personal phone numbers, message text, drawings, uploaded equipment documents or form contents to GA4. Redact sensitive URL/referrer parameters before collection; avoid generic form variables or full contact URLs. Keep raw click IDs only in approved restricted attribution records. Configure retention and least-privilege account access; review Google Signals, advertising personalisation and automated user-provided data collection before enabling any of them. Do not enable remarketing or automatic enhanced-conversion field scraping by default. [Google: PII prevention](https://support.google.com/analytics/answer/6366371?hl=en), [GA4 data redaction](https://support.google.com/analytics/answer/13544947?hl=en).

### 10.6 Verification before launch

Use staging/test properties and GTM Preview/Tag Assistant, followed by controlled production checks with appropriate consent. Confirm one page view, one event per contact click, correct method/location, no PII, rejection/withdrawal behavior and no production data from preview/local builds. Do not send real WhatsApp inquiries as an automated test. A synthetic GCLID can test preservation but cannot establish Ads attribution.

If a form/import is introduced, test success, failure, retry, double-click, refresh, deduplication and rejected imports. Verify one approved real attributed outcome through Ads diagnostics when permitted; sandbox events alone cannot prove a full paid-click match. Exclude internal/debug activity and compare inquiry records with reported outcomes after allowing processing time. Record expected differences caused by consent, blocked tags, attribution windows, reporting dates and unmatchable inquiries.

## 11. Website technical improvements

**Priority meanings:** Critical = required before this plan's measured pilot; Recommended = likely improvement or robustness work; Optional = future enhancement. A conditional Critical item is required only if that route/feature is selected. These are readiness recommendations, not assertions that Google mandates every feature.

### 11.1 Developer backlog

Paths below are relative to the inspected repository root. Edit generators/assets, then regenerate through the existing workflow; do not hand-edit only generated HTML.

| ID / priority | Issue | Proposed solution | Relevant files / components | Expected benefit / acceptance evidence |
|---|---|---|---|---|
| **D01 Critical** | No measurement integration. | Production-only GTM installation and one Google tag path; preserve static runtime and preview isolation. | `tools/build.py` shared `shell()`; build target configuration; `tools/test_production.py`, `tools/test_experience.py` | Tag Assistant shows one installation and no production hits from preview/local builds. |
| **D02 Critical** | Contact clicks have no classification or outcome distinction. | Add stable CTA metadata and one delegated click-event pathway; optional initial service/landing-section context. Keep hrefs functional with blocked JS/tags. | `tools/build.py` hero/contact/footer/`whatsapp()`; `public/assets/site.js` or a small dedicated tracking asset; `tools/landing_services.py` only if metadata needed | One sanitised event per interaction; no duplication, navigation delay or false lead event. |
| **D03 Critical** | No linked privacy notice/consent behavior for planned tags. | Generate `/privacy/`, link in footer, implement approved consent controls before measurement activation; preserve untracked contact use. | `tools/build.py`; `public/assets/site.css`; small consent asset if needed; `tools/production.htaccess`; `tools/deploy_release.php` route assumptions; build/package/check tests | Notice reachable; deny/grant/withdraw verified; no undisclosed automatic field capture. New route supported through deployment validation. |
| **D04 Critical for selected ad URLs** | Attribution can be lost in redirects/navigation; no dedicated checks. | Test canonical final URLs with query + fragment. Capture supported click/session data before internal navigation, subject to consent. Add redirect and paid-entry regression checks. | `tools/check_live.py`, `tools/test_live_checks.py`, `tools/test_navigation.cjs`; tracking configuration and shared shell | Actual Ads expanded URLs preserve identifiers and open the intended scope; direct primary entry already passed HTTP/browser probes. |
| **D05 Recommended; Critical if used by paid traffic** | `.com` sends paths/queries to root; legacy QSD and compatibility JS drop query. | Review `.com` forwarding in hosting, preserve equivalent supported paths and approved attribution parameters. Deliberately revise legacy query handling without enabling old files/PHP; preserve compatibility hash mapping and query in JS. | Rumahweb/cPanel domain redirect (outside Git); `tools/production.htaccess`; `public/assets/service-redirect.js`; `tools/check_live.py` and redirect tests | `.com/noris/` → `.co.id/noris/`; synthetic parameters survive supported redirects. Unknown/retired paths remain properly rejected. Do not blindly preserve unsafe legacy routing. |
| **D06 Recommended** | English generic page is a weak match for specific Indonesian automation ads. | One focused `/layanan/otomasi-industri/` page using real scope/evidence, concise Indonesian copy and one final inquiry block. Confirm regional service availability. | New generator/helper under `tools/`; `tools/build.py` including depth-safe URLs/lang/canonicals; `tools/site_content.py`; `tools/production.htaccess`; `tools/deploy_release.php`, `tools/package_release.py` and route validators | New page loads directly, assets/links work at nested depth, service match is clear, mobile CTA reachable. No duplicate/thin pages. |
| **D07 Recommended** | All sampled resources require revalidation; performance baseline unavailable. | Measure actual waterfall first; apply differentiated HTML/asset caching and content-hashed names before immutable caching. Retain compression and hero priority; adjust eager below-fold images only if trace shows contention. | `tools/production.htaccess`; `tools/build.py` asset versioning; `tools/prepare_site_assets.py`, `tools/prepare_work_photos.py` as needed; `tools/test_loading.py`, deployment hash/cache checks | Repeated loads reduce revalidation without stale releases; measured mobile LCP/interaction results documented before scaling. No unsupported speed-score promise. |
| **D08 Recommended** | Logos/counts lack service-specific project context. | Add one or two owner-approved examples with factual equipment, scope and image; publish exact credentials only when supplied. Keep leadership before Contact. | `tools/site_content.py`; landing generator; existing responsive images / `tools/prepare_work_photos.py`; content-source docs | Buyers can connect experience to requested work; no invented outcomes, approvals or testimonials. |
| **D09 Optional** | No successful website form outcome or deterministic form-to-lead join. | Only if approved: lightweight delivery endpoint/provider, minimal company/contact/service fields, success reference, abuse protection and failure handling; no database required. Do not expose mail/API secrets in JS. | New form component + reviewed delivery service; `tools/build.py`; production route/packaging/security checks; GTM | Confirmed lead receipt and deduplication. Static thank-you visit alone cannot trigger conversion. |
| **D10 Optional; required before qualified-lead bidding** | No demonstrated click-to-qualified-inquiry link. | Secure reference/click-ID capture and private lead register/import workflow, with consent and retention controls. Keep unmatched inquiries visible. | Future approved form/delivery integration; private CRM/register and Google Ads Data Manager configuration; implementation documentation | Reconciled qualified leads accepted by Ads; duplicates/rejected records reviewed. No raw lead data in Git/GA4. |
| **D11 Recommended** | New tracking/content could regress existing responsive behavior. | Bounded mobile, keyboard and navigation QA; preserve focus, reduced motion, native disclosures and existing image dimensions. | `public/assets/site.css`, `site.js`; `tools/test_hierarchy.py`, `tools/test_navigation.cjs`, `tools/test_loading.py`, `tools/test_experience.py` | Home and both brand pages plus paid destinations remain usable; test menu/contact at 320/390/768/1280 widths. No full redesign. |
| **D12 Optional** | Sitemap lastmod follows build date even for unrelated deployments. | Derive dates from substantive page changes, or omit when unknown; retain production canonicals/indexing and preview noindex. | `tools/build.py` sitemap generation; `tools/test_production.py` | More trustworthy crawl metadata; no claim of direct Ads performance improvement. |

The D03/D06 route work must inspect deployment allowlists/tests rather than assuming all arbitrary HTML paths are served. D05 must retain private WordPress backups and current denial rules. No VM, new frontend framework, database or company-profile download is needed for these improvements.

### 11.2 Manual platform / business work

| ID / priority | Owner | Required action |
|---|---|---|
| **M01 Critical** | Ads administrator + business owner | Confirm account ownership, billing/currency/timezone, advertiser verification, access roles, existing campaigns/conversions and spending approval. Do not create a duplicate account/property without checking. |
| **M02 Critical** | Ads specialist | Keyword Planner research; choose initial keywords and CPC cap; configure Search-only campaign, locations/entities, Presence, languages, schedule, negatives and reviewed ads. Keep campaign paused until launch approval. |
| **M03 Critical** | Araya sales/operations | Assign inquiry handler and backup process; verify phone/WhatsApp/email receipt; define qualification/deduplication and response targets; operate restricted inquiry register. No “local team” positioning is needed. |
| **M04 Critical** | Analytics/GTM administrator | Confirm/create appropriate GA4 property and web stream, company-controlled GTM container, timezone, Ads link, access roles, Google tag/Ads destination, event dimensions and secondary click actions. Test consent and preview isolation with developer. |
| **M05 Critical** | Ads/analytics administrator | Enable auto-tagging; test final URL suffix; explicitly configure goals/counting/windows; avoid duplicate imports and custom-goal promotion of secondary clicks. Document whether pilot has a reliable primary or uses manual qualification only. |
| **M06 Critical** | Business owner / responsible privacy adviser | Approve notices, collection/retention/consent choices, inquiry workflow and actual advertising claims. Confirm service availability and publishable credentials/project references. Review the completed plan before implementation/launch. |
| **M07 Recommended** | SEO administrator | Inspect Search Console indexing, mobile experience reports and sitemap; review Business Profile accuracy. Account access is needed; SEO visibility is not established by this audit. |
| **M08 Optional** | Sales + Ads administrator | Set up supported offline imports and review diagnostics; later consider forwarding-number reporting or enhanced conversions with appropriate permissions. |

## 12. Budget and testing strategy

### 12.1 Spending controls

- The starting **average** daily budget is Rp100,000. It is not a hard daily cap. Usual unchanged full-month campaign limit: Rp3,040,000; usual maximum billed day: Rp200,000. Served costs and billed costs can differ where overdelivery is credited. [Google: overdelivery](https://support.google.com/google-ads/answer/1704443?hl=en).
- If Rp3,000,000 is a strict full-month advertising-charge ceiling, use an average daily budget no higher than approximately **Rp98,684** (`3,000,000 / 30.4`, rounded down), subject to the account's available increments. Confirm whether the owner's ceiling includes tax/fees.
- Do not assume a 7-day trial can spend only 7 × Rp100,000. Daily variation can bring a short flight nearer 2× on individual days. Review cumulative spend during the pilot; a schedule or end date alone is not a hard total-spend cap. Alerts/manual pauses can lag. Mid-month changes and end-date changes affect the budget calculation. Google's current documentation also describes fixed-duration total budgets for Search; check availability before campaign creation if a hard flight ceiling is needed. They have different pacing, no equivalent daily cap, and cannot simply replace an existing campaign's average-daily-budget mode. [Google: budget changes and total budgets](https://support.google.com/google-ads/answer/10487143?hl=en).
- Keep all four groups under one campaign budget. The 40/25/20/15 mix is a planning benchmark; actual distribution is monitored, not guaranteed. Do not create four underfunded campaigns just to force it.

### 12.2 Test sequence

| Phase | Work and decision |
|---|---|
| Before spend | Resolve Critical tasks, validate selected URLs and tags, confirm ad language/destination fit, research bids, agree qualification and total test exposure. No launch under this audit task. |
| Days 1–3 after separately approved launch | Check spend, location settings, disapprovals, query relevance, event duplication and inquiry handling daily. Pause immediately for broken destination, incorrect tracking, material irrelevant traffic or budget/control errors. |
| Days 4–14 | Review search terms and negatives two or three times a week, with extra checks if spend rises. Track service/location and actual qualification. Avoid changing multiple variables at once. |
| Weeks 3–4 | Reconcile inquiries and outcomes, allowing qualification delay. Review ad group cost share, devices, hours and geography. Decide keep/refine/pause; sparse data is inconclusive, not success or failure. |
| After a complete qualification cycle | Consider bidding/landing tests only when primary outcomes are reliable. Expand a service/area only with demand, capacity, budget and acceptable observed economics. |

Search-term reports may omit some queries. Label relevance estimates as based on visible/reviewed terms rather than claiming all clicks are explained. Review attributed and unattributed leads, duplicate rate and response delay together.

### 12.3 Decision metrics and economics

Keep a weekly sheet with spend, clicks, CPC, impressions, CTR, contact clicks by channel, actual unique inquiries, qualified inquiries, matched attribution rate, quotes and wins. Separate Ads click-date reports from inquiry/qualification-date records when reconciling.

`Cost per qualified inquiry = attributable ad spend / unique attributed qualified inquiries`. If there are none, report “no qualified inquiries yet” plus spend; do not display Rp0 CPL. Also report total spend and unmatched inquiries so partial attribution does not look complete. Event counts are not unique leads.

An owner-defined ceiling can be calculated from **expected contribution margin per won job × qualified-inquiry-to-win rate × the acceptable acquisition-spend fraction**. Use actual business data and a conservative sales-cycle allowance. No numerical ceiling or forecast is supplied because those inputs are unknown.

Pause/repair on technical faults. Exclude clearly irrelevant queries promptly. Investigate service mismatch, slow response or weak landing relevance before merely raising bids. If a keyword/group reaches its pre-agreed test-spend limit without qualified leads after the normal delay, pause and review it; choose that limit from approved economics, not an invented industry benchmark. High CTR with poor inquiry quality is not a reason to expand.

## 13. Future expansion plan

| Expansion | When / structure |
|---|---|
| Mojokerto, Pasuruan | Add to the existing regional campaign if the same services, delivery economics, hours and landing proposition apply. Validate demand and map entities first; track new areas separately in reports. |
| Jakarta | Separate regional campaign when staffing, schedule, service capacity, bids or spending accountability need independent control. Use verified Jakarta business details; do not invent a full address beyond the supplied Townhouse PIK information. |
| Batam | Research marine/industrial demand and travel/delivery capability first. Usually consider a separate regional or marine campaign if its economics differ; not an automatic nationwide expansion. |
| Marine focus | Split from industrial only when demand, primary outcomes and budget justify independent prioritisation. Provide actual marine evidence/landing content. |
| Noris / ComAp procurement | Separate brand-intent structure with `/noris/` and `/comap/`, product availability and appointment wording confirmed. Research distributor, sensor, controller and spare-part intent individually. Do not imply Araya is the manufacturer. |
| Additional service pages | Add only for distinct recurring needs with original evidence; no cloned city doorway pages or near-identical PLC/automation pages. |
| Conversion bidding | Introduce after reliable outcome capture and an understood qualification cycle; assess whether added volume stays qualified. |
| Remarketing, Display, Performance Max | Optional later evaluation with privacy, attribution and budget readiness. Not part of the proposed initial Search test. |

Expand one major dimension at a time. A new city can be added within the existing campaign when the proposition/economics are shared; use a separate campaign when independent budget, location, operating hours, goals or sales ownership is necessary. Additional campaigns require additional viable budget, not simply reallocating Rp100,000 across many tiny tests.

## 14. Implementation checklist

### 14.1 Completed for this planning task

- [x] Read the full brief, repository conventions and current source.
- [x] Inspect live homepage, services/contact journey and both brand introductions on mobile; capture desktop home.
- [x] Check production routes, metadata, canonical/indexing signals, robots/sitemap and bounded internal destinations.
- [x] Verify secondary-domain redirects, including query and brand-path loss.
- [x] Inventory tags/forms and inspect resource delivery; record PageSpeed quota limitation without invented scores.
- [x] Research current Google platform rules using official documentation.
- [x] Prepare campaign/keyword/RSA/landing/tracking/budget proposals and prioritised ownership.
- [x] Save plan locally; no production-code edits, push, deployment, account creation or campaign launch.

### 14.2 Developer implementation, only after separate approval

- [ ] D01–D04: measurement, stable contact metadata, privacy/consent and selected-URL attribution tests.
- [ ] D05: coordinate hosting redirect fixes; preserve legacy security and bookmarks.
- [ ] D06–D08: prioritise focused Indonesian service content, measured caching improvements and owner-approved proof.
- [ ] D11: mobile/keyboard/navigation verification across home, brands and paid destinations.
- [ ] Keep D09/D10/D12 conditional; do not add form/CRM dependencies merely to complete a checklist.
- [ ] Run existing relevant checks and a production build in an isolated output; verify generated routes/links and release package allowlists.
- [ ] Inspect workflow triggers before any PR. Current workflows have no PR triggers; retain default-branch push checks/deployment. Do not put skip-CI instructions in merge commits.
- [ ] Obtain implementation/deployment authorisation at the appropriate next step; the current brief explicitly prohibits deployment. Preserve existing backups and rollback capability.

### 14.3 Manual platform and business configuration, after approval

- [ ] M01: confirm account/billing/access/verification and inspect existing assets first.
- [ ] M02: export Keyword Planner research; agree keywords, negatives, CPC cap and exact location entities.
- [ ] M03: verify contact delivery, handling responsibility and qualification register.
- [ ] M04–M05: configure/link GA4/GTM/Ads; test deduplication, consent, goals and auto-tagging.
- [ ] M06: approve claims, privacy and the pilot's spending exposure; clarify whether Rp3m includes taxes.
- [ ] Review Indonesian and English ad drafts and actual destination language.
- [ ] Keep campaign paused until a separate explicit launch instruction and all selected readiness gates pass.
- [ ] Record a baseline, verification evidence, stop conditions and first review date at launch.

### 14.4 Inputs still required

Google Ads/Keyword Planner access or exports; any existing GA4/GTM/Search Console details; billing/tax treatment; acceptable total test spend and inquiry economics; who receives/qualifies inquiries; actual response and sales-cycle data; supported PLC/drive platforms; publishable project examples; exact certification/appointment records if those claims enter ads; and approval of the proposed privacy/consent approach.

**Review decision:** approve or revise the strategy and Critical implementation scope first. No live campaign or production change follows automatically from this document.

## 15. Subsequent authorised implementation — 23 October 2026

The owner subsequently authorised consent/contact tracking installation, Analytics–Ads linking and verification, while explicitly prohibiting an Ads launch. This supersedes the original audit-only restriction for that specific implementation scope. GA4 property 560191836 is now linked to Ads account 115-719-0739 with personalisation disabled. GTM-NK3C3RVZ version 2 is published with consent-required base/contact tags and user-provided data detection disabled. Website source e0992aa was deployed through successful main CI/CD; the live verifier checked 78 exact file hashes and protected routes. GA4 Realtime received one test event each for WhatsApp, email and phone. Consent refusal, grant, persistence and withdrawal were verified; three event-scoped reporting dimensions are registered. Ads remains at zero campaigns/drafts and IDR0/day. Full implementation details, findings, evidence and remaining business gates: [Consent and contact measurement](docs/CONSENT-TRACKING-2026-10-23.md). Campaign research, spending approval, actual enquiry qualification and any advertising launch remain separate unfinished work.
