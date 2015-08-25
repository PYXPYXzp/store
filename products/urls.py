from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^tobacco/$', views.tobacco_company, name = 'tobacco_company'),
    url(r'^tobacco/(?P<comp_id>\d+)/(?P<models_flower>\w+)/$', views.detailproduct, name='detail'),
    url(r'^shisha/$', views.shisha_company, name = 'shisha_company'),
    url(r'^other/$', views.other_company, name = 'other_company'),
    url(r'^product/(?P<comp_id>[0-9]+)/$', views.list, name = 'list'),

]
