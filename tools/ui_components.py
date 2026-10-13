"""Small shared navigation and enquiry components."""
from html import escape
from urllib.parse import quote


def enquiry_url(topic):
    return 'https://wa.me/6281326396262?text=' + quote(
        f'Hello Araya, I would like to discuss {topic}.')


def page_index(label, sections):
    links = ''.join(f'<a href="#{escape(anchor)}">{escape(title)}</a>' for anchor, title in sections)
    return f'''<nav class="page-index" aria-label="{escape(label)} page sections"><div class="container">
    <button type="button" class="page-index-toggle" aria-expanded="false" aria-controls="page-index-links"><span>On this page</span><span class="page-index-current">{escape(label)}</span><span aria-hidden="true">⌄</span></button>
    <div class="page-index-links" id="page-index-links">{links}</div></div></nav>'''
