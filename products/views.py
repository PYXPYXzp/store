
# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from .models import Type
from .models import Product
from .models import Company

def index(request):
    return render(request, 'products/main.html')

def tobacco_all(request):
    tabak = Type.objects.get(type_product = 'Табак')
    tobacco_list = Product.objects.filter(type = tabak)
    all_company = Company.objects.all()
    context = {'tobacco_list': tobacco_list,'all_company':all_company}
    return render(request, 'products/complist.html', context)


def shisha_list(request):
    product_shisha = Product.objects.filter(type__type_product='Кальян')
    context = {'product_shisha': product_shisha}
    return render(request, 'products/shisha.html', context)

def other_list(request):
    product_other = Product.objects.filter(type__type_product='Разное')
    context = {'product_other': product_other}
    return render(request, 'products/other.html', context)