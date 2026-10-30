# GitHub organization rename — 30 October 2026

The owner requested renaming `at-control` to `arayainternusa`. GitHub confirmed the rename, retaining organization ID `327695786` and all ten repository IDs, with the same nine private repositories and one public repository.

- Repository: https://github.com/arayainternusa/arayaweb
- Preview: https://arayainternusa.github.io/arayaweb/
- Production: https://arayainternusa.co.id/

The local Git remotes now use the new organization. The preview build base, preview validator, repository fixture and README links use the new namespace. Generated preview HTML and the sitemap were rebuilt. Production metadata still uses the company domain, and production validation rejects both old and new GitHub Pages URLs. Preview analytics isolation now covers the new hostname as well.

The existing main-only preview/build and production-promotion workflows remain unchanged. They use `github.repository` / `GITHUB_REPOSITORY`, rather than a hard-coded old owner. No pull-request triggers or skip-CI instructions were added. The original WordPress rollback data remains untouched.

Local validation: preview build and link/metadata checks, experience checks, JavaScript syntax, production metadata/package tests, release-candidate checks, and preview measurement-isolation checks. Remote deployment results are retained with the organization-rename audit in the local workspace.

The dated 29 October transfer notes retain the organization name used at that time.
