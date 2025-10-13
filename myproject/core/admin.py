from django.contrib import admin
# Импортируем нашу модель Product
from .models import Product

# Простая регистрация модели
admin.site.register(Product)
