from django.conf.urls import url

from products import views
from order import views

urlpatterns = [
    url(r'^$', views.order, name='order'),
    url(r'^add_info/$', views.add_info, name='add_info'),
]