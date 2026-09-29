/* SPACE TO RISE — tienda: catálogo, ficha de producto, carrito y pedido por WhatsApp */
(function () {
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const WA = '573107503359';
  const fmt = (n) => n === 0 ? 'Gratis' : '$ ' + n.toLocaleString('es-CO');
  const CART_KEY = 'str-cart';
  let products = [];
  const cart = { items: JSON.parse(localStorage.getItem(CART_KEY) || '[]') };
  const save = () => localStorage.setItem(CART_KEY, JSON.stringify(cart.items));

  /* ---------- Carrito (existe en todas las páginas) ---------- */
  const drawer = $('.drawer'), scrim = $('.scrim'), countEl = $('.cart-btn .count');
  function renderCart() {
    if (countEl) { const n = cart.items.reduce((a, b) => a + b.qty, 0); countEl.textContent = n; countEl.classList.toggle('show', n > 0); }
    if (!drawer) return;
    const box = $('.drawer__items', drawer), total = $('.drawer__total b', drawer), foot = $('.drawer__foot', drawer);
    if (!cart.items.length) { box.innerHTML = '<div class="drawer__empty">Tu carrito está vacío.<br>Elige un audio y empieza hoy.</div>'; foot.style.display = 'none'; return; }
    foot.style.display = '';
    box.innerHTML = cart.items.map(i => `
      <div class="citem">
        <img src="${i.img}" alt="">
        <div><h5>${i.name}</h5><span class="muted" style="font-size:.85rem">${fmt(i.price)}</span></div>
        <button class="rm" data-rm="${i.id}" aria-label="Quitar">Quitar</button>
      </div>`).join('');
    total.textContent = fmt(cart.items.reduce((a, b) => a + b.price * b.qty, 0));
    $$('[data-rm]', box).forEach(b => b.addEventListener('click', () => { cart.items = cart.items.filter(i => i.id != b.dataset.rm); save(); renderCart(); }));
  }
  function openCart(o = true) { drawer && drawer.classList.toggle('open', o); scrim && scrim.classList.toggle('open', o); document.body.style.overflow = o ? 'hidden' : ''; }
  $('.cart-btn') && $('.cart-btn').addEventListener('click', () => openCart(true));
  $('.drawer__close') && $('.drawer__close').addEventListener('click', () => openCart(false));
  scrim && scrim.addEventListener('click', () => { openCart(false); closeModal(); });
  function add(p) {
    const ex = cart.items.find(i => i.id == p.id);
    if (!ex) cart.items.push({ id: p.id, name: p.name, price: p.price, img: '/assets/img/' + p.img.split('/').pop(), qty: 1 });
    save(); renderCart(); window.strToast && strToast('Añadido al carrito');
  }
  $('.drawer__foot .btn') && $('.drawer__foot .btn').addEventListener('click', () => {
    const lines = cart.items.map(i => `• ${i.name} — ${fmt(i.price)}`).join('\n');
    const total = fmt(cart.items.reduce((a, b) => a + b.price * b.qty, 0));
    const msg = `Hola Andrea 😊 Quiero comprar estos audios de autohipnosis:\n${lines}\n\nTotal: ${total}\n\n¿Me indicas cómo realizar el pago?`;
    open(`https://wa.me/${WA}?text=${encodeURIComponent(msg)}`, '_blank');
  });
  renderCart();

  /* ---------- Catálogo (solo en /shop) ---------- */
  const grid = $('[data-shop]');
  if (!grid) return;
  const CATS = [
    ['Trabaja en ti sana tu cuerpo y mente', 'Trabaja en ti: sana tu cuerpo y tu mente'],
    ['Libérate de todo lo que no quieres', 'Libérate de todo lo que no quieres'],
    ['Supera todos tus miedos para que nada te detenga', 'Supera tus miedos para que nada te detenga'],
    ['Desarrollo profesional', 'Desarrollo profesional'],
    ['Proyectos de vida', 'Proyectos de vida'],
  ];
  fetch('/assets/data/products.json').then(r => r.json()).then(list => {
    products = list.filter(p => !p.cats.includes('Citas Agendadas') && !p.cats.includes('Gif'));
    grid.innerHTML = CATS.map(([key, title]) => {
      const items = products.filter(p => p.cats.includes(key));
      if (!items.length) return '';
      return `<div class="shop-cat rv"><h3>${title}</h3><div class="products">${items.map(card).join('')}</div></div>`;
    }).join('');
    $$('.rv', grid).forEach(el => { requestAnimationFrame(() => el.classList.add('in')); });
    $$('[data-open]', grid).forEach(el => el.addEventListener('click', () => openModal(el.dataset.open)));
    $$('[data-add]', grid).forEach(b => b.addEventListener('click', (e) => { e.stopPropagation(); add(products.find(p => p.id == b.dataset.add)); b.classList.add('added'); b.textContent = 'Añadido'; }));
    // abrir por hash (#p=ID)
    const m = location.hash.match(/p=(\d+)/); if (m) openModal(m[1]);
  });
  function card(p) {
    const img = '/assets/img/' + p.img.split('/').pop();
    return `<article class="product">
      <div class="product__img" data-open="${p.id}"><img src="${img}" alt="${p.name}" loading="lazy"><span class="tag">Audio</span></div>
      <h4 data-open="${p.id}" style="cursor:pointer">${p.name}</h4>
      <div class="p"><b>${fmt(p.price)}</b><button class="add" data-add="${p.id}">Añadir</button></div>
    </article>`;
  }

  /* ---------- Ficha ---------- */
  const modal = $('.modal');
  function openModal(id) {
    const p = products.find(x => x.id == id); if (!p || !modal) return;
    const img = '/assets/img/' + p.img.split('/').pop();
    const desc = p.desc.split('\n').map(s => s.trim()).filter(Boolean).map(s => `<p>${s}</p>`).join('');
    $('.modal__img', modal).innerHTML = `<img src="${img}" alt="">`;
    $('.modal__body', modal).innerHTML = `
      <span class="eyebrow">Audio de autohipnosis · 15–20 min</span>
      <h3>${p.name}</h3>
      <div class="desc">${desc}</div>
      <div class="price">${fmt(p.price)}<small>COP</small></div>
      <div style="display:flex;gap:12px;flex-wrap:wrap"><button class="btn" data-madd="${p.id}">Añadir al carrito</button><a class="btn ghost" target="_blank" rel="noopener" href="https://wa.me/${WA}?text=${encodeURIComponent('Hola Andrea 😊 Quiero comprar el audio "' + p.name + '" (' + fmt(p.price) + '). ¿Me indicas cómo realizar el pago?')}">Comprar por WhatsApp</a></div>
      <p class="muted" style="font-size:.82rem;margin-top:18px">Después del pago recibirás el audio en tu correo, junto con las instrucciones para escucharlo durante 21 días.</p>`;
    $('[data-madd]', modal).addEventListener('click', () => { add(p); closeModal(); openCart(true); });
    modal.classList.add('open'); document.body.style.overflow = 'hidden';
    history.replaceState(null, '', '#p=' + p.id);
  }
  function closeModal() { if (!modal) return; modal.classList.remove('open'); if (!drawer || !drawer.classList.contains('open')) document.body.style.overflow = ''; history.replaceState(null, '', location.pathname); }
  modal && $('.modal__close', modal).addEventListener('click', closeModal);
  modal && modal.addEventListener('click', (e) => { if (e.target === modal) closeModal(); });
  addEventListener('keydown', (e) => { if (e.key === 'Escape') { closeModal(); openCart(false); } });
})();
