from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^tobacco/$', views.tobacco_company, name = 'tobacco_views'),
    url(r'^tobacco/(?P<comp_id>[0-9]+)/$', views.flower_list, name = 'flowers'),
    url(r'^shisha/$', views.shisha_company, name = 'shisha'),
    url(r'^shisha/(?P<comp_id>[0-9]+)/$', views.shisha_list, name = 'shisha'),
    url(r'^other/$', views.other_company, name = 'other'),
    url(r'^other/(?P<comp_id>[0-9]+)/$', views.other_list, name = 'other'),
]
