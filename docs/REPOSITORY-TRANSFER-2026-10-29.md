# Repository transfer and CI/CD verification

29 October 2026, Asia/Jakarta.

The owner approved transferring the public repository from `hakiimm8/arayaweb` to `at-control/arayaweb`. The transfer completed before a cancellation message; the owner subsequently accepted keeping it in the organisation provided CI/CD works.

- Repository: https://github.com/at-control/arayaweb
- Preview: https://at-control.github.io/arayaweb/
- Production: https://arayainternusa.co.id/

## Inspection and changes

- Repository Actions are enabled and allow the existing actions.
- GitHub Pages retains the workflow deployment source and HTTPS enforcement.
- Both `github-pages` and `production` environments retain their `main` branch restriction.
- All five production secret names remain present: SSH host, port, user, private key and known hosts. No secret values were displayed.
- Workflows have no `pull_request` or `pull_request_target` triggers. Main pushes run checks and publish preview; successful main builds trigger production deployment.
- Production scripts use GitHub's current repository identity dynamically for run validation, artifact download and source checks.
- Updated the preview generator/checker and README to the new Pages hostname. Historical release notes retain their original URLs.
- Production validation rejects both preview hostnames. Measurement isolation covers both Pages hostnames; preview must never initialise production analytics.
- Existing uncommitted Ads research and progress notes are excluded from this transfer commit. Ads remain unlaunched.

## Verification

Local preview build/check passed, along with five production packaging/isolation tests, six release-candidate tests and consent/contact measurement tests. The new preview hostname is explicitly covered by measurement isolation.

Post-transfer check/deployment run IDs and live verification will be recorded after the new main build completes. The existing production release is independent of repository ownership and remains hosted on Rumahweb. Current runs are available at https://github.com/at-control/arayaweb/actions.
