// The 404 page: an address with the language prefix in another case (/pt-BR/install/) goes to the real one
// (/pt-br/install/). Anything else stays on the "not found" page.
(() => {
  const match = location.pathname.match(/^\/(pt-br|en-us)(\/.*)?$/i);
  if (!match || match[1] === match[1].toLowerCase()) return;
  location.replace("/" + match[1].toLowerCase() + (match[2] || "/") + location.search + location.hash);
})();
