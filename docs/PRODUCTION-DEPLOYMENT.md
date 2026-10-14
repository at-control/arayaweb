# Production deployment: arayainternusa.co.id

Prepared 14 October 2026, Asia/Jakarta. **Status: owner-approved SSH and GitHub production secrets configured; manual private staging workflow ready for its first run. Live cutover has not been performed.**

## Hosting continuation — 14 October 2026

Browser control recovered after the connection failure. The cPanel Terminal works. Git, tar, unzip, SHA-256 tools, SFTP/SCP, PHP, WordPress CLI and mysqldump are available in the account shell; rsync and Python were not found on its PATH. Use an SSH/SFTP or SCP package transfer rather than assuming rsync is installed.

- Created a private backup directory outside the web root with permissions 0700; backup files are 0600. Archived the complete active WordPress directory, root PHP entry point and `.well-known` validation files. The archive is 748,150,974 bytes, creation exited 0 and a full archive read exited 0. Downloaded it to the owner's computer and verified its SHA-256 against the server value.
- Downloaded the WordPress database through cPanel Backup. Gzip integrity passes; the dump contains 62 CREATE TABLE statements, matching the live database's 62 tables. Local compressed size is 10,881,928 bytes. No SQL data or WordPress configuration was committed to Git.
- Tested extracting the backed-up root entry point and WordPress `.htaccess` into a separate private restore-check folder; both recovered files match the live originals by SHA-256. A complete database import/whole-site restore rehearsal has not been performed. Unrelated untouched root directories and old ZIP archives were not duplicated into this active-site backup; this is not a full mail/hosting-account backup.
- WordPress CLI `db export` failed because PHP `proc_open`/`proc_close` are disabled. Used cPanel's supported database backup instead; PHP restrictions remain unchanged.
- Exported the actual published page/post URLs: 58 pages and 7 posts. Inventory includes real service/about/contact pages plus shop/cart/checkout, sample pages, theme element pages and dated theme articles. Review these individually; likely demo content should not receive unrelated homepage redirects. The full inventory and proposed classifications are retained privately outside the repository; no existing pages were deleted or changed.
- Root deployment destinations (`assets`, `noris`, `comap`, `index.html`, `robots.txt`, `sitemap.xml`) did not exist at inspection. No root `.htaccess` appeared in the full directory listing. The WordPress subdirectory uses `RewriteBase /araya/` and WordPress/LiteSpeed directives. Preserve the SSL validation directory and unrelated root folders.
- Rumahweb's [current SSH guide](https://www.rumahweb.com/journal/cara-menggunakan-ssh-di-hosting/) specifies port **2223**. Recorded the server's RSA/Ed25519 public host keys from loopback through the authenticated cPanel Terminal. A strict-host-key SSH handshake from the owner's computer accepted those pinned keys and reached authentication on port 2223; with credentials deliberately disabled it returned Permission denied. The dedicated key has since been authorized with owner approval, and pinned-host key authentication succeeds.
- The Windows OpenSSH `ssh-keyscan` utility failed with an unsupported hybrid KEX error. The connection check used the authenticated-server host keys and modern `curve25519-sha256` key exchange with strict host-key checking; no host-key or certificate validation was disabled.
- Manually uploaded the clean CI package for commit `f66ada91a4c19c82adf283d27db3f7e99893ab64` into a private incoming directory and extracted a private release. Verified its archive SHA-256 against the independently downloaded CI manifest, then verified all **65 extracted file hashes** on the server. Archive SHA-256: `7029d22b00d6ac3b498d38628f7b05477b22913af556b91c79df47dc8f5276b1`.
- No files in the live document root were replaced, no redirect/HTTPS/DNS/email configuration changed, and no public staging URL was created. The existing WordPress site remains live.
- After explicit owner approval, imported and authorized the dedicated public key through cPanel; the private key was not entered there. Verified SSH key authentication with strict host-key checking. Created the GitHub `production` environment restricted to `main` and stored the five connection secrets through private standard input. Added the manual private staging workflow; activation remains excluded.

Private paths, backup manifests, URL inventory, deployment key and administrative screenshots remain in the owner's local workspace, outside the public Git repository. This section supersedes the earlier unverified Terminal/port/backup statements below; pending cutover gates still apply.

## Recommended workflow

1. Edit templates/assets and commit to `main`.
2. GitHub Actions builds and checks the noindex preview, runs content/loading/counter/date regressions, builds an isolated production target and checks its SEO metadata and file safety.
3. The same run retains `araya-production-<commit SHA>` containing a ZIP and SHA-256/provenance manifest, then publishes the preview to GitHub Pages.
4. Review that preview. Promote the checked production package to Rumahweb using SSH/SFTP, initially through a manually triggered production workflow with a `production` GitHub environment and serialized deployments.
5. Verify the live root, brand pages, images, navigation, contacts, redirects and indexing. Retain the previous release for rollback.

**Steps 1–3 and manual private staging are implemented. Live activation and post-cutover verification remain pending.** The staging workflow transfers only the checked ZIP and manifest outside the web root. No workflow activates production, and no hosting credentials are stored in repository files.

GitHub builds the static site; Rumahweb serves the resulting HTML/CSS/JavaScript. The optional Linux VM is unnecessary for this site. Do not introduce a self-hosted runner on the hosting account just to upload static files.

## Hosting findings — directly observed

Read-only inspection of the owner's open Rumahweb cPanel session confirmed:

- Main domain: `arayainternusa.co.id`; document root: the account's `public_html`.
- SSL certificate is active. cPanel's Force HTTPS Redirect switch is off; existing server/hidden-file HTTPS behavior still needs checking before deciding on a change.
- SSH Access, Terminal, Git Version Control, FTP Accounts, Backup, Backup Wizard and file restoration interfaces are present. Their presence does **not** prove external SSH connectivity, the SSH port, rsync availability or permission to use a particular deployment layout.
- `public_html` contains the existing `araya` WordPress directory and a 44-byte root `index.php`.
- Viewed root `index.php` reads `header("Location: araya/"); exit;`. This explains the root-to-subdirectory redirect. A new `index.html` alone may not take precedence.
- No files, credentials, DNS, keys, permissions or live configuration were changed during inspection.

Actual account paths belong in private deployment configuration. Older local notes contain a different account-name spelling; re-read the current panel/SSH path when configuring deployment rather than copying those notes.

## Upload options

| Option | Assessment |
| --- | --- |
| GitHub Actions → SSH/SFTP to Rumahweb | Recommended, once real connectivity is verified. Build/test once, transfer the checked artifact, preserve release provenance and rollback. Use rsync only if installed and only within a dedicated release directory. |
| cPanel Git Version Control | Available as a fallback. Deployment requires a checked-in `.cpanel.yml`, clean worktree and appropriate shell/access setup. Never clone the whole repository into the public document root or copy it there with a wildcard. |
| File Manager ZIP upload | Useful for an initial supervised upload or recovery, but manual work does not provide repeatable CI/CD. Extract the ZIP into a private staging directory first. |
| FTPS | Fallback if SSH cannot be enabled. Use TLS and certificate verification; plain FTP is unsuitable for credentials/deployment traffic. File-by-file replacement also needs an explicit backup and activation strategy. |

The recommendation uses [cPanel's supported SSH/key facilities](https://docs.cpanel.net/cpanel/security/ssh-access/) and separates deployment from [cPanel Git deployment](https://docs.cpanel.net/knowledge-base/web-services/guide-to-git-deployment/). Rumahweb describes plan-dependent availability in its [SSH hosting guide](https://www.rumahweb.com/journal/cara-menggunakan-ssh-di-hosting/).

## Prepared build and package

From the repository directory:

```text
python tools/build.py
python tools/check.py
python tools/test_experience.py
python tools/test_loading.py
node tools/test_counters.cjs
node tools/test_company_dates.cjs
python tools/test_production.py
python tools/package_release.py
```

`python tools/build.py --target production` generates `dist/production/`; the production regression command above also runs that build. The production build copies the site's static assets and writes fresh pages; it does not overwrite `public/` and does not delete arbitrary files. Unexpected/stale files fail validation rather than being silently uploaded.

- `public/`: GitHub Pages preview; `noindex, nofollow`; preview canonical/OG/sitemap URLs. Preview robots permits crawling so search engines can read the noindex meta tags, following [Google's noindex guidance](https://developers.google.com/search/docs/crawling-indexing/block-indexing).
- `dist/production/`: root-domain canonical/OG/structured-data/sitemap URLs. Home, Noris and ComAp are `index, follow`. The three compatibility service routes are `noindex, follow`, canonical to the homepage, and retain their hash redirects. Production robots allows crawling and identifies the root sitemap.
- `dist/araya-production.zip`: site files at the ZIP root, ready for staging. Includes the font licence. Excludes repository metadata, tools, docs, deployment secrets, backups and PHP/WordPress files.
- `dist/release.json`: source commit, `source_tree_dirty`, raw `working_tree_dirty`, UTC build time, archive SHA-256 and individual file SHA-256 values. Source cleanliness excludes only the eight generated preview HTML/discovery files; templates, assets, docs, workflows and untracked source edits still count. The raw working-tree flag can be true solely because build dates changed generated pages. Keep the manifest with the release record outside the public document root.
- `dist/` is ignored by Git. The package is generated by CI; do not commit binary release archives.

Local packages built from uncommitted source edits have `source_tree_dirty: true` and are review candidates. Promote a successful CI package with `source_tree_dirty: false` from a reviewed `main` commit for the real release. The artifact is retained for 14 days; preserve the chosen package and manifest in private release storage before expiry. Rebuild/test a new package if the selected artifact has expired. CI provenance is evidence of which source was built, not a guarantee of server compatibility.

## Production workflow activation requirements

Prepare these settings only after owner authorization to grant deployment access:

| GitHub environment setting | Purpose |
| --- | --- |
| `PRODUCTION_SSH_HOST` | Provider-confirmed SSH host; a cPanel browser URL is not an SSH endpoint. |
| `PRODUCTION_SSH_PORT` | Provider-confirmed SSH port; do not assume the cPanel HTTPS port. |
| `PRODUCTION_SSH_USER` | Deployment identity with the smallest access the provider supports. |
| `PRODUCTION_SSH_KEY` | Dedicated private key as an environment secret; never paste it into chat or commit it. |
| `PRODUCTION_KNOWN_HOSTS` | Host key independently verified against Rumahweb, with strict host-key checking enabled. Do not blindly trust an unverified `ssh-keyscan` result. |
| Future activation release root | Must be verified outside `public_html`; not a secret consumed by the staging workflow. |
| Activation configuration | Exact approved document-root/entry-point configuration, discovered from the real account. |

The production job should be manual at first, restricted to main, use a single `production` concurrency group with `cancel-in-progress: false`, and consume an immutable successful build from this repository's main workflow. Verify the build's repository, workflow, conclusion, branch, source SHA, `source_tree_dirty: false`, archive checksum and every staged file checksum before activation. Do not rebuild a different commit after approval or select an artifact by a mutable name such as "latest".

Use a GitHub `production` environment to scope secrets and branch restrictions; enable required reviewers if the account/repository plan supports them. [GitHub documents environment protections and their availability](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments). The owner approved this access; the production environment now contains the five SSH connection secrets and a main-only branch policy. API readback confirms the policy and secret names. No required-reviewer rule was present or removed; live activation is not implemented.

The final activation script must validate resolved paths and reject a release/document root outside its configured account directories. If permitted, keep versioned release directories and switch a verified symlink atomically. **Symlink support and main-domain document-root behavior are unverified**; do not assume cPanel allows replacing the main document root. If unavailable, use a supervised staged copy with per-file rollback and an explicit managed-file manifest. Never run `rsync --delete` against the whole `public_html` or the hosting home directory.

## First cutover runbook

These are pending operational steps, not actions already performed:

1. Confirm SSH login, host key, effective user/home, document root, disk headroom, available transfer tools and permissions. Inspect hidden root and WordPress `.htaccess`, symlinks, DirectoryIndex order, HTTPS/www handling and any verification files. Keep all connection details private.
2. Make a current full file backup **and WordPress database backup**. Store/download them outside the web-accessible document root. Verify archive contents and a usable restoration procedure. Existing archives alone do not prove a current complete backup.
3. Inventory the old site's actual public URLs, PDFs and linked media. Public crawler access to the root robots and WordPress sitemap could not be confirmed during this session; the URL inventory remains a cutover prerequisite. Obtain it through the current WordPress/admin/files or Search Console if necessary.
4. Write explicit 301 mappings from the actual legacy URLs to the relevant new content. At minimum the old `/araya/` landing page will map to `/`. Map service URLs to their corresponding homepage sections; keep useful brand destinations distinct. Do not redirect every old path blindly to `/`: assets/downloads/admin routes need separate handling. Retain the previous WordPress files privately or otherwise prevent duplicate indexing after cutover.
5. Download the approved CI package and manifest; verify checksums. Upload/extract only the package into the confirmed private staging/release directory. Do not upload the repository or backup archives to the public root.
6. Review a protected staged copy and test the intended server configuration. If exposed at a staging URL, protect it from indexing separately; the production package itself is intentionally indexable. Verify no mail/account files are in the managed deployment set.
7. At an agreed cutover, back up the exact existing root entry point and hidden configuration privately. Apply the approved entry-point change so root serves the static site instead of redirecting to WordPress. Merge necessary HTTPS/DirectoryIndex/redirect directives with existing provider settings; do not overwrite `.htaccess` blindly. Uploading `index.html` alone is insufficient evidence of activation.
8. Verify HTTPS root and `/noris/`, `/comap/`, CSS/fonts/images, mobile navigation, final contact destinations, old-link 301s, canonical/OG/JSON-LD, robots and sitemap. Verify that missing URLs return a real 404 and that no redirect loop or old noindex header remains. Do not send a test WhatsApp message or email without authorization.
9. Keep the old release and database backup available. Submit the production sitemap in the owner's Search Console after successful cutover; DNS and email records should not need a change when retaining Rumahweb hosting. Server-side performance and caching must be checked on Rumahweb after deployment; preview timing is not a production measurement.

## Rollback

Before activation, record the exact previous root entry point, hidden configuration, deployment-owned files and release destination. If the new root fails, restore that entry point/configuration (including the old redirect if restoring WordPress), switch back the previous release where supported, and undo only the files owned by this deployment. Restore WordPress files/database only if they were actually changed; the static deployment should not write to its database. Re-test the old home/brand links and SSL before closing the incident.

No general recursive-delete command or guessed server path is supplied here. The tested rollback commands must be filled in from the verified layout before the first real deployment.

## Actions policy and verification

`.github/workflows/pages.yml` runs on `push` to `main` or manual dispatch, with a main-only job guard. `.github/workflows/production-stage.yml` runs only by manual dispatch on main and uploads into private Rumahweb staging. Neither workflow has PR event triggers or activates the live website. Validation and production packaging precede preview publication, so a failure stops publication. Do not add skip-CI text to merge commits; default-branch checks/deployment should run normally.

Fresh verification results and published preparation commit/run are recorded in `PROGRESS.md` after review. Implementation plan: [PRODUCTION-PLAN-2026-10-14.md](PRODUCTION-PLAN-2026-10-14.md).


## Manual private staging operation

1. Wait for a successful **Check website and publish preview** run on reviewed `main` source. Copy its numeric run ID.
2. In Actions, run **Stage production package on Rumahweb** on `main`, supplying that ID as `build_run_id`.
3. The job verifies the same repository, expected workflow, successful completed run, branch, source SHA, clean-source manifest, archive hash and every file hash. It rejects unsafe paths, unexpected files, duplicate entries and symlinks.
4. The job authenticates using pinned host keys, creates a fresh private directory identified by source SHA/run/attempt, transfers ZIP plus manifest, and verifies both remote SHA-256 values. The directory must physically resolve under the expected account staging base.
5. Record the source/build/staging run and verify the existing live entry point still matches its backup. A successful staging run does not extract the package or switch the site.

The dedicated SSH key has hosting-account shell/file access. GitHub environment scoping and branch restriction govern workflow access to it; the key itself is not restricted to staging paths by the provider. To revoke it, deauthorize the dedicated key in cPanel and remove/rotate the GitHub environment key secret. Keep private backups and host-key evidence outside Git.

Checks: six release-candidate regression tests passed; Bash syntax passed; independent critical review found no blocking or major issues. See [staging plan and evidence](PRODUCTION-SSH-PLAN-2026-10-14.md). First end-to-end run evidence will be recorded after execution.
