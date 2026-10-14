# Brand simplification, motion and owner corrections — 14 October 2026

## Owner decisions

This supersedes the earlier detailed-brand-Contents implementation where noted. The owner found the task layer, repeated navigation and per-entry actions confusing.

- **Noris:** show products grouped into Measurement & instruments (five) and Marine systems (three). Remove Choose by task and its separate application section. Show noriMeter, noriMos, noriStar and noriNet names in the list. Product descriptions follow the same grouping.
- **ComAp:** only two top-level Contents choices: Applications and Products. Explain applications first, then show six controller/software product families. The eighteen manufacturer application explanations remain, organized within Applications into marine, power generation and smart energy management.
- **Both brand pages:** remove hero actions, product finder duplication, the persistent multi-section menu, all four per-application shortcut/action links, per-product actions, related service cards and cross-brand promotions. No external page links in the guide body; image credits remain visible and source URLs remain in research data/docs. Diagram enlargement remains an in-page interaction with a local-image fallback.
- CTA buttons appear only in the final shared contact section. The equipment brief is informational. Shared site navigation and footer navigation remain available.
- Brand hero company labels are exactly **Noris Group GmbH** and **ComAp a.s.**, without the INDONESIA suffix.
- Header order: Home, About Us, Our Services, Our Clients, Brand Partners, Contact Us.
- About paragraph: “with branch offices in Sidoarjo and Jakarta.” The supplied Townhouse PIK address stays in contact details.
- Remove repeated Equipment we work on lists from each of the three service disclosures. The shared equipment section appears once, with “and many more...” beneath it. Old equipment bookmarks still resolve to the corresponding service overview.

## Reading order

Information lists use CSS columns so readers finish a column before moving right. This applies to service scope lists, ComAp application detail fields, the final equipment brief and shared manufacturer groups. At mobile width they become one column. Product groups already contain vertical lists; actual product descriptions remain sequential.

Brand flow: hero → simple contents/product groups → brand background → applications (ComAp only) → products → FAQ → equipment brief → final contact CTA.

## Animation

- Removed the logo Pause/Play button, handler and hover pause. Desktop logos scroll continuously, including without JavaScript.
- Added staggered 600ms entrances for hero copy, product groups/rows, brand panels, enquiry steps and contact introduction.
- Added slow 24-second decorative hero-photo drift and smoother disclosure entry.
- Content remains visible if scripts or animation APIs fail. Reduced-motion preferences are retained; mobile logos keep their readable grid.
- Owner explicitly requested no animation pause controls. Independent review identified the continuous autoplay without on-page pause as an accessibility tradeoff; reduced-motion support does not establish WCAG 2.2.2 conformance. No conformance claim is made.

## Verification

- Build and six-document asset/fragment/metadata checks pass.
- Five experience tests pass: brand body links are limited to internal fragments/local diagrams; no per-entry/hero/cross-page action blocks; final contact draft names the brand; Noris still has eight products, ComAp has eighteen application disclosures and six products; simple Contents targets and reading order remain valid.
- Automatic Jakarta-year tests and JavaScript syntax check pass; no whitespace errors.
- Independent review found no blocking content/code regressions. Diagram viewer no longer depends on external caption anchors.
- Local desktop inspection: logo tracks report `client-scroll` and `running`; while hovered they still report `running`, with a changed transform. No Pause/Play control.
- ComAp marine diagram opened successfully with plain “Diagram: ComAp” credit after caption shortcut removal.
- Desktop ComAp definition fields were measured: first two occupy the left column, then the next two occupy the right column.
- Noris at 390px: two product groups, no content CTA buttons and no horizontal overflow.
- Shared equipment section: zero service-equipment disclosures, one closing and many more... line. The approved cities-only About sentence and Our Clients → Brand Partners menu order were confirmed in the browser.
- No console errors in the final inspected browser session.
- Desktop/mobile screenshots and final checks are saved in [evidence](reviews/motion-products-2026-10-14/).

## Publication

Local implementation verified. Release and deployed-file verification will be recorded after publishing to the GitHub Pages preview. Production WordPress is separate.

## Selected visual evidence

- [Noris grouped products](reviews/motion-products-2026-10-14/02-noris-products-desktop.png)
- [ComAp two-part Contents](reviews/motion-products-2026-10-14/03-comap-two-sections.png)
- [Vertical-first application fields without actions](reviews/motion-products-2026-10-14/04-comap-information-columns.png)
- [Single equipment section and many more](reviews/motion-products-2026-10-14/05-equipment-once.png)
- [Noris mobile](reviews/motion-products-2026-10-14/06-noris-products-mobile.png)

Final desktop captures use a 900px viewport to fit the available browser panel; 1440px column positions were additionally measured. The logo-motion capture predates the final menu reorder and is retained only as motion evidence.
