from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
import random

from .models import ProductCategory, Product
from geekshop.settings import LOGIN_URL


def get_basket(request):
    return request.user.is_authenticated and request.user.basket.all() or []


def get_menu():
    return ProductCategory.objects.all()


def index(request):
    product = Product.objects.all()

    context = {
        'categories': get_menu(),
        'product': product,
        'page_title': 'Main',
        'basket': get_basket(request),
    }

    return render(request, 'mainapp/index.html', context)


def item(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        'page_title': 'item',
        'categories': get_menu(),
        'category': product.category,
        'product': product,
        'item': item,
        'basket': get_basket(request),
    }

    return render(request, 'mainapp/item.html', context)


def hot_product(request):
    hot_product_pk = random.choice(Product.objects.values_list('pk', flat=True))
    hot_product = Product.objects.get(pk=hot_product_pk)

    same_products = hot_product.category.product_set.exclude(pk=hot_product.pk)

    context = {
        'page_title': 'Hot Offers',
        'categories': get_menu(),
        'item': item,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': get_basket(request),
    }

    return render(request, 'mainapp/hot_product.html', context)


def products(request):
    product = Product.objects.all()

    context = {
        'page_title': 'Works',
        'categories': get_menu(),
        'product': product,
        'basket': get_basket(request),
    }

    return render(request, 'mainapp/products.html', context)


def category_product(request, pk):
    if pk == '0':
        category = {'pk': 0, 'name': 'All'}
        product = Product.objects.all()

    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        product = category.product_set.all()

    context = {
        'page_title': 'works',
        'categories': get_menu(),
        'product': product,
        'category': category,
        'basket': get_basket(request),
    }

    return render(request, 'mainapp/category_product.html', context)


def contacts(request):
    context = {
        'page_title': 'Contacts',
        'basket': get_basket(request),
    }

    return render(request, 'mainapp/contacts.html', context)
