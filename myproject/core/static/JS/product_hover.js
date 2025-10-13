document.addEventListener('DOMContentLoaded', () => {
    // Находим все изображения с классом 'product-image'
    const productImages = document.querySelectorAll('.product-image');

    productImages.forEach(img => {
        // Проверяем, есть ли у изображения второе (hover) изображение
        const hoverSrc = img.getAttribute('data-hover-src');

        if (hoverSrc) {
            // Если есть, добавляем слушатели событий
            img.addEventListener('mouseover', () => {
                // При наведении меняем src на hoverSrc
                img.src = hoverSrc;
            });

            img.addEventListener('mouseout', () => {
                // При убирании мыши меняем src обратно на originalSrc
                img.src = img.getAttribute('data-original-src');
            });
        }
    });
});