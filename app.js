/*
 * riera.co.uk — Portfolio System chrome
 * Ships on every site in the family. Each page declares data-site on <html>
 * to mark itself as the current entry in the switcher + family footer.
 */

const SITES = [
  { id: 'hub', num: '00', url: 'riera.co.uk',     href: 'https://riera.co.uk/',        title: 'Portfolio',           desc: 'The index. Commercial entry point and the map of everything.',   tag: 'index' },
  { id: 'cv',  num: '01', url: 'cv.riera.co.uk',  href: 'https://cv.riera.co.uk/',     title: 'Curriculum vitae',    desc: 'Platform engineering and infrastructure leadership profile.',    tag: 'career' },
  { id: 'cxo', num: '02', url: 'cxo.riera.co.uk', href: 'https://cxo.riera.co.uk/',    title: 'CTO playbook',        desc: 'The strategy and operating-model lens. Shifts as scope widens.',  tag: 'strategy' },
  { id: 'sme', num: '03', url: 'sme.riera.co.uk', href: 'https://sme.riera.co.uk/',    title: 'SME automation',      desc: 'The inspectable stack behind the paid Automation Audit.',         tag: 'practice' },
  { id: 'cnc', num: '04', url: 'cnc.riera.co.uk', href: 'https://cnc.riera.co.uk/',    title: 'CNCraft',             desc: 'Prompt to CNC-ready output. SVG, DXF, plotter, G-code.',          tag: 'tool' },
  { id: 'i2e', num: '05', url: 'i2e.riera.co.uk', href: 'https://i2e.riera.co.uk/',    title: 'Image to Excalidraw', desc: 'A diagram screenshot becomes an editable Excalidraw scene.',      tag: 'tool' },
  { id: 'llm', num: '06', url: 'llm.riera.co.uk', href: 'https://llm.riera.co.uk/',    title: 'Personal LLM',        desc: 'Domain-specialised, local-first LLM scaffolding with strict scope.', tag: 'lab' },
  { id: 'mac', num: '07', url: 'mac.riera.co.uk', href: 'https://mac.riera.co.uk/',    title: 'Mac rebuild',         desc: 'Opinionated MacBook Pro rebuild notes. Homebrew presets.',        tag: 'notes' },
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

/* ── Audit form (hub only) ── */
function initAuditForm() {
  const form = document.getElementById("audit-form");
  const statusEl = document.getElementById("form-status");
  if (!form || !statusEl) return;

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;

    const button = form.querySelector("button[type='submit']");
    const payload = {
      name: form.name.value.trim(),
      email: form.email.value.trim(),
      company: form.company.value.trim(),
      website: form.website.value.trim(),
      team_size: form.team_size.value,
      current_tools: form.current_tools.value.trim(),
      repetitive_process: form.repetitive_process.value.trim(),
      admin_time_lost: form.admin_time_lost.value,
      desired_outcome: form.desired_outcome.value.trim(),
      contact_consent: form.contact_consent.checked,
      source: "riera.co.uk"
    };

    button.disabled = true;
    button.textContent = "Sending…";
    statusEl.className = "form-status";
    statusEl.textContent = "";

    try {
      const response = await fetch(
        "https://n8n.joanmarcriera.es/webhook/automation-audit-intake",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        }
      );

      if (!response.ok) throw new Error("Request failed: " + response.status);

      form.reset();
      statusEl.classList.add("is-success");
      statusEl.textContent = "Audit request sent. I will follow up after qualification.";
    } catch (err) {
      statusEl.classList.add("is-error");
      statusEl.innerHTML = 'Submission failed. Email <a href="mailto:joanmarcriera@gmail.com">joanmarcriera@gmail.com</a> and mention "Automation Audit".';
    } finally {
      button.disabled = false;
      button.textContent = "Send audit request";
    }
  });
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

  initAuditForm();
});
