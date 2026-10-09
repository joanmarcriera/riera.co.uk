/*
 * riera.co.uk, Portfolio System chrome
 * Ships on every site in the family. Each page declares data-site on <html>
 * to mark itself as the current entry in the switcher + family footer.
 */

const SITES = [
  { id: 'hub', num: '00', url: 'riera.co.uk',     href: 'https://riera.co.uk/',        title: 'Profile',             desc: 'HPC and AI infrastructure architect: profile, CV and contact.',  tag: 'index' },
  { id: 'cv',  num: '01', url: 'cv.riera.co.uk',  href: 'https://cv.riera.co.uk/',     title: 'Curriculum vitae',    desc: 'HPC and AI infrastructure architect: CV download and contact.',  tag: 'career' },
  { id: 'blog', num: '02', url: 'blog.riera.co.uk', href: 'https://blog.riera.co.uk/',  title: 'Lab notes',           desc: 'Hands-on HPC, storage, Linux and self-hosted AI infrastructure.', tag: 'notes' },
];

const currentSite = document.documentElement.dataset.site || 'hub';

/* ── Directory (hub only) ── */
function buildDirectory() {
  const root = document.getElementById('directory');
  if (!root) return;
  root.innerHTML = SITES.map(s => `
    <a class="dir-row" href="${s.href}">
      <span class="dir-num">${s.num}</span>
      <span class="dir-url">${s.url}</span>
      <div class="dir-title-row">
        <div class="dir-title">${s.title}</div>
        <div class="dir-desc">${s.desc}</div>
      </div>
      <span class="dir-tag">${s.tag}</span>
      <span class="dir-arrow">→</span>
    </a>
  `).join('');
}

/* ── Footer family grid ── */
function buildFooter() {
  const root = document.getElementById('foot-grid');
  if (!root) return;
  root.innerHTML = SITES.map(s => `
    <a class="foot-link ${s.id === currentSite ? 'is-current' : ''}" href="${s.href}">
      <span class="u">${s.url}</span>
      <span class="d">${s.tag}</span>
    </a>
  `).join('');
}

/* ── Switcher (⌘K) ── */
function buildSwitcher() {
  const root = document.getElementById('switcher-list');
  if (!root) return;
  root.innerHTML = SITES.map(s => `
    <a class="switch-row ${s.id === currentSite ? 'is-current' : ''}" href="${s.href}">
      <span class="row-num">${s.num}</span>
      <div class="row-body">
        <div class="row-title">${s.title}</div>
        <div class="row-desc">${s.desc}</div>
      </div>
      <span class="row-url">${s.url}</span>
    </a>
  `).join('');
}

function openSwitcher() {
  const el = document.getElementById('switcher');
  if (!el) return;
  el.classList.add('open');
  buildSwitcher();
  const firstRow = el.querySelector('.switch-row');
  if (firstRow) firstRow.focus({ preventScroll: true });
}
function closeSwitcher() {
  const el = document.getElementById('switcher');
  if (el) el.classList.remove('open');
}

/* ── Boot ── */
document.addEventListener('DOMContentLoaded', () => {
  buildDirectory();
  buildFooter();

  const openBtn = document.getElementById('switcher-open');
  if (openBtn) openBtn.addEventListener('click', openSwitcher);
  const closeBtn = document.getElementById('switcher-close');
  if (closeBtn) closeBtn.addEventListener('click', closeSwitcher);
  const switcherEl = document.getElementById('switcher');
  if (switcherEl) {
    switcherEl.addEventListener('click', (e) => {
      if (e.target.id === 'switcher') closeSwitcher();
    });
  }

  window.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      openSwitcher();
    }
    if (e.key === 'Escape') closeSwitcher();
  });
});
