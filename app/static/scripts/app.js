// Responsive Navigation menu
const menuBtn = document.querySelector(".menu-btn");
const navigation = document.querySelector(".navigation")


menuBtn.addEventListener("click", () => {
    menuBtn.classList.toggle("active");
    navigation.classList.toggle("active");
});

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

const scrollRevealOption = {
    distance: "50px",
    origin: "bottom",
    duration: 1000,
}

ScrollReveal().reveal(".content h1", {
    ...scrollRevealOption,
});

ScrollReveal().reveal(".content p", {
    ...scrollRevealOption,
    delay: 500,
});

ScrollReveal().reveal(".content a", {
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
    autoplay: {
        delay: 5000, // Adjust the delay (in milliseconds) as needed
        disableOnInteraction: false, // Set to true if you want to stop autoplay on user interaction
    }
})
