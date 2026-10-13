"""Build the homepage, service pages and brand guides using a shared shell."""
from pathlib import Path
from html import escape
from urllib.parse import quote
import json
import hashlib
from brand_profiles import BRANDS
from brand_pages import brand_content
from ui_components import page_index
from site_content import SERVICES, CLIENTS, BRAND_GROUPS, CAPABILITIES

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
BASE = "https://hakiimm8.github.io/arayaweb/"
PRODUCTION = "https://arayainternusa.co.id/araya/"
ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15M13 5l7 7-7 7"/></svg>'
def asset_version(name):
    # Normalise line endings so Windows (CRLF) and Linux checkouts produce identical output.
    return hashlib.sha256((PUBLIC / 'assets' / name).read_bytes().replace(b'\r\n', b'\n')).hexdigest()[:10]

CSS_VERSION = asset_version('site.css')
JS_VERSION = asset_version('site.js')
EMAIL = "cs@arayainternusa.com"
MAP = "https://www.google.com/maps/search/?api=1&query=" + quote("Gateway Citra Harmoni RKG 32-33, Taman, Sidoarjo")
JAKARTA_MAP = "https://www.google.com/maps/search/?api=1&query=" + quote("Townhouse PIK, Jakarta")


def whatsapp(topic="a project"):
    return "https://wa.me/6281326396262?text=" + quote(f"Hello Araya, I would like to discuss {topic}.")


def organization():
    return {
        "@type": "ProfessionalService", "@id": BASE + "#organization",
        "name": "PT Araya Internusa", "alternateName": "Araya Internusa", "url": PRODUCTION,
        "logo": BASE + "assets/images/araya-logo.png", "image": BASE + "assets/images/og-araya.jpg",
        "description": "Marine, industrial and automation engineering company serving Indonesia: supply, repair, modification, upgrade and retrofit since 2009.",
        "email": EMAIL, "telephone": "+62-31-7877990", "foundingDate": "2009",
        "founder": {"@type": "Person", "name": "Arif Fatkur Rohman"},
        "address": {"@type": "PostalAddress", "streetAddress": "Gateway Citra Harmoni RKG 32–33", "addressLocality": "Taman, Sidoarjo",
                    "addressRegion": "Jawa Timur", "postalCode": "61257", "addressCountry": "ID"},
        "location": [{"@type": "Place", "name": "Sidoarjo branch office", "address": {"@type": "PostalAddress", "streetAddress": "Gateway Citra Harmoni RKG 32–33", "addressLocality": "Taman, Sidoarjo", "addressRegion": "Jawa Timur", "postalCode": "61257", "addressCountry": "ID"}},
                     {"@type": "Place", "name": "Jakarta branch office — Townhouse PIK", "address": {"@type": "PostalAddress", "streetAddress": "Townhouse PIK", "addressLocality": "Jakarta", "addressCountry": "ID"}}],
        "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "08:00", "closes": "17:00"},
        "areaServed": {"@type": "Country", "name": "Indonesia"},
        "knowsAbout": ["Marine automation", "Ship electrical systems", "Generator systems", "PLC and SCADA", "Industrial machinery repair", "Crane repair", "Hazardous-area electrical equipment", "Noris", "ComAp"],
    }


def breadcrumb(route, name):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
        {"@type": "ListItem", "position": 2, "name": name, "item": BASE + route}]}


def shell(title, description, content, route="", schema=()):
    prefix = "../" if route else "./"
    home = prefix + "index.html"
    brand_links = ''.join(f'<li><a href="{prefix}{key}/">{escape(data["name"])}</a></li>' for key, data in BRANDS.items())
    brand_footer_links = ''.join(f'<a href="{prefix}{key}/">{escape(data["name"])}</a>' for key, data in BRANDS.items())
    service_footer_links = ''.join(f'<a href="{prefix}{key}/">{escape(data["name"])}</a>' for key, data in SERVICES.items())
    contact_topic = (BRANDS.get(route.strip("/")) or SERVICES.get(route.strip("/")) or {}).get("name", "a project")
    def nav(label, target):
        return f'<a href="{home}{target}">{label}</a>'
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <script>document.documentElement.classList.add('js')</script>
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description, quote=True)}">
  <meta name="robots" content="noindex, nofollow">
  <meta name="theme-color" content="#1e2023">
  <link rel="canonical" href="{BASE}{route}">
  <meta property="og:site_name" content="PT Araya Internusa">
  <meta property="og:title" content="{escape(title, quote=True)}">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <meta property="og:type" content="website"><meta property="og:url" content="{BASE}{route}">
  <meta property="og:image" content="{BASE}assets/images/og-araya.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="{prefix}assets/images/favicon.png">
  <link rel="preload" href="{prefix}assets/fonts/space-grotesk.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{prefix}assets/site.css?v={CSS_VERSION}">
  <script src="{prefix}assets/site.js?v={JS_VERSION}" defer></script>
  <script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": [organization(), *schema]}, ensure_ascii=False)}</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="utility"><div class="container utility-inner"><span>Sidoarjo &amp; Jakarta · Indonesia · Mon–Sat 08.00–17.00</span><a href="mailto:{EMAIL}">{EMAIL}</a><a href="tel:+62317877990">+62 (031) 7877990</a></div></div>
  <div class="container navigation">
    <a class="brand" href="{home}" aria-label="PT Araya Internusa home"><img src="{prefix}assets/images/araya-logo-transparent.png" alt="PT Araya Internusa" width="238" height="52"></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="main-navigation"><span>Menu</span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
    <nav class="main-nav" id="main-navigation" aria-label="Main navigation">
      {nav('Home', '')}{nav('About Us', '#about')}{nav('Our Services', '#services')}<details class="brand-menu"><summary>Brand Partners<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></summary><ul class="brand-dropdown">{brand_links}</ul></details>{nav('Our Clients', '#clients')}
      <a class="nav-contact" href="#contact">Contact Us {ARROW}</a>
    </nav>
  </div>
</header>
<main id="main">{content}</main>
<section class="contact" id="contact" aria-labelledby="contact-heading">
  <div class="container contact-intro"><div><p class="eyebrow">GET IN TOUCH</p><h2 id="contact-heading">Let’s find the right solution.</h2><p>Send the equipment model, a nameplate photo and the problem or change you need.</p></div><div class="contact-actions"><a class="button" href="{whatsapp(contact_topic)}">Chat on WhatsApp {ARROW}</a><a class="button button-outline" href="mailto:{EMAIL}">Email our team {ARROW}</a></div></div>
  <div class="container footer-grid">
    <div class="footer-company"><img src="{prefix}assets/images/araya-logo-transparent.png" alt="PT Araya Internusa" width="238" height="52" loading="lazy"><p>Marine, industrial and automation engineering across Indonesia since 2009.</p><a class="text-link light" href="{PRODUCTION}">Visit our current website {ARROW}</a></div>
    <div><h3>Explore Araya</h3><a href="{home}#about">About Us</a>{service_footer_links}{brand_footer_links}<a href="{home}#clients">Our Clients</a></div>
    <div><h3>Branch Offices</h3><p><strong>Sidoarjo</strong><a href="{MAP}">Gateway Citra Harmoni RKG 32–33<br>Taman, Sidoarjo<br>Jawa Timur 61257, Indonesia</a></p><p><strong>Jakarta</strong><a href="{JAKARTA_MAP}">Townhouse PIK<br>Jakarta, Indonesia</a></p><p class="contact-note">Mon–Sat, 08.00–17.00 WIB</p></div>
    <div><h3>Contact Us</h3><a href="mailto:{EMAIL}">{EMAIL}</a><a href="tel:+62317877990">+62 (031) 7877990</a><a href="{whatsapp(contact_topic)}">WhatsApp: +62 813 2639 6262</a><p class="contact-note">Share your system details with our team.</p></div>
  </div>
</section>
<footer class="copyright"><div class="container"><span>© 2026 PT Araya Internusa.</span><span>Design preview · Current website remains live</span></div></footer>
</body></html>'''


def srcset(variants, prefix="./"):
    return ', '.join(f'{prefix}assets/images/{name} {width}w' for name, width in variants)


def home():
    cards = ''.join(f'''<a class="service-card" href="./{key}/"><img src="./assets/images/{s['card_image']}"{f' srcset="{srcset(s["card_variants"])}" sizes="(max-width: 680px) 100vw, 33vw"' if s.get('card_variants') else ''} alt="{escape(s['card_alt'], quote=True)}" width="{s['card_width']}" height="{s['card_height']}" loading="lazy"><div class="service-body"><span class="service-number">0{i}</span><h3>{escape(s['name'])}</h3><p>{escape(s['summary'])}</p><span class="card-link">Explore {escape(s['short'])} services {ARROW}</span></div></a>''' for i, (key, s) in enumerate(SERVICES.items(), 1))
    capabilities = ''.join(f'<a href="./{page}/#{anchor}">{escape(label)}{ARROW}</a>' for label, page, anchor in CAPABILITIES)
    # Not lazy-loaded: logos clipped sideways inside the scrolling strip would never load.
    clients = ''.join(f'<li><img{' class="is-emblem"' if c.get("emblem") else ''} src="./assets/images/{c["logo"]}" alt="{escape(c["name"], quote=True)}" width="{c["width"]}" height="{c["height"]}" fetchpriority="low" decoding="async"></li>' for c in CLIENTS)
    groups = ''.join(f'<div><h3>{escape(title)}</h3><p>{escape(" · ".join(brands))}</p></div>' for title, brands in BRAND_GROUPS)
    return f'''
<section class="hero" aria-labelledby="hero-heading">
  <img class="hero-photo" src="./assets/images/ship-1400.webp" srcset="{srcset((("ship-800.webp", 800), ("ship-1400.webp", 1400)))}" sizes="100vw" alt="PELNI passenger vessel alongside a quay, from Araya’s marine project photographs" width="1400" height="784" fetchpriority="high">
  <div class="hero-shade"></div>
  <div class="container hero-content"><p class="eyebrow">PT ARAYA INTERNUSA</p><h1 id="hero-heading">Marine, industrial &amp;<br>automation engineering<br><span>across Indonesia.</span></h1><p class="hero-description">Supply, repair, modification, upgrade and retrofit for marine equipment, industrial systems and automation.</p><div class="hero-actions"><a class="button" href="{whatsapp()}">Discuss your project {ARROW}</a><a class="button button-outline" href="#services">Our services {ARROW}</a></div></div>
  <div class="hero-index" aria-hidden="true"><span>1,500+</span> / PROJECTS SINCE 2009</div>
</section>
<section class="section about" id="about"><div class="container about-grid">
  <div class="about-media"><img src="./assets/images/team.webp" alt="Araya technicians working together in a vessel’s engine room" width="600" height="600" loading="lazy"><div class="since"><strong>2009</strong><span>Where our story began</span></div></div>
  <div><p class="eyebrow">ABOUT PT ARAYA INTERNUSA</p><h2>Professional experience.<br>International technical backing.</h2><p class="lead">Experienced engineering for marine and industrial systems, supported by standardised working practices and international technical expertise.</p><p>Founded in 2009 by Arif Fatkur Rohman, PT Araya Internusa brings together repair, modification, upgrade and retrofit experience. International technical backing includes HIT (Haven- und Industrietechnik GmbH), Noris Automation and ComAp.</p><p>Araya serves projects across Sumatra, Jawa, Kalimantan, Sulawesi and Papua, with branch offices in Sidoarjo and Jakarta (Townhouse PIK). We also extend the life of obsolete or end-of-sale equipment with practical, reliable solutions.</p><div class="scope-list"><span>Marine</span><span>Industrial</span><span>Automation &amp; electrical</span></div><p class="working-practice"><strong>Standardised working practices</strong><br>Equipment requirements, agreed scope and technical references guide each engineering discussion.</p><p class="leaders"><strong>Leadership:</strong> Arif Fatkur Rohman, S.T., M.MT (Founder &amp; Director) · M Rosul Akbar (Manager) · Anjas Budiarso (Manager)</p></div>
</div></section>
<section class="section section-muted" id="services"><div class="container">
  <div class="section-heading"><div><p class="eyebrow">WHAT WE DO</p><h2>Marine. Industrial.<br>Automation.</h2></div><p>Total solutions for engineering, automation and ship repair needs, delivered with speed, precision and professionalism.</p></div>
  <div class="service-grid">{cards}</div>
  <div class="capabilities"><h3>Common requests</h3><nav class="capability-list" aria-label="Common requests">{capabilities}</nav></div>
</div></section>
<section class="section projects" id="clients"><div class="container">
  <div class="section-heading"><div><p class="eyebrow">OUR CLIENTS</p><h2>Partners who<br>trust Araya.</h2></div><p>Organisations that trust PT Araya Internusa with their engineering and automation work.</p></div>
  <div class="project-reach"><div class="project-total"><strong>1,500+</strong><span>projects across Indonesia</span></div><div class="project-coverage"><h3>Across the archipelago</h3><ul><li>Sumatra</li><li>Jawa</li><li>Kalimantan</li><li>Sulawesi</li><li>Papua</li></ul></div></div>
  <div class="client-marquee"><ul class="client-track" aria-label="Selected clients">{clients}</ul><ul class="client-track" aria-hidden="true">{clients}</ul></div>
  <div class="client-footer"><button class="marquee-toggle" type="button" aria-pressed="false">Pause logos</button></div>
</div></section>
<section class="section" id="brands"><div class="container">
  <div class="section-heading"><div><p class="eyebrow">BRAND PARTNERS &amp; EQUIPMENT</p><h2>Specialist partners.<br>Multi-brand expertise.</h2></div><p>PT Araya Internusa distributes Noris and ComAp in Indonesia, and works on equipment from many other manufacturers.</p></div>
  <div class="brand-grid">
    <article class="brand-panel"><div class="brand-name">NORIS<span>NORIS GROUP GmbH</span></div><h3>Instruments &amp; sensors.<br>Marine automation.</h3><p>{escape(BRANDS['noris']['home_summary'])}</p><a class="text-link" href="./noris/">Explore Noris in Indonesia {ARROW}</a></article>
    <article class="brand-panel"><div class="brand-name">ComAp<span>ENGINE &amp; POWER CONTROL</span></div><h3>Engine control.<br>Power management.<br>Load sharing.</h3><p>{escape(BRANDS['comap']['home_summary'])}</p><a class="text-link" href="./comap/">Explore ComAp in Indonesia {ARROW}</a></article>
  </div>
  <div class="equipment-brands"><h3>We also work on equipment from</h3><div class="equipment-brand-grid">{groups}</div></div>
</div></section>'''


def sector_content(key, s):
    rows = ''.join(f'<article class="scope-detail" id="{anchor}"><span class="portfolio-number">{i:02}</span><h3>{escape(title)}</h3><p>{escape(body)}</p></article>' for i, (anchor, title, body) in enumerate(s['groups'], 1))
    scope_links = ''.join(f'<a href="#{anchor}">{escape(title)}{ARROW}</a>' for anchor, title, _ in s['groups'])
    equipment = ''.join(f'<div><dt>{escape(title)}</dt><dd>{escape(" · ".join(brands))}</dd></div>' for title, brands in s['equipment'])
    featured = ''.join(f'<a href="../{brand}/"><h3>{escape(BRANDS[brand]["name"])}</h3><p>{escape(text)}</p><span class="text-link">Explore {escape(BRANDS[brand]["name"])} details {ARROW}</span></a>' for brand, text in s['featured'])
    checklist = ''.join(f'<li>{escape(item)}</li>' for item in s['enquiry'])
    others = ''.join(f'<a class="text-link" href="../{other}/">{escape(SERVICES[other]["name"])} services {ARROW}</a>' for other in SERVICES if other != key)
    variants = f' srcset="{srcset(s["hero_variants"], "../")}" sizes="(max-width: 680px) 100vw, 45vw"' if s.get('hero_variants') else ''
    return f'''<section class="brand-hero"><div class="container"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="../index.html">Home</a><span aria-hidden="true">/</span><span>{escape(s['name'])}</span></nav><p class="eyebrow">{escape(s['label'].upper())}</p><h1>{s['heading']}</h1><p>{escape(s['intro'])}</p><div class="brand-actions"><a class="button" href="{whatsapp(s['short'] + ' work')}">Discuss your project {ARROW}</a><a class="text-link light" href="#project-scopes">See what we handle {ARROW}</a></div></div></section>
{page_index(s["name"], [("project-scopes", "Service scopes"), ("equipment", "Equipment"), ("contact", "Enquire with Araya")])}
<section class="section"><div class="container brand-overview"><div><p class="eyebrow">PT ARAYA INTERNUSA</p><h2>{s['scope_heading']}</h2><p class="lead">{escape(s['overview'])}</p><p>Our experienced team brings standardised working practices and international technical backing to marine and industrial engineering. Tell us what needs to be repaired, replaced, controlled or monitored. We agree the scope around your equipment, operating requirements and site or vessel conditions.</p></div><figure><img src="../assets/images/{s['hero_image']}"{variants} alt="{escape(s['hero_alt'], quote=True)}" width="{s['hero_width']}" height="{s['hero_height']}" loading="lazy"><figcaption>From Araya’s engineering and service photography.</figcaption></figure></div></section>
<section class="section section-muted" id="project-scopes"><div class="container"><p class="eyebrow">WHAT WE DO</p><h2>Typical {escape(s['short'])} project scopes.</h2><details class="scope-finder"><summary>Find a service scope</summary><nav class="product-finder" aria-label="Service scopes">{scope_links}</nav></details><div class="scope-details">{rows}</div></div></section>
<section class="section" id="equipment"><div class="container"><p class="eyebrow">EQUIPMENT WE WORK ON</p><h2>Multi-brand experience.</h2><p class="portfolio-intro">A selection of the manufacturers and systems our engineers supply or repair.</p><dl class="equipment-list">{equipment}</dl></div></section>
<section class="section section-muted"><div class="container"><p class="eyebrow">FEATURED PARTNER TECHNOLOGY</p><h2>International technology.<br>Professional support.</h2><div class="connection-grid">{featured}</div><div class="equipment-note"><h3>What to send us.</h3><ul class="enquiry-checklist">{checklist}</ul><a class="text-link" href="{whatsapp(s['short'] + ' work')}">Send your project details on WhatsApp {ARROW}</a></div></div></section>
<section class="related container"><div class="related-services">{others}</div><a href="../index.html#services">Back to our services</a></section>'''


def write(route, html):
    folder = PUBLIC / route if route else PUBLIC
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "index.html").write_text(html, encoding="utf-8")


def main():
    routes = [""]
    website = {"@type": "WebSite", "@id": BASE + "#website", "name": "PT Araya Internusa", "url": BASE, "publisher": {"@id": BASE + "#organization"}}
    write("", shell("Marine & Industrial Automation Engineering | Araya Internusa",
                    "Marine, industrial and automation engineering in Indonesia since 2009: ship systems, generators, PLC/SCADA, cranes and machinery. Noris and ComAp partner.",
                    home(), schema=[website]))
    for key, s in SERVICES.items():
        service = {"@type": "Service", "name": s['name'] + " engineering services", "serviceType": s['name'], "provider": {"@id": BASE + "#organization"},
                   "areaServed": {"@type": "Country", "name": "Indonesia"}, "description": s['description']}
        write(key, shell(s['title'], s['description'], sector_content(key, s), key + '/', [breadcrumb(key + '/', s['name']), service]))
        routes.append(key + '/')
    for key, data in BRANDS.items():
        faq = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in data['faqs']]}
        write(key, shell(data['title'], data['description'], brand_content(key, data, ARROW), key + '/', [breadcrumb(key + '/', data['name']), faq]))
        routes.append(key + '/')
    urls = ''.join(f'<url><loc>{BASE}{route}</loc><lastmod>2026-10-09</lastmod></url>' for route in routes)
    (PUBLIC / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n', encoding="utf-8")
    print(f"Built {len(routes)} pages and sitemap.xml.")


if __name__ == "__main__":
    main()
