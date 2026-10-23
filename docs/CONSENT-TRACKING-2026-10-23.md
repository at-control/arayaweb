# Consent and contact measurement — 23 October 2026

## Approved scope and implementation plan

The owner authorised installation, Ads linking and verification, with **no advertising launch**. This implements section 10 of GOOGLE_ADS_PLAN.md. Preserve the static design, short service copy, existing navigation, main-only CI/CD, backups and rollback.

- [x] Add a shared, accessible consent banner with equally available Accept analytics and Reject optional actions, a linked privacy notice and a persistent footer control. Remember the choice for 180 days; handle unavailable storage safely.
- [x] Load GTM-NK3C3RVZ only on the HTTPS production host after analytics consent. Queue denied defaults, then analytics-only grant before loading GTM; advertising storage, personalisation and user-data consent remain denied. Preview/local builds send no production events.
- [x] Add one delegated allowlisted contact listener; contact_click includes method and static CTA/page context, never phone/email/message contents or arbitrary URL/text. Rejecting consent never blocks contact links. Do not replay pre-consent clicks.
- [x] On withdrawal disable collection, clear GA cookies and reload to unload Google scripts. Synchronise withdrawal between tabs. Avoid duplicate initialisation and duplicate listeners.
- [x] Add /privacy/ to generator, route/package validation and guarded deployment aliases; explain Analytics, contact handling, choice storage and withdrawal without inventing certification, retention, CRM or legal claims.
- [x] Configure GTM contact-event tag, consent requirement and bounded event parameters. Link GA4 property 560191836 only to Ads customer 115-719-0739; disable advertising personalisation and leave campaigns inactive. Contact clicks remain secondary observations, never qualified leads.
- [x] Verify refusal/grant/persistence/withdrawal, storage failure, preview isolation, exact contact allowlists, page-view duplication, attribution handling, mobile layout and keyboard access. Run existing CI gates and deployment fixtures.
- [x] Publish the checked container and deploy the checked website through main CI/CD. Verify live routes/assets and Google diagnostics; record exact results and limits here. Do not create or enable a campaign.

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
- Three event-scoped GA4 custom dimensions were saved and verified in the definitions table: **Contact method → contact_method**, **CTA location → cta_location**, **Page group → page_group**. Regular reporting needs processing time; Realtime already received the parameters. No click event was promoted into a primary Ads bidding goal or a qualified-lead key event.

### Browser and source verification before website deployment

- Desktop screenshot inspected; mobile viewport override tested at 390 × 844 (375 CSS px content width with browser scrollbar). Banner text/buttons fit; privacy notice is readable. Viewport override reset afterwards.
- Keyboard: Skip to content → Privacy notice → Reject optional. Footer reopen/escape returns focus correctly.
- Refusal persists across reload; acceptance persists across reload; footer reopen reports the saved status. Local preview had zero Google script elements both before and after acceptance. This DOM check verifies script installation, not a full network trace.
- Passing: `node tools/test_measurement.cjs`, `python tools/test_tracking_build.py` (2), production (5), experience (6), hierarchy (4), loading (3), release candidate (6), live-verifier fixtures (5), JavaScript syntax and PHP package/provenance/hash/symlink-refusal fixtures. Linux activation fixtures require CI and are not claimed as locally executed on Windows.
- Workflow triggers remain main push / manual / post-build; no PR-triggered workflow was added. Website publication and live Google ingestion verification remain pending at this checkpoint.

### Production installation and live verification — completed

- Source commit **e0992aa8407ab9701a1cc70510fca7272cba12ff**, pushed to main with no skip-CI instruction.
- [Build/preview run 39880644654](https://github.com/hakiimm8/arayaweb/actions/runs/39880644654) succeeded. Linux CI also passed atomic activation, stale rollback refusal, static/legacy rollback and filesystem guards; these cover the activation fixtures unavailable in Windows.
- [Production run 39880685917](https://github.com/hakiimm8/arayaweb/actions/runs/39880685917) succeeded. Release **e0992aa8407ab9701a1cc70510fca7272cba12ff-39880685917-1** activated at 07:53:10 WIB. Previous release **f4a3803d438ba0ff0d0b909bacba5c9bf23042cc-38673578168-1** remains available for guarded rollback. Original WordPress backups were not modified.
- CI's live verifier passed **78 exact file hashes**, all four indexable routes, canonical/legacy redirects, retired downloads and protected paths. Privacy is served at `https://arayainternusa.co.id/privacy/`.
- The live HTTPS page reports production mode with zero Google script elements before consent. Refusal persists after reload with zero Google scripts. Accepting loads GTM. Tag Assistant then connected to the correct container and showed the base tag firing once for that document.
- Actual Page View and contact hits use **G-WMBDHTFPBJ**. Hit Details shows the sanitized `page_location` retaining only the diagnostic source/medium, with the debug parameter removed, and origin-only referrer. The non-personalised-ads flag is 1. The contact event contains `contact_method=whatsapp`, `cta_location=hero`, `page_group=home`; no phone, email, arbitrary link URL or message contents appear in that contact payload.
- Tag Assistant's contact-event Consent table confirms `analytics_storage=Granted`, while `ad_storage`, `ad_user_data` and `ad_personalization` remain **Denied** (default, update and current state as applicable).
- GA4 **Realtime received all three real link activations exactly once** in this test: `whatsapp=1`, `email=1`, `phone=1`. The WhatsApp link opened the expected contact destination; no message was sent. Email/phone link activation measured intent only; no email was sent or phone call placed. This is collection verification, not a test of sales response or message delivery.
- Withdrawal unloaded Google scripts; another reload retained refusal with zero Google script elements. After all channel checks, the normal browser tab was returned to Reject optional and reloaded, again showing zero Google scripts. The diagnostic popup was closed and Tag Assistant reports no actively debugged domains. Browser viewport override was reset.
- Ads campaign page reloaded and explicitly displayed **0 campaigns**, **0 drafts**, **no enabled campaigns** and **IDR0/day**. No ad launch, budget allocation or financial action occurred.
- Total page views across this test include deliberate reloads, back navigation and renewed consent. They must not be interpreted as customer traffic or as evidence of duplicate tagging. Tag Assistant showed one base firing and one page-view hit for the inspected accepted document.

### Evidence and next steps

Screenshots are stored outside the public deployment tree in `../docs/evidence/google-ads-audit-20261021/`:

Two selected screenshots are also retained in this repository for portable review: [mobile banner](evidence/consent-20261023/mobile-consent.png) and [GA4 receipt of all three contact methods](evidence/consent-20261023/ga4-contact-methods.png). Other diagnostic screenshots stay in the local evidence folder; they are not website assets.

- `ga4-ads-linked-20261023.png`: successful link to the correct Ads account.
- `gtm-v2-live-20261023.png`: published GTM version summary.
- `consent-mobile-20261023.png`: mobile consent banner and keyboard focus.
- `ga4-pageview-hit-20261023.png`: actual destination, page-view hit and consent encoding.
- `ga4-contact-hit-20261023.png`: contact payload contains only the bounded reporting values.
- `consent-state-20261023.png`: analytics granted, advertising categories denied.
- `ga4-realtime-contact-20261023.png`: received contact event in GA4.
- `ga4-all-contact-methods-20261023.png`: email, phone and WhatsApp, one received event each.
- `ads-inactive-20261023.png`: no enabled campaigns and IDR0/day.

### Remaining business work, outside this installation

No task blocker remains for the authorised installation and connection. Standard/custom-dimension reports can lag and were not claimed as populated. An actual paid-click attribution test is not possible without traffic and was not simulated using a fabricated click ID. Ads billing, advertiser verification, keyword/bid research, sales qualification, campaign goals and launch approval remain separate gates in GOOGLE_ADS_PLAN.md. No campaign or conversion-bidding action should be enabled from these diagnostic clicks. A true enquiry requires a received message/call and sales qualification; website clicks alone do not establish that outcome.
