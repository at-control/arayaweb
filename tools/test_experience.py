"""Regression checks for enquiry context and navigation in the generated site."""
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, parse_qs

PUBLIC = Path(__file__).resolve().parents[1] / 'public'


class Links(HTMLParser):
    def __init__(self, path=None, *, html=None):
        super().__init__()
        self.links = []
        self.feed(html if html is not None else path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.links.append(dict(attrs))


class ExperienceTests(unittest.TestCase):
    def test_contact_keeps_current_page(self):
        for path in PUBLIC.rglob('index.html'):
            if path.parent.name in {'marine', 'industrial', 'automation'}:
                continue  # These URLs are now compatibility redirects.
            with self.subTest(page=path.parent.name):
                link = next(a for a in Links(path).links if a.get('class') == 'nav-contact')
                self.assertEqual(link['href'], '#contact')

    def test_every_product_and_application_has_contextual_enquiry(self):
        for brand, expected in [('Noris', 8), ('ComAp', 24)]:
            links = [a for a in Links(PUBLIC / brand.lower() / 'index.html').links
                     if 'context-enquiry' in a.get('class', '').split()]
            self.assertEqual(len(links), expected)
            for link in links:
                url = urlsplit(link['href'])
                self.assertEqual(url.netloc, 'wa.me')
                self.assertEqual(url.path, '/6281326396262')
                draft = parse_qs(url.query)['text'][0]
                self.assertIn(brand, draft)
                self.assertGreater(len(draft), len('Hello Araya, I would like to discuss ' + brand + '.'))

    def test_company_positioning(self):
        html = (PUBLIC / 'index.html').read_text(encoding='utf-8')
        self.assertNotIn('Local engineers', html)
        self.assertNotIn('local talent', html)
        self.assertIn('International technical backing', html)
        self.assertIn('Certified &amp; experienced', html)

    def test_single_landing_page(self):
        html = (PUBLIC / 'index.html').read_text(encoding='utf-8')
        self.assertNotIn('Common requests', html)
        for service in ['marine', 'industrial', 'automation']:
            self.assertIn(f'id="{service}-services"', html)
            self.assertIn(f'href="#{service}-services"', html)
            for page in ['index.html', 'noris/index.html', 'comap/index.html']:
                self.assertNotIn(f'href="./{service}/"', (PUBLIC / page).read_text(encoding='utf-8'))
                self.assertNotIn(f'href="../{service}/"', (PUBLIC / page).read_text(encoding='utf-8'))
        sitemap = (PUBLIC / 'sitemap.xml').read_text(encoding='utf-8')
        self.assertEqual(sitemap.count('<url>'), 3)

    def test_brand_contents_covers_all_topics_and_application_first_flow(self):
        from brand_profiles import BRANDS
        import re
        for brand, data in BRANDS.items():
            html = (PUBLIC / brand / 'index.html').read_text(encoding='utf-8')
            # Limit links to the Contents component so unrelated product links
            # cannot mask a missing index entry.
            contents = re.search(r'<section class="brand-toc".*?</section>', html, re.S).group()
            links = Links(html=contents)
            anchors = {a['href'][1:] for a in links.links}
            expected = {p['id'] for p in data['products']}
            for group in data.get('application_groups', []):
                expected.update(item['id'] for item in group['items'])
            if not data.get('application_groups'):
                expected.update(f'choose-{anchor}' for _, _, anchor, _ in data['applications'])
            expected.update(['about-brand', 'araya-support', 'brand-faq'])
            self.assertEqual(anchors, expected, brand)
            positions = [html.index(f'id="{anchor}"') for anchor in
                         ['contents', 'about-brand', 'applications', 'portfolio', 'araya-support', 'brand-faq']]
            self.assertEqual(positions, sorted(positions), brand)
            for anchor in anchors:
                self.assertIn(f'id="{anchor}"', html, brand)


if __name__ == '__main__':
    unittest.main()
