# Hierarchy and mobile audit — paused

**Continuation completed:** owner resumed work on 14 October 2026. The final findings and resolution of provisional observations are in [HIERARCHY-REVIEW-2026-10-14.md](HIERARCHY-REVIEW-2026-10-14.md). The pause record below is historical. No UI fixes were implemented during the review.

14 October 2026, Asia/Jakarta. **Paused at the owner's explicit request. Review is incomplete; no UI fixes have been implemented.**

## Request and scope

Review the homepage and both brand pages for section hierarchy, subsection grouping, headings and reading order. Owner subsequently added the mobile client-logo layout and verification of navbar destinations, active labels and sticky-header clearance. Preserve the current orange/charcoal/white design, original logo and typography. Keep vertical-first reading order and final-section contact actions; do not reintroduce repeated shortcuts or per-item enquiry buttons.

The three content pages are Home, Noris and ComAp. Marine/Industrial/Automation URLs are compatibility redirects into homepage sections. Production WordPress and the staging workflow were not changed during this audit.

## Evidence collected

Current published preview inspected through the in-app browser; local templates/CSS/JS inspected to explain observed structure. Owner-local screenshots and JSON evidence are retained outside this repository in `arayaweb/docs/evidence/hierarchy-20261014/`.

- 01–06: desktop homepage hero, services, expanded Marine, About, Clients and Brand Partners.
- 07–11: Noris entry, product detail, noriNet, FAQ and equipment brief.
- 12–17: ComAp entry, Applications, expanded AC/DC example, Power Generation, Products and shared Contact.
- 18–22: narrow-mobile Applications/expanded diagrams, Noris groups/product and homepage services.
- 23–30: mobile menu, Clients/About/Services/Contact navigation, client logos and both brand entries.
- 31–32: 390 CSS-pixel mobile client logos and Noris catalogue hierarchy.
- 33: settled desktop About navigation.
- `navbar-static-check.json`: 21 navbar href/page/fragment checks across all three pages.
- `heading-outline-source.json`: generated HTML heading outlines, including compatibility routes.
- `navbar-browser-checks.json`: browser destination, title position, header edge, menu state and aria-current observations. Some desktop readings were taken during scroll/loading transitions and are explicitly provisional, as described below.

Browser zoom affects the requested viewport size. Initial 1440×900 override produced approximately 1309 CSS pixels of width; initial 390×844 override produced 355×767 CSS pixels. Later adjusted overrides were verified as 390×844 CSS pixels and 1440×900 CSS pixels. Record actual DOM dimensions when resuming. Early same-page screenshots occasionally showed the preceding scroll position; rejected views were replaced. Do not use transient counter values or screenshot capture blur as content/asset-quality findings.

## Confirmed findings

### 1. Homepage: service hierarchy and repetition

- The image cards introduce Marine/Industrial/Automation, followed by another Explore our services heading and three expandable sector headers. This creates repeated entry layers.
- Computed desktop sizes: Explore our services 26px, sector summary 25px and service-item heading 22px. Parent/child distinctions are small, and the shared background/left edge provides little containment.
- Sector summaries use `strong` rather than headings; their child items are h4. The visual and semantic outline should be reconciled. This is an accessibility review concern, not a claim of full WCAG failure.
- The Marine summary and opening paragraph repeat supply/repair language.
- Mobile About places the large photo before its title. About navigation reaches the correct section, but the heading appears well below the landing point.

### 2. Noris: weak distinction between product groups and products

- Desktop group headings are 30px and product headings 28px.
- Mobile group h3 and product h4 are both **26px**, confirmed at 390 CSS pixels. Weight is also the same.
- Entry, profile and catalogue headings repeatedly describe sensors/instruments/marine systems without clearly naming the section role.
- Product details and the noriNet system explanation need a stronger visual connection to their parent product/group.
- The two-group product index is straightforward and should remain; do not restore task-based navigation.

### 3. ComAp: section names and introductory density

- Contents offers Applications and Products, but destination titles are The application defines the control system and From one engine to coordinated power. Direct matching section names would make orientation easier.
- Applications has three introductory paragraphs before its group introduction. On narrow mobile, this occupies nearly a full screen before the first actual application group.
- Three application groups contain 4, 10 and 4 items. The ten-entry Power Generation group needs clear containment and spacing; preserve all applications as requested by the owner.
- Expanded applications insert substantial diagram content before their technical detail fields. Their relationship to the parent group needs clearer nesting.
- Application titles use strong in summary elements, rather than heading elements. Include this in the semantic-outline review.

### 4. Shared brand endings: repeated emphasis

- FAQ, Share your equipment details / Let’s define the scope, and the final Let’s find the right solution block each use prominent section-heading treatment.
- The equipment brief can be more compact and visibly associated with final contact. Keep CTA buttons only in that final contact area.

### 5. Mobile clients: reproduced owner screenshot

- At both narrow and 390px mobile widths, the seven logos form irregular rows: mostly one logo, with Pelindo and the Navy emblem sharing a row.
- The white logo block is approximately **547 CSS pixels tall** at 390px. Flexible wrapping and intrinsic logo widths explain the inconsistent arrangement.
- Recommend a consistent two-column grid with equal slots, contained source images and balanced visual sizing. Keep original logo colours and avoid extra controls.

### 6. Navbar: destinations valid, current-section indication missing

- Static inspection confirms all **21** navbar destinations across the three content pages resolve to the intended page and existing target ID.
- Browser checks confirmed mobile Home, About, Services, Clients and Contact destinations; both Brand Partners links; same-page Contact on each brand; Noris-to-home Services and ComAp-to-home Clients navigation.
- Mobile menu closes after selecting a destination. Escape closes it and returns focus to Menu.
- Home retains aria-current=page at About, Services, Clients and Contact. Brand pages mark their own dropdown child as current, but the collapsed Brand Partners parent has no visible current-page indication. Section navigation is not tracked by the main navbar.
- Narrow-mobile header wraps into two rows; observed scrolled header edge is about 140px at 355 CSS pixels. At 390px the header fits one row at about 79px.
- `--header-edge` remains 78px on narrow mobile even when the actual header is about 140px. The JS that updates this value is inside the `pageIndex && siteHeader` guard, while current pages have no page-index element. This explains a clearance risk for detailed anchors. Section padding can protect top-level headings despite this stale value.

## Provisional observations — do not report as settled defects yet

- Detailed Marine/ComAp anchor screenshots sometimes show a title partly behind the narrow-mobile header. Re-test after navigation/scroll settle and measure header bottom versus title top; distinguish actual clearance from transient captures.
- One desktop cross-page Clients reading still showed the newly loaded hero; a subsequent same-page Clients check settled correctly. A later desktop Services reading returned titleTop -403px and needs reproduction. Do not claim every desktop navbar landing is correct or broken from this incomplete evidence.
- Header active styling from hover/focus must be distinguished from aria-current. The confirmed problem is absence of persistent section tracking.

## Proposed shared hierarchy — not implemented

| Role | Desktop direction | Mobile direction |
| --- | --- | --- |
| Page title / h1 | 56–64px | 36–40px |
| Main section / h2 | 40–44px | 30–32px |
| Group / h3 | 28–30px | 24px |
| Product/service/application / h4 where nested | 22px | 20px |
| Body | 17px | 16px |
| Metadata/captions | 12–14px | 12–13px |

Use shared spacing roles and containment as well as type size: generous section separation, moderate group separation, compact item spacing. Use direct section labels: About Noris, Products & systems, Applications, Products, Common questions and Equipment details. Keep concise supporting descriptions, one consistent disclosure chevron and vertical-first ordering. Avoid giving every information block the same full-section emphasis.

## Resume checklist

- [x] Reproduce desktop navbar landings after loading and smooth scrolling settle; record actual section/title positions.
- [x] Verify detailed-anchor clearance at 355px and 390px with actual header height.
- [x] Complete remaining brand profile/closing-section mobile captures and any uncovered homepage sectors.
- [x] Check desktop Brand Partners dropdown navigation and visible active parent treatment.
- [x] Consolidate a prioritised final review with accepted screenshot references, confirmed findings and evidence limits.
- [x] Prepare the shared hierarchy proposal in the completed report for delivery to the owner; current request is a review, and implementation remains pending.

## Pause state

The audit-created in-app browser tab was marked for handoff. Its last requested navigation was homepage Contact after desktop Services; the owner's ambient context still reported Services. Check current visible state before the next interaction. Viewport override was still set for 1440×900 CSS-pixel desktop testing; reset it when finishing the audit.

This note, its documentation-index entry and progress entry are local and **not committed or pushed** at pause. The website repository's previous published HEAD remains `6e426f9`. No further CI run, deployment, UI fix or production cutover was started after the pause request.
