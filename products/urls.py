from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^tobacco/$', views.tobaccolist),
    #url(r'^shisha/$', views.shisha_list),
    #url(r'^other/$', views.other_list),
]
