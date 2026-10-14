"""Trace the owner's high-resolution PDF artwork into sharp web SVG assets.

Requires Pillow, numpy, pypdf and vtracer 0.6.15. The PDF stays outside the repo.
Run with --pdf path/to/cp.pdf; no generated or substituted lettering is used.
"""
import argparse
from io import BytesIO
from pathlib import Path
import re
import numpy as np
from PIL import Image
from pypdf import PdfReader
import vtracer


def trace(mask, fill, title):
    rgba = np.full((*mask.shape, 4), 255, dtype=np.uint8)
    rgba[mask, :3] = 0
    encoded = BytesIO()
    Image.fromarray(rgba).save(encoded, format='PNG')
    svg = vtracer.convert_raw_image_to_svg(encoded.getvalue(), img_format='png',
        colormode='binary', mode='spline', filter_speckle=4, path_precision=2)
    height, width = mask.shape
    svg = svg.replace(f'width="{width}" height="{height}"',
                      f'viewBox="0 0 {width} {height}" width="{width}" height="{height}"')
    svg = re.sub(r'fill="#[0-9A-Fa-f]{6}"', f'fill="{fill}"', svg)
    svg = svg.replace('<!-- Generator:', f'<!-- Source: owner company profile, first-page original artwork. {title}. -->\n<!-- Generator:')
    return svg


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdf', type=Path, required=True)
    args = parser.parse_args()
    artwork = next(image for image in PdfReader(args.pdf).pages[0].images
                   if Image.open(BytesIO(image.data)).size == (4165, 961))
    rgba = np.asarray(Image.open(BytesIO(artwork.data)).convert('RGBA'))
    white = np.all(rgba[:, :, :3] > 220, axis=2)
    black = np.all(rgba[:, :, :3] < 50, axis=2)
    # Original white emblem; original black wordmark becomes white for the dark header.
    mask = ((white & (np.arange(rgba.shape[1])[None, :] < 1000)) |
            (black & (np.arange(rgba.shape[1])[None, :] >= 1000))) & (rgba[:, :, 3] > 128)
    destination = Path(__file__).resolve().parents[1] / 'public/assets/images'
    (destination / 'araya-logo.svg').write_text(trace(mask, '#FFFFFF', 'White web lockup'), encoding='utf-8')
    (destination / 'araya-icon.svg').write_text(trace(mask[:, :961], '#ee5c03', 'Orange emblem'), encoding='utf-8')
    print('Traced the original 4165 × 961 artwork into header and tab-icon SVGs.')
