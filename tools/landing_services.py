"""Engineering services live on the company landing page."""
from html import escape
from ui_components import enquiry_url


def service_details(key, service, arrow, brands):
    rows = ''.join(f'''<article class="scope-detail" id="{key}-{anchor}"><h4>{escape(title)}</h4><p>{escape(body)}</p></article>'''
                   for anchor, title, body in service['groups'])
    equipment = ''.join(f'<div><dt>{escape(title)}</dt><dd>{escape(" · ".join(brands))}</dd></div>'
                        for title, brands in service['equipment'])
    checklist = ''.join(f'<li>{escape(item)}</li>' for item in service['enquiry'])
    featured = ''.join(f'<a href="./{brand}/"><strong>{escape(brands[brand]["name"])}</strong><p>{escape(description)}</p><span class="text-link">Explore {escape(brands[brand]["name"])} {arrow}</span></a>'
                       for brand, description in service['featured'])
    return f'''<details class="service-detail" id="{key}-services">
    <summary><span><strong>{escape(service['name'])} services</strong><span>{escape(service['intro'])}</span></span><span class="application-expand" aria-hidden="true">+</span></summary>
    <div class="service-detail-body"><p class="service-overview">{escape(service['overview'])}</p><div class="scope-details">{rows}</div>
    <details class="service-equipment" id="{key}-equipment"><summary>Equipment we work on</summary><dl class="equipment-list">{equipment}</dl></details>
    <div class="service-brand-links">{featured}</div>
    <div class="equipment-note"><h4>What to send us</h4><ul class="enquiry-checklist">{checklist}</ul><a class="button" href="{enquiry_url(service['short'] + ' work')}">Discuss {escape(service['short'])} work {arrow}</a></div>
    </div></details>'''


def legacy_targets(key, service):
    return {'': f'{key}-services', 'project-scopes': f'{key}-services',
            'equipment': f'{key}-equipment', 'contact': 'contact',
            **{anchor: f'{key}-{anchor}' for anchor, _, _ in service['groups']}}
