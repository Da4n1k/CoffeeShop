from django.db import models

# Create your models here.
class Product(models.Model):
    # Название товара, максимальная длина 100 символов
    title = models.CharField(max_length=100)

    # Описание товара, может быть длинным текстом
    description = models.TextField()

    # Цена. Используем DecimalField для точности с деньгами
    # max_digits - общее кол-во цифр, decimal_places - кол-во цифр после запятой
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Картинка товара. Картинки будут загружаться в папку 'products/'
    image = models.ImageField(upload_to='products/')
    image_hover = models.ImageField(upload_to='products/hover/', blank=True, null=True)
    # Это нужно для красивого отображения названия товара в админке
    def __str__(self):
        return self.title