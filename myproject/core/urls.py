from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.order_page, name='order'),
    path('promo/', views.promo_page, name='promo'),
    path('cart/', views.cart_page, name='cart'),
    # Теперь это обычный путь для формы
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('apply-promo/', views.apply_promo, name='apply_promo'),
    path('checkout/', views.checkout, name='checkout'),
]