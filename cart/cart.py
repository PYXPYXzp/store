# -*- coding: utf-8 -*-
import decimal
import random

from django.shortcuts import get_object_or_404
from models import CartItem
from products.models import Product
from django.http import JsonResponse
from django.core import serializers


CART_ID_SESSION_KEY = 'cart_id'

def _cart_id(request):
    if request.session.get(CART_ID_SESSION_KEY, '') == '':
        request.session[CART_ID_SESSION_KEY] = _generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]

def _generate_cart_id():
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_length = 50
    for y in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters)-1)]
    return cart_id

def get_cart_items(request):
    return CartItem.objects.filter(cart_id = _cart_id(request))

def add_to_cart(request):
    postdata = request.POST.copy()
    # product_slug = postdata.get('product_slug', '')
    quantity = postdata.get('quantity', 1)
    id = postdata.get('product_id')
    # p = get_object_or_404(Product, slug = product_slug)
    p = get_object_or_404(Product, id=id)
    cart_products = get_cart_items(request)
    product_in_cart = False
    for cart_item in cart_products:
        if cart_item.product.id == p.id:
            cart_item.augment_quantity(quantity)
            product_in_cart=True
            return JsonResponse({'product in cart':product_in_cart})
    if not product_in_cart:
        ci = CartItem()
        ci.product = p
        ci.quantity = quantity
        ci.cart_id = _cart_id(request)
        ci.save()
        return JsonResponse({'product in cart':product_in_cart})

def cart_distinct_item_count(request):
    return get_cart_items(request).count()

def get_single_item(request, product_id):
    return get_object_or_404(CartItem, id=product_id, cart_id=_cart_id(request))

def cart_subtotal(request):
    cart_total = decimal.Decimal('0.00')
    cart_products = get_cart_items(request)
    for cart_item in cart_products:
        cart_total += cart_item.product.cost * cart_item.quantity
    return cart_total

def update_cart(request):
    postdata = request.POST.copy()
    product_id = postdata['product_id']
    quantity = postdata['quantity']
    cart_item = get_single_item(request,product_id)
    if cart_item:
        if int(quantity)>0:
            cart_item.quantity=int(quantity)
            cart_item.save()
        else:
            remove_from_cart(request)

def remove_from_cart(request):
    postdata = request.POST.copy()
    product_id = postdata['id_product']
    cart_item = get_single_item(request, product_id)
    if cart_item:
        cart_item.delete()
    return JsonResponse({'cart_item':'remove'})

def empty_cart(request):
    user_cart = get_cart_items(request)
    user_cart.delete()
    return JsonResponse({'user_cart':'cart_empty'})