// A página raiz: português para quem usa pt*, espanhol para es*, inglês para os demais. Sem JS, o meta refresh leva ao português.
(() => {
  if (location.pathname !== "/") return; // os outros redirecionamentos (/pt-BR/, /en-US/) seguem o meta refresh
  const langs = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || ""];
  const first = langs[0] || "";
  const target = /^pt\b/i.test(first) ? "/pt-br/" : /^es\b/i.test(first) ? "/es/" : "/en-us/";
  location.replace(target);
})();
