from django.conf.urls import url
from django.conf.urls import patterns

urlpatterns = patterns('cart.views',
    url(r'^$',  'show_cart', { 'template_name': 'cart/cart.html'}, 'show_cart'),
                       )