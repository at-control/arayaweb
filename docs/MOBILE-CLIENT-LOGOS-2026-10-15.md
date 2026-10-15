# Mobile client logo animation — 15 October 2026

The owner confirmed that the client logos should slide left on mobile like the desktop layout. This supersedes the earlier static mobile grid decision.

Extended the existing CSS-only continuous marquee to all screen widths. Both identical tracks move together; the duplicated list stays hidden from assistive technology. Mobile uses 48px spacing, 22px vertical padding, existing proportionate logo sizes and a 30-second loop. Desktop keeps its 38-second loop and existing sizes. Overflow remains contained in the white logo strip; no JavaScript, assets, controls or dependencies were added.

Reduced-motion preference retains the static readable two-column mobile grid and hides the duplicated track. No pause/play control or hover pause was added.

Verification and deployment status are recorded in [Progress](PROGRESS.md). Browser evidence is retained privately under `arayaweb/docs/evidence/mobile-client-logos-20261015/`.

Local browser checks at 390px and 355px confirm two equal-width 1261.74px tracks, flex layout, continuous 30-second animation and no document overflow. Successive transform readings moved from -9.81px to -118.29px, confirming leftward movement. The tracks meet within 0.001px at the loop boundary. At 1280px, the original 38-second duration and 72px spacing remain. Mobile strip height is approximately 98px. Screenshot saved; temporary viewport overrides reset. Static validation, existing hierarchy/loading checks and production build checks are used rather than a new test that mirrors the CSS.

Release `b73fb8c` passed CI/Pages run 38669115057 and automatic production run 38669162639. Public browser at 390px loads stylesheet version `2e17786487`; both tracks animate for 30 seconds, successive transforms move left and document overflow remains contained. Published mobile screenshot is saved with the local evidence. Experience (6), hierarchy (4), loading (3), production (5) checks and JavaScript syntax also pass; main CI runs the full existing suite and every-file live deployment verification.
