# GitHub SSH staging implementation plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Configure the owner-approved deployment key and verify a manual GitHub Actions upload into private Rumahweb staging.

**Architecture:** A manual, main-only workflow selects a successful main preview/build run, validates its immutable production ZIP/manifest, then transfers only those two files through pinned-host SSH/SCP. It verifies both remote checksums and does not activate/extract into the live document root.

**Tech Stack:** Python standard library, GitHub CLI/Actions, OpenSSH/SCP, Bash.

**Spec:** Owner approved authorizing the prepared key and storing it in the `hakiimm8/arayaweb` production environment on 14 October 2026. Live cutover is excluded. Hosting findings in PRODUCTION-DEPLOYMENT.md apply.

## Constraints and review focus

- Production job is workflow_dispatch only, main-only, serialized and environment-scoped; no PR triggers.
- Consume only completed successful main runs of this repository's pages.yml; reject forks, other workflows/branches and dirty sources.
- Validate ZIP and manifest contents/checksums; reject unsafe paths, duplicates, symlinks, unexpected publication files and incomplete packages.
- Use strict host-key verification. Credentials never appear in repository files, logs or process arguments.
- Upload only to a new private directory below `/home/<validated account>/araya-deploy/incoming`; reject symlink/physical-path mismatch. No root activation or recursive deletion.
- Preserve existing environment protections; restrict the new production environment to main. No reviewer gate is silently disabled.

## Tasks / ledger

- [x] Import/authorize the approved public key; verify pinned-host authentication and save private evidence.
- [x] Write negative/positive candidate-validation tests and observe failure; implement run/package/destination validation.
- [x] Add the manual staging workflow/script and run checks plus independent review.
- [x] Configure approved environment/secrets privately, preserving any existing protections.
- [ ] Push, dispatch a staging upload, verify remote SHA-256s and unchanged live root, and record the run.

Ruling: use SCP package transfer because rsync is absent from the hosting shell; staging remains separate from activation because the owner explicitly excluded the live switch from this approval.

## Verification record

The initial candidate tests failed because the validation module did not exist; implementation made them pass. Six tests now cover run provenance, source cleanliness, exact publication contents, unsafe paths, duplicates, destination injection, inner-file tampering with a correct outer ZIP hash, and symlink entries. Bash syntax validation passed. Independent critical review found no blocking or major issues. Its suggested inner-tamper and symlink fixtures were added. A separate shell fixture suite for remote-directory guards is deferred; the first staging run will exercise the real directory creation and upload, but will not prove every refusal case.

GitHub API readback confirmed the production environment permits only the `main` branch and contains the five expected secret names. The key value was provided through standard input, never a command-line argument or repository file. Pinned-host SSH authentication succeeded, and the root entry-point hash still matched the backup.
