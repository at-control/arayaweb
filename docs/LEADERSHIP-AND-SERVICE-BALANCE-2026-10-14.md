# Leadership and service-photo balance — 14 October 2026

## Owner correction

The owner found the new service pictures too large and disproportionate, requested more visual depth, and asked to remove Araya at Work until more photographs are available. They also explicitly requested a new section for the director and managers. This supersedes the earlier removal of the inline Leadership sentence and the first photo-led layout.

## Changes

- Removed the entire Araya at Work / Engineering in action gallery from the landing page. Original owner photographs, their derivative assets and preparation helper remain available for future use; they are not requested by the page.
- Service pictures now occupy about 32% of their inset feature row, rather than 60%, and are capped at 260px tall on desktop, 230px on tablets and 210px on mobile. At the checked 1309px desktop viewport the first picture is 370.5 × 260px, compared with the previous 743 × 495px at a wider viewport.
- Added inset image framing, a soft off-white feature background, subtle card shadows and an orange rule beside each introduction. The existing orange/charcoal/white identity and sharp geometry remain.
- All 30 service scopes remain in native disclosures, with column-first reading order and legacy scope/equipment bookmarks preserved.
- Added a dedicated **Leadership & management** section. The owner subsequently requested its placement immediately before **Get in Touch**, after Brand Partners & Equipment. Three equal portrait cards use the owner's earlier reference: orange edge accents, overlapping white name panels, clear roles and restrained shadows. No new menu choices, biographies, links or CTA buttons.

## Names, roles and photo provenance

Names and roles come from the owner's supplied screenshot and explicit request, not from the old theme's placeholder staff names. Photo correspondence was visually checked against that screenshot.

| Name | Role | Original WordPress upload |
| --- | --- | --- |
| Arif Fatkur Rohman, S.T., M.MT. | Director | `2024/03/dir1.png` |
| M Rosul Akbar | Manager | `2024/02/man1.png` |
| Anjas Budiarso | Manager | `2024/01/man2.png` |

Originals were recovered from the owner's `D:/Download/araya/araya/wp-content/uploads` copy. No portrait retouching or replacement artwork. `tools/prepare_leadership_photos.py --source <uploads-directory>` uses Pillow for orientation, proportional resizing and WebP encoding. CSS frames the portrait without changing the exported composition.

| Published asset | Dimensions | Bytes |
| --- | --- | ---: |
| `leadership-arif-400.webp` | 400 × 483 | 27,400 |
| `leadership-arif-720.webp` | 720 × 870 | 55,970 |
| `leadership-rosul-400.webp` | 400 × 393 | 20,266 |
| `leadership-rosul-720.webp` | 720 × 708 | 43,966 |
| `leadership-anjas-400.webp` | 400 × 533 | 26,186 |
| `leadership-anjas-720.webp` | 720 × 960 | 51,752 |

Three smaller variants total 73,852 bytes; three larger variants total 151,688 bytes. Explicit dimensions, responsive selection, lazy loading, low priority and asynchronous decoding are used. The checked mobile browser selected all three 400px variants. Source PNGs are not added to Git.

## Verification and evidence

Preview static checks, experience (6), hierarchy (4), loading (3) and JavaScript syntax pass. Browser checks at 1309px desktop, 390px mobile and 355px narrow mobile confirm three loaded portraits, contained names/roles, equal desktop caption heights, single-column mobile cards and no horizontal overflow. Native marine disclosure opens and retains all ten scopes. A settled generator bookmark opens its disclosure and lands at 92.99px below the 72.73px sticky header. The work gallery is absent.

Accepted screenshots are retained outside Git in the owner's docs under `evidence/leadership-balance-20261014/`. Release status is in [Progress](PROGRESS.md). WordPress production is unchanged.
