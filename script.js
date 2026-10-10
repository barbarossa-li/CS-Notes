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

  links.forEach(function (link) {
    link.addEventListener("click", function () {
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

  if ("IntersectionObserver" in window) {
    var observer = new IntersectionObserver(
      function (entries) {
        var visible = entries
          .filter(function (entry) {
            return entry.isIntersecting;
          })
          .sort(function (a, b) {
            return b.intersectionRatio - a.intersectionRatio;
          })[0];
        if (visible) setCurrent(visible.target.id);
      },
      { rootMargin: "-30% 0px -55% 0px", threshold: [0.2, 0.5, 0.8] }
    );
    sections.forEach(function (section) {
      observer.observe(section);
    });
  }
})();
