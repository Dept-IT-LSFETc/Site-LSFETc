$(document).ready(function () {
    const images = $('.gallery-grid img');
    const lightbox = $('.lightbox');
    const lightboxImg = $('.lightbox img');
    let currentIndex = 0;

    initializeLightbox();
    hideLightbox();

    function initializeLightbox() {
        lightbox.hide(); 
        $('body').removeClass('lightbox-active');
        lightboxImg.attr('src', ''); 
    }

    function hideLightbox() {
        lightbox.fadeOut(() => {
            $('body').removeClass('lightbox-active');
            lightboxImg.attr('src', ''); 
        });
    }

    function showLightbox(index) {
        currentIndex = index;
        const imgSrc = images.eq(index).attr('src');
        if (imgSrc) {
            lightboxImg.attr('src', imgSrc); 
            $('body').addClass('lightbox-active');
            lightbox.fadeIn();
        }
    }

    function showImage(index) {
        currentIndex = index;
        const imgSrc = images.eq(index).attr('src');
        if (imgSrc) {
            lightboxImg.attr('src', imgSrc); 
        }
    }


    images.click(function () {
        const index = images.index(this);
        showLightbox(index);
    });

    $('.lightbox .close').click(function () {
        hideLightbox();
    });

    $('.lightbox .prev').click(function () {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        showImage(currentIndex);
    });

    $('.lightbox .next').click(function () {
        currentIndex = (currentIndex + 1) % images.length;
        showImage(currentIndex);
    });

    const esuButton = $('#esuButton');
    const esuInfo = $('#esuInfo');

    esuButton.click(function () {
        if (esuInfo.is(':visible')) {
            esuInfo.slideUp(); 
        } else {
            esuInfo.slideDown(); 
        }
    });

    const ftfmmButton = $('#ftfmmButton');
    const ftfmmInfo = $('#ftfmmInfo');

    ftfmmButton.click(function () {
        if (ftfmmInfo.is(':visible')) {
            ftfmmInfo.slideUp(); 
        } else {
            ftfmmInfo.slideDown(); 
        }
    });
});
