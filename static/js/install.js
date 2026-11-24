// Página Instalar: as seções por distro viram abas, e cada bloco de comando ganha um botão de copiar.
// Sem JS, as seções ficam uma embaixo da outra e o texto dos comandos continua selecionável.
(() => {
  // --- Abas (o padrão de abas da WAI-ARIA: setas, Home e End trocam de aba) ---
  document.querySelectorAll("[data-tabs]").forEach((box) => {
    const panels = Array.from(box.querySelectorAll(":scope > .distro"));
    if (panels.length < 2) return;
    const list = document.createElement("div");
    list.className = "tabs";
    list.setAttribute("role", "tablist");
    if (box.dataset.label) list.setAttribute("aria-label", box.dataset.label);
    const tabs = panels.map((panel) => {
      const title = panel.querySelector(".distro__title");
      const tab = document.createElement("button");
      tab.type = "button";
      tab.className = "tabs__tab";
      tab.id = panel.id + "-tab";
      tab.setAttribute("role", "tab");
      tab.setAttribute("aria-controls", panel.id);
      tab.textContent = title ? title.textContent : panel.id;
      panel.setAttribute("role", "tabpanel");
      panel.setAttribute("aria-labelledby", tab.id);
      panel.tabIndex = 0;
      if (title) title.classList.add("sr-only"); // o nome já está na aba
      list.appendChild(tab);
      return tab;
    });
    box.insertBefore(list, box.firstChild);

    const select = (i, focus) => {
      tabs.forEach((tab, j) => {
        const on = i === j;
        tab.setAttribute("aria-selected", String(on));
        tab.tabIndex = on ? 0 : -1;
        panels[j].hidden = !on;
      });
      if (focus) tabs[i].focus();
    };
    const fromHash = () => {
      let id = "";
      try { id = decodeURIComponent(location.hash.slice(1)); } catch (e) { return -1; } // a malformed % in the hash
      if (!id) return -1;
      return panels.findIndex((panel) => panel.id === id || !!panel.querySelector('[id="' + CSS.escape(id) + '"]'));
    };

    tabs.forEach((tab, i) => {
      tab.addEventListener("click", () => {
        select(i, false);
        history.replaceState(history.state, "", "#" + panels[i].id);
      });
      tab.addEventListener("keydown", (event) => {
        const last = tabs.length - 1;
        const to = { ArrowRight: i === last ? 0 : i + 1, ArrowLeft: i === 0 ? last : i - 1, Home: 0, End: last }[event.key];
        if (to === undefined) return;
        event.preventDefault();
        select(to, true);
        history.replaceState(history.state, "", "#" + panels[to].id);
      });
    });
    window.addEventListener("hashchange", () => { const i = fromHash(); if (i >= 0) select(i, false); });
    const start = fromHash();
    select(start >= 0 ? start : 0, false);
  });

  // --- Copiar ---
  const status = document.createElement("p");
  status.className = "sr-only";
  status.setAttribute("role", "status");
  document.body.appendChild(status);

  const selectText = (node) => {
    const range = document.createRange();
    range.selectNodeContents(node);
    const sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
  };

  document.querySelectorAll(".cmd").forEach((block) => {
    const code = block.querySelector("code");
    if (!code) return;
    const label = block.dataset.copy || "Copy";
    const done = block.dataset.copied || "Copied";
    const button = document.createElement("button");
    button.type = "button";
    button.className = "cmd__copy";
    button.textContent = label;
    let timer = 0;
    button.addEventListener("click", () => {
      const text = code.textContent;
      const ok = () => {
        button.textContent = done;
        status.textContent = done;
        clearTimeout(timer);
        timer = setTimeout(() => { button.textContent = label; status.textContent = ""; }, 2000);
      };
      // Sem a API (http, navegador antigo) ou se ela recusar: o texto fica selecionado, para Ctrl+C
      if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).then(ok, () => selectText(code));
      else selectText(code);
    });
    block.appendChild(button);
  });
})();
