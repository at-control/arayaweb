"""Package the validated production site, never repository or hosting files."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile
from check import ALL_ROUTES

ROOT = Path(__file__).resolve().parents[1]


def git_provenance(root):
    def git(*args):
        return subprocess.check_output(['git', *args], cwd=root, text=True).strip()
    # HTML/discovery files are generated from committed tools; asset edits are sources.
    generated = sorted(ALL_ROUTES | {'sitemap.xml', 'robots.txt'})
    source_status = git('status', '--porcelain', '--untracked-files=all', '--', '.',
                        *(f':(exclude)public/{name}' for name in generated))
    return {
        'source_commit': git('rev-parse', 'HEAD'),
        'source_tree_dirty': bool(source_status),
        'working_tree_dirty': bool(git('status', '--porcelain', '--untracked-files=all')),
    }


def main():
    check = subprocess.run([sys.executable, str(ROOT / 'tools/check.py'), '--target', 'production'], cwd=ROOT)
    if check.returncode:
        return check.returncode
    source = ROOT / 'dist/production'
    archive = ROOT / 'dist/araya-production.zip'
    files = sorted(p for p in source.rglob('*') if p.is_file())
    hashes = {}
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as output:
        for path in files:
            name = path.relative_to(source).as_posix()
            data = path.read_bytes()
            hashes[name] = hashlib.sha256(data).hexdigest()
            output.writestr(name, data)
    manifest = {
        'target': 'https://arayainternusa.co.id/',
        **git_provenance(ROOT),
        'built_at_utc': datetime.now(timezone.utc).isoformat(),
        'archive': archive.name, 'archive_sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
        'files': hashes,
    }
    (ROOT / 'dist/release.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    print(f'Packaged {len(files)} site files: {archive.name}; checksum/provenance: release.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
