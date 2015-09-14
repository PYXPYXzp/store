from django.shortcuts import render_to_response
from django.http import HttpResponse

from cart1 import Cart
from products.models import Product

def add_to_cart(request, product_id, quantity):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.unit_price, quantity)

def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

def get_cart(request):

    return render_to_response('cart.html', dict(cart=Cart(request)))

def test_view(request):
    print request.POST
    return HttpResponse("Here's the text of the Web page.")