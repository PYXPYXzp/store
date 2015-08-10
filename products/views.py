
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

def shisha_list(request):
    product_shisha = Product.objects.filter(type__type_product='Кальян')
    context = {'product_shisha': product_shisha}
    return render(request, 'products/shisha.html', context)

def other_list(request):
    product_other = Product.objects.filter(type__type_product='Разное')
    context = {'product_other': product_other}
    return render(request, 'products/other.html', context)