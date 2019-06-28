from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(\d+)$', views.detail, name='detail'),
    url(r'^(?P<p2>\d+)/(?P<p3>\d+)/(?P<p1>\d+)/$', views.show),
    url(r'^getTest1$', views.getTest1),
    url(r'^getTest2$', views.getTest2),
    url(r'^getTest3$', views.getTest3)
]