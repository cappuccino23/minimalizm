from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from authapp.models import ShopUser
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from django.urls import reverse

from myadminapp.forms import AdminShopUserCreateForm, AdminShopUserUpdateForm


@user_passes_test(lambda x: x.is_superuser)
def index(request):
    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    content = {
        'title': 'Admin | User',
        'object_list': users_list
    }

    return render(request, 'myadminapp/index.html', content)


@user_passes_test(lambda x: x.is_superuser)
def user_create(request):
    title = 'Users/Created'

    if request.method == 'POST':
        user_form = AdminShopUserCreateForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('myadmin:index'))
    else:
        user_form = AdminShopUserCreateForm()

    context = {
        'title': 'Create User',
        'form': user_form
    }

    return render(request, 'myadminapp/user_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_update(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user_form = AdminShopUserUpdateForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('myadmin:index'))
    else:
        user_form = AdminShopUserUpdateForm(instance=user)

    context = {
        'title': 'Update User',
        'form': user_form,
    }

    return render(request, 'myadminapp/user_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_delete(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('myadmin:index'))

    context = {
        'title': 'Delete User',
        'user_to_delete': user,
    }

    return render(request, 'myadminapp/user_delete.html', context)
