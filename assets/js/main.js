/* SPACE TO RISE — comportamiento común
   Loader (una respiración), header, revelados, video con scroll,
   acordeón, transición de página, WhatsApp. */
(function () {
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Loader ---------- */
  const loader = $('.loader');
  const bar = $('.loader__bar i');
  document.body.classList.add('is-loading');
  const start = performance.now();
  const MIN = reduce ? 0 : 2400; // deja que se vea al menos una respiración
  function finishLoader() {
    const wait = Math.max(0, MIN - (performance.now() - start));
    setTimeout(() => {
      if (bar) bar.style.transform = 'scaleX(1)';
      setTimeout(() => {
        loader && loader.classList.add('done');
        document.body.classList.remove('is-loading');
        $('.hero') && $('.hero').classList.add('is-in');
        sessionStorage.setItem('str-visited', '1');
      }, 300);
    }, wait);
  }
  // La segunda vez que se entra en la sesión, el loader es breve.
  if (sessionStorage.getItem('str-visited')) { /* MIN se reduce */ }
  if (bar) requestAnimationFrame(() => (bar.style.transform = 'scaleX(.55)'));
  const heroMedia = $('.hero__media img, .hero__media video');
  if (heroMedia && heroMedia.tagName === 'IMG' && !heroMedia.complete) {
    heroMedia.addEventListener('load', finishLoader, { once: true });
    heroMedia.addEventListener('error', finishLoader, { once: true });
  } else if (document.readyState === 'complete') finishLoader();
  else window.addEventListener('load', finishLoader, { once: true });

  /* ---------- Header ---------- */
  const header = $('.header');
  const onScroll = () => header && header.classList.toggle('scrolled', scrollY > 24);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();
  const burger = $('.burger'), nav = $('.nav');
  burger && burger.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    burger.classList.toggle('open', open);
    burger.setAttribute('aria-expanded', open);
    document.body.style.overflow = open ? 'hidden' : '';
  });
  // marcar página actual
  const here = location.pathname.replace(/\/+$/, '') || '/';
  $$('.nav a').forEach(a => {
    const p = a.getAttribute('href').replace(/\/+$/, '') || '/';
    if (p === here) a.setAttribute('aria-current', 'page');
  });

  /* ---------- Revelados (una sola vez) ---------- */
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.18, rootMargin: '0px 0px -6% 0px' });
  $$('.rv, .frame, .card-img').forEach(el => io.observe(el));

  /* ---------- Hero: palabras que respiran ---------- */
  $$('.breathe-in').forEach(el => {
    const words = el.textContent.trim().split(/\s+/);
    el.innerHTML = words.map((w, i) => `<span class="w" style="transition-delay:${0.25 + i * 0.09}s">${w}</span>`).join(' ');
  });

  /* ---------- Video con scroll (escala hasta llenar) ---------- */
  const stage = $('.video-stage');
  if (stage) {
    const fr = $('.frame-v', stage), vid = $('video', stage), play = $('.play', stage), cap = $('.caption', stage);
    const tick = () => {
      const r = stage.getBoundingClientRect();
      const total = stage.offsetHeight - innerHeight;
      const p = Math.min(1, Math.max(0, -r.top / total));
      const s = 0.62 + 0.38 * Math.min(1, p / 0.6);
      fr.style.setProperty('--s', s.toFixed(3));
      fr.style.setProperty('--r', (28 - 28 * Math.min(1, p / 0.6)).toFixed(1) + 'px');
      if (cap) cap.style.opacity = p > 0.5 ? 0 : 1;
      // autoplay silencioso cuando está casi lleno
      if (p > 0.45 && vid.paused && !stage.dataset.user) { vid.muted = true; vid.play().catch(() => {}); }
      if (p < 0.1 && !vid.paused && !stage.dataset.user) vid.pause();
    };
    addEventListener('scroll', tick, { passive: true }); tick();
    play && play.addEventListener('click', () => {
      stage.dataset.user = '1'; vid.muted = false; vid.controls = true; vid.currentTime = 0; vid.play();
      stage.classList.add('playing');
    });
  }

  /* ---------- Acordeón ---------- */
  $$('.acc__item').forEach(item => {
    $('.acc__q', item).addEventListener('click', () => {
      const open = item.classList.contains('open');
      $$('.acc__item.open', item.parentElement).forEach(i => { i.classList.remove('open'); $('.acc__q', i).setAttribute('aria-expanded', 'false'); });
      if (!open) { item.classList.add('open'); $('.acc__q', item).setAttribute('aria-expanded', 'true'); }
    });
  });

  /* ---------- Transición entre páginas ---------- */
  const veil = $('.veil-page');
  if (veil && !reduce) {
    $$('a[href]').forEach(a => {
      const href = a.getAttribute('href');
      if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('mailto') || href.startsWith('tel') || a.target === '_blank' || a.hasAttribute('download')) return;
      a.addEventListener('click', (e) => {
        if (e.metaKey || e.ctrlKey) return;
        e.preventDefault();
        veil.classList.add('on');
        setTimeout(() => (location.href = href), 650);
      });
    });
    addEventListener('pageshow', (e) => { if (e.persisted) veil.classList.remove('on'); });
  }

  /* ---------- WhatsApp: se asoma una vez ---------- */
  const wa = $('.wa');
  if (wa) setTimeout(() => { wa.classList.add('peek'); setTimeout(() => wa.classList.remove('peek'), 3200); }, 5200);

  /* ---------- Toast ---------- */
  window.strToast = (msg) => {
    let t = $('.toast'); if (!t) { t = document.createElement('div'); t.className = 'toast'; document.body.appendChild(t); }
    t.textContent = msg; t.classList.add('show'); clearTimeout(t._h); t._h = setTimeout(() => t.classList.remove('show'), 2400);
  };
})();
