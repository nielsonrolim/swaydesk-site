// A página raiz: português para quem usa pt*, inglês para os demais. Sem JS, o meta refresh leva ao português.
(() => {
  if (location.pathname !== "/") return; // os outros redirecionamentos (/pt-BR/, /en-US/) seguem o meta refresh
  const langs = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || ""];
  const target = /^pt\b/i.test(langs[0] || "") ? "/pt-br/" : "/en-us/";
  location.replace(target);
})();
