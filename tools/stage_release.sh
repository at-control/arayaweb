#!/usr/bin/env bash
# Transfer a checked candidate into a new private directory; no live activation.
set -euo pipefail

[[ "$PRODUCTION_SSH_HOST" =~ ^[A-Za-z0-9][A-Za-z0-9.-]*$ ]] || exit 1
[[ "$PRODUCTION_SSH_PORT" =~ ^[0-9]{1,5}$ ]] || exit 1
(( 10#$PRODUCTION_SSH_PORT > 0 && 10#$PRODUCTION_SSH_PORT <= 65535 )) || exit 1
[[ "$ARCHIVE_SHA" =~ ^[a-f0-9]{64}$ && "$MANIFEST_SHA" =~ ^[a-f0-9]{64}$ ]] || exit 1
remote_path=$(python tools/release_candidate.py destination "$PRODUCTION_SSH_USER" "$BUILD_SHA" "$GITHUB_RUN_ID" "$GITHUB_RUN_ATTEMPT")
remote_base=${remote_path%/*}
target="$PRODUCTION_SSH_USER@$PRODUCTION_SSH_HOST"

umask 077
ssh_dir=$(mktemp -d "$RUNNER_TEMP/araya-ssh.XXXXXX")
trap 'rm -f "$ssh_dir/key" "$ssh_dir/known_hosts"; rmdir "$ssh_dir"' EXIT
printf '%s\n' "$PRODUCTION_SSH_KEY" > "$ssh_dir/key"
printf '%s\n' "$PRODUCTION_KNOWN_HOSTS" > "$ssh_dir/known_hosts"
unset PRODUCTION_SSH_KEY PRODUCTION_KNOWN_HOSTS
options=(-i "$ssh_dir/key" -o "UserKnownHostsFile=$ssh_dir/known_hosts" -o StrictHostKeyChecking=yes
         -o BatchMode=yes -o IdentitiesOnly=yes -o IdentityAgent=none -o PasswordAuthentication=no
         -o ClearAllForwardings=yes -o ConnectTimeout=15 -o ServerAliveInterval=15 -o ServerAliveCountMax=2)

# Reject a base resolving through a symlink or outside the expected account path.
ssh -p "$PRODUCTION_SSH_PORT" "${options[@]}" "$target" \
  "test -d '$remote_base' && test \"\$(cd '$remote_base' && pwd -P)\" = '$remote_base' && mkdir -m 700 '$remote_path'"
scp -q -P "$PRODUCTION_SSH_PORT" "${options[@]}" payload/araya-production.zip payload/release.json "$target:$remote_path/"
archive_result=$(ssh -p "$PRODUCTION_SSH_PORT" "${options[@]}" "$target" "sha256sum '$remote_path/araya-production.zip'")
manifest_result=$(ssh -p "$PRODUCTION_SSH_PORT" "${options[@]}" "$target" "sha256sum '$remote_path/release.json'")
[[ "${archive_result%% *}" == "$ARCHIVE_SHA" && "${manifest_result%% *}" == "$MANIFEST_SHA" ]]
printf 'Private staging upload verified for commit %s. Live website unchanged.\n' "$BUILD_SHA"
printf '### Private staging verified\n\nSource commit: `%s`\n\nBuild run: `%s`\n\nZIP and manifest SHA-256 match. No live activation.\n' "$BUILD_SHA" "$BUILD_RUN_ID" >> "$GITHUB_STEP_SUMMARY"
