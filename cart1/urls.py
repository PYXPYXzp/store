from django.conf.urls import patterns, url
from cart1 import views

urlpatterns = [
    url(r'^add_cart/$', views.test_view, name='add_cart'),
]
