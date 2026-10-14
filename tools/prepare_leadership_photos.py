"""Prepare original Araya portraits, retaining their composition and appearance.

Requires Pillow. Pass the original WordPress uploads directory with --source.
Only orientation, resize and WebP encoding are applied.
"""
import argparse
from pathlib import Path
from PIL import Image, ImageOps

IMAGES = Path(__file__).resolve().parents[1] / 'public/assets/images'
PORTRAITS = {'2024/03/dir1.png': 'leadership-arif',
             '2024/02/man1.png': 'leadership-rosul',
             '2024/01/man2.png': 'leadership-anjas'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True, type=Path)
    args = parser.parse_args()
    for name, stem in PORTRAITS.items():
        with Image.open(args.source / name) as source:
            original = ImageOps.exif_transpose(source).convert('RGB')
            for width in (400, 720):
                photo = original.copy()
                photo.thumbnail((width, width * 2), Image.Resampling.LANCZOS)
                target = IMAGES / f'{stem}-{width}.webp'
                photo.save(target, 'WEBP', quality=82, method=6)
                print(f'{target.name}: {photo.width}x{photo.height}, {target.stat().st_size} bytes')


if __name__ == '__main__':
    main()
