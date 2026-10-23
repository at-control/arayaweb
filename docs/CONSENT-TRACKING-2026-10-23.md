# Consent and contact measurement — 23 October 2026

## Approved scope and implementation plan

The owner authorised installation, Ads linking and verification, with **no advertising launch**. This implements section 10 of GOOGLE_ADS_PLAN.md. Preserve the static design, short service copy, existing navigation, main-only CI/CD, backups and rollback.

- [ ] Add a shared, accessible consent banner with equally available Accept analytics and Reject optional actions, a linked privacy notice and a persistent footer control. Remember the choice for 180 days; handle unavailable storage safely.
- [ ] Load GTM-NK3C3RVZ only on the HTTPS production host after analytics consent. Queue denied defaults, then analytics-only grant before loading GTM; advertising storage, personalisation and user-data consent remain denied. Preview/local builds send no production events.
- [ ] Add one delegated allowlisted contact listener; contact_click includes method and static CTA/page context, never phone/email/message contents or arbitrary URL/text. Rejecting consent never blocks contact links. Do not replay pre-consent clicks.
- [ ] On withdrawal disable collection, clear GA cookies and reload to unload Google scripts. Synchronise withdrawal between tabs. Avoid duplicate initialisation and duplicate listeners.
- [ ] Add /privacy/ to generator, route/package validation and guarded deployment aliases; explain Analytics, contact handling, choice storage and withdrawal without inventing certification, retention, CRM or legal claims.
- [ ] Configure GTM contact-event tag, consent requirement and bounded event parameters. Link GA4 property 560191836 only to Ads customer 115-719-0739; disable advertising personalisation and leave campaigns inactive. Contact clicks remain secondary observations, never qualified leads.
- [ ] Verify refusal/grant/persistence/withdrawal, storage failure, preview isolation, exact contact allowlists, page-view duplication, attribution handling, mobile layout and keyboard access. Run existing CI gates and deployment fixtures.
- [ ] Publish the checked container and deploy the checked website through main CI/CD. Verify live routes/assets and Google diagnostics; record exact results and limits here. Do not create or enable a campaign.

## Interfaces and files

- tools/measurement.py: shared markup and privacy content; tools/build.py: target-aware injection and generated privacy route.
- public/assets/measurement.js: consent lifecycle and a single contact_click dataLayer event.
- public/assets/measurement.css: banner/notice styles scoped to this feature.
- tools/test_measurement.cjs: state/lifecycle/contact boundary tests; tools/test_tracking_build.py: production/preview and privacy package checks.
- GTM: GA4 - Araya - Base plus GA4 - Contact click, using the same production stream G-WMBDHTFPBJ. No direct duplicate gtag.js install and no native Ads conversion tag duplicating a GA4 outcome.

## Verification focus

Unknown, expired, corrupt or unavailable preference storage means no Google loading. A preview with copied accepted storage still cannot load production tags. Nested SVG clicks resolve to their anchor; external lookalike WhatsApp hosts and unrelated telephone/email targets are ignored. Contact functionality remains ordinary link navigation. Withdrawal unloads measurement and revokes the choice across tabs. New privacy routing must be allowed and hashed through the existing immutable deployment path.

## Progress and evidence

### Local implementation and review

Implemented shared consent, a privacy notice, footer choices, production-only GTM loading and allowlisted contact metadata. No database, form or company-profile download was added. Consent lasts 180 days. Withdrawal disables GA, removes accessible measurement cookies and reloads to unload Google listeners; cross-tab withdrawal is handled. Local and GitHub preview builds cannot load production Google scripts even after acceptance.

The independent code review identified three issues, all corrected with regression checks:

1. Both measurement assets are now mandatory in the Python and PHP immutable-package validators. The SSH activation alias list also includes the new privacy route.
2. Analytics page-location overrides drop fragments, arbitrary parameters and free-text UTM values. Only approved source/medium/campaign labels and bounded click IDs survive. Currently approved labels: source `google` / `araya_audit`, medium `cpc` / `diagnostic`, campaign `araya_ej_services`. New campaign labels require an explicit allowlist update; `utm_term`, `utm_content` and `utm_id` are excluded. The actual visitor URL is unchanged. This reduces accidental PII transmission; it cannot identify a deliberately disguised personal value in an otherwise valid click-ID field.
3. The banner appears directly after Skip to content in the DOM, before the header, so keyboard users reach the choices early. Reopening from the footer focuses Reject optional; Escape returns focus to Privacy choices.

Observed red-to-green checks for attribution filtering, early consent tab order and required package assets. Runtime unit tests cover unknown/rejected/accepted/corrupt/expired/future preferences, inaccessible storage, exact contact allowlists, no pre-consent click replay, repeat acceptance, withdrawal and cross-tab clearing.

### Google configuration saved and published

Browser attachment initially failed in both Edge and the in-app browser. The owner's latest tab reattachment restored browser-only control; no whole-screen automation was used.

- GA4 property **560191836**, stream **16182653195**, measurement **G-WMBDHTFPBJ** is linked to Ads **PT Araya Internusa / 115-719-0739**. The completed link is visible in Analytics. Personalised advertising OFF; optional embedded Analytics-editing access from Ads OFF; auto-tagging enabled through the link setup. The unrelated cancelled account was not selected.
- GTM **GTM-NK3C3RVZ**, version **2**, **Araya consent-based Analytics and contact clicks**, published 23 October 2026 at 07:49 WIB. Two tags, one custom trigger, three data-layer variables and two settings.
- Base tag **GA4 - Araya - Base**: Google Analytics template, G-WMBDHTFPBJ, Initialization - All Pages, additional `analytics_storage` consent required.
- Event tag **GA4 - Contact click**: GA4 event `contact_click`, parameters `contact_method`, `cta_location`, `page_group`, each mapped through its same-name Data Layer Variable (version 2). Additional `analytics_storage` required. Trigger **CE - contact_click** matches the exact event and Page Hostname equals `arayainternusa.co.id`.
- Automatic event setting: scrolls ON; history page views, outbound clicks, form interactions, video and file downloads OFF. GA4 stream enhanced measurement had already been limited to page views and scrolls.
- Publication review found the new template had created an enabled **Allow user-provided data capabilities** setting with automatic personal-data detection. Both controls were explicitly disabled and saved before publication. No extra read-only destination account access was granted.
- No native Ads conversion tag, campaign, audience or bidding goal was created. Contact clicks are observations, not verified enquiries; no primary lead conversion has been declared.

### Browser and source verification before website deployment

- Desktop screenshot inspected; mobile viewport override tested at 390 × 844 (375 CSS px content width with browser scrollbar). Banner text/buttons fit; privacy notice is readable. Viewport override reset afterwards.
- Keyboard: Skip to content → Privacy notice → Reject optional. Footer reopen/escape returns focus correctly.
- Refusal persists across reload; acceptance persists across reload; footer reopen reports the saved status. Local preview had zero Google script elements both before and after acceptance. This DOM check verifies script installation, not a full network trace.
- Passing: `node tools/test_measurement.cjs`, `python tools/test_tracking_build.py` (2), production (5), experience (6), hierarchy (4), loading (3), release candidate (6), live-verifier fixtures (5), JavaScript syntax and PHP package/provenance/hash/symlink-refusal fixtures. Linux activation fixtures require CI and are not claimed as locally executed on Windows.
- Workflow triggers remain main push / manual / post-build; no PR-triggered workflow was added. Website publication and live Google ingestion verification remain pending at this checkpoint.

### Evidence and next steps

Screenshots are stored outside the public deployment tree in `../docs/evidence/google-ads-audit-20261021/`:

- `ga4-ads-linked-20261023.png`: successful link to the correct Ads account.
- `gtm-v2-live-20261023.png`: published GTM version summary.
- `consent-mobile-20261023.png`: mobile consent banner and keyboard focus.

Next: run final source/build gates, commit/push the authorised website installation, watch immutable CI/CD, verify live files/redirects/privacy and actual Google collection after consent, check no collection before consent/after withdrawal, and recheck Ads has no enabled campaigns. Do not launch ads. Google reports can lag; distinguish browser/tag diagnostics from processed reporting.
