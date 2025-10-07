from django.shortcuts import render

# Create your views here.
# core/views.py
from django.shortcuts import render

def index(request):
    # Эта функция ищет файл index.html в папке templates
    return render(request, 'index.html')