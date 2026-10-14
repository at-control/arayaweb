# Photo-led landing page — 14 October 2026

Historical first arrangement: superseded by [Leadership and service-photo balance](LEADERSHIP-AND-SERVICE-BALANCE-2026-10-14.md). The owner requested smaller service pictures and removal of the work gallery for now.

## Owner direction and implementation

The owner supplied two work photographs, asked for larger service pictures, and requested more photography than text on the landing page. The orange, charcoal and white style remains.

- Each service is now a visible photo-led feature: approximately 60% photo and 40% title/short description on desktop. The previous desktop image width was 220px; the new image measures 743px at the checked 1584px viewport.
- Full service scopes sit in a native, keyboard-operable disclosure below the feature, initially collapsed. All 30 scopes and their bookmarked IDs remain. Individual scope/equipment bookmarks expand the matching disclosure; service overview bookmarks show the photo and introduction.
- Mobile stacks the large photo above the title and description. Scope lists remain vertical before moving across columns on larger screens.
- Added “Engineering in action” after the service features, using two cards with orange edge accents and overlapping white captions from the owner's reference. No additional enquiry or navigation links.
- Brand pages retain their existing information structure; only the shared CSS cache version changes there.

## Photograph provenance

Originals remain in the owner's `arayaweb/picture` directory, outside the Git repository. These are owner-supplied Araya photographs, not manufacturer examples.

| Original | Published stem | Caption |
| --- | --- | --- |
| `003.jpg` (1280 × 596) | `work-engine-room` | Marine machinery — Engineering work in the engine room. |
| `IMG_3859.JPG` (1600 × 1200) | `work-switchboard` | Electrical systems — Onboard switchboard inspection and technical review. |

No vessel names, project dates, customer names or individuals' roles were supplied, so none are inferred. The switchboard photograph's original camera date stamp is retained; its format is not interpreted. Images are resized and encoded, with EXIF orientation respected. CSS frames images with `object-fit`; exported assets retain the full source composition. No retouching or date-stamp removal.

## Image preparation and loading

`tools/prepare_work_photos.py --source ../picture` uses Pillow to generate the committed responsive WebP assets. Pillow is needed only to prepare new photographs, not to build or deploy the site.

| Asset | Dimensions | Bytes |
| --- | --- | ---: |
| `work-engine-room-800.webp` | 800 × 373 | 47,426 |
| `work-engine-room-1280.webp` | 1280 × 596 | 83,406 |
| `work-switchboard-800.webp` | 800 × 600 | 54,932 |
| `work-switchboard-1280.webp` | 1280 × 960 | 112,550 |

Both cards use `srcset`/`sizes`, explicit dimensions, asynchronous decoding and lazy loading below the fold. The two 800px candidates total 102,358 bytes; the two 1280px candidates total 195,956 bytes. Selection also depends on device pixel ratio. The checked desktop selected 800px candidates for 604px-wide cards. Existing service photographs stay at low fetch priority; the early-image budget remains below 750KB.

## Verification

- Preview build and static validator passed: six routes, assets/fragments, metadata and no PR workflow triggers.
- Existing experience (6), hierarchy (4), loading (3) and production (5) tests passed; updated hierarchy assertions reflect photo-first features with preserved scope content.
- JavaScript syntax and navigation fixtures passed.
- Browser checked at 1584px desktop, 390px mobile and 355px narrow mobile. No horizontal overflow. Photos load; captions remain contained; mobile cards stack; native service disclosure opens with Enter and retains all ten marine scopes.
- A settled `#marine-generators` bookmark opens its disclosure and lands at 92.5px below the 72.8px sticky header.
- Gallery keeps Our Services selected in the main navigation.

Accepted screenshots are retained outside Git in the owner's docs under `evidence/work-photos-20261014/`: desktop services/gallery, mobile services and narrow-mobile gallery. Publication status is recorded in [Progress](PROGRESS.md). Production WordPress has not been changed.
