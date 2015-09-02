from django.conf.urls import url

from products import views
from order import views

urlpatterns = [
    url(r'^$', views.order_tobacco, name = 'order_tobak'),
]