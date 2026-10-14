# Remove repeated blocks from every service sector — 14 October 2026

The owner pointed out that the earlier equipment-list cleanup still left repeated Noris/ComAp promotions, What to send us checklists and Discuss work buttons in every service sector. This was missed in that earlier pass.

Removed those three blocks from the shared service renderer for **Marine, Industrial and Automation & Electrical**. Each disclosure now contains its overview and service scopes only. Brand information appears in the shared Brand Partners section; the shared final Contact section handles enquiries. Existing service scope and legacy equipment hashes are preserved.

Verification:

- A regression check first failed in all three sectors, demonstrating their duplicate links/CTA blocks. After removal, all six experience tests pass.
- Browser DOM confirms zero promotion/checklist/action links in each service disclosure, with all 10 marine, 8 industrial and 12 automation scopes retained.
- One shared Brand Partners section and one final Contact section remain.
- Build, six-document fragment/asset/metadata checks, JavaScript syntax and whitespace checks pass.
- Visual evidence: [automation section ending](reviews/sector-cleanup-2026-10-14/01-automation-end.png).

Published release [3aecf59](https://github.com/hakiimm8/arayaweb/commit/3aecf59c63a5e53bf56404fab648a031f1c11958); [Pages deployment](https://github.com/hakiimm8/arayaweb/actions/runs/38511742944) succeeded. The published homepage returns HTTP 200, matches the verified artifact and was checked again for absent duplicate blocks in all three sectors. The GitHub Pages preview and production WordPress remain separate.
