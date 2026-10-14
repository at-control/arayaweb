# Section hierarchy, mobile layout and navigation review

Completed 14 October 2026, Asia/Jakarta. Reviewed the published GitHub Pages preview for **Home, Noris and ComAp**, with source inspection to explain findings. This is an audit and implementation proposal; no website code, live hosting or production staging configuration was changed.

## Conclusion

The visual identity is coherent: original Araya logo, orange/charcoal palette, Space Grotesk, square edges and manufacturer imagery. Top-level homepage sections are reasonably distinct. The main weakness is the hierarchy inside those sections, especially service disclosures and the Noris catalogue. Mobile exposes additional navigation and content-density problems. Correct these before the live cutover.

## Review steps and health

| Step | Surface / task | Health |
| --- | --- | --- |
| 1 | Home: hero, About, services, three expanded sectors, Clients, Brand Partners, equipment list and Contact | Main sections identifiable; service hierarchy and repeated introductions need correction. |
| 2 | Noris: entry, grouped product index, profile, catalogue, noriNet system content, FAQ, equipment brief and Contact | Useful two-group catalogue; group/product distinction weak, particularly on mobile. |
| 3 | ComAp: entry, two-part Contents, profile, three application groups, expanded Marine example, Products, FAQ, brief and Contact | Applications-first flow is appropriate; section labels, introductory density and nested information need improvement. |
| 4 | Mobile: narrow 355px and typical 390px CSS viewports | Irregular client-logo grid; narrow header wraps and obscures some anchor titles. |
| 5 | Navbar: destination validation and representative desktop/mobile journeys | All destination IDs valid; tested routes reach the intended sections after settling. Current-section indication and narrow anchor clearance fail. |

Three old service URLs are compatibility redirects, not additional content pages. Source checks confirm they retain service-redirect behavior. They were not treated as independent visual layouts.

## Findings, in priority order

### P1 — Narrow-mobile header obscures detailed anchor titles

At 355 CSS pixels, the logo/menu header wraps into two rows. Its scrolled bottom is about **140px**, while `--header-edge` remains **78px**. The JS updater is guarded by the presence of a removed `.page-index` element, so it does not update the offset on current pages.

Settled measurements:

| Target | Width | Header bottom | Title top | Result |
| --- | --- | --- | --- | --- |
| Marine | 390px | 79px | 122px | Clear |
| Industrial | 355px | 140px | 122px | Partly covered |
| Automation & Electrical | 355px | 140px | 121px | Partly covered |
| Noris Speed sensors | 355px | 140px | 167px | Product title clear; preceding row metadata reaches the header |
| ComAp AC/DC power management | 355px | 140px | 120px | Partly covered |
| ComAp AC/DC power management | 390px | 79px | 120px | Clear |

**Recommendation:** keep a compact single-row logo/menu header where practical and measure actual header height independently of any contents component. Apply the resulting scroll offset consistently to section, disclosure and product anchors. Test after menu close, resize, font loading and cold navigation.

Evidence: `42-narrow-industrial-anchor.png`, `43-narrow-automation-anchor.png`, `44-narrow-noris-anchor.png`, `45-narrow-comap-anchor.png`, `47-mobile390-comap-anchor.png`, `anchor-clearance-checks.json`.

### P1 — Parent and child headings look almost equal

- **Home:** Explore our services is 26px; sector summary is 25px; service item is 22px. Similar weight and alignment flatten three levels.
- **Noris desktop:** product-group heading is 30px and product heading 28px.
- **Noris mobile:** group h3 and product h4 are both **26px**, with the same weight. Visitors must infer the relationship from a divider and a number.
- Summary elements in Home/ComAp use strong text rather than headings; homepage child services use h4. The semantic outline does not consistently expose the same hierarchy the layout intends.

**Recommendation:** define shared roles for page title, section, group, item and metadata. Use size, spacing, inset and containment together. Reconcile heading semantics with that nesting while preserving native disclosure behavior and keyboard operation.

Evidence: `03-home-marine-expanded.png`, `08-noris-product.png`, `32-noris-mobile390-portfolio.png`, `heading-outline-source.json`; computed-style observations in the audit log.

### P2 — Section names do not consistently identify the content

ComAp Contents links say Applications and Products, but destination headings say The application defines the control system and From one engine to coordinated power. Noris entry, profile and catalogue repeatedly use variations of instruments/sensors/marine systems. The brand profile can be mistaken for another product introduction.

**Recommendation:** use direct section names that match navigation: **About Noris / About ComAp**, **Products & systems** for Noris, **Applications** and **Products** for ComAp. Keep descriptive supporting copy below those labels. Preserve the two Noris product groups and the two ComAp Contents choices.

Evidence: `07-noris-entry.png`, `12-comap-entry.png`, `13-comap-applications.png`, `16-comap-products.png`, `36-comap-mobile-profile.png`, `39-noris-mobile-profile.png`.

### P2 — Repeated introductions delay useful information

Homepage image cards are followed by another Explore our services introduction and repeated sector summaries. Expanded Marine repeats supply/repair language. ComAp Applications has three introductory paragraphs before the first group introduction. On narrow mobile, introductory text occupies nearly a full screen before the group content.

Mobile About puts the large image before its heading, so selecting About initially shows the image rather than the section name. Both brand profiles include repeated project-discussion/support positioning.

**Recommendation:** retain one services section heading, concise sector summaries and the actual systems list. Keep existing service imagery, but connect it to the corresponding sector rather than making a second entry layer. Move mobile section headings before supporting media. Reduce ComAp Applications to one useful introduction, retaining project-scope qualifications where they explain real applicability.

Evidence: `02-home-services.png`, `03-home-marine-expanded.png`, `18-comap-mobile-applications.png`, `25-mobile-about-nav.png`, `36-comap-mobile-profile.png`.

### P2 — Expanded content has weak visual containment

Service items and their parent summary share the background and left edge. In ComAp, application summaries, diagrams and technical fields are primarily separated by spacing and fine rules. Power Generation has ten application entries; clarity of group membership matters over that length.

**Recommendation:** make group headers distinct and visibly contain their child information with modest insets, a consistent boundary and shorter spacing inside a group than between groups. For each product, keep title/model, image, overview and detail fields in a clearly associated unit. Treat system diagrams as nested explanatory content with a caption. Keep all 18 ComAp applications and current manufacturer assets; do not introduce extra shortcut links or per-item CTAs. Preserve vertical-first desktop ordering and linear mobile ordering.

Evidence: `14-comap-application-expanded.png`, `15-comap-power-generation.png`, `19-comap-mobile-expanded.png`, `21-noris-mobile-product.png`, `46-comap-mobile-products.png`.

### P2 — Mobile client logos form an irregular tall block

The seven logos wrap according to intrinsic widths. Most rows have one logo; Pelindo and the Navy emblem share a row. The white block is approximately **547px high** at 390px. This reproduces the owner's screenshot.

**Recommendation:** use a consistent **two-column grid** on phones, with equal slots and balanced optical logo sizes. Preserve the original images and colours, fit them within each slot, and avoid forced stretching. Keep desktop logo motion and reduced-motion behavior; no new controls are needed.

Evidence: `28-mobile-client-logos.png`, `31-mobile390-client-logos.png`.

### P2 — Navbar highlights page identity, not the current section

All **21 navbar href/page/fragment combinations** across the three content pages resolve to valid destinations in generated HTML. Browser journeys verified Home/About/Services/Clients/Contact, both dropdown brands, brand-local Contact and cross-page homepage section navigation. Mobile menu closes on selection; Escape closes it and returns focus to Menu.

However, Home remains `aria-current=page` while viewing About, Services, Clients or Contact. On brand pages the current brand is marked only on the dropdown child; the collapsed Brand Partners control has no current-brand indication. Hover/focus orange styling is temporary and does not solve this.

**Recommendation:** distinguish current page from current section. On Home, track the visible section and update the matching main-nav link consistently, including browser Back/Forward and hash navigation. On brand pages, visibly identify Brand Partners/current brand without adding another menu. Preserve the current link order.

Evidence: `navbar-static-check.json`, `navbar-browser-checks.json`, `24-mobile-clients-nav.png`, `34-desktop-services-settled.png`, `35-desktop-cross-page-clients.png`.

### P3 — Supporting brand endings receive too much section emphasis

FAQ, the equipment brief and final contact each have large standalone headlines. The brief title Share your equipment details / Let’s define the scope is followed by another invitation in Contact. Mobile requires substantial scrolling through repeated preparation language.

**Recommendation:** keep FAQs, make the equipment brief a compact informational subsection beside/above final Contact, and keep enquiry buttons only in that final area. Use direct labels and moderate subheading sizes. Do not add repeated sector/brand promotions.

Evidence: `10-noris-faq.png`, `11-noris-brief.png`, `17-shared-contact.png`, `37-comap-mobile-faq.png`, `38-comap-mobile-brief.png`, `40-noris-mobile-faq.png`, `41-noris-mobile-brief.png`.

## Shared hierarchy specification proposed for implementation

| Role | Desktop | Mobile | Treatment |
| --- | --- | --- | --- |
| Page title | 56–64px | 36–40px | One h1; establish page identity |
| Main section | 40–44px | 30–32px | Clear h2 name; one supporting description |
| Content group | 28–30px | 24px | h3; distinct group header and boundary |
| Nested item | 22px | 20px | h4 where nested; compact descriptive title |
| Body | 17px | 16px | Comfortable line height and controlled measure |
| Metadata/caption | 12–14px | 12–13px | Secondary emphasis; avoid headline styling |

Suggested spacing roles: section 88/56px, group 48/32px, item 24/20px and internal content 16/12px for desktop/mobile respectively. These are starting values to verify in the existing layout, not a mandate to make every block identical. Use one consistent disclosure chevron and clear focus states.

Recommended page organisation:

- **Home:** hero → About → Services (three clearly grouped sectors) → Clients → Brand Partners and other equipment → Contact.
- **Noris:** hero and brief profile → existing two-group product index → grouped catalogue (Measurement & instruments; Marine systems, including noriNet) → concise FAQ → final equipment brief/contact.
- **ComAp:** hero and brief profile → existing two-choice Contents → Applications (Marine; Power generation; Smart energy management) → Products → concise FAQ → final equipment brief/contact.

No new pages or per-item actions are proposed. Keep original artwork, manufacturer diagrams, owner-approved scope and project count, automatic years, professional positioning and existing contact destinations.

## Evidence limits and settled observations

This is a visual/DOM/source audit of the current preview, not a new SEO score, performance benchmark, manufacturer-content verification or full accessibility certification. Header-clearance measurements and key navigation journeys were tested; every possible browser, width and application disclosure was not exercised. No enquiry message was sent.

Earlier desktop screenshots occasionally caught loading or smooth scrolling in progress. Resumed tests confirmed settled Services and cross-page Clients headings appear below the header (about 255px versus 91px). Those transient readings are **not** reported as persistent desktop navigation defects. Narrow-mobile overlap was independently reproduced after settling and remains a confirmed defect.

Accepted screenshots, JSON and a screenshot-illustrated copy of this report are retained in the owner's local documentation folder outside Git. Browser viewport override was reset after the review. No UI implementation was performed in this review.
