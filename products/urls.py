from django.conf.urls import url

from products import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^tobacco/$', views.tobacco_company, name = 'tobacco_company'),
    url(r'^tobacco/(?P<comp_id>\d+)/(?P<models_flower>[\w\s]+)/$', views.detail_tobacco, name='detailtobacco'),
    url(r'^shisha/$', views.shisha_company, name = 'shisha_company'),
    url(r'^shisha/(?P<comp_id>\d+)/(?P<models_model>[\w\s]+)/$', views.detail_shisha, name='detailshisha'),
    url(r'^other/$', views.other_company, name = 'other_company'),
    url(r'^product/(?P<comp_id>[0-9]+)/$', views.list, name = 'list'),

]
