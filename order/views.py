from django.shortcuts import render

from order.models import Person
from order.models import Order
from order.models import Delivery
from products.models import Product
from products.models import Company


def order_tobacco(request, type_product, comp_id):
    detail = Product.objects.filter(type_product = type_product)
    company = Company.objects.filter(pk=comp_id)
    context = {'detail':detail, 'company':company}
    return render(request, 'products/order_tobak.html', context)