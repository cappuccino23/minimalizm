from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from mainapp.models import Product
from basketapp.models import Basket
from geekshop.settings import LOGIN_URL


@login_required()
def index(request):
    context = {
        'basket': request.user.basket.all()
    }
    return render(request, 'basketapp/index.html', context)


@login_required()
def add_product(request, pk):
    if LOGIN_URL in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('mainapp:item', kwargs={'pk': pk}))

    product = get_object_or_404(Product, pk=pk)
    # basket = request.user.basket_set.filter(product_pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def delete_product(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    basket.delete()

    return HttpResponseRedirect(reverse('basket:index'))


@login_required()
def change(request, pk, quantity):
    if request.is_ajax():
        basket = get_object_or_404(Basket, pk=pk)

        if quantity <= 0:
            basket.delete()
        else:
            basket.quantity = quantity
            basket.save()

        context = {
            'basket': request.user.basket.all()
        }
        result = render_to_string('basketapp/includes/inc__cart.html', context, request=request)

        return JsonResponse({'result': result})

        # return JsonResponse({'result':
        # 'total_cost': basket.total_cost,
        # 'total_quantity': basket.total_quantity,
        # 'product_cost': basket.product_cost,
    # })
