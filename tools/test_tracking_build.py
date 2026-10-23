"""Tracking build boundaries and privacy deployment contract."""
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class TrackingBuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        for target in ('preview', 'production'):
            subprocess.run([sys.executable, 'tools/build.py', '--target', target], cwd=ROOT, check=True, capture_output=True)

    def test_shared_consent_and_privacy_navigation(self):
        for folder, target in [('public','preview'), ('dist/production','production')]:
            for route in ('', 'noris/', 'comap/', 'privacy/'):
                path = ROOT / folder / route / 'index.html'
                self.assertTrue(path.exists(), 'Privacy must be a real generated route')
                html = path.read_text(encoding='utf-8')
                self.assertIn('id="consent-banner"', html)
                self.assertLess(html.index('id="consent-banner"'),html.index('<header'),'Consent choices must be early in keyboard tab order')
                self.assertIn('data-consent-action="reject"', html)
                self.assertIn('data-consent-action="open"', html)
                self.assertIn(f'data-measurement="{target}"', html)
                self.assertNotIn('src="https://www.googletagmanager.com', html, 'No unconditional Google loading')
                self.assertNotIn('googletagmanager.com/ns.html', html, 'No pre-consent noscript request')
                self.assertIn('data-contact-location="footer"', html)
            for legacy in ('marine','industrial','automation'):
                html=(ROOT/folder/legacy/'index.html').read_text(encoding='utf-8')
                self.assertNotIn('data-measurement="production"',html,'Compatibility redirects must not add a page view')

    def test_privacy_can_be_packaged_and_routed(self):
        sys.path.insert(0,str(ROOT/'tools'))
        from release_candidate import allowed_name
        from release_candidate import REQUIRED
        self.assertTrue({'assets/measurement.js','assets/measurement.css'} <= REQUIRED,'Immutable releases must include the consent runtime and styles')
        self.assertTrue(allowed_name('privacy/index.html'))
        router=(ROOT/'tools/production.htaccess').read_text()
        self.assertIn('automation|privacy',router)
        deploy=(ROOT/'tools/deploy_release.php').read_text()
        self.assertIn("'privacy/index.html'",deploy)
        self.assertIn("'automation','privacy','robots.txt'",deploy)
        activation=(ROOT/'tools/activate_release.sh').read_text()
        self.assertIn('automation privacy robots.txt',activation,'SSH must prepare the new privacy link on hosts without PHP symlink support')

if __name__=='__main__': unittest.main()
