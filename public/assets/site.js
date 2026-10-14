// The `js` class is set inline in <head> so the collapsed mobile menu is styled before first paint.
// Service and application links reveal their explanation, including nested deep links.
const revealApplication = (hash) => {
  if (!hash || hash === '#') return;
  let id;
  try { id = decodeURIComponent(hash.slice(1)); } catch (_) { return; }
  const target = document.getElementById(id);
  let disclosure = target?.closest('details');
  while (disclosure) {
    disclosure.open = true;
    disclosure = disclosure.parentElement?.closest('details');
  }
};
revealApplication(window.location.hash);
window.addEventListener('hashchange', () => revealApplication(window.location.hash));
document.addEventListener('click', (event) => {
  const link = event.target.closest('a[href]');
  if (link && link.origin === location.origin &&
      link.pathname.replace(/index\.html$/, '') === location.pathname.replace(/index\.html$/, '')) {
    revealApplication(link.hash);
  }
});
const diagramViewer = document.querySelector('.diagram-viewer');
if (diagramViewer && typeof diagramViewer.showModal === 'function') {
  const image = diagramViewer.querySelector('.diagram-stage img');
  const stage = diagramViewer.querySelector('.diagram-stage');
  const zoomOut = diagramViewer.querySelector('[data-zoom="out"]');
  const zoomIn = diagramViewer.querySelector('[data-zoom="in"]');
  let trigger, zoom = 1, imageWidth = 900, imageHeight = 506;
  const resizeDiagram = () => {
    const fitWidth = Math.min(imageWidth, Math.max(1, stage.clientWidth - 32), Math.max(1, stage.clientHeight - 32) * imageWidth / imageHeight);
    image.style.width = `${fitWidth * zoom}px`;
    diagramViewer.querySelector('.diagram-zoom-status').textContent = `${Math.round(zoom * 100)}%`;
    zoomOut.disabled = zoom <= 1;
    zoomIn.disabled = zoom >= 3;
  };
  document.querySelectorAll('.diagram-trigger').forEach(link => {
    link.addEventListener('click', event => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      trigger = link;
      const thumbnail = link.querySelector('img');
      image.src = link.href;
      image.alt = thumbnail.alt;
      imageWidth = Number(thumbnail.getAttribute('width'));
      imageHeight = Number(thumbnail.getAttribute('height'));
      diagramViewer.querySelector('#diagram-viewer-title').textContent = link.dataset.diagramCaption;
      diagramViewer.querySelector('.diagram-viewer-source').textContent = `Diagram: ${link.dataset.diagramBrand}`;
      zoom = 1;
      diagramViewer.showModal();
      document.body.classList.add('diagram-view-open');
      resizeDiagram();
      stage.scrollTop = stage.scrollLeft = 0;
    });
  });
  diagramViewer.querySelector('.diagram-close').addEventListener('click', () => diagramViewer.close());
  diagramViewer.addEventListener('keydown', event => {
    if (event.key !== 'Tab') return;
    const controls = [...diagramViewer.querySelectorAll('button:not(:disabled), a[href], [tabindex="0"]')];
    const first = controls[0], last = controls[controls.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  });
  diagramViewer.querySelectorAll('[data-zoom]').forEach(button => {
    button.addEventListener('click', () => {
      zoom = button.dataset.zoom === 'reset' ? 1 : Math.max(1, Math.min(3, zoom + (button.dataset.zoom === 'in' ? .5 : -.5)));
      resizeDiagram();
      if (zoom === 1) stage.scrollTop = stage.scrollLeft = 0;
    });
  });
  diagramViewer.addEventListener('click', event => {
    if (event.target !== diagramViewer) return;
    const box = diagramViewer.getBoundingClientRect();
    if (event.clientX < box.left || event.clientX > box.right || event.clientY < box.top || event.clientY > box.bottom) diagramViewer.close();
  });
  diagramViewer.addEventListener('close', () => {
    document.body.classList.remove('diagram-view-open');
    trigger?.focus({preventScroll:true});
  });
  window.addEventListener('resize', () => { if (diagramViewer.open) resizeDiagram(); });
}
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#main-navigation');
const brandMenu = document.querySelector('.brand-menu');
if (brandMenu) {
  document.addEventListener('click', (event) => {
    if (!brandMenu.contains(event.target)) brandMenu.open = false;
  });
  brandMenu.addEventListener('focusout', (event) => {
    if (event.relatedTarget && !brandMenu.contains(event.relatedTarget)) brandMenu.open = false;
  });
}
if (menuButton && navigation) {
  const setMenu = (open) => {
    menuButton.setAttribute('aria-expanded', String(open));
    navigation.dataset.open = String(open);
    menuButton.querySelector('span').textContent = open ? 'Close' : 'Menu';
    if (!open && brandMenu) brandMenu.open = false;
  };
  menuButton.addEventListener('click', () => setMenu(menuButton.getAttribute('aria-expanded') !== 'true'));
  navigation.addEventListener('click', (event) => {
    if (event.target.closest('a')) setMenu(false);
  });
  document.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape') return;
    if (brandMenu && brandMenu.open) {
      brandMenu.open = false;
      brandMenu.querySelector('summary').focus();
    } else if (menuButton.getAttribute('aria-expanded') === 'true') {
      setMenu(false);
      menuButton.focus();
    }
  });
  window.matchMedia('(min-width: 981px)').addEventListener('change', () => setMenu(false));
}
// Keep section navigation available, accounting for the actual shared header height.
const pageIndex = document.querySelector('.page-index');
const siteHeader = document.querySelector('.site-header');
if (pageIndex && siteHeader) {
  const toggle = pageIndex.querySelector('.page-index-toggle');
  const links = [...pageIndex.querySelectorAll('.page-index-links a')];
  const sections = links.map(link => document.getElementById(link.hash.slice(1)));
  const closeIndex = () => {
    pageIndex.dataset.open = 'false';
    toggle.setAttribute('aria-expanded', 'false');
  };
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    pageIndex.dataset.open = String(open);
    toggle.setAttribute('aria-expanded', String(open));
  });
  links.forEach((link, i) => link.addEventListener('click', () => {
    closeIndex();
    // A mobile index link is hidden after selection; move keyboard focus to its destination.
    const target = sections[i];
    if (target) {
      const temporaryTabIndex = !target.hasAttribute('tabindex');
      if (temporaryTabIndex) target.setAttribute('tabindex', '-1');
      target.focus({preventScroll:true});
      if (temporaryTabIndex) target.addEventListener('blur', () => target.removeAttribute('tabindex'), {once:true});
    }
  }));
  pageIndex.addEventListener('keydown', event => {
    if (event.key === 'Escape') { closeIndex(); toggle.focus(); }
  });
  document.addEventListener('click', event => {
    if (!pageIndex.contains(event.target)) closeIndex();
  });
  let pending = false;
  const updateIndex = () => {
    pending = false;
    const headerEdge = Math.max(0, siteHeader.getBoundingClientRect().bottom);
    const compact = window.matchMedia('(max-width:680px)').matches;
    const indexHeight = compact ? toggle.offsetHeight : pageIndex.offsetHeight;
    document.documentElement.style.setProperty('--header-edge', `${headerEdge}px`);
    document.documentElement.style.setProperty('--index-height', `${indexHeight}px`);
    // Anchor offsets may include the utility row before the header compacts on scroll.
    const utilityHeight = siteHeader.querySelector('.utility')?.offsetHeight || 0;
    const threshold = headerEdge + indexHeight + utilityHeight + 40;
    let active = -1;
    sections.forEach((section, i) => {
      if (section && section.getBoundingClientRect().top <= threshold) active = i;
    });
    links.forEach((link, i) => {
      if (i === active) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
    pageIndex.querySelector('.page-index-current').textContent = active >= 0 ? links[active].textContent : 'Explore sections';
  };
  const scheduleIndex = () => {
    if (!pending) { pending = true; requestAnimationFrame(updateIndex); }
  };
  pageIndex.classList.add('is-ready');
  window.addEventListener('scroll', scheduleIndex, {passive:true});
  window.addEventListener('resize', () => { closeIndex(); scheduleIndex(); });
  if ('ResizeObserver' in window) new ResizeObserver(scheduleIndex).observe(siteHeader);
  updateIndex();
}

// Page identity is separate from the changing section selection.
const normalizedPath = value => value.replace(/index\.html$/, '').replace(/\/$/, '');
document.querySelectorAll('.main-nav a').forEach(link => {
  if (!link.hash && normalizedPath(link.pathname) === normalizedPath(location.pathname)) {
    link.setAttribute('aria-current', 'page');
  }
});

// Staggered, once-only entrances for hero copy and engineering content. Content stays visible if scripts or APIs fail.
const motionPreference = window.matchMedia('(prefers-reduced-motion:reduce)');
if ('IntersectionObserver' in window && typeof Element.prototype.animate === 'function') {
  const running = new Set();
  const entranceObserver = new IntersectionObserver(entries => {
    entries.forEach((entry, index) => {
      if (!entry.isIntersecting) return;
      entranceObserver.unobserve(entry.target);
      if (motionPreference.matches) return;
      const animation = entry.target.animate(
        [{opacity:.65, transform:'translateY(20px)'}, {opacity:1, transform:'translateY(0)'}],
        {duration:600, delay:Math.min(index, 3) * 70, easing:'cubic-bezier(.2,.7,.3,1)', fill:'backwards'});
      running.add(animation);
      animation.finished.catch(() => {}).finally(() => running.delete(animation));
    });
  }, {threshold:.12});
  document.querySelectorAll('.hero-content>*,.brand-landing-grid>div>*,.hero-product,.about-media,.section-heading,.service-card,.brand-panel,.brand-profile,.brand-toc-heading,.brand-toc-group,.application-group-intro,.portfolio-row,.application-row,.enquiry-list>li,.connection-grid>a,.contact-intro')
    .forEach(element => entranceObserver.observe(element));
  motionPreference.addEventListener('change', () => {
    if (motionPreference.matches) running.forEach(animation => animation.cancel());
  });
}
