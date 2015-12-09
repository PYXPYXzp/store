from django.conf.urls import url
from django.conf.urls import patterns
import cart

urlpatterns = patterns('cart.views',
    url(r'^$',  'show_cart', { 'template_name': 'cart/cart.html'}, 'show_cart'),
    url(r'^add_to_cart/$', cart.add_to_cart, name='add_to_cart'),
                       )