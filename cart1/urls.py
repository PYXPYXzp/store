from django.conf.urls import patterns, url
from cart1 import views

urlpatterns = [
    url(r'^add_cart/$', views.add_to_cart, name='add_cart'),
    #url(r'^cart/$', views.get_cart, name = 'cart_view')
]
