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
    
    total_items = sum(cart.values())

    for p_id, quantity in cart.items():
        product = Product.objects.filter(id=p_id).first()

        if not product:
            continue  # просто пропускаем удалённый товар

        total_price = product.price * quantity
        grand_total += total_price

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': total_price
        })

    # 🔥 применяем скидку если есть
    discount = request.session.get("discount", 0)

    if discount:
        grand_total = grand_total - (grand_total * discount / 100)

    if not cart:
        request.session.pop("discount", None)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'grand_total': grand_total,
        'total_items': total_items,
        'discount': discount
    })

def apply_promo(request):
    if request.method == "POST":
        promo = request.POST.get("promo_code")

        if promo == "GAME2026":
            request.session["discount"] = 20
        else:
            request.session.pop("discount", None)  # удаляем скидку если код неверный

    return redirect("cart")

def checkout(request):
    # очищаем корзину
    request.session['cart'] = {}
    
    # очищаем скидку
    request.session.pop("discount", None)
    
    request.session.modified = True

    return render(request, "success.html")