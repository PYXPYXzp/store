from django.conf.urls import url
from django.conf.urls import patterns
import cart

urlpatterns = patterns('cart.views',
    url(r'^$',  'show_cart', { 'template_name': 'cart/cart.html'}, 'show_cart'),
    url(r'^add_to_cart/$', cart.add_to_cart, name='add_to_cart'),
    url(r'^empty_cart/$', cart.empty_cart, name='empty_cart'),
    url(r'^remove_item/$', cart.remove_from_cart, name='remove_item'),
                       )