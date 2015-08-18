from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^tobacco/$', views.tobacco_all, name = 'tobacco_views'),
    #url(r'^tobacco/(?P<question_id>[0-9]+)/$', views.company_all, name = 'company_views'),
    url(r'^shisha/$', views.shisha_list, name = 'shisha'),
    url(r'^other/$', views.other_list, name = 'other'),
]
#