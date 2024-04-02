const menuBtn = document.getElementById("menu-btn");
const navLinks = document.getElementById("nav-links");
const menuBtnIcon = menuBtn.querySelector("i");

menuBtn.addEventListener("click", (e) => {
    navLinks.classList.toggle("open");

    const isOpen = navLinks.classList.contains("open");
    menuBtnIcon.setAttribute("class", isOpen ? "ri-close-line" : "ri-menu-line");
});

navLinks.addEventListener("click", (e) => {
    navLinks.classList.remove("open");
    menuBtnIcon.setAttribute("class", "ri-menu-line");
});

const scrollRevealOption = {
    distance: "50px",
    origin: "bottom",
    duration: 1000,
}

ScrollReveal().reveal(".header_container h1", {
    ...scrollRevealOption,
});

ScrollReveal().reveal(".header_container p", {
    ...scrollRevealOption,
    delay: 500,
});

ScrollReveal().reveal(".header_container p span", {
    ...scrollRevealOption,
    delay: 1000,
});

ScrollReveal().reveal(".popular_card", {
    ...scrollRevealOption,
    interval: 500,
});

ScrollReveal().reveal(".register_image img", {
    ...scrollRevealOption,
    origin: "right",
});

ScrollReveal().reveal(".register_content h4", {
    ...scrollRevealOption,
    delay: 500,
});

ScrollReveal().reveal(".register_btn", {
    ...scrollRevealOption,
    delay: 1000,
});

const swiper = new Swiper(".swiper", {
    slidesPerView: "auto",
    spaceBetween: 0,
})

// Responsive Slider
const btns = document.querySelectorAll(".nav-btn");
const slides = document.querySelectorAll(".picture-slide");

let currentSlide = 0;

const nextSlide = () => {
    slides[currentSlide].classList.remove("active");
    btns[currentSlide].classList.remove("active");

    currentSlide = (currentSlide + 1) % slides.length;

    slides[currentSlide].classList.add("active");
    btns[currentSlide].classList.add("active");
};

const prevSlide = () => {
    slides[currentSlide].classList.remove("active");
    btns[currentSlide].classList.remove("active");

    currentSlide = (currentSlide - 1 + slides.length) % slides.length;

    slides[currentSlide].classList.add("active");
    btns[currentSlide].classList.add("active");
};

btns.forEach((btn, i) => {
    btn.addEventListener("click", () => {
        slides[currentSlide].classList.remove("active");
        btns[currentSlide].classList.remove("active");

        currentSlide = i;

        slides[currentSlide].classList.add("active");
        btns[currentSlide].classList.add("active");
    });
});

// Automatic slide change every 5 seconds
setInterval(nextSlide, 5000);