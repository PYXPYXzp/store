# -*- coding: utf-8 -*-
from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404


from order.models import Person
from order.models import Order
from order.models import Delivery
from products.models import Product
from products.models import Company
from .forms import FormPerson
from cart.models import CartItem



def order(request):
    cart_id = request.POST.get('cart_id')
    cart_subtotal = request.POST.get('cart_subtotal')
    delivery =  get_list_or_404(Delivery)
    if request.method == 'POST':
        form = FormPerson(request.POST)
    context = {'delivery': delivery, 'form': form, 'cart_id': cart_id, 'cart_subtotal': cart_subtotal}
    return render(request, 'order/order_tobak.html', context)


def add_info(request):
     if request.method == 'POST':
        postdata = request.POST.copy()
        comment = postdata.get('comment')
        delivery = postdata.get('delivery')
        print delivery
        cart_id = postdata.get('cart_id')
        form = FormPerson(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            tel_namb = form.cleaned_data['tel_namb']
            city = form.cleaned_data['city']
            Person.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                tel_namb = tel_namb,
                comment = comment,
                city = city,
                )
        delivery = Delivery.objects.get(type_delivery=delivery)
        person = get_object_or_404(Person, email=email, tel_namb=tel_namb)
        order1 = CartItem.objects.get(cart_id=cart_id)
        ord = Order()
        ord.delivery = delivery
        ord.person = person
        ord.order = order1
        ord.save()
        return redirect('http://127.0.0.1:8000/index/')
