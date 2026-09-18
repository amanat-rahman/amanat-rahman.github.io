(function () {
  var root = document.documentElement;
  var toggle = document.querySelector('.theme-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('theme', next); } catch (e) {}
    });
  }
  // Reassemble obfuscated email addresses into real mailto links.
  document.querySelectorAll('.email[data-u][data-d]').forEach(function (el) {
    var rev = function (x) { return x.split('').reverse().join(''); };
    var addr = rev(el.getAttribute('data-u')) + String.fromCharCode(64) + rev(el.getAttribute('data-d'));
    var a = document.createElement('a');
    a.className = 'email';
    a.href = 'mailto:' + addr;
    a.textContent = addr;
    el.replaceWith(a);
  });

  var navToggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (navToggle && nav) {
    navToggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { nav.classList.remove('is-open'); navToggle.setAttribute('aria-expanded', 'false'); });
    });
  }
})();
