# -*- coding: utf-8 -*-
from django.conf.urls import include, url, patterns
from django.contrib import admin
from order import views
from django.conf import settings

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', include('products.urls', namespace="products")),
    url(r'^order/', include('order.urls', namespace='order')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    ]
urlpatterns += patterns('',
         (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
         'document_root': settings.MEDIA_ROOT}))
