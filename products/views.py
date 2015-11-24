
# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from products.models import Type
from products.models import Product
from products.models import Company

def index(request):
    return render(request, 'products/main.html')

def tobacco_company(request):
    companytob = Company.objects.filter(product__type__type_product ='Табак').distinct()
    context = {'companytob': companytob}
    return render(request, 'products/comptobaklist.html', context)

def shisha_company(request):
    product_shisha = Company.objects.filter(product__type__type_product='Кальян').distinct()
    context = {'product_shisha': product_shisha}
    return render(request, 'products/compshishalist.html', context)

def other_company(request):
    product_other = Company.objects.filter(product__type__type_product='Разное').distinct()
    types = Product.objects.filter(type__type_product='Разное')
    context = {'product_other': product_other, 'types':types}
    return render(request, 'products/compotherlist.html', context)

def list(request, comp_id):
    model = Product.objects.filter(company__pk=comp_id)
    context = {'comp_id': comp_id, 'model': model}
    return render(request, 'products/list.html', context)

def detail_tobacco(request, models_flower, comp_id):
    detail = Product.objects.filter(flower = models_flower)
    company = Company.objects.filter(pk=comp_id)
    context = {'detail':detail, 'company':company, 'id':id}
    return render(request, 'products/details_tobak.html', context)

def detail_shisha(request, models_model, comp_id):
    detail = Product.objects.filter(model = models_model)
    company = Company.objects.filter(pk=comp_id)
    context = {'detail':detail, 'company':company}
    return render(request, 'products/details_kal.html', context)

def detail_other(request, comp_id, type_product):
    detail = Product.objects.filter(type_product = type_product)
    company = Company.objects.filter(pk=comp_id)
    context = {'detail':detail, 'company':company}
    return render(request, 'products/details_other.html', context)