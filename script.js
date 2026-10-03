/* ============================================================
   SCRIPT.JS — Portfolio interactions
   ============================================================ */

// ── Dark Mode Toggle ───────────────────────────────────────
const themeToggle = document.getElementById('themeToggle');
const html = document.documentElement;

const savedTheme = localStorage.getItem('theme');
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
  html.setAttribute('data-theme', 'dark');
}

themeToggle.addEventListener('click', () => {
  const isDark = html.getAttribute('data-theme') === 'dark';
  if (isDark) {
    html.removeAttribute('data-theme');
    localStorage.setItem('theme', 'light');
  } else {
    html.setAttribute('data-theme', 'dark');
    localStorage.setItem('theme', 'dark');
  }
});


// ── Active Nav Link (per page) ─────────────────────────────
const page = document.body.getAttribute('data-page'); // home | work | about | connect
const activeNav = document.getElementById(`nav-${page}`);
if (activeNav) activeNav.classList.add('active');


// ── Custom Cursor ──────────────────────────────────────────
const cursorDot = document.getElementById('cursorDot');

document.addEventListener('mousemove', (e) => {
  cursorDot.style.left = e.clientX + 'px';
  cursorDot.style.top  = e.clientY + 'px';
});

const hoverTargets = document.querySelectorAll('a, button, .project-item, .link-item, .nav-link');
hoverTargets.forEach((el) => {
  el.addEventListener('mouseenter', () => cursorDot.classList.add('hovered'));
  el.addEventListener('mouseleave', () => cursorDot.classList.remove('hovered'));
});

document.addEventListener('mouseleave', () => { cursorDot.style.opacity = '0'; });
document.addEventListener('mouseenter', () => { cursorDot.style.opacity = '1'; });


// ── Nav Link Click — fade out before navigating ────────────
document.querySelectorAll('.nav-link').forEach((link) => {
  link.addEventListener('click', (e) => {
    const href = link.getAttribute('href');
    // Only intercept links on same origin
    if (!href || href.startsWith('#') || href.startsWith('mailto')) return;
    e.preventDefault();
    const main = document.querySelector('.main');
    if (main) {
      main.style.transition = 'opacity 0.2s ease, transform 0.2s ease';
      main.style.opacity    = '0';
      main.style.transform  = 'translateY(-8px)';
    }
    setTimeout(() => { window.location.href = href; }, 200);
  });
});
