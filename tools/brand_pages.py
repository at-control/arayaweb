"""Shared layout for Araya's dedicated manufacturer guides."""
from html import escape
from ui_components import page_index, enquiry_url


def portfolio_image(product, brand):
    """Optional local manufacturer image; never imply an Araya installation."""
    if 'image' not in product:
        return ''
    picture = product['image']
    return f'''<figure class="portfolio-picture"><img src="../assets/images/{escape(picture['file'], quote=True)}" alt="{escape(picture['alt'], quote=True)}" width="{picture['width']}" height="{picture['height']}" loading="lazy" decoding="async"><figcaption><a href="{escape(product['source'], quote=True)}">{escape(picture['caption'])} · Image: {escape(brand)}</a></figcaption></figure>'''


def diagram_figure(diagram, source=None, brand='ComAp'):
    credit = source or diagram['source']
    return f'''<figure class="application-diagram"><a class="diagram-trigger" href="../assets/images/{diagram['file']}" target="_blank" rel="noopener" aria-label="Enlarge diagram: {escape(diagram['caption'], quote=True)}" data-diagram-caption="{escape(diagram['caption'], quote=True)}" data-diagram-brand="{escape(brand, quote=True)}"><img src="../assets/images/{diagram['file']}" alt="{escape(diagram['alt'], quote=True)}" width="{diagram['width']}" height="{diagram['height']}" loading="lazy" decoding="async"><span class="diagram-enlarge" aria-hidden="true">Enlarge diagram ↗</span></a><figcaption><a href="{escape(credit, quote=True)}">{escape(diagram['caption'])} · Diagram: {escape(brand)}</a></figcaption></figure>'''


def portfolio_system(product, brand):
    if 'diagram' not in product:
        return ''
    flow = ''.join(f'<li>{escape(step)}</li>' for step in product.get('flow', []))
    return f'''<div class="portfolio-system"><h4>How the system connects</h4><ol class="application-flow" aria-label="Conceptual system flow">{flow}</ol>{diagram_figure(product['diagram'], product['source'], brand)}<p class="system-note">{escape(product['diagram_note'])}</p></div>'''


def diagram_viewer(source='https://www.comap-control.com/application-areas/'):
    return f'''<dialog class="diagram-viewer" aria-labelledby="diagram-viewer-title"><div class="diagram-toolbar"><h2 id="diagram-viewer-title">Application diagram</h2><button type="button" class="diagram-close" autofocus aria-label="Close diagram">Close ×</button><div class="diagram-zoom" role="group" aria-label="Diagram zoom"><button type="button" data-zoom="out" aria-label="Zoom out">−</button><button type="button" data-zoom="reset">Fit</button><button type="button" data-zoom="in" aria-label="Zoom in">+</button><span class="diagram-zoom-status" aria-live="polite">100%</span></div></div><div class="diagram-stage" tabindex="0" aria-label="Diagram image. Scroll to explore when enlarged."><img alt="Enlarged manufacturer system diagram"></div><div class="diagram-viewer-footer"><a class="diagram-viewer-source" href="{escape(source, quote=True)}" target="_blank" rel="noopener">Manufacturer source</a><span>Zoom in, then scroll to explore. Escape closes this view.</span></div></dialog>'''


def application_guide(groups, arrow):
    navigation = ''.join(f'<a href="#{group["id"]}"><span>0{i}</span>{escape(group["title"])}{arrow}</a>' for i, group in enumerate(groups, 1))
    rendered = []
    for i, group in enumerate(groups, 1):
        diagram = group['diagram']
        flow = ''.join(f'<li>{escape(step)}</li>' for step in group['flow'])
        items = []
        for item_index, item in enumerate(group['items']):
            fields = ''.join(f'<div><dt>{label}</dt><dd>{escape(item[key])}</dd></div>' for label, key in [('Typical system', 'system'), ('What ComAp controls', 'control'), ('Example product families', 'families'), ('What to review with Araya', 'review')])
            related = ''.join(f'<a class="text-link" href="#{target}">{escape(label)}{arrow}</a>' for label, target in item['related'])
            diagrams = ''.join(diagram_figure(picture, item['source']) for picture in item.get('diagrams', []))
            gallery = f'<div class="application-diagrams">{diagrams}</div>' if diagrams else ''
            items.append(f'''<details class="application-detail" id="{item['id']}"><summary><span><strong>{escape(item['title'])}</strong><span>{escape(item['summary'])}</span></span><span class="application-expand" aria-hidden="true">+</span></summary><div class="application-body">{gallery}<dl>{fields}</dl><div class="application-links"><a class="button context-enquiry" href="{enquiry_url("ComAp " + item["title"])}">Discuss this application {arrow}</a>{related}<a class="application-source" href="{escape(item['source'], quote=True)}">ComAp application reference {arrow}</a><a class="application-source" href="#applications">Back to applications ↑</a></div></div></details>''')
        rendered.append(f'''<section class="application-group" id="{group['id']}" aria-labelledby="{group['id']}-heading"><div class="application-group-intro"><div><p class="eyebrow">APPLICATION GROUP 0{i}</p><h3 id="{group['id']}-heading">{escape(group['title'])}</h3><p>{escape(group['intro'])}</p><ol class="application-flow" aria-label="Conceptual system flow">{flow}</ol></div>{diagram_figure(diagram)}</div><div class="application-details">{''.join(items)}</div></section>''')
    return f'''<section class="section application-guide" id="applications"><div class="container"><p class="eyebrow">COMAP APPLICATIONS</p><h2>The application defines<br>the control system.</h2><p class="lead application-guide-intro">Start with what your engine, vessel or power system needs to do. Then select the controller family, interfaces and operating logic.</p><p class="application-scope">Explore the manufacturer application examples below. Araya confirms the controller, configuration and scope for your project.</p><nav class="application-index" aria-label="ComAp application groups">{navigation}</nav><p class="application-hint">Select an application to see its system, control functions and diagrams. Select a diagram to enlarge it.</p>{''.join(rendered)}</div></section>{diagram_viewer()}'''


def brand_content(key, data, arrow):
    name = escape(data['name'])
    sections = [('about-brand', 'About the brand'), ('portfolio', 'Products & systems'),
                ('applications', 'Applications'), ('araya-support', 'Enquire with Araya'), ('brand-faq', 'FAQs')]
    has_guide = bool(data.get('application_groups'))
    if has_guide:
        sections[1], sections[2] = sections[2], sections[1]
    facts = ''.join(f'<div><dt>{escape(label)}</dt><dd>{escape(value)}</dd></div>' for label, value in data['facts'])
    finder = ''.join(f'<a href="#{product["id"]}"><span>{i:02}</span>{escape(product["short"])}{arrow}</a>' for i, product in enumerate(data['products'], 1))
    portfolio = ''.join(f'''<article class="portfolio-row" id="{product['id']}">
      <div><span class="portfolio-number">{i:02}</span><h3>{escape(product['title'])}</h3><p class="family-name">{escape(product['family'])}</p>{portfolio_image(product, data['name'])}</div>
      <div><p>{escape(product['body'])}</p><dl><div><dt>Applications</dt><dd>{escape(product['application'])}</dd></div><div><dt>Selection details</dt><dd>{escape(product['selection'])}</dd></div></dl><div class="product-actions"><a class="button context-enquiry" href="{enquiry_url(data["name"] + " " + product["title"])}">Enquire about this product {arrow}</a><a class="text-link" href="{escape(product['source'], quote=True)}">Manufacturer details &amp; documents {arrow}</a><a class="application-source" href="#portfolio">Back to products ↑</a></div></div>
{portfolio_system(product, data['name'])}
    </article>''' for i, product in enumerate(data['products'], 1))
    applications = ''.join(f'''<article class="application-row"><span>{i:02}</span><h3>{escape(title)}</h3><div><p>{escape(body)}</p><a class="text-link" href="#{anchor}">{escape(label)} {arrow}</a></div></article>''' for i, (title, body, anchor, label) in enumerate(data['applications'], 1))
    application_section = application_guide(data['application_groups'], arrow) if has_guide else f'''<section class="section" id="applications"><div class="container"><p class="eyebrow">START WITH YOUR APPLICATION</p><h2>What does your system need?</h2><div class="application-list">{applications}</div></div></section>'''
    primary_action = f'<a class="button" href="#applications">Explore {name} applications {arrow}</a><a class="text-link light" href="#portfolio">View products {arrow}</a>' if has_guide else f'<a class="button" href="#portfolio">Explore {name} products {arrow}</a>'
    enquiry = ''.join(f'<li><h3>{escape(title)}</h3><p>{escape(body)}</p></li>' for title, body in data['enquiry'])
    faqs = ''.join(f'<details><summary><span>{escape(question)}</span><span class="application-expand" aria-hidden="true">+</span></summary><p>{escape(answer)}</p></details>' for question, answer in data['faqs'])
    return f'''<section class="brand-hero brand-landing"><div class="container">
      <nav class="breadcrumb" aria-label="Breadcrumb"><a href="../index.html">Home</a><span aria-hidden="true">/</span><span>{name}</span></nav>
      <div class="brand-landing-grid"><div><p class="eyebrow">{escape(data['label'])}</p><h1>{data['heading']}</h1><p class="brand-intro">{escape(data['intro'])}</p><div class="brand-actions">{primary_action}<a class="text-link light" href="#araya-support">Talk to Araya {arrow}</a></div></div>
      <figure class="product-figure hero-product"><img src="../assets/images/{data['image']}" alt="{escape(data['alt'], quote=True)}" width="{data['image_width']}" height="{data['image_height']}" fetchpriority="high"><figcaption><a href="{escape(data['image_source'], quote=True)}">{escape(data['image_caption'])}</a></figcaption></figure></div>
    </div></section>
    {page_index(data["name"], sections)}
    <section class="section" id="about-brand"><div class="container"><div class="brand-profile"><div><p class="eyebrow">ABOUT {name.upper()}</p><h2>{data['profile_heading']}</h2><a class="text-link" href="{escape(data['profile_source'], quote=True)}">Manufacturer background {arrow}</a></div><div><p class="lead">{escape(data['profile'])}</p><p>{escape(data['local'])}</p><p>Professional engineering experience, certification and international technical backing support your project discussion with Araya.</p></div></div><dl class="brand-facts">{facts}</dl></div></section>
{application_section if has_guide else ''}
    <section class="section section-muted" id="portfolio"><div class="container"><p class="eyebrow">{name.upper()} PRODUCTS &amp; SYSTEMS</p><h2>{data['portfolio_heading']}</h2><p class="portfolio-intro">Find the product family for your application, then share your requirements. Araya confirms the right model and configuration for your project.</p><nav class="product-finder" aria-label="{name} product families">{finder}</nav><div class="portfolio-list">{portfolio}</div></div></section>
{'' if has_guide else application_section}
{diagram_viewer(next(product['source'] for product in data['products'] if 'diagram' in product)) if not has_guide and any('diagram' in product for product in data['products']) else ''}
    <section class="section brand-enquiry" id="araya-support"><div class="container"><div class="section-heading"><div><p class="eyebrow">{name.upper()} IN INDONESIA</p><h2>Share your equipment details.<br>Let’s define the scope.</h2></div><p>Discuss {name} supply, replacement, and integration requirements with PT Araya Internusa. A clear equipment brief helps us review the work around your installation.</p></div><ol class="enquiry-list">{enquiry}</ol><div class="brand-actions"><a class="button" href="{enquiry_url(data["name"] + " products and systems")}">Discuss {name} on WhatsApp {arrow}</a><a class="text-link" href="mailto:cs@arayainternusa.com">Email your project details {arrow}</a></div></div></section>
    <section class="section" id="brand-faq"><div class="container brand-faq"><div><p class="eyebrow">COMMON QUESTIONS</p><h2>Before you<br>choose {name}.</h2></div><div class="faq-list">{faqs}</div></div></section>
    <section class="section section-muted project-connections"><div class="container"><p class="eyebrow">FROM PRODUCT TO PROJECT</p><h2>Connect the technology<br>to the work you need.</h2><div class="connection-grid"><a href="../marine/"><h3>Marine project scopes</h3><p>{escape(data['marine_connection'])}</p><span class="text-link">Explore marine work {arrow}</span></a><a href="../industrial/"><h3>Industrial project scopes</h3><p>{escape(data['industrial_connection'])}</p><span class="text-link">Explore industrial work {arrow}</span></a></div></div></section>
    <section class="related container"><a class="text-link" href="../{data['other']}/">{escape(data['other_label'])} {arrow}</a><a href="../index.html#brands">Back to our solutions</a></section>'''
