
# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from .models import Type
from .models import Product
from .models import Company

def index(request):
    return render(request, 'products/main.html')

def tobacco_company(request):
    companytob = Company.objects.filter(product__type__type_product ='Табак').distinct()
    context = {'companytob':companytob}
    return render(request, 'products/complist.html', context)

def flower_detail(request, comp_id):
    flower_tobacco = Product.objects.filter(pk=comp_id)
    context = {'flower_tobacco':flower_tobacco}
    return render(request, 'products/flowerlist.html', context)

def shisha_list(request, ):
    product_shisha = Product.objects.filter(type__type_product='Кальян')
    context = {'product_shisha': product_shisha}
    return render(request, 'products/shisha.html', context)

def other_list(request):
    product_other = Product.objects.filter(type__type_product='Разное')
    context = {'product_other': product_other}
    return render(request, 'products/other.html', context)