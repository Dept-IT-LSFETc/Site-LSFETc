const galleryItems = document.querySelectorAll('.gallery-item');
        const overlay = document.getElementById('imageOverlay');
        const overlayImage = document.getElementById('overlayImage');
        const closeBtn = document.getElementById('closeBtn');
        const prevBtn = document.getElementById('prevBtn');
        const nextBtn = document.getElementById('nextBtn');
        let currentIndex = 0;

        // Open overlay when clicking an image
        galleryItems.forEach((item, index) => {
            item.addEventListener('click', () => {
                currentIndex = index;
                updateOverlayImage();
                overlay.classList.add('active');
            });
        });

        // Close overlay
        closeBtn.addEventListener('click', () => {
            overlay.classList.remove('active');
        });

        // Navigate to previous image
        prevBtn.addEventListener('click', () => {
            currentIndex = (currentIndex - 1 + galleryItems.length) % galleryItems.length;
            updateOverlayImage();
        });

        // Navigate to next image
        nextBtn.addEventListener('click', () => {
            currentIndex = (currentIndex + 1) % galleryItems.length;
            updateOverlayImage();
        });

        // Update the overlay image source
        function updateOverlayImage() {
            const src = galleryItems[currentIndex].getAttribute('data-src');
            overlayImage.src = src;
        }

        // Close overlay when clicking outside the image
        overlay.addEventListener('click', (e) => {
            if (e.target === overlay) {
                overlay.classList.remove('active');
            }
        });