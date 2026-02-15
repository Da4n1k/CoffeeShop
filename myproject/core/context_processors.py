# core/context_processors.py

def cart_total_items(request):
    """
    Возвращает общее количество товаров в корзине (из сессии) 
    для отображения в базовом шаблоне (base.html).
    """
    cart = request.session.get('cart', {})
    total_items = sum(cart.values()) # Считаем сумму всех значений (количества)
    return {'cart_total_items': total_items}