document.addEventListener('DOMContentLoaded', () => {
    console.log("Скрипт корзины активен");

    document.querySelectorAll('.btn-order').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const productId = this.getAttribute('data-product-id');
            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

            console.log("Отправка запроса для ID:", productId);

            fetch(`/cart/add/${productId}/`, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrftoken
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Обновляем число в шапке (id="cart-count")
                    const counter = document.getElementById('cart-count');
                    if (counter) counter.textContent = data.total_items;
                    
                    alert('Товар добавлен в корзину!');
                }
            })
            .catch(error => {
                console.error('Ошибка AJAX:', error);
                alert('Произошла ошибка при добавлении');
            });
        });
    });
});