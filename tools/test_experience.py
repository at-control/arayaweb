"""Regression checks for enquiry context and navigation in the generated site."""
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, parse_qs

PUBLIC = Path(__file__).resolve().parents[1] / 'public'


class Links(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.links = []
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.links.append(dict(attrs))


class ExperienceTests(unittest.TestCase):
    def test_contact_keeps_current_page(self):
        for path in PUBLIC.rglob('index.html'):
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


if __name__ == '__main__':
    unittest.main()
