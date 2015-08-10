
# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponse
from .models import Type
from .models import Product



def index(request):
    type_product = Type.objects.all()
    context = {'type_product': type_product}
    return render(request, 'products/index.html', context)

def tobaccolist(request):
    product_tobacco = Product.objects.filter(type = 2)
    context = {'product_tobacco': product_tobacco}
    return render(request, 'products/tobacco.html', context)
