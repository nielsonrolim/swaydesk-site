// O carrossel: os links a[data-lightbox] da página abrem a imagem num <dialog> modal (o foco fica nele e o
// resto da página fica inerte), com legenda, contador, setas, teclado e deslizar. A imagem aberta vai para o
// endereço (#shot-3), e o "voltar" do navegador fecha. Sem JS, os links abrem a imagem, como antes.
(() => {
  const dialog = document.querySelector("dialog.lightbox");
  const links = Array.from(document.querySelectorAll("a[data-lightbox]"));
  if (!dialog || !links.length || typeof dialog.showModal !== "function") return;
  dialog.hidden = false;

  const img = dialog.querySelector(".lightbox__img");
  const count = dialog.querySelector(".lightbox__count");
  const caption = dialog.querySelector(".lightbox__caption");
  const prev = dialog.querySelector("[data-lb=prev]");
  const next = dialog.querySelector("[data-lb=next]");
  const total = links.length;
  const many = total > 1;
  prev.hidden = next.hidden = !many;

  let current = -1;   // a imagem aberta, ou -1
  let pushed = false; // abrimos com pushState: fechar volta no histórico
  let opener = null;  // o link que abriu, para devolver o foco

  const captionOf = (link) => {
    const fig = link.closest("figure");
    const text = fig && fig.querySelector("figcaption");
    const thumb = link.querySelector("img");
    return ((text && text.textContent) || (thumb && thumb.alt) || "").trim();
  };
  const hashOf = (i) => "#shot-" + (i + 1);
  const indexOfHash = () => {
    const m = /^#shot-(\d+)$/.exec(location.hash);
    const i = m ? parseInt(m[1], 10) - 1 : -1;
    return i >= 0 && i < total ? i : -1;
  };
  const preload = (i) => { const pre = new Image(); pre.src = links[(i + total) % total].href; };

  const show = (i) => {
    current = (i + total) % total;
    const link = links[current];
    const text = captionOf(link);
    img.classList.remove("is-new");
    void img.offsetWidth; // reinicia a animação (só com prefers-reduced-motion: no-preference)
    img.classList.add("is-new");
    img.src = link.href;
    img.alt = text;
    caption.textContent = text;
    count.textContent = (current + 1) + " / " + total;
    if (many) { preload(current + 1); preload(current - 1); }
  };

  const open = (i, push) => {
    if (!dialog.open) {
      opener = links[i];
      document.documentElement.classList.add("lb-open");
      dialog.showModal();
    }
    show(i);
    if (push) { history.pushState({ lightbox: true }, "", hashOf(current)); pushed = true; }
    else if (location.hash !== hashOf(current)) history.replaceState(history.state, "", hashOf(current));
  };

  // Só fecha a janela; o endereço fica por conta de quem chamou
  const finish = () => {
    if (dialog.open) dialog.close();
    document.documentElement.classList.remove("lb-open");
    current = -1;
    pushed = false;
    img.removeAttribute("src");
    const back = opener || null;
    opener = null;
    if (back) back.focus();
  };

  const close = () => {
    if (current < 0) return finish();
    if (pushed) history.back(); // o popstate chama finish
    else { history.replaceState(history.state, "", location.pathname + location.search); finish(); }
  };

  const go = (step) => { if (many && current >= 0) open(current + step, false); };

  links.forEach((link, i) => link.addEventListener("click", (event) => {
    if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    open(i, true);
  }));

  dialog.addEventListener("click", (event) => {
    const action = event.target.closest("[data-lb]");
    if (action) {
      const what = action.dataset.lb;
      if (what === "close") close(); else go(what === "next" ? 1 : -1);
    } else if (event.target !== img && !event.target.closest(".lightbox__bar")) {
      close(); // clique fora da imagem (a legenda não fecha, para dar para selecionar o texto)
    }
  });
  dialog.addEventListener("cancel", (event) => { event.preventDefault(); close(); }); // Esc
  dialog.addEventListener("keydown", (event) => {
    if (event.key === "ArrowRight") { event.preventDefault(); go(1); }
    else if (event.key === "ArrowLeft") { event.preventDefault(); go(-1); }
  });

  // Deslizar no celular: um gesto mais horizontal que vertical, de pelo menos 50 px
  let startX = 0, startY = 0, tracking = false;
  dialog.addEventListener("touchstart", (event) => {
    if (event.touches.length !== 1) { tracking = false; return; }
    tracking = true;
    startX = event.touches[0].clientX;
    startY = event.touches[0].clientY;
  }, { passive: true });
  dialog.addEventListener("touchend", (event) => {
    if (!tracking) return;
    tracking = false;
    const dx = event.changedTouches[0].clientX - startX;
    const dy = event.changedTouches[0].clientY - startY;
    if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.5) go(dx < 0 ? 1 : -1);
  }, { passive: true });

  window.addEventListener("popstate", () => {
    const i = indexOfHash();
    if (i >= 0) { open(i, false); pushed = !!(history.state && history.state.lightbox); }
    else if (dialog.open) finish();
  });

  // Um link com #shot-N abre direto
  const initial = indexOfHash();
  if (initial >= 0) open(initial, false);
})();
