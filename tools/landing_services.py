"""Engineering services live on the company landing page."""
from html import escape
from ui_components import disclosure_summary, srcset


def service_details(key, service):
    rows = ''.join(f'''<article class="scope-detail" id="{key}-{anchor}"><h4>{escape(title)}</h4><p>{escape(body)}</p></article>'''
                   for anchor, title, body in service['groups'])
    return f'''<details class="service-detail" id="{key}-services">
    {disclosure_summary(service['name'] + ' services', service['intro'])}
    <div class="service-detail-body" id="{key}-equipment"><figure class="service-photo"><img src="./assets/images/{service['card_image']}"{f' srcset="{srcset(service["card_variants"])}" sizes="(max-width: 680px) 100vw, 240px"' if service.get('card_variants') else ''} alt="{escape(service['card_alt'], quote=True)}" width="{service['card_width']}" height="{service['card_height']}" loading="eager" fetchpriority="low" decoding="async"></figure><div class="scope-details">{rows}</div>
    </div></details>'''


def legacy_targets(key, service):
    return {'': f'{key}-services', 'project-scopes': f'{key}-services',
            'equipment': f'{key}-equipment', 'contact': 'contact',
            **{anchor: f'{key}-{anchor}' for anchor, _, _ in service['groups']}}
