from django.shortcuts import render

# Create your views here.
# core/views.py
from django.shortcuts import render
from .models import Product

def index(request):
    # Эта функция ищет файл index.html в папке templates
    return render(request, 'index.html')


def order_page(request):
    products = Product.objects.all()

    print("--- DEBUG: order_page view called ---")
    print(f"Number of products found: {products.count()}")
    for p in products:
        print(f"  Product: {p.title}, Price: {p.price}, Image URL: {p.image.url if p.image else 'No Image'}")
    print("-----------------------------------")

    # Проверим, что контекст формируется правильно
    context = {
        'products': products
    }
    print(f"Context being passed: {context}")  # Добавьте эту строку

    return render(request, 'order.html', context)

def promo_page(request):
    # Эта функция ищет файл index.html в папке templates
    return render(request, 'promo.html')