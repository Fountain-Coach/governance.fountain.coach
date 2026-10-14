(() => {
  const button = document.querySelector('[data-nav-toggle]');
  const nav = document.querySelector('[data-site-rail], [data-chapter-nav]');
  if (!nav) return;
  const canonical = document.querySelector('link[rel="canonical"]');
  const pagePath = canonical
    ? new URL(canonical.href).pathname
    : window.location.pathname;
  const routeLink = (root, href) => root.querySelector(`a[href="${href}"], a[href$="${href}"]`);

  if (button) {
    button.addEventListener('click', () => {
      const open = nav.dataset.open === 'true';
      nav.dataset.open = String(!open);
      button.setAttribute('aria-expanded', String(!open));
    });
  }

  const semanticEntries = [
    ['Choose by intention', '/chapters/01-reading-index/'],
    ['Scenario development', '/chapters/73-reframe-scenario-development-cycle/'],
    ['Publication architecture', '/chapters/145-one-estate-one-publication-state-estatepublisher-and-reframe-semantic-browser/'],
    ['EstatePublisher authority', '/chapters/134-estatepublisher-publication-authority/'],
    ['MIDI2 instrument plane', '/chapters/150-one-midi2-instrument-plane-multiple-governed-transports/'],
    ['Csound Teatro', '/chapters/151-csound-teatro-speaking-sound-in-space/']
  ];
  if (!nav.querySelector('[data-semantic-rail]')) {
    const semantic = document.createElement('section');
    semantic.className = 'semantic-rail';
    semantic.dataset.semanticRail = '';
    semantic.setAttribute('aria-label', 'Governance conceptual paths');
    const semanticLabel = document.createElement('div');
    semanticLabel.className = 'rail-label';
    semanticLabel.textContent = 'BY INTENTION';
    semantic.append(semanticLabel);
    semanticEntries.forEach(([label, href]) => {
      const link = document.createElement('a');
      link.className = 'semantic-rail-link';
      link.href = href;
      link.textContent = label;
      semantic.append(link);
    });
    const home = nav.querySelector('.rail-home');
    home.insertAdjacentElement('afterend', semantic);

    const links = [...nav.querySelectorAll(':scope > .chapter-link')];
    if (links.length) {
      const details = document.createElement('details');
      details.className = 'chronology-rail';
      const summary = document.createElement('summary');
      summary.textContent = 'Chronological catalogue · ' + links.length + ' chapters';
      details.append(summary, ...links);
      nav.append(details);
    }
  }

  const current = routeLink(nav, pagePath);
  if (current) {
    const chronology = current.closest('.chronology-rail');
    if (chronology) chronology.open = true;
    nav.querySelectorAll('.chapter-link.active').forEach((link) => link.classList.remove('active'));
    nav.querySelectorAll('[aria-current="page"]').forEach((link) => link.removeAttribute('aria-current'));
    current.classList.add('active');
    current.setAttribute('aria-current', 'page');
  }
  const active = nav.querySelector('.chapter-link.active');
  // Marking the active chapter must not reposition the document. The rail is
  // a reading index; its startup state cannot pull the article toward the
  // latest chapter or the footer.

  const pager = document.querySelector('[data-chapter-pager]');
  if (!pager) return;
  const previous = pager.querySelector('[data-chapter-prev]');
  const next = pager.querySelector('[data-chapter-next]');
  document.addEventListener('keydown', (event) => {
    if (window.matchMedia('(max-width: 52rem)').matches) return;
    if (event.defaultPrevented || event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
    const target = event.target;
    if (target instanceof HTMLInputElement || target instanceof HTMLTextAreaElement || target instanceof HTMLSelectElement || target.isContentEditable) return;
    const link = event.key === 'ArrowLeft' ? previous : event.key === 'ArrowRight' ? next : null;
    if (!link) return;
    event.preventDefault();
    window.location.assign(link.href);
  });
})();
