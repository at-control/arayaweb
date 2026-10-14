"""Critical-image discovery and early picture loading budgets."""
from html.parser import HTMLParser
from pathlib import Path
import unittest

PUBLIC = Path(__file__).resolve().parents[1] / 'public'


class Resources(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.images, self.preloads, self.pictures = [], [], []
        self.in_product = False
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'figure':
            self.in_product = attrs.get('class') == 'portfolio-picture'
        if tag == 'img' and attrs.get('src'):
            self.images.append(attrs)
            if self.in_product:
                self.pictures.append(attrs)
        if tag == 'link' and attrs.get('rel') == 'preload' and attrs.get('as') == 'image':
            self.preloads.append(attrs)

    def handle_endtag(self, tag):
        if tag == 'figure':
            self.in_product = False


class LoadingTests(unittest.TestCase):
    def test_hero_is_discovered_in_head_without_duplicate_candidate(self):
        for route in ['index.html', 'noris/index.html', 'comap/index.html']:
            with self.subTest(route=route):
                page = Resources(PUBLIC / route)
                self.assertEqual(len(page.preloads), 1)
                hero = next(img for img in page.images if img.get('fetchpriority') == 'high')
                preload = page.preloads[0]
                self.assertEqual(preload['href'], hero['src'])
                self.assertEqual(preload.get('imagesrcset'), hero.get('srcset'))
                self.assertEqual(preload.get('imagesizes'), hero.get('sizes'))

    def test_product_pictures_do_not_wait_for_scrolling(self):
        for route, count in [('noris/index.html', 8), ('comap/index.html', 6)]:
            page = Resources(PUBLIC / route)
            # The high-priority hero and logo are separate from the catalogue.
            pictures = page.pictures
            self.assertEqual(len(pictures), count)
            for picture in pictures:
                self.assertEqual(picture.get('loading'), 'eager')
                self.assertEqual(picture.get('fetchpriority'), 'low')

    def test_early_images_stay_small_and_hidden_diagrams_stay_deferred(self):
        for route in ['index.html', 'noris/index.html', 'comap/index.html']:
            path = PUBLIC / route
            page = Resources(path)
            files = {(path.parent / img['src']).resolve() for img in page.images
                     if img.get('loading') != 'lazy'}
            self.assertLess(sum(file.stat().st_size for file in files), 750_000, route)
        comap = Resources(PUBLIC / 'comap/index.html')
        hidden_diagrams = [img for img in comap.images if 'comap-diagram-' in img['src']]
        self.assertGreater(len(hidden_diagrams), 0)
        self.assertTrue(all(img.get('loading') == 'lazy' for img in hidden_diagrams))


if __name__ == '__main__':
    unittest.main()
