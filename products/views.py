from itertools import chain
from django.shortcuts import render, Http404
from .models import ProductMen, ProductMenImage, Variation, ProductWomen, ProductWomenImage, ProductKids, ProductKidsImage, ProductAccessory, ProductAccessoriesImage
# Create your views here.

def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None

    if q:
        prodmensearch = ProductMen.objects.filter(title__icontains=q)
        prodwomensearch = ProductWomen.objects.filter(title__icontains=q)
        prodkidsearch = ProductKids.objects.filter(title__icontains=q)
        prodaccsearch = ProductAccessory.objects.filter(title__icontains=q)

        results = chain(prodmensearch,prodwomensearch,prodkidsearch,prodaccsearch)

        context = {'query':q, 'results':results}
        template = 'products/result.html'
    else:
        context = {}
        template = 'products/home.html'
    return render(request, template, context)



def home(request):
    productmen_home = ProductMen.objects.all()
    productwomen_home = ProductWomen.objects.all()
    productkids_home = ProductKids.objects.all()
    productaccesor_home = ProductAccessory.objects.all()
    context = {'productmen_home':productmen_home, 'productwomen_home':productwomen_home,'productkids_home':productkids_home,'productaccesor_home':productaccesor_home}
    template = 'products/home.html'
    
    return render(request, template, context)



def productmen(request):
    productmen = ProductMen.objects.all()
    context = {'productmen':productmen}
    template = 'products/productmen.html'
    return render(request, template, context)


def productmendetails(request, slug):
    try:
        productmendetails = ProductMen.objects.get(slug=slug)
        productdetailsingle = productmendetails.productmenimage_set.all()
        context = {'productmendetails':productmendetails, 'productdetailsingle':productdetailsingle}
        template = 'products/productmendetails.html'
        return render(request, template, context)
    except:
        raise Http404


def productwomen(request):
    productwomen = ProductWomen.objects.all()
    context = {'productwomen':productwomen}
    template = 'products/productwomen.html'
    return render(request, template, context)

def productwomendetails(request, slug):
    try:
        productwomendetails = ProductWomen.objects.get(slug=slug)
        prodwomendetailsingle = productwomendetails.productwomenimage_set.all()
        context = {'productwomendetails':productwomendetails, 'prodwomendetailsingle':prodwomendetailsingle}
        template = 'products/product-women-dress-details.html'
        return render(request, template, context)
    except:
        raise Http404


def productkids(request):
    productkids = ProductKids.objects.all()
    context = {'productkids':productkids}
    template = 'products/productkids.html'
    return render(request, template, context)

def productkidsdetails(request, slug):
    try:
        productkidsdetails = ProductKids.objects.get(slug=slug)
        productkidetailssingle = productkidsdetails.productkidsimage_set.all()
        context = {'productkidsdetails':productkidsdetails, 'productkidetailssingle':productkidetailssingle}
        template = 'products/product-kids-dress-details.html'
        return render(request, template, context)
    except:
        raise Http404


def productaccessory(request):
    productaccessory = ProductAccessory.objects.all()
    context = {'productaccessory':productaccessory}
    template = 'products/productaccessory.html'
    return render(request, template, context)


def productaccessdetails(request, slug):
    try:
        productaccessdetails = ProductAccessory.objects.get(slug=slug)
        productaccessdetailsingle = productaccessdetails.productaccessoriesimage_set.all()
        context = {'productaccessdetails':productaccessdetails, 'productaccessdetailsingle':productaccessdetailsingle}
        template = 'products/product-accessories-dress-details.html'
        return render(request, template, context)
    except:
        raise Http404