# Static production launch and continuous deployment — 15 October 2026

## Owner-approved outcome

Deploy the current website at https://arayainternusa.co.id/. No database or company-profile download is needed. Pushes to main must validate and deploy the site. Keep the original design/content, preview noindex, backups and rollback. This supersedes earlier notes excluding live activation.

## Design and implementation plan

Use the existing checked CI ZIP and pinned SSH credentials. A successful main build triggers a separate production workflow. It validates build provenance and every package hash, refuses an outdated main revision, uploads into private staging, then activates an immutable static release by atomically replacing a symlink. A hosting lock and GitHub production concurrency prevent overlapping activation. Root routing is versioned and managed explicitly; unknown existing configuration is never overwritten.

The main domain keeps Rumahweb hosting, SSL and email. Apache-compatible rules tested on this account's LiteSpeed serve only the new static routes, preserve SSL validation paths, redirect equivalent old URLs, retire old WordPress routes/downloads and block unrelated archives/direct release access. Old files and database remain backed up and are not deleted or used by the new website.

- [x] Verify fresh file/database backups on server and owner's computer.
- [x] Implement tested package validation, guarded activation, rollback and live HTTP checks (`tools/deploy_release.php`, `tools/test_deploy_release.php`, `tools/check_live.py`, `tools/production.htaccess`).
- [x] Wire automatic production promotion after successful main CI, plus manual deployment and rollback; keep no PR triggers and existing environment protections.
- [ ] Run existing checks and deployment refusal/rollback fixtures, then push main and verify the first production run.
- [ ] Verify HTTPS, brand pages, assets, SEO, old redirects, retired downloads, 404 behavior and mobile navigation; save screenshots and release notes.

## Failure and recovery requirements

- Failed checks must prevent activation; failed HTTP checks after activation restore the previous pointer/router, guarded against rolling back a newer deployment.
- Reject traversal, symlinks in the ZIP, altered bytes, dirty/fork/non-main builds, unexpected file types and filesystem paths resolving outside the expected directories.
- Keep releases and private deployment records. Do not recursively delete the document root, migrate a database, change DNS/mail, add a self-hosted runner or expose backups/configuration files.
- The first rollback restores the original PHP redirect and absent root routing file; later rollbacks restore the previous static pointer and router. Verify fixtures and real server behavior before launch.

## Observed hosting behavior

Fresh backup integrity passes: file archive SHA-256 `738155ed98379c32ab350beefab5161c0a27fcdf4bccd81ba55673dfab89e69d`; database gzip SHA-256 `92b9df3779a66c096a234d2cacd1fc01aa3a2dc000a01ad93bc9d27016363bb7`, 62 tables. Original root index.php remains SHA-256 `8305556db7c82cd97c81cb0dcae96d85b4334a039e25d14c2bb5da91f9c8e7ab`.

A disposable hosting probe demonstrated symlink-based static serving, but LiteSpeed sometimes served an internal symlink alias despite root rewrite guards. The final design avoids that dependency: versions and the atomic pointer live outside the document root. Nine stable links expose only intended static files/routes. A fresh probe confirmed home/brand/assets 200, hidden alias 404, legacy WordPress 410 and missing URLs 404. Probe files were removed.

PHP's symlink function is disabled, so the SSH wrapper creates guarded links and reserves the previous pointer for recovery. PHP performs atomic rename, exact file verification and managed routing changes. No PHP security setting was weakened. LiteSpeed takes several seconds to refresh routing changes, so HTTP verification retries at most five times with five-second intervals before guarded rollback.

Private hosting fixtures verified A → B → rollback B → rollback A and stale rollback refusal. An independent critical code review identified activation/rollback routing-write recovery gaps; both were fixed, with Linux permission-denied fixtures added. All existing website regression gates and four HTTP-verifier refusal tests pass locally. Full Linux fixtures also run in main CI, before production promotion.

## Operation after launch

1. Edit templates/assets, build/check locally and push `main` in [hakiimm8/arayaweb](https://github.com/hakiimm8/arayaweb).
2. `pages.yml` runs all content, navigation, motion/date/loading, package and deployment tests, retains the immutable production artifact and publishes the noindex preview.
3. `production.yml` automatically runs only after that main build succeeds. It validates repository/run/commit provenance, clean source, file allowlist and hashes; strict-host-key SSH uploads the package. An outdated main build is skipped before activation. GitHub production concurrency and a hosting file lock serialize changes.
4. Every package file is verified over public HTTPS, alongside indexing, legacy/canonical redirects, retired downloads, hidden paths and true 404s. Failure triggers rollback to the expected previous release; success is recorded in the Actions summary with the exact release ID.
5. Manual recovery: Actions → **Deploy production on Rumahweb** → Run workflow on `main` → mode **rollback**, using the exact current release ID from its successful deployment summary. It refuses a stale ID and verifies the previous release bytes before restoration. Use deploy mode with a successful current-main build ID to retry a checked deployment. If GitHub/SSH is unavailable, use cPanel Terminal and the private incoming deployment script/records; restore only managed routing/pointers. Keep the verified WordPress backup available for the initial legacy rollback.

The production environment retains its main-only policy and encrypted SSH secrets. No workflow has a PR trigger. The website runs without a database or PHP application; PHP is used only by the private deployment utility. No company-profile download is linked or packaged. Manufacturer product PDFs can be supported later as static assets, but none are currently packaged.

The owner's static-only cutover retires the 55 remaining WordPress URLs instead of preserving the old application. The [65-URL map](LEGACY-URL-MAP-2026-10-15.csv) records ten equivalent-content redirects and 55 retired routes. Old WordPress assets/downloads return 410; unrelated root archives return 404. Original files/database remain intact for rollback; DNS, email and SSL settings are unchanged.

## First live verification and correction

Source `656d4e0` passed [main CI 38663695623](https://github.com/hakiimm8/arayaweb/actions/runs/38663695623), including all Linux activation/refusal/rollback fixtures. [Production run 38663747721](https://github.com/hakiimm8/arayaweb/actions/runs/38663747721) activated the static release and verified its 75 file hashes, but rejected the old `/araya/` route (old WordPress 200, subsequently directory-index 403). The legacy application's directory configuration interfered with parent routing. Automatic rollback restored the original root entry point, absent root routing file and WordPress directory; independent SSH readback confirmed the original entry-point hash. This run is a failed release, not a successful launch.

Correction: first activation now moves the validated existing WordPress directory into private deployment storage after installing the static pointer/router. Its exact relative destination is recorded privately. Initial rollback restores that directory before removing static routing and public aliases. Later static releases leave it in private storage. No database contents are changed. Additional fixture checks verify private legacy retention and full original-directory restoration; the actual hosting fixture passed with PHP symlink disabled. This removes child-directory routing ambiguity and prevents the old application/assets remaining publicly accessible.

Sources: [GitHub workflow triggers](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow), [Apache rewrite flags](https://httpd.apache.org/docs/2.4/rewrite/flags.html). Actual account tests govern compatibility.
