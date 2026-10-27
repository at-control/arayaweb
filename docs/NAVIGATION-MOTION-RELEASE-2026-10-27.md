# Navigation and motion fixes — 27 October 2026

Owner approved deployment of the locally reviewed fixes:

- Anchor offsets use the settled sticky-header height and compensate for section padding; desktop/mobile text lands about 44px below the header.
- Same-page Home/logo clicks scroll to the top without reloading and restarting entrances. Modified and cross-page clicks remain native.
- Hero/brand text entrances now last 950ms, other text 600ms; interaction/disclosure transitions are gentler. Reduced-motion support remains.
- Removed duplicate homepage company eyebrow and its line.
- Hidden utility strip at widths up to 680px; mobile sticky top is zero, preventing the wrapped WhatsApp number from clipping above navigation. Footer contact links remain.

Local static validation, existing navigation regression, new Home no-reload regression, six experience tests and JS syntax checks passed during implementation. Browser checked desktop About/Clients/Home and mobile Services alignment, active links, menu collapse and horizontal overflow; mobile utility is display:none with sticky top 0. Main-push workflow includes the new Home regression test and retains no PR triggers. Use the normal validated artifact promotion and live checksum verification; no Ads launch or tracking configuration change.
