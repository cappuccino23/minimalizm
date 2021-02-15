from django.contrib import admin
from django.urls import path

import myadminapp.views as myadminapp


app_name = 'myadminapp'

urlpatterns = [
    path('', myadminapp.index, name='index'),
    path('user/create/', myadminapp.user_create, name='user_create'),
    path('user/update/<int:pk>', myadminapp.user_update, name='user_update'),
    path('user/delete/<int:pk>', myadminapp.user_delete, name='user_delete'),

]
