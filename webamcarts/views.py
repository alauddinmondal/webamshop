from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from products.models import ProductMen, Variation
from .models import Cartmen, CartItem, Cartwomen, Cartkids, Cartaccessry


# Create your views here.

# Cart update for men.

def cartmenview(request):
    try:
        the_men_id = request.session['men_cart_id']
        cartmen = Cartmen.objects.get(id=the_men_id)
    except:
         the_men_id = None
    if the_men_id:
        new_total = 0.00
        for menitem in cartmen.cartitem_set.all():
            line_total = float(menitem.product.price) * menitem.quantity
            new_total += line_total
            # new_total += line_total
        request.session['cart_men_total'] = cartmen.cartitem_set.count()
        cartmen.total = new_total
        cartmen.save()
        context = {'cartmen':cartmen}
    else:
        cart_men_empty_message = 'Your cart is empty! Please keep shopping.'
        context = {'cartmen_empty':True, 'cart_men_empty_message':cart_men_empty_message}

    template = 'cart/viewmen.html'
    return render(request, template, context)

def remove_from_cart(request, id):
    try:
        the_men_id = request.session['men_cart_id']
        cartmen = Cartmen.objects.get(id=the_men_id)
    except:
        return HttpResponseRedirect(reverse('cartmen'))
    cart_item = CartItem.objects.get(id=id)
    cart_item.cart = None
    cart_item.save()
    return HttpResponseRedirect(reverse('cartmen'))
    

def update_cartmen(request, slug):
    request.session.set_expiry(2592000) #set to 1 Month

    try:
        the_men_id = request.session['men_cart_id']
    except:
        newcart_men = Cartmen()
        newcart_men.save()
        request.session['men_cart_id'] = newcart_men.id
        the_men_id = newcart_men.id

    cartmen = Cartmen.objects.get(id=the_men_id)
    

    try:
        producstmen = ProductMen.objects.get(slug=slug)
    except ProductMen.DoesNotExist:
        pass
    except:
        pass

    product_var = []
    if request.method == 'POST':
        qty = request.POST['qty']
        for item in request.POST:
            key = item
            val = request.POST[key]
            try:
                v = Variation.object.get(productmen=producstmen, category__iexact=key, title__iexact=val)
                product_var.append(v)
            except:
                pass
        cart_item = CartItem.objects.create(cart=cartmen, product=producstmen)
        if len(product_var)>0:
            cart_item.variations.add(*product_var)  
        cart_item.quantity = qty
        cart_item.save()
    
        for prodqtytotal in CartItem.objects.all():
            prdtotal = float(prodqtytotal.product.price) * prodqtytotal.quantity
            prodqtytotal.line_total = prdtotal
            prodqtytotal.save()

        return HttpResponseRedirect(reverse('cartmen'))
    
    return HttpResponseRedirect(reverse('cartmen'))



# Cart update for women.   

def cartwomenview(request):
    cartwomen = Cartwomen.objects.all()[0]
    context = {'cartwomen':cartwomen}
    template = 'cart/viewomen.html'
    return render(request, template, context)


# Cart update for kids   

def cartkidsview(request):
    cartkids = Cartkids.objects.all()[0]
    context = {'cartkids':cartkids}
    template = 'cart/viewkids.html'
    return render(request, template, context)




# Cart update for accessory.   

def cartaccryview(request):
    cartaccry = Cartaccessry.objects.all()[0]
    context = {'cartaccry':cartaccry}
    template = 'cart/viewaccessory.html'
    return render(request, template, context)
