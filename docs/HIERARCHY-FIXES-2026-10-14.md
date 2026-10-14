# Hierarchy fixes — implementation record

14 October 2026. Implements the owner-approved [hierarchy, mobile and navigation review](HIERARCHY-REVIEW-2026-10-14.md). Work started from `ba05ce7` on `codex/hierarchy-fixes`, in the existing owner-selected preview checkout.

## Scope and decisions

- Preserve existing colours, Space Grotesk, original SVG logo, engineering photos, manufacturer products/diagrams, project totals, automatic years and final contact destinations.
- Replace duplicate service cards/second service introduction with one set of expandable sector groups. Retain the photos inside each sector, all 30 scopes and every legacy equipment/scope anchor.
- Use shared section/group/item typography, distinct group boundaries and native disclosure chevrons. Put About's heading before its supporting photo in DOM/mobile reading order.
- Brand profile precedes the existing Contents; direct section names match Applications/Products. Noris retains two catalogue groups; ComAp retains all 18 applications and six product families. Technical application explanations precede diagrams.
- Compact FAQs/equipment briefs; enquiry CTA stays in final contact. No new shortcut or cross-brand promotion blocks.
- Measure header edge independently of the removed page-index component, track current navbar section and indicate the current brand on the closed dropdown. Keep single-row mobile branding/menu and a regular two-column client-logo grid.

## Verification ledger

- Baseline: existing experience (6) and loading (3) tests passed.
- New hierarchy tests initially failed on all four behaviours: title/media reading order, semantic sector headings/duplicate service layer, brand section naming/order and application explanation/diagram order.
- Navigation regression initially failed because header measurement was absent without page-index. New implementation passes independent offset measurement, active sections/brand, menu collapse, ResizeObserver and Back/Forward checks.
- Existing reading-flow regression updated for the approved profile-before-Contents order. Existing service-link regression now checks preserved fragment destinations, since duplicate service-card shortcuts were removed.
- During implementation, fixed a build import error by moving the existing srcset helper into shared UI components; no new dependency added.
- Current local result: hierarchy (4), experience (6), loading (3) and navigation checks pass; static publication check and JavaScript syntax pass.
- Browser testing caught a section-selection edge case when a target already occupied the upper reading area. Added a failing regression and adjusted the selection band. Independent review caught Contact selection at page end and a hardcoded/current-brand cue; added coverage and fixed both. No review findings remain deferred.
- Final local checks passed: hierarchy (4), experience (6), loading (3), production (5), release-candidate (6), navigation/history/header cases, counters, Jakarta date rollover, static publication, JavaScript syntax and whitespace.
- Browser verified desktop 1440px, mobile 390px and narrow mobile 355px. No horizontal overflow or broken sourced images observed in the checked views. Native Enter expansion and diagram Escape/focus return pass.
- The narrow header initially still wrapped with flexible widths. Changed it to a two-column grid for logo/menu; final measured header edge is about 73px at 355px, with Industrial heading at 113px (fully clear). ComAp explanation precedes its diagrams. Noris group/item sizes are 30/22px desktop and 24/20px mobile.
- Mobile client grid is two columns, about 353px high at 355px versus the former 547px irregular block. About title precedes its image. Current navbar selection correctly shows About/Services/Clients/Contact in tested journeys; Contact remains selected at page bottom on both Home and ComAp. Closed dropdown retains brand-page identity and supports future entries.
- Accepted evidence retained privately as `hierarchy-fixes-20261014/01-services-desktop.png` through `11-services-desktop-final.png`, plus `desktop-contact-check.json`. Early screenshots 01/02 and 04 precede the selection/header corrections; use 05 onward and the final desktop capture for acceptance.
- Preview release follows the verified merge to main. Production activation is outside this change.
