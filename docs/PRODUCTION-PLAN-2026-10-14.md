# Root-domain production preparation

## Design and scope

Owner request: prepare the static Araya site for `https://arayainternusa.co.id/` and review GitHub CI integration. Keep the existing design/content. Preparation does not switch the live domain or create deployment credentials.

Use GitHub Actions to validate the preview and create a separate, indexable production package from the same commit. Retain GitHub Pages as the noindex preview. Recommend SSH/SFTP to Rumahweb for deployment, with a manual production promotion initially; no VM is required for this static site.

Do not automate activation before confirming SSH connectivity, server tools, existing hidden configuration, full backup and restoration, and the permitted release layout. Root `index.php` currently redirects to `araya/`; copying HTML alone is insufficient.

# Production preparation implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a checked production package and an actionable hosting deployment runbook without changing production.

**Architecture:** Fixed preview and production build targets. CI runs existing regressions and validates both targets before preview publication, then retains the production ZIP and checksum manifest. SSH deployment remains a separate activation step after hosting prerequisites are verified.

**Tech Stack:** Python standard library, static HTML/CSS/JavaScript, GitHub Actions, Rumahweb cPanel.

**Spec:** Design and scope above; detailed findings in PRODUCTION-DEPLOYMENT.md.

## Global Constraints

- Production base URL: `https://arayainternusa.co.id/`.
- Preview retains `noindex, nofollow`; only production content routes are indexable.
- Never deploy repository files, credentials, databases, backups or tooling.
- No Actions triggers for pull requests. Default-branch pushes retain validation and preview deployment.
- No production write, DNS change or access grant in this preparation.

## Review Focus

- Production metadata accidentally references preview or the old subdirectory: assert canonical/OG/structured-data/sitemap origin.
- Production build overwrites the preview: compare preview bytes before/after isolated build.
- Empty/incomplete or sensitive package: require six routes, real assets, allowlisted files and matching checksums.
- Failed validation still publishes: workflow validation must precede deployment; packaging validates its input.
- Existing WordPress/root redirect causes a cutover failure: document entry-point, hidden configuration and backup gates; do not automate unverified root changes.

## Tasks

- [x] Add production regression tests; run them and confirm the current build lacks the required target.
- [x] Add fixed production build target, target-aware validation and ZIP/checksum packaging. Run both target checks and regressions.
- [x] Add checks and production artifact retention before Pages deployment. Inspect all workflows for PR triggers.
- [x] Document verified hosting facts, SSH recommendation, cutover, redirect mapping and rollback prerequisites.
- [x] Obtain independent code review and resolve findings. Review caught preview crawl/noindex interaction and generated-date provenance; both corrected with regression coverage. Final local verification passed; CI publication result is recorded in PROGRESS.md.
