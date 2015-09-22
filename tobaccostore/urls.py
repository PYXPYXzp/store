# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from order import views

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', include('products.urls', namespace="products")),
    url(r'^order/', include('order.urls', namespace='order')),
    url(r'^cart/', include('cart1.urls', namespace='cart'))
    ]
