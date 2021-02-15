from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from authapp.forms import ShopUserLoginForm, ShopUserRegistrationForm, ShopUserEditForm


def login(request):
    next = request.GET.get('next', '')

    if request.method == 'POST':

        form = ShopUserLoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user and user.is_active:
                auth.login(request, user)
                if 'next' in request.POST:
                    return HttpResponseRedirect(request.POST['next'])

            return HttpResponseRedirect(reverse('main:index'))

    else:
        form = ShopUserLoginForm()

    context = {
        'title': 'Вход в систему',
        'form': form,
        'next': next,
    }

    return render(request, 'authapp/login.html', context)


def registration(request):
    if request.method == 'POST':

        form = ShopUserRegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:index'))

    else:
        form = ShopUserRegistrationForm()

    context = {
        'title': 'Регистрация пользователя',
        'form': form,
    }

    return render(request, 'authapp/registration.html', context)


def edit(request):
    if request.method == 'POST':

        form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:edit'))

    else:
        form = ShopUserEditForm(instance=request.user)

    context = {
        'title': 'Профиль пользователя',
        'form': form,
    }

    return render(request, 'authapp/edit.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


