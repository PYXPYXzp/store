
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
    context = {'companytob': companytob}
    return render(request, 'products/comptobaklist.html', context)

def flower_list(request, comp_id):
    flower_tobacco = Product.objects.filter(company__pk=comp_id)
    context = {'flower_tobacco': flower_tobacco}
    return render(request, 'products/flowerlist.html', context)

def shisha_company(request):
    product_shisha = Company.objects.filter(product__type__type_product='Кальян').distinct()
    context = {'product_shisha': product_shisha}
    return render(request, 'products/compshishalist.html', context)

def shisha_list(request, comp_id):
    model_shisha = Product.objects.filter(company__pk=comp_id)
    context = {'model_shisha': model_shisha}
    return render(request, 'products/shishalist.html', context)

def other_company(request):
    product_other = Company.objects.filter(product__type__type_product='Разное').distinct()
    context = {'product_other': product_other}
    return render(request, 'products/compotherlist.html', context)

def other_list(request, comp_id):
    model_other = Product.objects.filter(company__pk=comp_id)
    context = {'model_other': model_other}
    return render(request, 'products/otherlist.html', context)