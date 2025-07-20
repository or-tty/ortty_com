document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.querySelector("nav");
    let lastScrollTop = window.scrollY;

    window.addEventListener("scroll", function () {
    const currentScroll = window.scrollY;

    if (currentScroll > lastScrollTop && currentScroll > 100) {
        // Скролл вниз — прячем меню
        navbar.classList.add("hide");
    } else {
        // Скролл вверх — показываем меню
        navbar.classList.remove("hide");
    }

    lastScrollTop = currentScroll;
    });
});