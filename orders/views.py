import time
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from webamcarts.models import Cartmen
from .models import Order
from .utils import id_generator

# Create your views here.

def orders(request):
    context = {}
    template = 'orders/user.html'
    return render(request, template, context)

@login_required
def checkout(request):
    try:
        the_men_id = request.session['men_cart_id']
        cartmen = Cartmen.objects.get(id=the_men_id)
    except:
        the_men_id = None
        return HttpResponseRedirect(reverse('cartmen'))

    try:
        new_order = Order.objects.get(cartmen=cartmen)
    except Order.DoesNotExist:
        new_order = Order()
        new_order.cartmen = cartmen
        new_order.user = request.user
        new_order.order_id = id_generator()
        new_order.save()
    except:
        return HttpResponseRedirect(reverse('cartmen'))

    if new_order.status == 'Finished':
        del request.session['men_cart_id']
        del request.session['cart_men_total']
        return HttpResponseRedirect(reverse('cartmen'))
    
    context = {}
    template = 'products/home.html'

    return render(request, template, context)