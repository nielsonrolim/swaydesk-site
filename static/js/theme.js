// Tema claro/escuro: a preferência fica só neste navegador (localStorage); sem ela, segue o sistema.
(() => {
  const root = document.documentElement;
  const stored = () => { try { return localStorage.getItem("theme"); } catch (e) { return null; } };
  const media = window.matchMedia("(prefers-color-scheme: dark)");
  const apply = (theme) => {
    root.dataset.theme = theme;
    const button = document.querySelector("[data-theme-toggle]");
    if (button) button.setAttribute("aria-pressed", String(theme === "dark"));
  };
  apply(stored() || (media.matches ? "dark" : "light"));
  document.addEventListener("DOMContentLoaded", () => apply(root.dataset.theme));
  document.addEventListener("click", (event) => {
    if (!event.target.closest("[data-theme-toggle]")) return;
    const next = root.dataset.theme === "dark" ? "light" : "dark";
    try { localStorage.setItem("theme", next); } catch (e) {}
    apply(next);
  });
  media.addEventListener("change", (event) => { if (!stored()) apply(event.matches ? "dark" : "light"); });
})();
