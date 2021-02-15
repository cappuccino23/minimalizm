from django.contrib import admin
from django.urls import path, re_path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('products/', mainapp.products, name='products'),
    re_path(r'^category/(?P<pk>\d+)/products/$', mainapp.category_product, name='category_product'),
    re_path(r'^item/(?P<pk>\d+)/$', mainapp.item, name='item'),
    # path('item/<int:pk>/', mainapp.item, name='item'),
    path('contacts/', mainapp.contacts, name='contacts'),
    path('hot/product/', mainapp.hot_product, name='hot_product'),
]
