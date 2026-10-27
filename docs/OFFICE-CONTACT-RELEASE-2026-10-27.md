# Office, coverage and contact update — 27 October 2026

Owner authorised deployment after local review. Shared header now says “Surabaya & Jakarta Offices”; marine copy and metadata state ship maintenance, repair and retrofit across Indonesia. Precise Sidoarjo postal address remains. Business hours removed from header, footer and structured data. WhatsApp +62 813 2639 6262 replaces the landline in visible contact links and organization telephone; footer avoids duplicate numbers.

Before deployment, consent/runtime tests, two tracking-build tests and five production tests passed. Earlier static validation and six experience tests passed. The live measurement.js matches the local runtime; the published GTM-NK3C3RVZ container contains G-WMBDHTFPBJ and contact_click. Production builds retain consent-controlled measurement and local previews remain isolated. This verifies installation/configuration, not new event receipt in GA4; actual receipt was previously verified on 23 October. Contact clicks are not qualified leads. No advertising campaign is launched by this release.

Deploy through the existing successful-main-build → production workflow. No PR triggers exist. Main CI runs full checks before production promotion and verifies public file hashes after activation, with guarded rollback on failure. Deployment outcome is recorded in GitHub Actions and local progress notes.
