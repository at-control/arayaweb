# Loading, counters and original branding — 14 October 2026

## Request and diagnosis

The owner reported sluggish pages and pictures appearing late, then requested removal of the Leadership line, counting on project/experience metrics, a new tab title/icon and a sharper original logo.

- Product images were already small: Noris hero 15,574 bytes; ComAp hero 28,762 bytes. Recompressing them would not address the main observed delay.
- One concurrent HTTP sample from this workstation to GitHub Pages measured first-response times of 610–1,688ms, with total transfer times of 612–1,877ms. Noris HTML was 1,747ms, its hero image 1,692ms; ComAp HTML 1,877ms, its hero 612ms; CSS 1,252ms, JS 680ms. This is a single connection sample including network/connection setup, not a representative user benchmark or browser Core Web Vitals result.
- Below-fold product pictures used native lazy loading, so a quick scroll or distant Contents jump could start a request only after approaching that section.
- New entrance effects animated whole image/product/section wrappers for 600ms plus up to 210ms delay. This can add visible settling and compositing work. No FPS or long-task trace was collected, so it is not a measured frame-rate diagnosis.
- The visible header used a 238 × 52px resized raster. The owner's company profile `download/cp.pdf`, first page, includes the original 4,165 × 961px RGBA logo artwork.

## Implemented changes

### Loading and motion

- Preload each page's hero image from the document head. Homepage preload uses the exact image srcset/sizes from its responsive hero, avoiding a second candidate download.
- Request small catalogue photos, homepage service/about photos and visible group/system diagrams early, with low fetch priority and async decoding. Hero retains high priority.
- Hidden ComAp application-detail diagrams remain lazy; no eager download of all closed explanations.
- Remove image/large-section entrance fades and stagger delays. Text-only entrances now use a short 280ms, 8px movement with no opacity fade. Large disclosure bodies are no longer animated.
- Existing continuous logos and decorative hero motion remain; reduced-motion behavior remains supported.
- Current unique eager-image bytes (after SVG branding): Home 606,980; Noris 276,704; ComAp 352,200. Eager image bytes are guarded below 750,000 per content page (unique source files, excluding alternate responsive candidates). Early fetching trades a modest initial download increase for pictures being ready before distant jumps. `fetchpriority=low` limits competition, but a throttled mobile waterfall is still needed to measure the result on constrained networks.

These changes remove artificial settling and defer less small-image work. They do not eliminate the underlying hosting/network response time. No numeric speedup or Core Web Vitals score is claimed.

### Number counting

- Count 1,500+ projects and experience age in the homepage hero/About/Clients metrics, once when visible.
- 800ms animation uses requestAnimationFrame and exact final formatting. No extra script request or permanent counter timer.
- Dates, phone numbers, addresses, model names and manufacturer founding years do not count.
- Static final text remains in HTML for script failure/no JavaScript. Reduced motion uses final values directly; hidden tabs finish active counters.
- Jakarta New Year updates cancel any older age animation before it can restore a stale age. The existing automatic-year timer remains intact.

### Original logo and tab branding

- `araya-logo.svg` and `araya-icon.svg` are deterministic vector traces of the owner’s first-page company-profile artwork, not AI-generated redesigns or replacement fonts. White emblem shapes and original wordmark contours are preserved; original black lettering is rendered white for the established dark/orange header.
- Reproduction: `tools/trace_original_logo.py --pdf path/to/cp.pdf`, using Pillow/numpy/pypdf and vtracer 0.6.15. The company PDF, extracted source PNG and temporary tool installation remain outside Git/deployment (`tmp/` is ignored).
- Header/footer use the scalable SVG. The tab uses the orange SVG emblem and the owner's original 64px PNG as a fallback. Icon query hashes refresh cached tab artwork.
- Page titles: Home - PT Araya Internusa; Noris - PT Araya Internusa; ComAp - PT Araya Internusa. Descriptions and product content remain.
- Removed the requested Leadership paragraph. The separate company founding-history sentence remains.

## Verification

- Loading regression tests were run before implementation and failed for missing hero preloads and lazy catalogue images. All three pass after implementation, including matching responsive candidates, complete early catalogue loading and the image-byte budget.
- Counter component test failed before implementation; it now passes progression, exact totals, finite frames, repeat-observation guard, reduced-motion change and New Year race checks.
- Build, six-document asset/fragment/metadata checks, five experience tests, automatic-year boundary/open-tab tests, JS syntax checks and whitespace checks pass.
- Independent code review found no blocking regression; it noted the early-image network tradeoff recorded above and exclusion of temporary tooling artifacts.
- Local browser: header SVG loads; title/hashed icon references are correct; Leadership is absent; hero opacity is 1; counters settle at 1,500+ and the current age; no horizontal overflow at the inspected width.
- Local Noris at 390px: all eight catalogue photos are already complete before scrolling; the product row has opacity 1 and transform none. Hero loads, no overflow and no browser console errors in that inspected state.
- Published-site browser attachment timed out. HTTP measurements are from the published preview; visual/interaction checks use localhost. This limitation is not a site speed measurement.

## Release

Published website-content release [fe80362](https://github.com/hakiimm8/arayaweb/commit/fe80362574d96b1ec99cc1d8cae81e9f760cea15); [Pages deployment](https://github.com/hakiimm8/arayaweb/actions/runs/38509655085) succeeded. All fourteen published HTML/sitemap/script/style/logo/icon files return HTTP 200 and match the verified artifact (text line endings normalized; PNG compared directly). Browser visual checks were local. Production WordPress is separate; the preview retains noindex,nofollow.

## Visual evidence

- [Scalable original header logo](reviews/loading-branding-2026-10-14/01-sharp-logo-desktop.png)
- [Finished project metric](reviews/loading-branding-2026-10-14/02-project-total.png)
- [Mobile SVG logo and loaded hero](reviews/loading-branding-2026-10-14/03-sharp-logo-mobile.png)
