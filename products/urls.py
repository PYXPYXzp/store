from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^tobacco/$', views.tobaccolist, name = 'tobacco'),
    url(r'^tobacco/(?P<company_id>[0-9]+)/$', views.afzal_list, name = 'afzal'),
    url(r'^tobacco/(?P<company_id>[0-9]+)/$', views.alfakher_list, name = 'alfakher'),
    url(r'^tobacco/(?P<company_id>[0-9]+)/$', views.nakhla_list, name = 'nakhla'),
    url(r'^shisha/$', views.shisha_list, name = 'shisha'),
    url(r'^other/$', views.other_list, name = 'other'),
]
