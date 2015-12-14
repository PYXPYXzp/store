# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect

import cart

def show_cart(request, template_name = 'cart/cart.html'):
    if request.method == 'POST':
        postdata = request.POST.copy()
        if postdata['submit']=='Remove':
            cart.remove_from_cart(request)
        if postdata['submit']=='Update':
            cart.update_cart(request)
    cart_item = cart.get_cart_items(request)
    cart_id = cart._cart_id(request)
    page_title = 'Корзина'
    cart_subtotal = cart.cart_subtotal(request)
    context = {'cart_item': cart_item, 'cart_id': cart_id, 'cart_subtotal': cart_subtotal}
    return render(request, template_name, context)

