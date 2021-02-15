from django.db import models


class ProductCategory(models.Model):
    name = models.CharField('Имя категории', max_length=64)
    description = models.TextField('Описание категории', blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.category = None

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory,
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория продукта')

    name = models.CharField('Название модели', max_length=64)
    image = models.ImageField(upload_to='models_image', blank=True)
    short_desc = models.TextField('Краткое описание модели', blank=True)
    description = models.TextField('Описание модели', blank=True)
    price = models.DecimalField('Цена пошива модели', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField('количество на складе', default=0)

    def __str__(self):
        return f'{self.name} ({self.category.name})'
