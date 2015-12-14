# -*- coding: utf-8 -*-
from django.shortcuts import get_list_or_404, render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


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
        cart_id = postdata.get('cart_id')
        form = FormPerson(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            tel_namb = form.cleaned_data['tel_namb']
            city = form.cleaned_data['city']
            x = Person.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                tel_namb = tel_namb,
                comment = comment,
                city = city,
                )
        delivery = Delivery.objects.get(type_delivery=delivery)
        person = Person.objects.get(id = x.id)
        order1 = CartItem.objects.get(cart_id=cart_id)
        ord = Order()
        ord.delivery = delivery
        ord.person = person
        ord.order = order1
        ord.save()
        send_email(request, delivery, person, order1, comment, email, ord.id)
        return redirect('http://127.0.0.1:8000/index/')

def send_email(request, delivery, person, order1, comment, email, ord_id):
    order=Order.objects.get(id = ord_id)
    subject = ('New Order')
    message = ('Город', order.person.city, 'Доставка', order.delivery.type_delivery,
               'Получатель', order.person.first_name, order.person.last_name, order.person.tel_namb,
               "заказ", order.order.product.flower, order.order.quantity)
    message = str(message)
    from_email = email
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['winner1040@gmail.com'])

        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    else:
        return HttpResponse('Make sure all fields are entered correct')



    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'