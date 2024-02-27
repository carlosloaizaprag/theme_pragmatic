var swiper = new Swiper(".mySwiper", {
    slidesPerView: 2,
    spaceBetween: 20,
    centeredSlides: false,
    autoplay: {
        delay: 3500,
        disableOnInteraction: false,
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        "@0.00": {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        "@0.75": {
            slidesPerView: 3,
            spaceBetween: 30,
        },
        "@1.00": {
            slidesPerView: 4,
            spaceBetween: 50,
        },
        "@1.50": {
            slidesPerView: 5,
            spaceBetween: 60,
        },
        "@1.75": {
            slidesPerView: 6,
            spaceBetween: 70,
        },
       
    },
});