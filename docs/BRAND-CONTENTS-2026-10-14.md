# Brand content flow and Contents — 14 October 2026

## Review findings

Reviewed the current generated ComAp and Noris guides against the owner’s request for clearer organization and a daftar isi. Fresh desktop baselines are saved under [review evidence](reviews/brand-contents-2026-10-14/).

| Finding | Evidence | Resolution |
| --- | --- | --- |
| Both guides require substantial scrolling. | At a 1440 × 1000 viewport, ComAp document height was 12,319px with its 18 application explanations closed; Noris was 11,167px. These are whole-document heights, including header/footer, rather than reading-time estimates. | Added a compact grouped Contents section near the top of both pages. |
| The existing sticky menu gives only broad sections. | It cannot jump directly to generator synchronisation, individual sensors or noriNet. | Added individual topic links and a persistent Contents menu entry; product/application explanations link back to Contents. |
| Noris asks visitors to choose a task after the entire product catalogue. | Original order: About → eight products → four task guides → enquiry → FAQ. | Moved the four task guides before products and added a hero application link. |
| A single expanded list would be long on mobile. | ComAp has 24 detailed application/product topics. | Native collapsible groups, closed by default, show topic counts. Links remain usable without JavaScript. |

## Reading order and organization

Both guides now use: **Overview → Contents → About the brand → Applications → Products & systems → Enquire with Araya → FAQs → related Araya work**.

- **ComAp:** Marine (4), Power generation (10), Smart energy management (4), Products & systems (6). Application explanations describe the system and operating duty; product explanations describe the controller family and selection inputs. Both remain useful and cross-linked.
- **Noris:** Choose by task (4), Measurement & instruments (5), Marine systems (3). The last group includes noriMos, noriStar and noriNet through their existing product-family labels.
- About, enquiry and FAQ shortcuts appear beneath each list.
- Existing manufacturer images, diagrams, references, technical explanations and contextual WhatsApp enquiries are retained. No new service, certification, authorization or stock claim was introduced.
- Native details/summary provides keyboard expansion. Existing hash handling opens a selected ComAp explanation before navigation; existing mobile menu behavior closes the overlay and focuses the destination.

The Contents data is generated from the same application/product records used by the guide. Noris product groups reference explicit stable IDs in `brand_profiles.py`; reordering the portfolio does not change its grouping. Other brands default to a single product group unless configured.

## Verification

- `python tools/build.py`: three content pages, three compatibility routes and sitemap built.
- `python tools/check.py`: all six documents pass local asset/fragment, metadata, alt text, font and publication checks. No PR-triggered workflow.
- `python tools/test_experience.py`: five tests pass, including complete topic coverage, destination presence and application-before-product ordering on both guides; existing enquiry checks retained.
- `node tools/test_company_dates.cjs`: automatic-year regression checks pass.
- `node --check public/assets/site.js` and `git diff --check`: pass.
- Independent scoped code review: no blockers. Its minor positional-grouping concern was resolved by explicit product IDs.
- Local browser at 1440px: selecting generator synchronisation from Contents opens `#parallel-generation`; target top 178.6px, sticky menu bottom 159px. Heading is visible.
- Local browser at 390px: keyboard opens Noris Marine systems; noriNet link reaches `#norinet` with target top 149px and menu bottom 129.7px. Persistent menu returns to Contents, closes, and focuses `#contents`.
- ComAp mobile: keyboard opens Marine; AC / DC power management jumps to and opens `#marine-ac-dc-pms`, with target top 148.6px below the menu bottom of 129.7px. No browser console errors in the inspected ComAp state.
- No horizontal overflow in those measured desktop/mobile states. No enquiry submitted.

## Visual evidence

- [ComAp before](reviews/brand-contents-2026-10-14/01-comap-before.png)
- [Noris before](reviews/brand-contents-2026-10-14/02-noris-before.png)
- [ComAp Contents, desktop](reviews/brand-contents-2026-10-14/03-comap-contents-desktop.png)
- [ComAp selected application](reviews/brand-contents-2026-10-14/04-comap-topic-open.png)
- [Noris expanded group, mobile](reviews/brand-contents-2026-10-14/05-noris-contents-mobile.png)
- [Noris return to Contents, mobile](reviews/brand-contents-2026-10-14/06-noris-contents-return-mobile.png)
- [ComAp Contents, mobile](reviews/brand-contents-2026-10-14/07-comap-contents-mobile.png)

- [Compact desktop overview](reviews/brand-contents-2026-10-14/08-comap-contents-overview-desktop.png)

## Release

Implementation verified locally; publication verification will be recorded here after the content release. Production WordPress remains a separate deployment. The GitHub Pages preview retains noindex,nofollow.
