import os
import json
from django.core.management.base import BaseCommand
from django.conf import settings

from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(
            os.path.join(settings.JSON_PATH, file_name + '.json'),
            encoding='utf-8'
    ) as infile:
        return json.load(infile)


class Command(BaseCommand):

    help = 'Fill DB new data'

    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()

        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_from_json('products')
        Product.objects.all().delete()

        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            _category = ProductCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        # Создаем суперпользователя
        if not ShopUser.objects.filter(username='django').exists():
            ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')
