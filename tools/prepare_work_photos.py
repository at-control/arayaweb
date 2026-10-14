"""Encode owner-supplied work photos as responsive web assets.

Run with a Python environment containing Pillow:
    python tools/prepare_work_photos.py --source ../picture

Original photos are kept outside the repository. This only changes encoding,
size and EXIF orientation; no retouching or date-stamp removal is performed.
"""
import argparse
from pathlib import Path
from PIL import Image, ImageOps

IMAGES = Path(__file__).resolve().parents[1] / 'public/assets/images'
SOURCES = {'003.jpg': 'work-engine-room', 'IMG_3859.JPG': 'work-switchboard'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True, type=Path)
    args = parser.parse_args()
    for name, stem in SOURCES.items():
        with Image.open(args.source / name) as source:
            original = ImageOps.exif_transpose(source).convert('RGB')
            for width in (800, 1280):
                photo = original.copy()
                photo.thumbnail((width, width * 2), Image.Resampling.LANCZOS)
                target = IMAGES / f'{stem}-{width}.webp'
                photo.save(target, 'WEBP', quality=84, method=6)
                print(f'{target.name}: {photo.width}x{photo.height}, {target.stat().st_size} bytes')


if __name__ == '__main__':
    main()
