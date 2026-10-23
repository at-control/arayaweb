"""Validate an immutable main-build artifact before private SSH staging."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import zipfile
from check import ALL_ROUTES, ASSET_SUFFIXES

SHA_PATTERN = re.compile(r'[a-f0-9]{40}')
REQUIRED = ALL_ROUTES | {'robots.txt', 'sitemap.xml', 'assets/site.css', 'assets/site.js',
    'assets/measurement.js', 'assets/measurement.css',
    'assets/company-date.js', 'assets/service-redirect.js', 'assets/fonts/space-grotesk.woff2',
    'assets/fonts/OFL.txt'}


def validate_run(run, repository):
    if (run.get('path') != '.github/workflows/pages.yml' or run.get('head_branch') != 'main'
            or run.get('status') != 'completed' or run.get('conclusion') != 'success'
            or run.get('event') not in {'push', 'workflow_dispatch'}
            or (run.get('head_repository') or {}).get('full_name', '').casefold() != repository.casefold()
            or not SHA_PATTERN.fullmatch(run.get('head_sha', ''))):
        raise ValueError('Candidate must be a successful main build from this repository')
    return run['head_sha']


def allowed_name(name):
    path = PurePosixPath(name)
    if (not name or '\\' in name or path.is_absolute() or name != path.as_posix()
            or any(part in {'.', '..'} or part.startswith('.') for part in path.parts)):
        return False
    return (name in ALL_ROUTES | {'robots.txt', 'sitemap.xml', 'assets/fonts/OFL.txt'}
            or (name.startswith('assets/') and path.suffix.lower() in ASSET_SUFFIXES))


def validate_package(directory, expected_sha):
    directory = Path(directory)
    if not SHA_PATTERN.fullmatch(expected_sha):
        raise ValueError('Invalid source commit')
    manifest_path, archive_path = directory / 'release.json', directory / 'araya-production.zip'
    if (manifest_path.is_symlink() or archive_path.is_symlink() or not manifest_path.is_file()
            or not archive_path.is_file() or manifest_path.stat().st_size > 2_000_000
            or archive_path.stat().st_size > 50_000_000):
        raise ValueError('Invalid or oversized candidate files')
    manifest_bytes = manifest_path.read_bytes()
    manifest = json.loads(manifest_bytes)
    archive_bytes = archive_path.read_bytes()
    archive_hash = hashlib.sha256(archive_bytes).hexdigest()
    files = manifest.get('files')
    if (manifest.get('source_commit') != expected_sha or manifest.get('source_tree_dirty') is not False
            or manifest.get('target') != 'https://arayainternusa.co.id/'
            or manifest.get('archive') != archive_path.name or manifest.get('archive_sha256') != archive_hash
            or not isinstance(files, dict) or not REQUIRED.issubset(files)
            or not all(allowed_name(name) and isinstance(value, str) and re.fullmatch(r'[a-f0-9]{64}', value)
                       for name, value in files.items())):
        raise ValueError('Invalid candidate provenance, file set or checksum')
    try:
        with zipfile.ZipFile(archive_path) as archive:
            entries = archive.infolist()
            if (len(entries) > 5000 or len(entries) != len(files)
                    or len({entry.filename for entry in entries}) != len(entries)
                    or {entry.filename for entry in entries} != set(files)
                    or sum(entry.file_size for entry in entries) > 100_000_000):
                raise ValueError('Invalid or oversized ZIP entries')
            for entry in entries:
                if (entry.is_dir() or stat.S_ISLNK(entry.external_attr >> 16)
                        or hashlib.sha256(archive.read(entry)).hexdigest() != files[entry.filename]):
                    raise ValueError('Invalid ZIP file content or symlink')
    except (zipfile.BadZipFile, RuntimeError) as exc:
        raise ValueError('Unreadable production ZIP') from exc
    return archive_hash, hashlib.sha256(manifest_bytes).hexdigest()


def destination(user, sha, run_id, attempt):
    if (not re.fullmatch(r'[a-z_][a-z0-9_-]{0,31}', user) or not SHA_PATTERN.fullmatch(sha)
            or not re.fullmatch(r'[1-9][0-9]{0,19}', run_id)
            or not re.fullmatch(r'[1-9][0-9]{0,9}', attempt)):
        raise ValueError('Invalid private staging destination')
    return f'/home/{user}/araya-deploy/incoming/{sha}-{run_id}-{attempt}'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    run = commands.add_parser('run')
    run.add_argument('json_file', type=Path)
    run.add_argument('repository')
    package = commands.add_parser('package')
    package.add_argument('directory', type=Path)
    package.add_argument('sha')
    target = commands.add_parser('destination')
    for name in ('user', 'sha', 'run_id', 'attempt'):
        target.add_argument(name)
    args = parser.parse_args()
    if args.command == 'run':
        print('sha=' + validate_run(json.loads(args.json_file.read_text(encoding='utf-8')), args.repository))
    elif args.command == 'package':
        archive_hash, manifest_hash = validate_package(args.directory, args.sha)
        print(f'archive_sha={archive_hash}\nmanifest_sha={manifest_hash}')
    else:
        print(destination(args.user, args.sha, args.run_id, args.attempt))


if __name__ == '__main__':
    main()
