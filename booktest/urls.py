from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(\d+)$', views.detail),
    url(r'^(?P<p2>\d+)/(?P<p3>\d+)/(?P<p1>\d+)/$', views.show)
]