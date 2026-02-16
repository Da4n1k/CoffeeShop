console.log("ФАЙЛ CART.JS ЗАГРУЖЕН УСПЕШНО!"); // Эта строка должна появиться в консоли сразу

document.addEventListener('click', function (e) {
    const btn = e.target.closest('.btn-order');
    if (btn) {
        e.preventDefault();
        console.log("Клик по кнопке зафиксирован!"); // Это при нажатии
        
        document.addEventListener('click', function (e) {
    // Ищем ближайшего родителя с классом btn-order (на случай клика по тексту внутри кнопки)
    const btn = e.target.closest('.btn-order');
    
    if (btn) {
        e.preventDefault();
        e.stopPropagation(); // Останавливаем всплытие, чтобы React не перехватил клик

        const productId = btn.getAttribute('data-product-id');
        const csrfElement = document.querySelector('[name=csrfmiddlewaretoken]');
        
        if (!csrfElement) {
            console.error("CSRF токен не найден на странице!");
            return;
        }

        const csrftoken = csrfElement.value;

        console.log("Отправка запроса для ID товара:", productId);

        fetch(`/add/${productId}/`, {
            method: 'POST',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrftoken
            },
        })
        .then(response => {
            if (!response.ok) throw new Error('Ошибка сервера');
            return response.json();
        })
        .then(data => {
            if (data.total_items !== undefined) {
                // Ищем ссылки навигации
                const links = document.querySelectorAll('.nav-link');
                let found = false;
                links.forEach(link => {
                    if (link.innerText.includes('Корзина')) {
                        link.innerHTML = `<span class="nav-icon">🛒</span> Корзина (${data.total_items})`;
                        found = true;
                    }
                });
                
                if (!found) console.warn("Элемент корзины в меню не найден для обновления");
                alert('Добавлено в корзину!');
            }
        })
        .catch(err => {
            console.error("Ошибка:", err);
            // Если JS упал, мы увидим это здесь
        });
    }
});
    }
});

