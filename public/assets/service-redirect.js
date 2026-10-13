/* Retain old bookmarks while service content lives on the main landing page. */
(() => {
  const data = document.querySelector('#legacy-service-targets');
  if (!data) return;
  const targets = JSON.parse(data.textContent);
  let fragment = '';
  try { fragment = decodeURIComponent(location.hash.slice(1)); } catch (_) { /* Use the service overview. */ }
  const target = Object.hasOwn(targets, fragment) ? targets[fragment] : targets[''];
  location.replace(new URL(`../index.html#${encodeURIComponent(target)}`, location.href).href);
})();
