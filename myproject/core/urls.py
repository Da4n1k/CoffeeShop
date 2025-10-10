# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Пустая строка '' означает главную страницу
    path('', views.index, name='index'),
    path('promo/', views.promo_page, name='promo'),
    path('order/', views.order_page, name='order'),
]