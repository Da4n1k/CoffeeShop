<<<<<<< Updated upstream
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def index(request):
    cart = request.session.get('cart', {})
    total_items = sum(cart.values())
    return render(request, 'index.html', {'total_items': total_items})

def promo_page(request):
    cart = request.session.get('cart', {})
    total_items = sum(cart.values())
    return render(request, 'promo.html', {'total_items': total_items})

def order_page(request):
    products = Product.objects.all()
    cart = request.session.get('cart', {})
    total_items = sum(cart.values())
    return render(request, 'order.html', {
        'products': products, 
        'total_items': total_items
    })

def add_to_cart(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        p_id = str(product_id)
        cart[p_id] = cart.get(p_id, 0) + 1
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('order')

def cart_page(request):
    cart = request.session.get('cart', {})
    cart_items = []
    grand_total = 0
    
    # Считаем общее количество для счетчика в шапке
    total_items = sum(cart.values())

    for p_id, quantity in cart.items():
        product = get_object_or_404(Product, id=p_id)
        total_price = product.price * quantity
        grand_total += total_price
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': total_price
        })
        
    return render(request, 'cart.html', {
        'cart_items': cart_items, 
        'grand_total': grand_total,
        'total_items': total_items  # Добавили передачу счетчика сюда!
    })
=======
from django.shortcuts import render
from django.http import JsonResponse

# 1. Твой контролируемый список цен (можно менять прямо здесь)
COFFEE_DATA = {
    "1": {"name": "Капучино", "price": 249},
    "2": {"name": "Латте", "price": 279},
    "3": {"name": "Флэт Уайт", "price": 299},
    "4": {"name": "Раф", "price": 319},
}

def index(request):
    """Главная страница"""
    return render(request, 'index.html')

def promo_page(request):
    """Страница акций"""
    return render(request, 'promo.html')

def order_page(request):
    """Страница меню (если нужно)"""
    return render(request, 'order.html', {'products': COFFEE_DATA.values()})

def add_to_cart(request, product_id):
    """Добавление в корзину через AJAX"""
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        pid = str(product_id)
        
        # Проверяем, существует ли такой кофе в нашем списке
        if pid in COFFEE_DATA:
            cart[pid] = cart.get(pid, 0) + 1
            request.session['cart'] = cart
            request.session.modified = True
            
            total_items = sum(cart.values())
            return JsonResponse({'status': 'ok', 'total_items': total_items})
            
    return JsonResponse({'status': 'error', 'message': 'Invalid product'}, status=400)

def cart_page(request):
    """Страница корзины с защитой от подмены цен"""
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for pid, qty in cart.items():
        # Берем данные ТОЛЬКО из нашего словаря COFFEE_DATA
        if pid in COFFEE_DATA:
            item_info = COFFEE_DATA[pid]
            subtotal = item_info['price'] * qty
            total_price += subtotal
            
            cart_items.append({
                'product': {
                    'id': pid,
                    'name': item_info['name'],
                    'price': item_info['price'],
                },
                'quantity': qty,
                'total_price': subtotal
            })

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'total_items': sum(cart.values())
    }
    return render(request, 'cart.html', context)

def clear_cart(request):
    """Дополнительная функция для полной очистки корзины"""
    if 'cart' in request.session:
        del request.session['cart']
    return render(request, 'cart.html', {'cart_items': [], 'total_price': 0, 'total_items': 0})
>>>>>>> Stashed changes
