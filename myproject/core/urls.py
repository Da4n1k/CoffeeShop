# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Пустая строка '' означает главную страницу
    path('', views.index, name='index'),
]