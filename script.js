(function () {
  var header = document.querySelector(".header-bar");
  var button = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".site-nav");
  var links = Array.prototype.slice.call(nav.querySelectorAll('a[href^="#"]'));
  var sections = links
    .map(function (link) {
      return document.querySelector(link.getAttribute("href"));
    })
    .filter(Boolean);
  var mobile = window.matchMedia("(max-width: 719px)");

  function closeMenu(focusButton) {
    header.classList.remove("is-open");
    button.setAttribute("aria-expanded", "false");
    if (focusButton) button.focus();
  }

  function openMenu() {
    header.classList.add("is-open");
    button.setAttribute("aria-expanded", "true");
  }

  button.addEventListener("click", function () {
    if (button.getAttribute("aria-expanded") === "true") closeMenu(false);
    else openMenu();
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && header.classList.contains("is-open")) {
      closeMenu(true);
    }
  });

  document.addEventListener("click", function (event) {
    if (!header.classList.contains("is-open")) return;
    if (header.contains(event.target)) return;
    closeMenu(false);
  });

  var holdCurrent = false;

  links.forEach(function (link) {
    link.addEventListener("click", function () {
      setCurrent(link.getAttribute("href").slice(1));
      holdCurrent = true;
      window.setTimeout(function () {
        holdCurrent = false;
        syncFromScroll();
      }, 700);
      if (mobile.matches) closeMenu(false);
    });
  });

  if (typeof mobile.addEventListener === "function") {
    mobile.addEventListener("change", function () {
      if (!mobile.matches) closeMenu(false);
    });
  }

  function setCurrent(id) {
    links.forEach(function (link) {
      if (link.getAttribute("href") === "#" + id) {
        link.setAttribute("aria-current", "true");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  }

  function headerHeight() {
    var bar = document.querySelector(".site-header");
    return bar ? bar.getBoundingClientRect().height : 0;
  }

  function syncFromScroll() {
    if (!sections.length) return;
    var marker = window.scrollY + headerHeight() + 32;
    var current = sections[0];
    sections.forEach(function (section) {
      if (section.offsetTop <= marker) current = section;
    });
    var canScroll = document.documentElement.scrollHeight > window.innerHeight + 8;
    var atBottom = canScroll && window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4;
    if (atBottom) current = sections[sections.length - 1];
    setCurrent(current.id);
  }

  var frame = 0;
  window.addEventListener("scroll", function () {
    if (holdCurrent) return;
    if (frame) return;
    frame = window.requestAnimationFrame(function () {
      frame = 0;
      syncFromScroll();
    });
  }, { passive: true });

  syncFromScroll();
})();
