document.addEventListener("DOMContentLoaded", () => {
  const navbar = document.querySelector(".navbar");

  window.addEventListener("scroll", () => {
    if (window.scrollY > 0) {
      navbar.style.backgroundColor = "rgb(233, 143, 43)";
    } else {
      navbar.style.backgroundColor = "transparent";
    }
  });
});
