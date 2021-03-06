from django.conf.urls import url, patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from products import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^tobacco/$', views.tobacco_company, name = 'tobacco_company'),
    url(r'^tobacco/(?P<comp_id>\d+)/(?P<models_flower>[\w\s]+)/$', views.detail_tobacco, name='detailtobacco'),
    url(r'^shisha/$', views.shisha_company, name = 'shisha_company'),
    url(r'^shisha/(?P<comp_id>\d+)/(?P<models_model>[\w\s]+)/$', views.detail_shisha, name='detailshisha'),
    url(r'^other/$', views.other_company, name = 'other_company'),
    url(r'^other/(?P<comp_id>\d+)/(?P<type_product>[\w\s]+)/$', views.detail_other, name='detailother'),
    url(r'^product/(?P<comp_id>[0-9]+)/$', views.list, name = 'list'),

)